# Spectral identifiability of near-isotropic random zonogon deficits

## Finding

Fix an integer \(K\ge1\) and a real, mean-zero trigonometric polynomial on the unoriented direction circle \([0,\pi)\),
\[
g(\theta)=\sum_{m=1}^K(\eta_m e^{-2im\theta}+\overline{\eta_m}e^{2im\theta}),\qquad\eta_m\in\mathbb C.
\]
For each integer \(n\ge2\), let \(\theta_1,\ldots,\theta_n\) be independent with common density \(f_n(\theta)=(1+\varepsilon_n g(\theta))/\pi\), where \(\varepsilon_n\ge0\), \(\varepsilon_n\to0\), and the density is nonnegative. Set \(u_j=(\cos\theta_j,\sin\theta_j)\), and form the planar zonogon
\[
Z_n=\sum_{j=1}^n[-u_j/2,u_j/2].
\]
Its perimeter equals \(2n\). Let \(A_n\) denote its area, define the normalized isoperimetric deficit by
\[
D_n=\frac1n\left(\frac{P(Z_n)^2}{4\pi}-A_n\right)=\frac{n^2/\pi-A_n}{n},
\qquad c_m=\frac2{\pi(4m^2-1)}.
\]
Extend \(\eta_m=0\) for all \(m>K\). Then the following statements hold.

**Exact finite-sample identity and expectation.** For every realization,
\[
D_n=\sum_{m=1}^{\infty}c_m\left|\frac1{\sqrt n}\sum_{j=1}^n e^{2im\theta_j}\right|^2\ge0,
\]
with an absolutely convergent nonnegative series. Its exact expectation is
\[
\mathbb E D_n=\frac1\pi+(n-1)\varepsilon_n^2 Q(g),
\qquad Q(g)=\sum_{m=1}^Kc_m|\eta_m|^2.
\]

**Critical anisotropy window and its inverse theorem.** Suppose \(n\varepsilon_n^2\to\lambda\in[0,\infty)\). Let \(G_m\) be independent standard circular complex Gaussians, normalized by \(\mathbb E|G_m|^2=1\). Then, in distribution and for the first two moments,
\[
D_n\ \Longrightarrow\ Y_{\lambda,g}=\sum_{m=1}^{\infty}c_m|G_m+\sqrt\lambda\,\eta_m|^2.
\]
For \(s\ge0\), its Laplace transform is
\[
\mathbb E e^{-sY_{\lambda,g}}=F(s)
\exp\!\left[-\lambda\sum_{m=1}^K\frac{s c_m|\eta_m|^2}{1+s c_m}\right],
\qquad F(s)=\prod_{m\ge1}(1+s c_m)^{-1}.
\]
Explicitly, with \(a=\sqrt{1-2s/\pi}\) for \(0\le s<\pi/2\),
\[
F(s)=\frac{a}{\sin(\pi a/2)}.
\]
At \(s=\pi/2\), \(F(s)=2/\pi\); for \(s>\pi/2\), with \(b=\sqrt{2s/\pi-1}\), \(F(s)=b/\sinh(\pi b/2)\).

For each **fixed known \(\lambda>0\)** and any two real trigonometric polynomials of the stipulated form, their limit variables have equal laws **if and only if** their complete power spectra \((|\eta_m|^2)_{m\ge1}\) agree. Angular phases are intrinsically invisible to the scalar deficit law. If \(\lambda\) itself is unknown, only the products \(\lambda|\eta_m|^2\) are identified.

The limiting mean and variance are
\[
\mathbb E Y_{\lambda,g}=\frac1\pi+\lambda Q(g),\qquad
\operatorname{Var}(Y_{\lambda,g})=\frac14-\frac2{\pi^2}
+2\lambda\sum_{m=1}^Kc_m^2|\eta_m|^2.
\]
At fixed total angular Fourier power \(H=\sum_{m=1}^K|\eta_m|^2>0\), the leading mean shift \(\lambda Q(g)\) is uniquely maximized, apart from angular phase, by placing all power at \(m=1\), and uniquely minimized by placing it all at \(m=K\) (when \(K=1\), these coincide).

**Above the critical window.** If \(n\varepsilon_n^2\to\infty\), while \(\varepsilon_n\to0\), then
\[
\frac{D_n}{n\varepsilon_n^2}\longrightarrow Q(g)\quad\text{in }L^1.
\]

