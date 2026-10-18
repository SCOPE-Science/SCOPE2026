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

For independent uniform q-th-root phases, centered purity P−μ=(4/N²)∑_{rectangles} Re(z_rectangle), where N=UV. Each rectangle has mean zero, pairwise distinct rectangles are uncorrelated. In cubic expansion, only three copies of the same plaquette (q=3: moment 1/4) or triangle of 3 different rectangles supported on 2×3/3×2 grids survive. Ordered triples contribute 6T for q=2 or 6T/4 otherwise, with lone q=3 contribution R/4. Therefore E[(P−μ)^3]=64/N^6 times [6T,(6T+R)/4,3T/2] for q=2,3,>=4/continuous, respectively, with established variance and skewness. Independent complete finite phase-state expectation computations for U,V=(2,2),(2,3),(3,3), alphabets 2,3,4: eight cases, 25,437 enumerated states, all exact target moments to numerical comparison tolerance; full proof is exponent-divisibility argument, not the tests.

## originality

PASS

Trotta et al 2026 original full 12-page arxiv paper Eq.23–26 gives fixed-cut purity and only mean/variance, not the cubic plaquette-triangle cumulant or q=3 single-plaquette resonance. Scarafile et al arXiv:2609.24508 treats the distinct averaged-cut real hypergraph purity; complete manuscript unavailable, leaving overlap risk especially at real phases. Its inaccessibility is expressly NOT treated as automatic failure. Resultary semantic search for exact third moment and cubic phase resonance did not locate covering result. Best-of-knowledge O PASS with explicit residual risk.

## value

PASS

Third central moment is the next natural fixed-cut distributional invariant once first two cumulants and approximate Gaussian profiles are known. The exact q=3 exception and explicit 1/d asymptotic skewness provide useful finite-size non-Gaussian discrimination for real signs, Butson phases and continuous flat phases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
