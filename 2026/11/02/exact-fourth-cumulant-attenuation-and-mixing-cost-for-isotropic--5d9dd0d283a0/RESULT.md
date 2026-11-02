# Exact fourth-cumulant attenuation and mixing cost for isotropic noisy Kaczmarz

## Finding

Consider the fresh-row, normalized noisy projection iteration
\[
X_{n+1}=X_n+(Y_{n+1}-U_{n+1}^{\mathsf T}X_n)U_{n+1},
\]
where the directions are independent and uniform on the unit sphere in \(\mathbb R^d\), and independent response values \(Y_n\) have second moment \(\sigma^2>0\) and finite fourth moment \(\mu_4\). This is the row projection onto the newly observed hyperplane \(U_{n+1}^{\mathsf T}x=Y_{n+1}\), not iteration against a frozen matrix.

For every integer \(d\ge2\), there is a unique stationary distribution with finite fourth moment. With \(X\) drawn from it, every unit vector \(e\) satisfies
\[
\mathbb EX=0,\qquad \operatorname{Cov}(X)=\sigma^2I_d,
\]
\[
\boxed{\mathbb E[(e^{\mathsf T}X)^4]
=3\sigma^4+\frac{3}{2d+1}(\mu_4-3\sigma^4).}
\]
In particular, the stationary coordinate excess kurtosis is exactly \(3/(2d+1)\) times the excess kurtosis of the refreshed response. The identity is exact, not a Gaussian weak-convergence assertion.

For the stationary chain and every integer lag \(k\ge0\),
\[
\boxed{\operatorname{Cov}(e^{\mathsf T}X_0,e^{\mathsf T}X_k)
=\sigma^2(1-1/d)^k.}
\]
Consequently, if \(\overline Z_N=N^{-1}\sum_{j=0}^{N-1}e^{\mathsf T}X_j\), then
\[
\lim_{N\to\infty}N\operatorname{Var}(\overline Z_N)
=\sigma^2(2d-1).
\]
Thus the dimension-dependent suppression of non-Gaussian fourth cumulants is accompanied by an exact growth of stationary time-average correlation cost.

## Assumptions and scope

Fix an integer \(d\ge2\). For each time \(n\ge1\), \(U_n\) is Haar-uniform on \(S^{d-1}\), \(Y_n\) is real-valued, and the pairs are independent over time. Within a pair, \(U_n\) and \(Y_n\) are independent. Only \(0<\sigma^2=\mathbb E Y_n^2<\infty\) and \(\mu_4=\mathbb E Y_n^4<\infty\) are required; \(Y_n\) need not have zero mean, be symmetric, or be Gaussian. An initial law with finite fourth moment suffices for Wasserstein convergence. The stationary identities refer to the stationary process.

This is a continuously resampled direction-and-response model; a fixed noisy matrix, a fixed right-hand-side vector, and general nonisotropic row distributions are not asserted to obey the same formulas.

## Proof

Write \(P_u=I_d-uu^{\mathsf T}\). Since \(P_uu=0\), the update is \(P_{U_{n+1}}X_n+Y_{n+1}U_{n+1}\). Rotational invariance gives, for each deterministic \(v\),
\[
\mathbb E(U^{\mathsf T}v)^2=\frac{\|v\|^2}{d},\qquad
\mathbb E(U^{\mathsf T}v)^4=\frac{3\|v\|^4}{d(d+2)}.
\]
To verify the second identity from first principles, let \(a=\mathbb EU_1^4\) and \(b=\mathbb EU_1^2U_2^2\). Uniform spherical rotation by 45 degrees in the first two coordinates yields \(a=3b\); squaring \(\sum_iU_i^2=1\) yields \(da+d(d-1)b=1\). Hence \(a=3/[d(d+2)]\).

