# Constancy of H2 across square classes for L6,22(eps) and L6,24(eps)

## Context

The arbitrary-field classification of 6-dimensional nilpotent Lie algebras
(Cicalo-de Graaf-Schneider, arXiv:1011.0361) parametrizes the 2-step
families L6,22(eps) and L6,24(eps) by square classes eps in F/(F*)^2
(char != 2), using Gram-determinant / Arf-invariant orbit separation.
That classification uses H2 of smaller algebras as a tool but publishes
no function eps -> dim H2 of the resulting 6-dimensional algebras.
Over R there are only 2 square classes; over Q there are infinitely many,
so whether dim H2 is constant or jumps with eps decides extension and
degeneration distinctions that collapse over R.

## Definitions

Work over any field F (certificates below are determinants +-1).
Use the characteristic != 2 bracket lists of Cicalo et al., Section 3:

- L6,22(eps): [x1,x2]=x5, [x1,x3]=x6, [x2,x4]=eps*x6, [x3,x4]=x5
  (all other [xi,xj]=0, i<j);
- L6,24(eps): [x1,x2]=x3, [x1,x3]=x5, [x1,x4]=eps*x6,
  [x2,x3]=x6, [x2,x4]=x5.

H2(g,F) is ordinary trivial-coefficient Chevalley-Eilenberg cohomology,
C1 -> C2 -> C3 with dim C2=15, dim C3=20.
Let tij be the coordinate of theta in C2 on xi ^ xj.
The cocycle condition is
theta([xa,xb],xc)+theta([xb,xc],xa)+theta([xc,xa],xb)=0
on each triple a<b<c. A coboundary is d(xk*),
d(xk*)(xi,xj)=xk*([xi,xj]).

## Result

Theorem. For every eps in F (hence for every square class [eps]):

- dim H2(L6,22(eps)) = 8 (dim Z2=10, dim B2=2);
- dim H2(L6,24(eps)) = 5 (dim Z2=8, dim B2=3).

In particular f22([eps]) and f24([eps]) are constant; the jump locus
is empty. The two families are separated by H2 at every class (8 vs 5),
while H2 separates no members within either family.

Anchor values (all equal by the theorem):

| eps | dim H2(L6,22) | dim H2(L6,24) |
|-----|---------------|---------------|
| 0   | 8             | 5             |
| 1   | 8             | 5             |
| -1  | 8             | 5             |
| 2   | 8             | 5             |

Uniform cocycle bases:

- L6,22: free coordinates t12,t13,t14,t16,t23,t24,t34,t35,t36,t46 with
  t26=t35, t45=-eps*t16, t15=-t46, t25=eps*t36, t56=0 (10 vectors).
- L6,24: free coordinates t12,t13,t14,t15,t16,t23,t24,t26 with
  t25=t16, t34=t15-eps*t26, t35=t36=t45=t46=t56=0 (8 vectors).

## Proof / evidence

L6,22: the only nonzero cocycle rows are
(1,2,3): t26-t35=0; (1,2,4): -eps*t16-t45=0; (1,2,6): t56=0;
(1,3,4): -t15-t46=0; (1,3,5): -t56=0; (2,3,4): -t25+eps*t36=0;
(2,4,5): -eps*t56=0; (3,4,6): t56=0; all other triples give 0=0.
Rows {(1,2,6),(1,2,3),(1,2,4),(1,3,4),(2,3,4)} on columns
{t56,t26,t45,t15,t25} form diag(1,1,-1,-1,-1), det -1, independent
of eps, so rank(d2)>=5; the remaining nonzero rows are scalar multiples
(1,-1,+/-eps,0) of these, so rank(d2)=5 exactly, dim Z2=10.
Coboundaries: d(x5*) has t12=t34=1; d(x6*) has t13=1,t24=eps;
all others zero; the 2x2 minor on (t12,t13) is the identity, det 1,
so rank(d1)=2, dim B2=2. Hence dim H2=10-2=8 for every eps.

L6,24: the nonzero rows are
(1,2,3): -t16+t25=0; (1,2,4): -t15+eps*t26+t34=0; (1,2,5): t35=0;
(1,2,6): t36=0; (1,3,4): eps*t36-t45=0; (1,3,6): t56=0;
(1,4,5): -eps*t56=0; (2,3,4): t35-t46=0; (2,3,5): -t56=0;
(2,4,6): t56=0.
Rows {(1,2,5),(1,2,6),(1,3,6),(1,3,4),(2,3,4),(1,2,3),(1,2,4)} on columns
{t35,t36,t56,t45,t46,t16,t15} are lower-block-triangular with diagonal
(1,1,1,-1,-1,-1,-1), det +1 for every eps (the eps entry is strictly
below the diagonal), so rank(d2)>=7; the remaining rows are multiples
(+/-1,+/-eps) of the t56=0 row, so rank(d2)=7 exactly, dim Z2=8.
Coboundaries: d(x3*) has t12=1; d(x5*) has t13=t24=1;
d(x6*) has t14=eps,t23=1; others zero; the 3x3 minor on
(t12,t13,t23) is the identity, det 1, so rank(d1)=3, dim B2=3.
Hence dim H2=8-3=5 for every eps.

Explanation: eps enters at most two cocycle rows and one coboundary row,
always as an off-diagonal entry beneath an eps-independent unit pivot;
no rank-governing minor can vanish as eps varies, so the Gram/square-class
invariant is invisible to dim H2. All Jacobi identities hold for every
eps (verified symbolically: all eps-polynomial Jacobiator coefficients
vanish). Since every certificate determinant is +-1, the rank argument
holds over any field, including characteristic 2, for these bracket tables.

## Limitations

- Trivial-coefficient Chevalley-Eilenberg H2 only; no claim about adjoint
  coefficients or other cohomology theories.
- Holds over any field for the stated bracket tables; the
  characteristic-2 exceptional families L6,7(2), L6,8(2) are not covered.
- Isomorphism classification of the families (square-class indexing) is
  cited from Cicalo-de Graaf-Schneider, not reproved; only the H2
  dimensions are proved here.
- No claim about H2 ring structure, deformations, or degenerations
  beyond the dimension count and exhibited bases.

## Reproducibility

`artifacts/verify_h2.py` (stdlib only, exact Fraction arithmetic) builds
d1,d2 from the two committed bracket tables and checks: Jacobi at
eps in {0,1,-1,2}; anchor dimensions (Z2,B2,H2)=(10,2,8) and (8,3,5);
the +-1 minor determinants at every anchor; and that all d2 rows lie in
the span of the certificate rows. Result: ALL VERIFY_OK.
Run: python3 artifacts/verify_h2.py

## References

- S. Cicalo, W. A. de Graaf, C. Schneider, "Six-dimensional nilpotent Lie
  algebras," arXiv:1011.0361 (brackets, square-class parametrization,
  Gram/Arf orbit separation; motivation only).
- M. Degrijse, "On a filtration of the second cohomology of nilpotent Lie
  algebras," arXiv:1007.5150 (general bounds; not used for the exact law).
- V. J. del Barco, "On a spectral sequence for the cohomology of a
  nilpotent Lie algebra," arXiv:1204.4123 (real Betti data; contrast).
