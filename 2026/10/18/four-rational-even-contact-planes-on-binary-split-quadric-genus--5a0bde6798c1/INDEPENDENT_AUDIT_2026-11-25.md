# Independent mathematical audit

## correctness

PASS

The corrected finding passes; the frozen witness geometry failed. For 0x7889, the sextuple contacts have second coordinate [0:1] at each of the three rational first coordinates. The three points originally listed as sextuple contacts are instead the double-contact points of the fourth plane; just one is shared. The frozen wording also suggested that only six masks have three distinct sextuple-contact planes without the four-plane restriction. A counterexample is smooth mask 0x6bbb with e=3: on [r:w]=[t:s+t], [s:t], [s+t:s] its restrictions are all t^6, with distinct contact points. It has a unit Jacobian ideal on each chart. The repaired RESULT.md explicitly limits the six-mask count to e=4 and displays the verified graph parametrizations and contact locus of 0x7889, and the accompanying REVIEW.md no longer claims the wrong coincidence. Independent replay: python /workspace/branches/independent-reproductions/contact_reproduction.py 4. It enumerates all 65535 masks using direct binary substitution on six graphs and membership in linear-times-square spaces on the nine reducible sections. The criterion on the latter uses odd degree on each fibre and even multiplicities off their crossing, so each fibre restriction has odd multiplicity at that crossing; addition gives even contact. A smooth (3,3) divisor cannot contain a ruling fibre or the graph, since any complementary effective divisor then meets it. The mask census agrees with all frozen e-buckets. For e>4, 1009 have F2 singular witnesses and two further F4 witnesses; for e=4 the exclusion counts are 8280 and 60. On all four charts the 60 e=4 survivors have unit ideals (f,f_x,f_y), certifying geometric smoothness. Independent substitutions by the 72 quadric symmetries give disjoint orbits of sizes 18,36,6 and stabilizers 4,2,12. Binary cubic factors, including the root at infinity and the reducible-section crossing multiplicities, verify all three frozen partition multisets and the corrected witness. The frozen scripts and data were inspected as evidence, not executed.

## originality

PASS

Pass for the repaired inclusive extremum, 60 masks, and nonreduced contact profiles. The 18-element proper-tritangent maximizer orbit is shared with a distinct same-day indexed result, now precisely credited; no priority ordering is imputed from the date. The coordinate correction does not create a separate novelty claim.

## value

PASS

The rational canonical even-contact statistic is a natural arithmetic invariant, and the complete classification of its extremizers separates proper from genuinely nonreduced contact in the smallest field. The 60-mask and three-profile classification answers a precise finite question not furnished by curve-model catalogues; in particular the sharp inclusive maximum is not the proper-plane maximum. The repair retains this result and corrects the sextuple witness without extending the assertion to nonsplit quadrics or other genera.

The dated certificate retains the supplied scientific assessment, sources and limitations.
