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
# Verification

The proof is symbolic and uniform. The critical identity is obtained by expanding two substitutions through the first degree at which they can differ:
\[
[f,g]=x+(r-s)a_rb_sx^{r+s-1}+O(x^{r+s}).
\]
The truncation boundary is then explicit. The top layer \(H_{n-1}\) always commutes with the whole group. The preceding layer contributes a potentially visible degree-\(n\) commutator only against a quadratic leading term, with coefficient proportional to \(n-3\). Every lower layer is separated by one of the probes \(x+x^2\) or \(x+x^3\).

The attached `verify.py` independently constructs the finite substitution law and exhaustively enumerates centers for multiple primes and truncation levels. It verifies all tested congruence and noncongruence branches and ends with `CHECK_OK`. These finite cases are regression checks, not a substitute for the universal proof.

Unproved limits: no assertion is made about coefficient fields larger than \(\mathbf F_p\), the full untruncated Nottingham group, automorphism groups, conjugacy-class counts, or higher terms of the upper central series.
