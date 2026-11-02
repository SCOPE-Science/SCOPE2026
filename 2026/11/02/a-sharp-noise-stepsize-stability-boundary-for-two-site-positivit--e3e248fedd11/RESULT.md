# A sharp noise–stepsize stability boundary for two-site positivity-preserving stochastic heat splitting

## Finding

For a two-site discrete stochastic heat equation with independent diagonal multiplicative Brownian noise, exact Lie–Trotter splitting is positivity preserving at every timestep but does not always preserve long-time mean-square stability. Fix a diffusion rate \(b>0\), noise variance rate \(v\geq0\), and timestep \(h>0\). Put \(\eta=bh\). The exact sharp critical noise intensity for the geometric-Brownian-then-heat splitting is

\[
\boxed{\frac{v_*(h)}b=2+\frac1\eta\log\!\left(\frac{2e^{4\eta}+e^{2\eta}+1}{e^{4\eta}+e^{2\eta}+2}\right).}
\]

For every deterministic initial state, the split iterates decay exponentially in mean square if \(v<v_*(h)\). At or above this boundary, the method is not asymptotically mean-square stable, even for some strictly positive initial data. The critical ratio \(v_*(h)/b\) decreases *strictly* from \(3\) to \(2\) as \(h\) increases from zero to infinity. The underlying continuous-time Itô system, by contrast, is exponentially mean-square stable precisely when \(v<3b\). Thus for every \(2b<v<3b\), there is one sharp positive step cutoff separating a stable discretization from an unstable one, although every computed state remains nonnegative whenever the starting state is nonnegative.

An exact rational second-moment witness occurs at \(b=1\), \(h=\log2\), and \(v=\log7/\log2\), where the continuous SDE is mean-square stable, whereas the split second-moment matrix has \(\det(I-K)=-9/256\), hence a Perron eigenvalue greater than one.

## Assumptions and scope

Consider the two-dimensional Itô SDE

\[
\mathrm dX_t=b\begin{pmatrix}-2&1\\1&-2\end{pmatrix}X_t\,\mathrm dt
 +\sqrt v\begin{pmatrix}X_{t,1}&0\\0&X_{t,2}\end{pmatrix}\mathrm dW_t,
\]

where \(W\) has two independent standard real Brownian components. The random numerical step, with independent fresh Gaussian increments \(\Delta W_{k,i}\sim N(0,h)\), is

\[
X_{k+1}=H_hD_kX_k,\quad
H_h=\exp\!\left(bh\begin{pmatrix}-2&1\\1&-2\end{pmatrix}\right),\quad
D_k=\operatorname{diag}\!\left(e^{\sqrt v\Delta W_{k,1}-vh/2},e^{\sqrt v\Delta W_{k,2}-vh/2}\right).
\]

The noise subsystem is advanced first, then the deterministic heat subsystem. It is the two-interior-node linear-noise specialization of the Lie–Trotter construction in Bréhier, Cohen and Ulander (2023). In that spatial normalization \(b=9\) and \(v=3c^2\) for noise nonlinearity \(g(u)=cu\). The parameters \(b,v,h\) are independent for the general matrix statement. Stability means that \(\mathbb E\|X_k\|_2^2\leq C\gamma^k\|X_0\|_2^2\) for some finite \(C\) and \(\gamma<1\), for all deterministic initial vectors; continuous stability is analogous with \(e^{-ct}\). No statement about almost-sure Lyapunov exponents or nonnormal transient growth is included.

## Proof

**1. Positivity and exact moment reduction.** Diagonalize the heat generator, whose eigenvalues are \(-b\) and \(-3b\). For \(\eta=bh\),

\[
H_h=e^{-2\eta}\begin{pmatrix}\cosh\eta&\sinh\eta\\\sinh\eta&\cosh\eta\end{pmatrix}.
\]

Every matrix entry of \(H_h\) is strictly positive when \(h>0\); every entry of \(D_k\) is positive almost surely. Therefore the splitting preserves the nonnegative orthant without a timestep restriction.

