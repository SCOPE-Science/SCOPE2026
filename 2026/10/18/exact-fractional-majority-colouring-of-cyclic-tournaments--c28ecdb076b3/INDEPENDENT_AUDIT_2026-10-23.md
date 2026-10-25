# Independent mathematical audit

## correctness

PASS

In any majority-stable subtournament S of size s, the sum of internal outdegrees is s(s-1)/2 while each is <=k=floor((n-1)/4); hence s<=2k+1. Alternating even or odd residues supply a 2k+1-member set with all outdegrees exactly k, with n=3 handled by singleton. Summing fractional coverage yields lower bound n/(2k+1); averaging cyclic translates of an extremal stable set with weights 1/(2k+1) attains it. For n=4k+1, complementary alternating residue classes are stable, so integer 2, whereas n=4k+3 has 2(2k+1)<n and requires integer 3; complement partition into two blocks of k+1 is stable. Independently enumerated all stable subsets for odd n=3..17 to verify maxima 1,3,3,5,5,7,7,9, including fractions n/alpha. The all-order result uses arc-count and orbit argument, not finite sampling.

## originality

PASS

General fractional majority coloring inequalities from Anastos et al and Ben-Ameur/Maddaloni 2026 apply to arbitrary digraphs and tournaments but no exact cyclic-carousel formula was identified in accessible publications. The published cyclic-tournament acyclic dichromatic number 2 has a stronger transitive-color-class requirement, distinct from internal outdegree <=k. The known concave-round tournament integral 2/3-coloring aligns with ordinary values but does not by itself imply the fractional optimum. Full Ben-Ameur and 2025 integral paper access gaps remain priority risks.

## value

PASS

Every odd-order cyclic/carousel tournament is a canonical vertex-transitive tournament, so the closed exact fractional LP optimum and dual cardinality certificate give benchmark instances for general majority coloring. The strict parity split across the reference value 2 (and integral 2 versus 3) illustrates an intrinsic sharp combinatorial boundary, not a handful of computed examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
