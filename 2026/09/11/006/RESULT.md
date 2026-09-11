# Degree constancy and isolation of the square-with-center family on the 4+1 section (mu in [1,2])

## Context

Finiteness of planar central configurations (CCs) is the Smale sixth-problem-adjacent
frontier (Albouy-Kaloshin, Moeckel, Hampton-Moeckel). Generic planar 5-body finiteness
is settled, but the symmetry-breaking boundary is not: along natural mass sections,
where must asymmetric families bifurcate, and where are symmetric families provably
isolated? The admitted target is explicitly disjunctive: compute the equivariant
Morse degree from certified Hessian indices at two endpoint masses and either (horn 1)
a degree jump forcing a symmetry-breaking branch, or (horn 2) constant degree with
certified nondegeneracy proving isolation. This result establishes horn 2.

## Definitions

- Masses `m1=m2=m3=m4=1`, `m5=mu>0`; positions `q1..q5` in `R^2`.
- CC equations with multiplier `c`: `U_i + c m_i q_i = 0`, `U = -sum_{i<j} m_i m_j/|q_i-q_j|`,
  `U_i = dU/dq_i`. Center of mass at origin, `I = sum m_i|q_i|^2 = 1`, modulo rotation.
- `Z2` section (half-turn+swap): `sigma:(q1,q2,q3,q4,q5)->(-q3,-q4,-q1,-q2,-q5)`,
  fixed locus `q3=-q1, q4=-q2, q5=0` (4-dim ambient; COM automatic).
- Square-with-center point (I=1, half-side `s=1/2`):
  `q1=(1/2,1/2), q2=(-1/2,1/2), q3=-q1, q4=-q2, q5=0`.
- Constrained Hessian `S(mu) = Hbar(mu) - c(mu) M(mu)` on COM-eliminated outer
  coordinates (`q5 = -(s1+..+s4)/mu`), with `nu = 1/mu`,
  `M = I_8 + nu J_adj` (all-ones 2x2-block matrix).
- Local Morse-degree contribution of a transverse nondegenerate point: `(-1)^index`.

## Result

On the section `m1=..=m4=1, m5=mu`:

1. The transverse Hessian at the square-with-center configuration has Morse index 0
   at `mu=1` and Morse index 0 at `mu=2` (local degree contribution `+1` at each).
2. It is certified nondegenerate, in fact positive definite, for every `mu in [1,2]`.
3. Hence the degree does not jump, and no symmetry-breaking bifurcation of planar
   asymmetric 5-body CCs emerges from the square-with-center family over `(1,2)`:
   the symmetric configurations of this family are provably isolated there.

Closed forms: even block eigenvalues `24` and `Eaa+Eab = 24+6s+24s/nu > 66.4`
(`s=sqrt2`); odd eigenvalues `p +/- sqrt(b^2+q^2)`, each doubled, with
`p = 8nu+18s nu+6+17s+6s/nu`, `b = 24s+6s/nu`, `q = 8nu+18s nu-2+16s`;
zero condition `Z := p^2-b^2-q^2 = 2(4nu+1)L(nu)/nu`,
`L(nu) = (25+38s)nu-84+36s` affine increasing with `L(1/2) >= 6.28 > 0`.
Transverse destabilisation threshold: unique root
`nu* = (84-36s)/(25+38s)`, i.e. `mu* = 1/nu* = (13+11s)/12 ~ 2.38`
(exact form; crossing itself not certified here). Only `[1,2]` is certified.

## Proof / evidence

Exact `Q(sqrt2)` derivation in `inputs/DRAFT.md`, verified by independent audit:

- Square+center is a CC for every `mu>0` (D4 symmetry: outer forces radial, `U5=0`);
  direct force assembly matches `c(mu) = 2(-(1+s/4)-s mu)` to `1e-15`.
- `T(d) = (|d|^2 I - 3dd')/|d|^5` blocks match direct assembly to `1e-15`.
- Elimination formula (DRAFT eq. 5) matches direct COM elimination entrywise
  (`8.9e-15`) and as quadratic forms (`3.4e-13` over 200 random vectors).
- Even/odd contractions match closed forms; cross-couplings `~1e-15`; the
  `2+4=6` basis is exactly `I`- and rotation-transverse and complete.
- `Z` factorisation verified symbolically (`Z - 2(4nu+1)L/nu = 0`).
- Full-space constrained Hessian (COM+`dI` tangent, rotation quotiented) has
  strictly positive quotient spectrum at `mu=1, 1.5, 2` (index 0).
- `output/artifacts/certify_isolation.py` (stdlib only, `Fraction` + rigorous
  `1.4142 < sqrt2 < 1.4143`) exits PASS in <1s, certifying uniform PD.
- Uniform transverse PD on compact `[1,2]` implies no transverse zero eigenvalue,
  so the implicit function theorem gives unique continuation mod rotation with
  no bifurcation point in `(1,2)`.

## Limitations

1. Isolation is local to the square-with-center family; disjoint asymmetric
   families elsewhere on the section, and non-square symmetric CCs, are not
   classified or excluded.
2. Only `mu in [1,2]` is certified; the family destabilises at `mu* ~ 2.38`.
3. The degree used is the local Morse contribution `(-1)^index`, not a global
   section degree.
4. The Albouy-Chenciner reduction is used in its COM-eliminated position-form
   fixed-point-section equivalent at a nondegenerate point; the mutual-distance
   polynomial ideal was not separately eliminated.

## Reproducibility

`python3 output/artifacts/certify_isolation.py` (stdlib only) exits PASS in <1s.

## References

- Meyer-Schmidt, Bifurcations of relative equilibria in the 4- and 5-body problem
  (DSS-19): square family; degeneracy only at `(13+11sqrt2)/12 ~ 2.38` with kite /
  trapezoid branches. Nearest prior; implies nondegeneracy on `[1,2]` but states
  no endpoint Morse indices (see audit).
- Hu-Long-Ou, arXiv 1903.10270: (1+n)-gon ERE monodromy (spectral) stability,
  not CC Hessian inertia.
- Oliveira, arXiv 1207.1305: infinitesimal-mass 1+4 coorbital counts; disjoint regime.
- Moeckel, Scholarpedia, Central configurations: centered polygons are CCs;
  generic finiteness; no section index table.
- Albouy-Kaloshin, Annals 176 (2012): generic planar 5-body finiteness.
- Lee-Santoprete: equal-mass 5-body counts (no section index).
