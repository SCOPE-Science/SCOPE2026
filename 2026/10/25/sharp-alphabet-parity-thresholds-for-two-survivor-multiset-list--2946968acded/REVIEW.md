# Independent mathematical audit

## correctness

PASS

Every multiset of size n>=q+1 has a coordinate of multiplicity at least two. Writing S for singly-heavy and T for multi-heavy codewords gives S+2T<=qL by monochromatic received pairs; the complete singly-heavy family has qK words, K=2^(q-1), hence |C|<=floor(qL/2)+qK/2. Direct counting gives E=(q+2)k singly-heavy parents for each mixed received pair, k=2^(q-3). If equality holds, the integral deficit from all singly-heavy words is at most the parity p in q(L+K); mixed-pair headroom yields the even/odd L0 barriers. Round-robin one-factors (even q) and Walecki Hamilton cycles plus a matching (odd q) realize degree/multiplicity-constrained multigraphs used for new exactly-two-heavy source words. For odd q at L0-1, omitting the fully supported singly-heavy source and removing a near-perfect matching from kK_q gives exactly the floor-bound size. At L0 saturated mixed pair headroom forces all extra words supported on one heavy pair and exactly k per pair, producing the binomial optimizer count. Own direct multiset receive-list tally gives (q,n,L,size)=(4,5,14,44),(5,7,31,117), with no list overload. Infinite statements follow from combinatorial counting and factorization, not those two tests.

## originality

PASS

Kreindel--Essayag--Zabokritskiy, Multiset Deletion Codes (arXiv:2601.05636v2), Theorem 10 and Corollary 11, prove size q for UNIQUE DECODING with two survivors when n>=q+1. The present two-survivor L-list setting is a different incidence packing, with sharp high-L parity boundaries and all-optimizer enumeration. The accessible primary preprint explicitly focuses on one-list decoding and general code bounds, without implying the new high-list formulas. No matching published table or stronger theorem was located; risk of independent list-decoding formulation remains.

## value

PASS

Exact high-list cardinalities, sharp onset differences between even and odd alphabets, constructions, and the complete family of extremizers for a natural deletion channel are meaningful finite-alphabet coding invariants. A gap in achievable list budget and an exact optimizer enumeration are not routine known unique-decoding conclusions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
