# Sharp reentrant mean-square stability of randomized damped-shear time splitting

## Finding

For every \(a>0\) and \(b\ge0\), consider the damped planar rotation
\[
A=A_1+A_2,\qquad
A_1=\begin{pmatrix}-a&b\\0&-a\end{pmatrix},\quad
A_2=\begin{pmatrix}-a&0\\-b&-a\end{pmatrix}.
\]
Each summand is Hurwitz, with both eigenvalues equal to \(-a\); the complete system satisfies \(\|e^{At}x\|_2=e^{-2at}\|x\|_2\). On a fixed grid of step \(h>0\), independently at every step choose \(I_k\) uniformly from \(\{1,2\}\) and evolve exactly under \(2A_{I_k}\), i.e. \(X_{k+1}=e^{2hA_{I_k}}X_k\). This is the equal-probability, probability-corrected, one-generator-at-a-time randomized splitting from [1].

For every deterministic initial vector \(x_0\in\mathbb R^2\) and integer \(k\ge0\), the **exact** second-moment and mean-vector identities are
\[
\mathbb E\|X_k\|_2^2=q(h)^k\|x_0\|_2^2,\qquad
\|\mathbb E X_k\|_2^2=m(h)^k\|x_0\|_2^2,
\]
where
\[
q(h)=e^{-4ah}(1+2b^2h^2),\qquad m(h)=e^{-4ah}(1+b^2h^2).
\]
Consequently the scheme is mean-square asymptotically stable for all nonzero initial vectors exactly when \(q(h)<1\); if \(q(h)=1\) its expected squared Euclidean energy stays constant, and if \(q(h)>1\) that energy grows exponentially with the number of grid steps.

For \(b=0\), stability holds at every positive \(h\). For \(b>0\) put \(\beta=b/a\) and define \(s_*>1\) as the unique positive solution other than zero of
\[
\log(1+s_*)=\frac{2s_*}{1+s_*},\qquad
z_*=\sqrt{2s_*},\qquad
\beta_*:=\frac{2z_*}{\log(1+s_*)}=3.514699022529\ldots.
\]
The **complete sharp phase diagram** over all positive grid steps is:

* If \(0<\beta<\beta_*\), then \(q(h)<1\) for every \(h>0\).
* If \(\beta=\beta_*\), then \(q(h)=1\) at the unique positive step \(h_*=z_*/(2b)\), and \(q(h)<1\) for every other positive step.
* If \(\beta>\beta_*\), there are exactly two positive steps \(h_-<h_+\) solving \(q(h)=1\); the scheme is mean-square unstable exactly on the open interval \(h_-<h<h_+\), and strictly stable on \(0<h<h_-\) and \(h>h_+\).

Thus stability is **reentrant**: intermediate grid steps may be unstable while both finer and coarser steps are stable. The two component generators, as well as their sum, remain Hurwitz throughout. In particular, at \(a=1\), \(b=4\), and \(h=1/4\),
\[
q(h)=3/e>1,\qquad m(h)=2/e<1,
\]
so the norm of the expected state decays geometrically while the expected squared norm grows geometrically, for every nonzero initial vector.

## Assumptions and scope

The matrix dimension is exactly two. Parameters satisfy \(a>0\), \(b\ge0\), \(h>0\); the random choices are independent across steps, equiprobable, and independent of the current state. The same strictly positive grid step is used indefinitely. Each sampled subsystem is solved **exactly** over one grid step, with the factor of two required to make its generator unbiased. The studied quantity is expected squared Euclidean state norm at grid points, not a pathwise error criterion, finite-horizon control performance, or computational runtime. All computations assume exact real arithmetic.

## Proof

**Exact propagators and moments.** Write \(N_1=E_{12}\), \(N_2=E_{21}\), and \(z=2bh\). As \(N_i^2=0\), exponentiation gives
\[
M_1=e^{2hA_1}=e^{-2ah}\begin{pmatrix}1&z\\0&1\end{pmatrix},\qquad
M_2=e^{2hA_2}=e^{-2ah}\begin{pmatrix}1&0\\-z&1\end{pmatrix}.
\]
Direct multiplication establishes the global identity
\[
\frac{M_1^{\mathsf T}M_1+M_2^{\mathsf T}M_2}{2}
=e^{-4ah}\left(1+\frac{z^2}{2}\right)I_2=q(h)I_2.
\]
Independence of the next choice from \(X_k\) therefore gives
\(\mathbb E[\|X_{k+1}\|_2^2\mid X_k]=q(h)\|X_k\|_2^2\). Iterating proves the second-moment formula **for every initial vector and every nonnegative integer** \(k\).

Similarly
\[
\overline M:=\mathbb E M_{I_k}
=e^{-2ah}\begin{pmatrix}1&z/2\\-z/2&1\end{pmatrix},\qquad
\overline M^{\mathsf T}\overline M
=e^{-4ah}\left(1+\frac{z^2}{4}\right)I_2=m(h)I_2.
\]
Hence \(\mathbb E X_k=\overline M^{k}x_0\). Since \(\overline M\) is a positive scalar multiple of a rotation, \(\|\overline M^kx_0\|_2^2=m(h)^k\|x_0\|_2^2\). Finally \(A=-2aI+b\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}\) is a scalar damping plus skew-symmetry, proving the asserted deterministic exact contraction.

