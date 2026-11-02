# Exact Parikh-matrix distribution of maximally universal binary words at minimum letter support

## Finding

Fix integers \(k\ge 1\) and \(s\ge 0\). A word \(w\) is *\(k\)-subsequence universal* if each of the \(2^k\) binary words of length \(k\) is a scattered subsequence of \(w\). Let \(C(w)\) be the number of pairs of positions \(i<j\) with \(w_i=a\) and \(w_j=b\). Define
\[
U_{k,s}(z)=\sum_{\substack{w\in\{a,b\}^{2k+s}\\ |w|_a=k,\ \iota(w)=k}}z^{C(w)},
\]
where \(\iota(w)\) is the subsequence-universality index. Then the following is an identity of polynomials with nonnegative integer coefficients:
\[
\boxed{U_{k,s}(z)=z^{\binom{k}{2}}[u^s]\frac{1}{1-u z^k}\prod_{j=1}^{k}\left(z+\frac{1}{1-u z^{j-1}}\right).}
\]
In particular, for \(0\le C\le k(k+s)\), the *exact* proportion of \(k\)-universal words in the binary Parikh-matrix language with \(k\) letters \(a\), \(k+s\) letters \(b\), and \(C\) scattered occurrences of \(ab\) equals
\[
\boxed{\frac{[z^C]U_{k,s}(z)}{[z^C]\begin{bmatrix}2k+s\\k\end{bmatrix}_{z}}.}
\]
The denominator is strictly positive for this range of \(C\), and the bracket denotes the usual Gaussian binomial polynomial. The total number and its fixed-slack asymptotic are
\[
\boxed{U_{k,s}(1)=\sum_{j=0}^k\binom{k}{j}\binom{s+j}{j}\sim\frac{2^k k^s}{2^s s!}\qquad(k\to\infty,\ s\text{ fixed}).}
\]
Consequently, if a word is uniform among all words having \(k\) letters \(a\) and \(k+s\) letters \(b\), then
\[
\boxed{\Pr(\iota(w)=k)\sim \frac{\sqrt{\pi}}{4^s s!}\,k^{s+1/2}2^{-k}\qquad(k\to\infty,\ s\text{ fixed}).}
\]
The coefficient distribution is palindromic: \(U_{k,s}(z)=z^{k(k+s)}U_{k,s}(z^{-1})\).

## Assumptions and scope

The alphabet is exactly \(\{a,b\}\), with distinguishable symbols. All words are counted once as positional strings. There are no probabilistic independence assumptions. The parameters range over every integer \(k\ge1\) and \(s\ge0\). A word with only \(k\) copies of \(a\) cannot be \((k+1)\)-subsequence universal because it has no subsequence \(a^{k+1}\); hence the event \(\iota(w)=k\) is equivalent to \(k\)-universality in this domain. The Gaussian coefficient is defined by
\[
\begin{bmatrix}A+B\\A\end{bmatrix}_{z}=\sum_{\substack{w\in\{a,b\}^{A+B}\\|w|_a=A}}z^{C(w)}\quad (A,B\ge0).
\]
The asymptotic statements take \(s\) fixed as \(k\) grows; no uniformity in a growing \(s\) is asserted.

## Proof

**Greedy arches.** Scan from left to right, ending an arch at the first point when both symbols have occurred; repeat on the unused suffix. The terminal uncompleted suffix may be empty. Each completed arch contains at least one \(a\), and the number of completed arches equals the universality index. One direction follows by extracting one required symbol from each complete arch. For the converse, if only \(r\) arches complete, take in succession the terminal letter of each arch and append a letter absent from the unfinished suffix. Each terminal letter first appears at its own arch endpoint after the preceding greedy match, so this word of length \(r+1\) is absent as a subsequence. This is the standard greedy-arch characterization, stated and proved in the cited literature.

**Exhaustive structural decomposition.** If a word with exactly \(k\) copies of \(a\) has \(k\) complete arches, each arch must have precisely one \(a\), and the unfinished suffix has no \(a\). In each of the \(k\) arches, the only possibilities, uniquely determined by the greedy rule, are \(ab\) or \(b^{h+1}a\) with \(h\ge0\). The suffix is \(b^e\) with \(e\ge0\). Conversely, every choice of these arches and the suffix gives a word with exactly \(k\) greedy complete arches. The exact word/choice correspondence is bijective.

