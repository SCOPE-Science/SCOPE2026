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
# Reproducibility

Run `python3 verify.py` with Python 3.10+ and NumPy. The script and the corresponding `verification_output.txt` are included intact. The script independently evaluates the defining ambiguity using FFTs and the expanded quadratic Gauss sums; checks least singular margins/multiplicities on fourteen odd prime-power examples; exactly compares dyadic zero locations for \(N=2,4,\ldots,512\); and compares full lifted-map singular spectra at four small orders by direct matrix singular-value decomposition.

The proof is the algebraic argument in `RESULT.md`; these finite checks independently probe its critical boundary cases but cannot certify claims over infinitely many prime powers. No external or independent validation was performed. NumPy floating-point tolerances are stated in the script and do not decide symbolic zero conditions in the proof.
