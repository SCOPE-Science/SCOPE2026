# Independent mathematical audit

## correctness

PASS

A distinct-window orbit gives a closed trail. Across the cut by whether a vertex begins with a nonzero symbol, every bad edge goes U to B, and cyclic rotation bijects good U-to-B edges with all B-to-U edges. Thus each used bad edge costs an omitted good U-to-B edge, proving the bound tr(A^n). For attainment, each good-edge vertex has equal incoming and outgoing symbol options, and appending zeros gives paths to the all-zero vertex, from which any admissible vertex can be built. Its Euler circuit is primitive by distinct windows. The trace count exceeds the number of linear (n−1)-words: the differences start with q,q at n=2,3 and satisfy the same positive recurrence. This proves the exact gap r^(n−1). For the all-maximizer claim the frozen cylinder proof explicitly handles only Euler witnesses; the needed equality case follows as follows. At equality all good edges outside U-to-B must be present. Relative to the complete good-edge graph, a maximizing trail therefore changes only U-to-B edges. Outdegrees of all B vertices are unchanged, hence by balance their indegrees are unchanged. But added bad edges end at B vertices ending in a nonzero symbol, and omitted good U-to-B edges end only at vertices ending in zero. No addition can be balanced there. Thus every maximizer uses all and only good edges (also for n=2, when bad edges are absent). This supplies the missing inference without changing the claim. For any large orbit with longest common prefix L, the finite bound at n=L+1 gives the content upper bound lambda+tau^(L+1)/lambda^L, and L tends to infinity uniformly with orbit size. The Euler orbits give the matching limit; changing the exponent multiplies by a power of the gap and gives zero above s and infinity below it. Fixing k−1 transitions of a closed n-walk gives exactly the stated matrix entry. The positive and negative eigenvectors yield the Parry cylinder masses and spectral correction, with beta<alpha; q=2 gives alpha=2/3 and beta=1/3 as claimed.

## originality

PASS

The periodic-content framework and existence of restricted universal cycles are covered prior art. The supported distinction is the finite upper bound over the full admissible window graph and its rigidity at equality, yielding the exact critical content and quantitative cylinder law. The spectral evaluation after the window set is identified is standard matrix counting.

## value

PASS

This natural constrained shift tests how much periodic separation is lost relative to counting all linear words: arbitrary optimizing words may try to gain windows by using nonclosing edges, and the cut proves there is no gain. The exact content gives a normalized metric benchmark beyond the dimension alone. The forced window set and nonzero alternating Parry discrepancy give additional information on exactly extremal orbits without dependence on the Euler circuit chosen.

The dated certificate retains the supplied scientific assessment, sources and limitations.