**Refined pair count.** Regard the first \(b\) in each completed arch as its baseline \(b\). For every pair of distinct arches \(i<j\), the \(a\) in arch \(i\) precedes the baseline \(b\) in arch \(j\). This supplies \(\binom{k}{2}\) scattered \(ab\) pairs. An \(ab\) arch contributes one additional internal pair and consumes no extra \(b\). In arch \(j\), a choice \(b^{h+1}a\) consumes \(h\) extra copies of \(b\), each of which follows precisely the \(j-1\) earlier copies of \(a\); it adds \((j-1)h\) pairs. Every trailing \(b\) follows all \(k\) copies of \(a\), adding \(k\) pairs. Marking extra copies of \(b\) with \(u\) and all \(ab\) pairs with \(z\) gives the arch factor \(z+\sum_{h\ge0}u^h z^{(j-1)h}=z+(1-u z^{j-1})^{-1}\), and suffix factor \(\sum_{e\ge0}u^e z^{ke}=(1-u z^k)^{-1}\). Exactly \(s\) extra copies of \(b\) must be distributed, proving the boxed polynomial.

**Parikh-matrix probabilities.** For fixed \(k,s\), the coefficient \([z^C]U_{k,s}(z)\) is exactly the number of words in the Parikh-matrix language that attain \(\iota=k\). The Gaussian polynomial counts all of the language's words by the same \(ab\) statistic. Every integer from \(0\) to \(k(k+s)\) is realized, so the ratio is well-defined.

**Totals, asymptotics, symmetry.** Set \(z=1\) in the polynomial to obtain
\[
U_{k,s}(1)=[u^s](1-u)^{-1}\bigl(1+(1-u)^{-1}\bigr)^k
=\sum_{j=0}^k\binom{k}{j}\binom{s+j}{s}.
\]
For fixed \(s\), this is \(2^k\mathbb E\binom{s+J}{s}\) with \(J\sim\mathrm{Binomial}(k,1/2)\). Because \(\binom{s+j}{s}=j^s/s!+O_s((j+1)^{s-1})\) for \(s\ge1\), while \(J/k\to1/2\) in every fixed moment, the first asymptotic follows; for \(s=0\) it holds exactly with total \(2^k\). There are \(\binom{2k+s}{k}\sim 4^k2^s/\sqrt{\pi k}\) words with the prescribed letter counts, yielding the displayed probability. Finally, reversal of words preserves subsequence universality and maps the \(ab\) count \(C\) to \(k(k+s)-C\). This bijection proves palindromicity.

## Verification

The standalone `verification.py` computes the polynomial coefficients by independent formal product convolution. It separately enumerates **every** positional binary word for \(1\le k\le7\), \(0\le s\le4\), computes its greedy arch count directly, and compares complete \(ab\)-count histograms (35 exhaustive cases). Another 160 parameter cases check the product against the separately derived closed total, reversal symmetry, and extremal support. The script and its exact recorded output accompany this result. These finite tests check arithmetic and indexing only; the infinite-parameter proof above is symbolic.

For example, at \(k=3,s=1\), there are exactly \(20\) universal words among \(35\) fixed-composition words, with consecutive \(C\)-counts \(1,3,4,4,4,3,1\) on \(C=3,4,5,6,7,8,9\).

## Relationship to prior work

Fazekas, Huang, and Mercaş (2026), *Subsequence Analysis Problems for Binary Parikh Matrices*, studies exactly the languages \(L_{A,B,C}\). Their Theorem 3.3 gives necessary and sufficient arithmetic inequalities for **existence** of a \(k\)-universal representative; their Section 5 studies approximation of **fixed-pattern** subsequence-containment probabilities. Lemma 2.1 provides the greedy-arch characterization and Lemma 3.2 counts pair contributions for minimal-length arches. These known facts are inputs and are not claimed as new. The additional result here is an exact \(C\)-refined count of *all* maximally universal representatives for the infinite family \(A=k,B=k+s\), together with its fixed-slack rarity constant.

Barker and collaborators (2020) establish the standard arch treatment of scattered-factor universality. Other available finite-length universality tallies sum over compositions and do not specify the inversion/Parikh-matrix distribution. A previously published equivalent refined product formula is a residual priority risk; mathematical novelty is not established by absence from searches alone.

## Limitations

The refinement assumes that one alphabet symbol occurs precisely \(k\) times, so maximal universality consumes all occurrences of that symbol. For general \(A>k\) the arch types and suffix require additional variables, and the present product is not asserted to apply. The asymptotic does not allow \(s\) to grow with \(k\). The formula is explicit but does not guarantee polynomial-time evaluation in the **bitlength** of \(k,s,C\). No independent audit has been performed.

## References

1. S. Z. Fazekas, X. Huang, and R. Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices*, arXiv:2610.06717, first posted October 5, 2026. https://arxiv.org/abs/2610.06717
2. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, and D. Nowotka, *Scattered factor-universality of words*, Developments in Language Theory, 2020. https://doi.org/10.1007/978-3-030-48516-0_2
3. J.-J. Hébrard, *An algorithm for distinguishing efficiently bit-strings by their subsequences*, Theoretical Computer Science **82** (1991), 35–49. https://doi.org/10.1016/0304-3975(91)90170-7
