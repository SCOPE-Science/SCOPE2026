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

The universal proof is analytic. The accompanying `verify.py` replays three finite consistency checks from the packaged files:

1. After substituting \(\beta=1-\alpha(1+1/(3S))\), it verifies exactly that
\[
45S^2\left(g-\frac4{15}\right)
=\alpha\left(6S^2+2S-\alpha(3S^2-3S+2)\right).
\]
2. It verifies the exact rational arithmetic
\[
\frac{246}{875}-\frac4{15}=\frac{38}{2625},
\qquad
\frac2{38/2625}=\frac{2625}{19}.
\]
3. It verifies the endpoint reduction
\[
6S^2+2S-\frac32(3S^2-3S+2)=\frac{3S^2+13S-6}{2}.
\]

The checker does not enumerate all \(L\) or \(\varepsilon\), and its output is not used as a substitute for the inequalities in the proof. The conclusion is limited to the projection-diameter certificate described in `RESULT.md`.
