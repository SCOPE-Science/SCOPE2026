# Palindromic subsequence spectra of repeated alphabet permutations

## Finding

Let \(q\ge 3\) and \(k\ge 1\) be integers, let \(A=\{a_1,\ldots,a_q\}\) be a labeled alphabet of distinct symbols, and let
\[
W_{q,k}=(a_1a_2\cdots a_q)^k.
\]
Write \(\mathcal P(W)\) for the set of **distinct, nonempty palindromic scattered subsequence words** of \(W\), counted once regardless of their number of embeddings. Define the length enumerator
\[
F_{q,k}(t)=\sum_{p\in\mathcal P(W_{q,k})}t^{|p|},\qquad F_{q,0}(t)=0.
\]
Then the entire length spectrum, simultaneously for all \(q\ge3\) and \(k\ge1\), has the rational generating function
\[
\boxed{\sum_{k\ge0}F_{q,k}(t)z^k=\frac{qzt(1+zt)}{(1-z)\bigl(1-z t^2(q-1+z)\bigr)}.}
\]
In particular, the total number \(P_q(k)=F_{q,k}(1)\) satisfies
\[
\boxed{\sum_{k\ge0}P_q(k)z^k=\frac{qz(1+z)}{(1-z)\bigl(1-(q-1)z-z^2\bigr)}.}
\]
Let \(\Delta_k=P_q(k)-P_q(k-1)\) for \(k\ge1\), with \(P_q(0)=0\). Then
\[
\Delta_1=q,\qquad \Delta_2=q^2,\qquad \Delta_k=(q-1)\Delta_{k-1}+\Delta_{k-2}\quad(k\ge3).
\]
The longest scattered palindrome has length exactly \(2k-1\), with exactly \(q(q-1)^{k-1}\) different palindromes attaining that length. By contrast, \(W_{q,k}\) has exactly \(q\) nonempty palindromic **contiguous factors**, all of length one. The total scattered-palindrome count has exponential growth rate
\[
\lim_{k\to\infty}P_q(k)^{1/k}=\frac{q-1+\sqrt{(q-1)^2+4}}2.
\]
For illustration, \((P_3(1),\ldots,P_3(6))=(3,12,33,84,207,504)\) and \((P_4(1),\ldots,P_4(6))=(4,20,72,244,812,2688)\).

## Assumptions and scope

An embedding of a finite word \(u=u_1\cdots u_s\) in \(W_{q,k}\) is a strictly increasing selection of positions spelling \(u\). Only distinct resulting words are counted. The alphabet is ordered in the order \(a_1,\ldots,a_q\) occurring in each block. Changing that order by a consistent permutation of the symbols gives an isomorphic statement. The proof also works for \(q=2\); the stated new scope is \(q\ge3\), since binary alternating words have a previously available separate length-spectrum calculation.

For a nonempty palindrome \(p\) of length \(2m+1\) or \(2m\), let \(h\) be its first \(m+1\) letters in the odd case, and its first \(m\) letters in the even case. Let \(e(h)\) count adjacent equal-letter pairs in \(h\). The exact membership characterization, a part of the theorem, is
\[
\boxed{p\in\mathcal P(W_{q,k})\quad\Longleftrightarrow\quad m+e(h)+1\le k.}
\]
All quantifiers above hold for every fixed labeled alphabet with \(q\ge3\) and for every positive integer \(k\).

## Proof

**1. Minimum permutation-block requirement.** For an arbitrary nonempty word \(u=u_1\cdots u_s\) on the ordered alphabet, set
\[
d(u)=\#\{i:1\le i<s,\ u_{i+1}\le u_i\},
\]
where the inequality compares alphabet ranks. Inside one block \(a_1\cdots a_q\), selected ranks must increase strictly. Therefore every weak descent in \(u\) forces advancement to another block. Conversely, embed the first symbol into the first block, retain the current block precisely on a strict ascent, and advance one block at each weak descent. This greedy embedding is always valid, as every block contains each letter once and in increasing order. Hence
\[
u\text{ embeds in }W_{q,k}\quad\Longleftrightarrow\quad 1+d(u)\le k.
\]
No unproved optimality assertion is hidden here: the first direction follows from the strict order inside each block, and the reverse direction is the explicit greedy construction.

**2. Palindromic symmetry.** Write an odd palindrome as \(p=h h'\) with \(h\) of length \(m+1\), where \(h'\) is the reversal of the first \(m\) letters of \(h\). The \(2m\) adjacent transitions pair into \(m\) mirrored pairs. If the letters of an adjacent pair in \(h\) are different, exactly one of the two mirrored transitions is a weak descent; if they are equal, both are weak descents. Consequently \(d(p)=m+e(h)\). For an even palindrome \(p=hh^{\mathrm R}\) with \(|h|=m\), the central equal-letter transition contributes one weak descent, and the remaining \(m-1\) mirrored transition pairs contribute \(m-1+e(h)\). Again \(d(p)=m+e(h)\). This proves the displayed membership test in both parities.

