#!/usr/bin/env python3
"""Presburger counterexample queries for majority on the three-row rook graph.

Execute with a Z3 command-line executable (z3 -smt2 <file>) or with a
system-installed libz3 dynamic library (standard ctypes interface).
The generated files require no Python SMT package. No finite-size cutoff
is used: the parameter k is unbounded in the integer theory.
"""
from pathlib import Path
import ctypes
import ctypes.util
import sys


def generate(parity, entry):
    if (parity, entry) not in ((1, 3), (0, 4)):
        raise ValueError('supported universal cases: odd/3 and even/4')
    n = f'(+ (* 2 k) {parity})'
    lines = ['(set-logic QF_LIA)', '(declare-const k Int)', '(assert (>= k 1))']
    for j in range(8):
        lines += [f'(declare-const p{j} Int)', f'(assert (>= p{j} 0))']
    lines.append(f'(assert (= (+ {" ".join(f"p{j}" for j in range(8))}) {n}))')
    for t in range(entry+3):
        for j in range(8):
            for i in range(3):
                b = f'b{t}_{j}_{i}'
                lines.append(f'(declare-const {b} Int)')
                lines.append(f'(assert (and (<= 0 {b}) (<= {b} 1)))')
                if t == 0:
                    lines.append(f'(assert (= {b} {(j >> i) & 1}))')
                else:
                    rs = '(+ ' + ' '.join(f'(ite (= b{t-1}_{q}_{i} 1) p{q} 0)' for q in range(8)) + ')'
                    vertical = '(+ ' + ' '.join(f'b{t-1}_{j}_{h}' for h in range(3) if h != i) + ')'
                    old = f'b{t-1}_{j}_{i}'
                    twice_count = f'(* 2 (+ {rs} {vertical} (- {old})))'
                    threshold = f'(+ {n} 1)'
                    successor = f'(ite (> {twice_count} {threshold}) 1 (ite (< {twice_count} {threshold}) 0 {old}))'
                    lines.append(f'(assert (= {b} {successor}))')
    violations = ' '.join(
        f'(and (> p{j} 0) (not (= b{entry}_{j}_{i} b{entry+2}_{j}_{i})))'
        for j in range(8) for i in range(3))
    lines.append(f'(assert (or {violations}))')
    lines.append('(check-sat)')
    return '\n'.join(lines) + '\n'


def check_with_library(script):
    name = ctypes.util.find_library('z3') or 'libz3.so.4'
    lib = ctypes.CDLL(name)
    lib.Z3_mk_config.restype = ctypes.c_void_p
    lib.Z3_mk_context.argtypes = [ctypes.c_void_p]
    lib.Z3_mk_context.restype = ctypes.c_void_p
    lib.Z3_eval_smtlib2_string.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
    lib.Z3_eval_smtlib2_string.restype = ctypes.c_char_p
    lib.Z3_del_context.argtypes = [ctypes.c_void_p]
    lib.Z3_del_config.argtypes = [ctypes.c_void_p]
    config = lib.Z3_mk_config()
    context = lib.Z3_mk_context(config)
    try:
        raw = lib.Z3_eval_smtlib2_string(context, script.encode('utf-8'))
        answer = raw.decode('utf-8') if raw else ''
    finally:
        lib.Z3_del_context(context)
        lib.Z3_del_config(config)
    return answer.strip()


def main():
    out = Path(sys.argv[1]) if len(sys.argv)>1 else Path('.')
    out.mkdir(parents=True, exist_ok=True)
    for label,parity,entry in (('odd',1,3),('even',0,4)):
        script=generate(parity,entry)
        file=out/f'{label}_counterexample.smt2'
        file.write_text(script,encoding='utf-8')
        result=check_with_library(script)
        print(f'{label}: {result}; bytes={file.stat().st_size}')
        if result!='unsat':
            raise AssertionError(f'Universal identity NOT proved: {label}: {result}')
    print('UNBOUNDED_PRESBURGER_OK')

if __name__=='__main__':
    main()
