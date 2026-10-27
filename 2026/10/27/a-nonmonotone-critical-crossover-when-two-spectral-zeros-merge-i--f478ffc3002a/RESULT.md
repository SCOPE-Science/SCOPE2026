# A nonmonotone critical crossover when two spectral zeros merge in a Gaussian power series

## Finding
Let \((G_j)_{j\in\mathbb Z}\) be independent standard circular complex Gaussian variables and put
\[
c=\cos\varepsilon,\quad
\xi_j^{(\varepsilon)}=\frac{G_j-2cG_{j-1}+G_{j-2}}{\sqrt{2+4c^2}},\quad
X_\varepsilon(z)=\sum_{j=0}^\infty \xi_j^{(\varepsilon)}z^j.
\]
For \(0\le\varepsilon<\pi/2\), this is an analytic Gaussian random power series whose stationary coefficient spectral density is proportional to \((\cos t-\cos\varepsilon)^2\). For \(\varepsilon>0\), the spectral density has two distinct double zeros at \(\pm\varepsilon\); at \(\varepsilon=0\), these merge into one quartic zero.

Write \(N_\varepsilon(r)\) for the number of zeros of \(X_\varepsilon\) in \(|z|<r\), counted with multiplicity, and \(D_\varepsilon(r)=r^2/(1-r^2)-\mathbb E N_\varepsilon(r)\). The exact identity
\[
D_\varepsilon(r)=-1+\operatorname{Re}
\frac{c+i/(2\delta)}{\sqrt{(c+i\delta)^2-r^2}},
\qquad \delta=\sqrt{(1-r^2)/2},
\]
holds for \(0<r<1\), where the square root is taken with positive real part.

**Sharp crossover theorem.** For each finite \(L\ge0\), uniformly over \(\lambda\in[0,L]\), as \(h\downarrow0\),
\[
\boxed{D_{\lambda h^{1/4}}(1-h)
 = h^{-3/4} F(\lambda)+O_L(h^{-1/4}),\qquad
F(\lambda)=\frac12\operatorname{Re}(\lambda^2+2i)^{-1/2}.}
\]
The profile is positive for all \(\lambda\ge0\), increases strictly until the unique maximum at
\[
\boxed{\lambda_*=\sqrt{2/\sqrt3},\qquad
F(\lambda_*)=\frac{3^{3/4}}8,}
\]
and strictly decreases afterward. In particular \(F(0)=1/4\), and \(F(\lambda)\sim1/(2\lambda)\) as \(\lambda\to\infty\). The strongest deficit in the singular crossover occurs at **nonzero** spectral-zero separation, not at the quartic collision.

## Assumptions and scope
The coefficients are a single *stationary proper complex Gaussian* process of moving-average order two, with the displayed independent underlying Gaussian sequence. The summation defining \(X_\varepsilon\) is almost surely analytic in \(|z|<1\). Each model parameter is constant within each random power series. Only in the asymptotic theorem does the model parameter \(\varepsilon\) depend on \(h=1-r\). The expected zero count is over the open disk; almost surely no zero lies on any fixed circle. Uniformity is on each bounded interval of nonnegative \(\lambda\). No assertion of uniformity as \(\lambda\to\infty\) is made.

## Proof
**1. Coefficient covariance and diagonal kernel.** The normalization makes \(\mathbb E|\xi_j|^2=1\). Direct multiplication gives lag-one and lag-two covariances \(\gamma_1=-4c/(2+4c^2)\) and \(\gamma_2=1/(2+4c^2)\), with all higher-lag covariances zero. For \(z=re^{it}\), the variance kernel is
\[
K_\varepsilon(z,z)=\frac{1}{1-r^2}
\frac{4(r\cos t-c)^2+2(1-r^2)}{2+4c^2}.
\]
This quantity is strictly positive for every \(r<1\). Hence the expected zero-count identity for nondegenerate Gaussian analytic functions (the Poincaré–Lelong/Edelman–Kostlan formula) yields
\[
\mathbb E N_\varepsilon(r)
 =\frac r2\frac{d}{dr}\left(\frac1{2\pi}
\int_0^{2\pi}\log K_\varepsilon(re^{it},re^{it})\,dt\right).
\]

