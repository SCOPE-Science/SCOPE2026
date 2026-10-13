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

The classification in `RESULT.md` is proved for all integers \(n>2\) with \(\omega(n)\le2\), without a finite bound.

The attached standalone `verify.py` independently evaluates \(\varphi\), \(\sigma\), primality, and \(\omega\) for every integer
\[
3\le n\le1{,}000{,}000.
\]
Direct satisfaction of simultaneous primality is compared against the complete predicted prime-or-10 classification. It also records the direct solutions without any prime-support restriction.

The expected and verified solution list over this finite range is
\[
3,5,10,17,65537.
\]

This finite computation is corroborative. The prime-power divisor-sum lemma, distinct-binary-digit argument, modulus constraints, and final factorization establish the unrestricted theorem. There is no computational claim beyond the stated range.
