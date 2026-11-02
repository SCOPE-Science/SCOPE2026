# Self-review

## Correctness — PASS

The claim concerns all finite all-edge subdivisions of complete bipartite graphs, not general subdivided graphs. Reconstructing every distance type gives the orbit decomposition into row, column, doubly centered, and two-dimensional class-constant sectors. The row and column exponential-distance blocks have positive first minors and determinant \((1-q^2)^2(1+(n-1)q^4)\) or its transposed analogue; the doubly centered sector has eigenvalue \((1-q^2)^2\). A Bernstein integral therefore establishes strict powered-distance negativity outside the global sector for every \(0<p<1\). Explicit summation produces the global matrix \(H(p)\). Its balanced critical value is negative semidefinite by strict concavity, and the unequal case has a unique determinant zero before the known biclique cap. The uniqueness argument uses the strict-interior negative-type property, which is also proved directly from Schoenberg kernels. The endpoint nullity and fixed-part implicit-function expansion are explicitly derived. The included independent graph-BFS checker replayed with 86 assertion groups; it does not replace the full proof. For \((2,2)\), separate analysis correctly yields the eight-cycle's three-dimensional endpoint nullspace.

## Originality — PASS, with historical-priority risk

Compared statements, not mere titles: Sánchez (arXiv:1108.0451, Sections 2–3) gives the original biclique exponent and a generic finite-metric test, but no all-edge subdivision computation. Lou, Obata and Huang (arXiv:2001.06752, introduction and Sections 3–5) give \(p=1\) embedding constants for joins and graph operations, not the present powered-distance family. Młotkowski, Skrzypczyk and Wojtylak (arXiv:2409.17662, Sections 0–2, 4 and 8) treat deleted-matchings and three-path theta graphs and do not state or imply the incidence-graph determinant or its fixed-part asymptotics. Searches for incidence/subdivision/negative type and relevant published mathematical records found no directly covering statement. The proof does not claim priority over general negative-type theory or the known eight-cycle boundary. Risk: an earlier theorem under a different term for the full incidence subdivision might imply this special formula; indexed searches do not rule out that possibility.

## Mathematical value — PASS

The objects are a canonical two-parameter subdivision of bicliques and their natural sharp Hilbert-snowflake exponents. The balanced/unbalanced dichotomy is not a mere parameter substitution: full subdivision is exactly exponent-neutral in every balanced biclique but exponent-reducing for every unbalanced one. Moreover a fixed original part yields a vanishing exponent with a sharp \(1/n\) law, contrasting with the positive limiting exponent of the unsubdivided metric. The exact all-parameter classification, endpoint embedding dimensions, and asymptotic constant are useful quantitative constraints for incidence-graph Hilbert embeddings. The scope expressly excludes partial subdivisions, weighted lengths, and general incidence systems.

## Closest literature and residual limitation

Primary closest source: Młotkowski–Skrzypczyk–Wojtylak, arXiv:2409.17662 (first posted 2024-09-26), which gives ordinary \(p=1\) QE results for edge deletion and theta graphs, not the full subdivision metric. The baseline theorem of Sánchez, arXiv:1108.0451, is fully credited. The fixed-part asymptotic is derived analytically rather than extrapolated from finite experiments. Independent scholarly refereeing and independent mathematical validation have not been performed.

Self-review: passed. Independent audit: not yet performed.
