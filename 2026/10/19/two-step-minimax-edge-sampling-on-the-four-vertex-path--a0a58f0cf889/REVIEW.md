# Review: finite-horizon edge sampling on a path

## Correctness

**PASS.** The worst-case expected squared error is exactly the top eigenvalue of the two-step moment matrix restricted to the zero-mean subspace; the order of the three factors in each quadratic moment term is essential and is derived explicitly. An exact reflection symmetrization identity holds for all admissible edge probabilities. Its positive-semidefinite remainder is strictly positive along the top eigendirection at every interior asymmetric law, reducing the full simplex optimization to the one-parameter reflection-symmetric family. The resulting two-by-two block has the claimed characteristic radical. Analytic strict convexity, endpoint derivative signs, and a strict derivative sign at the one-step optimum prove both uniqueness and horizon dependence. The smaller-path calculation establishes minimality. A standalone rational-arithmetic checker reproduces critical matrix identities and an optimizer bracket. Decimal values are supplementary, not proofs.

## Originality

**PASS, with explicit residual risk.** The closest established general formula is Agaskar–Wang–Lu's exact finite-time randomized-Kaczmarz mean-square expression, but its paper optimizes the asymptotic annealed exponent, not the globally worst-case exactly-two-step law on the four-vertex path. Boyd and collaborators optimize the average matrix spectral gap, which determines the one-step law but only an upper-bound mechanism at later finite horizons. Gower–Richtárik provides generic sketch-and-project analysis. Related published results about optimal coordinate sampling, deterministic cyclic two-row Kaczmarz, and delayed Gauss–Seidel do not imply the stated i.i.d. three-edge finite-two-step optimizer or its minimal-size boundary. Searches for the precise combination, equivalent incidence-matrix formulation, and stronger general coverage found no decisive source asserting this optimizer. Unindexed exact small-graph calculations remain possible; no absolute novelty guarantee is claimed.

## Value

**PASS.** Fixed i.i.d. edge-selection design is a natural practical optimization variable in randomized consensus and row-projection solvers. The result identifies the first graph size where optimizing the sharp one-step bound ceases to optimize the exact next finite-horizon expected error, gives the unique probability laws on both sides, and proves the transition by symmetry and strict convexity rather than a numerical search. Its value is this rigorous structural boundary and complete small-path classification; the strict numerical improvement itself is modest and is not exaggerated into a broad performance claim.

## Literature and limitations

The principal comparison is Agaskar, Wang, and Lu (2014), DOI 10.1109/GlobalSIP.2014.7032145, specifically the exact-MSE derivation and the asymptotic optimization section. Additional comparators are Boyd et al. (2004), *Analysis and Optimization of Randomized Gossip Algorithms*, and Gower and Richtárik (2015), *Randomized Iterative Methods for Linear Systems*. The theorem applies only to one or two independent updates of the same fixed law on paths with at most four vertices; it neither determines longer-horizon laws nor covers arbitrary networks, weighted graphs, adaptive choices or different objective norms. The published general exact-MSE formula is not claimed as new.

Self-review: passed. Independent audit: not yet performed.
