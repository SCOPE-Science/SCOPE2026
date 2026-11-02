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

For a weighted m-leaf star, effective resistances yield (L^dagger)_00=S/n², (L^dagger)_ii=(S+(m²−1)r_i)/n² with r_i=1/w_i, S=Σr_i, n=m+1. The primal budget is Σc_i/r_i≤B. For any simplex p, max r_i≥Σp_i r_i and Cauchy–Schwarz give global lower bound [Σsqrt((1+αp_i)c_i)]²/(n²B), α=m²−1. Strictly concave dual maximization gives p_i=(c_i/τ−1)_+/α with Σ(...)=α, unique τ>0. Taking y_i=min(1,sqrt(c_i/τ)), r_i=Z y_i/B, Z=Σc_i/y_i attains all inequalities and is uniquely optimal by CS equality and budget saturation. Active set formula, iff equal allocation criterion min c_i≥C/(m²+m−1), and sharp price-uniformity factor (m²+m−1)/m² follow. Independent Laplacian pseudoinverse calculation for m=4, c=(240,32,1,4), B=284 gave w=(1,1,4,2) and max diagonal .71, matching analytic formula 71/100; ratio limit argument is analytic, not sample inference.

## originality

PASS

Ghosh–Boyd–Saberi (2008) optimize total effective resistance and mention maximum pairwise resistance; those two objectives are different from max vertex diagonal of L†. Patterson–Bamieh trace coherence and Summers et al adding edges do not give arbitrary positive price star edge allocation. Van Mieghem et al calculate unweighted star pseudoinverse diagonals but not the global priced minimax water-filling law, equal-price threshold and sharp universal ratio. The optimization combines known resistance and convex-duality techniques into a natural exact classification.

## value

PASS

For a standard noisy-consensus network observable, the result computes an exact unique optimal resource allocation on every weighted star with arbitrary linear prices. The active-set phase transition, sharp condition for uniform conductances and universal price-of-uniformity limit are useful structural design facts, not mere reproduction of generic convexity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
