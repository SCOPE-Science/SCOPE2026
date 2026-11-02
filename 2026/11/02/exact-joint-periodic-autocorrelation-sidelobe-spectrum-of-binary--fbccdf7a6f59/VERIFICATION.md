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

Run `python3 verify.py` from a directory containing the embedded script. Only Python 3 standard-library modules are needed. The expected final line is `VERIFY_OK`.

The checker has four exact stages: (1) enumerate all \(2^{16}\) four-bit Boolean feedback functions and accept a rooted cycle if its state-zero orbit visits exactly all 32 states; (2) independently enumerate cyclic words by extending `00000` without repeated five-bit windows and testing all four closing windows; (3) compare the two complete canonical-word sets; (4) calculate correlations independently by the sign-vector product and the cyclic XOR/Hamming identity and test the full matrix including absent cells.

The sorted rooted-word-set SHA-256 digest is `e8b5746482780303fec542789b123a2d51a892f460137bb9f8a96c85fec30421`. The feedback-state bijection is proved in `RESULT.md`; enumeration alone would not establish coverage absent that argument.

The exact finite result does not apply automatically to other orders or to aperiodic autocorrelation. The previously published low-sidelobe counts of 12 and 784 are treated as independent controls, not as the new result. Scientific originality cannot be certified by negative searches alone. External independent validation has not been performed.
