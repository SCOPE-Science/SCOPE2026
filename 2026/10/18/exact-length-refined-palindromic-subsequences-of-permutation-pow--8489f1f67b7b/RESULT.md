# Exact length-refined palindromic subsequences of permutation powers

## Finding

Fix an integer \(q\ge2\), a permutation \(P=p_0p_1\cdots p_{q-1}\) of \(q\) distinct letters, and an integer \(m\ge1\). Let \(W=P^m\) be the concatenation of \(m\) copies of \(P\). Count **distinct nonempty palindromic scattered subsequence words** of \(W\), not position embeddings. Let \(C_{q,m}(\ell)\) be their number of length \(\ell\).

For every integer \(t\) with \(0\le t\le m-1\),
\[
C_{q,m}(2t+1)=q\sum_{e=0}^{\min\{t,m-t-1\}}\binom{t}{e}(q-1)^{t-e}.
\]
For every integer \(t\) with \(1\le t\le m-1\),
\[
C_{q,m}(2t)=q\sum_{e=0}^{\min\{t-1,m-t-1\}}\binom{t-1}{e}(q-1)^{t-1-e}.
\]
All other positive lengths have count zero. The complete bivariate generating function is
\[
\sum_{m\ge0}\sum_{\ell\ge1}C_{q,m}(\ell)u^\ell z^m
=\frac{quz(1+uz)}{(1-z)\bigl(1-u^2z(q-1+z)\bigr)},
\]
where the empty repetition \(m=0\) contributes zero. Consequently, the maximum palindrome length is \(2m-1\), with exactly \(q(q-1)^{m-1}\) different palindromes attaining it. The total number \(T_{q,m}=\sum_{\ell\ge1}C_{q,m}(\ell)\) has generating function
\[
\sum_{m\ge0}T_{q,m}z^m=\frac{qz(1+z)}{(1-z)(1-(q-1)z-z^2)},
\]
initial values \(T_{q,0}=0\), \(T_{q,1}=q\), \(T_{q,2}=q(q+1)\), and recurrence, for all \(m\ge3\),
\[
T_{q,m}=qT_{q,m-1}-(q-2)T_{q,m-2}-T_{q,m-3}.
\]
For each fixed \(q\ge2\), growth is \(T_{q,m}=\Theta_q(\lambda_q^m)\), where
\[
\lambda_q=\frac{q-1+\sqrt{(q-1)^2+4}}2.
\]

## Assumptions and scope

A word \(v=v_1\cdots v_s\) is a scattered subsequence of \(W\) if positions strictly increasing in \(W\) spell \(v\). Equality of output words, rather than equality of position sets, defines distinctness. A palindrome reads identically from both ends. Order alphabet letters by their positions within \(P\), so \(p_0<p_1<\cdots<p_{q-1}\); this is a proof device, not an assumption about their external labels. Binomial coefficients are ordinary integers and the displayed sums are finite. All assertions hold for each choice of \(q,m,P\) in the stated ranges, without a limiting or generic-position assumption.

## Proof

**Greedy embedding lemma.** For a nonempty word \(v=v_1\cdots v_s\) over the letters of \(P\), put
\[
d(v)=\#\{i\in\{1,\ldots,s-1\}:v_i\ge v_{i+1}\}.
\]
Within one period \(P\), strictly increasing letter indices appear in order; equal or decreasing successive indices force a new period. Thus any embedding uses at least \(1+d(v)\) periods. Conversely, embed the first letter in the first period and greedily put each next letter in the current period exactly when it is larger than its predecessor, otherwise in the next period. Every requested letter occurs there, establishing the exact equivalence
\[
v\preceq P^m\quad\Longleftrightarrow\quad 1+d(v)\le m.
\]
This construction respects endpoints, including a first or last letter at a period boundary.

**Palindromic weak descents.** Every odd palindrome of length \(2t+1\) is uniquely \(h\) followed by the reversal of the first \(t\) letters of \(h\), with \(|h|=t+1\). Let \(e(h)\) be the number of equal adjacent pairs of \(h\). Each of the \(t\) adjacent pairs in \(h\) has a mirrored adjacent pair in the other half of the palindrome. If the letters differ, exactly one of the two directed comparisons is weakly descending; if equal, both comparisons are. Hence \(d(v)=t+e(h)\).

Every even palindrome of length \(2t\) is uniquely \(h\operatorname{rev}(h)\), with \(|h|=t\). The middle equal pair contributes one weak descent, and the other \(t-1\) mirrored pairs contribute \(t-1+e(h)\), so again \(d(v)=t+e(h)\). Therefore both parities are present exactly when \(t+e(h)\le m-1\).

**Enumerating distinct words.** For a first-half string \(h\) of length \(s\ge1\), choose its initial letter in \(q\) ways. To obtain exactly \(e\) equal adjacent pairs choose their locations among \(s-1\) links; at each other link choose one of \(q-1\) different letters. There are exactly
\[
q\binom{s-1}{e}(q-1)^{s-1-e}
\]
such halves. Mapping each half to its full odd/even palindrome is injective. Substituting \(s=t+1\) or \(s=t\) and restricting to \(e\le m-t-1\) proves both formulas. In particular the odd case requires \(t\le m-1\) and the even case \(1\le t\le m-1\), hence the asserted support. The longest words have odd length \(2m-1\), correspond to \(e=0\), and number \(q(q-1)^{m-1}\).

