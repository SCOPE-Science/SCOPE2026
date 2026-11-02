"""Exact VC/Littlestone checks for Dyck paths with two missing peaks.

Run with Python 3.10+: python VERIFY.py
The adjacent certificates.json file contains explicit adaptive trees.
"""
from __future__ import annotations
import functools
import itertools
import json
import math
from pathlib import Path

VALUES = {3: (1, 0, 0), 4: (6, 2, 2), 5: (20, 3, 4),
          6: (50, 4, 5), 7: (105, 4, 6), 8: (196, 4, 7),
          9: (336, 4, 7), 10: (540, 4, 8), 11: (825, 4, 8)}


def dyck(n):
    result = []
    def step(s, u, d):
        if d == n:
            result.append(s)
            return
        if u < n:
            step(s+'U', u+1, d)
        if d < u:
            step(s+'D', u, d+1)
    step('', 0, 0)
    return result


def layer(n):
    return [s for s in dyck(n) if sum(s[i:i+2] == 'UD' for i in range(2*n-1)) == n-2]


def make_solver(paths):
    num = len(paths)
    cols = [sum(1<<i for i,p in enumerate(paths) if p[j]=='U')
            for j in range(len(paths[0]))]
    all_states = (1<<num)-1
    @functools.lru_cache(None)
    def feasible(state, depth):
        if depth == 0:
            return bool(state)
        if state.bit_count() < (1<<depth):
            return False
        for col in cols:
            one = state & col
            zero = state ^ one
            if min(one.bit_count(), zero.bit_count()) < (1<<(depth-1)):
                continue
            if feasible(zero,depth-1) and feasible(one,depth-1):
                return True
        return False
    def tree(state, depth):
        if depth == 0:
            i = (state & -state).bit_length()-1
            return {'witness': paths[i]}
        for j,col in enumerate(cols):
            one = state & col
            zero = state ^ one
            if min(one.bit_count(), zero.bit_count()) >= (1<<(depth-1)) and feasible(zero,depth-1) and feasible(one,depth-1):
                return {'query_position': j+1, 'D': tree(zero,depth-1), 'U': tree(one,depth-1)}
        raise AssertionError('infeasible certificate request')
    return feasible, tree, all_states


def vc_exact(paths):
    n = len(paths[0])//2
    if len(paths)==1:
        return (0, ())
    for d in range(min(len(paths[0])-2,len(paths).bit_length()-1),0,-1):
        for comb in itertools.combinations(range(1,2*n-1),d):
            if len({tuple(p[i] for i in comb) for p in paths}) == (1<<d):
                return d,tuple(i+1 for i in comb)
    return (0,())


def verify_tree(tree, paths, depth):
    allowed = set(paths)
    all_witnesses=[]
    def walk(node, d, constraints):
        if d==0:
            assert set(node)=={'witness'}
            w=node['witness']
            assert w in allowed and all(w[i-1]==a for i,a in constraints)
            all_witnesses.append(w)
            return 0,1
        assert set(node)=={'query_position','D','U'}
        j=node['query_position']
        assert type(j)==int and 1 <= j <= len(paths[0])
        assert j not in [i for i,a in constraints]
        a,b=walk(node['D'],d-1,constraints+[(j,'D')])
        c,e=walk(node['U'],d-1,constraints+[(j,'U')])
        return 1+a+c,b+e
    nodes,leaves=walk(tree,depth,[])
    assert len(set(all_witnesses))==leaves==1<<depth
    assert nodes==(1<<depth)-1
    return nodes,leaves


def check():
    cert=json.loads(Path(__file__).with_name('certificates.json').read_text(encoding='utf-8'))
    assert sorted(map(int,cert))==[8,9,10,11]
    for n,(count,VC,LD) in VALUES.items():
        paths=layer(n)
        assert len(paths)==count==n*(n-1)**2*(n-2)//12
        assert len(set(paths))==len(paths)
        for p in paths:
            assert len(p)==2*n and p.count('U')==p.count('D')==n
            assert min(sum(1 if c=='U' else -1 for c in p[:i]) for i in range(2*n+1))==0
            assert sum(p[i:i+2]=='UD' for i in range(2*n-1))==n-2
        possible,build,whole=make_solver(paths)
        assert possible(whole,LD)
        assert not possible(whole,LD+1)
        if n<=6:
            got_vc,support=vc_exact(paths)
            assert got_vc==VC
            print('VC_EXHAUSTIVE',n,got_vc,support)
        if n>=6:
            sample_positions=(2,4,7,8)
            # The first twelve positions embed the six-size witness.
            assert len({tuple(p[i-1] for i in sample_positions) for p in paths})==16
        if n in (8,9,10,11):
            c=cert[str(n)]
            assert c['depth']==LD
            nodes,leaves=verify_tree(c['tree'], paths, LD)
            print('TREE_CERTIFICATE',n,LD,nodes,leaves)
        print('EXACT',n,'concepts',count,'VC',VC,'Ldim',LD,'cardinality_bound',count.bit_length()-1)
    # Independent, literal-family implementation of the online recurrence.
    for n in (3,4,5,6):
        paths=frozenset(layer(n))
        @functools.lru_cache(None)
        def literal(S):
            if len(S)<2:return 0
            return max([1+min(literal(frozenset(p for p in S if p[j]=='D')),
                              literal(frozenset(p for p in S if p[j]=='U')))
                        for j in range(2*n)
                        if any(p[j]=='D' for p in S) and any(p[j]=='U' for p in S)] or [0])
        assert literal(paths)==VALUES[n][2]
    print('INDEPENDENT_LITERAL_RECURSION_PASS')
    print('TWO_DEFECT_DYCK_ALL_CHECKS_PASS')

if __name__ == '__main__':
    check()
