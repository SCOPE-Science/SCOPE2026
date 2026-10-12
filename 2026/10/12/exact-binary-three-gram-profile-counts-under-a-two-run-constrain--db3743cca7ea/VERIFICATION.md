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
# Reproducible finite corroboration

Run `python3 verify_profiles.py` in the same directory as this file. It uses the Python 3 standard library only and constructs profiles by three separate approaches: a directed-walk state-set recurrence through \(m=72\), direct integer flow-balance parametrization through \(m=40\), and literal enumeration of all admissible binary strings through \(n=17\). It compares all counts against coefficients of the claimed rational generating function, with no preloaded profile data.

The actual successful invocation printed:

`VERIFY_OK max_m 72 direct_strings_through_n 17 balance_through_m 40 first_16 [1, 6, 9, 12, 20, 28, 34, 44, 55, 66, 79, 92, 106, 124, 140, 156] at_m72 2971`

The verifier is a finite check only. Formal proof for all \(n\ge2\) is supplied by the Euler-trail characterization, exact shift classification, double geometric summation and exact rational-function identities in `RESULT.md`. The test does not establish unexamined empirical cases beyond its enumerated lengths, does not independently verify bibliographic priority, and does not constitute external certification.
