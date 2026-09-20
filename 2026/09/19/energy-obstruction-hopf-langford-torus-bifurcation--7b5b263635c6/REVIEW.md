# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The central calculation is exact. Cylindrical reduction gives an autonomous two-dimensional amplitude flow and uniform angular rotation. With s=alpha-mu, T=mu-2 gamma s, R^2=s(mu/gamma-s), and w=r^gamma, direct differentiation gives

w''-T w' = gamma^2 R^2 w - gamma^2 w^(1+2/gamma).

The associated mechanical energy satisfies E'=T(w')^2. Therefore a nonconstant recurrent amplitude orbit is impossible when T is nonzero. Since the angular Poincare return map is exactly a fixed-time map of this amplitude flow, an invariant circle surrounding the periodic fixed point is excluded. At T=0 and gamma>0, R^2>0, the potential has a strict local minimum, giving a nonlinear center and a family of nearby closed amplitude curves. The symbolic artifact independently checks the algebraic identities and the Example-2 arithmetic.

The argument was stress-tested against the possibility that a three-dimensional torus need not be a product torus. Because theta advances uniformly and independently, a smooth torus surrounding the periodic circle intersects a theta-section in a compact invariant curve for the fixed-time amplitude map. Strict monotonicity of E under that map when T is nonzero contradicts invariance of such a curve.

## Originality — PASS, narrowly scoped

Cylindrical reduction of Hopf–Langford systems is established prior art. More importantly, Vassilev and Nikolov (Axioms 2025, Proposition 2) give a first-integral condition for a larger Hopf–Langford family. Under the parameter identification for the 2026 source system, their condition is exactly T=0. The earlier completely-integrable Hopf–Langford literature is therefore explicitly credited, and no priority claim is made for the critical integrability itself.

The accepted contribution is restricted to: (i) the exact off-critical monotone-energy identity E'=T(w')^2 for this source subfamily; (ii) the resulting obstruction to the specific Neimark–Sacker torus asserted in arXiv:2609.18010v1; (iii) the exact center-versus-focus classification across T=0; and (iv) the diagnosis of the source paper's printed Example 2. Searches by the source paper identifier, title, Hopf–Langford integrability terminology, torus bifurcation, first integrals, and equivalent Lienard/Duffing formulations did not reveal a prior source-specific correction.

The full text of Nikolov–Vassilev, *Completely integrable dynamical systems of Hopf–Langford type* (CNSNS 92, 105464, 2021; DOI 10.1016/j.cnsns.2020.105464) was not fully inspected; its abstract states equivalence to a force-free Duffing oscillator and complete integrability in special cases. It could contain an equivalent form of the energy transformation, so broad novelty of that transformation is not claimed. This residual risk does not remove the source-specific 2026 contradiction, because the corrected preprint postdates that literature.

## Value — PASS

The source paper's main theorem asserts a unique unstable invariant torus born through a Neimark–Sacker bifurcation. The exact amplitude structure instead forces the unit-modulus surface to be a first-integrable center and prohibits any one-sided surrounding torus branch. This changes the qualitative interpretation of the main result, yields an exact critical surface independent of the angular frequency beta, and also shows that the paper's showcased torus example violates its own gamma0>0 assumption and has saddle transverse linearization for the printed parameters.

## Limitations

The conclusion concerns the exact rotationally symmetric system written in arXiv:2609.18010v1. Generalized Hopf–Langford systems with extra terms can support genuine torus bifurcations. The record does not identify the precise symbolic line in the averaging derivation responsible for the discrepancy, and it does not claim that every prior numerical torus result for broader Langford models is invalid.
