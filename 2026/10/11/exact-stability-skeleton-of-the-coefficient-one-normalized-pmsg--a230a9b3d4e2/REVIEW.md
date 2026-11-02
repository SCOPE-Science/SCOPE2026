# Independent mathematical audit

## correctness

PASS

All seven frozen source files were read and the Git tree reconstructed from their actual blob IDs as 019c30acfb81e33e1c4d8b0cd598c4939c9c9a55. Exact independent SymPy differentiation confirmed that V=(x²+(a/b)y²+(a/b-1)z²)/2 obeys Vdot=-a(x-y)²-a(1/b-1)y²-(a/b-1)z² for 0<b<1. Since a=109/20>1, this is negative definite with positive radially unbounded V, proving GAS/global forward completeness; b=1 remains semidefinite and LaSalle's largest invariant zero-derivative subset is only origin (x=y,z=0 forces zdot=x²). Solving equilibria with s=xy gives exactly the ± branch at s>0 and b=s+a/(a+s), uniquely increasing because db/ds=1-a/(a+s)²>0 for s>=0. Independent Jacobian determinant reconstruction gives q(λ)=λ³+(a+2)λ²+A2λ+A3 with A2=(a³+a²s+a²+2as²+as+s³)/(a(a+s)), A3=2s((a+s)²-a)/(a+s), all >0 for s>0. At a=109/20, (a+2)A2-A3=-(552000s³+6016800s²+394580s-228364701)/(43600(20s+109)); positive cubic derivative and opposite endpoint signs prove exactly one s_H>0. Cubic Routh-Hurwitz gives 3 stable eigenvalues below, pair imaginary with third -149/20 at equality, and 2 RHP eigenvalues beyond. Exact symbolic identity residuals were 0; computations check algebra and do not replace the unbounded-domain proof. The packaged verify.py and prior verification logs are not used as sole evidence.

## originality

PASS

Best-of-knowledge PASS, not historical-priority certification. Inspected exact 2022 published PMSG paper full PDF (source gives numerical b~5.2 only), earlier 2015 full original publisher HTML (feedback stabilization), Borah/Roy 2017 full FO treatment, Zhang/Liao/Mu 2017 full same nonsmooth coefficient family (global absorbing ellipsoids, not global equilibrium attraction), and foundational 2002 plus He/Han 2017 smooth-gap exact bifurcation work (epsilon=0 differs from target epsilon=1). Neither accessible theorem is shown to imply the combined sharp critical-origin global result and explicit coefficient-one stable-pair threshold. Crucial unresolved source Jing/Yu/Chen 2004 directly studies nonsmooth air-gap motor stability and Hopf and could already imply the local branch criterion: searched lawful OA/arXiv first and authorized institutional text route returned disconnected VPN. Its abstract and known scope are recorded positively, not dismissed as NOT_COVERING. A self-matching Resultary record is excluded from prior-art evidence. No failed-search novelty proof.

## value

PASS

The parameter slice a=5.45 is the precise numerical sweep used in the 2022 published uncontrolled PMSG system, not an arbitrary selected number. A sharp global theorem for the full unbounded physical state space including the nonhyperbolic endpoint b=1, exact existence/uniqueness of the born equilibrium pair, and an algebraic Routh-Hurwitz stability partition distinguish equilibrium spectral changes at b≈5.5859 from trajectory Lyapunov changes near b≈5.2. This resolves a natural mathematical control/interpretation gap and exposes the possibility of coexisting basins/attractors without claiming them. Although algebraically accessible once the model is chosen, global endpoint stability and exact spectral thresholds are motivated structural facts for the cited natural system; no paper-scale generalization is demanded.

The dated certificate retains the supplied scientific assessment, sources and limitations.
