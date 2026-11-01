# Scientific review

## Correctness — PASS

The claimed one-step normalization is \(C_G(s)=2(I+sL_G)^{-1}-I\), with physical time step \(h=2s\). Reconstructing the proof, the auxiliary matrix \(H_G=A_G+\operatorname{diag}(\Delta-\deg_G)\) has nonnegative entries and row sums \(\Delta\); the corresponding Neumann series converges absolutely. Distinct labelled rooted closed walks in the infinite \(\Delta\)-regular tree inject into those in the auxiliary port graph. The resulting resolvent comparison is a coefficientwise inequality, not a heuristic stochastic domination. Exact Schur-complement equations for the regular tree yield the unique half-return threshold \(\sigma_\Delta=(2\Delta-1)/(2\Delta(\Delta-1))\). Boundary balls yield asymptotic equality by bounded dominated convergence, and the strict finite inequality follows from a cycle or deficiency port. The standard-library verification script passed its exact checks. Scientific limit: finite checking is not the all-graph proof; the explicit port-lifting and convergence arguments supply the infinite assertions.

## Originality — PASS on inspected evidence, with residual risk

Closest literature: Faragó–Horváth (DOI `10.1137/050627241`, inspected full-text Sections 4–6) provides a general matrix criterion and sufficient mesh-dependent bounds; it does not give a sharp uniform degree-only result. Bressloff–Dwyer–Kearney (DOI `10.1088/0305-4470/29/9/005`, inspected author-uploaded article Sections 1–2 and its stated section structure) develops diffusion Green functions on trees, but no inspected Crank–Nicolson positivity classification. Angel–Friedman–Hoory (`arXiv:0712.0192`, abstract inspected) studies covering-tree resolvents, not the asserted positivity threshold. Earlier finite-path results and a general resolvent-return positivity criterion cover components of the reasoning but do not imply the sharp all-graph \(\Delta\)-only bound without a new extremal comparison. Full-text access to Z. Horváth (2005) was unsuccessful; specialized prior literature could still contain an equivalent result. The original contribution is the complete sharp degree-class theorem, not its classical sublemmas.

## Mathematical value — PASS

A maximum-degree cap is a natural, readily known structural constraint for diffusion on arbitrary sparse networks. The result gives the **exact** uniform positivity frontier for all finite topologies and sizes under that cap, improves the simple diagonal sufficient condition \(s\le1/\Delta\) to \(s\le(1+1/[2(\Delta-1)])/\Delta\), and proves that finite regular-tree balls force sharpness. This is an all-graph extremal statement, not a graph-specific computation or a reformulation of the matrix criterion. It does not claim weighted, normalized, or nonlinear extensions.

## Qualification

The literature comparisons support originality to the extent inspected; absence of a search hit is not proof of publication novelty. A human independent mathematical and priority assessment is still necessary.

Self-review: passed. Independent audit: not yet performed.
