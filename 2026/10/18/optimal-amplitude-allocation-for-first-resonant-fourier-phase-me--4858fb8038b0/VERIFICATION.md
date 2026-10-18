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

Run `python3 verify_first_resonance.py` with Python 3 and its standard library only. The program checks multinomial collision multiplicities for all coprime \(0<A<B\le14\) at every integer order \(1\le r\le B\), four Gaussian-integer middle-coefficient phases at first resonance, and rational squared optimal amplitudes and their strict gap above equal coefficients.

Expected exact terminal output: `VERIFY_OK collision_cases=614 B_max=14 exact_first_response_and_allocation`.

This finite program does not certify infinitely many frequency pairs. The theorem for all integer frequencies follows from the elementary collision-vector classification and the strict weighted power-product optimization in RESULT.md. These checks are independent recomputations of finite instances, not an independent scientific audit. Two-probe inverse conditioning assumes known magnitudes and deterministic Euclidean measurement errors, with angle estimator explicitly specified.
