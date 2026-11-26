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

An independent spectral upper bound uses an embedding with hub at zero. The other n−1 clique vertices have a regular simplex of side one in an orthogonal plane or subspace, of squared circumradius (n−2)/(2(n−1)), translated along an axis to height S_n/(n−1) so every hub edge has length one. Their resultant is S_n along the axis. If m<S_n, put all pendant vertices at the opposite axial unit vector. Otherwise use unit vectors with common axial coordinate −S_n/m and transverse components summing to zero; m>=2 permits this, and the equality case has zero transverse component. All graph edge lengths are at most one, and the centered sum of squared norms is D_{n,m}. Applying the Rayleigh inequality to each centered coordinate gives lambda_2*D_{n,m}<=sum_e w_e times its squared length<=B for every feasible weight vector. For attainability, the two difference spaces have eigenvalues c and a+(n−1)b; the nonzero quotient roots have sum na+(m+1)c and product (n+m)ac. Substitution of the stated active weights gives one quotient root equal to 1, the other greater than 1, and the difference-space constraints, with exact cost D_{n,m}. At and above equality the stated uniform star has unit target gap. If m>=S_n, equality in the embedding bound forces its nonzero centered axial coordinate vector to be a lambda_2 eigenvector. At each non-hub clique vertex, interior clique terms cancel (same axial value); at each leaf there is one term. Because all these axial entries are nonzero and the centered hub entry is zero, every hub edge has weight lambda_2, consuming the budget and forcing the claimed zero weights, including at m=S_n. If m<S_n, omitting all interior clique edges reduces to a star, whose best gap is B/(n+m−1) by averaging, strictly below the optimum. The exhibited active design has every edge positive.

## originality

PASS

The distinct contribution is the exact two-parameter optimum and transition at m=sqrt(n(n−1)/2), together with the every-optimizer aggregate support assertion on both sides, not the general fastest-mixing SDP, separator embedding theory or graph definition. The closest general work gives usable prior machinery and structural information on a more restricted large-leaf regime. The closest catalogue records differ in topology, objective or constraints and do not supply this sharp threshold or the explicit active optimum.

## value

PASS

A budgeted diffusion on the canonical clique-with-leaves graph can optimally use less of the available topology. The result tells exactly when interior edges go from necessary in any optimum to forbidden in every optimum, and the explicit penalty relative to a star shows the size of the spectral gain in the active regime. The equality and nonsymmetric cases make the cutoff informative beyond finding a symmetric example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
