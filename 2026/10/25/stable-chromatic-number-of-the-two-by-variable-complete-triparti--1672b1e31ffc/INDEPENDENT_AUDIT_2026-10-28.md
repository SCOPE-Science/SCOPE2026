# Independent mathematical audit

## correctness

PASS

The part-directed acyclic orientation gives maximum reachable-set size m+3. A two-part augmentation lemma shows adding q vertices to each of two parts forces q additional palette colors: level-i rankings forbid every level-i vertex color <i by an envy 2-cycle, and forbid the core colors <=q. An explicit K222 seed profile exhausts all 96 proper 4-color assignments, 92 with envy 2-cycles and four with 3-cycles. Independent pure Python enumeration recovered exactly these numbers and exceptional color vectors, so the seed holds; induction and subgraph monotonicity yield all m,n.

## originality

PASS

Koana–Oh–Yoneda defines this exact invariant, proves reachability upper bound, subgraph monotonicity and a prism obstruction implying K222>=5; published K233=6 is prior. Neither identified statement gives the two-part amplification to all m>=4. Relevant full Koana paper could not be retrieved (OA attempt and Oxford VPN disconnected), leaving a nonzero priority risk but no strong identified coverage.

## value

PASS

An exact infinite-family preference-stable coloring threshold for complete tripartite graphs is a natural combinatorial invariant. A general lower-bound amplification lemma provides structurally reusable content beyond isolated small examples; its value is not based on 96-case enumeration alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
