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

The mathematical proof in `RESULT.md` is unrestricted. The attached `verify.py` performs corroborating exact-integer checks.

It tests every integer pair
\[
2\le x\le y\le1200
\]
against the universal pair obstruction, totaling \(719400\) cases. It also enumerates every
\[
2\le n\le1{,}000{,}000
\]
using sieve factorization and exact arithmetic formulas for \(\sigma(n)\) and \(\varphi(n)\). Of these, \(288533\) have \(\Omega(n)\le2\); none has all three integer means.

The count of eligible indices in that finite range, including the trivial index \(1\), is \(67\). The sharpness examples are checked explicitly:
\[
(\varphi(418),\sigma(418))=(180,720),
\qquad
(\varphi(477),\sigma(477))=(312,702).
\]

Neither the pair enumeration nor the finite index census is an infinite proof. The symbolic primitive-Pythagorean contradiction and the exhaustive \(\Omega(n)\le2\) case split establish the theorem for all eligible inputs.
