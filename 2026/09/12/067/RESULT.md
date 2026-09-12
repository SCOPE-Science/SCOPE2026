# Mutation-invariant cubed structure and spectral rigidity of cubic-del-Pezzo Vianna potentials

## Context

Let X3 be the monotone cubic del Pezzo surface, CP^2 blown up at six general
points. Monotone Vianna-type Lagrangian tori in X3 are studied through their
disk (Landau-Ginzburg) potentials. The admitted target asked for a torus L3
whose potential has two nondegenerate critical points with distinct nonzero
values in distinct quantum-cohomology summands, a pearl-complex Floer
dichotomy at two explicit rank-one local systems, and a second torus with a
different critical-value multiset. While scouting that target via exact
critical-scheme computations, the cubed structure below was discovered.

## Definitions

- Seed (Pascaleff-Tonkonog Table 1, Galkin-Usnich): W0(x,y) = (1+x+y)^3/(xy) - 6.
- Cluster wall-crossing map (Def 4.1): mu_v(x,y) = (x(1+t)^{-v1}, y(1+t)^{-v2}),
  t = x^{v2} y^{-v1}; mutated potential W' = W o mu_v.
- Mutants examined: W1 = mu_{(1,0)}(W0), W2 = mu_{(0,1)}(W1),
  W3 = mu_{(0,-1)}(W2) as a formal recovery pullback with common factors cancelled.
- A point is Morse/nondegenerate if the gradient vanishes and the Hessian
  determinant is nonzero; the critical value is the potential value there.

## Result

For the cubic seed W0 and its three successive wall-crossing mutants
W1, W2, W3, each potential has the cubed form W+6 = S^3/M for explicit
polynomial S and denominator M:

- W0+6 = S0^3/(xy), S0 = 1+x+y;
- W1+6 = S1^3/(xy^2(y+1)^2), S1 = xy+(y+1)^2;
- W2+6 = S2^3/(xy^2(x+1)^2(x+y+1)^2),
  S2 = x^2y+x^2+3xy+2x+y^2+2y+1;
- cancelled W3+6 = S3^3/(x^3y^2(x+y)^2), S3 = x^2y+x^2+2xy+y^2.

Consequently each potential admits exactly one admissible nondegenerate
critical point, of value 21 (the simple eigenvalue of quantum multiplication
by c1(X3)): (1,1) with Hessian determinant 243; (2,1) with 243/4;
(2,3) with 27/4; (2,2) with 243/16. All remaining critical points lie on the
positive-dimensional curve {S=0} of value -6 on which the Hessian determinant
vanishes identically (verified at (1,-2), (1,-3/2+/-sqrt(5)/2),
(1,-3+/-sqrt(5)), (2,-4+/-2sqrt(3))). Hence the unordered critical-value set
is constantly {21,-6} across all four potentials, so no such torus supplies
two nondegenerate distinct-nonzero-value critical points and critical values
cannot separate these tori from one another.

## Proof / evidence

All identities are exact rational-function identities. Since
dW = S^2(3M dS - S dM)/M^2, every point of {S=0} away from poles is
automatically critical and Hessian entries carry an overall factor of S, hence
vanish there; only transverse-factor zeros can be isolated. Gradient
numerators factor as S^2 times transverse factors in each case (listed in the
draft). Exhaustiveness: W0 and W1 follow from linear/transverse solves; W2
from an exhaustive factor-pair solve (only (2,3) admissible, all other
combinations on S2=0 or poles); cancelled W3 from Groebner/resultant solves
(V&(x-y) gives only the pole (0,0) and (2,2); V&U2 gives only (0,0)).
Pullback by mu_v sends S^3/M to S(mu_v)^3/M(mu_v) with extra (1+t) powers
absorbed into the denominator, explaining persistence. The pearl-dichotomy
mechanism itself works for W0 (rho_+=(1,1) critical value 21 vs
rho_-=(-1,-1) value -7 gradient (2,2) noncritical) but cannot rescue the
blocked spectral conjuncts. Reproduction script:
`output/artifacts/cubic_critical_loci.py` (sympy factorization,
differentiation, substitution), independently re-executed at audit.

## Limitations

Proved for the seed plus three explicit mutants with a general pullback
mechanism and a depth-3 recovery test; extension to arbitrary mutation depth
is a mechanism-backed expectation, not a fully formal induction tracking
LG-seed direction bookkeeping at every step. W3 is a formal pullback recovery
test (its denominator retains a non-monomial factor after cancellation) rather
than a certified torus potential with full seed bookkeeping. The obstruction
applies to the Vianna/Lagrangian-mutation class reached by wall-crossing from
the Table-1 seed; it does not rule out hypothetical monotone tori outside that
class. Floer consequences (Clifford vs exterior self-Floer, split-generation)
are cited from Pascaleff-Tonkonog/Sheridan, not reproved.

## Reproducibility

Run `python3 output/artifacts/cubic_critical_loci.py` with sympy installed.
It prints factored W+6 numerators/denominators, factored gradient numerators,
Morse checks at the four value-21 points, degenerate-curve samples, and pearl
samples. The audit additionally verified the W3 cancellation identity, the W2
exhaustive factor-pair solve, and W3 Groebner/resultant uniqueness.

## References

- J. Pascaleff, D. Tonkonog, The wall-crossing formula and Lagrangian
  mutations, arXiv:1711.03209 (Table 1 seeds; Defs 4.1-4.2; Thm 4.6, 4.8;
  Props 4.29-4.30; Sec 4.14 eigenvalues -6 and 21).
- R. Vianna, Infinitely many monotone Lagrangian tori in del Pezzo surfaces,
  arXiv:1602.03356 (Newton-polytope distinction; different invariant).
- N. Sheridan, HMS for Fano hypersurfaces (Fukaya summands; Conjecture B.2).
- Fukaya-Oh-Ohta-Ono (cubic-surface potential, Sec 24, as cited in PT).
