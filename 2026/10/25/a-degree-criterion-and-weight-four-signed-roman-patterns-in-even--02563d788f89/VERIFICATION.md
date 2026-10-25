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

# Verification details

Run `python verify_kn_signed_roman.py` and `python check_criterion.py` from the directory containing the two scripts. Both require only Python's standard library.

The first script builds labelings exactly as defined in the theorem. For each even size from \(12\) through \(40\), it forms every Kneser vertex, explicitly enumerates its disjoint vertices, sums their assigned labels together with the vertex itself, checks the result is at least one, and independently verifies a disjoint label-\(2\) neighbor for every negative vertex. It also checks every vertex with the algebraic identity through even order \(128\) and evaluates the exact subfamily counting formula at orders \(12\) and \(14\).

The second script independently compares the proposed degree criterion with the original neighborhood and defender definition for all \(8{,}320\) internal-subgraph selections at orders \(6\) and \(8\), together with \(300\) seeded random selections at order \(12\). The small orders are used solely to test the structural criterion, which is algebraically valid beyond the theorem's size range.

Both checks finished with `PASS`; the raw terminal output is preserved in `verification_output.txt`. Finite checks cannot exclude a counterexample at an unchecked order or replace the all-orders proof in `RESULT.md`. The global minimum over all signed Roman functions was not computationally or theoretically determined.
