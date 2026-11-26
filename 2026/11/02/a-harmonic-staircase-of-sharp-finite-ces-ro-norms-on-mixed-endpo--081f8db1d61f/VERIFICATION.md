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

The nonnegative matrix allows replacement by |x|. Decompose it into nested support indicators with coefficient differences of its decreasing rearrangement. The input norm is exactly the corresponding positive linear combination of 1+ε(k−1), so the triangle inequality reduces the maximum to indicators. A k-support has sup output at most 1 by the row-sum bound and ℓ1 output equal to its sum of columns c_j(t). The latter decrease strictly for all 0≤t≤1 by termwise comparison (including the diagonal at t=0). The prefix {1,…,k} maximizes the sum and attains sup output 1 at row 1, so it is optimal among all k-support indicators. For t=1, summing the harmonic column sums gives k[1+H_n−H_k]. For 1≤k<n, set h=H_n−H_k; subtracting the next quotient gives the sign of (h−1)−ε(h+k−1), for r_{k+1}−r_k. For h≤1 it is strictly negative for ε>0. Otherwise the unique zero lies in (0,1), and the zeros strictly decrease as h decreases and k increases. This yields the asserted single peak or adjacent tie among candidate indicators. It includes rank one for n≤3, the threshold 1/13 at n=4, and the ℓ1 endpoint at ε=1. The ε↓0 first variation is k(H_n−H_k). Along k/n→u, this divided by n tends to u log(1/u), with the endpoint 0 controlled by (k/n)log(n/k), and the unique maximizer is u=1/e; comparing to k=floor(n/e) proves the assertion for every maximizing sequence. The checker and verification notes were inspected, not rerun. Their exact finite support evaluations and threshold comparisons do not substitute for the argument over all parameters.

## originality

PASS

The prefix-indicator supremum architecture on d(w,1) is prior, and is not credited as original. The distinct supported result is the evaluated finite harmonic optimization as the endpoint weight changes: exact adjacent transition values, their global order, and the limiting optimal support fraction. The closest prior Lorentz framework supplies the type of supremum, but the inspected statements do not give this staircase or resolve its optimization for plateau weights. The finite formula is treated as an ingredient of that specific result, not a new general Lorentz norm theorem.

## value

PASS

The mixed norm is a natural finite interpolation between two endpoint measurements. Exact optimization shows that even a small positive ℓ1 weight can select a macroscopic prefix, whereas a larger weight selects smaller ranks, all the way to rank one, and gives the precise switching weights instead of an endpoint or operator bound. Knowing which finite supports realize amplification is useful in its own right; the contribution is not the standard indicator reduction or known pure endpoint norm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
