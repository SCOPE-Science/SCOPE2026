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

# Verification details

`verify.py` uses only Python 3 standard library `fractions.Fraction` and exact Gaussian elimination. It constructs the six stationary moment equations directly from the diffusion-switch generator and independently obtains a signed area rate from those moments. It compares this result to the simplified theorem formula on 250 parameter combinations with different temperature, anisotropy, cross-coupling signs and switching rates, as well as exact canonical rational and denominator identities. At creation, `python verify.py` returned `PASS: 267 exact rational assertions; canonical optimum 0.7879601723110169`.

The code's finite rational checks and numerical root approximation do not independently prove the uniform theorem, stationary ergodicity, or uniqueness of the optimal rate. Those are established analytically in `RESULT.md` by coercive stiffness, the moment identities, a positive-denominator polynomial, and Descartes' sign rule. No external independent audit was performed.
