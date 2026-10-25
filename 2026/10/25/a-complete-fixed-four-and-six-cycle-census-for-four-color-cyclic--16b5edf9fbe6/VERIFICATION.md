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

# Computational verification and limits

The standalone `verify.py` constructs the deterministic support map on **all** 225 ordered nonempty pairs of four-color masks, follows every directed orbit, and counts every periodic mask pair. It reconstructs the induced color permutations, confirms no collisions on periodic supports, computes each primitive labelled period and asserts exactly seven coefficient-table rows with total 25 periodic support pairs.

It then independently constructs the labelled synchronous update rule and exhaustively simulates all 115,600 initial configurations on the 16 labelled graphs with shore sizes \(1\le a,b\le4\). For every graph it computes cycle lengths without using the support-census formulas to drive the simulation and compares the recurrent population by period with the theorem.

Reproduction command: `python3 verify.py`. Recorded output: `verification_output.txt`. Successful terminal marker: `FOUR_COLOR_BICLIQUE_VERIFY_OK`.

The unbounded-family proof is the 225-state support reduction plus surjective assignment counting. The labelled graph enumeration is finite corroboration, not a proof for unbounded shore sizes. No independent audit has been performed.
