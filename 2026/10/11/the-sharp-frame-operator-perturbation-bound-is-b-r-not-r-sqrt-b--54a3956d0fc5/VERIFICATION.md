---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

At the source Corollary 2 (preprint Corollary 6), the prescribed one-point H=R family W=H, v=1, Lambda=2I and Theta=sqrt(5)I satisfies A=B=4 and sum ||(Lambda*Lambda-Theta*Theta)f||=||f||, hence R=1<A. The printed min{B+R sqrt(B/A),R+sqrt(B)}=min{5,3}=3 while actual perturbed quadratic energy is 5||f||^2; numerical claim false. For arbitrary index sets the hypothesis makes the coefficient-operator difference series absolutely convergent on each vector, and its sum D=S_Theta-S_Lambda is bounded self-adjoint with ||D||<=R. Thus -RI<=D<=RI, so (A-R)I<=S_Theta<= (B+R)I, giving frame bounds with R<A. Scalar one-point systems Theta=sqrt(c+R)I and sqrt(c-R)I attain both endpoints for any c>R. All steps use the stated source summed action operator difference, not the different analysis-operator perturbation metric. Exact scalar witness recomputed independently.

## originality

PASS

Statement-level comparisons against direct primary mathematical texts found no implication of this full exact claim in the inspected sources; separate specific comparisons below, with documented residual priority risks rather than a negative-search novelty proof.

## value

PASS

Identifies a concrete false published universal quantitative bound in g-fusion-frame robustness, supplies an explicit admissible counterexample and the sharp replacement at both endpoints. This directly affects certified frame stability estimates and is more consequential than a minor algebraic reformulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
