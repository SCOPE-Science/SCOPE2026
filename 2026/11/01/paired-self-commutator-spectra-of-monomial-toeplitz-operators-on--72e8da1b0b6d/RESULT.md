# Paired self-commutator spectra of monomial Toeplitz operators on weighted harmonic Bergman spaces

## Finding

Fix a real parameter \(\alpha>-1\) and an integer \(m\ge1\). On the complex weighted harmonic Bergman space \(\mathscr H^2_\alpha(\mathbb D)\), let \(\Pi_\alpha\) denote harmonic orthogonal projection, \(T_m=\Pi_\alpha M_{z^m}|_{\mathscr H^2_\alpha}\), and
\[
C_{\alpha,m}=T_m^*T_m-T_mT_m^*.
\]
Put
\[
h_j=\frac{\Gamma(j+1)\Gamma(\alpha+2)}{\Gamma(j+\alpha+2)}\quad(j=0,1,\ldots),
\]
and, for each integer \(k\ge1\),
\[
c_k=\begin{cases}
\displaystyle \frac{h_{k+m}-h_m^2/h_{m-k}}{h_k},&1\le k<m,\\[4pt]
\displaystyle \frac{h_{k+m}}{h_k}-\frac{h_k}{h_{k-m}},&k\ge m.
\end{cases}
\]
Then \(c_k>0\), and **the complete nonzero eigenvalue multiset** of the compact self-adjoint operator \(C_{\alpha,m}\) consists of \(\{c_k,-c_k:k\ge1\}\), with one zero eigenvalue corresponding to the constant function. Coincidental numerical repetitions are counted with their full multiplicity. In particular, every \(T_m\) is neither hyponormal nor cohyponormal, and \(\operatorname{Tr}(C_{\alpha,m})=0\).

The following sharp spectral and norm conclusions hold simultaneously:
\[
\boxed{c_k=\frac{m^2(\alpha+1)}{k^2}+O_{\alpha,m}(k^{-3}),\qquad
s_n(C_{\alpha,m})\sim\frac{4m^2(\alpha+1)}{n^2}.}
\]
Consequently, for every \(p>0\),
\[
\boxed{C_{\alpha,m}\in\mathcal S_p\iff p>\tfrac12,\qquad
\lim_{N\to\infty}\frac1{\log N}\sum_{n=1}^N s_n(C_{\alpha,m})^{1/2}
=2m\sqrt{\alpha+1}.}
\]
Here the Schatten classes with \(0<p<1\) are understood in the quasi-norm sense, and singular values are counted with multiplicity in nonincreasing order. Thus \(C_{\alpha,m}\) lies in the weak endpoint ideal \(\mathcal S_{1/2,\infty}\), but not in \(\mathcal S_{1/2}\).

Its exact nuclear norm is a **finite moment expression**:
\[
\boxed{\|C_{\alpha,m}\|_{\mathcal S_1}=2m-2\sum_{j=0}^{m-1}\frac{h_m^2}{h_jh_{m-j}}.}
\]
For each fixed \(m\), this norm is strictly increasing as \(\alpha\) runs through \((-1,\infty)\), with respective endpoint limits \(0\) and \(2m\). On the unweighted space \(\alpha=0\), both trace and operator norms simplify:
\[
\boxed{\|C_{0,m}\|_{\mathcal S_1}=\frac{m(5m+1)}{3(m+1)},\qquad
\|C_{0,m}\|=\frac{m^2}{(m+1)(2m+1)}.}
\]

## Assumptions and scope

All functions are complex-valued and harmonic in the open disk \(\mathbb D\), with square-integrability for the probability measure
\[
d\mu_\alpha(z)=\frac{\alpha+1}{\pi}(1-|z|^2)^\alpha\,dx\,dy,\qquad z=x+iy.
\]
This normalization gives \(\int_{\mathbb D}|z|^{2j}\,d\mu_\alpha=h_j\) and \(h_0=1\). Multiplication by \(z^m\) is bounded on ambient \(L^2\), so its harmonic compression \(T_m\) is bounded. Use the orthonormal basis \(e_0=1\), \(e_k=z^k/\sqrt{h_k}\) for \(k>0\), and \(e_{-j}=\overline z^{\,j}/\sqrt{h_j}\) for \(j>0\), indexed by all integers. We use \(\mathcal S_p\) for the Schatten ideal on this Hilbert space and \(s_n\) for decreasing singular values indexed from one.

## Proof

