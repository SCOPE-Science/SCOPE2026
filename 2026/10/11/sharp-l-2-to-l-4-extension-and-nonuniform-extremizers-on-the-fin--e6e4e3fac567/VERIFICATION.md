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

# Reproduction and scientific limits

Run `python3 checker.py` using Python 3 with only its standard library. The script enumerates the complete two-sum fiber structure in each of the prime fields of cardinality \(5\), \(7\), \(11\), and \(13\). It then checks the exact integer convolution energy \(12q^2-3\) of the certified extremizer with squared mass \(2q+1\), and verifies the sharp rational inequality on random Gaussian-integer inputs using integer arithmetic. Passing this program corroborates finite cases only. The symbolic identity \(u^3+v^3=(u+v)^3-3(u+v)uv\), the exact exceptional-fiber convolution, and the weighted Cauchy--Schwarz argument in RESULT.md prove the result for every field of characteristic above three.

No claim of a computer-assisted exhaustive search for all complex amplitudes, or of independent assessment, is made.
