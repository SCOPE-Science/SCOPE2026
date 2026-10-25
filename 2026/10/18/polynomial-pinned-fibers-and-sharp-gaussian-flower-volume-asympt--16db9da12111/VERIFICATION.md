---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For fixed ell>=3, integrating McCormick edge intervals after a_i=1-2|x_i-1/2| gives q_ell(u)=2^-ell K^ell(a,a), K=min(s,t), hence Dirichlet-Neumann eigenseries. The disjoint odd-cycle inequality simplex slices yield d_ell(u)=2^-ell/((ell-1)!)^2∫_(2|u|)^1(s²-4u²)^(ell-1)ds. Bernoulli cosine polynomial conversion shows the lone odd |u|^(2ell-1) terms in q and d cancel, giving exact even p_ell=q-d with degree <=2ell-2. Differentiating central fibers gives b_Q,b_D,b_P and strict b_P<b_Q; central strict maxima and one-dimensional Laplace asymptotics yield ratio rho_ell^k sqrt(bQ/bP)(1+O_ell(1/k)) with Gaussian pinned fluctuations. Independent exact symbolic checks ell=3..7 reconstruct p_3,p_4 and verify cancellations; arbitrary ell follows from cosine series and integration, not finite experiments.

## originality

PASS

Important overlap: Jon Lee arXiv:2610.00734 §7.2 already states a broader even-polynomial pinned-fiber property for all series-parallel blocks, so parity/polynomiality alone is NOT NEW. Its Theorem 8.8 provides exponential flower ratio with only bounded polynomial prefactor; explicit all-u missing-fiber formula, sharp constant sqrt(b_Q/b_P), O(1/k) correction and pinned Gaussian limit are not implied. Scientific PASS rests on these surviving refinements, not on prior polynomiality.

## value

PASS

The exact all-u cycle volume fibers and especially the sharp order-one prefactor and Gaussian fluctuation law resolve a quantitatively natural gap between known exponential central ratios and bounds with polynomial-in-petal losses. Explicit b_P,b_Q distinguish concentration under relaxation and true polytope, a motivated geometric question rather than a table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
