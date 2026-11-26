# Independent mathematical audit

## correctness

PASS

Each transitive triple contributes once to the sum over vertices of binomial(outdegree,2), whereas a cyclic triple contributes zero. For an independent proof of the signed expectation, let S be the number of odd outdegrees and m the number of edges. Since binomial(d,2) has parity floor(d/2), the sign of the triad count is (-1)^(binomial(n,3)+(m-S)/2). After conditioning on all edges off a fixed star, the other n-1 vertices' outdegree parities are independent fair bits, and the star center's parity is fixed by the sum m. Thus the parity vector is uniform over the required parity hyperplane. Summing the sign over the binomial Hamming weights yields (-1)^binomial(n,3) times 2^(1-n) Re[i^m(1-i)^n], confirming the roots-of-unity expression in the frozen proof. For n=2k the cosine has argument pi*k*(k-1), hence is one, and binomial(n,3) is even. For n=2k+1 the cosine is (-1)^k/sqrt(2), canceled in sign by binomial(n,3) of parity k. The resulting bias is positive 2^(-floor((n-1)/2)); since all 2^m orientations have equal mass this gives the exact difference and both probabilities. The same proof agrees with the trivial n=2 boundary.

## originality

PASS

The score identity is classical and gives the necessary reduction, but neither the exact fixed-triad enumerator nor the score-type or fluctuation results inspected give the exact all-order alternating sum. The supported distinct claim is evaluation of this signed marginal in the fair labeled ensemble, not discovery of the score identity or of triad enumeration. The retrieval and scope limitations below remain.

## value

PASS

For a classical tournament statistic, parity is the basic discrete oscillatory marginal not resolved by moment calculations or fluctuation limits. The result determines its exact positive excess for every order and identifies the odd-to-next-even plateau; neither follows from a finite table. The cancellation based on outdegree parity gives a concrete structural explanation of the bias, not merely re-enumeration of small tournaments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
