# Independent mathematical audit

## correctness

PASS

Read actual 5512-byte RESULT.md at blob 299b9ae3f37b94a4541ca8bdd8eef5a3cd98bc94 and checked the cited FULL 33-page primary PDF at Theorem 20, Claim 21 and Problem 43, including diagram/screenshot. Claim 21 supplies an actual bounded saturation witness for A=Γ_{0,1,0}. Independent exact edge-set inspection shows no B edge joins consecutive pattern positions, whereas A has the unique consecutive (4,5); deleting vertices 4 and 5 of A leaves B (after order-preserving renumbering). Therefore in any {A,B}-saturated H, a missing edge between consecutive isolated vertices cannot create B and would create an old B if it creates A. Thus no two consecutive isolated vertices, so z≤r+1 and |E(H)|≥r/2≥(n−1)/4. The argument holds for every n (vacuous for tiny n) and needs no incomplete enumeration.

## originality

PASS

Qualified PASS: the same 2022/2023 primary paper proves sat_<(n,A)=O(1) and explicitly poses the universal two-forbidden-family comparison as Problem 43, rather than resolving it. The new forbidden-pair obstruction defeats that comparison with an infinite linear lower bound. Subsequent independent solutions could exist; targeted Resultary and web searches did not locate one.

## value

PASS

The graph pair answers a clearly identified open comparison question by a short but structurally informative skeleton/minedge obstruction. It exhibits a striking loss of bounded saturation when a second forbidden graph is imposed; linear lower bound suffices without an exact matching upper bound. This is a mathematically motivated general-failure witness, not an arbitrary tiny counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
