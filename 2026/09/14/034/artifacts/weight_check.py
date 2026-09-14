"""Weight/Euler certificate for lane-1919 Higgs fixed point.
E0 = L+O+L^{-1}, deg L=1, g=2, K deg 2.
End = 3O + 2L + 2L^{-1} + L^2 + L^{-2}; gauge weights 0,0,0,+1,+1,-1,-1,+2,-2.
Higgs field total weight 0. Target twists End x K shift gauge by +1 (deg K=2).
Per total-weight Euler chi = chi(End_w) - chi(End_{w-1} x K):
chi(F)=deg F + rk(F)(1-g).
"""
terms = [("O",0,0,3),( "L",1,1,2),("Lm1",-1,-1,2),("L2",2,2,1),("Lm2",-2,-2,1)]
g=2
def chi_tot(d_percopy,r): return r*(d_percopy+(1-g))
print("summand: name deg rk gauge-w chi")
tot=0
chis={}
for n,d,gw,r in terms:
    c=chi_tot(d,r); chis[gw]=chis.get(gw,0)+c; tot+=c
    print(n,d,r,gw,c)
print("chi(End) =",tot)
# twist: summand F tensor K has deg d+2r, gauge weight gw+1
from collections import defaultdict
e=defaultdict(int)
for n,d,gw,r in terms:
    e[gw]+=chi_tot(d,r)          # End part
    e[gw+1]-=chi_tot(d+2,r)    # minus End(w-1) tensor K part -> total weight gw+1... careful
# recompute directly per total weight w: chi(End_w) - chi((End tensor K)_w)
# (End tensor K)_w comes from End_{w-1} tensor K
twist_chi={}  # chi of End_{u} tensor K
for n,d,gw,r in terms:
    twist_chi[gw]=twist_chi.get(gw,0)+chi_tot(d+2,r)
print("twist chi per gauge u:",dict(twist_chi))
tot2=0
for w in range(-2,4):
    cw=e.get(w,0) if False else (chis.get(w,0)-twist_chi.get(w-1,0))
    tot2+=cw
    print(f"total weight {w}: chi = {cw}")
print("sum =",tot2, "(expect 1-20+1=-18)")
assert tot2==-18
for w in range(-2,4):
    assert chis.get(w,0)-twist_chi.get(w-1,0)==-3
print("OK: chi_w=-3 for w=-2..3")
# H^1 dims: H^0: w0 dim1; H^2: Serre-dual weights 1-w... H^2_1 dim1; rest in H^1
# chi = h0-h1+h2 per weight
h0={0:1}; h2={1:1}
for w in range(-2,4):
    h1=h0.get(w,0)+h2.get(w,0)-(-3)
    print(f"w={w}: h1={h1}")
print("H^1 dims sum:",3+3+4+4+3+3,"(expect 20)")
