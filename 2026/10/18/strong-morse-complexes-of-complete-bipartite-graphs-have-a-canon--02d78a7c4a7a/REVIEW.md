# Scientific review: strong Morse complexes of complete bipartite graphs

## Correctness — PASS

The claim concerns the full vertex-filtration-generated complex on the **one-dimensional** graph \(K_{m,n}\), \(m,n\geq2\). The key combinatorial point is exact: because descending links are discrete, a graph vertex is paired precisely when it has one earlier neighbor. The first and second appearances of the two sides force every gradient into one of the displayed side-centered star subcomplexes. All generating facets are independently shown to arise from explicit orders, proving equality of complexes rather than a one-way containment.

Every cover piece is contractible by eliminating its outward wing vertices; every cross-side intersection contains exactly two isolated incidence vertices; same-side and triple intersections are empty. A cofibration-based graph-of-spaces reduction establishes the full wedge-of-circles homotopy type. Its naturality yields the integral equivariant graph-cycle module, and the zero-row/column matrix argument yields the integral splitting and character. No unproved independence assumption or finite-to-infinite extrapolation is used.

The standalone verifier exhausts all vertex orders for seven graph sizes through \(K_{4,5}\), checks cover equality, calculates all mod-two boundary ranks, and tests 224 signed automorphism Lefschetz characters (including part exchange). It provides consistency checks; the uniform proof is separate.

## Originality — PASS, with residual risk

Primary full-text comparisons: Knudson--Owens-White, arXiv:2609.06844v1, Definition 4.2 and Sections 7 and 10; Fernández, arXiv:2504.15729, theoretical framework. Knudson--Owens-White prove contractibility of strong complexes of stars and describe paths, cycles, simplices, complete graphs and disjoint unions; they do not state the two-nontrivial-part classification or its integral automorphism module. The ordinary Chari--Joswig Morse complex is a distinct, generally larger object. Closely indexed ordinary-bipartite Morse findings likewise concern that other object.

The already documented thin family \(K_{2,n}\) is a genuine special case, so originality is specifically the unrestricted two-parameter family, particularly \(m,n\geq3\), and the natural doubled-edge cycle-module description. Searches for strong matchings, bicliques, vertex filtrations, bipartite graph homotopy, and the numerical formula returned no equivalent broader theorem. Search failure alone is not proof of uniqueness; unindexed overlap remains the principal risk.

## Mathematical value — PASS

The complete bipartite graphs form a canonical two-parameter family, with their full strong Morse complexes having unbounded simplicial dimension but always one-dimensional homotopy. The global gluing creates \(mn\) backtracking generators alongside \((m-1)(n-1)\) ordinary bipartite cycle generators. The natural integral symmetry module distinguishes this classification from a Betti-number table and provides exact characters for all graph automorphisms. It is a natural complete classification, not a selected numerical example or a renaming of the star result.

## Boundaries

There is no claim about the pure strong complex, arbitrary bipartite graphs, ordinary Morse matchings or higher-dimensional flag complexes. The partition-preserving integral direct-sum decomposition need not respect part-exchanging automorphisms; the full-group kernel presentation does. The report is not independently audited, and bibliographic risk is not zero.

Self-review: passed. Independent audit: not yet performed.
