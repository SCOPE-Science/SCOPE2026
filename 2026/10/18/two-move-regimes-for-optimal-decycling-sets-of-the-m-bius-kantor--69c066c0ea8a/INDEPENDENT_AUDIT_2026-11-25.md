# Independent mathematical audit

## correctness

PASS

For a size-k deletion S the retained graph has 24−3k+e(S) edges. For k≤4 the retained vertex set is nonempty and the forest bound gives 2k−e(S)≥9, impossible. The displayed five-set leaves a tree; at size five every forest has 2−e(S) components, so only e(S)=0,1 occur. A fresh implementation used leaf stripping to enumerate every five-set, then tested all unordered pairs by intersection size four and, for slides, adjacency of the two differing vertices. It obtained 672 sets (192 with no internal edge, 480 with one), and matched the certificate's literal ordered state and edge lists. All-pairs unweighted shortest paths gave finite distances everywhere: jump has 5664 edges, degrees 13:96, 15:336, 17:48, 19:96, 25:96, and eccentricity 5 at every root; slide has 1848 edges, degrees 4:288, 5:144, 6:96, 7:48, 9:48, 10:48, and eccentricities 7:96, 8:560, 9:16. Both pair-distance histograms, both SHA-256 fingerprints, and the length and minimality of the certified two diameter paths were checked independently. Replay: python3 /workspace/branches/independent_mk.py (NumPy/SciPy); output independent_mk.out in the same directory. The fingerprint encoding is in fact a compact object with keys states and edges holding the two arrays. The proof's crude forest bound is used only for nonempty retained sets; neither this restriction nor the serialization gloss changes a Finding claim. No larger graph, temporary size changes, or weighted moves are tested.

## originality

PASS

The scalar decycling number five is not an originality claim. No inspected statement or indexed table establishes the full optimum census together with these two exact exchange graphs and their metrics. The nearest forest-exchange method fixes side cardinalities and cannot imply the result for either of these move rules. This judgment is specific to the evaluated classification and is not priority certification.

## value

PASS

The natural choice between unconstrained relocation and adjacency-only relocation leaves reachability intact on a standard symmetric cubic graph, but changes eccentricity from uniform 5 to three strata with radius 7 and diameter 9. Knowing the precise optimum state space and distinct distance costs is useful for benchmarking fixed-cardinality cycle-breaking dynamics; it is not a recomputation of the known optimum size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
