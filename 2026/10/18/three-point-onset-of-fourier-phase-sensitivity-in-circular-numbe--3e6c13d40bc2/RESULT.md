# Three-point onset of Fourier-phase sensitivity in circular number variance

## Finding
Let \(0<\varepsilon<1/2\) and consider the two strictly positive probability densities on the unit circle \(\mathbb T=\mathbb R/\mathbb Z\):
\[
f_+(x)=1+\varepsilon\bigl(\cos(2\pi x)+\cos(4\pi x)\bigr),\qquad
f_\perp(x)=1+\varepsilon\bigl(\cos(2\pi x)+\sin(4\pi x)\bigr).
\]
For independent observations \(X_1,\ldots,X_N\) drawn from either density, set
\[
V_N(s)=\int_0^1\bigl(S_N(x,s)-Ns\bigr)^2\,dx,
\qquad S_N(x,s)=\#\{j:X_j\in(x,x+s]\pmod 1\}.
\]
The two densities have identical Fourier power spectra but are not rotations or reflections of one another. For every integer \(N\ge1\), their means \(\mathbb E V_N(s)\) agree for every \(s\in[0,1]\). For \(N=1,2\), the **entire random curve** \(s\mapsto V_N(s)\) has the same distribution for the two densities. Nonetheless, for every integer \(N\ge3\),
\[
\boxed{\operatorname{Var}_{f_+}\!\left(V_N(1/2)\right)
-\operatorname{Var}_{f_\perp}\!\left(V_N(1/2)\right)
=\frac{N(N-1)(N-2)\varepsilon^3}{\pi^4}>0.}
\]
Hence **three observations are the sharp first sample size** for revealing, through circular number-variance fluctuations, a Fourier-phase difference invisible in any statistic of a single pairwise displacement.

## Assumptions and scope
All observations are independent and identically distributed within each experiment; they have one of the two displayed densities, with fixed \(\varepsilon\in(0,1/2)\). Intervals wrap around the unit circle; endpoints do not affect integrals because the densities are continuous. The statement is exact for every finite integer \(N\ge1\), not a large-sample approximation. The claim about identical laws at sample size two concerns the full curve \(V_N(\cdot)\), while the separation for larger samples concerns variance at the natural half-circle window \(s=1/2\). It does not claim identification of arbitrary densities from this statistic.

## Proof
**1. Pairwise decomposition.** Put \(I_x(y)=\mathbf 1\{y\in(x,x+s]\}\), and define the real periodic kernel
\[
K_s(u,v)=\int_0^1 (I_x(u)-s)(I_x(v)-s)\,dx.
\]
The diagonal integral equals \(s(1-s)\), and expansion of the square gives, for every deterministic configuration,
\[
V_N(s)=Ns(1-s)+2\sum_{1\le i<j\le N}K_s(X_i,X_j).
\tag{1}
\]
The kernel depends only on the circular difference \(u-v\). If \(\delta(u,v)=\min\{|u-v|,1-|u-v|\}\), then at \(s=1/2\),
\[
K_{1/2}(u,v)=\tfrac14-\delta(u,v).
\tag{2}
\]
This follows because the overlap of two half-circle intervals is \(1/2-\delta(u,v)\). As a periodic function of \(u-v\), the Fourier series has coefficient
\[
\widehat K_{1/2}(k)=
\frac{\sin^2(\pi k/2)}{\pi^2 k^2}\quad(k\in\mathbb Z\setminus\{0\}),
\qquad\widehat K_{1/2}(0)=0.
\tag{3}
\]
In particular, the coefficients at \(k=\pm1\) equal \(1/\pi^2\), and those at even nonzero \(k\) vanish.

**2. Pairwise indistinguishability.** For \(\widehat f(k)=\int_0^1 f(x)e^{-2\pi ikx}\,dx\), both densities have the same coefficients at zero and the same absolute values at every integer frequency: \(\widehat f(0)=1\); \(|\widehat f(\pm1)|=|\widehat f(\pm2)|=\varepsilon/2\); all remaining coefficients vanish. Thus, for two independent samples, the circular difference \(X_1-X_2\) has the same law in both models, since its Fourier coefficients equal \(|\widehat f(k)|^2\). Formula (1) proves equality in law of the entire curve for \(N=2\); \(N=1\) is deterministic. The mean in (1) depends only on the pair-difference distribution, and so agrees for all \(N,s\).

These densities are not rotations or reflections: the first-harmonic coefficient is real and positive for both, fixing the possible rotational alignment, whereas their second-harmonic coefficients are respectively \(\varepsilon/2\) and \(-i\varepsilon/2\). Under reflection the aligned real coefficient stays real; it cannot become purely imaginary. Equivalently, the ratio \(\widehat f(2)/\widehat f(1)^2\) is invariant under rotation and conjugated under reflection; its values are \(2/\varepsilon\) and \(-2i/\varepsilon\).

