# Independent mathematical audit

## correctness

PASS

The frozen witness sentence at RESULT.md lines 74–76 omitted good 1: good 5 plus just one good valued 1 does not give utility 4. The complete corrected RESULT.md is in /workspace/repairs/5/. MNW gives agent 1 exactly {1,5}; leximin gives agent 1 one of {1,2,5}, {1,3,5}, {1,4,5}, with complements going to agent 2. The repaired proof also includes the empty allocation and proves that every Nash tie at product 18 has sorted pair (3,6), since all other positive factor pairs of 18 exceed the utility-sum bound 10. Leximin fixes its sorted pair by definition. An independent labeled exhaustive enumeration retained the full argmax sets at all m=0,…,5. The (equal, leximin proper subset, disjoint) counts are (1,0,0), (4,0,0), (16,0,0), (56,8,0), (240,16,0), (892,32,100), with no other relation type. A second type-count calculation with multinomial weights verifies the eight bad vectors and four swap classes of sizes 10,10,40,40. Optimizer multiplicities on the bad profiles are MNW 1:80 and 4:20; leximin 3:80 and 6:20. These checks verify the full repaired claim, not merely some tie-breaking. Independently, if a Nash optimum with sorted pair (r,R) strictly beats leximin at higher minimum, moving a rich agent's good gives R<=2r+2. If r=1 this cannot strictly beat higher min; if r=2 and R>=5, any good worth 1 to the rich agent gives a strict improvement by transfer, so R=6 with three goods worth 2, and a transfer reaches (at least 3,4), enough to rule out lexicographic conflict. Thus r>=3. A leximin minimum of 5 would maximize product as well by the total bound. Only (3,6) can beat a leximin minimum of 4 with at most five goods; this needs two goods for the poorer agent and three worth 2 for the richer one. Each of the latter must be worth 1 to the poorer agent or a transfer improves the Nash product. The poorer agent's original goods give it 1 and 2, yielding exactly the stated four classes up to swap. Conversely in each class transferring a rich good yields (4,4); comparing products by bundle sizes shows that 18 is optimal. No uploaded verifier was executed. Replay: /workspace/branches/ae7e9d31-6949-42a6-9b8f-b5ddecd1849b/{independent_census.py,small-run.txt,full-census.txt}.

## originality

PASS

The repaired claim is about first disjointness of the entire optimizer sets and its exact first-layer classification in the positive {1,2} domain. It is not the first example in which the objectives disagree in some sense or a claim to fair-division approximation bounds. The verified nearby primary and catalogue statements do not establish this specific claim.

## value

PASS

The positive two-level domain is a minimal natural change from the binary equivalence setting. The first unavoidable conflict tests whether that equivalence can be salvaged by tie-breaking, and the exact census plus common welfare profiles identify how it fails, beyond an isolated example. The bound at five is forced by the first possible conflict, not an arbitrary stop in a larger computation. The corrected witness explicitly realizes the structural obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
