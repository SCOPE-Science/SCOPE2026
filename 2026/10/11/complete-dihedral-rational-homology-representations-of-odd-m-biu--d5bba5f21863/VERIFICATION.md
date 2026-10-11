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

# Reproducibility and scope

The mathematical proof is in RESULT.md. Independently run `python3 verify_dihedral.py` with an ordinary Python 3 standard-library installation. Successful output ends with `VERIFY_OK cases= 107 faces_total= 204100`.

The program enumerates perfect-matchable faces and dihedral permutations directly rather than using the induced-module calculation. For \(n=3,5,7,9\), it checks all group elements; for \(n=11\), it checks eleven stated rotation/reflection elements. It also independently checks the forbidden-pair-cycle intersections and the union decomposition; for \(n=3,5,7\) it computes exact mod-two reduced homology ranks of both the full complex and the central subcomplex by sparse boundary elimination. These checks are finite cross-checks, not an exhaustive proof for infinitely many \(n\); the uniform proof uses the relative-chain decomposition and cycle homology calculation.

Independent audit has not been performed; no external certificate is asserted.
