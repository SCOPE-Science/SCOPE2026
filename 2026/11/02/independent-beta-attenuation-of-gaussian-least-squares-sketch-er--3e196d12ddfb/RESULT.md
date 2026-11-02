# Independent beta attenuation of Gaussian least-squares sketch error by a Haar sketch

## Finding

For any fixed real rank-one least-squares design, a uniform orthonormal sketch has **the full coefficient-error distribution of a Gaussian sketch multiplied by an independent beta square-root factor**. Thus the mean-squared-error advantage of orthonormal sketching extends to *every* upper error quantile, all increasing error losses, and exact leading constants for catastrophic-error tails.

Precisely, fix integers \(n>\ell\ge2\), \(d,p\ge1\), a deterministic rank-one matrix \(A\in\mathbb R^{n\times d}\), and an arbitrary deterministic right-hand-side matrix \(B\in\mathbb R^{n\times p}\). Let \(X_*=A^+B\) be the minimum-norm least-squares solution. For a random \(n\times\ell\) sketch \(\Omega\), define \(\widehat X_{\Omega}=(\Omega^\mathsf TA)^+(\Omega^\mathsf TB)\). Let \(\Omega_G\) have independent standard real Gaussian entries, and \(\Omega_H\) have Haar-uniform orthonormal columns. Their experiments are considered separately.

There is a coupling of their *error laws* such that
\[
\boxed{\widehat X_{\Omega_H}-X_*\ \overset{d}=\ \sqrt{\mathcal B}\,(\widehat X_{\Omega_G}-X_*)},
\qquad
\mathcal B\sim\operatorname{Beta}\left(\frac{n-\ell}{2},\frac{\ell-1}{2}\right),
\]
where \(\mathcal B\) is independent of the Gaussian-sketch error on the right. Equality in distribution does **not** assert an almost-sure identity between independently implemented algorithms.

Put \(R=(I-AA^+)B\), the optimal least-squares residual, and \(\Delta_\Omega=\|A(\widehat X_\Omega-X_*)\|_F^2=\|B-A\widehat X_\Omega\|_F^2-\|R\|_F^2\). Then
\[
\boxed{\Delta_H\overset d=\mathcal B\Delta_G},
\]
with independent factors on the right. If \(R\ne0\), then \(\Pr(\Delta_H>t)<\Pr(\Delta_G>t)\) for **every** \(t>0\). For \(0<s<\ell/2\),
\[
\frac{\mathbb E\Delta_H^s}{\mathbb E\Delta_G^s}
=\frac{\Gamma((n-\ell)/2+s)\Gamma((n-1)/2)}
{\Gamma((n-\ell)/2)\Gamma((n-1)/2+s)};
\]
both moments are infinite for \(s\ge\ell/2\) when \(R\ne0\). In particular, if \(\ell>2\), the expected excess residual-error ratio is \((n-\ell)/(n-1)\), in agreement with the existing mean-error theorem.

More sharply, take a standard Gaussian vector \(Z\) in the \((n-1)\)-dimensional space orthogonal to the column space of \(A\), and put \(Q=\|Z^\mathsf TR\|_2^2\). If \(R\ne0\), then
\[
\Pr(\Delta_G>t)\sim
\frac{\mathbb E Q^{\ell/2}}{2^{\ell/2}\Gamma(\ell/2+1)}\,t^{-\ell/2},
\qquad
\Pr(\Delta_H>t)\sim
\mathbb E\mathcal B^{\ell/2}
\frac{\mathbb E Q^{\ell/2}}{2^{\ell/2}\Gamma(\ell/2+1)}\,t^{-\ell/2}.
\]
The tail attenuation is strictly between zero and one, even when the mean squared error is infinite.

## Assumptions and scope

All matrices and sketches are **real**; arithmetic is exact. The data \(A,B\) are fixed independently of the sketch. The design has rank **exactly one**; its number of columns \(d\) is arbitrary, including rank-deficient designs. Every right-hand side and every number of right-hand sides \(p\ge1\) are allowed. The sketch is used in the standard unregularized minimum-norm sketch-and-solve estimator. The range \(2\le\ell<n\) ensures both beta parameters are strictly positive. The nontrivial strict-order and tail statements require \(R\ne0\). The endpoints \(\ell=1\) and \(\ell=n\) are excluded from the beta-density formula: at \(\ell=1\) the two error laws coincide, while at \(\ell=n\) Haar sketch-and-solve is exact.

## Proof

