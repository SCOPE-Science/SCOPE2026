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
The universal proof is algebraic. For each Bernoulli variable the modal mass is written as \(u=(1+r)^{-1}\) with \(r\in[0,1]\). The two possible modal orientations give normalized convolution maxima \(\max\{1,r+s\}\) and \(1+rs\), respectively. Each is at most both \(1+r\) and \(1+s\), which yields the claimed inequality directly.

The accompanying `verify.py` independently evaluates the original Bernoulli probabilities with exact rational arithmetic on \(10201\) grid pairs and checks the sharp fair-pair ratio. A successful replay prints `VERIFY_OK ratio=1/2 grid_pairs=10201`. This finite check is supplemental and is not used to establish the universal quantifiers.

The equality analysis in the proof shows that, apart from the zero-deficit fully deterministic case, equality requires both Bernoulli variables to be fair. No claim is made for three or more summands.
