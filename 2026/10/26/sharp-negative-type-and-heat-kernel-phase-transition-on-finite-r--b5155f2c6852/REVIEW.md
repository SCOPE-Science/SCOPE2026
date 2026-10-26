# Self-review of the rank-two finite Grassmannian distance-kernel classification

## Correctness — PASS

The point-to-two-subspace incidence matrix gives the identities \(BB^\top=(r-1)I+J\) and \(B^\top B=(q+1)I+A\). These supply every eigenvalue and its multiplicity without an external spectrum assertion. The distance-power matrix has zero-sum eigenvalues \(-b+(1-b)(r-q-2)\) and \(q+1-qb\), so the stated threshold and minimal embedding ranks follow. The exponential kernel has the three explicit eigenvalues in RESULT.md; two remain strictly positive for \(0<t<1\), while the third has the proved one-root convexity classification. Exact finite-field checks passed for \((q,n)=(2,4),(2,5),(3,4)\). Risks: finite tests do not certify arbitrary dimensions; the universal conclusion depends on the displayed algebra and elementary calculus.

## Originality — PASS within the inspected literature

The closest general theory is Sánchez's finite-distance-matrix approach and Murugan's vertex-transitive determinant criterion. The inspected full texts do not calculate the rank-two \(q\)-Grassmann threshold or its critical embedding dimension. Harandi et al. treat real continuous Grassmannians and different kernels. Related finite Grassmannian results concern restrictions of Fourier eigenspaces or projector norms, not the graph-distance negative-type/heat-kernel criterion. An equivalent result derived elsewhere from the classical adjacency spectrum remains the strongest residual risk; literature-search absence alone is not a proof of novelty.

## Mathematical value — PASS

This is a full natural-invariant classification for every rank-two finite-field Grassmann graph, not a selected numerical instance: it determines its exact generalized-roundness endpoint, yields an explicit optimal Euclidean snowflake embedding at the endpoint, determines the sharp rank collapse, and classifies all exponential powered-distance covariances, including the unexpected isolated trivial admissibility point when \(p>p_*\). The special case \(p=1\) gives the exact kernel threshold \(a=\log q\) uniformly in ambient dimension. The proof uses classical association-scheme inputs, but the combined exact phase diagram and optimal embedding answer well-motivated harmonic-analysis questions.

## Limitations and closest comparison

The finite-field two-subspace result is not extended to higher subspace rank. Full indexing of the literature cannot be guaranteed, and the close consequence of known adjacency spectra and general negative-type theory is acknowledged. Independent mathematical replication has not been performed.

Self-review: passed. Independent audit: not yet performed.