**Step 1: rank-one reduction.** Write a singular-value decomposition \(A=\sigma uv^\mathsf T\), where \(\sigma>0\), \(\|u\|_2=\|v\|_2=1\). Since \(u^\mathsf TR=0\), elementary pseudoinverse algebra, valid almost surely for both sketch models, gives
\[
\widehat X_\Omega-X_*=\sigma^{-1}v e_\Omega,
\quad e_\Omega=\frac{u^\mathsf T\Omega\Omega^\mathsf TR}{u^\mathsf T\Omega\Omega^\mathsf Tu}.
\]
Here \(e_\Omega\) is a \(1\times p\) row. As \(A(\widehat X_\Omega-X_*)=u e_\Omega\) and \(u^\mathsf TR=0\), the excess squared residual is exactly \(\Delta_\Omega=\|e_\Omega\|_2^2\). It suffices to compare entire distributions of these rows.

**Step 2: Gaussian sketch.** Orthogonal invariance permits taking \(u\) as the first coordinate vector. The first row of \(\Omega_G\) is an independent \(\ell\)-vector \(g\) with \(\|g\|_2^2=:X\sim\chi^2_\ell\). The remaining rows are independent standard Gaussian vectors. Conditioning on \(g\), taking the Gaussian linear combination along \(g/\|g\|_2\), and removing that conditioning yield
\[
e_G\overset d=\frac{Z^\mathsf TR}{\sqrt X},
\]
where \(Z\) is a standard Gaussian vector in \(u^\perp\), independent of \(X\). This holds jointly for all \(p\) outputs, not just separately for their coordinates.

**Step 3: Haar geometry.** Put \(P=\Omega_H\Omega_H^\mathsf T\) and \(T=u^\mathsf TPu\). Haar symmetry gives
\[
T\sim\operatorname{Beta}\left(\frac\ell2,\frac{n-\ell}2\right).
\]
The projector identity \(\|Pu\|_2^2=u^\mathsf TPu=T\) implies that the component of \(Pu\) orthogonal to \(u\) has squared norm \(T(1-T)\). Conditional rotational invariance about \(u\) shows that its direction \(S\) is uniform on the unit sphere of \(u^\perp\) and is independent of \(T\). Therefore
\[
e_H\overset d=\sqrt{\frac{1-T}{T}}\,S^\mathsf TR
=\frac{\sqrt Y}{\sqrt X}\,S^\mathsf TR,
\]
where \(X\sim\chi^2_\ell\), \(Y\sim\chi^2_{n-\ell}\), and \(S\) are mutually independent. The ratio representation follows from the standard chi-square representation of a beta variable.

**Step 4: independent beta–gamma factorization.** Independently draw \(\mathcal B\sim\operatorname{Beta}((n-\ell)/2,(\ell-1)/2)\) and a standard normal \(Z\in u^\perp\). The norm \(\|Z\|_2^2\) has the \(\chi^2_{n-1}\) law. The beta–gamma identity gives
\[
\mathcal B\|Z\|_2^2\sim\chi^2_{n-\ell}.
\]
For completeness, this identity follows by taking independent gamma variables \(G_1,G_2\) with common scale two and shape parameters \((n-\ell)/2\) and \((\ell-1)/2\): the ratio \(G_1/(G_1+G_2)\) is beta, independent of their sum, and their product is \(G_1\). Both vectors \(\sqrt{\mathcal B}Z\) and \(\sqrt YS\) are rotationally invariant in \(u^\perp\), with identical nonnegative radial distributions; hence their entire vector laws agree. Since \(X\) is independent, multiplication by \(R\) and comparison with Step 2 give
\[
e_H\overset d=\sqrt{\mathcal B}\,e_G.
\]
This proves the matrix coupling and its excess-error consequence.

**Step 5: stochastic order and moments.** Since \(0<\mathcal B<1\) almost surely, \(\mathcal B\Delta_G\le\Delta_G\) under the coupling. If \(R\ne0\), the variable \(\Delta_G=Q/X\) has a continuous, strictly positive density on \((0,\infty)\), and the beta density is positive on \((0,1)\), yielding strict tail inequality at every positive threshold. Independence gives the displayed moment ratio, evaluated by the beta integral. Because \(Q\) is a nonzero Gaussian quadratic form with positive finite moments of all orders, while \(\mathbb E X^{-s}\) is finite exactly for \(s<\ell/2\), this condition is the exact common moment cutoff.

