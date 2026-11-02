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

Run `python3 verify.py` in the directory containing `enumerate.cpp`, `direct_census.cpp` and `PROFILES.tsv` (requires a C++17 compiler). The verifier compiles and reruns the exact 12-bounded Euler-trail enumeration, checks the 316 canonical profiles and all 18 grouped categories against the embedded certificate, evaluates the generating function coefficients through length 120 and compares them against the stated law. An independently written direct enumeration of all binary words through length 21 groups the actual contiguous three-mer counts and two endpoints, and agrees. On the packaged files, the exact output was:

`VERIFY_OK 316 bases, 18 groups, coefficients n=2..120, independent direct census n=4..21`

The all-length conclusion uses the mathematical reduction in `RESULT.md`; the finite checks do not alone establish the infinite statement. The accessible 2016 primary literature was compared by mathematical implication. The expanded 2017 article was not read in full, so the priority conclusion is qualified.
