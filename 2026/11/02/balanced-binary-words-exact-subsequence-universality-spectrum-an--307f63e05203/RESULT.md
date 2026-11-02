# Balanced binary words: exact subsequence-universality spectrum and a Gaussian law

## Finding

For integers \(n,k\geq0\), let \(b_{n,k}\) be the number of distinct binary words containing exactly \(n\) zeros and \(n\) ones whose scattered-subsequence universality index equals \(k\). The ambient subsequence alphabet is always \(\{0,1\}\). Then the **complete joint distribution** is the formal algebraic series

\[
\boxed{B(t,u)=\sum_{n,k\geq0}b_{n,k}t^nu^k
=\sqrt{\frac{1-t}{1-(1+4u)t+4u^2t^2}}.}
\]

The square root is the unique branch with constant term one. In particular, \(b_{0,0}=1\); if \(n\geq1\), the index belongs to \(\{1,\dots,n\}\), and
\[
\sum_{k=0}^n b_{n,k}=\binom{2n}{n},\qquad b_{n,n}=2^n.
\]
For example, the index distributions for semilengths \(n=1,2,3,4\) (with the zero coefficient omitted) are, respectively, \((2)\), \((2,4)\), \((2,10,8)\), and \((2,16,36,16)\). For \(n\geq2\), the next-to-maximal coefficient also has the explicit boundary formula
\[
b_{n,n-1}=2^{n-2}\left(\binom{n+1}{2}-1\right).
\]

Let \(W_n\) be uniform among all \(\binom{2n}{n}\) strictly balanced binary words of length \(2n\), and put \(X_n=\iota(W_n)\). Then
\[
\mathbb E X_n=\frac23n+\frac29+O(n^{-1}),\qquad
\operatorname{Var}(X_n)=\frac4{27}n-\frac2{81}+O(n^{-1}),
\]
and
\[
\boxed{\frac{X_n-2n/3}{\sqrt{4n/27}}\ \xrightarrow{\mathrm d}\ \mathcal N(0,1).}
\]

## Assumptions and scope

A binary word \(w\) is *strictly balanced* when its numbers of zeros and ones agree. A word \(v\) is a *scattered subsequence* of \(w\) if \(v\) results from deleting zero or more symbols without changing the order of the retained symbols. The universality index \(\iota(w)\) is the largest \(k\geq0\) such that **each** binary word of length \(k\) occurs as a scattered subsequence of \(w\). Distinct indexed words are counted separately: there is no quotient by reversal, complementation, rotation or Dyck-path equivalence. The empty word has index zero. All generating-function identities hold as formal series; asymptotic statements are for integer \(n\to\infty\).

## Proof

**1. Greedy arches characterize universality.** Repeatedly remove the shortest initial segment containing both binary symbols, terminating with a possibly empty monochromatic remainder. Every completed segment is uniquely one of \(0^r1\) or \(1^r0\), with \(r\geq1\); call it an *arch*. The factorization is unique. If there are \(k\) arches, any prescribed binary word of length \(k\) is a subsequence by selecting one suitable symbol from each arch. Conversely, the terminal symbol from each consecutive arch must be encountered at or after that arch's end when its sequence is matched greedily. Appending the symbol absent from the final monochromatic remainder therefore gives a length-\(k+1\) binary word that cannot be a subsequence. Hence \(\iota(w)=k\), exactly the number of completed arches. This is the standard arch-factorization characterization, included to fix the precise convention.

**2. Mark signed composition before extracting balance.** Let \(z\) mark word length, \(u\) mark completed arches, and \(x\) mark the excess of ones over zeros, so a zero contributes \(zx^{-1}\) and a one contributes \(zx\). One binary arch has Laurent generating function
\[
A(z,x)=\sum_{r\geq1}z^{r+1}(x^{r-1}+x^{1-r})
=z^2\left(\frac1{1-zx}+\frac1{1-z/x}\right).
\]
The monochromatic remainder contributes
\[
R(z,x)=1+\sum_{r\geq1}z^r(x^r+x^{-r}).
\]
Writing \(S=x+x^{-1}\), straightforward common-denominator identities give
\[
A(z,x)=\frac{z^2(2-zS)}{1-zS+z^2},\qquad
R(z,x)=\frac{1-z^2}{1-zS+z^2}.
\]
As every word has exactly one ordered list of arches followed by one remainder, its length/composition/index generating function is
\[
F(z,x,u)=\frac{R(z,x)}{1-uA(z,x)}
=\frac{1-z^2}{1+(1-2u)z^2-z(1-uz^2)(x+x^{-1})}.
\]
Every term at a fixed length has a finite Laurent expansion. Strict balance is precisely exponent zero in \(x\), so the desired series is \(\operatorname{CT}_{x}F(z,x,u)\) with \(t=z^2\).

