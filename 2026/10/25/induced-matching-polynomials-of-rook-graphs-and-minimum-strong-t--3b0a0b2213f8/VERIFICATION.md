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

# Reproducible verification

Run `python3 verify_rook_induced.py` and `python3 verify_strong_cover_subsets.py` using an ordinary Python 3 standard-library interpreter. The first independently builds each rook graph, counts every induced matching in ten small rectangles, and excludes smaller strong total covers in four instances by exhaustive enumeration at the immediate smaller cardinality. The second uses a distinct vertex-subset enumeration: for each unselected induced subgraph it counts compulsory internal edges and crossing-edge choices, independently checking all optimum-cover multiplicities in two-row graphs of width two through eight, plus one square graph instance.

Observed results: the first reports `VERIFY_OK exact_induced_polynomials 10 strong_cover_exhaustive [(2, 2, 3), (2, 3, 5), (2, 4, 6), (3, 3, 7)]`. The second reports `VERIFY_OK`, including two-row optimum counts 8, 45, 6, 30, 90, 210, and 420.

## Scope of verification
The universal coefficient formula, the two-row structural necessity, and the two exceptional classifications are proved mathematically in RESULT.md. The finite enumeration does not certify all orders. The supplied scripts are reproducible consistency checks, not independent audit or proof assistants. The motivating paper's general strong-total-cover/induced-matching identity is earlier literature and is separately rederived for completeness.
