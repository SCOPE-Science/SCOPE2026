# Independent mathematical audit

## correctness

PASS

Independence and domination require gaps 2 or 3, respectively bounded below and above, and a legal slide swaps an unlike adjacent gap pair. Distinct legal slides give different vertex sets. Marking a token gives n choices for the anchor and binomial(k,t) for its gap word; each unmarked placement occurs k times. Counting distinguished 3-run starts among indexed gap words by two compositions gives the degree multiplicities, with Vandermonde giving the edge count. When t=0 there are just the two immobile alternating sets. Otherwise slides disjoint from a marked token can rearrange its linear gaps by adjacent swaps. Placing gap 2 behind it and 3 ahead lets it advance; this proves connectivity. Even degree proves the Eulerian assertion and t=1 gives C_n. Position sum sends each slide to ±1 modulo n; it gives even-n bipartiteness and forbids odd returns shorter than n for odd n. In the floor schedule use integer lifts with F_(i+k)=F_i+n. With remainder k−1 a moving token has gap 2 behind and 3 ahead; other moving indices are spaced by k/gcd(n,k)≥2. Serializing the disjoint swaps gives n clockwise unit slides, with terminal positions cyclically relabeled. No shorter subreturn is possible by position sum, so the n-cycle is simple. Independent bitmask enumeration checked 15 eligible layers for 8≤n≤17, including exact odd girth via parity-double-cover BFS in all seven odd layers. Replay: python -B /workspace/branches/frozen_recheck.py 1.

## originality

PASS

Best of checked evidence, the distinct theorem is the active, maximal-only nonminimum layer result, especially the constructive n-cycle and exact odd girth together with the full degree spectrum. An exact sector/count comparator is later-dated and lacks these parity results. The ordinary token-slide graph's bipartiteness on even cycles already implies that portion by restriction; no novelty is assigned to it alone.

## value

PASS

The layer is the natural counterpart to minimum independent domination, keeping domination at every step rather than relaxing it for reachability. The exact histogram measures how many legal updates states have; the explicit n-cycle and sharp odd obstruction separate local mobility from the shortest odd return. These are useful layer invariants not supplied by ambient reachability or minimum-layer classifications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
