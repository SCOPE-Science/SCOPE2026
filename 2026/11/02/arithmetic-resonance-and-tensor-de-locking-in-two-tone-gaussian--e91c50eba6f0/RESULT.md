# Arithmetic resonance and tensor de-locking in two-tone Gaussian localization

## Finding
In the Gaussian Bargmann–Fock spaces of one and two complex variables, consider the two positive radial or separately radial weights
\[
 a_\eta(z)=\frac12+\frac14\bigl(\cos(2|z|)+\cos(2\eta|z|)\bigr),\qquad
 b_\eta(z_1,z_2)=\frac12+\frac14\bigl(\cos(2|z_1|)+\cos(2\eta|z_2|)\bigr),
\]
for every real \(\eta>0\). Both lie in \([0,1]\). Their Toeplitz compressions are denoted \(T_\eta^{\mathrm{lock}}\) and \(T_\eta^{\mathrm{sep}}\). Write \(A=e^{-1/2}\), \(B_\eta=e^{-\eta^2/2}\), and let \(\nu_\eta\) be the probability law
\[
 \frac12+\frac14(A\cos U+B_\eta\cos V),
\]
where \(U,V\) are independent uniform angles on \([0,2\pi)\).

**Resonance theorem.** The empirical eigenvalue law of \(T_\eta^{\mathrm{sep}}\), under both square and total-degree Hermite cutoffs, converges weakly to \(\nu_\eta\) for **all** \(\eta>0\). The one-dimensional empirical eigenvalue law converges to \(\nu_\eta\) for irrational \(\eta\), but for rational \(\eta=p/q>0\) in lowest terms it converges to the law \(\mu_{p/q}\) of
\[
 \frac12+\frac14(A\cos(qU)+B_{p/q}\cos(pU)).
\]
For integers \(0\le r<p+q\), the centered \(r\)-th moments of \(\mu_{p/q}\) and \(\nu_{p/q}\) agree exactly. At the first possible distinguishing order they differ by the strictly positive amount
\[
 \int(x-\tfrac12)^{p+q}\,d\mu_{p/q}(x)
 -\int(x-\tfrac12)^{p+q}\,d\nu_{p/q}(x)
 =\frac{\binom{p+q}{p}A^pB_{p/q}^{q}}{2^{3(p+q)-1}}.
\]
Thus **the first moment that detects a reduced rational frequency ratio \(p/q\) is precisely order \(p+q\)**; separating the two oscillations into independent Fock coordinates erases this resonance from the limiting moments at every order.

The one-variable Fredholm essential spectrum is always a compact interval. Its upper endpoint is \(\frac12+\frac14(A+B_\eta)\). Its lower endpoint equals \(\frac12-\frac14(A+B_\eta)\) when \(\eta\) is irrational or, in lowest terms, has both numerator and denominator odd. For a reduced rational with one even member, the lower endpoint is strictly greater. In the illustrative exact resonance \(\eta=2\),
\[
 \sigma_{\mathrm{ess}}(T_2^{\mathrm{lock}})=
 \left[\frac12+\frac{-A+e^{-2}}4,\ \frac12+\frac{A+e^{-2}}4\right],
 \qquad \int(x-\tfrac12)^3\,d\mu_2(x)=\frac{3A^2e^{-2}}{256}.
\]
Along irrational \(\eta\to2\), its lower essential spectral endpoint approaches the strictly smaller value \(\frac12-\frac14(A+e^{-2})\), a drop of \(e^{-2}/2\).

## Assumptions and scope
Use \(\mathcal F^2(\mathbb C^d)=\{f\text{ entire}:\pi^{-d}\int_{\mathbb C^d}|f(z)|^2e^{-|z|^2}dA(z)<\infty\}\), with orthogonal projection \(P_d\) and \(T_a=P_dM_a|_{\mathcal F^2}\). The normalized monomials are \(e_{\mathbf n}(z)=z_1^{n_1}\cdots z_d^{n_d}/\sqrt{n_1!\cdots n_d!}\). No finite-support or compactness hypothesis is made on either bounded symbol.

