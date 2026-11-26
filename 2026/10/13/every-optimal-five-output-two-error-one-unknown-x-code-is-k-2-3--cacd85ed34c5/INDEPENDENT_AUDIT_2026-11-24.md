# Independent mathematical audit

## correctness

PASS

There is an independent short upper-bound and rigidity proof. For each unknown word U, projection outside supp(U) is injective on the whole code: no other word projects to zero (one-error condition), and no two other words have the same projection (two-error condition). Thus n<=2^(5-wt(U)) for every U, and for n>=6 all words have weight at most two. The zero word is impossible. If a singleton occurs, every other word avoids its coordinate; deleting that singleton and coordinate leaves at least five words in length four, all of weight at most one by the same bound, a contradiction. For the remaining weight-two words the X-condition is exactly triangle-freeness: two disjoint edges have four-point XOR, and two adjacent edges have two-point XOR covered by an unknown edge iff they form a triangle. At least six edges require maximum degree at least three; degree four forces a four-edge star; degree three leaves an independent three-neighbor set and only one other vertex, which must join all three neighbors to reach six edges. This forces K_2,3 and excludes seven. Conversely every labeled K_2,3 satisfies the X-condition. Its smaller shore can be chosen in ten ways, all one S_5 orbit, with stabilizer S_2 times S_3 of order 12. Read RESULT.md, VERIFICATION.md, the census and recorded output, and inspected artifacts/verify.py without executing it. Independent projection enumeration (`python3 /tmp/opencode/frozen_math_replay_1_2_4.py 1`) covered the remaining 5,005 six-subsets and 6,435 seven-subsets after the weight bound, giving 10 and 0 respectively. All census masks, edge lists, degree-three shores and recorded artifact hashes matched. The original larger candidate counts are binomial(31,6)=736281 and binomial(31,7)=2629575. No larger-parameter classification is inferred.

## originality

PASS

The known construction, weight-two extremum and its graph equality case are not the novelty. The justified distinction is that the extremum remains six without a fan-out constraint and that every unrestricted optimizer lies in the classical weight-two class. The checked literature does not already supply that reduction or the unrestricted equality classification for these parameters.

## value

PASS

This parameter lies at the first genuine compaction length for this error/unknown model. In fact, n>m for m=1,2 forces zero weight by the projection bound; for m=3,4 it forces weight at most one, hence n<=m. At m=5, the six-word construction gives n>m. It is useful at this natural cutoff to know not only that the fan-out-two architecture works but that no higher- or mixed-weight architecture competes, and to have all possible optima up to wire relabeling. The restricted graph result does not answer that structural question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
