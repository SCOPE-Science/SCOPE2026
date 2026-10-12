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

The algebraic proof in `RESULT.md` is valid for every integer \(m\ge2\); the local toric ring is given by an explicit monomial map and complete-intersection equations. `check.py` can be run with `python check.py` using SymPy. An actual execution, included in `check_output.txt`, independently enumerated all extreme rays of the dual cone for \(k=1,2,3\), obtaining counts \(6,12,22\) and torsion-free local class ranks \(2,6,14\). Gröbner bases were verified for \(k=1,\ldots,5\). The rays were generated and tested using exact rational linear algebra, not floating-point heuristics.

The finite computations do not establish primeness, normality, ray classification, or the class-group formula for all parameters. These follow from the general mathematical proof. An independent audit has not been performed.
