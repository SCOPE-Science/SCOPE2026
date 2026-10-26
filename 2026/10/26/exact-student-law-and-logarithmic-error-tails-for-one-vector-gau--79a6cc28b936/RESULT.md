# Exact Student law and logarithmic error tails for one-vector Gaussian-sketched matrix exponentials

## Finding
For every finite real symmetric positive-definite matrix \(A\in\mathbb R^{n\times n}\), nonzero \(b\in\mathbb R^n\), integer \(2\le\ell<n\), and \(t>0\), consider the **one-vector sketched FOM** approximation to \(e^{-tA}b\), using a real Gaussian sketch \(S\in\mathbb R^{\ell\times n}\) with independent \(N(0,1/\ell)\) entries:
\[
 v=b/\|b\|_2,\qquad
 \widehat\lambda=\frac{(Sv)^{\mathsf T}(SAv)}{\|Sv\|_2^2},\qquad
 \widehat y(t)=e^{-t\widehat\lambda}b.
\]
Set the ordinary Rayleigh quotient and its residual norm to
\[
 \alpha=v^{\mathsf T}Av,\qquad
 \rho=\|Av-\alpha v\|_2.
\]
If \(\rho=0\), then \(\widehat y(t)=e^{-tA}b\) almost surely. If \(\rho>0\), then the *exact*, unconditioned sketched Ritz law is
\[
 \boxed{\widehat\lambda\ \stackrel{\mathrm d}=\ \alpha+\frac{\rho}{\sqrt\ell}\,T_\ell},
\]
where \(T_\ell\) has the Student distribution with \(\ell\) degrees of freedom. Thus its absolute moments are finite precisely for orders below \(\ell\). More strikingly, letting \(E(t)=\|\widehat y(t)-e^{-tA}b\|_2\), both the approximation norm and the *actual error* have the same exact logarithmic tail asymptotic:
\[
 \boxed{\lim_{R\to\infty}(\log R)^\ell\,\Pr\{E(t)>R\}
 =\frac{\Gamma((\ell+1)/2)}{\ell\sqrt\pi\,\Gamma(\ell/2)}(t\rho)^\ell.}
\]
The identical limit holds with \(E(t)\) replaced by \(\|\widehat y(t)\|_2\). In particular, for **every** real \(p>0\),
\[
 \boxed{\mathbb E\,E(t)^p=\mathbb E\,\|\widehat y(t)\|_2^p=+\infty,}
\]
even when the exact semigroup \(e^{-tA}\) is contractive. The moment failure persists for every *finite* number of Gaussian sketch rows \(\ell\).

## Assumptions and scope
The construction is precisely the one-vector specialization of the sketched-FOM matrix-function approximation. The Gaussian sketch is sampled **without rejection or conditioning on the subspace-embedding event**. Sketch size \(\ell\) is any fixed integer with \(2\le\ell<n\); the matrix \(A\) is real symmetric positive definite; \(b\ne0\); the time \(t\) is strictly positive; all equalities concern exact arithmetic. No assertion is made for higher Krylov dimensions, structured bounded sketches, normalized or clipped Ritz values, or sketches explicitly required to pass a post-draw embedding check.

## Proof
**1. Exact projection identity.** A one-column Krylov basis is the unit vector \(v\), and \((Sv)^\dagger=(Sv)^{\mathsf T}/\|Sv\|_2^2\) whenever \(Sv\ne0\), an almost-sure event for a Gaussian sketch. Inserting this into the sketched FOM formula gives \(\widehat y(t)=e^{-t\widehat\lambda}b\) with the displayed \(\widehat\lambda\). If \(\rho=0\), then \(Av=\alpha v\), so \(\widehat\lambda=\alpha\) and the approximation is exact.

**2. Student-law lemma.** Suppose \(\rho>0\) and put \(w=(Av-\alpha v)/\rho\). Symmetry ensures \(w\perp v\), and \(w,v\) are unit vectors. Write \(Av=\alpha v+\rho w\). By rotational invariance of independent Gaussian rows, \(G=\sqrt\ell Sv\) and \(H=\sqrt\ell Sw\) are independent \(N(0,I_\ell)\) vectors. Hence
\[
 \frac{\widehat\lambda-\alpha}{\rho}
 =\frac{G^{\mathsf T}H}{G^{\mathsf T}G}
 =\frac{Z}{R_\ell},\qquad
 Z=\frac{G^{\mathsf T}H}{\|G\|_2},\quad R_\ell=\|G\|_2.
\]
Conditionally on \(G\), \(Z\) is standard normal with a distribution independent of \(G\); it is therefore independent of \(R_\ell\). Moreover \(R_\ell^2\sim\chi^2_\ell\). Thus \(Z/R_\ell=T_\ell/\sqrt\ell\), establishing the distribution. Equivalently, \(Y=(\widehat\lambda-\alpha)/\rho\) has exact density
\[
 g_\ell(y)=\frac{\Gamma((\ell+1)/2)}{\sqrt\pi\,\Gamma(\ell/2)}
       (1+y^2)^{-(\ell+1)/2},\qquad y\in\mathbb R.
\]
This strictly positive density is asymptotic to a positive constant times \(|y|^{-\ell-1}\), giving the stated polynomial-moment threshold for \(\widehat\lambda\).