**3. Exact constant-term extraction.** For formal \(a\) with constant term one and formal \(b\) of positive \(z\)-adic order,
\[
\operatorname{CT}_{x}\frac1{a-b(x+x^{-1})}
=\frac1a\sum_{j\geq0}\binom{2j}{j}\left(\frac b a\right)^{2j}
=\frac1{\sqrt{a^2-4b^2}}.
\]
Indeed, the constant coefficient of \((x+x^{-1})^{2j}\) is \(\binom{2j}{j}\), while every odd power has constant coefficient zero. Substituting \(a=1+(1-2u)z^2\), \(b=z(1-uz^2)\), and \(t=z^2\), gives
\[
B(t,u)=\frac{1-t}{\sqrt{(1+(1-2u)t)^2-4t(1-ut)^2}}.
\]
The exact polynomial factorization
\[
(1+(1-2u)t)^2-4t(1-ut)^2
=(1-t)\bigl(1-(1+4u)t+4u^2t^2\bigr)
\]
proves the displayed radical formula. Setting \(u=1\) reduces it to \((1-4t)^{-1/2}\), proving the central-binomial total. The only words attaining the maximal possible index \(n\) are concatenations of \(n\) length-two arches \(01\) or \(10\); hence there are \(2^n\) of them. To have exactly \(n-1\) arches in total length \(2n\), the two excess positions beyond the minimal arch lengths are necessarily distributed in one of two ways: one length-three arch and a length-one opposite monochromatic remainder, or two length-three arches of opposite signed excess and no remainder. The first contributes \((n-1)2^{n-1}\), and the second \(\binom{n-1}{2}2^{n-2}\); their sum simplifies to the displayed next-to-maximal coefficient. (A single length-four arch has nonzero imbalance and cannot yield a balanced word with empty remainder.)

**4. Singularity analysis and the limit law.** Near \(u=1\), the roots of \(Q(t,u)=1-(1+4u)t+4u^2t^2\) are
\[
\rho(u)=\frac2{1+4u+\sqrt{1+8u}},\qquad
\lambda(u)=\frac2{1+4u-\sqrt{1+8u}}.
\]
They are analytic locally and satisfy \(\rho(1)=1/4\), \(\lambda(1)=1\). The simple root \(\rho(u)\) is the unique dominant singularity in a sufficiently small complex neighborhood of \(u=1\). Locally,
\[
B(t,u)=\frac{g(t,u)}{\sqrt{1-t/\rho(u)}},\qquad
g(t,u)=\sqrt{\frac{1-t}{1-t/\lambda(u)}}.
\]
The analytic factor is nonzero at the dominant root. Uniform square-root transfer gives
\[
[t^n]B(t,u)=\frac{h(u)}{\sqrt{\pi n}}\rho(u)^{-n}(1+O(n^{-1})),
\qquad h(u)=\sqrt{\frac{1-\rho(u)}{1-\rho(u)/\lambda(u)}}.
\]
The error is uniform for \(u\) in a sufficiently small complex disk about one. As \(h(1)=1\), the probability generating function of \(X_n\) is
\[
\mathbb E[u^{X_n}]=h(u)\left(\frac{\rho(1)}{\rho(u)}\right)^n(1+O(n^{-1})).
\]
Set \(u=e^s\). Direct differentiation of the analytic logarithms at \(s=0\) gives
\[
\left.\frac{d}{ds}\log\frac{\rho(1)}{\rho(e^s)}\right|_{s=0}=\frac23,\qquad
\left.\frac{d^2}{ds^2}\log\frac{\rho(1)}{\rho(e^s)}\right|_{s=0}=\frac4{27},
\]
\[
\left.\frac{d}{ds}\log h(e^s)\right|_{s=0}=\frac29,\qquad
\left.\frac{d^2}{ds^2}\log h(e^s)\right|_{s=0}=-\frac2{81}.
\]
Analyticity of the error permits differentiation, yielding the mean and variance expansions. For fixed real \(v\), set \(s=iv/\sqrt{4n/27}\) in the centered moment generating function; the Taylor expansion of the log tends to \(-v^2/2\), so the characteristic functions converge to that of \(\mathcal N(0,1)\). Lévy's continuity theorem gives the claimed central limit law. No numerical experiment is used to establish this infinite result.

