---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
The packaged checker `artifacts/verify.py` reconstructs the algebra from
\[
[e_1,e_2,e_3]=e_1
\]
and its alternating extension.

It symbolically substitutes a general \(3\times3\) endomorphism into the \(3\)-Lie Nijenhuis identity and verifies that every defect coefficient is zero.

It independently checks the automorphism criterion
\[
Pe_1=\det(P)e_1
\]
and verifies all six normal forms satisfy
\[
E^2=I,\qquad E\ne\pm I.
\]

For each representative it checks the product-structure identity on all ordered basis triples. It also checks the abelian identity and distinguishes the strong and perfect identities, reproducing exactly two strong classes, two perfect classes, and two generic abelian classes.

Over \(\mathbf F_3\), the checker exhaustively enumerates all \(3^9\) matrices. It finds
\[
234
\]
product structures and a \(432\)-element automorphism group. The six product-structure orbits have sizes
\[
9,\quad9,\quad36,\quad36,\quad72,\quad72.
\]

Including the excluded scalar involutions gives
\[
236
\]
involutions in eight orbits.

Over \(\mathbf F_5\), orbit generation from the six normal forms gives
\[
25,\quad25,\quad150,\quad150,\quad600,\quad600,
\]
whose sum is
\[
1550.
\]

The checker returns `VERIFY_OK`.

The finite computations replay the theorem; they are not used as substitutes for the arbitrary-field argument.
