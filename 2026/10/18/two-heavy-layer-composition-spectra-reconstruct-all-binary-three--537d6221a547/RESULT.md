# Two-heavy-layer composition spectra reconstruct all binary three-marker strings

## Finding
Let \(w\) be any finite binary word containing **exactly three** occurrences of \(1\). For \(h\in\{2,3\}\) and \(\ell\ge1\), let \(N_h(w,\ell)\) be the number of contiguous factors of \(w\), counted with multiplicity of starting positions, that have length \(\ell\) and exactly \(h\) ones. Then the two arrays
\[
\bigl(N_2(w,\ell),N_3(w,\ell)\bigr)_{\ell\ge1}
\]
**uniquely determine \(w\) up to reversal**, for every possible length of \(w\). Neither its length nor its substrings with zero or one occurrences of \(1\) need be supplied separately. This is an exact all-length injectivity theorem for the two highest-weight layers of the ordinary substring-composition multiset.

The restriction to three ones is sharp for this type of universal recoverability: the two four-one words `01001101` and `01101001` are not reversals but have identical **complete** substring-composition multisets, as already recorded by Acharya et al. Thus no layer selection from that complete observation can reconstruct all four-one words.

## Assumptions and scope
Words are *linear*, binary, and have exactly three ones. A factor is a **nonempty contiguous substring**, counted once per position. Its composition records its numbers of zeroes and ones, not their order. Reversal means reading the entire linear word in the opposite direction; no circular rotations, bit complements, or alphabet relabelings are identified. The input comprises exact integer multiplicities for all lengths in the two stated weight layers. There is no probabilistic or asymptotic assumption.

Write the unique gap representation
\[
w=0^a1\,0^b1\,0^c1\,0^d,
\qquad a,b,c,d\in\mathbb Z_{\ge0}.
\]
Define \(S_r(t)=1+t+\cdots+t^r\) for every integer \(r\ge0\), and the length enumerators
\[
P_h(t)=\sum_{\ell\ge1}N_h(w,\ell)t^\ell
\quad(h=2,3).
\]

## Proof
**1. Exact two-layer generating polynomials.** A factor with three ones necessarily contains the three distinguished ones. It extends its left boundary through any of the \(a\) leading zeros and its right boundary through any of the \(d\) trailing zeros. Consequently
\[
P_3(t)=t^{b+c+3}S_a(t)S_d(t).
\tag{1}
\]
A factor with exactly two ones contains either the first two or the last two distinguished ones, but not all three. The two cases are disjoint and yield
\[
P_2(t)=t^{b+2}S_a(t)S_c(t)+t^{c+2}S_b(t)S_d(t).
\tag{2}
\]
These identities include zero gaps and endpoint boundary cases.

**2. Recover the unordered gap pairs.** Because every coefficient in the sums defining (1)–(2) is nonnegative, the smallest exponent in \(P_3\) is \(b+c+3\), while the largest exponent is \(a+b+c+d+3=|w|\). Hence \(b+c\) and the full word length are recovered. The normalized polynomial
\[
Q(t)=t^{-(b+c+3)}P_3(t)=S_a(t)S_d(t)
\]
determines the unordered pair \(\{a,d\}\). Indeed, if \(u=\min(a,d)\), its coefficients at degrees \(0,\ldots,u\) are \(1,2,\ldots,u+1\), and the coefficient at degree \(u+1\), interpreted as zero if beyond the degree, is strictly smaller than \(u+2\). Thus \(u\) is recovered as the last degree of the initial staircase. Since \(\deg Q=a+d\), the larger of \(a,d\) is also determined.

From (2), the smallest exponent in \(P_2\) is \(2+\min(b,c)\). Together with the already recovered sum \(b+c\), this yields the unordered pair \(\{b,c\}\).