**Unique critical ratio and all boundary cases.** If \(b=0\), \(q(h)=e^{-4ah}<1\). Assume \(b>0\), and set \(\beta=b/a\) and \(z=2bh>0\). Then
\[
\log q(h)=\log(1+z^2/2)-\frac{2z}{\beta}
=z\left(F(z)-\frac2\beta\right),\qquad
F(z)=\frac{\log(1+z^2/2)}z.
\]
The function \(F\) tends to zero at both endpoints \(z\downarrow0\) and \(z\to\infty\). Its derivative has the sign of
\[
g(s)=\frac{2s}{1+s}-\log(1+s),\qquad s=z^2/2.
\]
Indeed \(dg/ds=(1-s)/(1+s)^2\). Thus \(g(0)=0\); it is strictly increasing on \((0,1)\), strictly decreasing on \((1,\infty)\), and tends to minus infinity as \(s\to\infty\). There is exactly one zero \(s_*>1\), and \(F\) increases strictly until \(z_*\) and decreases strictly afterward. Consequently \(\max_{z>0}F(z)=\log(1+s_*)/z_*=2/\beta_*\). Comparing the horizontal level \(2/\beta\) with this unique maximum gives exactly the three cases in the finding, including uniqueness of \(h_\pm\), the neutral tangency at \(h_*\), and strict small- and large-step stability.

**Mean versus mean square.** For \(a=1\), \(b=4\), \(h=1/4\), we have \(z=2\) and \(e^{-4ah}=e^{-1}\). Thus \(q=3/e\) and \(m=2/e\). The elementary strict inequalities \(2<e<3\) establish \(m<1<q\) without approximation. Both generators have eigenvalues \(-1\), while the complete generator has eigenvalues \(-2\pm4i\).

## Verification

The standalone standard-library script `verify.py` computes exact rational averages over **every** selection word of lengths zero through seven, for four rational shear strengths and three nonzero initial vectors. It checks both moment identities against the closed-form expressions with the common exponential damping factored out; this produces 192 exact equalities. A separate numerical diagnostic checks the unique critical root and its location to approximately twelve decimal places and verifies the explicit \(2/e<1<3/e\) separation. Run `python verify.py` from this directory; expected final line: `VERIFICATION_OK`. The analytical derivative argument, not the finite test, proves the all-parameter and infinite-horizon claims.

## Relationship to prior work

Veldman–Zuazua [1] introduce the particular one-component-at-a-time, inverse-probability-corrected exponential randomization (their Example 1), and prove convergence as the mesh is refined over a fixed finite horizon. Their main clean error estimates assume dissipativity of each split generator, while Remark 9 addresses non-dissipative generators with time-growing error estimates, not an exact all-step infinite-horizon stability classification. The present shear family is dissipative only when \(b\le2a\); the instability occurs outside this hypothesis, so it **does not contradict** those estimates.

Ogura–Martin [2] give a broad mean-stability/mean-square Lyapunov characterization for random matrix products. That known machinery covers the *general decision problem* and is not claimed as new; it does not state the specialized scalar identity, the unique critical damping-to-shear ratio, or the reentrant two-threshold step geometry. Veldman–Borkowski–Zuazua [3] study a randomized **feedback** model-predictive-control scheme with sufficient stability estimates, rather than the zero-input independent exact-propagator experiment here. Eisenmann–Stillfjord [4] study a different randomized splitting discretization in monotone evolution and diffusion problems, with finite-horizon error bounds rather than this sharp planar exponential-splitting diagram.

## Limitations

The statement is exact only for the displayed two-generator family, equal probabilities, probability correction, exact subsystem exponentials and fixed steps. It does not characterize almost-sure Lyapunov exponents, higher moments, arbitrary nonnormal splits, stochastic forcing, feedback-controlled trajectories, or accuracy at large step sizes. Large-step mean-square stability is not a claim of good approximation to the true rotation. The finite enumeration in `verify.py` does not prove infinite-time behavior. The novelty comparison covers the inspected primary literature and relevant indexed results but cannot rule out unindexed equivalent work; independent external mathematical validation has not been performed.

## References

1. D. W. M. Veldman and E. Zuazua, *A framework for randomized time-splitting in linear-quadratic optimal control*, arXiv:2109.13798v1 (first posted 2021-09-28); *Numerische Mathematik* 151 (2022), 495–549. https://arxiv.org/abs/2109.13798 ; https://doi.org/10.1007/s00211-022-01290-3 .
2. M. Ogura and C. F. Martin, *On the mean stability of a class of switched linear systems*, arXiv:1409.6032v1 (2014). https://arxiv.org/abs/1409.6032 .
3. D. W. M. Veldman, A. Borkowski, and E. Zuazua, *Stability and Convergence of a Randomized Model Predictive Control Strategy*, arXiv:2211.05463v1 (2022). https://arxiv.org/abs/2211.05463 .
4. M. Eisenmann and T. Stillfjord, *A randomized operator splitting scheme inspired by stochastic optimization methods*, arXiv:2210.05375v1 (2022); *Numerische Mathematik* 156 (2024), 435–461. https://arxiv.org/abs/2210.05375 .
