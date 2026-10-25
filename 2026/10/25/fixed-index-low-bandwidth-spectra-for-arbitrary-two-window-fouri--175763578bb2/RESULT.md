# Fixed-index low-bandwidth spectra for arbitrary two-window Fourier concentration

## Finding
Let \(E,F\subset\mathbb R\) be bounded measurable sets with \(0<|E|,|F|<\infty\). Use the Fourier convention \(\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi i x\xi}\,dx\). For \(t>0\), let \(K_t\) be the spatial Fourier concentration operator on \(L^2(E)\):
\[
K_tf(x)=\int_E\left(\int_{tF}e^{2\pi i(x-y)\xi}\,d\xi\right)f(y)\,dy.
\]
Write its nonincreasing eigenvalues, counted with multiplicity, as \(\lambda_0(t),\lambda_1(t),\ldots\). For a bounded set \(D\) of positive measure, define its raw moments and Hankel determinants by
\[
 m_j(D)=\int_Dx^j\,dx,\quad H_0(D)=1,\quad H_r(D)=\det[m_{j+k}(D)]_{j,k=0}^{r-1}\quad(r\ge1).
\]
All the \(H_r(D)\) are positive. Put \(h_n(D)=H_{n+1}(D)/H_n(D)\). Then **for every fixed integer \(n\ge0\)**,
\[
\boxed{\lim_{t\downarrow0}\frac{\lambda_n(t)}{t^{2n+1}}=
\frac{(2\pi)^{2n}}{(n!)^2}\,h_n(E)h_n(F)>0.}
\]
Furthermore, if \(p_n^E\) denotes the real monic degree-\(n\) polynomial orthogonal to lower degrees in \(L^2(E)\), the normalized \(n\)-th concentration eigenfunction \(\phi_n(t)\) can be phased so that
\[
 \phi_n(t)\longrightarrow p_n^E/\sqrt{h_n(E)}\quad\hbox{strongly in }L^2(E).
\]
In particular, every fixed eigenvalue is simple for all sufficiently small \(t>0\), and the fixed-mode spectrum is asymptotically separated by two powers of bandwidth per successive mode. The analogous frequency-side singular functions converge to the normalized monic orthogonal polynomials of \(F\).

## Assumptions and scope
The sets \(E,F\) need not be intervals, connected, symmetric, or have regular boundary. Positivity of their Lebesgue measures is required, and boundedness ensures convergence of the analytic kernel expansion in Hilbert--Schmidt norm. The index \(n\) is fixed before \(t\downarrow0\); neither uniformity in \(n\) nor uniformity over changing sets is asserted. Frequency bandwidth is dilated about the origin, \(tF\); shifting the window changes only unitary modulation and not the eigenvalues.

## Proof
**1. Exact operator reduction.** Let \(A_t:L^2(E)\to L^2(tF)\) be \((A_tf)(\xi)=\int_Ee^{-2\pi ix\xi}f(x)\,dx\). Thus \(K_t=A_t^*A_t\). The unitary dilation \((U_tg)(u)=\sqrt t\,g(tu)\) maps \(L^2(tF)\) onto \(L^2(F)\), and \(U_tA_t=\sqrt t\,T_t\), where
\[
 T_t:L^2(E)\to L^2(F),\qquad (T_tf)(u)=\int_Ee^{-2\pi itxu}f(x)\,dx.
\]
If \(s_n(t)\) are the singular values of \(T_t\), indexed from zero, then \(\lambda_n(t)=t\,s_n(t)^2\).

**2. Orthogonal-polynomial normalization.** Since a nonzero polynomial cannot vanish on a set of positive Lebesgue measure, every finite moment Gram matrix of \(D=E,F\) is strictly positive definite. Gram--Schmidt produces monic \(p_j^D\) with squared norm \(h_j(D)=H_{j+1}(D)/H_j(D)\). Let \(e_j^D=p_j^D/\sqrt{h_j(D)}\). For \(r\ge1\), write \(L=r(r-1)/2\) and denote by \(v_r^D=e_0^D\wedge\cdots\wedge e_{r-1}^D\) the unit vector in \(\bigwedge^rL^2(D)\).

**3. Leading exterior-power operator.** The determinant of the analytic kernel on \(r\) input/output variables has the absolutely, locally uniformly convergent Cauchy--Binet expansion
\[
\det[e^{-2\pi itx_au_b}]_{a,b=1}^r
=\sum_{0\le k_1<\cdots<k_r}
\frac{(-2\pi it)^{k_1+\cdots+k_r}}{k_1!\cdots k_r!}
\det[x_a^{k_b}]_{a,b=1}^r\det[u_a^{k_b}]_{a,b=1}^r.
\]
The unique smallest exponent is \(L\), from \((k_1,\ldots,k_r)=(0,\ldots,r-1)\). Its determinants are the Vandermonde polynomials; expressed in the normalized orthogonal-polynomial bases, their exterior tensor is \(v_r^F\otimes(v_r^E)^*\), multiplied by \(\prod_{j=0}^{r-1}\sqrt{h_j(E)h_j(F)}\). Including the standard antisymmetrization normalization, the induced exterior-power operator therefore satisfies
\[
 t^{-L}\bigwedge{}^rT_t\longrightarrow
 c_r\,v_r^F\otimes(v_r^E)^*
 \quad\text{in Hilbert--Schmidt norm},\qquad
 c_r=\frac{(-2\pi i)^L}{\prod_{j=0}^{r-1}j!}
 \prod_{j=0}^{r-1}\sqrt{h_j(E)h_j(F)}.
\]
Uniform convergence on \(E^r\times F^r\), since both sets are bounded, proves the Hilbert--Schmidt assertion and ensures no uncontrolled interchange of infinite sums or limits.

