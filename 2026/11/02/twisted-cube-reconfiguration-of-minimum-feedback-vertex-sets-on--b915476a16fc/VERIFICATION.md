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

# Mathematical verification

The proof in `RESULT.md` establishes the entire infinite odd-prism family; the two standard-library Python programs are finite, independently structured checks of critical definitions and consequences.

1. Run `python3 verify_prism_direct.py`. It reconstructs each labeled prism from scratch, enumerates all sets of the proved optimal cardinality, and detects cycles with union-find. For \(n=5,7,9,11,13\), the verified counts of minimum sets are respectively \(20,56,144,352,832\); the square counts are \(0,42,252,1056,3744\). It checks every feasible exchange as an actual symmetric-difference-two pair, the prescribed support patterns, regular degrees, and connectedness. Successful completion prints `PRISM_DIRECT_EXHAUSTIVE_PASS`.
2. Run `python3 verify_prism_coordinates.py`. It builds only the independent coordinate graph and tests \(n=5,7,9,11,13,15,17\); the respective square counts are \(0,42,252,1056,3744,12000,35904\). It checks inverse transfer, connectedness, bipartition, regularity and the square formula. Successful completion prints `PRISM_SYMBOLIC_TRANSFER_PASS`.

The direct checker enumerates **all** candidate subsets of cardinality \(k+1\), not a sampling. The lower bound excludes smaller candidates. The symbolic checker does not assume the direct checker’s graph enumeration. Neither program proves novelty or substitutes for the infinite argument; the legal-move classification and square-count proof are given explicitly in `RESULT.md`. Independent scholarly validation has not occurred.
