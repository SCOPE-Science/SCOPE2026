# Self-review

## Correctness

**PASS.** In a proper coloring of a complete multipartite graph, each color is confined to one part. If part \(i\) uses \(c_i\) colors and \(q\) colors are used in total, every vertex in that part totally dominates exactly the \(q-c_i\) color classes supported on other parts. Hence the \(k\)-tuple condition is exactly \(q-c_i\ge k\) for every \(i\). This gives the feasibility boundary \(k\le N-L\), and after writing \(t=q-k\), the optimization is exactly \(r\le k+t\le\sum_i\min\{n_i,t\}\). The converse construction realizes every admissible optimal color-count vector. The labeled counting formula follows from allocating colors to parts and using Stirling numbers to count surjections. The packaged checker verifies the minimum and enumerator independently on exhaustive small instances.

## Originality

**PASS.** The recent Beggas–Marweni paper defines and studies the general \(k\)-tuple total dominator chromatic number, but its accessible abstract advertises general bounds, corona products, edge-corona products, and graph modifications rather than a complete-multipartite classification. Targeted database and web searches using the general name, the abbreviation kTD, the older double-total-dominator specialization, complete-bipartite and complete-multipartite aliases, and the exact biclique value \(2k\) found no statement implying the all-parameter water-filling formula or optimal-coloring enumeration. The \(k=1\) specialization is explicitly treated as prior-known. The main residual risk is that the inaccessible body of the 2025 initiating article could contain a complete-multipartite result not visible in its abstract or indexing.

## Value

**PASS.** The result gives a complete existence, optimization, structural, and enumerative classification on a canonical graph family for a recent multi-class domination-coloring invariant. It covers all part-size profiles and all feasible \(k\), exposes a sharp minimum-degree boundary, and reduces the parameter to a one-dimensional threshold. The exact biclique law \(2k\) and the count of all optimizers are useful corollaries rather than isolated finite cases.

## Closest literature and limitations

The closest source is Beggas–Marweni, DOI 10.1007/s40314-025-03466-7, whose abstract defines the same invariant and reports general bounds and graph-operation results. Beggas–Kheddouci–Marweni, DOI 10.1142/S1793830921501548, treats the \(k=2\) specialization, while Kazemi, DOI 10.22108/TOC.2015.6171, is foundational for \(k=1\). The accepted claim is the arbitrary-\(k\) complete-multipartite classification and enumeration; it does not claim novelty for these definitions or the \(k=1\) special case. The principal limitation in the originality review is incomplete access to the initiating article's body.

Self-review: passed. Independent audit: not yet performed.