**2. An exact Jensen evaluation.** Set \(\delta=\sqrt{(1-r^2)/2}\), \(v=c+i\delta\), and \(W=\sqrt{v^2-r^2}\) with \(\operatorname{Re}W>0\). The nontrivial angular factor is \(4|v-r\cos t|^2\). The classical cosine Jensen integral, valid since \(\operatorname{Im}v>0\), gives
\[
\frac1{2\pi}\int_0^{2\pi}
\log\bigl(4|v-r\cos t|^2\bigr)\,dt
 = 2\operatorname{Re}\log(v+W).
\]
As \(v'=-ir/(2\delta)\), differentiation using \(W^2=v^2-r^2\) yields the elementary identity
\[
\frac{d}{dr}\log(v+W)
 =\frac1r+\frac{v'-v/r}{W}.
\]
Therefore
\[
\mathbb E N_\varepsilon(r)
 =\frac{r^2}{1-r^2}+1+\operatorname{Re}\frac{rv'-v}{W}
 =\frac{r^2}{1-r^2}+1-
\operatorname{Re}\frac{c+i/(2\delta)}{W}.
\]
This proves the exact identity. The branch is unambiguous because \(v^2-r^2\) has strictly positive imaginary part \(2c\delta\) for \(c>0\).

**3. Uniform merger scaling.** Fix \(L<\infty\), put \(r=1-h\) and \(\varepsilon=\lambda h^{1/4}\), where \(0\le\lambda\le L\). Uniform Taylor estimates give
\[
\delta=h^{1/2}(1+O(h)),\quad
c=1-\tfrac12\lambda^2h^{1/2}+O_L(h),
\]
\[
(c+i\delta)^2-r^2
 =h^{1/2}(-\lambda^2+2i+O_L(h^{1/2})),
\qquad
c+\frac{i}{2\delta}
 =\frac{i}{2h^{1/2}}(1+O_L(h^{1/2})).
\]
The compact set \(\{-\lambda^2+2i:0\le\lambda\le L\}\) lies away from the square-root cut and zero. Thus inversion and square rooting preserve uniform \(O_L(h^{1/2})\) relative errors, and
\[
D_{\lambda h^{1/4}}(1-h)
 =\frac{h^{-3/4}}2\operatorname{Re}
\frac{i}{\sqrt{-\lambda^2+2i}}+O_L(h^{-1/4}).
\]
The principal-square-root identity \(i/\sqrt{-q+2i}=1/\sqrt{q+2i}\) for \(q\ge0\) gives precisely \(F(\lambda)\). This estimates the error **uniformly** in the stated range; the additive constant \(-1\) in the exact deficit is absorbed in \(O_L(h^{-1/4})\).

**4. Positivity, unique maximum and matching limits.** Put \(q=\lambda^2\) and \(\theta=\arg(q+2i)\in(0,\pi/2]\). Then \(F>0\) and
\[
\frac{d}{dq}\,\frac12\operatorname{Re}(q+2i)^{-1/2}
 =-\frac14|q+2i|^{-3/2}\cos(3\theta/2).
\]
Since \(\theta\) decreases strictly from \(\pi/2\) to zero as \(q\) increases, the derivative changes sign only where \(\theta=\pi/3\), namely \(q=2/\sqrt3\). Direct substitution gives \(F(\lambda_*)=3^{3/4}/8\), strictly greater than \(F(0)=1/4\), and a large-\(\lambda\) expansion gives \(F(\lambda)\sim1/(2\lambda)\). This last asymptotic matches the small-separation growth of the fixed-separated-double-zero coefficient of Noda–Shirai after taking the appropriate successive limits, but the two fixed regimes do not provide the uniform interpolation or its unique optimum.

## Verification
Run `python3 check_crossover.py` from a directory containing the accompanying standalone script. It uses only the Python standard library and checks the exact count against independently evaluated angular integrals, the scaled finite-radius deficits against the limiting profile, and the calculated location and height of the unique maximum. The checks are finite numerical corroboration; the preceding steps provide the infinite-domain proof.

## Relationship to prior work
Noda and Shirai, *Expected Number of Zeros of Random Power Series with Finitely Dependent Gaussian Coefficients* (first public preprint 5 June 2021), study the same two-dependent covariance family and obtain fixed-parameter boundary asymptotics, including the quartic collision \((a,b)=(-2/3,1/6)\) as well as separated double-zero cases. Their Section 3 also contains exact finite-parameter contour representations that are inputs from which further asymptotics can be derived. The exact finite-radius identity here is a convenient specialization/rewriting of such general machinery and is **not** asserted to be historically new. The specific result claimed here is the uniform coupled \(\varepsilon\asymp(1-r)^{1/4}\) crossover, its complete explicit profile, and the uniquely nonzero maximizing separation. Fixed-parameter asymptotics alone are not uniform as the two spectral zeros coalesce. The later article by Shirai, *The density of zeros of random power series with stationary complex Gaussian coefficients* (2025), studies asymptotic radial densities and provides additional related context, but an equivalent coupled parameter-merger profile has not been identified from the material checked.

## Limitations
This is a precisely specified moving-average family, not a universality theorem for all nonnegative spectral densities with two coalescing double zeros. The result concerns expectations rather than almost-sure zero counts, random fluctuations, or correlations. It makes no claim at large \(\lambda\) jointly with \(h\) beyond bounded \(\lambda\) intervals. The earliest-source and priority assessment is based on inspected relevant accessible literature; an equivalent result under another parameterization remains a possible historical risk. The cited fixed-parameter exact formulas mean that the novelty claim is solely the joint-scaling analysis and sharp profile optimization, not the general covariance-to-zero-count method.

## References
1. K. Noda and T. Shirai, *Expected Number of Zeros of Random Power Series with Finitely Dependent Gaussian Coefficients*, arXiv:2106.02860v1 (5 June 2021), later *Journal of Theoretical Probability* 36 (2023), 1534–1554; https://arxiv.org/abs/2106.02860 ; DOI 10.1007/s10959-022-01203-y.
2. T. Shirai, *The density of zeros of random power series with stationary complex Gaussian coefficients*, arXiv:2501.02586v1 (2025); https://arxiv.org/abs/2501.02586.
3. A. Edelman and E. Kostlan, *How many zeros of a random polynomial are real?*, *Bulletin of the American Mathematical Society* 32 (1995), 1–37 (expected zeros identity, complex analogue).
