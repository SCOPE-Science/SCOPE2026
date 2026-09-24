# Independent audit — flat-moduli stability for Loewner's torus inequality

**Review date (UTC):** 2026-09-24  
**Source path:** `2026/09/08/054`  
**Audited source tree:** `86c4428061508c3668a0a397ef14cfb351418f9b` at repository head `74d705e2e1502fee594b03ca7b21a29c4e077f24`  
**Review type:** separate AI independent audit.

## Claim audited

For every unit-area flat two-torus, with Loewner deficit `delta=2/sqrt(3)-sys^2` and hyperbolic quotient distance `d` to the hexagonal class in `SL(2,Z)\H`, the record claims `delta >= (1/2) min(d^2,1)`, with `delta=0` only at the hexagonal torus.

## Correctness — PASS

I reconstructed the proof independently on the standard fundamental domain `D={|x|<=1/2, x^2+y^2>=1}`. For the unit-covolume lattice `y^(-1/2)(Z+tau Z)`, `|m+n tau|^2 >= m^2-|mn|+n^2 >=1`, so `sys^2=1/y` and `delta(y)=2/sqrt(3)-1/y`. Projection to moduli is distance-nonincreasing, so it suffices to bound the nearer-corner distance to `tau_h^±=±1/2+i sqrt(3)/2`. At fixed `y` that distance is largest at `x=0` for `y>=1`, and on `|x|=sqrt(1-y^2)` for `sqrt(3)/2<=y<1`. Writing `t_max=cosh(d_max)-1=N/(2 y y_h)`, `cosh z>=1+z^2/2` gives `d_max^2<=2t_max`, while `sqrt(3)y delta=2y-sqrt(3)` and `sqrt(3)y t_max=N`.

For `1<=y<=8/5`, `N=1/4+(y-y_h)^2`; the difference reduces to `g(y)=2y-sqrt(3)-1/4-(y-y_h)^2`, with `g(1)=0` exactly and `g'(y)=2(1+y_h-y)>0`. For `y_h<=y<1`, putting `w=sqrt(1-y^2)` gives `N=2-w-sqrt(3)y`; the desired inequality is equivalent to `w >= (2+sqrt(3))(1-y)`, which after squaring reduces exactly to `y >= (3+2sqrt(3))/(4+2sqrt(3))=sqrt(3)/2`. On `[y_h,8/5]`, `t_max<=delta<=13/24<cosh(1)-1`, so `d_max<=1` and `delta>=d_max^2/2`. For `y>=8/5`, `delta>=1/2`, which dominates the capped right side. Finally `delta=0` forces the two hexagonal corners.

I independently sampled `delta(y)/min(d_max(y)^2,1)` on 199,999 points through `y=100`; the minimum was about `0.5127165` near `y=1`, consistent with but not used for the exact proof. I also inspected the committed verifier; its exact integer threshold checks match the derivation. No omitted boundary or sign case was found.

## Originality — PASS relative to checked literature

Searches included `Loewner torus inequality stability`, `systolic deficit flat torus moduli distance`, `Hermite constant stability hexagonal lattice`, and `quantitative Loewner inequality`, including 2026 results. Bangert–Katz, arXiv:math/0304494, §1 Theorems 1.1–1.2 gives sharp inequalities and equality characterization, not a deficit-to-moduli-distance estimate. Horowitz–Katz–Katz, arXiv:0803.0690, §1 eqs. (1.3)–(1.5) and §3 Lemma 3.2 gives a variance defect for conformal factors within the same conformal class; for flat metrics that defect does not measure displacement in flat moduli. Eyll, arXiv:2502.13715, treats L2 conformal-factor stability for the Möbius strip and Klein bottle, not this torus-moduli distance. Current 2026 systolic searches likewise did not reveal an equivalent or stronger flat-moduli estimate. This judgment is relative to checked literature.

## Scientific value — PASS

After subtracting classical Loewner optimality and rigidity, a genuine contribution remains: an explicit global stability modulus on the natural moduli space of flat unit-area tori. Small deficit quantitatively forces `O(sqrt(delta))` hyperbolic proximity to the hexagonal point until the global cap activates. This is a reusable continuum stability statement, not a finite table or numerical fit.

No repair was needed. The theorem is restricted to flat unit-area two-tori, and optimality of `1/2` is not claimed.

**Final disposition: PASSED.**
