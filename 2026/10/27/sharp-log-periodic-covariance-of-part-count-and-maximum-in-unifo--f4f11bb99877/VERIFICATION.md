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

Execute `python3 verify.py` from the same directory, using the Python standard library only. The script compares the finite inclusion–exclusion probability and its first derivative at one half with direct word enumeration for every length and threshold through nine bits, and checks the exact four-bit covariance. A separate dynamic program on trailing-zero states computes correlations at lengths 100, 200 and 1000, agreeing to six decimal places with published table values. Expected terminal message: `VERIFY_OK 45 exact IE/derivative comparisons; 3 published correlations`. These checks do not prove an infinite asymptotic; that rests on the factorial and pivotal summability estimates in RESULT.md. The lattice limiting law has small phase fluctuations; numerical tables at finite lengths should not be extrapolated to infer the exact phase coefficient. Independent scientific validation has not been performed.
