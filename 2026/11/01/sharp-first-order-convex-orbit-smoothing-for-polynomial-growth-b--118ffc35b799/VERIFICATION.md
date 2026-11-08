---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

PASS: B^j e_0=j^theta e_-j for j>=1 follows by telescoping negative weights and the j=0 initial orbit; lambda on positive indices never enters this fixed vector orbit. For y=(I-B)e_0 and convex coefficients a_0..a_(n-1), the squared norm is sum_(j=0)^n b_j²/R_j with b_j=a_j-a_(j-1), R_0=1, R_j=j^(-2theta), sum b_j=0 and sum(n-j)b_j=1. Weighted Cauchy–Schwarz yields 1/[S2-S1²/S0] and equality b_j=R_j(S1-jS0)/D. Since the signed b_j changes sign only once and sums to zero, every proper cumulative a_k is strictly positive, sums to 1, and attains the sharp constrained objective uniquely. Integral comparison gives S2~n^(3-2theta)/(3-2theta) for 1<=theta<3/2 and S2~log n at theta=3/2; the S1²/S0 term is lower-order there, while all moments converge for theta>3/2 to a strictly positive inverse-variance barrier. Independent exact rational coefficient and variational-energy tests reproduce all sample identities but do not prove the asymptotic for every theta.

## originality

PASS

PASS, best of knowledge: existing global convex-cyclicity and Cesaro sufficient criteria for bilateral weighted shifts concern all-vector orbit density and do not assert the exact degree-constrained convex hull distance for the special coboundary y, its positive unique optimizer or the sharp theta=3/2 boundary. Related Dirichlet value-interpolation is not the derivative constraint here. Recent Wang–Zhou primary full text remained inaccessible after lawful OA and authorized VPN attempt, so comparison is qualified, not whole-paper noncoverage.

## value

PASS

PASS: Exact one-vector convex-orbit distance and its positive minimizing polynomial provide a natural quantitative smoothing/coboundary invariant for a classical operator-dynamics model. The 3/2 decay/barrier transition separates density of this particular convex orbit without overclaiming full operator convex-cyclicity. Not merely renaming an inequality: positivity of the optimizer under inequality constraints is a nonstandard, relevant part.

The dated certificate retains the supplied scientific assessment, sources and limitations.
