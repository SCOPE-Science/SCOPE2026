# Harmonic inverse Lyndon prefixes and geometric border laws

## Finding

Fix an ordered alphabet of size \(q\geq 2\). Define
\[
L_q(m)=\frac{1}{m}\sum_{d\mid m}\mu(d)q^{m/d},\qquad C_q(k)=\sum_{m=1}^{k}L_q(m).
\]
An inverse Lyndon word is a nonempty word strictly lexicographically larger than each of its proper nonempty suffixes. Then, for each integer \(k\geq1\), there are exactly \(C_q(k)\) inverse Lyndon words of length \(k\); of those, exactly \(L_q(k-b)\) have longest proper border length \(b\), for each \(0\leq b<k\).

Let \(W_k\) be uniform among the length-\(k\) inverse Lyndon words, and \(B_k\) its longest-border length. For every fixed integer \(b\geq0\),
\[
\Pr(B_k=b)=\frac{L_q(k-b)}{C_q(k)}\xrightarrow[k\to\infty]{}(1-q^{-1})q^{-b},\qquad
\mathbb E[B_k]\xrightarrow[k\to\infty]{}\frac{1}{q-1}.
\]
The probability is interpreted as zero for \(b\geq k\).

Now let \(X_n\) be uniformly distributed over all words of length \(n\). At position \(i\), let \(\Lambda_n(i)\) be the maximum length of an inverse Lyndon factor starting there, among the available \(n-i+1\) symbols. For \(1\leq k\leq n\),
\[
\Pr(\Lambda_n(1)\geq k)=\frac{C_q(k)}{q^k}
=\frac{q}{(q-1)k}+O_q(k^{-2}).
\]
Consequently the expected *total entry mass* of the inverse Lyndon array has the exact finite-length expression and sharp first-order asymptotic
\[
\mathbb E\left[\sum_{i=1}^{n}\Lambda_n(i)\right]
=\sum_{k=1}^{n}(n-k+1)\frac{C_q(k)}{q^k}
=\frac{q}{q-1}\,n\log n+O_q(n).
\]
In particular, \(\mathbb E[\Lambda_n(1)]=\frac{q}{q-1}\log n+O_q(1)\). Natural logarithms are used.

## Assumptions and scope

The alphabet order is fixed, the word distribution for the array statements is uniform and independent across positions, and \(q\geq2\) is fixed when asymptotic notation is used. A border is a prefix that is also a suffix, strictly shorter than the whole word; the empty border has length zero. An anti-Lyndon word is the strictly lexicographically largest rotation in a primitive conjugacy class. The source characterization that inverse Lyndon words are precisely nonempty prefixes of positive powers of anti-Lyndon words is used as an *existing theorem*, not claimed as new. Results about \(B_k\) condition on a word being inverse Lyndon; they make no assertion about the border of the *maximal* inverse Lyndon factor of a random text.

## Proof

**1. Unique anti-Lyndon root and its border length.** By Bonizzoni--De Felice--Zaccagnino--Zizza (2018, Proposition 7.21), every inverse Lyndon word \(w\) of length \(k\) is the length-\(k\) prefix of \(u^\infty\), where \(u\) is an anti-Lyndon word of some length \(m\leq k\). Conversely every such prefix is inverse Lyndon. Anti-Lyndon words are unbordered, as they are Lyndon words for the reversed alphabet order.

The root is unique. If two anti-Lyndon roots \(u\) and \(v\), of lengths \(m<r\leq k\), give the same length-\(k\) prefix, then \(v\), as the initial \(r\)-letter segment of \(u^\infty\), has period \(m\), and therefore a nonempty proper border of length \(r-m\), contrary to its unborderedness. Equal-length roots plainly coincide. The length-\(k\) prefix of \(u^\infty\) has period \(m\), hence border length \(k-m\), with the empty border permitted. If it had a longer proper border, it would have a smaller positive period, which would restrict to a smaller period of \(u\), contradicting the unborderedness of \(u\). Thus its *longest* proper border has length exactly \(k-m\).

**2. Enumerating by root and border.** An anti-Lyndon word of length \(m\) is the unique maximum rotation of a primitive necklace. The classical necklace count is \(L_q(m)\). The map taking each anti-Lyndon root of length at most \(k\) to the length-\(k\) prefix of its infinite periodic extension is bijective by step 1. This proves both the total \(C_q(k)\) and the longest-border count \(L_q(k-b)\). Dividing by \(C_q(k)\) gives the exact conditional distribution.

**3. Geometric limit and its mean.** Möbius inversion gives, for fixed \(q\geq2\),
\[
L_q(m)=\frac{q^m}{m}+O_q(q^{m/2}),\qquad
C_q(k)=\frac{q^{k+1}}{(q-1)k}\bigl(1+O_q(k^{-1})\bigr).
\]
Indeed, proper divisors in the Möbius sum have exponents at most \(m/2\); the geometric weighted sum \(\sum_{m\leq k}q^m/m\) is \(q^{k+1}/((q-1)k)+O_q(q^k/k^2)\), splitting at \(m=k/2\) to justify the error uniformly. Consequently, for each fixed \(b\geq0\), the displayed probability tends to \((1-1/q)q^{-b}\).