For \(s_k=\mathbb E(X_{k,1}^2+X_{k,2}^2)/2\), \(c_k=\mathbb E(X_{k,1}X_{k,2})\), \(d_k=\mathbb E(X_{k,1}^2-X_{k,2}^2)/2\), independence of the diagonal noise and the lognormal identities \(\mathbb E D_{ii}=1\) and \(\mathbb E D_{ii}^2=\mu=e^{vh}\) give

\[
\begin{pmatrix}s_{k+1}\\c_{k+1}\end{pmatrix}
=K\begin{pmatrix}s_k\\c_k\end{pmatrix},\qquad
K=e^{-4\eta}\begin{pmatrix}\mu\cosh2\eta&\sinh2\eta\\\mu\sinh2\eta&\cosh2\eta\end{pmatrix},\qquad
d_{k+1}=\mu e^{-4\eta}d_k.
\]

The matrix \(K\) is entrywise strictly positive. Its Perron eigenvalue \(\rho(K)\) strictly exceeds its upper-left diagonal entry \(\mu e^{-4\eta}\cosh2\eta\), which is at least the absolute eigenvalue \(\mu e^{-4\eta}\) of the antisymmetric moment mode. Thus the full second-moment evolution has growth rate \(\rho(K)\); \(\rho(K)<1\) is necessary and sufficient for uniform exponential mean-square decay of all deterministic initial states. When \(\rho(K)\geq1\), the positive initial vector \((1,1)\) has a strictly positive projection onto the Perron left eigenvector and yields nondecay or growth.

**2. Exact critical curve.** At fixed \(\eta>0\), the entries of \(K\) increase with \(\mu\); Perron–Frobenius implies strict growth of \(\rho(K)\). At \(\mu=1\), \(\rho(K)=e^{-2\eta}<1\); as \(\mu\to\infty\), \(\rho(K)\to\infty\). Hence a unique crossing occurs. Solving \(\det(I-K)=0\) yields, with \(z=e^{2\eta}>1\),

\[
\mu_*(\eta)=\frac{e^{4\eta}-\cosh2\eta}{\cosh2\eta-e^{-4\eta}}
=z\,\frac{2z^2+z+1}{z^2+z+2}.
\]

The denominator is positive, so there is no extraneous root. Taking \(\log\mu_*/h\) gives the displayed \(v_*(h)\). For fixed \(\eta\), the strict stability range is exactly \(0\le v<v_*(h)\); equality is neutral in second moment, not asymptotically decaying.

