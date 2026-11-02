# Scientific review

## Correctness — PASS

Definitions and quantifiers were checked against the encoded graph. Every strand-closed code is precisely a union of reverse-complement orbits, the 136 orbit shadow masks represent all 256 source words without duplicate descendants, and compatibility edges are equivalent to disjoint deletion shadows. Greedy independent-class partition yields a valid **weighted clique upper bound** because any clique intersects each independent class in at most one vertex. Recursion explores each include/exclude choice and prunes only with that valid bound. The search recomputed the optimum 24 and all 160 equality cliques; the restricted search recomputed optimum 22 and 44 equality cliques. Explicit witnesses and every TSV inventory entry underwent direct deletion-shadow and closure checking. Permutation-orbit counting and fixed-word distributions were independently checked by direct codebook transforms. The executable checker returned `VERIFY_OK` when run in its actual package directory. Finite search is legitimately exhaustive for this finite universe, with no extrapolation.

## Originality — PASS, with historical-priority risk

Full-text comparisons covered the deletion-shadow formulation in Sloane (2002), reverse-complement **Hamming separation** in King (2003), length-three/length-four but different-deletion-radius perfect codes in Chee–Ge–Ling (2010), and quaternary single-indel asymptotic constructions in Cai et al. (2019). Each either lacks the Watson–Crick *closure* constraint, has different alphabet/length/error radius, or does not determine and classify the 24-word equality case. Published-record searches for the specific parameters, deletion shadows, complement-invariant codebooks, and 160/44 equality counts did not identify a stronger theorem implying this census. Risk remains that historical small-code tables or unpublished code could already imply some or all of it. No historical-priority certification is asserted.

## Value — PASS

A natural DNA design issue is whether both orientations are admissible under one-deletion decoding. This closes a concrete four-letter short-block benchmark with a full equality census, not just one construction. The distinction between accepting all reverse-complement orbits and excluding self-complementary words produces a **two-word sharp capacity loss** and shows that all 24-word optima necessarily contain 2–8 self-complementary strands. The symmetry classification reduces 160 labeled optima to 28 structural classes for later design screening. This is useful as a precise boundary for combining strand symmetry with deletion correction, without claiming in-vivo efficacy.

## Sources and limits

Sloane (2002), https://arxiv.org/abs/math/0207197; King (2003), https://arxiv.org/abs/math/0306197; Chee–Ge–Ling (2010), https://arxiv.org/abs/1008.1343; Cai et al. (2019), https://arxiv.org/abs/1910.06501; García-Claro (2025), https://arxiv.org/abs/2506.19170. The primary source date is 22 July 2002, not a later journal or revision date. Full-text historical coverage is incomplete and independent audit remains pending. All results here are conditional on the finite, labeled alphabet and stated one-deletion channel.

Self-review: passed. Independent audit: not yet performed.
