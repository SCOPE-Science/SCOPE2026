---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For n>=3 and 1<=k<=n-2, the two-level inclusion graph has Laplacian Schur complement the Johnson graph Laplacian, with a zero-sum edge source. Summing Green equations over Johnson distance balls yields strictly positive radial drops Delta_r; shell-ratio monotonicity verifies the nontrivial sign of each electrical edge current, including the formerly ambiguous z-in-S/i-in-A class. The explicitly displayed quadratic vertex potential w solves Lw=D sigma, so the signed sum of every edge column of Q=D^T(DD^T)^+D equals 2k+1-2k(k+1)/n. The source effective resistance Q_ee=1/(k+1)+(1-1/binom(n,k))/(n-k) gives the complementary P norm by |(I-Q)ee|=1-Qee. Complementation k -> n-k-1 covers remaining ranks; fixed-k and proportional-k asymptotics follow. Independently built rational grounded full-graph Laplacians reproduce norm, diagonal, and P norm for 10 (n,k) cases with 3<=n<=6; polynomial dual identity in the source was reconstructed by inspecting its coefficients rather than treating VERIFY_OK as proof. The infinite family follows from the Green/dual argument, not enumeration.

## originality

PASS

Best-of-knowledge mathematical comparison of the same object, definitions, parameter quantifiers, and implication strength. Foundation and partial coverage are credited explicitly; neither failed searches nor inaccessible full literature alone are represented as novelty proof. Cut-cycle projection and invariant projection are aliases of an orthogonal incidence-Hodge projector, but equality of graph and projector must also be shown; the inspected whole-cube formula is not an equivalent formula for the adjacency-rank graph. Neither cited formula implies the stated adjacent-rank Q and P norms solely by parameter substitution; the direct Johnson Green and sign solution add necessary work.

## value

PASS

Natural canonical Euclidean cut and cycle projections on adjacent ranks of the Boolean lattice are common in discrete Hodge theory and electrical flows. Exact induced endpoint norms, not solely upper bounds, distinguish bounded fixed-rank and linearly growing central-rank regimes. The uniform edge column and exact resistance provide reusable sharp constants; this is not a renaming of the full Hamming cube projection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
