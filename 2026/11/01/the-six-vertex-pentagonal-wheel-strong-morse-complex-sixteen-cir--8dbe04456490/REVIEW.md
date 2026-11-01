# Scientific review

## Correctness — PASS
The input is the unfilled one-dimensional pentagonal wheel. The defining strong-matching rule in the source [1, §§3–4] reduces, in a graph, to pairing a vertex with its unique preceding neighbor. All \(720\) orders are checked by two implementations, giving \(81\) generated matchings, \(45\) facets and face vector \((20,55,20)\). The exact twenty-pair certificate removes all triangles by verified elementary collapses, leaving a connected graph with \(20\) vertices and \(35\) edges. Thus the integral wedge of sixteen circles follows. The signed chain traces are recomputed for all ten dihedral symmetries; the Lefschetz identity and rational character comparison prove the representation formula. The verifier was executed from the supplied standalone files.

## Originality — PASS, residual uncertainty recorded
The closest original paper is Knudson–Owens–White [1]. Relevant full-text sections include the filtration definition, classified families and complete-graph/disjoint-union results; these do not include the pentagonal wheel. A published indexed calculation for **ordinary** wheel discrete-Morse complexes was examined in full and proves a distinct statement about \(\mathcal M(W)\), rather than \(\mathcal{SM}(W)\). A five-vertex wheel ordinary Morse calculation also concerns a different graph and different complex. Targeted published-finding corpus and literature searches for wheel aliases, strong matchings, homology and symmetry did not reveal an equivalent or stronger assertion. This is not an exhaustive guarantee: unindexed equivalent calculations remain possible.

## Mathematical value — PASS
This is the smallest noncomplete **odd-rim wheel**, a canonical dense graph with a universal vertex and five-cycle rim, outside the existing strong-Morse graph-family classifications. The full integral homotopy calculation distinguishes the strong complex from the very different ordinary wheel Morse complex; the nontrivial \(D_5\) representation detects vanishing global invariant homology despite sixteen loop classes. The explicit collapse and full symmetry character provide a reproducible benchmark for wheel-family investigations. No claim of an entire-wheel recurrence is made.

## Closest literature and limitations
[1] K. P. Knudson and A. Owens–White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844v1, §§3–4, 6–10. [2] *Dihedral top homology of wheel discrete-Morse complexes*, public published-finding corpus mathematical research record (2026), ordinary rather than strong complex. [3] *The five-vertex wheel Morse complex is a wedge of 64 three-spheres*, public published-finding corpus record (2026), smaller ordinary complex. Exact \(\mathbb Z[D_5]\)-module is not determined, and the result does not extend to other rim lengths. The collapse is not equivariant. No independent proof audit has been performed.

Self-review: passed. Independent audit: not yet performed.
