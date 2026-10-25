# Independent mathematical audit

## correctness

PASS

For path vertex labels {0,1,2} with weight the label sum, the original condition for an edge with both labels 0 is that one of the external neighboring labels be 2; a positive endpoint immediately satisfies the edge. A run of >=4 zeros has a central unprotected zero pair, whereas zero runs between positives have allowed lengths 0,1,2 (length2 needs at least one flanking 2) or 3 (length3 needs both flankers 2); boundary zeros have length <=2 and need their sole adjacent positive to be 2 at length2. The two-positive-letter 2×2 transfer matrix with weighted inter-run polynomials H_11=1+x,H_12=H_21=1+x+x²,H_22=1+x+x²+x³ and boundary factors (1+x),(1+x+x²) gives 1+x+U(I−M)^−1V, which simplifies to the exact displayed rational bivariate GF with numerator 1+x+x³z² and denominator 1−xz−xz²−x²z−x²z²−x³z²−x⁴z²−x⁴z³. The formal substitution x=y/t,z=t² shows minimum possible exponent of t is −1; the t^(−1) odd-length and t^0 even-length coefficients are y/(1−y²−y⁴) and (1−y²−y⁴)^(−2), respectively. Thus for n>=1 the minimum is floor(n/2), with odd multiplicity Fib_{k+1} and even multiplicity the Fibonacci convolution; n=0 has one empty word. Fresh independent brute enumeration of all 3^n ternary words for n=0..11 directly tested edge feasibility and compared complete weight distributions to recurrence coefficients, including Φ5 weights 2:2,3:16,4:37,5:49,6:45,7:30,8:15,9:5,10:1. Further algebraic coefficients through n=24 matched exact Fibonacci minima. Infinite identity is from run grammar and formal-series algebra, not finite checks.

## originality

PASS

The exact notion requires checking edge endpoints versus a vertex adjacent to exactly one 2. Other perfect Roman vertex-domination or nonperfect vertex–edge Roman formulas use different feasibility conditions. The known minimum is a consequence of the stronger new enumerator, not the novelty in itself.

A broad algorithm capable of evaluating weights does not automatically state or directly imply these explicit coefficients without carrying out substantial transfer calculation; an existing explicit path enumerator would cover the theorem but was not found in inspected sources.

The scalar value is credited and excluded as new; no located exact polynomial table for the same vertex–edge perfect Roman labelings. Search limitations do not prove novelty.

The general finite-state method motivates the technique, but the prior minimum theorem and differing Roman variants do not imply the particular rational generating function as a stated result. The new claim makes a concrete substantially stronger enumeration.

## value

PASS

The vertex–edge perfect Roman domination number on paths is already floor(n/2), but it discards almost all combinatorics. The complete rational weight enumerator, exact count of every feasible weight and exact multiplicity of the optimum are natural enumerative invariants of a recently defined graph-labeling notion. The Fibonacci convolution gives a meaningful structural classification for an entire graph family and is not an arbitrary finite slice or merely reproof of a scalar minimum. General bounded-treewidth countability is acknowledged, but a concrete closed polynomial series is separately useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
