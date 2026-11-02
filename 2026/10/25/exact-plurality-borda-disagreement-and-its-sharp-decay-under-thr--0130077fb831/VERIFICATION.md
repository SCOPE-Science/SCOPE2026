---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The four ranking types have plurality (a,b+c,d) and Borda (2a+b,n+b+c,c+2d). A unique Borda extreme winner forces the same plurality winner. A unique Borda middle winner opposite A-plurality is equivalent to a>max(b+c,d) and a<d+b+2c; reflection doubles the weighted multinomial cone. At t*=log(2)/2, tilting the a-b-c walk produces centered span-one increments with variance 2sqrt(2)/(1+2sqrt(2)); remaining inequalities have strict tilted slack. Their errors decay exponentially, and a lattice local limit plus bounded weighted summation supplies the explicit 1/sqrt(n) constant. Independent enumeration over all 4^n ballots for n=1..7 agrees, including 24/256 at n=4. Finite checks are not the asymptotic proof.

## originality

PASS

Best-of-knowledge specific comparison finds no demonstrated prior theorem covering this exact final claim; sourced close comparisons and residual priority risks are explicit, and unsuccessful search is not treated as proof of priority.

## value

PASS

Strict single-winner disagreement probability is a natural social-choice performance statistic, and an exact finite probability together with the sharp exponential rate and lattice prefactor refines qualitative convergence results. Excluding ties is explicit and mathematical, not an unnoticed normalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
