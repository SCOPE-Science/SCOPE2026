# Independent mathematical audit

## correctness

PASS

For all integers 2<=a<=b<=c, read proof: no single geodesic can span a+b+c-1 vertices because diameter<=floor((b+c)/2); an A-arm and two opposite-hub B/C geodesics cover the graph with three. With two geodesics, the diameter bound limits their overlap to <=3-a<=1, excluding a>=4. Hub and exclusive-arm cases force a+b<=6, and the shared-arm geodesic inequalities force even c for (a,b)=(2,4) and odd c for (3,3); (2,2),(2,3) unrestricted. Exact two-path construction covers all asserted cases. Independently wrote graph BFS/all-geodesic-set search (not packaged verifier) and confirmed the theorem for 84 triples; this finite check supports, but does not prove, the unlimited claim.

## originality

PASS

On best-of-knowledge available primary texts, the exact theta vertex-isometric COVER minimum (2 vs 3 for all 3-arm lengths, parity included) is not already implied by general complexity, partition bounds, general-position or pathwidth results. Full specialist Manuel 2021 text uninspected; historical duplication possible.

## value

PASS

An exact all-length classification on the natural minimal noncactus 2-connected series-parallel graph family resolves when two geodesics suffice, including two infinite parity-dependent exceptions, a motivated structural gap beyond bounded-width general algorithms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
