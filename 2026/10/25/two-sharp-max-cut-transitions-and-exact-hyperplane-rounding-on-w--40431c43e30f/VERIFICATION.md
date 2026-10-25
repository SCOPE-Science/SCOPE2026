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

# Reproducibility and limitations

Run `python3 verify.py` using Python 3 with its standard library. The program uses exact rational brute-force cuts on 42 parameterized small graphs and separately computes weighted Fourier-eigenvalue bounds and explicit unit-vector SDP objectives for 156 finite cases each. It also checks 2,240 nondegenerate hyperplane outputs against the claimed two-cycle-defect/all-antipodal-cut property. The recorded output in `verification_output.txt` matches a replay from the embedded script.

The script uses floating-point trigonometry for spectral and rounding spot checks, with tolerances where appropriate, and enumerates only finitely many integer-cut instances. It does not establish the full statement for unbounded graph order or all real weights; the analytic proof does. It does not constitute independent mathematical validation.
