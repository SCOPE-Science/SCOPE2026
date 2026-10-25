"""Reproducible finite checks for a two-fibre dependence disjunction.
Standard library only. Execute: python3 checker.py
"""
from itertools import product
from math import comb

def direct_split(team):
    n=len(team)
    for bits in range(1<<n):
        red=[team[i] for i in range(n) if (bits>>i)&1]
        blue=[team[i] for i in range(n) if not ((bits>>i)&1)]
        if (all(s[0]!=t[0] or s[1]==t[1] for s in red for t in red)
            and all(s[1]!=t[1] or s[2]==t[2] for s in blue for t in blue)):
            return True
    return False

def normal_form_sat(rows,b):
    # A red fibre for x has at most one y-value; the rest must fit
    # a single z-value at each y on the blue fibre.
    for f0 in range(-1,b):
        for f1 in range(-1,b):
            z_by_y={}
            good=True
            for x,y,z in rows:
                if (x==0 and y==f0) or (x==1 and y==f1):
                    continue
                if y in z_by_y and z_by_y[y]!=z:
                    good=False
                    break
                z_by_y[y]=z
            if good:return True
    return False

def check(b,c,brute=False):
    V=list(product(range(2),range(b),range(c)))
    size=len(V)
    truths=bytearray(1<<size)
    tally={4:0,6:0}
    assertions=0
    for mask in range(1<<size):
        rows=[V[i] for i in range(size) if mask>>i&1]
        ok=normal_form_sat(rows,b)
        truths[mask]=ok
        if brute:
            assert ok==direct_split(rows),(b,c,mask)
            assertions+=1
        if ok:continue
        minimal=all(truths[mask^(1<<i)] for i in range(size) if mask>>i&1)
        if minimal:
            assert len(rows) in (4,6),(b,c,len(rows),rows)
            tally[len(rows)]+=1
            assertions+=1
    t=comb(c,2)
    want4=2*comb(b,2)*t*t
    want6=(4*comb(b,2)+44*comb(b,3))*t**3
    assert tally=={4:want4,6:want6},(b,c,tally,want4,want6)
    print('b',b,'c',c,'universe',size,'minimal_obstructions',tally,'OK')
    return assertions

def main():
    checks=0
    for b,c in [(2,2),(2,3),(3,2),(3,3),(4,2),(5,2),(2,4)]:
        checks+=check(b,c,brute=(b,c) in ((2,2),(2,3),(3,2)))
    print('ALL_CHECKS_OK',checks)

if __name__=='__main__':main()
