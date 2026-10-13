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

Run `python verify.py` under Python 3 from the directory containing this file. The standalone program relies only on the Python standard library. It constructs every antipodal Rademacher class through dimension four and every distinct induced signed-permutation action; compares the sorted quadratic-form value multisets; enumerates the entire finite class of signed-coordinate maps for the explicit four-dimensional pair; checks the integer costs and matrix row-sum bounds; and verifies the stated example at \(\varepsilon=1/16\) in exact rational arithmetic.

Analytic checks independently required and supplied in `RESULT.md` are: (i) the uncrossing proof of the unrestricted sorted-matching formula and uniform Rademacher lift, (ii) the faithful order-24 signed-permutation action on four antipodal classes in dimension three, (iii) Walsh-character orthogonality yielding the restricted variance expression, and (iv) Gershgorin or strict diagonal-dominance control giving positive definiteness across the entire open interval.

The program is an exhaustive finite certificate for the four-dimensional comparison, not a numerical claim about every dimension or all matrix families. No external independent audit or validation has been performed.
