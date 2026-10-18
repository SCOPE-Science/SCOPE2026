# Exact asymptotic spectrum of four-point ordinal frequencies

## Finding

Let \((U_i)_{i\ge1}\) be independent observations from any common atomless distribution. Let \(N_{\pi,n}\) count sliding windows of four successive observations whose strict rank pattern is \(\pi\in S_4\). Write \(N_n=(N_{\pi,n})_{\pi\in S_4}\), indexed by the 24 rank patterns in lexicographic order. The limiting covariance
\[
A=\lim_{n\to\infty}\frac1n\operatorname{Cov}(N_n)
\]
exists. Set \(D=20160A\) and let \(x\) be an indeterminate. **The exact full characteristic polynomial** is
\[
\begin{aligned}
\det(xI_{24}-D)={}&x^6(x-1232)(x-840)^2(x-800)(x-784)(x-504)\\
&\cdot(x^2-2408x+1185408)\\
&\cdot(x^2-1792x+705600)\\
&\cdot(x^2-1256x+387072)\\
&\cdot(x^3-3696x^2+3471552x-616412160)\\
&\cdot(x^3-2912x^2+2549568x-663828480).
\end{aligned}
\]
The nullity is six and there are eighteen nonzero real eigenvalues, counted with multiplicity. In particular, these formulas determine all exact nonzero weights in the null limit of the unadjusted Pearson statistic on the 24 ordinal frequencies.

Write \(K=n-3\) and \(\widehat p_{\pi,n}=N_{\pi,n}/K\). The usual Pearson statistic is
\[
T_n=24K\sum_{\pi\in S_4}\bigl(\widehat p_{\pi,n}-1/24\bigr)^2.
\]
If \(r_1,\ldots,r_{18}\) are the positive roots, with multiplicity, of the factor above after deleting \(x^6\), then
\[
T_n\ \xrightarrow{d}\ \sum_{j=1}^{18}\frac{r_j}{840}\,Z_j^2,
\qquad Z_j\ \text{independent }N(0,1).
\]
The existence of this weighted chi-square form and general rank restrictions were established previously; the new contribution is the exact **length-four spectral factorization and hence the explicit eighteen weights**.

## Assumptions and scope

Observations are independent, identically distributed, and atomless; consequently ties occur with probability zero. The sample length \(n\) is at least four. For any four distinct real numbers, \(\operatorname{std}\) denotes the permutation recording their relative ranks, from smallest rank one to largest rank four. The theorem is specifically for all 24 *consecutive* four-point patterns, not arbitrary nonconsecutive four-index subsequences, and for the usual overlapping-window frequencies. No statement is made about dependent observations or tie-breaking methods. The eigenvalue scale is specified exactly by \(D=20160A\).

## Proof

For \(\ell\in\{0,1,2,3\}\), let \(C_\ell\) be the 24-by-24 matrix whose \((\pi,\tau)\) entry is
\[
(C_\ell)_{\pi,\tau}=\frac{b_\ell(\pi,\tau)}{(4+\ell)!}-\frac1{576},
\]
where \(b_\ell(\pi,\tau)\) counts permutations \(q\) of \(\{1,\ldots,4+\ell\}\) whose first four positions have pattern \(\pi\) and whose positions \(\ell+1,\ldots,\ell+4\) have pattern \(\tau\). For zero lag, \(C_0=I_{24}/24-\mathbf1\mathbf1^\top/576\). For positive lag the definition gives the exact joint distribution of overlapping rank windows: among \((4+\ell)!\) equally probable orders, precisely \(b_\ell(\pi,\tau)\) meet both restrictions.

Let \(K=n-3\). Indicators for windows at a separation of at least four are independent. Summing all indicator covariances gives the finite-size identity
\[
\operatorname{Cov}(N_n)=K C_0+\sum_{\ell=1}^{3}(K-\ell)_+\,(C_\ell+C_\ell^\top),
\]
where \((z)_+=\max\{0,z\}\). Dividing by \(n\) and taking the limit yields
\[
A=C_0+\sum_{\ell=1}^{3}(C_\ell+C_\ell^\top).
\]
Thus every entry is a finite rational number, determined by permutations of at most seven elements. In particular \(D=20160A\) has integer entries. The supplied verifier independently enumerates the rank restrictions, constructs every \(C_\ell\), computes the characteristic polynomial of the integer matrix with exact arithmetic, and verifies equality with the displayed factorization. This is a finite exhaustive computation: at lag \(\ell\), *all* \((4+\ell)!\) relative orders are enumerated. No numerical eigenvalue approximation is used to certify the factors.