**3. Resolve the only possible orientation ambiguity.** Knowing these two unordered pairs leaves at most four gap quadruples, grouped into two reversal orbits. Reversal sends \((a,b,c,d)\) to \((d,c,b,a)\). Representatives for the two possible orbits can be taken as \((a,b,c,d)\) and \((d,b,c,a)\). If \(a=d\) or \(b=c\), the two orbits already coincide. Otherwise, subtracting the second-layer polynomials for these two representatives gives
\[
\begin{aligned}
\Delta(t)
&=\bigl(S_a(t)-S_d(t)\bigr)
  \bigl(t^{b+2}S_c(t)-t^{c+2}S_b(t)\bigr)\\
&=\frac{t^2\bigl(S_a(t)-S_d(t)\bigr)
\bigl(t^b-t^c\bigr)}{1-t}.
\end{aligned}
\tag{3}
\]
Both factors in the numerator are nonzero when \(a\ne d\) and \(b\ne c\). The polynomial \(\Delta\) is therefore nonzero, so the observed \(P_2\) identifies the correct reversal orbit. This proves injectivity up to reversal for all allowed words.

**4. Sharp four-one boundary.** The known pair `01001101`, `01101001` has four ones in each word, is not related by reversal, and has the same complete substring-composition multiset [1]. Direct enumeration in `verify.py` also checks this fact. Accordingly, the three-one threshold cannot be increased to all words with four ones.

## Verification
Run `python3 verify.py` using standard Python 3. The program has no third-party dependencies. It implements the two-layer histogram directly from prefix sums, independently implements (1)–(2) by gap-extension enumeration, and exhaustively compares all binary words with exactly three ones at each length from 3 through 32. For each pair with identical two-layer histogram it checks that the words are equal or reversals. This comprises 40,920 tested words. It also directly checks the complete-spectrum four-one collision and a three-one example showing that the three-one layer alone need not suffice.

The finite check does not establish the theorem for arbitrary lengths; the universal quantifier is justified by the algebraic proof (1)–(3).

## Relationship to prior work
Acharya, Das, Milenkovic, Orlitsky, and Pan [1] formulated reconstruction from all substring compositions, proved general length-dependent reconstructability results, and exhibited the length-eight confusable pair above. Their general polynomial-factorization framework concerns **all composition layers**. The new claim identifies a particular sparse-weight subclass recoverable even after **discarding every zero- and one-one factor composition**; it does not claim the classical pair or full-spectrum problem as new.

Gupta and Mahdavifar [2] give algebraic reconstruction algorithms and codebooks under full substring-composition observation; their inspected statements do not give this two-heavy-layer injectivity for all three-one words. Ye and Elishco [3] primarily study prefix–suffix observations and other partial-data models, mathematically distinct from retaining all contiguous factors conditioned on their number of ones. Yang and Chen [4] study constant-weight *source strings* under prefix–suffix rather than all-factor observation, another distinct setting. Searches using the low-weight, sparse-marker, and equicomposability formulations did not identify an earlier identical theorem. This does **not** prove historical uniqueness; the adjacent literature is extensive.

## Limitations
The theorem requires multiplicities, exact counts, and precisely three ones. It does not apply to observations corrupted by missing counts, to arbitrary four-one strings, to scattered subsequences, or to circular factors. No statement is made about smaller measurement subsets or optimal noise resilience. The literature comparison is best effort, not an independent novelty certification.

## References
[1] J. Acharya, H. Das, O. Milenkovic, A. Orlitsky, S. Pan, *String Reconstruction from Substring Compositions*, arXiv:1403.2439v1 (first publicly submitted 2014-03-10), https://arxiv.org/abs/1403.2439 ; full author manuscript https://people.csail.mit.edu/jayadev/papers/str_rcn_sidma.pdf .

[2] U. Gupta, H. Mahdavifar, *A New Algebraic Approach for String Reconstruction from Substring Compositions*, arXiv:2201.09955, https://arxiv.org/abs/2201.09955 .

[3] Z. Ye, O. Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, arXiv:2208.14963, https://arxiv.org/abs/2208.14963 .

[4] Y. Yang, Z. Chen, *Reconstruction of Multiple Strings of Constant Weight from Prefix–Suffix Compositions*, arXiv:2411.03776v1, https://arxiv.org/abs/2411.03776 .
