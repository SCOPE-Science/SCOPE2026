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

The mathematical proof is exact and infinite. `verify.py` is a finite independent replay of the formulas, not a substitute for the proof.

It checks six exact rational parameters strictly inside \((-2,1)\) for every \(1\le n\le20000\), verifies that the zeros are exactly the primes, checks the endpoint witnesses \(P_{-2}(1)=0\) and \(P_1(18)=0\), and verifies the convolution identity \(\sigma_1^{(-1)}*\sigma_1=\varepsilon\) for \(1\le n\le500\).

Expected output:
`VERIFY_OK exact_params=6 n_max=20000 endpoint_witnesses=2 convolution_cases=500`

The unbounded claim rests on the case proof in `RESULT.md`; no inference from finite enumeration is used.
