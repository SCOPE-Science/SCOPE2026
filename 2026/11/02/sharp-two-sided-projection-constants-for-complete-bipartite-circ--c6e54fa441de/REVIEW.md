# Scientific review: sharp biclique circulation projection constants

## Correctness — PASS

The claim is about real matrices with zero row and column sums, equivalently oriented circulations on an unweighted complete bipartite graph. Double centering is idempotent and fixes exactly the target. Averaging any competing projection under all independent row and column permutations cannot increase either its own norm or its complement norm, for any entrywise \(\ell_p\) exponent. Four stabilizer orbits, their zero row/column sum constraints, and the fact that the projection fixes circulations prove that double centering is the unique equivariant projection, completing the infinite-family optimality proof. Direct kernel coefficients establish the exact endpoint operator norms; rank-one witnesses establish the entire \(\ell_p\) factorization. The calculation covers \(m,n\ge2\), \(p\in[1,\infty]\), and proves the equality boundary and asymptotic claims. A separate exact rational checker validated 71 small full-matrix instances, but finite checks are not treated as exhaustive proof.

## Originality — PASS, qualified

Dilworth–Kutzarova–Ostrovskii (arXiv:1807.03814v1) has the nearest known \(K_{2,n}\) projection case; that boundary is explicitly excluded from the new-contribution claim. Their later cycle-space paper (arXiv:2305.12582v1) supplies the general invariant-projection method, with concrete results on discrete tori and Hamming graphs, but the inspected mathematical statements do not supply the arbitrary \(K_{m,n}\) formula or the simultaneously optimal complement norm. Related published finite-metric transportation results determine quotient-space Banach–Mazur distances or molecular-coordinate projection constants, not these two cycle-space projection constants. Actual checks included aliases such as doubly centered matrices, zero-row-and-column-sum kernels, cycle spaces of complete bipartite graphs, and minimal complementary projections. No directly covering result was identified. Residual risk: an unindexed matrix projection result could derive this family immediately under a different name; absence from search results is not proof of novelty.

## Mathematical value — PASS

Complete bipartite circulations are among the basic nontrivial graph-flow kernels, and projection constants quantify their complementability as subspaces of edge \(\ell_p\). Simultaneous optimality of projection and complement across **all** exponents is a structural theorem, not merely the norm of one chosen operator. The exact two-parameter endpoint constants produce two distinct limiting costs and a sharp integer threshold at \((3,4)\) separating which of the two operators is more expensive. The result classifies an infinite natural graph family; no conjectural extension or generic graph claim is needed to motivate these exact facts.

## Literature and residual limitations

The comparison is based on the inspected full texts of arXiv:1807.03814v1 and arXiv:2305.12582v1 and relevant published mathematical finding statements, alongside claim-level searches for equivalent row/column centering formulations. Prior findings involving complete bipartite transportation quotients and cactus molecular projections concern different subspaces or norms. Unindexed historical calculations remain possible. The theorem is for unweighted real complete bipartite edge spaces, not weighted networks or other bipartite graphs. Intermediate-exponent complementary norms are characterized by the explicit operator, not evaluated in elementary closed form.

Self-review: passed. Independent audit: not yet performed.
