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

The infinite statement is proved symbolically in `RESULT.md`. The key witness for quasi-injectivity of \(F_k\) is a prime \(r\) not dividing \(ab\), which forces \(ar\) and \(br\) outside the set of perfect \(k\)-th powers. The failure of the composition is exact because every value of \(G_k\) is a perfect \(k\)-th power.

The standalone program `verify_qi_composition.py` provides bounded regression checks for \(2\le k\le8\). It verifies complete multiplicativity and injectivity of \(G_k\), constructs a separating prime witness for every tested pair \(a<b\le120\), and checks the constant composition on the first \(2000\) positive integers for each tested \(k\). It returned `VERIFY_OK`.

These finite checks are not used as evidence for an unbounded quantifier. No external certificate or unproved computational assumption is required by the proof.