**Step 6: sharp tails.** With \(X\sim\chi^2_\ell\), its distribution function satisfies \(\Pr(X\le y)\sim y^{\ell/2}/(2^{\ell/2}\Gamma(\ell/2+1))\) as \(y\downarrow0\), and this asymptotic is dominated globally by the same right-hand side with \(\sim\) replaced by \(\le\). Conditioning on \(Q\) therefore gives the Gaussian asymptotic by dominated convergence, since \(\mathbb E Q^{\ell/2}<\infty\). Conditioning also on the independent bounded \(\mathcal B\) gives the Haar coefficient multiplied by \(\mathbb E\mathcal B^{\ell/2}\). Both are strictly positive if \(R\ne0\).

## Verification

The accompanying `verify.py` implements the two algorithms independently (Gaussian sketches and QR-generated Haar orthonormal frames), compares the empirical Haar error to the derived independent beta–Gaussian mixture, checks exact gamma/beta moment identities, numerically evaluates scalar beta-prime mixtures, and checks the sharp large-threshold coefficient. With its fixed seed it passes 845 assertions, including 26,000 full independent direct-sketch trials per model. The script requires NumPy and SciPy and can be run as `python verify.py`.

For the exact benchmark \(n=10\), \(\ell=4\), and \(\|R\|_F=1\) with rank-one residual, one finds
\[
\mathbb E\Delta_G=\tfrac12,\qquad
\mathbb E\Delta_H=\tfrac13,\qquad
\Pr(\Delta_G>t)\sim\frac{3}{8t^2},\qquad
\Pr(\Delta_H>t)\sim\frac{2}{11t^2}.
\]
The catastrophic-tail coefficient ratio is \(16/33\), whereas the mean ratio is \(2/3\). Numerical work is a cross-check; the theorem for all stated dimensions and residual matrices is proved analytically.

## Relationship to prior work

Epperly and Webber (arXiv:2605.19096, Theorem 2.1 and Proposition 5.7) prove exact **expected** least-squares residual formulas and optimality of the Haar orthonormal embedding for worst-case mean-square error. Their analysis uses Wishart and matrix-beta moments. Neither the entire independent beta-scaling distribution nor stochastic dominance at every threshold nor the sharp tail-coefficient ratio follows from their expectation statements alone; those are the contributions here. For rank-one designs, our first-moment formula reproduces their factor, so that known factor is not claimed as novel.

Bartan and Pilanci (arXiv:2002.06538) establish Gaussian-sketch mean-error identities in a distributed setting. Sridhar, Pilanci, and Özgür (arXiv:2006.08160) derive conditional Gaussian laws and estimation lower bounds for Gaussian sketches. These correctly explain part of Step 2 but do not compare Haar and Gaussian rank-one error distributions by an independent beta factor. Asymptotic sketched-pseudoinverse and sketch-inference results address different regimes. Standard beta–gamma algebra and Student-ratio laws are classical and are used, not claimed, as original tools.

## Limitations

The stochastic dominance statement is proved only for rank-one real designs, not for arbitrary rank or arbitrary structured sketches. The coupling is distributional and does not compare two independently generated numerical runs samplewise. The results concern an unregularized sketch-and-solve estimator in exact arithmetic and provide no runtime benefit or end-to-end solver guarantee. The inequality for errors is strict only when the optimal residual matrix is nonzero. Historical priority for a pre-existing equivalent finite-sample distributional comparison in specialized matrix-variate probability remains a residual risk.

## References

1. E. N. Epperly and R. J. Webber, *Sharp analysis of sketched least squares and randomized low-rank approximation*, arXiv:2605.19096v1 (first public version 2026-05-18), Sections 2 and 5, particularly Theorem 2.1 and Proposition 5.7. https://arxiv.org/abs/2605.19096
2. B. Bartan and M. Pilanci, *Distributed Sketching Methods for Privacy Preserving Regression*, arXiv:2002.06538, Section 3. https://arxiv.org/abs/2002.06538
3. S. Sridhar, M. Pilanci, and A. Özgür, *Lower Bounds and a Near-Optimal Shrinkage Estimator for Least Squares using Random Projections*, arXiv:2006.08160, Section 2.1. https://arxiv.org/abs/2006.08160
4. L. Wang, Z. Zhang, and E. Dobriban, *Inference in Randomized Least Squares and PCA via Normality of Quadratic Forms*, arXiv:2404.00912 (2024), for asymptotic sketch-inference context. https://arxiv.org/abs/2404.00912
