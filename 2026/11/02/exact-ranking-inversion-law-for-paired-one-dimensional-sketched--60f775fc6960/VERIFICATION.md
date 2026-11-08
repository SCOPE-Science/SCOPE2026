---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Reconstructed from the actual RESULT.md blob: write g=Su,h=Sv, U=||g||²,Z=||h||²,V=g·h. Exact quotient cross-multiplication is (a-b)(c²-s²)[UZ+cs V(U+Z)]; denominator positivity makes inversion equivalent to 1-r²+rho*w<0 on normalized Wishart coordinates. For k>=2, density (k-1)/(2π)(1-r²-w²)^((k-3)/2) integrates to 1; beta conditioning, Tonelli and Gamma simplification yield the displayed 3F2; k=1 needs a circle law, k=2 elliptic E. Gamma duplication plus dominated convergence proves the fixed-rho (rho/2)^k/sqrt(k) asymptotic. Independently evaluated 8 k/rho hypergeometric-vs-beta/elliptic cases, all matched. rho=1 strict-event endpoint is excluded and discontinuous; independent sketches or joint 2D Ritz eigenvalues are not covered.

## originality

PASS

Best-knowledge PASS for the exact paired-common-Gaussian-sketch strict reversal probability, not for Wishart statistics or sketched Ritz methodology. The latter are old; precise one-common-sketch joint-event formula and asymptotic constant were not obtained from inspected primary sections.

## value

PASS

Pairwise ordering is a distinct numerical decision not controlled exactly by an individual quotient error bound. The eigen-gap cancellation, explicit hypergeometric all-row law, singular one-row case, elliptic two-row case and sharp rare-event rate give a nontrivial benchmark for randomized Rayleigh comparisons on a motivated symmetric pair; not a generic algorithmic stability theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
