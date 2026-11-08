# Independent mathematical audit

## correctness

PASS

For open ladder L_n=P2 square Pn, n>=2, with n rungs and 2(n−1) horizontals, a PED-set F requires precisely one selected neighbor for each unselected edge; selected edges have no restriction. Encoding current rung a_i and two outgoing horizontals b_i,d_i, the three local tests for an omitted rung, omitted upper horizontal and omitted lower horizontal correctly count selected adjacent edges with previous/current/next masks. The finite 64-state ordered-mask transfer is an exact complete logical certificate: forward/backward complete-walk filtering leaves the explicitly listed 14 states, comprised of a full-edge loop with terminal and a directed 6-cycle with 4 phases and terminal exits. Every accepted full-edge word has 3n−2 edges; every other accepted word has exactly n selected edges, with 4 words iff n ≡ 2 mod 3 and 2 otherwise, so Q_n(z)=z^(3n−2)+(2+2*1_{n≡2 mod3})z^n, for every n>=2. Independently enumerated literal edge-neighbor subsets for n=2..6, obtaining histograms {2:4,4:1}, {3:2,7:1}, {4:2,10:1}, {5:4,13:1}, {6:2,16:1}; no intermediate size. This also supplies an explicit counterexample to the 2020 printed claim that n=4 minimum is 10: two valid 4-edge sets exist. The finite transfer graph is exhaustive for all lengths; the brute finite checks alone are not the infinite proof.

## originality

PASS

There is direct prior coverage of the SAME minimum PED parameter on open ladders: Chitra–Prabhavathi (2020), Theorem 2.6, but its n ≡ 1 mod 3 branch incorrectly asserts 3n−2 as minimum, contradicted by explicit n=4 edge certificates and exact source transfer classification. The 2026 Grippo–Lin–Moyano–Vera full open arXiv article provides O(n+m) PED-counting on all generalized series-parallel graphs including ladders, but no inspected exact two-term size polynomial or complete all-length phase enumeration. Thus assessed claim corrects a published result and supplies a stronger full cardinality distribution; it is not just a copied special case.

## value

PASS

The cardinality distribution of all PED sets is an established graph counting problem, beyond its minimum-size parameter. A complete two-term polynomial for every open ladder, a constructive finite-state description, exact mod-3 multiplicity, and a published minimum-formula correction are substantive useful information. The all-length rigidity is not guaranteed by any generic counting algorithm or by routine single-instance enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
