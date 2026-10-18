# Exact three-layered criterion for \(2^a3^b5\)

## Finding
For every pair of nonnegative integers \(a,b\), let \(N=2^a3^b5\). A positive integer is *three-layered* if its distinct positive divisors can be partitioned into three sets with the same sum. Then the following statements are equivalent:

1. \(N\) is three-layered.
2. \(\sigma(N)\ge 3N\).
3. Either \(a\ge 3\) and \(b\ge 1\), or \(a=2\) and \(b\ge 2\).

In particular, the established \(2^a\cdot3\cdot5\) family extends to every higher power of \(3\) above the sharp abundance boundary. The proof gives a constructive partition at every admissible pair, including \(N=180\).

## Assumptions and scope
Here \(a,b\in\mathbb Z_{\ge0}\). All divisors are positive and distinct, each used exactly once. The sum-of-divisors function is \(\sigma\). The standalone file `certificates.json` gives thirteen small, exact, three-colored integer arrays; `verify.py` checks them and applies them to exponent rectangles. No numeric extrapolation is used to prove the infinite statement.

## Proof
**Necessity and parameter region.** A three-layered partition has class sum \(\sigma(N)/3\), while the class containing \(N\) has sum at least \(N\). Thus \(\sigma(N)\ge3N\). Direct multiplicativity gives
\[
\frac{\sigma(2^a3^b5)}{3\cdot 2^a3^b5}=
\frac{(2-2^{-a})(3-3^{-b})}{5}.
\]
For \(a\le1\), this is strictly below \((3/2)3/5<1\); for \(b=0\), it is strictly below \(2\cdot2/5<1\). For \(a=2\), the ratio reaches one exactly when \(3-3^{-b}\ge20/7\), which among integer \(b\ge0\) means \(b\ge2\). For \(a\ge3\), it is at least one for \(b\ge1\), with equality at \((a,b)=(3,1)\), and is increasing in both arguments. This proves equivalence of (2) and (3).

**Finite tile lemma.** For dimensions \((I,J)\), consider the \(2IJ\) distinct weighted cells
\[
W_{i,j,e}=2^i3^j5^e,\quad0\le i<I,\quad0\le j<J,\quad e\in\{0,1\}.
\]
For every \((I,J)\) in
\[
\mathcal T=(\{3,4,5\}\times\{3,4,5\})\cup(\{4,5,6,7\}\times\{2\}),
\]
these cells admit a three-color assignment of equal total weight. This is an exact finite lemma, witnessed in `certificates.json`: the entries called `colors` list the color indices in increasing \((i,j,e)\) order. To verify the lemma, add \(2^i3^j5^e\) for each indexed color. For every one of the thirteen tiles, the three sums are equal to
\[
(2^I-1)(3^J-1),
\]
which is one third of the total \(6(2^I-1)(3^J-1)\). The supplied independent integer-arithmetic checker verifies all thirteen finite assertions, without optimization libraries. As this is an explicitly specified finite witness and a direct sum computation, it establishes the finite lemma without relying on unchecked search.

**Exponent-rectangle tiling.** Multiplying a tile's entire set of weights by \(2^u3^v\) preserves its equal-color-sum property. This translates the tile by \((u,v)\) in the exponent rectangle without introducing overlapping divisors. If \(a,b\ge2\), both side lengths \(a+1,b+1\) are at least three. Every integer \(L\ge3\) is a sum of lengths from \(\{3,4,5\}\): write \(L=3q+r\), and if \(r>0\), replace one length three by \(3+r\). Partition each side into these consecutive lengths and take the Cartesian product grid. Every resulting rectangle belongs to the first nine types in \(\mathcal T\), so the three colored divisor classes combine to equal sums.

If \(b=1\) and \(a\ge3\), the second side has length two and the first has length \(a+1\ge4\). Every \(L\ge4\) is a sum of lengths \(4,5,6,7\), by the same division-and-replacement argument using four. The remaining four certified tiles partition this exponent rectangle and again give three equal divisor sums. These cases exhaust (3). Therefore (3) implies (1), proving the theorem.

## Verification
Run `python3 verify.py` in the directory containing `certificates.json`. It uses only the Python standard library, checks that every tile has exactly the advertised \(2IJ\) colored weights and the asserted common sum, and checks that the translated tiling construction partitions the complete divisor set for all \(0\le a,b\le15\). The output is `PASS: 13 tile certificates; 256 parameter checks; disjoint exhaustive divisor partitions`. The finite parameter loop is supplementary; the exact finite tile checks plus the unrestricted rectangle decomposition prove the result for every pair of nonnegative exponents.

## Relationship to prior work
Mahanta, Saikia and Yaqubi (arXiv:2008.11096v1, Section 3, Theorem 3.3) classify three-layered numbers of shape \(2^a p q\) with distinct odd primes and in particular prove the \(2^a3\cdot5\) case for \(a\ge3\). They do not analyze arbitrary positive exponents of the prime three. Jokar (arXiv:2207.09053v1, Sections 2, 4 and 5) proves conditional multiplicative/exponent-progression constructions and handles several isolated numbers, including the factorial example \(720=2^4 3^2 5\). The inspected results do not assert that three-abundance suffices on the whole two-parameter family, nor yield this exact characterization without new base certificates and an exponent-grid argument. The classification retains both known cases as prior results, not independent discoveries.

## Limitations
This theorem concerns exactly one factor \(5\) and arbitrary nonnegative exponents of \(2,3\); it does not assert an analogous classification for other three-prime supports or for \(5^c\) with \(c>1\). The construction proves existence, not the number of equal-sum partitions. The finite tile certificates have been checked by direct arithmetic, while full novelty beyond inspected literature cannot be guaranteed against unindexed publications. Independent external mathematical review has not been performed.

## References
1. P. J. Mahanta, M. Saikia and A. Yaqubi, *Some properties of Zumkeller numbers and k-layered numbers*, arXiv:2008.11096v1 (submitted 2020-08-07), https://arxiv.org/abs/2008.11096.
2. F. Jokar, *On k-layered numbers*, arXiv:2207.09053v1 (submitted 2022-07-19), https://arxiv.org/abs/2207.09053.