**1. Exact bilateral shift model.** Rotational symmetry makes each angular Fourier sector one-dimensional inside the harmonic subspace. Taking inner products with the unique sector basis vector gives
\[
T_m e_k=w_k e_{k+m},\qquad w_k>0,
\]
where
\[
w_k^2=\begin{cases}
\displaystyle h_{k+m}/h_k,&k\ge0,\\[3pt]
\displaystyle h_m^2/(h_{-k}h_{m+k}),&-m\le k<0,\\[3pt]
\displaystyle h_{-k}/h_{-k-m},&k<-m.
\end{cases}
\]
For example, in the middle regime the defining inner product reduces to \(\int |z|^{2m}\,d\mu_\alpha=h_m\). At \(k=-m\), the two applicable endpoint formulas agree. The weights obey the exact reflection \(w_{-m-k}^2=w_k^2\), as a direct case check shows.

**2. Symmetric diagonal commutator and positivity.** Orthogonality implies
\[
C_{\alpha,m}e_k=(w_k^2-w_{k-m}^2)e_k.
\]
The reflection identity makes the diagonal coefficient zero at \(k=0\), odd in \(k\), and exactly \(c_k\) at positive indices. To show strict positivity, note that
\[
\frac{h_{j+1}}{h_j}=\frac{j+1}{j+\alpha+2}
\]
is strictly increasing with \(j\ge0\), since \(\alpha+1>0\). Thus \((h_j)\) is strictly log-convex. When \(1\le k<m\), the inequality \(h_m^2<h_{m-k}h_{m+k}\) makes \(c_k>0\). For \(k\ge m\), the successive ratios \(h_{j+m}/h_j\) increase strictly in \(j\), giving \(c_k>0\) again.

**3. Sharp tail coefficient and complete ideal boundary.** For \(k\ge m\), set \(r(k)=h_{k+m}/h_k\). The exact product
\[
r(k)=\prod_{\ell=1}^m\frac{k+\ell}{k+\alpha+1+\ell}
\]
has an expansion \(r(k)=1-m(\alpha+1)/k+B_{\alpha,m}/k^2+O_{\alpha,m}(k^{-3})\). Consequently
\[
c_k=r(k)-r(k-m)=m^2(\alpha+1)/k^2+O_{\alpha,m}(k^{-3}).
\]
Because each \(c_k\) occurs with each sign, the counting function for singular values above a small level \(t>0\) is asymptotic to \(2m\sqrt{(\alpha+1)/t}\). Inverting this relation proves \(s_n\sim4m^2(\alpha+1)/n^2\) without presupposing that all low-index \(c_k\) are monotone. Summing their \(p\)-powers proves the exact \(p=1/2\) transition and the weak-ideal statement. Taking square roots and harmonic sums proves the stated logarithmic coefficient. The absolute summability also proves compactness and trace-class membership; the positive-negative pairing then gives trace zero.

**4. Finite formula for the nuclear norm.** Summation of the positive eigenvalues telescopes:
\[
\sum_{k=1}^{N}(w_k^2-w_{k-m}^2)
=\sum_{k=N-m+1}^{N}w_k^2-\sum_{k=1-m}^{0}w_k^2
\quad(N\ge m).
\]
The first sum tends to \(m\), because each \(w_k^2\to1\) as \(k\to\infty\). The second is exactly \(\sum_{j=0}^{m-1}h_m^2/(h_jh_{m-j})\). Twice the positive sum equals the trace norm, proving the finite formula.

**5. Strict weight-parameter monotonicity and limiting values.** Write \(S_q(\alpha)=\sum_{r=1}^{q}(\alpha+1+r)^{-1}\), with \(S_0=0\). Differentiating each positive term in the finite trace-norm subtraction gives
\[
\frac{d}{d\alpha}\log\frac{h_m^2}{h_jh_{m-j}}
=-2S_m(\alpha)+S_j(\alpha)+S_{m-j}(\alpha)<0
\quad(0\le j<m).
\]
Both \(j\) and \(m-j\) are at most \(m\), with at least one strictly smaller, so the inequality is strict. Hence the trace norm increases strictly. As \(\alpha\downarrow-1\), every fixed \(h_j\to1\), and the expression tends to zero. As \(\alpha\to\infty\), \(h_j\sim j!(\alpha+1)^{-j}\); every subtracted term tends to zero, and the trace norm tends to \(2m\).

