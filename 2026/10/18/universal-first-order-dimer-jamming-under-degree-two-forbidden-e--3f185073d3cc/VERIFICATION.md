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

Run `python3 verify.py` with Python 3 and no third-party dependencies. The script calculates exact failure probabilities from two-vertex-removal recursion over unoccupied subsets, for forbidden matchings, paths, and cycles at even sizes 6, 8, 10 and 12, together with a two-triangle boundary case. It separately exhausts the 362880 permutations of the nine available edges of \(K_6\setminus C_6\) and obtains 120960 jammed orders. These two independent routes agree at \(P_6=1/3\).

The computations do not establish the asymptotic law: the proof uses exact conditional ratios, uniform \(O(k^{-2})\) estimates, multi-vertex survival bounds, and a cutoff \(K\asymp N^{1/3}\). Finite coefficient values can deviate substantially from the limiting first-order approximation. Bibliographic comparisons have uninspected older full-text sources and cannot certify global novelty. Independent scientific audit remains unperformed.
