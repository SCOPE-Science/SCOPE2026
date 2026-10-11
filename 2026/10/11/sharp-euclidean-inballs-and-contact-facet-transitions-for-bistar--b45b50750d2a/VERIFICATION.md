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

# Reproducibility and verification

The embedded `verify.py` is a standalone Python 3 script using only the standard library (`itertools`, `fractions`, and `math`). Running `python3 verify.py` enumerates every signed incidence-edge potential for 36 distinct bistar parameters, computes every centered squared polar norm exactly, counts every norm-maximizer, and calculates the exact rational rank of the contact-normal span. It compares those quantities with the theorem's closed forms. Example checked triples \((M,F,\dim W)\) are \((19/2,2,1)\) for \((a,b)=(2,2)\), \((149/10,14,7)\) for \((2,6)\), and \((521/18,156,13)\) for \((4,12)\).

The test is exhaustive for each listed small finite instance only. It cannot establish infinitely many cases; the general proof uses the exact quadratic norm formula and integer first differences, together with a direct proof of the contact-normal rank. The literature comparison is not a comprehensive bibliography, and no independent external audit is represented by this file.
