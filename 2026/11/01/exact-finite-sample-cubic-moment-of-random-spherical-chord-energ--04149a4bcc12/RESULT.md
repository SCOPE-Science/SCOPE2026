# Exact finite-sample cubic moment of random spherical chord energy

## Finding

Let \(X_1,\ldots,X_n\), \(n\ge2\), be independent uniform points on the Euclidean unit sphere \(S^2\), and put
\[
E_n=\sum_{1\le i<j\le n}\|X_i-X_j\|.
\]
With \(\mu_n=\mathbb E E_n\), the **exact finite-sample formulas** are
\[
\mu_n=\frac43\binom n2,\qquad
\operatorname{Var}(E_n)=\frac29\binom n2,
\]
\[
\mathbb E[(E_n-\mu_n)^3]
=-\frac8{135}\binom n2
+6\left(\frac{15\pi^2}{64}-\frac{64}{27}\right)\binom n3.
\]
The negative, explicitly evaluated triangle interaction is
\[
\mathbb E\left[\prod_{\{i,j\}\in\{\{1,2\},\{2,3\},\{1,3\}\}}
\left(\|X_i-X_j\|-\frac43\right)\right]
=\frac{15\pi^2}{64}-\frac{64}{27}<0.
\]
For context, Bakshaev (2010, Theorem 4) **already established** the following equivalent chi-square limit (with weights given as Legendre integrals). Evaluating those integrals gives, as \(n\to\infty\),
\[
\frac{E_n-\mu_n}{n}\ \Longrightarrow\
W=\frac23-\sum_{\ell=1}^\infty
\frac{2}{(2\ell-1)(2\ell+1)(2\ell+3)}\,Q_\ell,
\]
where the \(Q_\ell\) are independent \(\chi^2\) random variables with \(2\ell+1\) degrees of freedom. The displayed series is absolutely convergent almost surely and in \(L^1\), and its centered version converges in \(L^2\). The limiting law is **not claimed to be a new limiting distribution**. Its **explicitly evaluated** cubic central moment equals \(15\pi^2/64-64/27\), standardized skewness
\[
\frac{405\pi^2}{64}-64\approx-1.5439096493564,
\]
and essential supremum \(2/3\). Thus it is not Gaussian. The limit is supported on \(( -\infty,2/3]\), with unbounded lower support.

## Assumptions and scope

The ambient dimension is exactly three, with the unit \(2\)-sphere and normalized rotation-invariant surface measure. Distances are **Euclidean chords**, not geodesic distances. The statistic sums unordered pairs once. For the limit, the ambient dimension remains fixed while the sample count tends to infinity. No claim is made about nonuniform or interacting point processes.

## Proof

**1. Pair moments and graph independence.** The dot product of two independent uniform points of \(S^2\) is uniform on \([-1,1]\); hence one chord \(R\) has density \(r/2\) for \(0<r<2\). Therefore
\[
\mathbb E R=\frac43,\qquad \mathbb E R^2=2,\qquad
\mathbb E R^3=\frac{16}{5},
\]
so its variance is \(2/9\) and third central moment is \(-8/135\). On any finite forest, the edge chords are jointly independent: remove a leaf, condition on its neighbor, and note that the conditional chord-length distribution is independent of the neighbor's position. In particular, distinct edge chords are pairwise independent. In the expansion of the cube of the sum of centered chords, a product of three distinct chords has zero expectation unless its edges form a triangle. Terms with one repeated edge and another distinct edge also vanish by conditional constancy. Consequently,
\[
\operatorname{Var}(E_n)=\binom n2\frac29,\quad
\mathbb E[(E_n-\mu_n)^3]=\binom n2\left(-\frac8{135}\right)
+6\binom n3\,\tau,
\]
where \(\tau\) is the centered three-chord product for one triangle.

