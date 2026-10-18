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

# Verification

For a finite simple graph, the ordinary total-domination condition requires every vertex, including selected vertices, to have a selected neighbor in its **open** neighborhood. The separately packaged `verify.py` constructs `M(K_{2,n})` directly using the incidence and line-adjacency rules and compares its exhaustive cardinality histogram with an integer expansion of the proposed polynomial. It checks cases \(n=3,4,5,6\), which have \(11,14,17,20\) vertices, and enumerates **1,198,080 candidate subsets** in total. The command is `python3 verify.py` from the directory containing this file and the verifier; no third-party Python packages are required.

The recorded result is in `verification_output.txt` and can be reproduced by running that script. In every tested case, all coefficients match. Minima and their counts are \((4,24)\), \((4,6)\), \((5,20)\), and \((6,50)\), respectively. The infinite-family statement does not rest on extrapolation: its proof is the exact singleton-row case split in `RESULT.md`. No independent assessment has been performed. The checks do not cover \(n=1,2\), nor do they establish bibliographic priority.
