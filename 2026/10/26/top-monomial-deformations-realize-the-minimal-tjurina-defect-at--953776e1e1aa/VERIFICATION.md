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

The accompanying verifier uses SymPy to compute a lexicographic Gröbner basis of the Tjurina ideal for the dimension-five example after eliminating the three quadratic variables. The leading-monomial staircase is bounded by \(x^5,y^6,z^6\) and has exactly \(124\) standard monomials. The principal weighted-homogeneous part has Milnor number \(5^3=125\), so the explicit defect is one. The general \(\mu\) and \(\tau\) formulas are proved in `RESULT.md` by the semiquasihomogeneous Milnor-algebra and weighted Euler-identity arguments.

The computation verifies only the finite example. It does not certify the Newton-spectrum theorem, semiquasihomogeneous invariance, Saito's criterion, or the general family; those are explicit mathematical inputs. No independent audit or external validation has been performed.