**Generating functions.** For each choice of \(t,e\), the *minimum* admissible period count is \(1+t+e\); the same word remains admissible for every larger \(m\). The odd-half enumerator, summed over arbitrary \(t\), is
\[
quz\sum_{t\ge0}\bigl(u^2z(q-1+z)\bigr)^t
=\frac{quz}{1-u^2z(q-1+z)}.
\]
For even palindromes, summing the \(t-1\) links and the extra middle letter produces
\[
\frac{qu^2z^2}{1-u^2z(q-1+z)}.
\]
Multiplying their sum by \(1/(1-z)\) accounts for all period counts at least the minimum and gives the stated bivariate rational function. Set \(u=1\) to obtain the total-count function. Its denominator expands to \(1-qz+(q-2)z^2+z^3\), which gives the initial values and recurrence by coefficient comparison.

The factor \(1-(q-1)z-z^2\) has positive simple reciprocal growth root \(\lambda_q\), with its other root of smaller absolute value when \(q\ge2\). The remaining pole at \(z=1\) is also farther from the origin, except that \(\lambda_q>1\) ensures it remains subdominant. The leading residue is nonzero and positive because the total generating function has a positive numerator at \(z=\lambda_q^{-1}\). Standard partial fractions therefore give \(T_{q,m}=\Theta_q(\lambda_q^m)\).

## Verification

Run `python3 check_spectrum.py` with Python's standard library. For 17 feasible small \((q,m)\) pairs with \(q\in\{2,3,4,5\}\) and \(qm\le17\), the program constructs every scattered subsequence from all nonzero position masks, deduplicates palindromic strings, and compares the exact length distribution against both displayed formulas and an independently summed coefficient representation. A second independent algorithm uses interval dynamic programming for *distinct* palindromic subsequences; it verifies total counts and the rational recurrence for 138 additional alphabet/period cells. Nine alphabet-size/period classes were tested under all letter permutations. All tests passed; the exact output is in `verification_output.txt`. These finite computations are corroboration, not the proof for arbitrary \(q,m\).

For instance, the total counts for the binary case start \(2,6,12,22,38\), and for the ternary case \(3,12,33,84,207\).

## Relationship to prior work

Müllner and Ryzhikov (2019) study longest palindromic subsequences of finite and circular words and specifically note that a binary alternating word has a palindromic subsequence of length one less than the source word (Section 4, before Proposition 16). Thus the binary longest-length special case is prior knowledge, not a new independent result. Their inspected original paper does not provide the present whole length spectrum, all-alphabet counts, or bivariate generating function. Brodal, Fagerberg, and Rysgaard (2024) analyze algorithmic correctness of recovering a longest palindrome through longest-common-subsequence backtracking, not length-refined enumeration for powers of an arbitrary alphabet permutation. Amarilli and coauthors (2025) give existence/optimization algorithms for regular-expression-constrained scattered subsequence matching; the language of all palindromes over an alphabet of size at least two is not regular, and no periodic-power palindromic counting theorem is derived there. Hasan, Islam, Rahman, and Sen (2017) introduce palindromic subsequence automata for general strings; their published abstract/first-page preview establishes a general representation and could in principle support counting, but access to their complete argument was not obtained. The explicit closed forms above are not inferred as already present in that general automata result.

## Limitations

The claim counts distinct *scattered* palindromes, not contiguous palindromic factors and not distinct position embeddings; replacing either convention changes the answer. No arbitrary nonperiodic-word theorem or efficient algorithm for arbitrary input strings is claimed. The binary maximum-length component is known from the 2019 primary source. The 2017 automata article was not fully accessible, and an equivalent closed-form specialization in unindexed literature cannot be excluded. The attached checker is finite and offers no independent validation of the general proof.

## References

1. C. Müllner and A. Ryzhikov, *Palindromic Subsequences in Finite Words*, 2019, arXiv:1901.07502, https://arxiv.org/abs/1901.07502 (original full text, especially Section 4 and Proposition 16).
2. G. S. Brodal, R. Fagerberg, and C. M. Rysgaard, *On Finding Longest Palindromic Subsequences Using Longest Common Subsequences*, ESA 2024, DOI:10.4230/LIPIcs.ESA.2024.35, https://doi.org/10.4230/LIPIcs.ESA.2024.35.
3. A. Amarilli, B. Dudek, F. Manea, T. Ringleb, and M. L. Schmid, *Linear Time Subsequence and Supersequence Regex Matching*, arXiv:2504.16288, first posted 2025-04-22, https://arxiv.org/abs/2504.16288 (the 2026 full version includes five authors).
4. M. M. Hasan, A. S. M. S. Islam, M. S. Rahman, and A. Sen, *Palindromic Subsequence Automata and Longest Common Palindromic Subsequence*, Mathematics in Computer Science 11 (2017), 219–232, DOI:10.1007/s11786-016-0288-7, https://doi.org/10.1007/s11786-016-0288-7 (abstract and publisher preview available).
