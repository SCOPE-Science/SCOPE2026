# Scientific review: weighted triangular-book cycle-space projection

## Correctness — PASS

The domain is the real edge space of a specified weighted triangular book with integer \(m\ge2\) and \(0<t\le2\). The cycle space has the explicit basis \(z_i=e_{x_i}+e_{y_i}-e_c\). Group averaging is norm contractive and preserves the projection identity and range. All invariant projections reduce to one real parameter; computing the weighted \(\ell_1\) column norms yields equation (1) in RESULT.md. Its monotone branches restrict the optimum to \(-1/m\le u\le0\); the change of sign of the second branch's slope occurs exactly when \(m(2-t)=4\). Every equality and endpoint is checked analytically. The separately packaged exact checker passes 112 comparisons and independently optimizes 20 unsymmetrized linear programs with SciPy (numerical corroboration only). The proof does not rely on those finite tests.

## Originality — PASS with residual bibliographic risk

Ostrovska–Ostrovskii (arXiv:1910.03625, §3) identifies finite transportation cost spaces as quotients of weighted edge \(\ell_1\)-spaces by their cycle spaces, without computing minimum projections for triangular books. Dilworth–Kutzarova–Ostrovskii (arXiv:1807.03814, §§4–6) develops averaging and projection estimates for recursively defined diamonds and Laakso graphs, not a weighted spine joined to all leaves. Their 2024 *Cycle Spaces* paper treats general invariant-projection structure, then explicitly focuses on discrete tori and Hamming graphs (§2); the general results motivate but do not supply the two-parameter optimum. Indexed book-graph results about ellipsoids, and cactus edge-basis projections, concern different operators or graphs. Record queries for the aliases "triangular book", \(K_{1,1,m}\), "shared-edge triangles", "cycle-flow complementability", and the special constants revealed no formula covering the claim. This is evidence of no identified coverage, not a proof that no unpublished or unindexed equivalent exists.

## Value — PASS

The exact minimum projection constant is a natural functional-analytic invariant of a canonical graph's cycle subspace in the weighted edge space. The theorem simultaneously resolves every page count and continuous spine-length deformation, detects a genuine sharp transition \(m(2-t)=4\), and proves an unexpected finite-page saturation at unit lengths: \(9/7,27/19,3/2,3/2,\ldots\). The spanning-edge coupling makes this a first non-cactus shared-cycle calculation, rather than the direct product of independent cycle projections. The quantity is specifically motivated by the cycle-space quotient model and complementability questions from the primary papers, not by an arbitrary isolated numerical example.

## Scientific limits

The scalar field is real. The exact optimal constant refers to the stated weighted edge \(\ell_1\)-presentation; at \(t=2\) the hub edge becomes metrically redundant but is retained in the operator's domain. No statement is made for general unequal spokes, other graph families, or the optimal complementary projection. Novelty remains subject to independent bibliographic confirmation.

Self-review: passed. Independent audit: not yet performed.
