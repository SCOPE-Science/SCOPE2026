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

The theorem is proved symbolically in `RESULT.md`; finite computation is corroborative.

The attached `verify.py` checks every ordered prime pair
\[
p<q<5000
\]
and every positive exponent pair with
\[
a+b\le5.
\]
It evaluates
\[
\sigma(p^a)\sigma(q^b)
\]
exactly and confirms that
\[
p^2q^2\nmid \sigma(p^a)\sigma(q^b)
\]
throughout this finite test region.

It separately verifies the sharpness witness
\[
96=2^5\cdot3,
\qquad
\gamma(96)^2=36,
\qquad
\sigma(96)=252.
\]

It also checks the three polynomial inequalities used in the universal proof over a representative prime range. These computations do not replace the proof's unbounded inequalities and complete exponent split.
