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

The proof is mathematical and all-dimensional. Exact rational verification is supplied by `verify.py` (standard Python library only) and covers \(3\le n\le22\) at nine representative ambient dimensions for each \(n\), totaling 2,070 layer/factor comparisons, and additional direct coordinate decompositions at \((n,m)=(3,11),(3,12),(4,19)\). Reproduce by running `python3 verify.py` after extracting this file next to the script. The checks test the moment parameters, all claimed contact equalities and strict inequalities, the factorization, and failure of the proposed ellipse below the threshold. Finite cases do not establish any statement for arbitrary untested parameters; the symbolic proof is in `RESULT.md`. A separate independent scientific audit has not been performed.
