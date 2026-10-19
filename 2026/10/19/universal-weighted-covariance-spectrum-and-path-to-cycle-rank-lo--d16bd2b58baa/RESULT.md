# Universal weighted covariance spectrum and path-to-cycle rank loss for categorical bigram counts

## Finding

For every integer \(q\ge2\), any full-support distribution \(p=(p_a)_{a=1}^q\), and any sample size \(n\ge2\), the covariance of the full \(q\times q\) table of **overlapping directed adjacent-pair counts** has a universal spectrum after whitening by the known cell probabilities. The spectrum is independent of the values of \(p\), even when the alphabet distribution is nonuniform.

Write \(m=n-1\), \(N_{ab}=\sum_{t=1}^{m}{\bf1}\{X_t=a,X_{t+1}=b\}\), and \(D=\operatorname{diag}_{a,b}(p_a p_b)\). The symmetric normalized covariance is
\[
K_m=\frac{1}{m}D^{-1/2}\operatorname{Cov}(N)D^{-1/2}.
\]
Its complete spectrum, **with algebraic multiplicities**, is

| Eigenvalue | Multiplicity | Letter-pair score space |
|---|---:|---|
| \(0\) | \(1\) | constants |
| \(1/m\) | \(q-1\) | \(v(a)-v(b)\) with \(\mathbb E_p v=0\) |
| \(1\) | \((q-1)^2\) | row- and column-centered interactions |
| \(2-1/m\) | \(q-1\) | \(u(a)+u(b)\) with \(\mathbb E_p u=0\) |

Eigenspaces in the table describe score vectors \((\sqrt{p_ap_b}\,f(a,b))_{a,b}\). Coincident eigenvalues add multiplicities; in particular all \(q^2-1\) nonzero eigenvalues equal \(1\) when \(m=1\). At every \(m\ge1\), \(\operatorname{rank}K_m=q^2-1\).

For **cyclic bigrams**, \(n\ge3\), define \(N^\circ_{ab}=\sum_{t=1}^n{\bf1}\{X_t=a,X_{t+1}=b\}\) with \(X_{n+1}=X_1\). Replacing \(m\) by \(n\) in the normalization gives the complete cyclic spectrum
\[
0\ (q\text{ times}),\qquad 1\ ((q-1)^2\text{ times}),\qquad 2\ (q-1\text{ times}).
\]
Hence \(\operatorname{rank}K_n^\circ=q^2-q\), exactly \(q-1\) smaller than the open-table rank. Cyclic gradient scores telescope, and the flow identity holds deterministically:
\[
\sum_b(N_{ab}-N_{ba})={\bf1}\{X_1=a\}-{\bf1}\{X_n=a\},
\qquad \sum_b(N^\circ_{ab}-N^\circ_{ba})=0.
\]

For a mean-zero cost array \(f\), measured in the weighted norm \(\|f\|^2_{p\otimes p}=\sum_{a,b}p_ap_b f(a,b)^2\), the open-path cost obeys the **sharp** bounds, whenever \(m\ge2\),
\[
\|f\|^2_{p\otimes p}\ \le\ \operatorname{Var}\Big(\sum_{t=1}^m f(X_t,X_{t+1})\Big)\ \le\ (2m-1)\|f\|^2_{p\otimes p}.
\]
Equality at the lower bound holds exactly for nonzero centered gradients \(f(a,b)=v(a)-v(b)\); equality at the upper bound holds exactly for nonzero centered symmetric potentials \(f(a,b)=u(a)+u(b)\). For \(m=1\), every centered cost attains both identical bounds. The finite-sample condition number on the nonconstant score space is exactly \(2m-1\).

As a statistical corollary, suppose the symbol probabilities are **known**, not estimated. With
\[
P_m=\sum_{a,b}\frac{(N_{ab}-m p_a p_b)^2}{m p_a p_b},
\]
one has, for all \(m\ge1\), \(\mathbb E[P_m]=q^2-1\), but as \(m\to\infty\) at fixed \(q,p\),
\[
P_m\ \xrightarrow{d}\ \chi^2_{(q-1)^2}+2\chi^2_{q-1},
\]
where the two chi-squared variables are independent. Thus the usual independent-cell chi-square reference law is not the null law of the overlapping table, despite the exact match in expectations.

## Assumptions and scope