For each three-point pattern \(\alpha\), define the 24-coordinate flow-difference vector by
\[
(v_\alpha)_\pi=\mathbf1\{\operatorname{std}(\pi_1,\pi_2,\pi_3)=\alpha\}
-\mathbf1\{\operatorname{std}(\pi_2,\pi_3,\pi_4)=\alpha\}.
\]
The sum over windows of each corresponding local difference telescopes to boundary indicators, so its variance is bounded independently of \(n\). Therefore \(Av_\alpha=0\); also \(A\mathbf1=0\) because exactly one four-pattern appears per window. The six flow vectors sum to zero, and direct exact row reduction verifies that \(\mathbf1\) together with the flow vectors spans a six-dimensional space. The characteristic polynomial has exactly six zero roots; consequently these account for the entire kernel. Covariance positive semidefiniteness makes all remaining roots positive.

Finally, the centered 24-dimensional window-indicator sequence is stationary, bounded, and three-dependent. The standard multivariate central limit theorem for finite-dependent stationary sequences gives \(K^{-1/2}(N_n-K\mathbf1/24)\Rightarrow N_{24}(0,A)\). Diagonalization of \(A\) and the continuous mapping theorem give the displayed weighted chi-square limit. Since \(24/20160=1/840\), its eighteen weights are precisely \(r_j/840\).

## Verification

Run `python verify_spectrum.py` using Python 3 and SymPy. The program enumerates every permutation of sizes four, five, six, and seven to rebuild the matrix from its probability definition, verifies the scale and integrality, checks six independent kernel vectors and the exact 24th-degree characteristic polynomial by integer arithmetic, and checks the finite-size covariance increment identity. It completes without reliance on a provided matrix dump or numerical eigensolver. The finite computation is exhaustive for the matrix defining the theorem; it is not an enumeration of infinitely many sample sizes.

## Relationship to prior work

Bandt and Shiha (first published 19 February 2007) developed order patterns in time series. Elsinger (2010), especially its ordinal-frequency covariance derivation and Section 3, already gives the general limiting covariance construction, a multivariate central limit theorem, rank upper bounds, and weighted-chi-square limits; it also computes length-three eigenvalues. None of those general statements is claimed as new. Bandt (2022) discusses the covariance geometry and length-three pattern contrasts and explicitly raises length-four contrast structure as a question. The present result evaluates and factors the **entire length-four white-noise covariance spectrum** in exact integers, thereby instantiating the general null law with all eighteen weights. A separate published result about the polytope of possible length-four pattern frequencies concerns a different geometric object and does not imply these white-noise covariance eigenvalues.

## Limitations

The factorization is special to consecutive length-four patterns and continuous i.i.d. sampling. Eigenvectors for each nonzero eigenspace are not classified, and the complete canonical system of length-four pattern contrasts is not constructed. The result yields an asymptotic test calibration, not a finite-sample calibration or finite-sample error bound. Prior works providing general transfer matrices could in principle imply the spectrum after nontrivial further calculation; the cited primary full text does not exhibit the exact length-four factorization. A related later source could not be fully inspected, leaving a residual historical-priority risk. Independent verification has not been conducted.

## References

1. C. Bandt and F. Shiha, *Order Patterns in Time Series*, Journal of Time Series Analysis 28 (2007), 646–665. DOI: 10.1111/j.1467-9892.2007.00528.x. First online 2007-02-19.
2. H. Elsinger, *Independence Tests based on Symbolic Dynamics*, Oesterreichische Nationalbank Working Paper 165 (2010), especially pp. 10–15 and Appendix A. https://www.oenb.at/dam/jcr:5390f35e-bf75-43c4-9d1a-248a26728d2a/wp165_screen_tcm16-208851.pdf
3. C. Bandt, *Statistics and modelling of order patterns in univariate time series* (2022), arXiv:2212.14386. https://arxiv.org/abs/2212.14386
4. C. H. Weiß, *Non-parametric tests for serial dependence in time series based on asymptotic implementations of ordinal-pattern statistics* (2022), relevant later testing literature; full text not verified.
