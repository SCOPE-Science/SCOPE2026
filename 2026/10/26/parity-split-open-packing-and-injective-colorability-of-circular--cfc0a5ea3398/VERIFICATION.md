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

# Verification scope

The included standalone `verify_prism.py` uses only Python's standard library. Run it from the directory containing the program with `python3 verify_prism.py`. Its recorded exact output is `verification_output.txt`.

For \(n=3,\ldots,10\), it builds \(P_n=C_n\square K_2\) directly, constructs every open neighborhood, and checks all \(2^{2n}\) subsets under the original pairwise-disjoint-neighborhood condition, totaling 1,398,080 subsets. It compares every coefficient with the independent-set polynomial predicted by the structural theorem; it also independently builds the common-neighbor adjacency and checks its explicit isomorphism to the predicted cycle-square graph. It separately checks the common-neighbor adjacency criterion for \(n=11,\ldots,80\). It separately checks the common-neighbor adjacency criterion for \(n=11,\ldots,80\). An additional test checks explicit cyclic three- and four-color constructions and the exact cardinality partition criterion for \(n=3,\ldots,300\).

All the actual checks passed. These tests are finite consistency checks only; the universal theorem follows from the proof in `RESULT.md`. There is no claim of independent external validation or of exhaustive bibliographic priority verification.
