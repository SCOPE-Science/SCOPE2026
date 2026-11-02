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

The packaged `verify.py` program uses only the Python standard library. Running `python verify.py` with Python 3.8 or later produced:

`VERIFY_OK low_profiles=120 parameter_sizes=40 exhaustive_m5=32768 errors_m5=1`

It checks the exact low-profile lists of original scores \(59,60,61\), the global lower bounds on surrogate scores for every original score \(\geq62\), and the maximum new score over the complete region of original score \(\leq58\). It verifies the one-exception tables, binomial orbit counts for the indicated sample of integer class sizes, and all labeled coalitions in the \(15\)-voter case.

The proof's four-profile obstruction, two all-size surrogate constructions, and class-permutation averaging argument are analytical. Finite checks are corroborative and do not certify every unbounded class size by themselves. No externally conducted independent audit is represented.
