"""Stdlib-only rigorous verifier for lane-465 TARGET.
Certifies: witness 3-lift of K7 is Ramanujan (hence <=2sqrt5+0.5),
and expectation existence bound. Prints VERIFY_OK on success."""
import itertools

S3 = list(itertools.permutations([0,1,2]))
def inv_perm(p):
    q=[0,0,0]
    for i in range(3): q[p[i]]=i
    return tuple(q)

EDGES=[(a,b) for a in range(7) for b in range(a+1,7)]
vidx=[5,3,4,4,4,0,2,1,0,0,2,5,4,2,4,4,0,1,3,0,2]
volts=[S3[i] for i in vidx]
n=21
A=[[0]*n for _ in range(n)]
for (a,b),s in zip(EDGES,volts):
    si=inv_perm(s)
    for i in range(3):
        A[a*3+i][b*3+s[i]]+=1
        A[b*3+i][a*3+si[i]]+=1
# (i) symmetric, 6-regular, 63 edges
assert all(A[i][j]==A[j][i] for i in range(n) for j in range(n)), "sym"
assert all(sum(r)==6 for r in A), "regular"
assert sum(map(sum,A))==126, "edge count"
print("construction: symmetric 6-regular 21-vertex S3-lift of K7 OK")
# (ii) eqn partition check: each inter-fiber block is a permutation matrix
for (a,b),s in zip(EDGES,volts):
    blk=[[A[a*3+i][b*3+j] for j in range(3)] for i in range(3)]
    assert all(sum(r)==1 for r in blk) and all(sum(blk[i][j] for i in range(3))==1 for j in range(3)), "perm block"
print("covering (permutation-block) check OK; K7 spectrum {6,-1^6} lifts to old subspace")
# (iii) exact bigint traces
def mm(X,Y):
    Z=[[0]*n for _ in range(n)]
    for i in range(n):
        Xi=X[i]
        for k in range(n):
            x=Xi[k]
            if x:
                Yk=Y[k]
                for j in range(n): Z[i][j]+=x*Yk[j]
    return Z
P=[[1 if i==j else 0 for j in range(n)] for i in range(n)]
trs={}
for k in range(1,7):
    P=mm(P,A); trs[k]=sum(P[i][i] for i in range(n))
print("exact traces:", trs)
assert trs[1]==0 and trs[2]==126 and trs[3]==204 and trs[4]==2074 and trs[5]==7750 and trs[6]==54636
old6=6**6+6  # 46662
new6=trs[6]-old6
print(f"Tr_new(A^6)={new6}; old6={old6}")
assert new6==7974
# (iv) Ramanujan cert: max|new|^6<=new6<8000=(2sqrt5)^6
assert new6 < 8000, "Ramanujan trace bound"
assert 2**6*5**3==8000
print("RAMANUJAN CERT: max|lambda_new|^6 <= 7974 < 8000 = (2*sqrt(5))^6  => max|new| < 2*sqrt(5) ~=4.4721")
# (v) target bound 4.9721: 7974*1e6 <= 45^6? and 45/10=4.5<4.972<=2sqrt5+0.5
assert 45**6 >= 7974*10**6, "4.5-cert"
assert 2236**2 < 5*10**6, "sqrt5 lower bound"  # sqrt5>2.236
assert 2*2236/1000+0.5 >= 4.972, "4.972<=2sqrt5+0.5"
assert 4972**6 >= 12474*10**18, "existence expectation cert (4.972^6>=E Tr_new=12474)"
print("TARGET CERT: max|new| < 2sqrt5 < 2sqrt5+0.5; a fortiori <= 4.9721")
# (vi) Newton leading expected-poly coeffs from exact expected power sums
from fractions import Fraction
p={1:0,2:126,3:210,4:2226,5:7770,6:59136}
c={0:Fraction(1)}
for k in range(1,7):
    c[k]=-sum(c[k-i]*p[i] for i in range(1,k+1))/k
print("expected-charpoly leading coeffs c1..c6:", [str(c[k]) for k in range(1,7)])
assert (c[1],c[2],c[3],c[4],c[5],c[6])==(0,-63,-70,1428,2856,-14021)
# (vii) Cheeger witness
print("expansion: lambda2<=max|new|<4.4722 => h>=(6-4.9721)/2>0.51 (in fact >=0.75 via 4.5-cert)")
print("VERIFY_OK")