For convergence of means, use \(L_q(m)\leq q^m/m\) (every primitive necklace has \(m\) distinct words), and the lower bound \(C_q(k)\gg_q q^k/k\). In the range \(0\leq b\leq k/2\), these imply \(\Pr(B_k=b)\ll_q q^{-b}\). In the complementary range the total contribution to \(\mathbb E[B_k]\) is \(O_q(k^2q^{-k/2})\). Dominated convergence on the first range proves \(\mathbb E[B_k]\to\sum_{b\geq0}b(1-q^{-1})q^{-b}=1/(q-1)\).

**4. Array prefix tail and total expectation.** It is known, and elementary from the defining suffix comparison, that every nonempty prefix of an inverse Lyndon word is inverse Lyndon (Bonizzoni et al. 2018; also Negri et al. 2026, Lemma 6). Therefore \(\{\Lambda_n(1)\geq k\}\) is exactly the event that the first \(k\) symbols are inverse Lyndon. There are \(C_q(k)\) such prefixes among \(q^k\) equally likely possibilities. By stationarity of the independent symbols, at any position \(i\), \(\Pr(\Lambda_n(i)\geq k)=C_q(k)/q^k\) whenever \(k\leq n-i+1\). The integer tail-sum formula followed by linearity of expectation gives
\[
\mathbb E\Bigl[\sum_{i=1}^n\Lambda_n(i)\Bigr]
=\sum_{i=1}^n\sum_{k=1}^{n-i+1}\frac{C_q(k)}{q^k}
=\sum_{k=1}^n(n-k+1)\frac{C_q(k)}{q^k}.
\]
The estimate in step 3 yields \(C_q(k)/q^k=q/((q-1)k)+O_q(k^{-2})\). Using \(\sum_{k\leq n}1/k=\log n+O(1)\), and \(\sum_{k\leq n}(n-k+1)/k=n\log n+O(n)\), gives the asserted leading coefficient and additive remainder. The same tail-sum argument proves the first-entry expectation.

## Verification

The accompanying dependency-free `check.py` implements two independent finite descriptions: direct proper-suffix comparison and enumeration of primitive lexicographically maximal rotations followed by periodic-prefix matching. It checks uniqueness of the root, maximal border, all finite counts, and both direct and predicted array lengths on test words. Its recorded output is in `verification_output.txt`. Exhaustive checks cover every binary word through length \(12\) and every ternary word through length \(8\). They support, but do not substitute for, the infinite proof above. Direct evaluations of the exact expectation at lengths \(100\) and \(1000\) are included for illustration.

To reproduce: run `python3 check.py` in the same directory as the verification output file. No external software package, database, or online service is required.

## Relationship to prior work

The 2018 inverse Lyndon characterization and the classical primitive-necklace formula are credited prerequisites; counting anti-Lyndon roots is not, by itself, the new contribution. Negri--Sica--Zaccagnino--Zizza (March 18, 2026) introduce and construct the inverse Lyndon array in linear time, and De Felice et al. (September 20, 2026) extend its algorithmic properties. Both address border correction structurally and report random-input runtime experiments, but the inspected works do not give the harmonic prefix-tail, geometric conditional-border law, or expected total entry-mass coefficient here. Bonizzoni et al. (2019/2020) prove boundary restrictions on borders of consecutive canonical factors, not this conditioned enumeration or random-array expectation. Probabilistic counts of distinct substrings and subsequence-universality statistics concern different random variables and do not imply the present formulas.

## Limitations

The results are for fixed finite uniform alphabets, not arbitrary biased or dependent sources. The expected sum of inverse Lyndon array lengths is a mathematical statistic, not a claim that any particular construction algorithm takes \(\Theta(n\log n)\) time. The geometric law conditions on independently uniform selection from the set of inverse Lyndon words at a fixed length; it does not model selecting the maximal inverse Lyndon prefix from a random text. The conclusions use established structural characterization and elementary necklace counting, so that antecedent is explicitly identified. Unindexed literature might include equivalent probabilistic consequences. Independent verification has not been performed.

## References

1. P. Negri, M. Sica, R. Zaccagnino, R. Zizza, *The Inverse Lyndon Array: Definition, Properties, and Linear-Time Construction*, arXiv:2603.17537v1, March 18, 2026. https://arxiv.org/html/2603.17537
2. C. De Felice, P. Negri, M. Sica, R. Zaccagnino, R. Zizza, *The Inverse Lyndon Array*, arXiv:2609.23401, September 20, 2026. https://arxiv.org/pdf/2609.23401
3. P. Bonizzoni, C. De Felice, R. Zaccagnino, R. Zizza, *Inverse Lyndon words and inverse Lyndon factorizations of words*, arXiv:1705.10277, 2017; *Advances in Applied Mathematics* **101** (2018), 281–319, especially Proposition 7.21. https://arxiv.org/pdf/1705.10277
4. P. Bonizzoni, C. De Felice, R. Zaccagnino, R. Zizza, *Lyndon words versus inverse Lyndon words: queries on suffixes and bordered words*, arXiv:1911.01851, November 2, 2019. https://arxiv.org/pdf/1911.01851
5. Classical primitive-necklace formula obtained by Möbius inversion (standard; included explicitly in the proof).
