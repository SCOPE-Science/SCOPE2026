---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Reconstructed equation (3.21) from the primary numerator, including normalization Q=s^(1-2n)P(s,s). For m=2n+1, parity gives L(2r)=L(2r+1)=r+1, kappa(2r)=n-1-r and kappa(2r+1)=2n-1-r. Summing yields endpoints n, a_j=(8n-4)j+2 for 1<=j<=n, center 8n^2+4n+1 and reciprocal degree 2(n+1). The centered circle polynomial is (8n-4)|sum_{j=0}^n exp(ij theta)|^2+5+4 sum_{j=1}^n cos(j theta)+2n cos((n+1)theta). With u=theta/2, v=(n+1)theta, H=(4n-2)/sin^2(u)-(2n-2)>=2n/sin^2(u), completion of the square gives T>=2n+1-(1-sin^2(u))/n>=2n+1-1/n>0. theta=0 is checked directly; theta=2pi/(n+1) gives T=2n+1. Nonzero endpoints and reciprocal pairing give exactly n+1 roots on each side of the unit circle, with multiplicity. An interior root s realizes product coordinates (s,s) by choosing both z coordinates sqrt(|s|) exp(i arg s), both w coordinates sqrt(|s|); both points lie in the domain since m/n>1. The denominator is nonzero. This is not the kernel diagonal z=w. Separately authored exact coefficient comparisons for n=1,...,500 corroborate, but do not replace, the uniform parity and inequality proof.

## originality

PASS

Best-of-knowledge originality of the exact normalized positivity and root-count claim. The claimed family m=2n+1 has unbounded gap k=n+1, whereas fixed gaps 1,2,3,4,5,6 and the n=1 integer family intersect it at finitely many parameters. The new uniform margin and nonzero diagonal root count are stronger than known existence of some kernel zero. Searches alone are not the novelty argument; the inspected primary statements and mathematical implication comparisons below are decisive within the documented scope.

## value

PASS

This is a natural arithmetic ray of the published all-coprime nonvanishing problem: exponents 2+1/n tend to the threshold 2 while degree 2(n+1) grows without bound. The uniform explicit margin, within 1/n of a realized upper bound on the minimum, controls circle separation and the exact diagonal root count. Its useful content is that quantitative unbounded-degree statement, not the already-known existence of some Bergman-kernel zero.

The dated certificate retains the supplied scientific assessment, sources and limitations.
