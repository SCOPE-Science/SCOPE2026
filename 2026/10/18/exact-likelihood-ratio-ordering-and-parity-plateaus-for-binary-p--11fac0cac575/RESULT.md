# Exact likelihood-ratio ordering and parity plateaus for binary Pólya run counts

## Finding

For each integer \(n\ge2\), let \(X_1,\ldots,X_n\) be the first \(n\) colors sampled from a two-color Pólya urn with initial color masses \(a,a>0\) and one added unit of the sampled color after every draw. Put \(T_{n,a}=\sum_{i=1}^{n-1}\mathbf1\{X_i\ne X_{i+1}\}\), the number of color switches, and \(p_a(t)=\Pr(T_{n,a}=t)\).

**Theorem.** For all real \(0<a<b\), the likelihood ratio \(p_b(t)/p_a(t)\) is nondecreasing over every integer \(0\le t\le n-1\). It increases *strictly* between \(t=2m\) and \(t=2m+1\) whenever both belong to this range, and is *equal* between \(t=2m-1\) and \(t=2m\), for each \(1\le m\le\lfloor(n-1)/2\rfloor\). In fact, every binary exchangeable sequence of length \(n\) with positive probabilities at all run counts has the universal identity

\[
\Pr(T=2m)=\frac{n-2m}{2m}\Pr(T=2m-1),\qquad 1\le m\le\left\lfloor\frac{n-1}{2}\right\rfloor.
\]

In particular, for each fixed integer \(1\le h\le n-1\), the upper-tail probability \(\Pr(T_{n,a}\ge h)\) is strictly increasing in \(a\). The law approaches a point mass at zero as \(a\downarrow0\), and approaches \(\operatorname{Binomial}(n-1,1/2)\) as \(a\to\infty\).

## Assumptions and scope

The urn has exactly two colors, a *symmetric* positive initial mass \(a\) for each color, and reinforcement \(+1\) after every draw. The parameter \(a\) is real, not necessarily integral. A \(k\)-run is a maximal constant-color block; the number of constant-color runs equals \(T_{n,a}+1\). This theorem concerns the *total number of color changes*, not the number of success blocks of some prescribed length. Likelihood-ratio order means that the two probability mass functions are everywhere positive and their pointwise ratio is nondecreasing in the switch-count argument. All statements are finite-sample, for each fixed \(n\ge2\), without asymptotic approximations.

Pólya exchangeability gives the beta-mixture representation: sample \(P\sim\operatorname{Beta}(a,a)\), then conditional on \(P\), sample the \(X_i\) independently with success probability \(P\). Thus, if \(K=\sum_i X_i\),

\[
\Pr(K=k)=\binom nk\frac{(a)_k(a)_{n-k}}{(2a)_n},\qquad
(x)_r=\prod_{i=0}^{r-1}(x+i),\quad (x)_0=1.
\]

## Proof

**1. Conditional composition kernel.** Fix \(K=k\). Exchangeability makes the binary word uniformly distributed among the \(\binom nk\) words containing exactly \(k\) ones. Put \(j=\min(k,n-k)\) and \(J=\min(K,n-K)\). For \(j\ge1\) and \(1\le m\le j\), let

\[
A_m(j)=\binom{j-1}{m-1}\binom{n-j-1}{m-1},
\]

with binomial coefficients interpreted as zero when their lower arguments fall outside the usual range. There are precisely \(2A_m(j)\) binary words with \(j\) occurrences of the minority color and \(T=2m-1\) switches: choose the initial color and compose the counts of the two colors into \(m\) positive blocks each. There are precisely \((n-2m)A_m(j)/m\) words with \(T=2m\) switches, since the initial and terminal color coincide and one color has \(m+1\) positive blocks while the other has \(m\). Hence, with \(H(j,t)=\Pr(T=t\mid J=j)\),

\[
H(j,2m-1)=\frac{2A_m(j)}{\binom nj},\qquad
H(j,2m)=\frac{n-2m}{m}\frac{A_m(j)}{\binom nj}.
\]

When \(j=0\), \(H(0,0)=1\) and \(H(0,t)=0\) for \(t\ge1\). The paired-mass identity follows by summing the conditional relation \(H(j,2m)=(n-2m)H(j,2m-1)/(2m)\) over arbitrary exchangeable composition weights.

**2. Total positivity of the kernel.** The nonzero kernel entries come in adjacent blocks \((2m-1,2m)\), with a constant ratio \(H(j,2m)/H(j,2m-1)=(n-2m)/(2m)\) independent of \(j\). Between consecutive blocks,

\[
\frac{A_{m+1}(j)}{A_m(j)}
=\frac{(j-m)(n-j-m)}{m^2}
=\frac{j(n-j)-m(n-m)}{m^2},
\]

where a zero entry is understood at \(j=m\). Since \(j(n-j)\) increases strictly for integer \(0\le j\le\lfloor n/2\rfloor\), these ratios increase in \(j\). The supports \(\{t:H(j,t)>0\}\) expand from low to high switch counts as \(j\) increases. Consequently every \(2\times2\) minor \(H(j,t)H(j',t')-H(j,t')H(j',t)\) is nonnegative whenever \(j<j'\) and \(t<t'\). The singleton row \(j=0\) respects the same inequality. Thus \(H\) is totally positive of order two (TP2).

**3. Concentration order of compositions.** Symmetry yields, for \(0\le j\le\lfloor n/2\rfloor\),

\[
w_a(j):=\Pr(J=j)
=(2-\mathbf1\{2j=n\})\binom nj\frac{(a)_j(a)_{n-j}}{(2a)_n}.
\]

