# Exact gap crossover and a sharp inverse-stability obstruction for two-interval Fourier intensities

## Finding
Fix real parameters \(\ell>0\), \(d>\ell\), and \(0<|\eta|<\ell\). Let \(E_\eta\subset\mathbb R\) consist of two closed intervals with centers \(-d/2\) and \(d/2\) and respective lengths \(\ell+\eta\) and \(\ell-\eta\). Put \(g=d-\ell>0\), \(a=|\eta|\), and
\[
P_\eta(\omega)=\left|\int_{E_\eta}e^{-2\pi i\omega x}\,dx\right|^2.
\]
Then, writing \(T_a(t)=(a-|t|)_+\), the difference of covariograms is exactly
\[
\mathbf 1_{E_\eta}*\mathbf 1_{-E_\eta}-\mathbf 1_{E_0}*\mathbf 1_{-E_0}
=T_a(\cdot-\ell)+T_a(\cdot+\ell)-T_a(\cdot-d)-T_a(\cdot+d).
\]
In particular the squared \(L^2(\mathbb R)\) difference of Fourier **intensities** has the universal exact crossover
\[
\boxed{\ \|P_\eta-P_0\|_2^2=a^3\Phi(g/a)\ },
\quad
\Phi(s)=\begin{cases}
4s^2-2s^3,&0<s\le1,\\
\frac83-\frac23(2-s)^3,&1\le s\le2,\\
\frac83,&s\ge2.
\end{cases}
\]
Consequently, at each fixed \(g>0\), for every sufficiently small \(0<a<\min\{\ell,g/2\}\),
\[
\boxed{\ \|P_\eta-P_0\|_2=\sqrt{8/3}\,a^{3/2}\ }.
\]
Let \(D(E,F)\) be the infimum of \(\|\mathbf1_E-\mathbf1_{\sigma F+t}\|_{L^1(\mathbb R)}\) over \(\sigma\in\{-1,1\}\) and real translations \(t\). For all sufficiently small \(a>0\),
\[
D(E_\eta,E_0)=2a=2(3/8)^{1/3}\|P_\eta-P_0\|_2^{2/3}.
\]
In particular, **no local inverse estimate with exponent exceeding \(2/3\)**, including Lipschitz inverse stability, can hold uniformly over the class of two-interval indicators containing the equal-length configuration, even when both component lengths and the gap remain uniformly bounded away from zero. This is an obstruction: no matching local \(2/3\)-Hölder *upper* bound on arbitrary interval pairs is asserted.

## Assumptions and scope
Use the unitary Plancherel Fourier normalization \(\widehat f(\omega)=\int_{\mathbb R}f(x)e^{-2\pi i\omega x}\,dx\). Both intervals have positive length, fixed distinct centers, and fixed gap \(g=d-\ell\). Endpoints are irrelevant up to null sets. The pair \(E_\eta,E_0\) always has the same total measure \(2\ell\); the sets are not identical modulo any translation or reflection when \(a>0\). The crossover formula covers arbitrary positive ratios \(g/a\) subject to \(a<\ell\). The inverse-stability assertion fixes positive \(\ell,g\) and lets \(a\downarrow0\).

## Proof
**1. Fourier identity and covariogram.** Put \(\xi=2\pi\omega\). Direct integration of the two intervals gives
\[
P_\eta(\omega)=\frac4{\xi^2}\{1-\cos(\ell\xi)\cos(\eta\xi)+[\cos(\eta\xi)-\cos(\ell\xi)]\cos(d\xi)\}
\]
for nonzero \(\xi\), with its continuous extension at zero. Subtraction yields
\[
P_\eta(\omega)-P_0(\omega)=\frac{4[1-\cos(a\xi)]}{\xi^2}[\cos(\ell\xi)-\cos(d\xi)].
\]
The elementary tent transform is \(\widehat T_a(\omega)=2[1-\cos(a\xi)]/\xi^2\). Taking inverse Fourier transforms proves the four-tent identity because \(P_\eta=\widehat{\mathbf1_{E_\eta}*\mathbf1_{-E_\eta}}\). The difference is in \(L^2\) since it is compactly supported; hence Plancherel applies.

