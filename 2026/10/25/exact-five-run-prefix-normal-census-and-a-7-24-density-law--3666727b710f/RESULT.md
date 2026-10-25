# Exact five-run prefix-normal census and a 7/24 density law

## Finding

A binary word is *prefix normal* (with respect to the symbol \(1\)) if, for every length \(k\), the prefix of length \(k\) has at least as many ones as every length-\(k\) factor. Let \(p_n\) be the number of prefix-normal words of length \(n\) that have exactly five nonempty maximal constant runs and begin and end with \(1\). Every such word is uniquely
\[
w=1^a0^b1^c0^d1^e,\qquad a,b,c,d,e\in\mathbb{Z}_{\ge1},\quad a+b+c+d+e=n.
\]
Then \(p_n=0\) for \(n<5\), and the ordinary generating function is exactly
\[
P(z)=\sum_{n\ge5}p_nz^n
=\frac{z^5(1+z+2z^2+2z^3+z^4)}{(1-z)^5(1+z)^3(1+z+z^2)}.
\]
In particular,
\[
p_n=\frac{7}{576}n^4+O(n^3),\qquad
\lim_{n\to\infty}\frac{p_n}{\binom{n-1}{4}}=\frac7{24}.
\]
The first seven nonzero counts (lengths \(5\) through \(11\)) are \(1,2,7,13,27,44,75\).

The exact run-length classification used to derive the count is
\[
1^a0^b1^c0^d1^e\text{ is prefix normal}
\quad\Longleftrightarrow\quad
c\le a,\quad e\le a,\quad (c+e\le a\ \text{or}\ d\ge b).
\]
The new enumerative assertion is the displayed rational function and its limiting density; the general gap/position test for prefix normality is already known in the literature.

## Assumptions and scope

All exponents \(a,b,c,d,e\) are positive integers. Factors are contiguous and may start at any position; the complete word and its prefixes are included. The alphabet is precisely \(\{0,1\}\). The class has exactly three runs of ones separated by exactly two runs of zeros, without initial or trailing zero runs. This is a count of **words**, not of prefix-normal equivalence classes and not of all prefix-normal words. The denominator \(\binom{n-1}{4}\) is the number of positive compositions of \(n\) into five parts, hence of all words of this form.

## Proof

**1. From factors to gap sums.** Let a word start with \(1\), and write the gaps between successive ones as \(g_1,\ldots,g_{N-1}\), where \(g_i\) counts intervening zeros and \(N\) is its total number of ones. For every \(1\le k<N\), the shortest contiguous factor containing \(k+1\) ones has length
\[
k+1+\min_{0\le j\le N-k-1}\sum_{i=j+1}^{j+k}g_i.
\]
The shortest prefix containing \(k+1\) ones has length \(k+1+\sum_{i=1}^kg_i\). Thus the word is prefix normal exactly when, for every \(k\) and every applicable \(j\),
\[
\sum_{i=1}^k g_i\le\sum_{i=j+1}^{j+k}g_i.
\tag{1}
\]
Indeed, if some \(k+1\) ones fit in a shorter factor, that factor has more ones than the prefix of its own length; conversely any violating factor containing \(k+1\) ones provides such a shorter span. This also proves the boundary cases \(k=0\) and \(k=N\) trivially.

**2. Solve the two-spike inequalities.** For the five-run word, the gaps are zero except at positions \(a\) and \(a+c\), carrying weights \(b\) and \(d\). If \(c>a\) or \(e>a\), a length-\(a\) gap window wholly inside one of the later all-zero stretches has sum zero, whereas the length-\(a\) prefix has sum \(b>0\); hence prefix normality fails. Assume now \(c,e\le a\).

If \(k<a\), the prefix gap sum is zero. If \(a\le k<a+c\), it is \(b\). Every length-\(k\) gap window avoiding the first spike must fit entirely after position \(a\), a suffix of length \(c+e-1\). Such a window necessarily contains the second spike: the all-zero stretches on its two sides have lengths \(c-1\) and \(e-1\), both less than \(k\). Thus inequality (1) at these lengths can fail exactly when \(c+e-1\ge a\) and \(d<b\). Conversely, if \(c+e-1\ge a\), a length-\(a\) window after the first spike exists and has sum exactly \(d\). Finally, if \(k\ge a+c\), every length-\(k\) window includes both spikes, since no stretch avoiding either spike has that length, and both sides of (1) equal \(b+d\). We conclude
\[
c\le a,\quad e\le a,\quad(c+e\le a\ \text{or}\ d\ge b),
\tag{2}
\]
with necessity and sufficiency, including all equality boundaries.

