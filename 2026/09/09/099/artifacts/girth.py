"""Lane 470: girth certificate. S={a,A,b,B,w,W}, w=abAB, W=baBA.
Check all reduced products of 3 and 4 generators != e (=> no triangles, no 4-cycles
through ANY vertex by vertex-transitivity), plus exhibit 5-cycle => girth exactly 5.
"""
import itertools
INV = {'a':'A','A':'a','b':'B','B':'b'}
def red(w):
    out=[]
    for ch in w:
        if out and out[-1]==INV[ch]: out.pop()
        else: out.append(ch)
    return ''.join(out)
def invw(w): return ''.join(INV[c] for c in reversed(w))
W = red('abAB'); Wi = invw(W)
S = ['a','A','b','B',W,Wi]
assert len(set(S))==6 and all(red(s)==s for s in S)

bad3=[p for p in itertools.product(S,repeat=3) if red(''.join(p))=='']
bad4=[p for p in itertools.product(S,repeat=4) if red(''.join(p))=='']
print("len-3 products = e:", len(bad3))
print("len-4 products = e:", len(bad4))
# exclude trivial backtracking? For Cayley girth, closed walks of len 3/4 at e:
# any closed walk s1..sk=e. Trivial backtracks (si+1 = si^-1) exist but simple cycles?
# Girth = shortest SIMPLE cycle. Closed walk len 3 non-backtracking?
def is_backtrack(p):
    for i in range(len(p)-1):
        if invw(p[i+1])==p[i]: return True
    return False
nb3=[p for p in bad3 if not is_backtrack(p)]
print("non-backtracking closed len-3 walks:", len(nb3), nb3[:10])
nb4=[p for p in bad4 if not is_backtrack(p)]
print("non-backtracking closed len-4 walks:", len(nb4))
for p in nb4[:12]: print("   ", p, [red(''.join(p[:k])) for k in range(5)])
# 5-cycle witness
cyc=['','a','ab','abA','abAB']
d=[red(invw(cyc[k])+cyc[(k+1)%5]) for k in range(5)]
print("5-cycle steps in S:", [x in S for x in d], d)
print("GIRTH = 5" if (len(nb3)==0 and len(nb4)==0) else "GIRTH < 5 !!")
# w infinite order (nontrivial reduced word in free group)
print("w nontrivial:", W!='', "W nontrivial:", Wi!='')
