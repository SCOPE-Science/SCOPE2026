# Sharp real–complex Gaussian oversampling thresholds for sketched Ritz moments

## Finding
Consider a real symmetric or complex Hermitian eigenproblem, with an orthonormal trial basis consisting of one noninvariant direction and an invariant spectator subspace. The least-squares Gaussian-sketched Rayleigh–Ritz matrix has one non-spectator Ritz eigenvalue \(\widehat\rho\). Its exact distribution depends only on the trial residual norm and the **excess sketch dimension** \(\nu=s-m+1\), not on the matrix size or the spectator eigenvalues.

In the real case, this eigenvalue has a scaled real Student distribution, and its absolute \(p\)-th moment is finite exactly for \(0<p<\nu\). In the complex case, it has a rotationally symmetric complex Student distribution, with finite absolute \(p\)-th moment exactly for \(0<p<2\nu\). In particular, if the trial residual is nonzero, its mean-square error relative to the corresponding ordinary Ritz value is finite **exactly when**
\[
\begin{array}{ll}
\text{real sketch:}&s\ge m+2,\\
\text{complex sketch:}&s\ge m+1.
\end{array}
\]
The complete squared-error expectations, when finite, are
\[
\mathbb E|\widehat\rho-\rho|^2=
\begin{cases}
\displaystyle \frac{\sigma^2}{s-m-1},&\text{real},\\[4pt]
\displaystyle \frac{\sigma^2}{s-m},&\text{complex},
\end{cases}
\]
where \(\rho=w^*Aw\) and \(\sigma=\|Aw-\rho w\|_2>0\). Thus one extra sketch row eliminates infinite mean-square error in the complex case, whereas two are necessary and sufficient in the real case. For every smaller sketch size the squared expectation is infinite, even though the sketched matrix and Ritz eigenvalues exist almost surely.

More precisely, let \(t\ge0\), and write \(I_z(a,b)\) for the regularized incomplete beta function. The *exact* upper-tail laws are
\[
\Pr(|\widehat\rho-\rho|>t)=
\begin{cases}
I_{\frac{1}{1+(t/\sigma)^2}}\!\left(\frac\nu2,\frac12\right),&\text{real},\\[6pt]
\left(1+(t/\sigma)^2\right)^{-\nu},&\text{complex}.
\end{cases}
\]
For \(p>0\), the finite moment formulas are
\[
\mathbb E|\widehat\rho-\rho|^p=\sigma^p
\begin{cases}
\displaystyle \frac{\Gamma((p+1)/2)\Gamma((\nu-p)/2)}{\sqrt\pi\,\Gamma(\nu/2)},&\text{real, }0<p<\nu,\\[6pt]
\displaystyle \frac{\Gamma(1+p/2)\Gamma(\nu-p/2)}{\Gamma(\nu)},&\text{complex, }0<p<2\nu.
\end{cases}
\]
At or beyond the indicated critical exponent, the corresponding moment diverges.

## Assumptions and scope
Let \(\mathbb F\) be either \(\mathbb R\) or \(\mathbb C\). Fix integers \(n\ge m+1\), \(m\ge2\), and \(s\ge m\). Let \(A=A^*\in\mathbb F^{n\times n}\), and let \(V\in\mathbb F^{n\times(m-1)}\) have orthonormal columns spanning an \(A\)-invariant subspace, so that \(AV=V\Lambda\) for some Hermitian \(\Lambda\). Let \(w\in\mathbb F^n\) be unit length and orthogonal to \(V\), and set \(W=[w,V]\).

Put \(\rho=w^*Aw\), \(r=Aw-\rho w\), and \(\sigma=\|r\|_2\). Assume \(\sigma>0\); the exactly invariant case \(\sigma=0\) has the deterministic non-spectator eigenvalue \(\rho\). Draw \(S\in\mathbb F^{s\times n}\) with independent standard real \(N(0,1)\) entries when \(\mathbb F=\mathbb R\), or standard circular complex Gaussian entries with independent real and imaginary \(N(0,1/2)\) parts when \(\mathbb F=\mathbb C\). Work in exact arithmetic and define the least-squares sketched Rayleigh–Ritz matrix
\[
M=(SW)^\dagger SAW\in\mathbb F^{m\times m},
\]
where \({}^\dagger\) is the Moore–Penrose inverse. Almost surely \(SW\) has full column rank, and \(M\) has all eigenvalues of \(\Lambda\), together with one non-spectator root \(\widehat\rho\). If eigenvalues coincide, this last root is defined by the distinguished first diagonal block rather than by sorting numerical eigenvalues.

No assertion here concerns selecting the correct root from an unlabeled numerical spectrum, refining it by a Rayleigh quotient, or non-Gaussian sketch distributions. The real and complex statements use their respective Gaussian normalizations; there is no hidden variance rescaling.

