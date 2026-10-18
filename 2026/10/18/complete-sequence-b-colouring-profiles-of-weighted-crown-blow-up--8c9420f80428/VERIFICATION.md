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

# Reproducibility and scope
Run `python3 verification.py` from the same directory. It generates the actual weighted crown blow-up graph on each tested parameter tuple, exhaustively assigns named palettes of each length from two through \(r+1\), rejects improper assignments, computes closed-neighbourhood colour sets, and records the number and exact sorted CDV counts for each valid \(b\)-colouring. It does not assume the theorem's classification when computing those counts.

Observed: `PASS 10 graph profiles; every named assignment for palette sizes 2 through r+1 checked`. Inputs comprise both unweighted and genuinely unequal block-size vectors at \(r=3\) and \(r=4\). The runtime of this check is finite; the proof in RESULT.md applies to all positive integer block sizes and arbitrary \(r\ge3\).

For each graph and admissible colour count, the comparison checks the complete set of sorted CDV-count vectors and the number of named \(b\)-colourings, including proving zero valid colourings at intermediate colour counts in the tested cases. It does not compute independent validation or establish novelty.
