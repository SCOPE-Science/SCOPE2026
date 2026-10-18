# Independent mathematical audit

## correctness

PASS

Encoding a species row by a nonzero site-mask m yields exact richness R(s)=sum_m 1[(m&s)!=0] for each site subset s and histogram L_k(j) by popcount(s)=k. Row/column twin-freeness implies if either guild size<=3 then opposite guild size <=2^3−1=7. Inspected full Git verify.py; independently enumerated all such relation shapes on each side (15 parameter-size cases), checked connectedness, nonzero and nonduplicate row/column masks, laws and guild-preserving isomorphism, with no collision. Direct witness A=(1,3,6,14), B=(1,3,6,13) is eligible and shares every k,j histogram, though A contains a four-cycle (rows 6 and 14 share two sites) while B does not; hence nonisomorphic. This is an exhaustive finite proof for the claimed first boundary, not statistical sampling.

## originality

PASS

Classic incidence-based rarefaction relates species-frequency counts and mean richness, but this complete joint k,j sampling-law reconstruction and sharp first nonuniqueness under connected twin-free constraints are strictly finer: identical mean curves do not imply identical entire distributions. Complete neighborhood hypergraphs are stronger input than histograms and their reconstruction theorem cannot be conflated with the present invariant.

## value

PASS

A sharp 4x4 failure of identifiability despite observing every finite sample richness distribution, under connectedness and twin-free hypotheses, is a natural obstruction relevant to ecological inverse problems and binary relation invariants. The finite character is intrinsic to the minimal-size classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
