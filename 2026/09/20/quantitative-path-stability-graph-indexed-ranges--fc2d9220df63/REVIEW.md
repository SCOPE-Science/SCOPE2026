# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

PASS. The argument uses Zhu's stated Proposition 3.3, parity-error bounds, auxiliary rank-surplus estimates, induction inequality, and lazy contraction identity as prior inputs. The new standard stability extraction was checked separately in the branching and cycle cases. A degree-at-least-three vertex creates an auxiliary triangle and hence a rank surplus at least 1/4; combined with the source parity bound and the elementary lower bound on J_d this gives a uniform order-n^{-1/2} loss. If maximum degree is at most two, a connected bipartite nonpath is an even cycle; its auxiliary zero-edge law can be evaluated exactly, giving rank surplus at least 2/5. The C4 boundary case is handled directly.

The proposed sharpness family is a path whose last vertex is split into two leaves. Direct conditioning on the last two Rademacher increments gives the exact gap one half times the probability that a simple-walk maximum equals one. Reflection and Stirling then give the n^{-1/2} asymptotic. The identity was also exhaustively checked for small n.

For the lazy model, the cyclic gap follows directly from Zhu's explicit p=2/3 margin and the same lower bound for J_d. For a nonpath tree, three fixed incident edges are simultaneously nonzero with probability 8/27; on that event zero-edge contraction retains a branching vertex, so the standard stability theorem applies to the quotient. On all other events the source standard extremal theorem keeps the integrand nonnegative. This yields the stated 2/(405 sqrt(n)) tree gap.

Potential failure modes checked include the d versus n conversion, the special C4 auxiliary weight, the all-zero rank correction on an auxiliary cycle, and the possibility that zero-edge contraction merges distinct branches of a tree. The latter cannot occur without an alternative path in the original tree.

## Originality

PASS, to the best of our knowledge, with a material residual risk from older tree-specific literature.

The expected-range inequalities are prior art: Wu--Xu--Zhu prove them for trees; Bok--Nešetřil treat unicyclic graphs; Berger--Ji--Metz prove full lazy stochastic domination for trees and partial standard distributional results; Zhu proves the expectation theorem for all connected bipartite graphs and the lazy corollary for all connected graphs. The auxiliary graph, rank-surplus machinery, parity envelope, and zero-edge contraction identities used here are explicitly treated as Zhu's ingredients.

Targeted searches for quantitative stability, strict path maximality with an explicit size-dependent gap, and equivalent tree-indexed range formulations did not locate the claimed universal 1/(60 sqrt(n)) standard bound, its sharp n^{-1/2} fork witness, or the stated lazy quantitative bounds. The principal residual risk is Wu--Xu--Zhu (2016): its accessible abstract confirms the tree theorem, but the complete text could not be inspected during this review. Because that work uses tree transformations, it is the source most likely to contain a quantitative tree inequality under different notation. Special-class formulas in Bok--Nešetřil and stochastic domination in Berger--Ji--Metz also limit any claim about qualitative strictness. Accordingly, the originality claim is restricted to the dimension-explicit stability statements and sharp standard order, not to path extremality or generic strictness.

## Value

PASS. The result converts a newly proved extremal inequality into a stability theorem, distinguishes the scale at which near-extremizers can approach the path, and supplies an explicit family showing that the standard exponent cannot be improved. The lazy tree transfer also shows that quantitative standard stability persists through random zero-edge contraction. These statements sharpen the structural interpretation of the path extremizer without attempting the still-stronger distributional conjecture.

## Limitations

The constants are not optimized. The universal lazy n^{-3/2} exponent is not proved sharp and may be improvable, especially for cyclic graphs. The proof depends on the correctness of specific lemmas in the recent Zhu preprint rather than reproving them from first principles. The result concerns expected range only. The full Wu--Xu--Zhu 2016 text was not inspected, leaving residual originality uncertainty for tree-specific quantitative refinements.
