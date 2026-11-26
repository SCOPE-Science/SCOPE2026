# Independent mathematical audit

## correctness

PASS

In the ordered pair list, the only possible inconsistency lies between the retained neighbors of the deletion. A mismatch forces that position and the unique missing pair, including the boundary cases because both anchor pairs are retained. If there is no mismatch, a constant pair was removed and the shortened padded word y has fixed endpoints a,b. Expanding each distinct run of y once gives a distinct parent, including for a single run containing both endpoints. Two distinct parents of a common output therefore have the same reduced itinerary and positive run lengths differing by a unit transfer. Conversely a transfer gives the common coordinatewise minimum, and transferring surplus to the first part proves connectivity. Stars-and-bars counts vertices and donor choices; each oriented edge has one donor and target, yielding the claimed undirected edge count. The off-diagonal-ones adjacency matrix counts reduced itineraries, with eigenvalues q−1 and −1, proving W_k and the histogram. As a separate check on total edges, two distinct confusable parents share a unique output, specified by their minimum run vector; the total is thus the sum over shorter y of binomial(number of runs of y,2). The run count is one plus the number of transitions among the n edges of y. For n>=3, any one or two selected edges form a forest not connecting both fixed endpoints. Under a uniformly chosen interior word, each selected edge changes with probability (q−1)/q, independently for the selected pair: sequentially choose symbols along each forest component rooted at its fixed endpoint, if any. The resulting sum is q^(n−1)[n(q−1)/q+binomial(n,2)((q−1)/q)^2], exactly the parameter formula. For n=1 the single y gives 0 or 1 edge; for n=2 equal endpoints give q−1 shorter words with two transitions and unequal endpoints give two words with one transition and q−2 with two, yielding both exceptions. The count of inconsistent outputs follows by summing nonconstant interior read incidences, with uniqueness as above. The recorded 270 finite checks in CHECK.out and the supplied checker were inspected, not executed.

## originality

PASS

The anchored model, constant-run shortening, zero-deletion equivalence and local consistency reconstruction are prior or covered by other exact treatments. The distinct supported contribution is the exhaustive anchored graph and output census: connected run-composition components with exact vertex and edge counts, the global boundary-independent edge law from n=3 with its exact exceptions, and the boundary-conditioned histogram accompanying the graph. The closest unpadded inverse-list result gives the per-output reconstruction mechanism under the anchoring restriction, but not the anchored graph classification and global edge law. No priority is inferred from catalogue dates.

## value

PASS

This is an exact finite-alphabet classification for a standard local-read deletion model, not a code-bound recomputation. It identifies what can be confusable and how such classes connect, and quantifies both overlap between distinct inputs and ambiguity of received vectors. The threshold for edge-count independence from boundary symbols, while the list histogram can still depend on them, is useful information not supplied by the zero-deletion equivalence alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
