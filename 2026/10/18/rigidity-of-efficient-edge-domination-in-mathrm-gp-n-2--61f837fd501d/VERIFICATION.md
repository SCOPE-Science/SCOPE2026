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

# Verification record

The primary result is proved analytically, for all integer orders \(n\ge5\), in `RESULT.md`. The following two independently coded reproducibility checks are also included.

`verify_exact_cover.py` generates all \(3n\) edges as pairs of vertex indices; for each edge it computes all five members of its closed edge neighborhood. Backtracking enumerates **every** exact cover of the edge set by these neighborhoods for each integer \(n\in[5,40]\). It tests the output against the five cyclic prescribed matchings (or emptiness) and checks that the five matchings partition all edges. `exact_cover_output.json` records the complete tested order/count profile; `status` must be `PASS`.

`verify_transfer.py` uses a separate direct model: triples of booleans indicate membership of the outer, spoke and inner edges at each index. A word of four triples has an arc to the shifted word on five triples precisely when the three local exact-cover equations at the central index all equal one. Exhaustive enumeration gives \(346\) active states, \(576\) transitions, \(342\) strongly connected components, and exactly one cyclic component: a simple directed five-cycle with exactly five internal arcs. A directed closed walk therefore exists exactly in lengths divisible by five, and the five distinct cyclic shifts exhaust it. The script also checks that these states match the explicit period-five edge selector word. This finite-state graph calculation is complete over all 4-tuples of the eight possible triples, not a truncated search.

Run `python3 verify_exact_cover.py` and `python3 verify_transfer.py` in the same directory as the programs. Compare each one-line JSON stdout, including its final newline, to `exact_cover_output.json` and `transfer_output.json`. Both recorded outputs were generated directly by these programs and returned `PASS`. Python 3.8 or newer, standard library only. These computational checks complement the detailed proof rather than replacing it.

The literature comparison inspected the 2016 original author-uploaded six-page text and 2021 original arXiv full HTML. A directly relevant 2018 paper's complete text remained unavailable despite lawful open-text searches; only the abstract was examined. All assertions of novelty are conditional on accessible literature, and no independent scientific audit has been performed.