**2. Exact crossover.** Because \(0<a<\ell<d\), the supports of tents centered at \(\ell\) and \(-\ell\) are disjoint, as are those centered at \(d\) and \(-d\). The only possible intersections among the four distinct tent supports are between \(\ell,d\) and between \(-\ell,-d\), at separation \(g=d-\ell\). Define \(C_a(g)=\int_{\mathbb R}T_a(t)T_a(t-g)\,dt\). Direct integration gives
\[
C_a(g)=\begin{cases}
\frac23a^3-ag^2+\frac12g^3,&0\le g\le a,\\
\frac16(2a-g)^3,&a\le g\le2a,\\
0,&g\ge2a.
\end{cases}
\]
Since \(\int T_a^2=2a^3/3\), expanding the squared four-tent sum gives
\[
\|P_\eta-P_0\|_2^2=4\int T_a^2-4C_a(g)=\frac83a^3-4C_a(g).
\]
Substituting the three overlap cases proves the displayed \(\Phi\) without approximation. In particular, the four supports are all disjoint when \(2a<g\), giving the exact separated-gap law.

**3. Sharp inverse exponent.** Reflection fixes \(E_0\) because its two component intervals have equal lengths and symmetric centers. Thus the quotient distance minimizes over translations of \(E_0\) alone. At translation zero, the four endpoint discrepancies each contribute \(a/2\); hence \(D\le2a\). Let \(t_a\) be any sequence of nearly minimizing translations. The triangle inequality implies \(\|\mathbf1_{E_0+t_a}-\mathbf1_{E_0}\|_1\le4a+o(a)\). The translation orbit of a bounded, nonempty union of intervals separates strictly away from zero, so \(t_a\to0\). For all sufficiently small \(a\) and \(|t_a|\), the four endpoint neighborhoods do not interact. Their exact symmetric-difference mass is
\[
2|t_a-a/2|+2|t_a+a/2|\ge2a.
\]
The same bound holds for every possible minimizer, proving \(D=2a\). Combining this identity with the separated-gap spectral norm yields the exact inverse \(2/3\) power along this family. If a uniform estimate \(D\le K\|P_\eta-P_0\|_2^\beta\) held for some \(\beta>2/3\) and fixed \(K\), it would require \(2a\le K(8/3)^{\beta/2}a^{3\beta/2}\) for all small \(a\), a contradiction. Uniform lower bounds on lengths and gap hold by taking, for example, \(0<a<\min\{\ell/2,g/2\}\).

## Verification
The standalone Python 3 script `verification/covariogram_check.py` computes interval intersections and exact rational integrals of the squared difference of piecewise-linear covariograms. Its independently constructed geometric answer equals \(a^3\Phi(g/a)\) in test cases in each of the three crossover regimes, and for several component lengths and gaps. The script also independently checks the Fourier-intensity identity at nonzero sample frequencies and the near-zero limit; these finite tests corroborate but do not replace the analytic proof. Reproduction: run `python3 verification/covariogram_check.py` from a directory containing the extracted artifact.

## Relationship to prior work
Xia and Xu, *Fourier Phase Retrieval for Finite Unions of Intervals* (arXiv:2606.19855v1, 18 June 2026), prove uniqueness modulo translation/reflection for two-interval indicators (their Theorem 1.2). Their Theorem 1.3(ii), as printed on page 4, also states an \(L^2\)-intensity-data Lipschitz estimate under uniform positive component-length and gap bounds. The exact family above satisfies those bounds and has data discrepancy of order \(a^{3/2}\) while its component-length difference and quotient symmetric difference are of order \(a\). **Consequently the printed Lipschitz assertion and this explicit calculation are incompatible under the stated hypotheses.** The precise point of discrepancy merits independent adjudication; this paper does not purport to correct or audit their proof. The new claimed contribution is the independently derived, exact three-regime covariogram/intensity crossover and its quantitative inverse-exponent obstruction, rather than the already known two-interval uniqueness statement. The general phase-retrieval literature supplies broader context but is not used as a substitute for comparing the primary paper.

## Limitations
This is a one-parameter family of two-interval sets with fixed centers, total length, and gap; it does not establish a universal recovery algorithm, optimality of a global Hölder upper exponent, or any statement about \(L^2\) distance of unsquared Fourier magnitudes. The \(2/3\) obstruction applies to the specifically defined \(L^2\) **squared-magnitude** data metric. Historical priority remains contingent on potentially unindexed equivalent covariogram calculations. The apparent conflict with the June 2026 publicly posted preprint's stability statement should be reviewed independently before relying on either bound.

## References
1. Yu Xia and Zhiqiang Xu, *Fourier Phase Retrieval for Finite Unions of Intervals*, arXiv:2606.19855v1 (posted 18 June 2026), https://arxiv.org/abs/2606.19855, Theorems 1.2 and 1.3(ii), pp. 3–4; primary manuscript full text, https://pdfs.assets.alphaxiv.org/2606.19855v1.pdf.
2. Standard Fourier Plancherel identity and the Fourier transform of the one-dimensional triangular kernel, used in the explicit derivation above.
