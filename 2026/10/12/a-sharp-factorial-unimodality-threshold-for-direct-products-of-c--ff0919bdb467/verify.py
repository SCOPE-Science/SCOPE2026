"""Independent finite checks for a factorial unimodality threshold in categorical complete-graph products."""
from itertools import combinations
from math import comb, factorial


def C(n,k):
    return comb(n,k) if 0 <= k <= n else 0


def falling(n,k):
    z=1
    for i in range(k):z*=n-i
    return z


def coefficient(a,r,k):
    if k==0: return 1
    if k==1: return a*r
    if k==2: return C(a*r,2)
    return (a*C(r,k)+r*C(a,k)+falling(r,k)*C(a,k)
            +C(a,2)*C(r,2)*C(4,k))


def brute_coefficients(a,r):
    vertices=[(i,j) for i in range(a) for j in range(r)]
    n=len(vertices)
    # Distance 1 if both coordinates differ, distance 2 otherwise; valid for a,r >=3.
    dist=[[0 if i==j else (1 if (vertices[i][0]!=vertices[j][0] and
            vertices[i][1]!=vertices[j][1]) else 2) for j in range(n)] for i in range(n)]
    counts=[0]*(n+1)
    for k in range(n+1):
        for ids in combinations(range(n),k):
            good=True
            for x,y,z in combinations(ids,3):
                if (dist[x][y]+dist[y][z]==dist[x][z] or
                    dist[y][x]+dist[x][z]==dist[y][z] or
                    dist[x][z]+dist[z][y]==dist[x][y]):
                    good=False
                    break
            if good: counts[k]+=1
    return counts


def unimodal(coeffs):
    falling_seen=False
    for x,y in zip(coeffs,coeffs[1:]):
        if x>y: falling_seen=True
        elif y>x and falling_seen: return False
    return True


def theorem(a,r):
    assert a>=5 and r>=2*a+4
    return r >= 2*a+2+factorial(a+1)//a


def main():
    count=0
    examples=[(3,3),(3,4),(3,5),(4,3),(4,4),(5,3)]
    for a,r in examples:
        actual=brute_coefficients(a,r)
        predicted=[coefficient(a,r,k) for k in range(a*r+1)]
        assert actual==predicted,(a,r,actual,predicted)
        count+=2**(a*r)
    print('Direct geodesic enumeration: PASS, configurations:',count,'on '+str(len(examples))+' graphs')
    tested=0
    for a in range(5,9):
        for r in range(2*a+4, min(210,2*a+2+factorial(a+1)//a+10)+1):
            s=[coefficient(a,r,k) for k in range(r+1)]
            assert unimodal(s)==theorem(a,r),(a,r)
            assert all(s[k+1]>s[k] for k in range(2,a)),(a,r,'prefix')
            tested+=1
        R=2*a+2+factorial(a+1)//a
        for r in (R-2,R-1,R,R+1,R+2):
            if r<=210:continue
            s=[coefficient(a,r,k) for k in range(a+3)]
            assert (s[a+1]>=s[a])==theorem(a,r),(a,r,'threshold')
            assert s[a+2]>s[a+1]
            assert all(s[k+1]>s[k] for k in range(2,a))
            tested+=1
    print('Exact polynomial/threshold comparisons: PASS, parameter pairs:',tested)
    for a in range(5,12):
        R=2*a+2+factorial(a+1)//a
        assert coefficient(a,R-1,a)>coefficient(a,R-1,a+1)
        assert coefficient(a,R,a)<coefficient(a,R,a+1)
    print('Factorial threshold transitions: PASS for a=5..11')
    print('All checks passed. Finite tests are not an infinite proof.')

if __name__=='__main__': main()