For the one-variable operator use \(\frac1N\sum_{n=0}^{N-1}\delta_{\lambda_n}\). For the two-variable operator, use either \(\frac1{N^2}\sum_{m,n=0}^{N-1}\delta_{\lambda_{m,n}}\), or \(\frac2{(N+1)(N+2)}\sum_{m+n\le N}\delta_{\lambda_{m,n}}\). These are distributions of diagonals under specified finite-dimensional Hermite exhaustions, not a claim about all alternative index-ordering conventions.

## Proof
**1. Exact diagonalization.** Angular orthogonality and product Gaussian integration show that, writing
\[
 c_n(\omega)=\frac1{n!}\int_0^\infty e^{-t}t^n\cos(2\omega\sqrt t)\,dt
 ={}_1F_1(n+1;\tfrac12;-\omega^2),
\]
we have
\[
 \lambda_n^{\mathrm{lock}}=\frac12+\frac14(c_n(1)+c_n(\eta)),\qquad
 \lambda_{m,n}^{\mathrm{sep}}=\frac12+\frac14(c_m(1)+c_n(\eta)).
\]
The hypergeometric identity follows by termwise integration of the cosine's everywhere-convergent power series (justified initially by absolute integration of its hyperbolic-cosine majorant). Alternatively, only the displayed gamma integral is needed.

**2. Gaussian radius asymptotic.** Let \(G_n\) be gamma-distributed with shape \(n+1\) and unit scale, so \(G_n\) is a sum of \(n+1\) independent unit exponentials. The central limit theorem and the identity
\[
 \sqrt{G_n}-\sqrt{n+1}=
 \frac{G_n-(n+1)}{\sqrt{G_n}+\sqrt{n+1}}
\]
show convergence in distribution to a centered normal with variance \(1/4\). Taking its characteristic function at fixed frequency \(2\omega\) yields
\[
 c_n(\omega)=e^{-\omega^2/2}\cos(2\omega\sqrt{n+1})+o_\omega(1),\qquad n\to\infty.
\]
The \(o(1)\) is absolute for each fixed \(\omega\), sufficient for all finite sums and empirical laws here.

**3. Square-root phases.** For every fixed nonzero real \(c\), comparing \(\sum_{n\le N}e^{ic\sqrt n}\) with its integral by the bound on \(\int|\frac d{dx}e^{ic\sqrt x}|dx\), then integrating \(2\int y e^{icy}dy\), gives \(\sum_{n\le N}e^{ic\sqrt n}=O_c(\sqrt N)\). The Weyl criterion therefore makes \(2\sqrt{n+1}\) equidistributed modulo \(2\pi\); the joint phases \((2\sqrt{n+1},2\eta\sqrt{n+1})\) are equidistributed on the full two-torus when \(\eta\) is irrational, and on the one-dimensional subgroup \(\{(qt,pt):t\in\mathbb T\}\) when \(\eta=p/q\) is reduced. A shift of \(\sqrt n\) to \(\sqrt{n+1}\) does not affect the argument.

For independent index coordinates \(m,n\), the two phases equidistribute on the product torus regardless of \(\eta\). The same holds over \(m+n\le N\): a nonconstant Fourier character of the phase pair leads to a double sum in which at least one frequency is nonzero; sum over that index first using the \(O_c(\sqrt L)\) bound, obtaining \(O(N^{3/2})\) against \(\asymp N^2\) index pairs. Uniform approximation of continuous test functions by trigonometric polynomials and then by polynomials in the spectral variable proves both weak convergence assertions. The asymptotic eigenvalue errors vanish in Cesàro mean because they tend to zero as their respective indices diverge, while the bounded number of boundary rows has vanishing normalized mass.

**4. Sharp rational moment threshold.** With \(\eta=p/q\), expand the centered moment using
\[
 (A\cos(qt)+B\cos(pt))^r
 =\sum_{j=0}^{r}\binom rj A^jB^{r-j}\cos^j(qt)\cos^{r-j}(pt).
\]
In the exponential expansion, a nontrivial mixed constant term requires nonzero integers \(k,\ell\) satisfying \(qk+p\ell=0\), with \(|k|\le j\), \(|\ell|\le r-j\). Coprimality forces \(|k|\ge p\), \(|\ell|\ge q\), and hence \(r\ge p+q\). Terms with \(k=\ell=0\) exactly match independent uniform angles. At \(r=p+q\), the only new terms use \(j=p\), opposite all-positive/all-negative exponential choices in the two factors, giving \(2\binom{p+q}{p}A^pB^q/2^{p+q}\), then the factor \(4^{-(p+q)}\). This gives the stated positive difference and proves minimality.

