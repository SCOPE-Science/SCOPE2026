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

The proof in `RESULT.md` is universal and does not depend on finite enumeration.

The attached `verify.py` independently factors every integer through
\[
1{,}000{,}000,
\]
computes \(\sigma(n)\) and \(\Omega(n)\), and tests
\[
\sigma(n)\mid n^2.
\]

It confirms that the only nontrivial hits with
\[
\Omega(n)\le3
\]
are
\[
6,\ 28.
\]
It also determines the least multiplicity among tested non-perfect hits and confirms that this value is
\[
4,
\]
first attained by
\[
364.
\]

These computations are consistency checks only. The infinite conclusion comes from the complete factorization-shape argument.