**3. Enumeration at each length.** Every palindrome is uniquely determined by its first half \(h\), so duplicate embeddings do not arise in the counting. A word of length \(r\ge1\) on a \(q\)-letter alphabet with exactly \(e\) equal adjacent pairs can be chosen in
\[
q\binom{r-1}{e}(q-1)^{r-1-e}
\]
ways: choose the first letter, the \(e\) equality locations, and a different next letter at each remaining transition. Thus for every \(m\ge0\) the number of odd palindromes of length \(2m+1\) requiring exactly \(1+m+e\) blocks is
\[
q\binom{m}{e}(q-1)^{m-e},\qquad 0\le e\le m.
\]
For every \(m\ge1\), the number of even palindromes of length \(2m\) requiring exactly \(1+m+e\) blocks is
\[
q\binom{m-1}{e}(q-1)^{m-1-e},\qquad 0\le e\le m-1.
\]
Restricting the block requirement to at most \(k\) gives each coefficient of \(F_{q,k}(t)\) explicitly. In particular,
\[
[t^{2m+1}]F_{q,k}(t)=q\sum_{e=0}^{\min\{m,k-m-1\}}\binom{m}{e}(q-1)^{m-e},
\]
and, for \(m\ge1\),
\[
[t^{2m}]F_{q,k}(t)=q\sum_{e=0}^{\min\{m-1,k-m-1\}}\binom{m-1}{e}(q-1)^{m-1-e},
\]
with the convention that a sum whose upper index is negative equals zero.

**4. Generating functions.** First count palindromes by their *least* number of required blocks, using \(z\) for that number and \(t\) for length. The preceding formulas and the binomial theorem give
\[
\begin{aligned}
D_q(z,t)&=\sum_{m\ge0}qz^{m+1}t^{2m+1}(q-1+z)^m\\
&\quad+\sum_{m\ge1}qz^{m+1}t^{2m}(q-1+z)^{m-1}\\
&=\frac{qzt}{1-zt^2(q-1+z)}+\frac{qz^2t^2}{1-zt^2(q-1+z)}\\
&=\frac{qzt(1+zt)}{1-zt^2(q-1+z)}.
\end{aligned}
\]
A palindrome requiring \(r\) blocks is present for every \(k\ge r\), so summing its contribution across all \(k\) multiplies by \(1/(1-z)\). This proves the bivariate formula; setting \(t=1\) proves the total-count formula.

**5. Extremal length and growth.** The membership test forces \(m\le k-1\). The largest possible odd length is \(2k-1\), achieved by halves of length \(k\) with no adjacent equal symbols; their number is \(q(q-1)^{k-1}\). Even palindromes have length at most \(2k-2\). For \(q\ge3\), the word \(W_{q,k}\) has neither adjacent equal symbols nor any equal symbols at distance two, even across block boundaries. Thus no contiguous palindrome can have a central two-letter or three-letter palindrome, and all nonempty contiguous palindromes are the \(q\) distinct individual letters. Finally, the dominant root in \(z\) of \(1-(q-1)z-z^2\) is the positive reciprocal of \((q-1+\sqrt{(q-1)^2+4})/2\), and has no cancellation in the nonnegative-coefficient generating function. Standard rational-series asymptotics yield the claimed growth rate. This completes the proof.

## Verification

A standalone standard-library Python checker, `tools/verify.py`, is embedded in the package. Execute `python tools/verify.py` from the package root. It independently generates **all distinct subsequences** by successive set updates and filters palindromes, rather than using the block-count argument. It compares the complete length histograms to the closed binomial formulas for 21 alphabet/block parameter pairs, including alphabets through size six and block counts through seven. It checks an independent candidate-by-candidate greedy embedding implementation where practical, 150 full alphabet permutations in specified small cases, and additional combinatorial boundary cases through \(q=10\), \(k=12\). The expected terminal line is `ALL_REPEATED_PERMUTATION_PALINDROME_CHECKS_PASSED main_pairs 21 permutations 150 q_range 2..10 k_range 1..12`. The infinite statements are established by the proof above, not by finite tests.

## Relationship to prior work

Pandoh’s public seminar presentation (June 21, 2021), followed by Mahalingam and Pandoh, *Counting scattered palindromes in a finite word* (arXiv:2108.02729, first preprint version August 5, 2021), study general bounds for the number of distinct scattered palindromes, extremal examples, and in particular count certain length-three palindromes of two-copy alphabet-permutation words. Their Theorem 5.4 concerns a maximal value when the number of distinct symbols is at least half the word length. It does not furnish the arbitrary-\(k\), length-refined formula above for a repeated fixed permutation, whose alphabet size \(q\) is fixed while the word length grows as \(qk\). An algorithm able to calculate counts for each finite input does not itself provide this uniform symbolic spectrum.

Müllner and Ryzhikov, *Palindromic Subsequences in Finite Words* (arXiv:1901.07502, 2019), analyze longest-palindrome existence and bounds, especially for circular words and concatenations of differently sized constant blocks. They do not count the distinct palindromic subsequences of the repeated-permutation word by length. The binary-alternating specialization \(q=2\) is not claimed as a new result.

## Limitations

This theorem counts distinct palindromic **scattered subsequence words**, not their positional embeddings, and makes no statement about extremal words of length \(qk\) among all words with \(q\) symbols. It does not classify concatenations of different permutations or count near-palindromes. The bibliographic searches cannot exclude an independently known equivalent formula in unindexed literature. The finite checker is corroboration rather than a proof for unbounded \(q\) or \(k\).

## References

1. P. Pandoh, *Counting scattered palindromes in finite words*, Combinatorics on Words seminar, June 21, 2021. https://www.i2m.univ-amu.fr/wiki/Combinatorics-on-Words-seminar/_media/seminar2021%3A20210621pandoh.pdf
2. K. Mahalingam and P. Pandoh, *Counting scattered palindromes in a finite word*, arXiv:2108.02729, first posted 2021-08-05. https://arxiv.org/pdf/2108.02729
3. C. Müllner and A. Ryzhikov, *Palindromic Subsequences in Finite Words*, arXiv:1901.07502, 2019. https://arxiv.org/pdf/1901.07502