The alphabet is finite with \(q\ge2\); \(X_1,\dots,X_n\) are independent and identically distributed; every \(p_a>0\); and a bigram is an **ordered** adjacent pair, with self-transitions allowed. The open version requires \(n\ge2\); the cyclic version requires \(n\ge3\) to ensure that distinct adjacent-pair windows are distinct and have only the stated one-letter overlaps. No uniformity assumption on \(p\) is made. The Pearson corollary assumes the probabilities \(p\) are externally known and held fixed.

## Proof

Give pair-score arrays the inner product \(\langle f,g\rangle=\sum_{a,b}p_ap_b f(a,b)g(a,b)\). Center a score \(f\) so that \(\mathbb Ef(X,Y)=0\) for independent \(X,Y\sim p\). Define its row and column conditional means
\[
r(a)=\sum_b p_b f(a,b),\qquad c(b)=\sum_a p_a f(a,b),
\]
and set \(u=(r+c)/2\), \(v=(r-c)/2\), and \(h(a,b)=f(a,b)-r(a)-c(b)\). All \(r,c,u,v\) are centered. Both the \(p\)-weighted row means and the \(p\)-weighted column means of \(h\) vanish. This gives the unique orthogonal decomposition
\[
f(a,b)=u(a)+u(b)+v(a)-v(b)+h(a,b),\qquad
\|f\|^2=2\|u\|_p^2+2\|v\|_p^2+\|h\|^2.
\]
The symmetric-potential and gradient subspaces are orthogonal: their inner product equals \(\mathbb E[u(X)v(X)]-\mathbb E[u(Y)v(Y)]=0\).

On an open sequence, the corresponding sum is exactly
\[
\sum_{t=1}^m f(X_t,X_{t+1})=
\big[u(X_1)+2\sum_{t=2}^{m}u(X_t)+u(X_{m+1})\big]
+\big[v(X_1)-v(X_{m+1})\big]
+\sum_{t=1}^m h(X_t,X_{t+1}).
\]
The first bracket has variance \((4m-2)\|u\|_p^2\), the second \(2\|v\|_p^2\), and the last \(m\|h\|^2\). The cross-covariances vanish: the only potential overlap between the first two brackets cancels between their endpoints, while conditional row/column centering makes the interaction bracket orthogonal to each potential bracket. Different interaction windows are uncorrelated, including consecutive windows, by conditioning on the shared symbol. Therefore
\[
\boxed{\operatorname{Var}\Big(\sum_{t=1}^m f(X_t,X_{t+1})\Big)
=2(2m-1)\|u\|_p^2+2\|v\|_p^2+m\|h\|^2.}
\]
This quadratic-form identity diagonalizes \(D^{-1/2}\operatorname{Cov}(N)D^{-1/2}\): with \(f\) mapped to \((\sqrt{p_ap_b}f(a,b))_{a,b}\), its eigenvalues are respectively \(2m-1\), \(1\), and \(m\), plus a constant-score null direction. The three nonconstant dimensions are \(q-1\), \(q-1\), and \((q-1)^2\); after division by \(m\), the first table follows, including all equality classes and the exact condition number.

For a cycle, the gradient bracket sums identically to zero. Each observation occurs twice in the symmetric-potential sum; therefore its variance is \(4n\|u\|_p^2\). The \(n\) degenerate interaction windows have mutually zero covariance, even when two windows share a vertex around the wrap-around, since \(n\ge3\). The cyclic quadratic form is consequently
\[
\boxed{\operatorname{Var}\Big(\sum_{t=1}^n f(X_t,X_{t+1})\Big)
=4n\|u\|_p^2+n\|h\|^2.}
\]
This proves the cyclic spectrum and the exact additional \(q-1\) null directions.

For reproducibility, the **unwhitened** open covariance entry for ordered pairs \((a,b)\), \((c,d)\), with \(s_{ab}=p_ap_b\), is
\[
\begin{split}
\operatorname{Cov}(N_{ab},N_{cd})={}&m\big[s_{ab}{\bf1}\{(a,b)=(c,d)\}-s_{ab}s_{cd}\big]\\
&+(m-1)\big[p_ap_bp_d{\bf1}\{b=c\}+p_cp_dp_b{\bf1}\{d=a\}-2s_{ab}s_{cd}\big].
\end{split}
\]
For the cyclic case, replace the leading \(m\) by \(n\) and the lag-overlap factor \(m-1\) by \(n\). These entries agree with the quadratic-form proof.

