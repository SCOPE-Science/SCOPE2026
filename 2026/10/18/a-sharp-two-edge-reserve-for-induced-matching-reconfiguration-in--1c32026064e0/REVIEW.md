# Independent mathematical audit

## correctness

PASS

The Pappus graph is the biaffine incidence graph with points (x,y), lines (m,b) over F_3 and incidence y=mx+b. An induced matching is an independent set in the conflict graph of its 27 graph edges. Increasing-edge-index recursion enumerates EVERY independent set, with counts (1,27,189,387,135,27,0) at cardinalities 0..6, so the maximum is five. Exactly 153 size-three matchings and 27 size-five matchings have no extension; all 135 size-four matchings have unique maximum extension. The reserve-four add/remove graph therefore has 27 isolated K_{1,5} components. For floor three, exhaustive BFS on 387+135+27=549 states and 675 transitions gives one 396-state component containing all 27 maxima and 153 isolated vertices. The exact certificate supplies explicit H->L(Pappus) permutation: H joins maximal matchings sharing three edges, has 54 edges and degree four, and every one of the 351 optimum pairs has d_TAR=4d_H. Exact distance spectrum: 54 at 4,108 at 8,162 at 12,27 at 16. Independently reconstructed F3 incidence, compatibility, all-size counts, BFS and a NetworkX L(P) isomorphism, not relying on logged VERIFY_OK. Exhaustiveness comes from enumerating all independent edge subsets, not from a search timeout.

## originality

PASS

Best-of-knowledge originality assessment of this EXACT final statement against published mathematical results and the source model, not certification of historical priority. General mathematical machinery and prior model definitions are attributed; claim-specific evaluated classification is not found among inspected primaries. A failed search is not novelty proof. Maximum-induced-matching complexity and FPT/reconfiguration tools could compute these properties after a dedicated finite calculation but do not logically imply a 27-star reserve-four graph or exact distance histogram. The certified enumeration supplies the missing finite object-specific theorem.

## value

PASS

The 18-vertex Pappus graph is a canonical cubic bipartite incidence graph. A sharp reserve threshold for connecting maximum induced matchings, the entire finite reconfiguration-component decomposition, the surprising compression onto the line graph of the same graph, and the exact optimal-state metric supply a reusable benchmark and structural obstruction to local improvement; these are not merely recomputed ordinary matching counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
