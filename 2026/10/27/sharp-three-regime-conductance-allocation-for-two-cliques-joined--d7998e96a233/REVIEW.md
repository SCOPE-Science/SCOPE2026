# Mathematical review

## Correctness (C) — PASS

The proof is exact for integers \(k\ge2\), \(m\ge1\), and \(B>0\). Concavity of the second Laplacian eigenvalue permits symmetrization without weakening the optimum. The invariant spectrum decomposes into the antisymmetric orbit-constant two-by-two block, the symmetric orbit-constant block, gateway transversals and nongateway transversals. The gap-one inequalities are necessary and sufficient. Minimizing their linear costs reduces to a single strictly convex scalar function, giving the three claimed regimes. Numerical finite tests check matrix eigenvalues and accounting but are not used as the general proof. A remaining review risk is an unnoticed boundary or multiplicity error; the proof explicitly handles \(m=1\) as the empty nongateway-transversal case.

## Originality (O) — PASS, subject to specialist literature risk

Sun, Boyd, Xiao, and Diaconis (2006) establish continuous-time rate-budget optimization and a geometric dual, while Göring, Helmberg, and Wappler (2005) establish general absolute-algebraic-connectivity theory. Both provide general methods but no identified evaluated formula for this partial-matching two-clique family. The 2009 symmetry paper concerns discrete-time SLEM; Shakeri and coauthors (2015) optimize only interlayer weights with intralayer Laplacians held fixed. Related published work on overlapping unions of two cliques uses a different discrete-time objective. An entire potentially relevant 2011 article was not accessible; absence of coverage there has **not** been certified. The all-parameter budget and support formulas were checked for implication, not just title match. No conclusion of global uniqueness of research findings is drawn from search failure.

## Mathematical value (V) — PASS

The same budget has three distinct exact allocation regimes indexed by \(k/m\), including a strict gateway–gateway edge-activation threshold and an all-optima theorem forcing nongateway edges unused. These classify resource allocation in a natural multi-bridge community topology; they are not routine normalization or a single numeric small graph.

## Residual scientific limits

The theorem covers equal-sized cliques connected by a nonempty *partial matching* with at least two links. It makes no assertion for a single bridge, a full matching, arbitrary intercommunity connections, or fixed intracluster conductances. The public numerical code uses floating-point checks; analytic equalities and inequalities constitute the infinite proof. Specialist literature may contain an equivalent exact classification, particularly in unavailable full texts.

Self-review: passed. Independent audit: not yet performed.