**6. Explicit unweighted maximum.** At \(\alpha=0\), \(h_j=(j+1)^{-1}\), so the positive eigenvalues reduce to
\[
c_k=\begin{cases}
\displaystyle\frac{k^2(k+1)}{(m+1)^2(k+m+1)},&1\le k<m,\\[4pt]
\displaystyle\frac{m^2}{(k+1)(k+m+1)},&k\ge m.
\end{cases}
\]
The first expression is strictly increasing in its index; the second strictly decreasing. Their common peak at \(k=m\) gives the exact operator norm. Finally,
\[
\sum_{j=0}^{m-1}\frac{h_m^2}{h_jh_{m-j}}
=\frac{m(m+5)}{6(m+1)}
\]
by elementary polynomial summation, producing the announced trace norm.

## Verification

The standalone file `verify.py` tests the bilateral-weight reflection, diagonal sign pairing, all positive-eigenvalue formulas, positivity, finite telescoping identities, exact unweighted rational identities, unweighted maximality, and high-precision tail coefficients. It reports `PASS checks: 29580` when executed using Python 3 and the `mpmath` package. Exact tests use `fractions.Fraction` for \(\alpha\in\{-3/4,-1/2,0,1/2,1,2,4\}\) and \(1\le m\le12\); the asymptotic tests use 65-digit arithmetic. The code does not replace the analytic infinite-index proof.

## Relationship to prior work

Chbichib and Ghiloufi (arXiv:2605.24698; first public May 23, 2026) find the order \(n^{-1}\) singular-value law for the *ambient projection commutator* \([M_u,\Pi_\alpha]\), acting on ambient \(L^2\), under their symbol hypotheses. The present claim concerns the different, compressed *Toeplitz self-commutator* \(T_m^*T_m-T_mT_m^*\), with the sharper \(n^{-2}\) tail and a signed complete spectrum. Their theorem does not state the finite trace-norm expression or the all-parameter ideal threshold here.

Huang, Wang, and Zhao (arXiv:2610.09638; October 7, 2026) determine ordinary spectra and isolated eigenvalue structure for analytic-polynomial Toeplitz operators on unweighted harmonic Bergman space, not the weighted self-commutator's full singular spectrum. Sadraoui and Halouani (2024, Theorem 2.9) already establish qualitative nonnormality for nonconstant analytic-symbol Toeplitz operators on this weighted harmonic space; that fact is credited, not claimed new. Existing work by Iqtaish–Louhichi–Yousef and Wang–Zhao likewise treats normality or commutation, not the exact signed spectrum and ideal formulas. The closed formulas here derive from direct radial-moment computation, and possible equivalent earlier weighted-shift identities cannot be ruled out solely by claim-focused searches.

## Limitations

This theorem concerns *single analytic monomials* and the specific beta-family disk weights, not general analytic polynomials, general radial weights, or higher-dimensional harmonic Bergman spaces. The closed operator-norm expression is proved only for \(\alpha=0\); no universal weighted operator-norm formula is claimed. Numerical tests are finite and do not certify the infinite spectrum or priority. Literature coverage is incomplete, especially inaccessible historical full texts and the possibility of a stronger general shift theorem. No independent mathematical audit has been performed.

## References

1. K. Chbichib and N. Ghiloufi, *Spectral properties of commutators on harmonic Bergman spaces of the unit disk*, arXiv:2605.24698 (first submitted May 23, 2026), https://arxiv.org/abs/2605.24698.
2. M. Huang, J. Wang, and X. Zhao, *The spectral structure of Toeplitz operators with polynomial symbols on the harmonic Bergman space*, arXiv:2610.09638 (first submitted October 7, 2026), https://arxiv.org/abs/2610.09638.
3. H. Iqtaish, I. Louhichi, and A. Yousef, *On the commuting problem of Toeplitz operators on the harmonic Bergman space*, AIMS Mathematics 10 (2025), 17232–17247, https://doi.org/10.3934/math.2025770.
4. C. Wang and X. Zhao, *Normal and hyponormal Toeplitz operators on the harmonic Bergman space*, Journal of the Korean Mathematical Society 63 (2026), 99–117, https://doi.org/10.4134/JKMS.j240518.
5. H. Sadraoui and B. Halouani, *Commuting Toeplitz operators on weighted harmonic Bergman spaces and hyponormality on the Bergman space of the punctured unit disk*, AIMS Mathematics 9 (2024), 20043–20057, https://doi.org/10.3934/math.2024977.
6. Z. Wu, *Operators on harmonic Bergman spaces* (1996), discussed in reference 1; full text not independently inspected.
