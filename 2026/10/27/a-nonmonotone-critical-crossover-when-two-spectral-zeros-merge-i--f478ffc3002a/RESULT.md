# A nonmonotone critical crossover when two spectral zeros merge in a Gaussian power series

## Finding

Let \((G_j)_{j\in\mathbb Z}\) be independent standard circular complex Gaussians, with \(\mathbb E|G_j|^2=1\). For \(0\le\varepsilon<\pi/2\), put \(c=\cos\varepsilon\) and define
\[
\xi_j^{(\varepsilon)}=\frac{G_j-2cG_{j-1}+G_{j-2}}{\sqrt{2+4c^2}},\qquad X_\varepsilon(z)=\sum_{j=0}^\infty \xi_j^{(\varepsilon)}z^j.
\]
The coefficient spectral density is proportional to \((\cos t-c)^2\), with two double zeros at \(\pm\varepsilon\) when \(\varepsilon>0\) and one quartic zero at \(0\) when \(\varepsilon=0\). Let \(N_\varepsilon(r)\) count the zeros in \(|z|<r\), with multiplicity, and write \(D_\varepsilon(r)=r^2/(1-r^2)-\mathbb E N_\varepsilon(r)\). For \(0<r<1\),
\[
D_\varepsilon(r)=-1+\operatorname{Re}\frac{c+i/(2\delta)}{\sqrt{(c+i\delta)^2-r^2}},\qquad \delta=\sqrt{(1-r^2)/2},
\]
where the square root has positive real part.

For every finite \(L\ge0\), uniformly in \(0\le\lambda\le L\) as \(h\downarrow0\),
\[
D_{\lambda h^{1/4}}(1-h)=h^{-3/4}F(\lambda)+O_L(h^{-1/4}),\qquad F(\lambda)=\tfrac12\operatorname{Re}(\lambda^2+2i)^{-1/2}.
\]
The profile is positive. It increases strictly up to its unique maximizer \(\lambda_*=\sqrt{2/\sqrt3}\), with \(F(\lambda_*)=3^{3/4}/8\), and decreases strictly thereafter. In particular \(F(0)=1/4\) and \(F(\lambda)\sim1/(2\lambda)\) as \(\lambda\to\infty\). The limiting crossover profile therefore has a stronger deficit at a nonzero scaled separation than at exact collision.

## Assumptions and scope

The coefficients form one stationary proper complex Gaussian process of moving-average order two. The series is almost surely analytic in the open unit disk: for each fixed \(r<1\), \(\sum_j\mathbb E|\xi_j^{(\varepsilon)}|r^j<\infty\), and one can exhaust the disk with countably many such radii. The parameter is held fixed in each series and in radial derivatives; only for the asymptotic theorem is it chosen as a function of \(h\). The estimate is uniform on bounded \(\lambda\)-intervals, not for diverging \(\lambda\) jointly with \(h\).

## Proof

**Covariance and radial zero count.** The nonzero lag covariances are \(\gamma_0=1\), \(\gamma_1=-4c/(2+4c^2)\), and \(\gamma_2=1/(2+4c^2)\), with \(\gamma_{-j}=\gamma_j\). The filter \(1-2ce^{-it}+e^{-2it}=2e^{-it}(\cos t-c)\) gives the asserted spectral density. Summing the lag contributions on the disk gives
\[
K_\varepsilon(re^{it},re^{it})=\frac{4(r\cos t-c)^2+2(1-r^2)}{(1-r^2)(2+4c^2)}.
\]
This is strictly positive. For this proper Gaussian analytic function, the expected zero measure has density \((4\pi)^{-1}\Delta\log K_\varepsilon(z,z)\), by Poincaré–Lelong and the expectation of the logarithm of a complex Gaussian's modulus. In particular every fixed circle has zero expected mass. Integration and Green's formula give
\[
\mathbb E N_\varepsilon(r)=\frac r2\frac{d}{dr}\frac{1}{2\pi}\int_0^{2\pi}\log K_\varepsilon(re^{it},re^{it})\,dt.
\]