For \(0<a<b\) and \(0\le j<\lfloor n/2\rfloor\), canceling the \(j\)-dependent multiplicities gives

\[
\frac{w_b(j+1)/w_a(j+1)}{w_b(j)/w_a(j)}
=\frac{(b+j)(a+n-j-1)}{(a+j)(b+n-j-1)}
>1.
\]

Indeed, the numerator minus denominator is exactly \((b-a)(n-2j-1)>0\). The composition distribution is therefore *strictly* monotone in likelihood-ratio order as \(a\) increases.

**4. Composition of orders and strictness.** Since \(p_a(t)=\sum_jw_a(j)H(j,t)\), the two-by-two Cauchy–Binet expansion gives, for all \(t<t'\),

\[
p_a(t)p_b(t')-p_a(t')p_b(t)
=\sum_{j<j'}\bigl[w_a(j)w_b(j')-w_a(j')w_b(j)\bigr]
\bigl[H(j,t)H(j',t')-H(j,t')H(j',t)\bigr]\ge0.
\]

Thus \(p_b(t)/p_a(t)\) is nondecreasing. For \(t=2m\) and \(t'=2m+1\), choose \(j=m\), \(j'=m+1\). The first bracket is strictly positive; the second is strictly positive because \(H(m,2m)>0\), \(H(m,2m+1)=0\), and \(H(m+1,2m+1)>0\). This includes \(m=0\) using \(j=0,1\). Hence each even-to-odd step is strict. Every odd-to-even step is an equality by step 1. Full support of \(p_a\) and these strict jumps imply strict upper-tail ordering for every nontrivial threshold \(h\): a nonconstant increasing likelihood ratio has positive covariance with the indicator of an upper tail, and the change-of-measure expectation of the ratio equals one.

**5. Endpoints.** For fixed \(n\), as \(a\downarrow0\), the beta mixing variable converges weakly to an equiprobable mixture of the two endpoints zero and one, so the binary word is constant with probability tending to one. As \(a\to\infty\), \(P\to1/2\) in probability, so the word tends to fair independent bits. Their consecutive XOR indicators are independent fair bits, whence \(T\) tends to \(\operatorname{Binomial}(n-1,1/2)\).

## Verification

Run `python verify.py` using only the Python standard library. The program exhaustively enumerates binary words for lengths \(2\) through \(9\), validates the exact conditional composition counts and all two-by-two kernel minors, and computes integrated Pólya word probabilities exactly with `fractions.Fraction` at concentration values \(1/3,1/2,1,2,5\). It checks the universal adjacent-mass identity, all strict/non-strict ratio comparisons, and all nontrivial strict tail inequalities. At preparation, it passed \(1{,}882\) exact finite assertions. These finite checks are **not** a proof for all lengths or real concentrations; that follows from the analytic TP2 and likelihood-ratio argument above.

## Relationship to prior work

Eryilmaz (2018) develops stochastic comparisons for *success runs of a fixed prescribed length* under exchangeability and beta-binomial models; its public abstract and introductory material were inspected. The present statistic is instead *all color changes*, and the result compares **two reinforcement concentrations** in the strong likelihood-ratio order, including its precise staircase of equality cases. Eryilmaz (2008) derives marginal total-run laws for exchangeable multistate sequences including urn models, but a marginal law alone does not state the monotone-likelihood-ratio relation across parameters. Eryilmaz and Demir (2007) establish conditional uniformity and exact success-run laws, ingredients acknowledged and used here. Meleşteu, Pascu and Pascu (2022) prove a convex order for total Pólya success counts, which does not imply a likelihood-ratio order for adjacent-change statistics. General TP2 composition is a classical tool; the specific folded-composition kernel, its plateau structure, and the parameter comparison are the asserted findings, not TP2 theory itself.

## Limitations

The assertion requires symmetric initial color masses; no order is asserted for arbitrary asymmetric Pólya urns, multi-color urns, or nonunit reinforcement without reparameterization. The claim is a finite-sample stochastic-order result, not an asymptotic mixing statement. The complete texts of Eryilmaz (2008) and Eryilmaz (2018) could not be inspected; despite the distinctions in their accessible abstracts and subject matter, an equivalent historical parameter-ordering result could exist there or in other classical exchangeable-runs literature. Historical priority has not been independently certified.

## References

- S. Eryilmaz (2018), “Stochastic Ordering Among Success Runs Statistics in a Sequence of Exchangeable Binary Trials,” *Methodology and Computing in Applied Probability* 20, 563–573. DOI: 10.1007/s11009-017-9576-1. First verifiable online public date: 2017-06-28. Primary listed MSC (2010): 60E05.
- S. Eryilmaz (2008), “Distribution of runs in a sequence of exchangeable multi-state trials,” *Statistics & Probability Letters* 78, 1505–1513. DOI: 10.1016/j.spl.2008.01.002.
- S. Eryilmaz and S. Demir (2007), “Success runs in a sequence of exchangeable binary trials,” *Journal of Statistical Planning and Inference* 137, 2954–2963. DOI: 10.1016/j.jspi.2006.10.015.
- D. Meleşteu, M. N. Pascu and N. R. Pascu (2022), “Convex ordering of Pólya random variables and monotonicity of the error estimate of Bernstein–Stancu operators,” arXiv:2201.05870 (first posted 2022-01-15).
- S. Karlin (1968), *Total Positivity*, Vol. I. Classical total-positivity theory; no new general TP2 composition theorem is claimed.