## Verification

Run `python3 verify.py` using Python 3 standard library only. It recomputes the series coefficients through \(n=8\) by the independent polynomial identity
\[
B(t,u)^2\bigl(1-(1+4u)t+4u^2t^2\bigr)=1-t,
\]
then independently enumerates all \(\sum_{n=0}^8\binom{2n}{n}=17{,}577\) strictly balanced binary words up to length 16. It compares the full index histograms at every size with the coefficients and with the central-binomial totals. It independently compares the greedy-arch index with the defining all-subsequence predicate for every binary word of length at most 10. Output must end in `VERIFY_OK total_balanced_words=17577; all_words_upto_length=10`. These checks corroborate the finite algebra but are not exhaustive over all lengths and do not replace the all-length proof.

## Relationship to prior work

Day, Fleischmann, Manea and Nowotka analyze the sizes and reconstructibility of fixed-length scattered-factor spectra of strictly balanced and \(c\)-balanced binary words [1]. Their key result concerning strictly balanced words of length \(2n\) characterizes full \(n\)-universality, corresponding to the already-known maximal-index boundary \(b_{n,n}=2^n\); the new statement is the *entire* joint index spectrum for all \(n,k\) and its fluctuations. Barker and collaborators [2], Schnoebelen and Veron [3], and Adamson [4] supply the arch universality framework and algorithmic counting of unconstrained words, but their inspected statements do not present this composition-conditioned radical distribution. Adamson and collaborators [5] give general regular-language counting procedures, not a fixed-composition closed form. An earlier explicit rational generating function for **all** binary words, \((1+z)/(1-z-2uz^2)\) [6], agrees after ignoring signed composition in the arch method; that two-variable law alone does not encode how many zeros and ones occur in each word, and therefore does not determine the constant-term specialization proved here. Previous Dyck-word universality distributions restrict to words whose prefix excess never falls below zero, rather than the full class of arbitrary balanced bridges; neither constraint is a relabeling of the other. The relationship can be made explicit: writing \(D(t,u)=C(T)\) for the earlier Dyck distribution and \(T=tu(1-tu)/(1-t)\), the radical identity \(1-2TC(T)=\sqrt{1-4T}\) yields \(B(t,u)=1/(1-2T D(t,u))\). This algebraic relationship is acknowledged as overlap, but its earlier formula does not assert that this transform counts **all** equal-composition words; the signed-arch argument above proves precisely that missing interpretation.

## Limitations

The result is specific to the fixed binary alphabet and *equal* total symbol counts. It concerns ordinary scattered subsequences, not factors, distinct-subsequence counts, or circular universality. The finite verifier reaches only \(n=8\) for balanced-word histograms. The proof does not establish an analogous radical law for larger alphabets or for a prescribed nonzero imbalance. Bibliographic searches and relevant full-text inspections found no equivalent formula or dominating statement, but unindexed or differently phrased work may exist. 

## References

1. Joel D. Day, Pamela Fleischmann, Florin Manea, Dirk Nowotka, *k-Spectra of weakly-c-Balanced Words*, first public 2019-04-19, arXiv:1904.09125. https://arxiv.org/abs/1904.09125
2. Laura Barker, Pamela Fleischmann, Katharina Harwardt, Florin Manea, Dirk Nowotka, *Scattered Factor-Universality of Words*, first public 2020-03-10, arXiv:2003.04629. https://arxiv.org/abs/2003.04629
3. Philippe Schnoebelen, Julien Veron, *On arch factorization and subword universality for words and compressed words*, first public 2023-04-24, arXiv:2304.11932. https://arxiv.org/abs/2304.11932
4. Duncan Adamson, *Ranking and Unranking k-subsequence universal words*, first public 2023-04-10, arXiv:2304.04583. https://arxiv.org/abs/2304.04583
5. Duncan Adamson, Pamela Fleischmann, Annika Huch, Tore Koß, Florin Manea, Dirk Nowotka, *k-Universality of Regular Languages*, first public 2023-11-17, arXiv:2311.10658. https://arxiv.org/abs/2311.10658
6. *Closed-form law for binary subsequence universality*, published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-closed-form-law-for-binary-subsequence-universality--e77c4e8d9f37
