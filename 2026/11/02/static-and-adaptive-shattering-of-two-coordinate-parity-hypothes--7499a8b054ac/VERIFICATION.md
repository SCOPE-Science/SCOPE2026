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

# Reproduction

`verify.py` checks the three complete adaptive decision trees on five, seven, and nine variables (56 distinct leaf witnesses), the five explicit additive-basis sets, and all dimension-table numerical bounds. It evaluates every leaf directly against the parity function of its designated pair. Run with `python3 verify.py` from this directory.

`no_nine_basis.cpp` performs complete enumeration of the 7,888,725 nine-element candidate subsets of the binary five-space after fixing one point to zero by translation. It recomputes every pairwise XOR and rejects every candidate lacking complete nonzero coverage. Compile with any C++17 compiler; one tested invocation was `g++ -O3 -std=c++17 no_nine_basis.cpp -o no_nine_basis && ./no_nine_basis`.

The exact output of both programs appears in `checks.txt`. The arithmetic upper bound and the additive-basis equivalence are mathematical arguments in RESULT.md, not empirical extrapolations. No all-order dimensions, independent scientific evaluation, or comprehensive historical-priority claim is established.
