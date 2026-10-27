# Self-review

## Correctness — PASS

With the exact marked path fixed, deleting its edges is a bijection to forests rooted at every path vertex. The complete-graph Dirichlet Laplacian minor counts these forests as \(r n^{n-r-1}\). Removing an off-path leaf and removing an isolated marked endpoint give independent counting identities, not independence assumptions. Summing indicators proves the claimed conditional mean. Direct subtraction yields a positive-factor multiple of \(2(n-1)-r^2(r-1)\), whose monotonicity proves the mode/tie classification and the asymptotic cube-root scale. Boundaries \(n=3\), \(k=1\), and \(k=n-1\) are included. Exact Prüfer enumeration through eight vertices and rational algebra checks through 350 vertices passed; the analytical argument, not the finite checks, proves the full theorem.

## Originality — PASS on inspected evidence

The nearest published Cayley-tree result gives the conditional degree of a **single marked endpoint**, including its leaf probability, which is credited. That does not supply the \(n-r\) off-path vertex contributions or the global leaf-count regression. The 2020 distance-profile study considers asymptotic profiles and marking leaves/edges; the leaf-count martingale study gives a marginal CLT; Pitman provides the classical forest enumeration used in our proof. Exact-formula, alias, conditional-distance, and theorem-implication comparisons found no result covering the new cubic sign boundary. The strongest residual concern is a possibly implicit joint leaf-distance generating function not identified in the inspected literature. No independence or exhaustive priority verification is claimed.

## Value — PASS

The dependence of global leaf count on two marked vertices' separation is a natural structural observable in random trees. Despite the known monotonic increase of a marked endpoint's chance of being a leaf, the global conditional leaf expectation rises and then falls. The exact first-step increase for every \(n\ge4\), complete finite plateau classification, and maximizing separation of order \(n^{1/3}\) are motivated, nonarbitrary qualitative conclusions that describe behavior missed by marginal asymptotic results.

## Limits

Only expected unrooted leaf count for uniform labeled trees is claimed, not a distributional stochastic ordering, results for weighted tree models, or historical-priority certification. Independent scientific verification remains outstanding.

Self-review: passed. Independent audit: not yet performed.