## Assumptions and scope

The orientations are **unoriented**, so the sample space is \([0,\pi)\), not the full directed circle. The polynomial is fixed as \(n\to\infty\) and its mean is zero; positivity of \(f_n\) holds automatically for all sufficiently large \(n\) since \(g\) is bounded and \(\varepsilon_n\to0\). Sampling within a row is independent, and no independence between different values of \(n\) is required. No unproved regularity or uniformity over growing degrees \(K\) is asserted. The statistic is scale-invariant only after a length-based normalization: all generator lengths here are exactly one.

## Proof

**1. Geometry and Fourier identity.** The perimeter of a Minkowski sum of unit segments is \(2n\). The planar zonotope area formula gives
\[
A_n=\sum_{1\le i<j\le n}|\sin(\theta_i-\theta_j)|.
\]
Use the uniformly and absolutely convergent Fourier series
\[
|\sin t|=\frac2\pi-\frac4\pi\sum_{m=1}^{\infty}\frac{\cos(2mt)}{4m^2-1},
\]
and the elementary pair identity
\[
\sum_{i<j}\cos(2m(\theta_i-\theta_j))
=\frac12\left(\left|\sum_j e^{2im\theta_j}\right|^2-n\right).
\]
Since \(\sum_{m\ge1}1/(4m^2-1)=1/2\), subtraction from \(n^2/\pi\) yields exactly
\[
\frac{n^2/\pi-A_n}{n}=\sum_{m\ge1}\frac2{\pi(4m^2-1)}\left|n^{-1/2}\sum_j e^{2im\theta_j}\right|^2.
\]
Every term is nonnegative. Absolute convergence follows even pointwise from the bound \(|n^{-1/2}\sum_j e^{2im\theta_j}|^2\le n\) and summability of \((c_m)\).

**2. Mean.** Orthogonality on \([0,\pi)\) gives \(\mathbb E e^{2im\theta}=\varepsilon_n\eta_m\) for \(1\le m\le K\), and zero for \(m>K\). Therefore
\[
\mathbb E\left|n^{-1/2}\sum_j e^{2im\theta_j}\right|^2
=1+(n-1)\varepsilon_n^2|\eta_m|^2.
\]
Since \(\sum_m c_m=1/\pi\), nonnegative summation proves the exact finite-sample expectation.

**3. Joint central limit and full infinite sum.** Put \(V_{m,n}=n^{-1/2}\sum_j e^{2im\theta_j}\). When \(n\varepsilon_n^2\to\lambda<\infty\), the vector of centered \(V_{m,n}\) for finitely many fixed positive \(m\) satisfies the real multivariate Lindeberg–Feller triangular-array central limit theorem: individual summands are bounded; their conjugate covariance tends to the identity, and their unconjugated covariance tends to zero, because \(f_n\to1/\pi\) uniformly. Hence the limit coordinates are independent standard circular complex normals, with deterministic mean shifts \(\sqrt\lambda\eta_m\).

For any cutoff \(M\ge K\), the exact expected remainder satisfies
\[
\mathbb E\sum_{m>M}c_m|V_{m,n}|^2
=\sum_{m>M}c_m=\frac1{\pi(2M+1)}.
\]
Thus the tail is uniformly negligible in \(L^1\). Moreover the centered bounded summands have uniformly bounded normalized fourth moments (and the means are uniformly bounded in the critical window), so \(\sup_{n,m}\mathbb E|V_{m,n}|^4<\infty\). Minkowski's inequality and summability of \((c_m)\) then make the tails uniformly small in \(L^2\). This proves convergence in distribution and in the first two moments; the limit series is almost surely finite by its finite expectation.

**4. Laplace transform and variance.** For a standard circular complex Gaussian \(G\) and \(v\in\mathbb C\), direct Gaussian integration gives
\[
\mathbb E e^{-t|G+v|^2}=\frac1{1+t}\exp\!\left(-\frac{t|v|^2}{1+t}\right),\qquad t\ge0.
\]
Independence gives the stated infinite product and finite noncentral correction. The Euler sine product applied to the factors \(4m^2-1+2s/\pi\) evaluates \(F\), with real hyperbolic continuation beyond the crossover. Also \(\operatorname{Var}|G+v|^2=1+2|v|^2\). Since \(\sum c_m^2=1/4-2/\pi^2\), the stated mean and variance follow.