**Exact angular integral.** Let \(v=c+i\delta\) and \(W=\sqrt{v^2-r^2}\) on the indicated branch. The radicand has positive imaginary part \(2c\delta\), so \(v\) and \(W\) both have positive real and imaginary parts. The identities \((v+W)(v-W)=r^2\) and \(|v+W|^2-|v-W|^2=4\operatorname{Re}(v\overline W)>0\) imply \(|r/(v+W)|<1\). With \(s=r/(v+W)\), factor
\[
v-r\cos t=\frac{v+W}{2}(1-se^{it})(1-se^{-it}).
\]
Each log-modulus term involving \(s\) has zero angular mean, by its convergent power series. The angular mean of \(\log(4|v-r\cos t|^2)\) is therefore \(2\log|v+W|\). Differentiation using \(W^2=v^2-r^2\) gives
\[
\frac{v'+W'}{v+W}=\frac1r+\frac{v'-v/r}{W},\qquad rv'-v=-c-i/(2\delta).
\]
Together with the derivative of \(-\log(1-r^2)\), these formulas give the stated exact deficit.

**Uniform expansion.** For \(r=1-h\) and \(\varepsilon=\lambda h^{1/4}\), Taylor estimates uniform on \([0,L]\) give
\[
\delta=h^{1/2}(1+O(h)),\quad c=1-\tfrac12\lambda^2 h^{1/2}+O_L(h),
\]
\[
v^2-r^2=h^{1/2}(-\lambda^2+2i+O_L(h^{1/2})),\qquad c+i/(2\delta)=\frac{i}{2h^{1/2}}(1+O_L(h^{1/2})).
\]
The limiting radicands form a compact subset of the upper half-plane, so taking their inverse square roots preserves the uniform additive \(O_L(h^{1/2})\) error after factoring out \(h^{1/2}\). This yields \(\tfrac12 h^{-3/4}\operatorname{Re}(i/\sqrt{-\lambda^2+2i})+O_L(h^{-1/4})\) for the deficit. On the principal branch, for \(q\ge0\),
\[
\sqrt{-q+2i}=i\,\overline{\sqrt{q+2i}},\qquad \frac{i}{\sqrt{-q+2i}}=\overline{(q+2i)^{-1/2}}.
\]
The real parts agree, which gives \(F\) and the uniform theorem. The additive constant \(-1\) is absorbed by the stated error.

**Optimization and limits.** Put \(q=\lambda^2\) and \(\theta=\arg(q+2i)\in(0,\pi/2]\). The real part of the inverse square root is positive. Differentiating with respect to \(q\) gives
\[
\frac{d}{dq}\frac12\operatorname{Re}(q+2i)^{-1/2}=-\frac14|q+2i|^{-3/2}\cos(3\theta/2).
\]
As \(q\) increases, \(\theta\) decreases strictly. The derivative is positive until \(\theta=\pi/3\), or \(q=2/\sqrt3\), and negative afterward. At the maximizer \(|q+2i|=4/\sqrt3\); substitution gives the asserted height. At \(q=0\) the inverse square root is \((1-i)/2\), giving \(F(0)=1/4\). As \(q\to\infty\) it is asymptotic to \(q^{-1/2}\), giving the stated tail.

## Verification

The accompanying `check_crossover.py` can be run with the Python 3 standard library. It compares the exact deficit with a radial angular-integral calculation and checks finite-radius convergence toward the profile and its optimum. These numerical checks are diagnostic; uniformity, the branch identity, and the uniqueness of the maximum follow from the analytical proof above.

## Relationship to prior work and limitations

Noda and Shirai [1] treat the same two-dependent covariance family and supply exact integral methods as well as the fixed-parameter asymptotics for both separated double zeros and the quartic collision. The exact finite-radius calculation here is a convenient specialization, not an originality claim. The coupled scale balances the vanishing separation in the radicand with the radial regularization; neither of the two fixed-parameter asymptotics is uniform through that balance. The assertion is the explicit uniform merger profile and its optimization. The limiting values agree with the fixed quartic coefficient and the small-separation limit of the separated coefficient, with the limits taken successively. Shirai [2] studies related fixed-spectral-measure radial density asymptotics. The theorem concerns the expected count for the specified moving-average model, not universality, fluctuations, correlations, or an optimization theorem for every finite radius.

1. K. Noda and T. Shirai, *Expected Number of Zeros of Random Power Series with Finitely Dependent Gaussian Coefficients*, arXiv:2106.02860; *Journal of Theoretical Probability* 36 (2023), 1534–1554, DOI 10.1007/s10959-022-01203-y.
2. T. Shirai, *The density of zeros of random power series with stationary complex Gaussian coefficients*, arXiv:2501.02586.