**2. Evaluate the triangle term without simulation.** Let \(\sigma\) be normalized surface measure and \(K(x,y)=\|x-y\|-4/3\). The integral operator \(Tf(x)=\int K(x,y)f(y)\,d\sigma(y)\) acts diagonally on spherical harmonics. Choose a real orthonormal basis \(Y_{\ell m}\) for \(L^2(S^2,\sigma)\), with \(m=1,\ldots,2\ell+1\). The Funk--Hecke formula and a beta integral give for every \(\ell\ge1\)
\[
\lambda_\ell=\frac12\int_{-1}^1\sqrt{2-2t}\,P_\ell(t)\,dt
=-\frac4{(2\ell-1)(2\ell+1)(2\ell+3)}.
\]
More explicitly, Rodrigues' formula followed by \(\ell\) integrations by parts gives
\[
\lambda_\ell=\frac{2(-1)^\ell}{\ell!}\left(\frac12\right)_{\!\underline{\ell}}\,B\left(\frac32,\ell+1\right),
\]
where \(\left(\frac12\right)_{\!\underline{\ell}}\) denotes the **falling** factorial and \(B\) is Euler's beta integral. Boundary terms vanish since the Rodrigues polynomial has order-\(\ell\) zeros at both endpoints; the endpoint singularity remaining after differentiation is integrable when multiplied by that polynomial. This evaluates to the displayed rational eigenvalues. For \(\ell=0\) the raw chord-kernel eigenvalue is \(4/3\), which is removed by centering. To verify the beta step directly, substitute \(u=(1-t)/2\), expand \(P_\ell(1-2u)\) as a polynomial, and integrate each monomial using \(2\int_0^1u^{j+1/2}du=4/(2j+3)\). This also gives a finite symbolic certificate at each degree. The coefficients decay cubically, so the addition-theorem expansion of \(K\) is absolutely and uniformly convergent and trace products may be interchanged with integration.

Cyclic integration gives
\[
\tau=\iiint K(x,y)K(y,z)K(z,x)\,d\sigma(x)d\sigma(y)d\sigma(z)
=\sum_{\ell\ge1}(2\ell+1)\lambda_\ell^3.
\]
Its summand admits the exact partial fractions
\[
\begin{aligned}
\frac{-64}{(2\ell-1)^3(2\ell+1)^2(2\ell+3)^3}
={}&\frac{15}{32}\left(\frac1{2\ell+3}-\frac1{2\ell-1}\right)\\
&+\frac7{16}\left(\frac1{(2\ell+3)^2}+\frac1{(2\ell-1)^2}\right)
+\frac1{(2\ell+1)^2}\\
&+\frac14\left(\frac1{(2\ell+3)^3}-\frac1{(2\ell-1)^3}\right).
\end{aligned}
\]
The linear and cubic reciprocal terms telescope; the squared odd reciprocals sum via \(\sum_{k\ge0}(2k+1)^{-2}=\pi^2/8\). The result is \(\tau=15\pi^2/64-64/27\). Substitution completes all exact finite-sample formulas.

**3. Known non-Gaussian limit, rederived for normalization and moment comparison.** The addition theorem gives the uniformly convergent identity
\[
K(x,y)=\sum_{\ell\ge1}\lambda_\ell
\sum_{m=1}^{2\ell+1}Y_{\ell m}(x)Y_{\ell m}(y).
\]
Set \(a_\ell=-\lambda_\ell/2>0\) and
\(Z_{n,\ell m}=n^{-1/2}\sum_{i=1}^nY_{\ell m}(X_i)\). Because \(K(x,x)=-4/3\) and every empirical pair is counted twice, the **exact finite-sample identity** is
\[
\frac{E_n-\mu_n}{n}=
\frac23-\sum_{\ell\ge1}a_\ell\sum_{m=1}^{2\ell+1}Z_{n,\ell m}^2.
\]
For each finite degree cutoff, orthogonality and the ordinary multivariate central limit theorem yield independent standard Gaussian limits for the corresponding \(Z_{n,\ell m}\). Uniformly in \(n\), the expected omitted positive tail equals \(\sum_{\ell>L}(2\ell+1)a_\ell\to0\), allowing passage to the infinite series in distribution. It also proves convergence in expectation of the positive series and almost-sure summability in the limit.