For synchronous copies driven by identical \((U,Y)\), the difference after one step is \(P_U(x-x')\), so
\[
\mathbb E\|P_U(x-x')\|^4=\alpha_d\|x-x'\|^4,
\quad \alpha_d=1-\frac2d+\frac{3}{d(d+2)}
=\frac{d^2-1}{d(d+2)}<1.
\]
The Markov operator is therefore a strict contraction on the complete space of probability laws with finite fourth moment under \(W_4\), with factor \(\alpha_d^{1/4}\), and maps that space into itself. Banach's contraction principle supplies a unique finite-fourth-moment invariant law and convergence to it. Rotating the transition preserves its law, so uniqueness makes the invariant law rotationally invariant. Its mean is zero.

Orthogonality gives the *exact* pathwise identity
\[
\|P_U X+YU\|^2=\|P_U X\|^2+Y^2.
\]
In stationarity, if \(M_2=\mathbb E\|X\|^2\), then \(M_2=(1-1/d)M_2+\sigma^2\), so \(M_2=d\sigma^2\). Rotational invariance then gives \(\operatorname{Cov}(X)=\sigma^2I_d\).

Squaring the same orthogonal decomposition, independence of \(Y\), and the spherical fourth moments yield, for \(M_4=\mathbb E\|X\|^4\),
\[
M_4=\alpha_dM_4+2\sigma^2\frac{d-1}{d}M_2+\mu_4,
\]
\[
M_4=\frac{d(d+2)}{2d+1}\bigl(2(d-1)\sigma^4+\mu_4\bigr).
\]
For a rotationally invariant vector, \(\mathbb E(e^{\mathsf T}X)^4=3M_4/[d(d+2)]\); substituting the preceding identity gives exactly the boxed fourth-moment formula. Dividing the resulting fourth cumulant by the stationary variance squared \(\sigma^4\) gives the excess-kurtosis statement.

Finally, \(\mathbb E U=0\), \(\mathbb E UU^{\mathsf T}=I_d/d\), and independence of \(U,Y\) give
\[
\mathbb E[X_{n+1}\mid X_n]=(1-1/d)X_n.
\]
Iterated conditional expectation yields \(\mathbb E[X_{n+k}\mid X_n]=(1-1/d)^kX_n\). Combining this with stationary covariance proves the lag law. Direct summation gives
\[
N^2\operatorname{Var}(\overline Z_N)
=\sigma^2\left[N+2\sum_{k=1}^{N-1}(N-k)(1-1/d)^k\right].
\]
Divide by \(N\), use convergence of the geometric series, and obtain \(\sigma^2[1+2(d-1)]=\sigma^2(2d-1)\).

## Verification

Run `python verification/verify.py` after installing `verification/requirements.txt`. The standalone verifier checks the spherical moment and fourth-moment identities using exact rational arithmetic for every \(2\le d\le128\), several noise fourth moments, and the finite-sample covariance sum in dimensions \(2\) through \(50\). Fixed-seed sample paths with two discrete response laws and dimensions \(2\) and \(5\) check the variance, fourth moment, and lag-one covariance numerically. It reports 1,068 successful check groups. The analytic proof, not these finite checks, establishes all-dimensional and stationary conclusions.

For fair sign responses \(Y=\pm1\), the formula gives stationary coordinate fourth moment \(3-6/(2d+1)\). For the sparse law \(Y=\pm\sqrt5\) with probability \(1/10\) each and zero otherwise, it gives \(3+6/(2d+1)\). Both have unit second moment, yet opposite fourth-cumulant signs and the *same* lag covariance sequence.

## Relationship to prior work

Bergou, Boucherouite, Dutta, Li, and Ma (2023), arXiv:2308.16904, analyze randomized Kaczmarz on a *fixed* doubly noisy coefficient matrix with a fixed perturbed right-hand side, obtaining mean-square convergence-horizon bounds. Their Theorem 3.1 does not yield the stationary fourth-moment identity for an independently re-drawn isotropic row and response at every update. The distinction between fixed data perturbation and renewed noise is essential.

Gower and Richtárik (2015), arXiv:1506.03296, develop sketch-and-project and Gaussian Kaczmarz, including the known isotropic mean-square contraction \(1-1/d\). This known contraction is used, not claimed as new. Their Gaussian Kaczmarz analysis concerns consistent fixed systems and does not specify the invariant fourth cumulant under independent non-Gaussian response replacement. Agaskar, Wang, and Lu (2014) present exact mean-square error and sampling analysis for randomized Kaczmarz, but the accessible abstract does not establish or exclude coverage of the higher stationary moment; its OA PDF could not be accessed for a full comparison in this round. Existing probability/thermostat terminology may contain an equivalent fourth-moment closure, so publication priority is not independently certified.

## Limitations

This is an exact result for a Haar-uniform *fresh* row and an independent freshly drawn response. Neither general row anisotropy nor frozen noisy matrices are covered. Fourth-kurtosis attenuation is not a proof of total-variation or weak convergence to Gaussian as \(d\to\infty\); response distributions with vanishing fourth cumulant may still be non-Gaussian. The stationary sample-mean variance formula does not by itself assert a central limit theorem. The proof assumes finite fourth moment of the response; external independent scientific audit has not been performed.

## References

1. E. H. Bergou, S. Boucherouite, A. Dutta, X. Li, and A. Ma. *A Note on Randomized Kaczmarz Algorithm for Solving Doubly-Noisy Linear Systems*. arXiv:2308.16904v1 (first public 2023-08-31). https://arxiv.org/abs/2308.16904
2. R. M. Gower and P. Richtárik. *Randomized Iterative Methods for Linear Systems*. SIAM Journal on Matrix Analysis and Applications 36 (2015), 1660–1690. First preprint arXiv:1506.03296, https://arxiv.org/html/1506.03296v5
3. A. Agaskar, C. Wang, and Y. Lu. *Randomized Kaczmarz Algorithms: Exact MSE Analysis and Optimal Sampling Probabilities*. GlobalSIP (2014), pp. 389–393. https://dash.harvard.edu/entities/publication/73120379-2750-6bd4-e053-0100007fdf3b
4. D. Needell. *Randomized Kaczmarz Solver for Noisy Linear Systems*. BIT Numerical Mathematics 50 (2010), 395–403. https://doi.org/10.1007/s10543-010-0265-5
