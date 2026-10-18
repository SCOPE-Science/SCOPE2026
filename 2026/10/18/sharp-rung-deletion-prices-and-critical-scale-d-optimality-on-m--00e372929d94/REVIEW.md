# Self-review

## Correctness — PASS

The final claim is the complete D-optimal conductance-allocation rule for the priced Möbius ladder, together with its fixed-price and linearly scaling-price limits. The proof treats the whole independent-edge budget simplex: injectivity of individual weights into the reduced Laplacian makes the log determinant strictly concave wherever the network is connected, while graph rotations force a two-orbit optimizer. Fourier eigenvalues and a Chebyshev root product give the exact spanning-tree enumerator. Its one-sided derivative at zero gives the support threshold \(t_c(n)=n^2/(2n-1)\); strict concavity settles uniqueness and the critical equality case. The hyperbolic stationary equation and sign bracketing prove the two asymptotic regimes and the limiting determinant gain. Exact rational matrix cofactors for 72 parameter triples and numerical scaling checks are supplementary, not infinite proofs. There are no unproved graph families or assumed algebraic root certifications.

## Originality — PASS, subject to historical uncertainty

The closest inspected primary sources are Bailey–Cameron, arXiv:1111.3768 (2011), on D-optimal graph-based block designs including a fixed, unweighted eight-vertex Möbius ladder, and Khosoussi–Sukhatme–Huang–Dissanayake, arXiv:1604.01116 (2016), on weighted spanning-tree design and discrete edge selection. An additional graph-enumeration reference by Daoud–Mohamed (DOI:10.1016/j.jtusci.2013.08.002) concerns spanning-tree counts of special graph families. None of the materially inspected passages establishes the exact independent-edge priced allocation or both asymptotic regimes. The matrix-tree theorem, Chebyshev identity, symmetry, and concavity are established tools; their individual statements are not asserted as original. Search non-hits do not prove historical novelty. An earlier optimization treatment hidden in the wider D-optimal design literature remains possible.

## Value — PASS

Optimizing the determinant is a natural D-optimality and tree-connectivity criterion rather than an arbitrary graph statistic. The theorem is global over independent edge weights for every ladder size and every positive price; it identifies exactly when a whole edge orbit is optimally deleted. The critical price grows linearly with size, while a price proportional to size exhibits a nontrivial hyperbolic crossover and an explicit strictly positive determinant advantage. At equal prices, the asymptotic optimal rung spending fraction is \(1/4\), rather than the \(1/3\) share of uniform edge weights. These are actionable structural distinctions, not just an isolated numerical example.

## Scope, evidence, and unresolved limits

The formal object is a two-price undirected Möbius ladder, not a general network or a stochastic reliability model. The exact matrix-tree and eigenvalue arguments prove the finite and asymptotic statements; the executable checker tests their concrete algebraic instances. The strongest overlap risk is an unlocated prior application of classical design theory to this specific two-orbit continuous-budget model. The scientific result has not undergone independent review.

Self-review: passed. Independent audit: not yet performed.
