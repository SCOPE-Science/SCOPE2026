# Review of the priced book-network resistance allocation

## Correctness — PASS

The claim is a global theorem over every integer \(m\ge2\), \(S,R,B>0\) and independent nonnegative edge conductances. The proof checks feasibility and connectivity, strict matrix-inverse trace convexity, the injective edge-to-Laplacian map, unique symmetry reduction, all nonzero eigenvalues and their multiplicities, and an exact strictly convex scalar derivative with its one-sided boundary condition. The reported radical formula has positive denominators precisely in the interior case. Equality \(R=R_c\) is included in the deleted regime. Exact-rational and unrestricted numerical tests from the included verifier were executed and passed; these are corroboration, not proof.

## Originality — PASS, qualified

The complete 2008 Ghosh–Boyd–Saberi PDF was inspected in its introductory formulation and analytical graph-family sections (trees, wheels and barbells); the accessible 2006 proceedings paper was also inspected. Their general strict-convexity/symmetry methods imply that the present optimization is tractable but do not state the specific budget-price transition. A later graph-join result gives fixed-weight resistance information rather than optimization; available coverage was partial. Database searches for shortcut deletion, Kirchhoff minimization, \(K_2\)-join graphs, and equivalent parallel two-edge routes did not reveal a theorem implying the stated threshold. A distinct priced book-network log-determinant problem optimizes a different spectral functional and cannot imply this trace-pseudoinverse threshold. Residual risk: unindexed or inaccessible specialized electrical-network design sources might contain a stronger equivalent formulation.

## Value — PASS

The result is a natural complete classification of the direct-connection support on a network family with overlapping cycles, together with exact globally optimal conductances, minimum objective and a nontrivial \(m^{-2}\) price scale. The equal-price two-page versus three-page transition is operationally clear, and the analysis distinguishes total-resistance minimization from other spectral design objectives. The endpoint asymptotics quantify how a cheaply supplied shortcut can have diverging conductance while receiving vanishing expenditure. This is more informative than a numerical SDP solution or an arbitrary finite evaluation.

## Limits and closest literature

The result requires the two spoke families to share a single price and restricts the graph to a book. Independently published absolute priority has not been established. See the cited Ghosh–Boyd–Saberi works and the graph-join comparison in `RESULT.md`; the accompanying originality checks record their different logical coverage.

Self-review: passed. Independent audit: not yet performed.