**5. Essential spectral edges in one variable.** A diagonal self-adjoint operator has as Fredholm essential spectrum precisely the set of tail accumulation values (including repeated tail eigenvalues). By step 2 and equidistribution in step 3, the tail cluster set is the connected image of the relevant one-torus or two-torus under the continuous cosine sum. Its maximum is always \(A+B\). Its minimum is \(-A-B\) in the irrational case. In the rational case, both cosine terms can be \(-1\) simultaneously exactly when coprime \(p,q\) are both odd; otherwise strict compactness gives a strictly larger minimum. For \(p=2,q=1\), the derivative of \(A\cos t+B\cos2t\) is \(-\sin t(A+4B\cos t)\); since \(A>4B\) (equivalently \(e^{3/2}>4\)), its minimum is \(-A+B\) at \(t=\pi\). This proves the displayed interval and discontinuous irrational approach.

## Verification
The supplied standalone Python checker recomputes the rational-versus-independent Haar moments with exact rational Fourier coefficients for every coprime \(1\le p,q\le7\), through the first resonance, independently tests the gamma-integral and confluent-hypergeometric formulas for several indices and frequencies at high precision, and performs numerical consistency checks on finite square-root-phase samples. It passed 388 deterministic assertions. These checks corroborate the calculations; they do not replace the Gaussian limit, Weyl, or essential-spectrum proofs above.

## Relationship to prior work
Esmeral and Maximenko (arXiv:1505.07906, 2015), especially Proposition 6.5 and Example 4.5, already prove general radial Gaussian heat-smoothing asymptotics and a single-cosine spectral example. Dewage and Ólafsson (arXiv:2107.01465, first public July 3, 2021) give the quasi-radial monomial decomposition in several Fock coordinates. Looi (arXiv:2603.10879, March 2026) develops single-frequency radial cosine asymptotics for an essential-positivity problem. Dörfler and Gröchenig (arXiv:0912.1945, 2009) establish the time-frequency localization framework. None of these inspected results states the rational \(p+q\) moment detection threshold and its disappearance under coordinate separation, or the parity classification of the locked essential lower edge. The diagonalization and one-frequency smoothing are **prior facts**, not claimed as new; the arithmetic comparison is the proposed contribution.

## Limitations
The results concern these explicit bounded two-tone weights, fixed positive frequency ratio, standard Gaussian normalization, and the indicated Hermite index exhaustions. The entire Fredholm essential spectrum of the *two-coordinate* operator is **not** asserted to equal its two-coordinate bulk limit interval: sequences with one index fixed and the other tending to infinity can contribute additional essential spectral values, and low-index one-dimensional cosine coefficients can lie outside their asymptotic amplitude range. No theorem about finite-index outlier counts, full operator norms, arbitrary radial apertures, or more than two tones is claimed. The completeness of historical priority beyond inspected works remains open; independent validation has not been performed.

## References
1. V. Dewage and G. Ólafsson, *Toeplitz operators on the Fock space with quasi-radial symbols*, arXiv:2107.01465 (first public 2021-07-03), especially Section 2 and Theorem 2.12.
2. K. Esmeral and E. A. Maximenko, *Radial Toeplitz operators on the Fock space and square-root-slowly oscillating sequences*, arXiv:1505.07906 (2015), Example 4.5 and Proposition 6.5.
3. S. Looi, *Positive Berezin liminf does not imply essential positivity for radial Toeplitz operators on Bergman and Fock spaces*, arXiv:2603.10879 (2026), Section 2.
4. M. Dörfler and K. Gröchenig, *Time-frequency partitions and characterizations of modulation spaces with localization operators*, arXiv:0912.1945 (2009), Section 1.
