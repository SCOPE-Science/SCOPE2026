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

# Reproducibility and limits

The proof in `RESULT.md` applies to all integer alphabet sizes \(q\ge2\) and all \(n\ge q+2\). Verification includes exact maximum-clique enumeration of the finite compatibility graphs for every \(q\in\{2,3,4,5\}\), \(q+2\le n\le2q+1\), and the immediate lower boundary \(n=q+1\); the clique checks agree in all 18 parameter pairs. The witness generator independently checks distinctness, lengths, and pairwise intersection bounds in 897 parameter pairs for \(q=2,\ldots,40\).

To reproduce with Python 3 and no third-party packages, run `python3 verify_small.py` and `python3 verify_witnesses.py`. Corresponding exact stdout transcripts are `verify_small_output.txt` and `verify_witnesses_output.txt`. The finite checks support the explicit instances, while the infinite claim is justified by the mathematical inequalities and constructions in `RESULT.md`. Publication priority has residual uncertainty; no independent mathematical audit has been performed.
