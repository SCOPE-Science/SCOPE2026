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
# Verification record

The analytic proof checks the quantifiers \(d\ge2\), \(p_i>0\), fixed \(p\), every \(n\ge2\), and the \(n-1\)-trial independent surrogate class. It shows both upper and lower asymptotic bounds, including surrogate sequences with shifted means, vanishing limiting variance, and arbitrary Bernoulli parameters.

Run `python3 check.py` in this folder. Its exact rational enumerations verify first and second moments for three categorical laws and three short lengths each; its independent dynamic program compares the observed Kolmogorov distance with the analytic limiting value for two nonuniform laws at lengths 80, 160, and 320, and checks the exact uniform law at length 12. The actual package checker returned `PASS 25 independent finite tests`.

These finite computations cannot establish a theorem about all lengths or all surrogate parameters; that work is done by the blocking central limit proof, Bernoulli variance envelope, Gaussian extremum and compactness/subsequence argument in RESULT.md. The accessible sources do not provide an independent novelty certification; the 1992 article was not available in full.