**3. Strict one-interval law.** Define \(\phi(\eta)=\log[(2z^2+z+1)/(z^2+z+2)]\) with \(z=e^{2\eta}\). Then \(\phi(0)=0\), \(\phi'(0)=1\) and \(\phi(\infty)=\log2\). Differentiating yields the exact factorization

\[
\phi''(\eta)=-\frac{8z(z-1)(z+1)(z^4+12z^3+10z^2+12z+1)}{(z^2+z+2)^2(2z^2+z+1)^2}<0
\quad(\eta>0).
\]

Thus \(\phi\) is strictly concave, and \(\phi(\eta)/\eta\) strictly decreases from one to zero. Hence \(v_*(h)/b=2+\phi(\eta)/\eta\) strictly decreases from three to two. It follows that \(v\le2b\) gives stability for every finite \(h>0\), \(2b<v<3b\) gives a unique finite upper step cutoff, and \(v\ge3b\) gives instability at every finite \(h>0\).

For reference, the sharp endpoint expansions are

\[
\frac{v_*(h)}b=3-\frac34\eta^2+\frac{11}{16}\eta^4+O(\eta^6)\quad(\eta\downarrow0),
\qquad
\frac{v_*(h)}b=2+\frac{\log2}{\eta}+O\!\left(\frac{e^{-2\eta}}\eta\right)\quad(\eta\to\infty).
\]

**4. Continuous-time threshold.** The Itô product formula gives

\[
\frac{\mathrm d}{\mathrm dt}\begin{pmatrix}s\\c\end{pmatrix}
=\begin{pmatrix}v-4b&2b\\2b&-4b\end{pmatrix}\begin{pmatrix}s\\c\end{pmatrix},
\qquad \dot d=(v-4b)d.
\]

The dominant exponent of this positive off-diagonal matrix is

\[
\lambda_+=\frac{v-8b+\sqrt{v^2+16b^2}}2,
\]

which is negative precisely when \(v<3b\), zero at \(v=3b\), and positive above. This dominates the exponent of \(d\), yielding the continuous claim.

**5. Exact stable-continuous/unstable-discrete witness.** Choose \(b=1\), \(h=\log2\), and \(v=\log7/\log2\). Here \(z=4\), \(\mu=7\), and \(2<v<3\), but

\[
K=\frac1{128}\begin{pmatrix}119&15\\105&17\end{pmatrix},
\qquad \det(I-K)=-\frac9{256}<0.
\]

The matrix \(I-K\) has one negative eigenvalue, so \(\rho(K)>1\). For \(X_0=(1,1)\), the first-step expected squared Euclidean norm is \(67/32\), compared with the initial norm squared of two. Scaling \(b=9\), \(h=(\log2)/9\), and \(v=9\log7/\log2\) places the same witness in the three-grid-point Dirichlet heat discretization.

## Verification

Run `python3 verify.py` with the Python standard library. It checks the exact rational crossing and instability certificate, the discrete/continuous stability parameters, nine numerical checks on both sides of the critical curve, a finite collection of concavity-polynomial evaluations and a seeded Gaussian second-moment simulation. The reported output for the bundled verifier is:

```
VERIFY_OK rational_witness=1 threshold_levels=9 curvature_factors=300 monte_carlo=120000
```

The analytical factorization, Perron–Frobenius crossing and second-moment equalities—not the finite tests—prove the theorem for the whole stated parameter range. Random simulations cannot certify asymptotic stability or exclusion of previously published equivalent theorems.

## Relationship to prior work

Bréhier, Cohen and Ulander (2023) introduce this positivity-preserving Lie–Trotter construction, including linear multiplicative-noise examples, and establish finite-horizon mean-square error control subject to mesh/timestep conditions. The current calculation isolates a *long-time* stability question and determines its sharp all-step boundary on two interior grid nodes; finite-horizon convergence estimates alone do not imply the boundary.

Lang, Petersson and Thalhammer (2017) develop general second-moment spectral stability criteria for stochastic numerical approximations, including stochastic heat discretizations. The covariance-matrix/spectral-radius principle is therefore not claimed as new. The specific exact lognormal splitting matrix, the monotone closed-form noise threshold, and the stable-SDE/unstable-splitting region are the assessed specialization. Erdogan and Lord (2018) and Torkzadeh et al. (2022) analyze other exponential or split-step stochastic integrators, not the displayed two-site geometric-noise-then-heat map.

## Limitations

The result concerns two interior sites, constant diffusion and independent equal-intensity diagonal geometric Brownian noise. It is an exact-arithmetic, unbounded-time mean-square result; positivity and mean-square stability are different properties. It does not establish a spatially uniform threshold, finite-time strong error, almost-sure stability or a theorem for higher dimensions, nonlinearity, correlated driving noise, or a different splitting order. General spectral stability criteria are classical; specialist priority for the present closed-form boundary still warrants independent examination.

## References

1. C.-E. Bréhier, D. Cohen, J. Ulander, *Analysis of a positivity-preserving splitting scheme for some nonlinear stochastic heat equations*, arXiv:2302.08858, first posted 17 February 2023. https://arxiv.org/abs/2302.08858
2. A. Lang, A. Petersson, A. Thalhammer, *Mean-square stability analysis of approximations of stochastic differential equations in infinite dimensions*, BIT Numerical Mathematics 57 (2017), 963–990. https://doi.org/10.1007/s10543-017-0684-7
3. S. Erdogan, G. Lord, *A new class of exponential integrators for SDEs with multiplicative noise*, IMA Journal of Numerical Analysis (2019). https://doi.org/10.1093/imanum/dry008
4. S. Torkzadeh, M. Ranjbar, M. Micula, K. Nouri, *Convergence and Stability of a Split-Step Exponential Scheme Based on the Milstein Methods*, Symmetry 14 (2022), 2413. https://doi.org/10.3390/sym14112413