**3. Sharp logarithmic tail.** Put \(c_\ell=\Gamma((\ell+1)/2)/(\sqrt\pi\Gamma(\ell/2))\). Direct integration of the exact density gives \(\Pr\{Y>u\}\sim(c_\ell/\ell)u^{-\ell}\) as \(u\to\infty\), and the law is symmetric. Since
\[
 \|\widehat y(t)\|_2=\|b\|_2\exp(-t\alpha-t\rho Y),
\]
for sufficiently large \(R\),
\[
 \Pr\{\|\widehat y(t)\|_2>R\}
 =\Pr\!\left\{Y< -\frac{\log(R/\|b\|_2)+t\alpha}{t\rho}\right\}.
\]
The preceding Student tail immediately gives the positive constant in the theorem. The reverse triangle inequality yields
\[
 \left|E(t)-\|\widehat y(t)\|_2\right|\le\|e^{-tA}b\|_2,
\]
and the exact norm on the right is finite. Sandwiching the error tail between those of \(\|\widehat y(t)\|_2\) at thresholds shifted by this constant yields the *same* logarithmic-tail coefficient.

**4. Infinite moments.** For any \(p,t,\rho>0\), the negative half-line in the density integral gives
\[
 \mathbb E\|\widehat y(t)\|_2^p
 =\|b\|_2^pe^{-pt\alpha}\int_{\mathbb R}e^{-pt\rho y}g_\ell(y)\,dy
 =+\infty,
\]
because exponential growth as \(y\to-\infty\) dominates polynomial density decay. On the event where \(\|\widehat y(t)\|_2>2\|e^{-tA}b\|_2\), the error is at least half the approximation norm. Excluding the complementary bounded-norm event cannot remove an infinite positive moment; therefore \(\mathbb E E(t)^p=+\infty\) as well.

**5. Genuine dimension reduction and the sharp special case.** For every \(\ell\ge2\), take \(n=\ell+2\), \(A=\operatorname{diag}(1,3,2,\ldots,2)\), and \(b=(e_1+e_2)/\sqrt2\). Then \(A\) is positive definite, \(\alpha=2\), and \(\rho=1\). The sketch has strictly fewer rows than columns. At \(\ell=2\) and \(t=1\), the actual error obeys
\[
 \boxed{\Pr\{E(1)>R\}\sim\frac1{4(\log R)^2}.}
\]
This is a nonvanishing and exactly calibrated rare-event phenomenon, not an artifact of an indefinite or singular input matrix.

## Verification
The self-contained `verify.py` reproduces the one-column sketched projection directly for five sketch sizes, checks the eigenvector exception, compares empirical one-sided tails with exact two- and three-row Student formulas, verifies the corresponding asymptotic constants, and constructs deterministic sketches with negative projected decay rates. It uses only the Python standard library, a fixed pseudorandom seed, and 120,028 check instances. The Gaussian simulation is corroboration only; the all-dimensional assertions above follow from the analytical change of variables and exact density.

## Relationship to prior work
The sketched FOM approximation comes from Güttel and Schweitzer (2022), particularly the sketched Galerkin formula and its one-dimensional specialization. Their Section 2.3 observes that sketched Ritz values can leave the spectral region, including the positive half-plane, and notes possible instability; that *qualitative observation is not new*. Cortinovis, Kressner and Nakatsukasa (2022) give equivalent randomized Krylov formulations. Palitta, Schweitzer and Simoncini (2023) analyze outlying sketched Ritz values and matrix-function approximations, especially conditional embedding quality and larger Krylov spaces. Bergermann (2026) develops deterministic embeddings, which are outside the unconditioned Gaussian experiment here. The present result is the exact **unconditional** Student law and its ensuing sharp error-tail constant and full moment-divergence classification for a one-vector Gaussian-sketched exponential; it does not contradict results conditioned on successful embeddings.

Indeed, on an \(\varepsilon\)-subspace-embedding event for \(\operatorname{span}\{v,w\}\), with \(0<\varepsilon<1\), the Gram inner-product error is at most \(\varepsilon\), giving \(|\widehat\lambda-\alpha|\le\rho\varepsilon/(1-\varepsilon)\). Such conditional deterministic bounds are consistent with the infinite unconditional moments arising from low-probability sketch failures. A previous heavy-tail result for one-row sketched GMRES(1) uses a different rational update and does not imply the exponential-of-a-Gaussian-ratio result here.

## Limitations
This is a one-vector, exact-arithmetic, *unconditioned Gaussian* statement. The impossibility of finite unconditional moments does **not** imply a typical sketch gives a large error, nor that the complete multi-vector Krylov process behaves similarly. It says nothing about floating-point overflow frequencies, runtime quality, complex or structured sketches, certified embedding rejection, or stable alternative formulations. The exact stationary or long-time behavior of an exponential integrator using this approximation is not considered. The probability-law ingredients are classical; possible equivalent expressions in random-design projection literature create a remaining publication-priority risk.

## References
1. S. Güttel and M. Schweitzer, *Randomized sketching for Krylov approximations of large-scale matrix functions*, arXiv:2208.11447v1, first submitted 2022-08-24. https://arxiv.org/abs/2208.11447
2. A. Cortinovis, D. Kressner and Y. Nakatsukasa, *Speeding up Krylov subspace methods for computing f(A)b via randomization*, arXiv:2212.12758v1, 2022-12-24. https://arxiv.org/abs/2212.12758
3. D. Palitta, M. Schweitzer and V. Simoncini, *Sketched and truncated polynomial Krylov methods: Evaluation of matrix functions*, arXiv:2306.06481v1, first submitted 2023-06-10. https://arxiv.org/abs/2306.06481
4. K. Bergermann, *Deterministic sketching for Krylov subspace methods*, arXiv:2604.07158v1, 2026-04-08. https://arxiv.org/html/2604.07158v1
