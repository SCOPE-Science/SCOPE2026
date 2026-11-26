# Independent mathematical audit

## correctness

PASS

For the repaired claim, every legal graph edge is exactly a swap of consecutive positions whose endpoint also belongs to the full derangement list. The fresh verifier enumerates all n! words at n=2,...,5, filters by the literal fixed-point condition, computes exact BFS distances and compares to the Kendall pair-disagreement count for every reachable unordered pair. I executed it: vertex counts 1,2,9,44; respective reachable pair counts 0,0,11,188; no detours. Independently reasoned the upper and lower bounds for all n>=6. The displayed path acts in the first five positions and its eight prefixes have no fixed point; T_n=(7,...,n,4) is fixed throughout and has no fixed point even at n=6. Only five pair orders change between the endpoints: 1 with 2,5,6 and 6 with 2,5. Each step on an unrestricted geodesic would decrease disagreement by one. The only decreasing first swaps are (1,2) and (5,6) as label pairs, which respectively fix positions 2 and 5; no tail swap decreases disagreement. Every path length has odd parity, and the seven legal prefix swaps reach the target, proving exact distances 7 and 5 even when additional tail moves are allowed. Fresh BFS also independently confirmed those distances at n=6. Verification front matter is byte-identical to the original.

## originality

PASS

The distinct repaired result is the sharp order threshold for within-component isometry and an exact detour persisting at all larger orders. Verified broader work covers the discarded connectivity claims, not this shortest-path result. The closest same-domain detour allows arbitrary switches, while the closest same-question first-detour theorem uses a different class of permutations.

## value

PASS

Once exact connectivity of the signature sectors is known, it is natural to ask whether standard Kendall geodesics already suffice for optimal routing within them. The answer is not a trivial consequence of disconnectedness: every connected pair retains its distance through order five, while a concrete local obstruction first forces a two-step surcharge at six and cannot be bypassed using extra labels at any larger order. The exact boundary and persistence make the witness independently useful, rather than retaining a covered theorem with a cosmetic disclaimer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