**5. Spectral identifiability.** With fixed \(\lambda>0\), dividing the two Laplace transforms by the same nonvanishing baseline \(F(s)\), taking logarithms, and cancelling \(-\lambda\) shows that equality in law is equivalent to equality for \(s>0\) of two rational functions
\[
\sum_{m=1}^K\frac{s c_m|\eta_m|^2}{1+s c_m}.
\]
The positive numbers \(c_m\) are pairwise distinct; each nonzero coefficient produces a unique simple pole at \(s=-1/c_m\). A rational function that vanishes on the positive real axis vanishes identically, so its partial-fraction residues, and hence all \(|\eta_m|^2\), agree. Conversely equal powers make the transforms identical. Phases cancel from every expression. This is an exact inverse statement, not a conclusion from finitely many simulated moments. Since \(c_1>c_2>\cdots>0\), the endpoint harmonic sensitivity statement follows by weighted averaging at fixed total power.

**6. Above the critical window.** For fixed \(m\), write \(V_{m,n}=\sqrt n\varepsilon_n\eta_m+\xi_{m,n}\) with \(\mathbb E\xi_{m,n}=0\) and \(\mathbb E|\xi_{m,n}|^2\le1\). By Cauchy–Schwarz, the summed cross terms have \(L^1\)-size at most \(2\sqrt n\varepsilon_n\sum_{m=1}^Kc_m|\eta_m|\), while the nonnegative noise terms have total expectation at most \(\sum_m c_m=1/\pi\). Divide by \(n\varepsilon_n^2\to\infty\) to obtain the stated \(L^1\) law.

## Verification

The included standalone `verify.py` checks the exact geometry–Fourier identity at several sizes and deterministic angle patterns with explicit Fourier-truncation error bounds; compares the Euler-product Laplace factor with its closed form on both sides of the hyperbolic crossover; tests the finite-row anisotropic expectation against independently generated angle samples; and checks the decreasing harmonic weights. The program completes with `ALL_CHECKS_PASSED`. The mathematical inverse assertion depends on the rational-function pole argument above, not on finite experiments.

## Relationship to prior work

Schneider, *Random zonotopes and valuations* (first public arXiv version, February 14, 2022), gives valuation expectations for iid random segments and a conventional \(U\)-statistic central limit theorem under nondegeneracy conditions. The fixed-unit-length uniform angular model considered here is degenerate at the first \(U\)-statistic projection, and the near-uniform triangular-array regime is outside his stated central-limit hypotheses. The exact baseline uniform-direction deficit series and certain single-long-generator noncentral limits were already known; neither baseline nor the isolated long-generator deformation is claimed as new. The present claim concerns a perturbation of the entire sampling direction law, an arbitrarily prescribed finite angular power spectrum, and an if-and-only-if inverse identification theorem.

Buffière and Marchal, *Fluctuations of lattice zonotopes and polygons* (March 31, 2023), study uniformly sampled **lattice** zonotopes and boundary-fluctuation processes. They do not use iid unit-length continuous orientations nor determine the above scalar inverse law. General Fourier, Gaussian central-limit, and partial-fraction techniques are standard ingredients rather than separate claims of novelty.

## Limitations

The theorem is two-dimensional, has fixed finite Fourier bandwidth \(K\), independent directions and equal unit-length generators. The inverse theorem identifies **Fourier powers only**, not phases, and assumes a known positive critical-window intensity \(\lambda\). At \(\lambda=0\), all angular perturbations have the same baseline limit and no inverse identification is possible. No extension to arbitrary angular densities with infinitely many modes, correlated directions, arbitrary segment lengths, or higher-dimensional zonotopes is proved. Although the explicit cited comparison does not imply the claim, exhaustive historical priority certification has not been performed.

## References

1. R. Schneider, *Random zonotopes and valuations*, arXiv:2202.06774, first submitted February 14, 2022. https://arxiv.org/abs/2202.06774
2. T. Buffière and P. Marchal, *Fluctuations of lattice zonotopes and polygons*, arXiv:2303.18045, first submitted March 31, 2023. https://arxiv.org/abs/2303.18045
3. Classical Fourier expansion of \(|\sin t|\), Euler's sine product, and the multivariate Lindeberg–Feller central limit theorem (standard tools used in the proof).
