---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For n>=3 cyclic gaps of iid uniform points have Dirichlet(1,...,1) law and twice each cell length is a sum of two adjacent gaps. Aggregation gives Beta(2,n-2) tail p_n=(1-q)^{n-2}(1+(n-2)q). Conditioning on the common spacing gives adjacent joint tail 2(1-q)^{n-1}-(1-2q)_+^{n-1}; aggregating four disjoint gaps gives the displayed three-term nonadjacent joint tail. For n=3 covariance factors strictly negative; for n=4 it factors into nonnegative expressions with unique interior zero at q=1/2. For n>=5, the proof shows F(q)+G(q) decreases below 2 when q<=1/2 (via an exponential strict bound), and F(q)<2 for q>=1/2, so adjacent covariance is positive. Conditional Beta decrease yields strict nonadjacent negativity even at n=4 via B=1-A. Fixed-x expansions at q=x/n give the positive adjacent limit and negative order-1/n nonadjacent term. Independent exact rational calculations checked signs at 185 sample-size/threshold points, n=3..39, not the continuum all-n proof.

## originality

PASS

The exact model is fixed-number iid uniform sites on a circle, not a Poisson/Voronoi limit or a shuffled lattice. Devroye et al. study the one-cell typical measure and asymptotics; Gabrielli–Torquato's two-cell laws concern a shuffled-lattice point process with a different dependence structure. The sharp adjacent covariance sign change at n=4/5 and independence at four cells are not implied by either distinct-model result. Search absence is not proof: older special exact circle calculations remain a risk.

## value

PASS

Adjacent-cell threshold dependence is a natural geometric-probability observable for finite samples. An all-threshold, all-finite-n phase diagram has a sharp sample-size transition and an exceptional exact independence point, alongside a strict sign distinction for nonadjacent cells and a Poisson-scale limiting separation. These structural facts extend beyond routine single-cell Dirichlet tails.

The dated certificate retains the supplied scientific assessment, sources and limitations.
