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

# Reproduction and boundaries

Execute `python3 check_crown_ltd.py` in this folder using a standard Python 3 interpreter (no external dependencies). The attached `verification_output.txt` records the expected stdout. This verifier builds the labeled graph from the defining edge relation, tests total domination of every vertex via open neighborhoods, compares outside-vertex signatures, and enumerates every selected vertex subset for \(n=3,4,5,6,7,8,9\). It independently tests the structural characterization, all bivariate coefficients, the univariate polynomial, the minimum cardinality, the minimum count, and equality of the families of inclusion-minimal sets. In total 349504 subsets are checked, all passing. The proof in `RESULT.md` is universal and does not depend on this finite computation. No independent audit is claimed.
