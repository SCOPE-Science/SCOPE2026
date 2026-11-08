# Independent mathematical audit

## correctness

PASS

Enumerating involutions by fixing/swapping the least unused position and filtering all 321 triples is exhaustive; the comparison mask maps permutations injectively, and counts match binom(n,floor(n/2)). Exact VC search adds query supports in strictly increasing order and keeps all nonempty pattern fibers, pruning only unsplittable singletons. Exact online recurrence for version spaces splits on all comparison pairs, with sound cardinality pruning; the source traverses every n<=12. Independently reconstructed sorted 321-avoiding involutions from scratch at n11 and n12 and validated the actual Git JSON tree certificates: depth7 at n11, 127 internal queries and 128 distinct valid path witnesses; depth8 at n12, 255 queries and 256 distinct valid witnesses. Independently evaluated every query minority split, maxima 126 at n11 and 252 at n12, strictly below 128 and 256 needed for deeper trees, proving critical Ldim upper bounds. Full finite claims only n<=12; no extrapolation.

## originality

PASS

The central binomial counts for 321-avoiding involutions are known (Fang–Hamaker–Troyka and earlier tableau bijections), as are general Littlestone/VC theory. Those results do not determine the two dimensions under the specific positional-comparison query model. The first n11 two-unit adaptive/static gap and complete n1..12 table were not found covered, but alternate tableaux/ballot-path coding of comparisons is a priority risk.

## value

PASS

Identifies a sharp first discrepancy between static VC and adaptive mistake-tree complexity for a natural Catalan-related pattern-avoidance class represented by positional comparisons. Exact finite dimension thresholds require both an exhaustive static shattering search and independently checkable adaptive certificates; this is a motivated natural classification, not an arbitrary tiny sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
