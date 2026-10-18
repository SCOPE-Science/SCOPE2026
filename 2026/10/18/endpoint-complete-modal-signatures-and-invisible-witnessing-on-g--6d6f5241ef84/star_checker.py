"""Finite exact algebra check for constant-free Godel-modal star semantics.

This checks the symbolic consequences of a separately given structural proof;
it does not enumerate all formulas or certify historical novelty.
Run: python star_checker.py
"""
from fractions import Fraction

A, B = Fraction(1, 3), Fraction(2, 3)
leaf_values = {"0": Fraction(0), "t": A, "1": Fraction(1)}
leaf_reverse = {v: k for k, v in leaf_values.items()}
root_values = {"0": Fraction(0), "a": A, "b": B, "1": Fraction(1)}
root_reverse = {v: k for k, v in root_values.items()}

def connective(name, x, y):
    if name == "and":
        return min(x, y)
    if name == "or":
        return max(x, y)
    if name == "imp":
        return Fraction(1) if x <= y else y
    raise ValueError(name)

def binary_signature(name, left, right):
    return (leaf_reverse[connective(name, leaf_values[left[0]], leaf_values[right[0]])],
            root_reverse[connective(name, root_values[left[1]], root_values[right[1]])])

def unary_signature(name, state):
    if name == "box":
        return "1", {"0": "0", "t": "a", "1": "1"}[state[0]]
    if name == "dia":
        return "0", {"0": "0", "t": "b", "1": "1"}[state[0]]
    raise ValueError(name)

# Finite semantic closure is a certificate for unbounded formula depth.
states = {("0", "0"), ("t", "0")}
for _ in range(20):
    nxt = set(states)
    for s in states:
        nxt.add(unary_signature("box", s))
        nxt.add(unary_signature("dia", s))
        for t in states:
            for op in ("and", "or", "imp"):
                nxt.add(binary_signature(op, s, t))
    if nxt == states:
        break
    states = nxt
else:
    raise AssertionError("closure did not stabilize")
assert states == {(l, r) for l in leaf_values for r in root_values}

# Independent syntax-tree evaluation of the twelve explicit witnesses.
BOT = ("bot",)
P = ("p",)
def op(name, *children): return (name,) + children
Box = lambda x: op("box", x)
Dia = lambda x: op("dia", x)
And = lambda x,y: op("and", x,y)
Or = lambda x,y: op("or", x,y)
Imp = lambda x,y: op("imp", x,y)
representatives = {
    ("0","0"): BOT,
    ("0","a"): And(Box(P), Dia(P)),
    ("0","b"): Dia(P),
    ("0","1"): Imp(P, BOT),
    ("t","0"): P,
    ("t","a"): Or(P, And(Box(P), Dia(P))),
    ("t","b"): Or(P, Dia(P)),
    ("t","1"): Imp(Box(BOT), P),
    ("1","0"): Box(BOT),
    ("1","a"): Box(P),
    ("1","b"): Or(Box(BOT), Dia(P)),
    ("1","1"): Imp(BOT, BOT),
}
def interpret_ast(t):
    if t[0] == "bot": return ("0","0")
    if t[0] == "p": return ("t","0")
    if t[0] in ("box", "dia"):
        return unary_signature(t[0], interpret_ast(t[1]))
    return binary_signature(t[0], interpret_ast(t[1]), interpret_ast(t[2]))
for target, ast in representatives.items():
    assert interpret_ast(ast) == target, (target, interpret_ast(ast))

# A separate finite-set evaluator checks that changing intermediate leaf degrees
# while preserving both extrema leaves all representative values unchanged.
def direct(t, which, S):
    name = t[0]
    if name == "bot": return Fraction(0)
    if name == "p": return Fraction(0) if which == "root" else which
    if name in ("box", "dia"):
        if which != "root":
            return Fraction(1) if name == "box" else Fraction(0)
        vv = [direct(t[1], leaf, S) for leaf in S]
        return min(vv) if name == "box" else max(vv)
    return connective(name, direct(t[1], which, S), direct(t[2], which, S))
S1 = [A, (A+B)/2, B]
S2 = [A, (2*A+B)/3, (A+2*B)/3, B]
for target, ast in representatives.items():
    assert direct(ast, "root", S1) == direct(ast, "root", S2) == root_values[target[1]]
    for s in S1+S2:
        assert direct(ast, s, S1 if s in S1 else S2) == (s if target[0] == "t" else leaf_values[target[0]])
print("GODEL_STAR_ENDPOINT_AND_12_SIGNATURES_OK")