The limit is centered because \(\sum_{\ell\ge1}(2\ell+1)a_\ell=2/3\), equivalently to the diagonal identity \(K(x,x)=-4/3\). Chi-square cumulants give
\[
\operatorname{Var}(W)=2\sum_{\ell\ge1}(2\ell+1)a_\ell^2=\frac19,
\quad
\mathbb E[W^3]=-8\sum_{\ell\ge1}(2\ell+1)a_\ell^3=\tau.
\]
The variance identity also follows from the exact finite-sample variance and \(L^2\) convergence of the chaos expansion. Since each coefficient is positive, \(W\le2/3\). The bound is its essential supremum: finitely many independent chi-squares can simultaneously be arbitrarily close to zero with positive probability, while the nonnegative tail can be made small with positive conditional probability. An individual chi-square can grow arbitrarily large, giving unbounded negative support. This rules out a normal law independently of the nonzero skewness.

## Verification

Execute `python verify.py` with Python, NumPy, and SymPy. The program independently integrates the first eleven Funk--Hecke coefficients as exact rational polynomial integrals, checks the rational partial-fraction identity, checks the resulting cubic constant against a rapidly convergent trace sum, and performs a separate simulation of 500,000 genuinely uniform spherical point triples. It also checks single-edge moments and pairwise covariance. Exact finite checks alone are not an infinite proof; the full harmonic and probability arguments above supply that proof.

## Relationship to prior work

Stolarsky's invariance principle relates Euclidean chord energy to squared spherical-cap discrepancy. **Bakshaev (2010, Theorem 4) proves the weighted chi-square null law for this same chord statistic and lists its first harmonic coefficients; no originality is claimed for that law.** Brauchart--Dick (2011) prove the deterministic identity using reproducing kernels. Bilyk--Dai--Matzke (2016) give a different proof and extensions to other discrepancies and energies. Borda--Grabner--Matzke (2023/2024) derive expected energies and discrepancies for repulsive determinantal ensembles, explicitly contrasting the iid first moment. The inspected primary texts do **not state the exact finite-sample cubic moment or its evaluated \(\pi^2\) triangle coefficient**. The chi-square law itself is already in Bakshaev (2010); the exact all-sample-size cubic moment and closed-form skewness evaluation are the focus. General degenerate \(U\)-statistic and spherical-harmonic frameworks, including the spectral null law for this exact statistic, are prior mathematics. The claimed contribution is the closed all-\(n\) third central moment with a nontrivial evaluated triangle term, plus its exact asymptotic skewness corollary. Historical priority remains provisional.

## Limitations

The result depends on iid rotation-invariant samples, the unit sphere in \(\mathbb R^3\), and chord rather than geodesic distance. The full chi-square null law (not just its abstract form) was previously established by Bakshaev (2010); the novel claim is confined to the finite cubic formula and the explicit evaluation of its associated skewness constant. This does not establish a Berry--Esseen rate or finite-sample density. Search coverage cannot prove novelty, and an independent mathematical audit has not been performed.

## References

1. A. Bakshaev, *N-distance tests of uniformity on the hypersphere*, Nonlinear Analysis: Modelling and Control 15 (2010), 15–28, Theorem 4, https://www.journals.vu.lt/nonlinear-analysis/article/download/14361/13277/21533.

2. J. S. Brauchart and J. Dick, *A simple Proof of Stolarsky's Invariance Principle*, first publicly posted 2011-01-24, arXiv:1101.4448, https://arxiv.org/html/1101.4448v1.
3. D. Bilyk, F. Dai and R. Matzke, *Stolarsky principle and energy optimization on the sphere*, first publicly posted 2016-11-14, arXiv:1611.04420, https://arxiv.org/abs/1611.04420.
4. B. Borda, P. Grabner and R. W. Matzke, *Riesz Energy, L² Discrepancy, and Optimal Transport of Determinantal Point Processes on the Sphere and the Flat Torus*, first publicly posted 2023-08-11, arXiv:2308.06216, https://arxiv.org/html/2308.06216v2.
5. K. B. Stolarsky, *Sums of distances between points on a sphere. II*, Proc. Amer. Math. Soc. 41 (1973), 575–582.
