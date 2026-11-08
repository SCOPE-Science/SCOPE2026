# Independent mathematical audit

## correctness

PASS

For labeled simple cycles C_n,n>=4, maximal independent sets have clockwise gaps exclusively 2 or 3: independence gives min2, domination max3. Any one-deletion/one-insertion preserving maximal independence must insert adjacent to deleted token (otherwise it remains undominated); gap moves swap adjacent (2,3). With a=3k-n,b=n-2k,a+b=k, anchored circular 2/3 words count n/k*C(k,a) configurations, each has degree twice number r of alternating run-pairs, giving multiplicity n/r*C(a-1,r-1)C(b-1,r-1) and edges n*C(k-2,a-1) from Vandermonde. Adjacent gap swaps while fixing one token then shifting token by 1 proves each mixed sector connected. Pure n=2k,3k sectors have exactly 2,3 isolates. Sum yields component and global coefficient formulas. Independent all-subsets exchange graph brute force n=4..14 corroborates exact distributions and components; source independent gap verifier also inspected, but finite tests do not replace the all-n proof. Five Git tree identities independently reconstructed.

## originality

PASS

Best-of-knowledge distinct combined claim survives comparison with actual relevant sources; precisely prior components are credited, and inaccessible or possibly dominating material is named as a priority risk, not treated as proof of noncoverage. The all-k connectivity, pure sector count, and unbounded degree spectrum are not direct corollaries of the stated prior minimum-only theorems.

## value

PASS

The exact all-cardinality component classification and complete degree distribution are natural invariants of the reconfiguration graph of maximal independent sets, including nonminimal sectors with unbounded local degrees. This substantially extends the minimum-cardinality-only i-graphs description.

The dated certificate retains the supplied scientific assessment, sources and limitations.