**4. Recover the individual eigenvalues.** The operator norm of \(\bigwedge^rT_t\) equals \(\prod_{j=0}^{r-1}s_j(t)\). From the rank-one norm limit,
\[
 \prod_{j=0}^{r-1}s_j(t)=|c_r|t^{r(r-1)/2}(1+o(1)).
\]
Divide this equation for \(r=n+1\) by the one for \(r=n\) (for \(n=0\), use the empty product \(1\)) to obtain
\[
 s_n(t)=\frac{(2\pi)^n}{n!}\sqrt{h_n(E)h_n(F)}\,t^n(1+o(1)).
\]
The exact factor \(\lambda_n=t\,s_n^2\) proves the boxed law. The ratio of successive eigenvalues is asymptotically proportional to \(t^2\), proving eventual strict separation for any fixed adjacent pair.

**5. Recover the eigenfunctions.** The normalized leading operator in Step 3 is rank one with simple nonzero singular value. Its top right singular line converges to \(\mathbb Cv_r^E\). Because the leading product of singular values is separated from the next exterior singular value, the wedge of the top \(r\) right singular vectors converges up to phase to \(v_r^E\). Consequently the rank-\(r\) right singular subspace converges in the gap topology to \(\operatorname{span}\{e_0^E,\ldots,e_{r-1}^E\}\). Subtract the limits of the consecutive rank-\(n\) and rank-\(n+1\) orthogonal projections. This yields convergence of the individual \(n\)-th right singular line to \(\mathbb Ce_n^E\) and hence the asserted strong convergence after phase choice. Applying the same reasoning to the left exterior singular vectors gives the frequency-side statement.

## Verification
A standalone reproducible numerical checker is provided in `checks/low_bandwidth_check.py`. It computes exact rational moment determinants of two disconnected, asymmetric window sets and compares predicted \(t^{2n+1}\) coefficients against singular-value quadrature. For \(E=[-1,-1/4]\cup[2/5,7/5]\) and \(F=[-1/2,-1/10]\cup[1/5,7/10]\), the ratios of the computed first three eigenvalues to their leading predictions at \(t=0.13\) were approximately \((0.9362078,0.9567692,1.0115857)\). The corresponding input-eigenfunction overlaps with the first three orthogonal polynomials were \((0.9964464,0.9958878,0.9957954)\). Both comparisons improve as \(t\) decreases. The finite computation checks normalization and examples; the proof is the exterior-power argument, not the numerical experiment.

As a closed-form normalization test, when both \(E\) and \(F\) are unit-length intervals, \(h_1(E)=h_1(F)=1/12\) and \(h_2(E)=h_2(F)=1/180\). Thus the first three limits are \(\lambda_0(t)/t\to1\), \(\lambda_1(t)/t^3\to\pi^2/36\), and \(\lambda_2(t)/t^5\to\pi^4/8100\).

## Relationship to prior work
Marceca--Romero--Speckbacher (first preprint January 27, 2023) formulate Fourier concentration on two irregular domains and prove non-asymptotic eigenvalue-counting estimates, rather than the fixed-index, shrinking-frequency limits or polynomial eigenfunction limits here. Israel--Mayeli (2023) prove spatial-spectral eigenvalue distribution estimates for expanding higher-dimensional windows. Bonami--Jaming--Karoui (2018) derive non-asymptotic bounds for the classical interval sinc operator. These results motivate the exact low-bandwidth question but their displayed statements do not determine the arbitrary-two-window constants above. Classic interval prolate asymptotics cover special geometries and are not claimed new here. Earlier moment expansions of the *principal* eigenvalue on a fixed set concern a different level of spectral information: they neither determine the entire fixed-index hierarchy for two independently irregular windows nor show convergence of every fixed eigenmode to the corresponding orthogonal polynomial.

## Limitations
The result is a fixed-mode, low-bandwidth asymptotic, not a formula for the full spectrum at a finite bandwidth or for indices increasing as \(t\downarrow0\). The convergence rate can deteriorate as the observation set degenerates or the index grows. It does not claim novel classical interval formulas. Priority comparisons were conducted with identified relevant work, but unindexed or older analytic-kernel treatments may contain an equivalent general theorem; independent historical-priority review remains appropriate. No independent verification has been performed.

## References
1. F. Marceca, J. L. Romero, M. Speckbacher, *Eigenvalue estimates for Fourier concentration operators on two domains*, arXiv:2301.11685 (version first public January 27, 2023); Archive for Rational Mechanics and Analysis 248 (2024), article 35; https://doi.org/10.1007/s00205-024-01979-9.
2. A. Israel, A. Mayeli, *On the Eigenvalue Distribution of Spatio-Spectral Limiting Operators in Higher Dimensions*, arXiv:2301.09616 (first public January 23, 2023).
3. A. Bonami, P. Jaming, A. Karoui, *Non-Asymptotic behaviour of the spectrum of the Sinc Kernel Operator and Related Applications*, arXiv:1804.01257 (first public April 4, 2018); Journal of Mathematical Physics 62 (2021), 033511.
4. S. Karnik, J. Romberg, M. A. Davenport, *Improved bounds for the eigenvalues of prolate spheroidal wave functions and discrete prolate spheroidal sequences*, arXiv:2006.00427 (first public May 31, 2020).
