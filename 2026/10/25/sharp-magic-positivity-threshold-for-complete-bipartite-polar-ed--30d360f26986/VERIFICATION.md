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

# Verification of the exact sign classification

Run `python3 verify.py` with Python 3 and no additional packages. The code independently interpolates the ordinary Ehrhart polynomial from the exact number of graph potentials for \(1\le m\le20\), reconstructs the Bernoulli coefficient identity, checks all finite magic-coefficient signs, and directly enumerates small graph potentials to cross-check normalization. All rational comparisons use `fractions.Fraction`; no floating-point tolerance is involved.

The exhaustive finite parameter checks apply to \(1\le m\le19\), and the proof for \(m\ge20\) uses the exact Bernoulli value \(B_{20}=-174611/330\). The computation is not an independent audit and does not establish any unclaimed assertion about \(h^*\)-polynomial roots or other complete bipartite graph families.
