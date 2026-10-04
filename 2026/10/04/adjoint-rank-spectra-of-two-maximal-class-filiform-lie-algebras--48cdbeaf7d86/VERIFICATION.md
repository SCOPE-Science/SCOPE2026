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
The universal proof is symbolic and does not depend on enumeration.

For \(L_n(q)\), the proof partitions all elements according to whether the \(e_1\)-coefficient is nonzero, zero but noncentral, or central. The corresponding adjoint ranks are \(n-2\), \(1\), and \(0\).

For \(M_n(q)\), the proof partitions all elements by the first two coefficients and then by the first nonzero coefficient among \(e_3,\ldots,e_{n-2}\). The resulting adjoint ranks are exactly
\[
0,\quad 1,\quad 2,\quad n-3,\quad n-2,
\]
with the multiplicities stated in RESULT.md.

The packaged checker `artifacts/verify.py` reconstructs the bracket tables and checks Jacobi on all basis triples. It then enumerates every element and computes every adjoint rank by finite-field Gaussian elimination for
\[
(q,n)=(2,9),\quad(3,7),\quad(4,6).
\]
The \(q=4\) test uses the field \(\mathbf F_2[\alpha]/(\alpha^2+\alpha+1)\).

For each family and each case, the checker verifies the complete predicted rank distribution, sums the corresponding centralizer sizes, and checks the exact rational commutativity-degree formula. It also directly enumerates all ordered commuting pairs for both algebras at \((q,n)=(2,6)\).

The checker returns `VERIFY_OK`.

Finite enumeration is not used as evidence for the universal quantifiers beyond replaying the stated consequences in representative fields and dimensions.