**3. A two-point versus three-point variance decomposition.** Fix the half-circle window. For a given density \(f\) let \(Y_{ij}=K_{1/2}(X_i,X_j)\), \(A_f=\operatorname{Var}(Y_{12})\), and \(B_f=\operatorname{Cov}(Y_{12},Y_{13})\). Disjoint pairs are independent. Counting unordered edges and pairs of edges sharing one vertex yields
\[
\operatorname{Var}_f(V_N(1/2))
=4\left[\binom N2 A_f+N(N-1)(N-2)B_f\right],
\tag{4}
\]
with the second term absent when \(N\le2\). Equality of pair-difference laws implies \(A_{f_+}=A_{f_\perp}\).

**4. Conditional overlap detects phase.** Define \(\Phi_f(x)=\mathbb E_f[K_{1/2}(x,X_2)]\) and \(\mu_f=\mathbb E_f[Y_{12}]\). Conditional independence gives
\[
B_f=\int_0^1\Phi_f(x)^2f(x)\,dx-\mu_f^2.
\tag{5}
\]
Convolution with the kernel in (3) retains the first harmonic and annihilates the second harmonic, so **for both models**
\[
\Phi_{f_+}(x)=\Phi_{f_\perp}(x)
=\frac{\varepsilon}{\pi^2}\cos(2\pi x),
\qquad \mu_{f_+}=\mu_{f_\perp}=\frac{\varepsilon^2}{2\pi^2}.
\tag{6}
\]
Consequently, using \(\cos^2(2\pi x)=(1+\cos(4\pi x))/2\),
\[
\begin{aligned}
B_{f_+}-B_{f_\perp}
&=\frac{\varepsilon^3}{\pi^4}
\int_0^1\cos^2(2\pi x)
\bigl(\cos(4\pi x)-\sin(4\pi x)\bigr)\,dx\\
&=\frac{\varepsilon^3}{4\pi^4}.
\end{aligned}
\tag{7}
\]
Substitution into (4) proves the displayed variance difference. It is strictly positive exactly when \(N\ge3\), since \(\varepsilon>0\). Together with the complete pairwise-law equality for \(N\le2\), this establishes the sharp sample-size cutoff.

## Verification
The accompanying `verify.py` independently evaluates the relevant Laurent-Fourier coefficients in exact rational Gaussian arithmetic, keeping the factor \(\pi^{-4}\) separate. It verifies the conditional-overlap moment identity and the all-size covariance-gap polynomial for 770 rational parameter/sample-size combinations. It also evaluates the defining circular integral against the pairwise formula for 250 exact-rational configurations. A separate numerical three-point quadrature at grid sizes 24, 48, and 96 reproduces the continuous variance gap to decreasing relative error; those finite-grid checks supplement but do not replace the all-size proof.

## Relationship to prior work
Aistleitner, Hörmann, and Manskova (2026) study circular number variance for *uniform* independent points, obtaining its distribution and exact variance under that null; their finite-sample formula is a degenerate order-two U-statistic calculation. The present result concerns two explicit, *nonuniform* sampling distributions with identical two-point difference laws and different second moments of number variance. The distinction is created by the three-observation shared-vertex covariance term, absent under the uniform null.

Rajala, Olhede, Grainger, and Murrell (2023) develop fourth-order Fourier moments for homogeneous spatial point processes, whereas the present mechanism uses inhomogeneous iid densities on a compact circle and isolates the first phase-sensitive sample size for this particular statistic. Classical homometric-set and bispectrum theory explains why two-point power spectra can lose phase and higher correlations may recover it; this work computes the exact half-circle number-variance separation and its coefficient for the first possible sample size. Neither the cited uniform-null result nor the inspected homogeneous-process formula states the precise claim here.

## Limitations
The phenomenon is exhibited by one natural two-harmonic family and the half-circle scale, not a classification of all circular densities or window lengths. The complete-curve identity is asserted only for sample sizes one and two. The variance difference does not quantify the statistical power of any proposed hypothesis test or provide a full distributional ordering. Previous results on general Fourier moments may furnish alternative derivations, and unindexed treatments of the exact same special case remain a literature risk. This is a mathematical proof supported by reproducible checks, not independent external validation.

## References
1. C. Aistleitner, S. Hörmann, and M. Manskova, *On the asymptotic behavior of the number variance of random points on the unit torus*, arXiv:2610.11687v1, publicly submitted 8 October 2026. https://arxiv.org/html/2610.11687v1
2. T. A. Rajala, S. C. Olhede, J. P. Grainger, and D. J. Murrell, *What is the Fourier Transform of a Spatial Point Process?*, IEEE Transactions on Information Theory 69 (2023), 5219–5252. https://doi.org/10.1109/TIT.2023.3269514
3. J. Rosenblatt and P. D. Seymour, *The Structure of Homometric Sets*, SIAM Journal on Algebraic and Discrete Methods 3 (1982), 343–350. https://doi.org/10.1137/0603035
