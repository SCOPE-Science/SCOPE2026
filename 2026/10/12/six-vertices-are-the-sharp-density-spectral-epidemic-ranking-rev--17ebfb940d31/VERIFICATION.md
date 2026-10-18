---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

At fixed n the inverse-average-degree proxy ranks only by edge count; the inverse-adjacency-spectral proxy ranks by Perron root. I independently generated ALL connected unlabeled simple graphs for n=2,3,4,5 (1,2,6,21 classes, respectively), computed exact characteristic polynomials and rational real-root isolating intervals, and compared each class pair with unequal edge counts. All n<=5 edge-rank orders were spectral-radius nondecreasing: zero strict reversal pairs. Symbolically K_{1,5} has 5 edges, mean degree 5/3, Perron root sqrt(5)>2, while C6 has 6 edges, mean 2 and Perron root 2. For all n>=6, n-1<n and sqrt(n-1)>2 ensure the same strict reversal. This is complete finite proof of minimality plus exact infinite family; neither numerical approximations nor finite checks support the infinite claim.

## originality

PASS

The published eigenvalue-viewpoint network epidemic papers establish the two competing threshold proxies and the star spectral formula, but do not exhibit the exhaustive sharp n<=5 boundary as a theorem. Full connected-graph census and exact rational spectra make the minimization statement distinct from the elementary star-cycle observation. Relevant published mathematical result search did not find exact coverage; a folklore graph-spectral exercise could still have this comparison.

## value

PASS

The precise first connected equal-order network size at which two widely-used epidemic vulnerability proxies induce opposite strict ranks is a motivated exact finite boundary. It quantifies a failure mode with a rigorous minimum and establishes persistence on a natural infinite graph family; the result does not assert true finite stochastic SIS extinction thresholds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
