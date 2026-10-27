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

# Reproducibility checks

The complete pure-Python verifier and its full 256-row exact census are in `verify.py` and `classification.csv`. Run `python3 verify.py` from any directory, provided the CSV remains beside the code. It reconstructs the two labeled binary de Bruijn relations from Wolfram rule bits, closes all generated Boolean relations in both packed-integer and row-tuple forms, and compares shortest cycles using algebraic powers versus a separate depth-first graph search for every reached relation. It verifies the four class counts, complete rule lists for multipliers three and four, all shortest-witness words and the sharp three-symbol bound, symmetry-orbit sizes, and the CSV. An independently formulated finite-ring evaluation checks every binary output word for all 256 rules and ring lengths one through seven (65,024 comparisons).

Expected output begins `VERIFY_OK: 256 rules; optimal multipliers 1/2/3/4 = 156/82/16/2;` and ends with `65024 independently checked cyclic image words for n<=7`.

The unrestricted theorem is derived from the finite-state path-lifting equivalence and full Boolean-relation closure. Bounded ring enumeration alone would not prove an infinite statement. The closure explores finitely many possible four-state relations, hence all arbitrarily long labels. Exact arithmetic avoids floating-point error. Scientific priority and applicability beyond the prescribed 256 local rules are not established by the checker. Independent external review has not been performed.
