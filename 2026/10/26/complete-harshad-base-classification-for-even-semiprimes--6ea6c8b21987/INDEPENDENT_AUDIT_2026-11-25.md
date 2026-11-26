# Independent mathematical audit

## correctness

PASS

For 2<=b<=2p, s_b(2p)<2p since a nonzero digit occupies some positive radix position; the only admissible sums are therefore 1, 2 and p. Sum 1 forces 2p to be a power of b, so squarefreeness gives b=2p. Sum p forces b-1 to divide p via the radix congruence; b=2 fails because s_2(2p)=s_2(p)<p, while b=p+1 has digits 1,p-1. For sum 2, a single digit 2 gives b=p, and two digits 1 give 2p=b^i+b^j with i>j. If j>0 then b divides 2p, and b>=p is too large, so b=2 and the 2-adic valuation forces j=1. Hence p=2^{i-1}+1, prime only if i-1 is a power of two, by factoring x^h+1 at any odd h>1. If j=0, b^i=2p-1; i=1 gives the baseline. For i>1, b is odd and an odd factor h>1 of i would split p into the nonunit factors (b^{i/h}+1)/2 and (b^i+1)/(b^{i/h}+1). Conversely each listed root produces the two ones, and each Fermat prime gives two binary ones. Root bases lie between 3 and sqrt(2p-1)<p, and distinct exponents give distinct bases. Unary completes the list. Prime factorization gives the 2-adic gcd formula, and the exceptional primes up to X are bounded by the number of square roots up to sqrt(2X) plus O(log log X) Fermat indices. Division by pi(X) proves the density-one statement. Independent bounded replay for the witness: test p=21523361 modulo every d=2 through 4639 (no divisor), and for b=1 through 43046722 sum the repeated radix remainders of 43046722 (unary sum is the number itself), retaining b if the sum divides 43046722. This gave exactly the nine listed bases with digit sums 43046722,2,2,2,2,2,21523361,2,1, respectively. It checks this witness only; the bundled checker was inspected, not run, and the universal result rests on the proof.

## originality

PASS

The distinct supported claim is the exhaustive base classification for every odd-prime 2p, including the general root multiplicity and quantitative density-one consequence. The standard counting function, five baseline bases, and the binary, square-root and fourth-root patterns and sample counts are prior evidence, not new. The strongest earlier OEIS discussion restricts which integers can have counts five or six; that implication does not classify the bases of every 2p. The targeted evidence did not establish equivalent coverage of the universal statement.

## value

PASS

There is a natural question behind the tabulated low counts: which twice-prime integers retain just the familiar five bases, and which acquire further ones? The complete classification turns the observed binary and root patterns into all and only the exceptions and shows their frequency is negligible among primes. The arithmetic witness illustrates multiple distinct higher-degree roots, but the value rests on the universal exhaustion and its quantitative consequence, not the large example alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
