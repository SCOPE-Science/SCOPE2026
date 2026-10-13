# Self-review

## Correctness — PASS
With degree-weighted inner product, \(P=D^{-1}A\) is self-adjoint and \(\Delta s=0\); the two states have unit norm for every connected graph with at least two vertices. Probability one forces equality of the two energy moments under the *same* Hamiltonian. The first moment uniquely forces \(\gamma=1-\pi\); the second gives \(R_w=\pi/(1-\pi)\). Cauchy–Schwarz and positive vertex degrees give the sharp inequality and its two equality conditions, exactly universal apex and constant degrees off the apex. The invariant two-state block at every such cone squares to a multiple of the identity and its exponential yields all perfect times. The full graph is covered regardless of other eigenvalue degeneracies. Exact-rational finite-graph checks and block checks in `verify.py` support, but do not replace, this analytic argument.

## Originality — PASS
The primary source arXiv:2207.01686 and its open-access 2024 final text were inspected in the model/overlap/completeness sections: they formulate this normalized-Laplacian search and solve the complete graph, but do not give the global cone-over-regular iff. The closest universal-vertex theorem by Razzoli–Bordone–Paris uses the different combinatorial Laplacian \(D-A\), which succeeds on *all* cones rather than just cones over regular bases. Coutinho–Baptista and Alvir et al. concern unperturbed vertex-to-vertex transfer with no oracle. Candidate-specific repository and literature searches uncovered no covering result. Residual risk: different nomenclature or weakly indexed equivalent classification, and independence has not been assessed.

## Value — PASS
This settles exact deterministic search for the canonical degree-reversible graph Laplacian on every finite simple connected graph, including the unique admissible tuning and the full hitting-time law. It isolates a physical distinction missed by transferring combinatorial-Laplacian intuition to degree-normalized dynamics: for example a universal vertex atop a nonregular base is not perfectly searchable in the normalized setting. The immediate regular-graph consequence excludes all noncomplete regular graphs from exact finite-time probability one under this fixed protocol. This is a structural model-specific classification, not a numerical threshold or a generic no-go claim for other protocols.

## Closest literature and residual limitations
Mograby et al., arXiv:2207.01686 / DOI:10.1007/s11128-023-04212-w; Razzoli et al., arXiv:2202.13824; Coutinho–Baptista, arXiv:2209.04668; Alvir et al., arXiv:1409.5840. This proof does not bound the supremum of success probabilities for nonqualifying graphs and does not treat weighted or nonstationary variants.

Self-review: passed. Independent audit: not yet performed.
