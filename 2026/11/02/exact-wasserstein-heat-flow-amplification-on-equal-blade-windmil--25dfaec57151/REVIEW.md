# Scientific review

## Correctness — PASS

The statement concerns every integer \(r\geq2\), \(m\geq1\), every real \(t\geq0\), the unit-edge unnormalized combinatorial Laplacian and graph-distance Wasserstein-one for arbitrary probability laws. The proof verifies the four invariant spectral subspaces and the exact hub-minus-leaf heat vector. Its crucial sign inequality \(rz-(r-1)-z^r\leq0\) on \(0\leq z\leq1\) is elementary and covers the boundary case \(m=1\); a matching explicit transportation plan and Lipschitz witness give equality. The Dirac-edge reduction proves the global probability-pair norm. Differentiation gives the full contractivity classification and unique amplified peak, without extrapolating finite computations to all graph sizes. The included checker independently compares matrix exponentials against transport linear programs on a finite test grid.

## Originality — PASS, with historical-priority limitation

The all-time \(W_1\) norm is not a windmill Laplacian spectrum calculation, a curvature lower bound or a previously established all-time expression in the inspected sources. Kooij (2018 online, Theorem 8) computes a known Laplacian spectrum for generalized windmills, but does not compute this induced transport norm. Münch–Wojciechowski (2017, Theorems 3.8 and 5.8) characterize graph coarse curvature by infinitesimal heat transport and provide gradient implications, not exact finite-time windmill coefficients. Pedrotti (2023, Section 5) gives general continuous-time curvature/coupling tools and other chain applications rather than the displayed windmill family formula. Lin–You (2024) analyze degree-normalized Lin–Lu–Yau curvature, a distinct operator and invariant. Literature searches and comparisons do not logically prove world-wide priority: equivalent older formulas using aliases such as friendship graphs, bouquets of cliques, or coupling rates remain a residual risk.

## Mathematical value — PASS

The all-parameter identity is a sharp induced transport norm on a natural infinite family of finite reversible, spectrally gapped semigroups. It completely classifies when graph-distance \(W_1\) temporarily amplifies, identifies the unique worst time and exact peak, and shows a nontrivial cancellation of the within-clique spectral mode. The critical phase line and the size limits are motivated as quantitative limits of coarse curvature bounds rather than arbitrary numerical slices.

## Limitations

The result does not cover nonuniform blade sizes, weighted edges, degree-normalized Laplacians, \(W_p\) with \(p\ne1\), or infinite graphs. There has been no independent proof audit or comprehensive historical-priority certification. The numerical checker is supplementary, not a replacement for an infinite-family argument.

Self-review: passed. Independent audit: not yet performed.
