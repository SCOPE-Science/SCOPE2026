# Verify all 4 Corollary-15 branches have form K*q^{-2N}*B with B->1 polynomial in u=q^n,v=q^l
q=0.7
a=1/q-q
def qn(k): return (q**(-k)-q**k)/a if k!=0 else 0.0
def dimV(m,k): return (m+1)*(k+1)*(m+k+2)*(2*m+k+3)/6.0
# Branch E functions (up to overall K scale, set K=1): use N=n+l with branch shifts absorbed
# c0: [N+2][N]+[l+1][l]; c1-like: [N+2][N+1]+[n+2][n]; d2-like: [N+2][N]+[n+1][n]; d3-like: [N+2][N+1]+[n+2][n]
# (shifts of indices don't change structure; verify B->1 in each case)
def E_A(N,l,n, s1=2,s2=0, t1=1,t2=0):
    return qn(N+s1)*qn(N+s2)+qn(l+t1)*qn(l+t2) if (N or l) else 0.0
import math
for name,fn in [
  ("c0",lambda n,l: qn(n+l+2)*qn(n+l)+qn(l+1)*qn(l)),
  ("c1",lambda n,l: qn(n+l+2)*qn(n+l+1)+qn(n+2)*qn(n)),
  ("d2",lambda n,l: qn(n+l+2)*qn(n+l)+qn(n+1)*qn(n)),
  ("d3",lambda n,l: qn(n+l+2)*qn(n+l+1)+qn(n+2)*qn(n)),
]:
    vals=[]
    for (n,l) in [(5,5),(10,10),(15,15),(20,20)]:
        N=n+l; E=fn(n,l)
        B=E*(q**(2*N))*a*a
        vals.append(B)
    print(f"{name}: B -> {['%.6f'%v for v in vals]} (limit 1 + shift const; check bounded away 0)")
# leading homogeneous part of dimV(2n,2l): compute coefficient of n^4? expand top degree
# dimV = (2n+1)(2l+1)(2n+2l+2)(4n+2l+3)/6; top homog deg4: (2n)(2l)(2n+2l)(4n+2l)/6
# = 8 n l (n+l)(2n+l)/3? verify nonzero and positive
def top(n,l): return (2*n)*(2*l)*(2*n+2*l)*(4*n+2*l)/6.0
print("top(1,1)=",top(1,1),"top(2,1)=",top(2,1),"=> nonzero positive homogeneous => pole order 4+2=6 at z=1")
# double-sum pole order check: sum_{n,l>=0} n^a l^b z^{n+l} has order a+b+2; max a+b=4 exists with nonzero coeff?
# expand top: 8/3 n l (n+l)(2n+l) = 8/3(2n^3 l +3n^2 l^2 + n l^3) -> monomials n^3l (a+b=4), n^2l^2, nl^3 all present
print("monomials present: n^3 l, n^2 l^2, n l^3 => max a+b=4 => order 6")