**3. Exact enumeration.** Partition the allowable triples \((a,c,e)\) into region I, \(c+e\le a\), and region II, \(c,e\le a<c+e\). The corresponding generating functions, where the exponent is \(a+c+e\), are
\[
A(z)=\sum_{c,e\ge1}\sum_{a\ge c+e}z^{a+c+e}
=\frac{z^4}{(1-z)(1-z^2)^2},
\]
\[
T(z)=\sum_{a\ge1}z^a\left(\sum_{j=1}^az^j\right)^2
=\frac{z^3(1+z^2)}{(1-z)^3(1+z)(1+z+z^2)},
\qquad B(z)=T(z)-A(z).
\]
In region I, both zero-run lengths \(b,d\) are arbitrary positive integers, contributing \(z^2/(1-z)^2\). In region II they satisfy \(d\ge b\ge1\), contributing
\[
\sum_{b\ge1}\sum_{d\ge b}z^{b+d}=\frac{z^2}{(1-z)(1-z^2)}.
\]
Hence
\[
P(z)=\frac{z^2}{(1-z)^2}A(z)
+\frac{z^2}{(1-z)(1-z^2)}(T(z)-A(z)).
\]
Common-denominator simplification yields the asserted rational expression, without any approximations.

**4. Limiting density.** The rational function has a pole of order five at \(z=1\), with leading principal-part coefficient
\[
\lim_{z\to1}(1-z)^5P(z)=\frac{7}{24}.
\]
Every other pole is on the unit circle and has order at most three, so coefficient extraction gives
\(p_n=\frac7{24}\binom{n+4}{4}+O(n^3)=\frac7{576}n^4+O(n^3)\). Since \(\binom{n-1}{4}=n^4/24+O(n^3)\), their ratio tends to \(7/24\).

As an independent analytic check of the leading proportion, five positive run lengths normalized by their sum converge in distribution to the normalization of five independent exponential random variables. For independent unit exponentials \((A,B,C,D,E)\), the classification event is the disjoint union \(A\ge C+E\) and \(A\ge C,E\), \(A<C+E\), \(D\ge B\). The first has probability \(\mathbb E[e^{-C-E}]=1/4\); \(A\) is the largest of \((A,C,E)\) with probability \(1/3\), and the second event therefore has probability \((1/3-1/4)/2=1/24\), giving \(7/24\).

## Verification

The included standard-library-only program `src/verify.py` enumerates **all** \(\binom{n-1}{4}\) five-run words separately at each length \(5\le n\le27\) (\(80{,}730\) words in total). It checks prefix normality directly by examining all factor lengths and positions, independently evaluates the run-length criterion, and generates coefficients from the denominator polynomial recurrence for the claimed rational function. All three counts agree for every tested length. Run `python src/verify.py` to reproduce the output `VERIFY_OK five_run_words_checked 80730 coefficient_range n=5..27`. These finite checks corroborate but do not prove the infinite formula; the proof above does.

## Relationship to prior work

Burcsi, Fici, Lipták, Ruskey and Sawada (2016 preprint, published 2017) established a general necessary-and-sufficient gap-inequality characterization (their Lemma 8) and exact generating functions for *fixed numbers of ones*, and thus their result already covers the **membership** portion of equation (2) in its general form. We do not present that general test as new. The enumerative distinction here is the fixed **five-run** stratum with all run lengths free, an explicit rational generating function, and the conditional limiting density \(7/24\). Their fixed-one-count formulas and general gap test do not state this run-refined count or its density.

Balister and Gerke (2019) obtained the exponential-order global asymptotic count of all prefix-normal binary words, rather than this polynomial five-run stratum. Burcsi et al. (2020) studied Gray-code generation and used run-based necessary rejection tests (Section 6); these do not give an exact five-run census. Fleischmann et al. (2019 preprint, revised 2020) treated prefix-normal palindromes and collapsing classes rather than this enumerative question. No identical five-run rational function or density was identified in the inspected sources or targeted literature/database searches. This absence is not a proof of novelty.

## Limitations

The finding concerns only words with exactly five runs starting and ending in \(1\). It does not determine the global prefix-normal generating function, general fixed-run families, or the number of distinct prefix-normal forms in this class. The elementary classification is a specialization of previously known general gap inequalities; only the explicit run-stratified count and its density are proposed as novel. The finite verifier is not a substitute for the all-length proof. Unindexed literature and worked examples of general polyhedral enumeration techniques remain possible sources of prior coverage; independent scholarly review has not been performed.

## References

1. P. Burcsi, G. Fici, Z. Lipták, F. Ruskey and J. Sawada, *On Prefix Normal Words and Prefix Normal Forms*, arXiv:1611.09017, first posted 2016-11-28; Theoretical Computer Science **659** (2017), 1–13. In particular Proposition 7, Lemma 8 and Section 4.
2. P. Balister and S. Gerke, *The asymptotic number of prefix normal words*, arXiv:1903.07957, first posted 2019-03-19; Theoretical Computer Science **784** (2019), 75–80.
3. P. Fleischmann, M. Kulczynski, D. Nowotka and D. B. Poulsen, *On Collapsing Prefix Normal Words*, arXiv:1905.11847, first posted 2019-05-28; LATA 2020, 412–424.
4. P. Burcsi, G. Fici, Z. Lipták, R. Raman and J. Sawada, *Generating a Gray Code for Prefix Normal Words in Amortized Polylogarithmic Time per Word*, arXiv:2003.03222, first posted 2020-03-05; Theoretical Computer Science **842** (2020), 86–99.
