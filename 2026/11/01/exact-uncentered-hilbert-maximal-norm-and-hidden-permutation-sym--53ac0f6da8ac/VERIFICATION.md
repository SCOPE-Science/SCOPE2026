---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Read RESULT.md and the exact Fraction verifier. The ball set is four singletons, four complements of singletons, and all vertices, invariant under S4. Sorting positive inputs reduces each output to four row-matrix branches; exact Sylvester minors rule out all three competitors below 377/250. Winning A^T A has det(zI-A^T A)=z(81z^3-162z^2+64z-6)/81, with a unique >1 root and positive strictly active Perron eigenvector (1,a,b,c), a=b+c and all entries distinct. The eigenvalue and S4/D4 equality orbits are therefore sharp, while exhaustive exact rational tests for all 3^4 centered row selections prove squared norm <377/250. Independently computed NumPy Gram spectra: winner lambda=1.5088893112813764, other maxima 1.4718163364,1.4805061467,1.4038255242, centered maximum 1.4805061467; these numerical checks do not replace the exact finite certificate.

## originality

PASS

Known finite-graph maximal-operator bounds and sharp centered complete/star families do not supply the exact uncentered C4 cubic, full S4 equivariance and equality classification. The graph-ball family, not just the name of the graph, was compared.

## value

PASS

This is the first small cyclic graph where uncentered balls realize an S4-symmetric 3-uniform hypergraph. An exact strong ell2 norm, unique spectral extremizing pattern and strict centered-vs-uncentered separation illuminate a nonobvious nonlinear symmetry: 24 extremizer rays from only eight graph automorphisms. The finite classification is exact and structurally motivated, not an arbitrary data-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
