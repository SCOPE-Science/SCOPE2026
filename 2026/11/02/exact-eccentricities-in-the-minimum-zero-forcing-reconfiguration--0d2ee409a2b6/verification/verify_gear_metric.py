"""Finite algebraic verifier for the infinite-cover distance and all-size metric."""
import json
from pathlib import Path
T='ABCDE'
D=json.loads(Path(__file__).with_name('cover_distance_table.json').read_text())
assert D['types']==list(T)

def f(s,t,j):
    if abs(j)<=5:return D['small'][s][t][j+5]
    if j>0:return 3*j//2+D['positive'][s][t][j%2]
    p=-j;return 3*p//2+D['negative'][s][t][p%2]

def neighbors(t,j):
    if t=='A':return [('B',j),('B',j-1),('C',j),('D',j-1)]
    if t=='B':return [('A',j),('A',j+1),('D',j),('E',j-1)]
    if t=='C':return [('A',j),('D',j),('D',j-1),('E',j)]
    if t=='D':return [('A',j+1),('B',j),('C',j),('C',j+1),('E',j),('E',j-1)]
    if t=='E':return [('B',j+1),('C',j),('D',j),('D',j+1)]

def metric(m,s,t,j):return min(f(s,t,j),f(s,t,j-m))
def ecc(m,s):return max(metric(m,s,t,j) for t in T for j in range(m))
def expected(m,s):
    r=(3*m+3)//4;d=(3*m+6)//4
    return d if s in 'AB' else r+1 if s in 'CE' and m%4==0 else r

def test():
    for s in T:
        for t in T:
            for j in range(-10,11):
                a=f(s,t,j);bs=[f(s,v,z) for v,z in neighbors(t,j)]
                assert a>=0 and all(abs(a-b)<=1 for b in bs)
                assert (a==0)==((t,j)==(s,0))
                assert a==0 or min(bs)==a-1
            for j in range(6,14):
                assert f(s,t,j+2)==f(s,t,j)+3
                assert f(s,t,-j-2)==f(s,t,-j)+3
            for sg in [-1,1]:
                a=[f(s,t,sg*j) for j in range(23)]
                assert max(a[:4])<=a[4] and all(a[k+1]>=a[k] for k in range(4,22))
    print('INFINITE_COVER_BELLMAN_PASS')
    # Each finite ring distance is the minimum of its cover-lift distances.
    # Distance is nondecreasing beyond layer 4, so the nearest two translates win.
    for m in range(4,28):
        for s in T:
            assert ecc(m,s)==expected(m,s),(m,s,ecc(m,s),expected(m,s))
            for t in T:
                for j in range(m):
                    best=min(f(s,t,j+q*m) for q in range(-3,4))
                    assert metric(m,s,t,j)==best
    print('RING_PROJECTION_AND_BASE_CASES_PASS m=4..27')
    # For m>=24, the possible extremal j lie in central band.
    # Under (m,j) -> (m+4,j+2), all distances there increase by 3.
    for m in range(24,28):
        j0=m//2
        for s in T:
            central=max(metric(m,s,t,j) for t in T for j in range(j0-5,j0+6))
            assert central==expected(m,s)
            left=max(f(s,t,j0-5) for t in T)
            right=max(f(s,t,j0+5-m) for t in T)
            assert left<=central and right<=central,(m,s,left,right,central)
            for t in T:
                for j in range(j0-5,j0+6):
                    assert f(s,t,j+2)==f(s,t,j)+3
                    assert f(s,t,j-m-2)==f(s,t,j-m)+3
            assert expected(m+4,s)==expected(m,s)+3
    print('ALL_SIZE_ECCENTRICITY_INDUCTION_PASS')

if __name__=='__main__':test()
