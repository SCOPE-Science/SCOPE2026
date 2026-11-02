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

# Verification notes

The theorem is proved symbolically for every complex triple satisfying \(abc(a^2-b)(b^2-ac)(ab-c)\ne0\). The geometric support is exhausted by the projective chart argument in `RESULT.md`. The local algebra of the first and last points is \(\mathbb C[z]/(z^3)\); the middle has quotient basis \(1,u,v,uv\), so is \(\mathbb C[u,v]/(u^2,v^2)\). In particular, the local lengths are \(3,4,3\). This is an algebraic proof with independently replayable finite checks, not an extrapolation from them.

The included `verify.py` generates Plücker coordinate vectors from the two parameterizations, checks the Grassmannian relation, and computes rational Gröbner bases for all three affine charts for the diagonal triples \((2,3,5)\), \((3,5,7)\), and \((2,7,11)\). Run `python3 verify.py` with Python 3 and SymPy. During preparation, all these checks completed, printing `VERIFY_OK`. The symbolic proof is necessary because computation at finitely many triples alone would not establish the stated open-parameter theorem.

The asserted lengths are scheme-theoretic intersection lengths **in the Grassmannian**. Two limiting tangent lines are included in the closed secant congruences although they are not proper common secants. Prior-literature coverage, especially potentially implicit classical specializations, remains a scientific priority risk. Independent audit has not been performed.
