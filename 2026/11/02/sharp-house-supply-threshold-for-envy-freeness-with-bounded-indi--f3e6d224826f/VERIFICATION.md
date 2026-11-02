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

# Verification of the bounded-tier house-supply theorem

The all-parameter theorem is proved analytically in `RESULT.md`. Run the supplementary exact-rank verifier from the same directory:

```sh
python3 verify.py
```

Expected final line (CPython standard library only):

```
VERIFY_OK exhaustive_profiles=39329 boundary_profiles=4096 random_profiles=11000 sharpness_cases=25
```

The checker independently enumerates all injective allocations and compares them with Hall-deficiency peeling on \(6,561\) three-level two-agent profiles and \(32,768\) dichotomous three-agent profiles. It exhaustively checks \(4,096\) labeled binary profiles with three agents and four houses, of which \(78\) lack an envy-free assignment. It additionally runs \(11,000\) reproducible randomized guaranteed-size examples and \(25\) parametric sharpness instances (with direct assignment enumeration only for small cases).

**Finite tests do not establish the infinite theorem**. The Hall-neighbor equality, tier-incidence count, house-removal bound, and lower-bound obstruction are separate mathematical proof steps in `RESULT.md`; the checker tests examples of them. Neither prior-work priority nor independence has been certified by these computations.
