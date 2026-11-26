---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The copy index jumps exactly at weak descents. Subtracting cumulative jumps gives the multiset count binom(m+ell-1-delta,ell). The delta+1 increasing runs have capacity q each. For each r<m, the best count within (r-1)q<ell<=rq grows strictly in ell, and is strict in the required direction as delta increases from r-1. At ell=qr, achieving minimum delta forces every run to equal P_q. The r=m band and the empty word contribute at most one, and m=1 has the stated exception. Factorial cancellation gives positive, strictly decreasing adjacent ratios (each product-factor derivative has numerator -qm-j); the negative-binomial sum over m gives the bivariate enumerator. The limiting adjacent-ratio equation has one interior root alpha=(1-rho)/(1+(q-1)rho), with rho=(1-rho)^q. The limiting ratio has strictly negative derivative at alpha; on a fixed interior neighborhood the finite ratio differs uniformly by O_q(1/m), so the optimizing integer differs from alpha*m by O_q(1). Stirling then gives the stated -1/2 log m, with exponential factor rho^-m=beta_q^(qm). The subsequence of source lengths qm bounds the existing global rate; it does not identify it. Independent bounded enumeration by position masks reproduced every occurring target count and the entire maximizing set at (q,m)=(3,2),(3,3),(3,4),(4,3),(5,3), with maxima 4,10,28,15,21. The frozen DP checker was inspected, not executed; its reported generating-function recurrence is for row sums, not a standalone proof of the bivariate identity.

## originality

PASS

Credit Fang's binary calculation, rationality framework and alphabet-independent upper estimate, and Bukh–Saatashvili's stronger large-alphabet estimates for the global minimum. The supported distinct contribution is the fixed-source q>=3 all-target extremal result with its explicit mode, enumerator and refined rate. A later indexed record has the same occurrence formula, an exact partial overlap, but does not establish earlier coverage of this frozen result or state its cross-length refined extremum. No priority beyond inspected evidence is certified.

## value

PASS

The complete maximizer classification and one-or-two-adjacent mode rule solve a natural periodic-source benchmark, not merely one target count. The prefactor-scale asymptotic distinguishes the maximum from the total number of admissible embeddings, and the explicit all-q construction provides a useful reference against other constructions even where stronger global upper bounds exist.

The dated certificate retains the supplied scientific assessment, sources and limitations.
