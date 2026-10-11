# Review of the book-graph enclosing-ellipsoid theorem

## Correctness (C): PASS
A normalized covariance of the signed graph edge roots has three rigorously derived eigenvalues. The two edge orbit leverages are \(R_{\mathrm{spoke}}=1/(2w)+1/[2(mw+2v)]\) and \(R_{\mathrm{hub}}=2/(mw+2v)\). The proposed weights sum to one and put all root vertices within the ellipsoid, with exact equality/strictness as claimed. Averaging the two signs of any root for a general off-center competitor and then applying arithmetic–geometric mean to the covariance certificate establishes minimum volume and uniquely forces the competitor's center and shape. The volume ratio, spectral multiplicities and all boundary cases \(m=2,3,4\) are evaluated explicitly. The exact rational checker passed every instance \(2\le m\le12\). Its scope is finite; the symbolic argument covers every integer \(m\ge2\).

## Originality (O): PASS, with a specific residual risk
The inspected graph-polytope papers of D'Alì–Delucchi–Michałek (arXiv:1910.05193), Chen–Davis–Korchevskaia (arXiv:2107.12315), and Mori–Mori–Ohsugi (arXiv:2312.11287) treat graph-root constructions, facets and join graphs, but do not state the computed book-graph enclosing ellipsoid. Suliman–Weinstein (arXiv:2302.05966) **does** already provide the general graph Laplacian, effective-resistance, infinity Lewis-weight and D-optimality equivalence; that general theory is prior work, not part of the novelty claim. The exact book-graph parameter evaluation, volume and invisibility threshold were compared under these equivalent formulations, and no covering calculation was located. An earlier exact optimal-design treatment of this family, not found in accessible searches, remains a genuine residual originality risk. A missing search hit is not a novelty proof.

## Value (V): PASS
The sharp edge-invisibility boundary distinguishes a natural one-parameter family of book graphs, not a contrived finite slice. For every \(m\ge3\), strict inclusion \(P(K_{2,m})\subsetneq P(B_m)\) leaves the unique minimum-volume enclosing ellipsoid invariant, although at \(m=3\) the new vertices still contact it and at \(m\ge4\) they lie strictly inside. This is paired with a complete all-dimensional quantitative metric answer and a nontrivial exceptional \(m=2\) volume ratio. It is a meaningful structural geometric boundary, not just a numerical test or a claim of general new ellipsoid theory.

## Limitations
The result is restricted to intrinsic Euclidean outer Löwner ellipsoids. The proof is mathematical; the finite exact checks are corroborative, and no external independent audit or claim of priority is made. The closest cross-disciplinary coverage risk is an unindexed exact infinity-Lewis-weight computation for book graphs.

Same-model review: passed. Independent audit: not yet performed.
