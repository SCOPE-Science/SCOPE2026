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

Run `python check_cycle_blowup.py` using Python 3. The script uses exact rational arithmetic and no third-party modules.

It builds the incidence Laplacian of the cyclic independent-fiber graph, grounds one vertex, performs Gauss--Jordan inversion, constructs all cut-projection columns as potential differences, and compares their absolute sums with the two asserted formulas. It independently checks projector symmetry and the defining incidence identity. Tested parameter pairs are \((4,1)\), \((4,2)\), \((4,3)\), \((5,2)\), \((5,3)\), \((6,2)\), \((7,2)\), \((8,2)\), and \((6,3)\), for 259 columns. The \(n=4\) cases are algebraic boundary checks outside the novel parameter domain.

Computations of finitely many graphs do not prove the result for all \(n,r\). The general proof is the tensor decomposition and explicit complete transfer-current classification in `RESULT.md`; it does not depend on those tests. No independent mathematical validation is recorded.
