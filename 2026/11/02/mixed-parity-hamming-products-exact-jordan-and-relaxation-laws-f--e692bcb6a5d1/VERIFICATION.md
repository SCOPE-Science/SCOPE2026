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

# Reproduction and verification

Run `python3 check_hamming.py` from the extracted bundle with Python 3 and no third-party dependencies. The program constructs the Cartesian-product adjacency matrix directly from Hamming distance, independently of the proof's tensor formula.

The exact matrix calculation tests 341 tuples with between one and four coordinate factors, each factor size 2 through 6 and total graph order at most 140. It checks `rank(A^2)=W`, `rank((A+I)^2)=Z`, `rank(A)=W+b0`, `rank(A+I)=Z+b1`, all multiplicity identities and `A^4=A^2` over GF(2).

For the finite-state checks, the verifier compares actual first-periodic-entry times and fixed-state populations against formulas for 17 cases, totalling 335,564 labelled initial configurations. Additions are XOR over GF(2) or GF(4); because the adjacency coefficients are in the prime field, this represents the same additive dynamics in a fixed polynomial basis. The enumerations are exhaustive **within the displayed finite cases only**.

Recorded output (also in `verification_output.txt`):

```
RANK_JORDAN_CASES_PASSED 341
EXHAUSTIVE_FINITE_STATE_CASES_PASSED 17 TOTAL_CONFIGURATIONS 335564
MIXED_HAMMING_JORDAN_ALL_CHECKS_PASSED
```

The all-size claim is proved algebraically in `RESULT.md`; these checks are not a substitute for an infinite proof. No external or independent audit was performed.
