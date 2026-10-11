---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
The all-parameter symbolic proof, rather than a finite scan, is in `RESULT.md`.

- The full \(N^2+2N\) facet system and dimension \(N^2-1\) for \(N\ge3\), \(2\le k<N\) come from the same-object 2009 Theorem 3 and facet table and the 2023 complete-bipartite H-representation.
- Projection of an entry normal into the fixed-total tangent space has norm \(q_N=\sqrt{1-1/N^2}\).
- A row/column-sum normal projects with norm \(\sqrt{N-1}\).
- Averaging all entry clearances and all row clearances bounds \(\rho\) by \(u_{N,k}\) and \(v_{N,k}\). The uniform matrix attains the smaller bound.
- Equality in the entry bound uniquely forces all entries to \(k/N^2\). Equality in the row and column bounds forces all margins to \(k/N\); subtracting the coordinate clearance floor leaves an exactly doubly stochastic residual matrix.
- The Birkhoff polytope has affine dimension \((N-1)^2\) and vertices the \(N!\) permutation matrices, giving the full set of high-rank incenters and its tangencies.
- Each assignment vertex has exactly \(k\) unit entries and average \(kJ/N^2\); the squared-distance barycenter identity proves the unique outer sphere.

Running `python verify.py` independently checks the intrinsic inradius linear program for every \(N=3,\ldots,15\), \(k=2,\ldots,N-1\), verifies formula thresholds, tests nonuniform optimal centers arising from permutation matrices, and enumerates all vertices for selected small cases to verify the exact outer sphere. It is numerical/exhaustive corroboration on bounded inputs, not an infinite or independent proof.
