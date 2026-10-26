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

# Verification and limits

The profile lemma is proved symbolically for all integers \(n\ge3\): total domination in a crown graph is equivalent to selecting at least two vertices from each side. A deficit argument proves optimal partition rigidity for all \(n\ge5\). The exceptional cases \(n=3,4\) admit exact profile-multiset sums using the factorial weight formula in `RESULT.md`.

Run `python verify_coalitions.py` in a directory containing the script. It exhausts profile multisets with deficit at most four for \(3\le n\le9\), and it exhaustively generates unlabelled set partitions of the labelled graph vertices and checks the actual open neighborhoods for \(n=3,4,5\). No external libraries or data files are required. Observed outputs: optimum class numbers \(3,4,6,8,10,12,14\) and corresponding counts \(48,857,900,3600,11025,28224,63504\). The finite checks do not replace the infinite proof.

The scientific boundary is the exact crown family; the corresponding parameter on graph families with arbitrary deleted matchings is not claimed. Priority beyond inspected literature remains uncertain. No independent audit has been performed.
