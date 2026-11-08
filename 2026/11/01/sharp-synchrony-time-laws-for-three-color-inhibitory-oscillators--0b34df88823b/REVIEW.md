# Independent mathematical audit

## correctness

PASS

The 49 nonempty support pairs for clique and independent vertices are an exact quotient: same-color vertices within either graph class have identical futures; a clique vertex at 2 is inhibited iff any other vertex currently blinks at 1, and independent class vertex at 2 iff any clique vertex blinks. Directly iterating the simultaneous three-color rule gives the complete 7x7 first-synchrony-time table, with the sole non-sync mask (4,7) a genuine primitive 3-cycle from time zero. Multiplying each mask by onto-coloring weights 1,2^k−2,3^k−3·2^k+3 gives the stated seven exact counts, summing to 3^{m+n}, the period census, bound 6 sharp n≥2 and bound 3 when n=1. Independent direct Python 49-support re-derivation and small m,n labelled enumeration agreed, not an extrapolation; the support quotient proves all sizes. Asymptotic distributions follow by normalized powers of 2/3.

## originality

PASS

Lyu studies this identical inhibitory firefly update largely on paths and trees, where graph structure differs; no inspected theorem implies exact complete split graph support census, hitting-time distribution, and clique-size uniform time-two concentration. The known general star and bipartite phenomena are special/different adjacency cases; searches do not establish global priority.

## value

PASS

The complete split graph is a natural dense/nonregular network extending the star. Exact size-independent 49-class reduction yields an all-size first-hitting-time distribution, sharp transients and recurrent-orbit classification; these are useful precise dynamical invariants, not routine small-case enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
