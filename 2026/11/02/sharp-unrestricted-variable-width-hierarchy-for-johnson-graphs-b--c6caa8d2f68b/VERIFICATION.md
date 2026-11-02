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

# Reproducible checks

Run `python verify_venn.py` and `python verify_logic.py` using Python 3 and its standard library. The output files `verify_venn.out` and `verify_logic.out` contain the exact recorded stdout for the corresponding programs. Both programs have been executed from the stated file paths and their outputs compared with the enclosed records.

`verify_venn.py` enumerates actual Johnson-graph pair extension supports at the rank-two and rank-three three-pebble cutoff. Independently, it enumerates ordered nonempty Venn profiles for three and four held subsets and the exact supports for adjoining a fourth or fifth subset. It confirms the sharp transitions at \(n=8\) for \((r,p)=(2,4)\), at \(n=12\) for \((r,p)=(3,4)\), and at \(n=15\) for \((r,p)=(3,5)\), and validates 60 constructive lower-bound configurations.

`verify_logic.py` performs an independent noncounting color refinement of pairs in small Johnson graphs, using sets rather than multisets for successor-color supports. For ranks two and three it confirms the expected three-variable equivalence classes. This logical computation is only a cross-check; the main higher-width argument uses the Venn-cell game.

The checks are finite, not a general symbolic certification. The unrestricted-depth theorem is justified by the proof in `RESULT.md`, including the indefinitely maintainable invariant and exact distinguishing sentences. No external independent audit has been performed.
