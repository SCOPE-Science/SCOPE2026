"""Independent verifier (stdlib only): rebuilds Gram matrices by its own formulas,
replays LDL upper-bound certificate, re-evaluates M(c), checks admissibility.
Run: python3 verify.py"""
from fractions import Fraction
import json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
def C(n,r):
    if r<0 or r>n: return Fraction(0)
    return Fraction(math.factorial(n), math.factorial(r)*math.factorial(n-r))
def S31(a,b):
    return sum(C(b,j)*Fraction((-1)**j)/Fraction((a+j+31)*math.factorial(30)) for j in range(b+1))
def RM(tp,a,b):
    tot=Fraction(0)
    for l in range(a+1):
        c=C(a,l); e1=tp+a-l; e2=l+b+30
        tot += c*Fraction(math.factorial(b)*math.factorial(l+29), math.factorial(l+b+30)*math.factorial(29)) \
                  *Fraction(math.factorial(e1)*math.factorial(e2), math.factorial(e1+e2+1))
    return tot
N=8
A=[[Fraction(0)]*N for _ in range(N)]; B=[[Fraction(0)]*N for _ in range(N)]
for m in range(7):
    for n in range(7):
        A[m][n]=Fraction(1,m+n+32)
        J=(S31(0,0)-S31(m+1,0)-S31(n+1,0)+S31(m+n+2,0))/Fraction((m+1)*(n+1))
        B[m][n]=J*math.factorial(31)*32
    A[m][7]=A[7][m]=Fraction(1,32*(m+33))
    J1=(S31(0,2)-S31(m+1,2))/Fraction(2*(m+1))
    J2=(RM(1,0,1)-RM(1,m+1,1))/Fraction(m+1)
    B[m][7]=B[7][m]=(J1+31*J2)*math.factorial(31)
A[7][7]=Fraction(2,34*33*32)
B[7][7]=(S31(0,4)/4+31*RM(2,0,2))*math.factorial(31)
G=json.load(open(os.path.join(HERE,"gram_final.json")))
for i in range(N):
    for j in range(N):
        assert str(A[i][j])==G["A"][i][j],("A",i,j)
        assert str(B[i][j])==G["B"][i][j],("B",i,j)
print("Gram matrices: independent rebuild MATCHES")
d=json.load(open(os.path.join(HERE,"ratio_bound.json")))
c=[Fraction(x) for x in d["coeffs"]]
num=sum(B[i][j]*c[i]*c[j] for i in range(N) for j in range(N))
den=sum(A[i][j]*c[i]*c[j] for i in range(N) for j in range(N))
assert den>0 and num==Fraction(d["L_num"]) and den==Fraction(d["L_den"])
L=num/den; assert L==Fraction(d["L"])
print("L =",L,"=",float(L))
U=Fraction(d["U"])
M=[[U*A[i][j]-B[i][j] for j in range(N)] for i in range(N)]
Dp=[None]*N; Lm=[[Fraction(0)]*N for _ in range(N)]
for i in range(N): Lm[i][i]=Fraction(1)
for j in range(N):
    s=M[j][j]-sum(Lm[j][t]**2*Dp[t] for t in range(j))
    Dp[j]=s; assert s>0,("PSD fail",j)
    for i in range(j+1,N):
        Lm[i][j]=(M[i][j]-sum(Lm[i][t]*Lm[j][t]*Dp[t] for t in range(j)))/Dp[j]
assert [str(x) for x in Dp]==d["pivots"]
print("U =",U,"PSD pivots all >0 OK")
assert L>Fraction(3) and U<=Fraction(61,20)
t=json.load(open(os.path.join(HERE,"tuple.json"))); H=t["tuple"]
assert len(H)==32 and H==sorted(H) and len(set(H))==32
for p in [2,3,5,7,11,13,17,19,23,29,31]:
    occ={h%p for h in H}
    assert len(occ)<p,("admissibility fail",p)
    assert t["witness"][str(p)] not in occ
print("Admissibility p<=32 OK; diameter =",max(H)-min(H))
print("VERIFY_OK")
