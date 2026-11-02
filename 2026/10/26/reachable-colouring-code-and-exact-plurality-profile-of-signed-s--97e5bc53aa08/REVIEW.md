# Independent mathematical audit

## correctness

PASS

If center is ignited first, all leaves spread in the next round with color a*s_i, giving exactly the canonical coloring. If a leaf ignites first, the center spreads in round 2 with a=s_i*b, while every other leaf still lacks a burned neighbor at that round start; the optional ignition can choose at most one second leaf with arbitrary color. In round 3 all remaining leaves are forced canonical. For n>=2 each desired flipped leaf is reachable by first igniting a different leaf. Hence center color and flipped index uniquely encode 2(n+1) colorings. Counting yellow leaves gives z^(p+1)(1+p/z+qz)+z^q(1+q/z+pz), and maximize exponents for Y. For positive signing a target disagreeing with its center on k leaves is distance max(k-1,0) from same-center code, or 1+max(n-k-1,0) from opposite-center code; maximizing minimum over k gives max(1,floor((n-1)/2)). Switching on trees transports signed processes and converts worst-signing plurality to n+1-covering_radius. n=1 has only two configurations. Independent simulator exhausted all 2^n signings for n=1..7, comparing literal reachable sets and counts. This finite check corroborates the complete first-ignition dichotomy.

## originality

PASS

Full text of the directly relevant founding signed-burning paper distinguishes the previously studied paths and general switching theorem from the new explicit star-specific reachability and yellow-count classification.

## value

PASS

Signed stars are the first branching tree family beyond the signed paths analyzed in the motivating primary paper. The result classifies every final coloring for every signing, computes its full distinct-color weight enumerator and covering radius, and identifies a sharp worst-signing plurality—natural coding and dynamic invariants across all n, rather than a routine n=3 sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
