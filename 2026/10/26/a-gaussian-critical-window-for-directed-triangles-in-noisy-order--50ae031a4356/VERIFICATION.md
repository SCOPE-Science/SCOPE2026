---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Writing X_ab as the rank-forward edge indicator and Y_ab=X_ab-p, direct expansion of the two cyclic orientations on a<b<c cancels the cubic term and yields (I_abc-r)=(1-2p)Y_ac+Y_abY_bc-Y_abY_ac-Y_bcY_ac. The linear and quadratic sums are orthogonal, as are distinct centered unordered incident-edge products, so E C_n=binom(n,3)r and Var C_n=3binom(n,3)r²+[n(n-1)²(n-2)/12]r(1-2p)². I independently enumerated every tournament orientation for n=3,4,5 at several rational p and matched moments. Inside sqrt(n)(p_n-1/2)->c, each linear coefficient O(sqrt n), each quadratic coefficient ±1. Any surviving k-th joint cumulant monomial diagram must have each centered edge repeated and connected; for s linear terms, at most k-s/2 distinct edges and k-s/2+1 labeled vertices. This gives O_k(n^{k+1}) k-th cumulants, which after division by n^{3k/2} vanish for k≥3. The variance coefficient tends to c²/12+1/32; Gaussian moment determinacy gives weak convergence. Outside the window with p away from {0,1}, Q has negligible L² variance and independent bounded weighted Y terms satisfy Lindeberg, giving the stated normalized CLT. The finite enumeration does not certify either limit theorem.

## originality

PASS

Best-of-knowledge original explicit varying-bias Gaussian crossover for rank-directed tournament triangles; exact coefficients must be calculated rather than inferred from the fair case alone. The fair p=1/2 component is acknowledged prior in general random tournament subgraph-count theory.

## value

PASS

The natural triangle count of a noisy total order exhibits a sharp change in stochastic fluctuation scale controlled by one bias parameter. The explicit critical-window variance, including the fair degenerate component and rank-induced linear component, gives a meaningful local phase diagram useful in random ranking and tournament models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
