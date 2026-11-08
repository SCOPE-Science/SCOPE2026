# Independent mathematical audit

## correctness

PASS

For each iid integer switching law p_b, the actual two-branch transfer operator has on Y one left preimage, giving h1=2h0, and on J_m left contribution h_{m+1}/2 plus c/2 sum_{b<=m} p_b 2^b. Substitution h_m=c sum_b p_b 2^min(b,m) verifies each equation exactly; positivity ensures Lebesgue equivalence and sigma-finiteness. Tonelli over shell lengths 2^(-m-1) gives mass c(E B+2)/2, hence normalized probability iff E B<infinity using the uniqueness in Inoue–Toyokawa. Differences h_m-h_{m-1}=c 2^(m-1) Pr(B>=m) yield the exact inverse and prove the stated nonincreasing-tail characterization with q1=1, limit zero, p_m=q_m-q_{m+1}. Under the induced normalized Lebesgue measure on Y, U=2x-1 is uniform; B independent and the first run of zero binary digits G is geometric with Pr(G=j)=2^(-j-1), yielding first-return time R=B+1+G. The induced return point remains conditionally uniform on Y, giving iid renewal clocks and PGF z E[z^B]/(2-z). I checked 3 explicit laws including multi-point supports with Fraction arithmetic through 99 shell recurrences, tail inversion and mass; the countable-law proof is via transfer identity, Tonelli and regeneration, not finite tests.

## originality

PASS

Best-of-knowledge originality after primary-literature reading and Resultary queries. The explicitly identified prior statements and implication gaps are documented under the four checks. A failed search is not proof of priority, and inaccessible literature was not treated as automatic failure.

## value

PASS

Exact identification of a countable random switching law from its full stationary dyadic density is a natural inverse problem, sharper than order-comparable density bounds. It provides a complete realizability characterization and a renewal-process representation, including infinite-mean sigma-finite dynamics and zero return frequency. These are reusable exact facts for a known intermittent random-map family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
