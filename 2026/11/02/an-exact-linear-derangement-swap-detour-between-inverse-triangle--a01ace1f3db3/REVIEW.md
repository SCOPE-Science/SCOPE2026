# Independent mathematical audit

## correctness

PASS

For n=3k (k>=2), perfect matchings in a crown graph are derangements; legal alternating four-cycle switches swap two positions without creating fixed points. With target tau=sigma^{-1}, relative permutation pi^{-1}tau changes by a transposition; its cycle count must increase from k to 3k, so length =2k+2m where m is number of cycle mergers. First use of an untouched forward 3-cycle must swap with a different block (every internal swap makes a fixed point), hence first interaction merges two distinct relative cycles; each merger can first touch at most two untouched blocks, proving m>=ceil(k/2). The explicit 6-move template on two 3-blocks and 10-move template on three blocks, then disjoint-block assembly, attain equality: distance 3k (even k), 3k+1 (odd k); k=1 is disconnected. Independently applied the given templates to all k=2..20 and checked no fixed points at any step, endpoints and move count, while the universal lower bound is structural and not merely computational.

## originality

PASS

Best-of-knowledge priority comparison on the exact final statement, allowing explicit inaccessible-primary-source risks; known related first-moment, connectivity, single-class and one/two-factor theorems are acknowledged as prior, not claimed new.

## value

PASS

Natural exact metric obstruction for local four-cycle reconfiguration of crown perfect matchings: the distance between explicit inverse products differs from the ambient transposition distance 2k by a linear, unbounded penalty. Gives a sharp witness family beyond previously known connectivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
