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
# Reproducibility and evidence limits

Execute `python3 rowmotion_direct.py` and `python3 rowmotion_toggles.py` in a directory containing these files, and compare stdout byte for byte with `direct_output.txt` and `toggle_output.txt` respectively. The direct program enumerates all ideals as \((A,B)\) pairs and implements generation from minimal elements of the complement. It verifies \(3\le n\le11\). The independent program treats the poset as lower-set masks and composes the individual toggles from maximal elements to minimal elements; it verifies \(3\le n\le8\). Both assert cycle histograms and rank-mean histograms; distinct code paths guard against a shared representation error.

The files are complete executable sources and exact recorded standard outputs. They are supplementary verification, not exhaustive mathematical proof of an infinite assertion. The all-\(n\) proof is the explicit orbit partition in `RESULT.md`. A finite test cannot justify the universal claim by itself. No independent external audit, peer review, or exhaustive priority certification has occurred.
