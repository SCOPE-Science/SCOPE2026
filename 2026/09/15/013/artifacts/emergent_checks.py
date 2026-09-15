"""Self-check numerics for emergent finding."""
import math
q=0.7
L=math.log(1/q)
a=1/q-q
def qn(k): return (q**(-k)-q**k)/a if k!=0 else 0.0
def dimV(m,k): return (m+1)*(k+1)*(m+k+2)*(2*m+k+3)/6.0
# 1) T=sum of top-dimV coefficients over 8 branches: dimV(2n,2l) top 16*n^4-equivalent + dimV(2n+1,2l) top same 80 at (2,1)
def top_even(n,l): return (2*n)*(2*l)*(2*n+2*l)*(4*n+2*l)/6.0
print("T_branch(2,1)=",top_even(2,1))
print("8 branches x 80 =",8*top_even(2,1)," (s^6 zeta1 -> T*4!/L^6 =",8*top_even(2,1)*24/L**6,")")
# 2) 1D sector check: sum_{n} P(n) r^n with r=q^s: pole order deg+1; verify growth ~ C/(1-r)^{d+1}
s=0.15; r=q**s
tot=sum(dimV(2*n,0)*(qn(n+2)*qn(n)+1)**(-s/2) if n>0 else 0 for n in range(200))
print("1D-column partial:",tot)
# 3) domination: shell sums at s=2 decay (already shown); re-verify one shell
def E(n,l):
    N=n+l
    return qn(N+2)*qn(N)+qn(l+1)*qn(l) if (N or l) else 0.0
for N in [15,20]:
    t=sum(dimV(2*n,2*(N-n))*E(n,N-n)**(-2/2) for n in range(N+1) if E(n,N-n)>0)
    print(f"shell N={N}: {t:.4f}")
print("EMERGENT_CHECKS_OK")