Finally, the bounded vector of adjacent-pair centered indicators is one-dependent, so its joint central limit theorem applies. The limit covariance has eigenvalues \(0\) on constants and gradients, \(1\) on the interaction space, and \(2\) on symmetric potentials. Diagonalizing the limiting Gaussian vector gives the displayed independent weighted-chi-square law. Its finite-sample expected Pearson statistic is the trace of \(K_m\): \((q-1)/m+(q-1)^2+(q-1)(2-1/m)=q^2-1\).

## Verification

Run `python3 verify_bigram.py` with Python 3; no external packages are needed. The script independently enumerates all categorical sequences for 25 full-support rational-probability models with alphabet sizes two, three, and four and sample sizes two through six (cyclic cases start at three). For both open and cyclic tables, it compares every directly enumerated mean and covariance entry with the formulas, verifies the complete eigenvector families using exact rational arithmetic, checks the weighted spectral trace, and checks the constant null direction. The script reports success only when all assertions pass. These finite cases test the formulas; the all-size conclusion is the preceding analytic argument.

## Relationship to prior work

General enumeration of overlapping word occurrences in Markov sequences appears in Park and Spouge (2004), while Percus and Percus (2005) treat words on rings. Such general distributional machinery is relevant but the accessible descriptions do not display the present **distribution-free, exact finite-sample whitened spectral factorization**, its sharp equality cases, or the open-versus-cyclic nullity jump. Those two original papers could not be inspected in full; implicit earlier coverage remains a material priority risk.

Bilodeau and Lafaye de Micheaux (2009) develop tests of serial independence for categorical variables and an orthogonal decomposition of serial contingency statistics, while Elsinger (2020) studies contingency-table serial correlation. Their related asymptotic testing theory is prior art; no broad claim of discovering serial-independence tests or the general central limit framework is made here. Pritchard and Scott (2004) address eigenvalues of a **random empirical Markov transition matrix**, not the covariance spectrum of its directed transition-count vector. Even-Zohar, Lakrec, and Tessler (2020/2021) study counts of **not-necessarily-consecutive subsequences**, not counts of adjacent length-two windows, so their spectral theorem is not directly interchangeable with this one.

The mathematical claim assessed here is the exact universal spectrum for nonuniform independent letters at every finite sample size, together with the precise path-to-cycle drop in rank and sharp cost-variance extremizers. The Pearson limit is included as an implication and calibrated interpretation, not a stand-alone novelty assertion.

## Limitations

The finite-sample spectrum does not directly extend to dependent Markov letters, zero-probability symbols, fitted rather than known cell probabilities, or arbitrary longer words. The chi-square corollary takes \(q,p\) fixed as the sample length tends to infinity. The exact enumerations do not by themselves prove statements for arbitrary sizes. The earlier general word-enumeration papers were not available in full text, so historical priority remains subject to independent comparison with their complete results and any implicit spectral consequences. No independent review is asserted.

## References

- Y. Park and J. L. Spouge, *Searching for Multiple Words in a Markov Sequence*, **INFORMS Journal on Computing** 16 (2004), 341–347. DOI: 10.1287/ijoc.1040.0095. First available online 2004-11-01.
- J. K. Percus and O. E. Percus, *The statistics of words on rings*, **Communications on Pure and Applied Mathematics** 59 (2006), 145–160. DOI: 10.1002/cpa.20096. First available online 2005-06-20.
- M. Bilodeau and P. Lafaye de Micheaux, *A-dependence statistics for mutual and serial independence of categorical variables*, **Journal of Statistical Planning and Inference** 139 (2009), 2407–2419. DOI: 10.1016/j.jspi.2008.11.006. Author-hosted text: https://www.dms.umontreal.ca/~bilodeau/A-dep.pdf.
- H. Elsinger, *Serial Correlation in Contingency Tables*, Oesterreichische Nationalbank Working Paper 228 (2020).
- G. Pritchard and D. J. Scott, *The eigenvalues of the empirical transition matrix of a Markov chain*, **Journal of Applied Probability** 41(A) (2004), 347–360. DOI: 10.1239/jap/1082552210.
- C. Even-Zohar, T. Lakrec and R. J. Tessler, *Spectral Analysis of Word Statistics*, preprint arXiv:2012.00742 (2020), extended abstract FPSAC 2021.
