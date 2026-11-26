---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

RESULT.md lines 68–108: merging unspecified Dirichlet coordinates gives u,v_r,w_r; the same-color indicator product vanishes, so the cross moment is m(m−1)w_r. After division by positive factors the sign compares R with m/(m−1). In k=n−r, the factor (a)_k/(b)_k decreases strictly since a=(m−2)α<b=(m−1)α. At r=1, increasing n from 1 multiplies R by 1−α(α+1)/[(b+n)(b+n−1)]<1; at r=n the product starts with m/(m−1) and has further factors greater than one. At α=1 the two marginal ratios give the exact sign of m(r−1)−2(n−1). Independent replay: start with probability 1 on the all-zero count vector, and at step t add color i with weight (α+N_i)/(mα+t); sum the three moments over the final state probabilities. Exact rational replay agrees with the formula and signs in all 420 cases m=3,4,5; n=2,…,8; α=1/2,1,3/2,2; 1≤r≤n, including the exact zero at (3,4,3,1). The reviewed frozen checker is finite, and its numeric checks do not prove asymptotic convergence. Lines 110–133: gamma ratios give R→B/(1−x)^α for r/n→x<1, so test points strictly bracketing the continuous crossing bound the discrete first nonnegative index. Log-convexity puts B in (0,1); Stirling gives (6). For fixed n the iid limit of R never equals m/(m−1): the equality would give (m/(m−1))^(n−1)=((m−1)/(m−2))^(n−r), impossible by taking the valuation of a prime dividing m−1. Thus the discrete index stabilizes as α→∞ at fixed n. Solving the iid logarithmic inequality yields (7). The m=3 fractions already disprove commutation; in fact the fixed-α-first limit is smaller for every m≥3. To verify the strict comparison, put x=1/(m−1), S=atanh(x), T=−log(1−x²)/2. The negative logarithm of the ratio subtracted from 1 in (6) is 2(S−T/x), while that for (7) is 2 atanh(T/S). Put U=S/x and W=T/x². The coefficient of x^(2j) in W(U+1)−U² is (1−B_j)/(2j+2), where B_j=∑_{i=0}^j 1/[(2i+1)(2i+2)]+H_(2j+2)/(2j+3) and H_k is the harmonic number. This follows by multiplying the logarithmic series and splitting the two reciprocal factors. B_0=1 and B_(j+1)−B_j=(3−2H_k)/[(k+1)(k+3)]≤0 for k=2j+2, so T/S≥S−T/x; strict atanh(T/S)>T/S gives the comparison. Neither limit covers a general joint α,n scaling.

## originality

PASS

The covered pieces are the raw Dirichlet-multinomial occupancy law and moments and the iid counterpart, including the iid limiting fraction. The closest indexed reinforced result varies sample size at fixed exact frequency for two labeled indicators, not frequency at fixed sample size for the aggregate counts. The supported distinct contribution is the finite-concentration aggregate sign/equality classification and the critical-fraction and limit-order comparison, not the distribution or a raw moment formula alone.

## value

PASS

The proof classifies a natural dependence measure across all frequencies, including exact cancellation at a natural parameter value where the iid analogue has none. The critical fraction and the strict limit-order difference show when an apparently natural iid approximation changes a qualitative dependence boundary, independently of the raw covariance computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