## Proof
Because \(A\) is Hermitian and \(V\) spans an invariant subspace, \(V^*Aw=(AV)^*w=0\). Also \(w^*r=0\). Consequently \(r\perp\operatorname{range}W\), and the nonzero unit vector \(u=r/\sigma\) is orthogonal to all columns of \(W\). With \(G=SW\) and \(z=Su\), the Gaussian vectors forming \(G\) and \(z\) are mutually independent, standard, and isotropic in \(\mathbb F^s\). We have
\[
SAW=[\rho G_{:,1}+\sigma z,\;G_{:,2:m}\Lambda].
\]
The Moore–Penrose identity \(G^\dagger G=I_m\) gives a reduced matrix whose final \(m-1\) columns equal \(\binom{0}{\Lambda}\). Therefore it is block lower triangular and its only other eigenvalue is
\[
\widehat\rho=\rho+\sigma e_1^*G^\dagger z.
\]
Let \(C=G_{:,2:m}\), and let \(P_C\) be its orthogonal projector. By the residualized least-squares coefficient formula,
\[
 e_1^*G^\dagger z=\frac{q^*z}{q^*q},\qquad q=(I-P_C)G_{:,1}.
\]
Conditionally on \(C\), the orthogonal complement of its range has \(\nu=s-m+1\) dimensions, \(q\) is a standard isotropic Gaussian vector there, and \(z\) remains independent of \(q\). Rotational invariance thus yields
\[
\frac{q^*z}{q^*q}\ \overset{\mathrm d}=\ \frac{U}{\sqrt H},
\]
where \(U\) and \(H\) are independent, with \(U\sim N(0,1)\), \(H\sim\chi^2_{\nu}\) in the real case, and \(U\sim\mathrm{CN}(0,1)\), \(H\sim\mathrm{Gamma}(\nu,1)\) in the complex case. The conditional phase of the direction \(q/\|q\|\) does not affect this law.

In the real case \(U^2\sim\chi^2_1\). The ratio \(U^2/(U^2+H)\) has the \(\mathrm{Beta}(1/2,\nu/2)\) distribution. The displayed incomplete-beta tail formula follows by inverting this ratio. In the complex case \(|U|^2\sim\mathrm{Exp}(1)\), so independence and the gamma Laplace transform give
\[
\Pr\left(\left|\frac U{\sqrt H}\right|>x\right)=\mathbb E(e^{-x^2H})=(1+x^2)^{-\nu}.
\]
The moment integrals separate into the numerator and inverse denominator moments. Standard gamma integrals yield precisely the two formulas in the Finding section. The inverse chi-square integral diverges at \(p=\nu\) in the real case, and the inverse gamma integral diverges at \(p=2\nu\) in the complex case; therefore these moment ranges are both necessary and sufficient. Substituting \(p=2\) proves the stated sharp mean-square thresholds and constants. Nothing here relies on finite sampling to establish an infinite expectation.

## Verification
The standalone `verify.py` constructs the full sketched matrices and checks the non-spectator reduced eigenvalue against an independently residualized regression formula for multiple trial dimensions, sketch widths, and both Gaussian fields. It separately tests the exact real/complex tail probabilities with seeded Gaussian experiments and checks beta/gamma moment expressions and normalization. Run `python verify.py` after installing NumPy, as specified by `requirements.txt`. The finite stochastic checks test implementation identities and distributions; the universal formulas and divergent-moment claims rest on the proof above.

## Relationship to prior work
Shao's 2026 randomized Rayleigh–Ritz proposal uses a *square* complex Gaussian Petrov–Galerkin pencil without oversampling and proves high-probability existence and convergence of favorable randomized Ritz pairs. Its Section 1 distinguishes that design from older **oversampled** sketched Rayleigh–Ritz methods. Nakatsukasa and Tropp's sketched Rayleigh–Ritz method uses the least-squares reduced matrix \((SW)^\dagger SAW\) and provides subspace-embedding and residual comparisons; it does not supply this exact field-dependent tail and moment cutoff. The present theorem treats the latter least-squares construction, not the same pencil as Shao's square procedure when \(s>m\).

An earlier exact Cauchy-law calculation covers the square complex invariant-spectator case \(s=m\). Here that case is recovered at \(\nu=1\), while positive oversampling yields a complete real/complex moment-integrability phase diagram. The underlying ratio-of-Gaussians and inverse-Wishart integrals are classical; their occurrence in this **identified non-spectator Ritz eigenvalue** and the sharp sketch-row comparison are the claims assessed here. These comparisons do not establish exhaustive uniqueness against all unindexed literature.

## Limitations
The result requires exact invariant spectator columns, an identified non-spectator root, iid Gaussian sketches, full rank almost surely, and exact arithmetic. It does not guarantee accuracy of every eigenpair, reliable selection among near-colliding Ritz values, robustness of numerical pseudoinverses, independence across adaptive sketches, or high-dimensional minimax optimality. The theorem concerns the raw sketched Ritz value, not Rayleigh-quotient refinement. The moment phase transition may also have an equivalent statement in older Gaussian regression literature under different notation; independent verification has not occurred.

## References
1. Nian Shao, *Stabilizing the Rayleigh–Ritz procedure by randomization*, arXiv:2604.01037v1 (first publicly available 2026-04-01), especially Algorithm 1, Introduction, and the probabilistic eigenpair guarantees. https://arxiv.org/abs/2604.01037
2. Yuji Nakatsukasa and Joel A. Tropp, *Fast and Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, SIAM Journal on Matrix Analysis and Applications 45 (2024), 1183–1214, DOI 10.1137/23M1565413, especially Section 6.3–6.6. Lawful author-posted text: https://www.tropp.caltech.edu/papers/NT24-Fast-Accurate-SIMAX.pdf
3. Classical Gaussian regression and chi-square/gamma ratio identities; the elementary derivations needed for this theorem appear explicitly in the Proof section.
