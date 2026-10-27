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

# Reproducibility and verification

Run `python3 verify.py` using a standard Python 3 interpreter. The script has no third-party dependencies and reconstructs its computations from scratch.

The observed output on direct execution was:

```
degree 2: finite Apéry envelope matches independent Dijkstra, total cumulative cases 232
degree 3: finite Apéry envelope matches independent Dijkstra, total cumulative cases 464
degree 4: finite Apéry envelope matches independent Dijkstra, total cumulative cases 696
degree 5: finite Apéry envelope matches independent Dijkstra, total cumulative cases 928
VERIFIED: all 928 independent finite comparisons; no extrapolation
```

One exact method computes shortest paths on the residue graph using all generators no larger than a rigorously justified Apéry upper bound; the other computes the binomial-index coin minimum using unbounded-change dynamic programming, then minimizes across the exact residue classes. The two routes agree on all coprime pairs \(2\le a\le50\), \(b\in\{1,2,3,5,7,11\}\), and degrees \(d=2,3,4,5\). Exact software checks do not establish the infinite bound or certify novelty; the complete symbolic proof of the result, including the quantitative coin-function lemma, appears in `RESULT.md`. Independent audit has not been performed.
