---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

With fixed unit-edge metric, Kantorovich-Rubinstein duality identifies the global W1 operator norm with the maximum absolute row sum of the edge-gradient semigroup. Direct generator substitution gives h_dot=-2eps h-sum g_j and g_dot_i=-eps h-g_i-sum g_j. Ordinary contrasts decay e^-t, and (h,avg g) follows a 2x2 matrix with eigenvalues lambda_plus/minus as defined; its explicit exponential yields exceptional row sum A exp(-lambda_- t)-(A-1)exp(-lambda_+ t). Sign inequalities using lambda_-<=1 and Delta<=r+1 prove this row dominates all ordinary gradient rows for all t>=0; the deficit pair w/o attains it via the dual gradient potential. Its derivative has at most one sign change and is positive at zero except r=2,eps=1, proving unique peak including boundary; direct Taylor expansion with fixed r gives eps log eps corrections. I independently reconstructed full Markov Q and scipy matrix exponentials and computed the star tree W1 edge costs in 96 parameter/time cases; defect dominance and exact formula matched. The analytic proof covers all r,eps,t, beyond the finite check.

## originality

PASS

Münch–Wojciechowski links Ollivier curvature and semigroup Lipschitz/Wasserstein contraction but does not yield this inhomogeneous 2-eigenvalue star profile. Bai et al. concerns weighted-star Ricci flow with evolving edge-length geometry, not the fixed-metric frozen generator. The equal-rate boundary is recoverable from the windmill/star profile; the entire eps<1, all-time sharp peak and weak-rate logarithmic correction are not implied by that boundary.

## value

PASS

A single slow edge turns a reversible unit-geometry star into an exact transient W1 amplifier with computable metastable peak. The all-time norm, optimizer, phase boundary and weak-bond scaling are a motivated sharp test for curvature/transport bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
