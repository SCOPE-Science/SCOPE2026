# An exact Gaussian positivity threshold for two-mode sketched harmonic Ritz extraction

## Finding
Let \(A\) be any real symmetric positive-definite matrix possessing orthonormal eigenvectors \(v_{\mu},v_L\) for distinct eigenvalues \(0<\mu<L\). Fix their invariant plane \(E=\operatorname{span}\{v_{\mu},v_L\}\) and write \(\kappa=L/\mu>1\). Let \(S\) have \(s\ge2\) rows of independent real \(N(0,1/s)\) entries. For \(b\in E\setminus\{0\}\), the one-dimensional sketched harmonic Ritz value from the Petrov--Galerkin pencil is
\[
\theta_S(b)=\frac{\|SAb\|_2^2}{(SAb)^{\mathsf T}(Sb)}.
\]
For a single shared sketch, define the **uniform positive-harmonic event** \(\mathcal P_S=\{\theta_S(b)\text{ is defined and positive for every }0\ne b\in E\}\). Its exact probability is
\[
\boxed{\mathbb P(\mathcal P_S)=I_{4\kappa/(\kappa+1)^2}\left(\tfrac12,\tfrac{s-1}{2}\right)},
\]
where \(I_z(a,b)=B_z(a,b)/B(a,b)\) is the regularized incomplete beta function. Outside this event, with probability one there exists a nonzero real \(b\in E\) for which \(\theta_S(b)<0\). This is a **simultaneous, all-starting-directions** statement, rather than a probability bound for a separately fixed \(b\).

For each fixed failure tolerance \(\delta\in(0,1)\), let \(s_\delta(\kappa)\) be the least integer \(s\ge2\) ensuring \(\mathbb P(\mathcal P_S)\ge1-\delta\). It exists, and the sharp large-condition-number sketch budget is
\[
\boxed{\lim_{\kappa\to\infty}\frac{s_\delta(\kappa)}{\kappa}=
\frac{\bigl[\Phi^{-1}(1-\delta/2)\bigr]^2}{4}},
\]
with \(\Phi\) the standard normal cumulative distribution. In particular, uniform two-mode positive-harmonic extraction has a **linear** rather than condition-number-independent Gaussian row budget. For every fixed \(s\ge2\), its success probability vanishes as
\[
\mathbb P(\mathcal P_S)\sim
\frac{4\Gamma(s/2)}{\sqrt\pi\,\Gamma((s-1)/2)}\,\kappa^{-1/2}.
\]
If \(\mu=L\), the event holds almost surely and the formula extends by continuity with probability one.

## Assumptions and scope
All vectors, matrices, and sketches are real; calculations are in exact arithmetic. The plane \(E\) is fixed independently of \(S\). The quantity being protected is positivity for **every vector in this plane using the same sketch**, not positivity over all vectors in the ambient space when its dimension exceeds two. The index \(s\) is any integer at least two, including sketches with more rows than the invariant-plane dimension. The selected harmonic Ritz value corresponds exactly to the one-dimensional sketched harmonic Petrov--Galerkin construction, regardless of the normalization of \(b\).

## Proof
First restrict the sketch to \(E\). By Gaussian orthogonal invariance, the two columns \(U=\sqrt{s}Sv_{\mu}\) and \(V=\sqrt{s}Sv_L\) are independent \(N(0,I_s)\) random vectors. They are linearly independent almost surely when \(s\ge2\); therefore \(\|SAb\|_2>0\) for every nonzero \(b\in E\). In eigen-coordinates \(b=xv_{\mu}+yv_L\), the sign of the denominator is the sign of the quadratic form with symmetric matrix
\[
H=\begin{pmatrix}
\mu\|U\|_2^2&(\mu+L)U^{\mathsf T}V/2\\
(\mu+L)U^{\mathsf T}V/2&L\|V\|_2^2
\end{pmatrix}/s.
\]
Both diagonal entries are strictly positive. By the exact \(2\times2\) Sylvester criterion, \(H\) is positive definite if and only if
\[
\frac{(U^{\mathsf T}V)^2}{\|U\|_2^2\|V\|_2^2}<\frac{4\mu L}{(\mu+L)^2}
=\frac{4\kappa}{(\kappa+1)^2}.
\]
If the inequality reverses strictly, \(\det H<0\) and there is a negative vector; for example, writing \(H=(h_{ij})\) and setting \(b=(-h_{12}/h_{11},1)\) yields \(b^{\mathsf T}Hb=h_{22}-h_{12}^2/h_{11}<0\). Its harmonic Ritz value is negative because the numerator is strictly positive. The equality case has probability zero when \(\mu<L\).

Conditional on the direction of \(U\), rotational invariance makes \(V/\|V\|_2\) uniform on the unit sphere in \(\mathbb R^s\). The squared inner product with a fixed unit vector consequently has distribution \(\mathrm{Beta}(1/2,(s-1)/2)\). The displayed Sylvester criterion thus integrates to the exact regularized beta probability. For \(\mu=L\), \(H=\mu S_E^{\mathsf T}S_E\) is positive definite almost surely.

For \(\kappa>1\), the beta distribution is strictly stochastically decreasing as its second shape parameter grows. Hence the success probability strictly increases with \(s\), and tends to one since the squared random directional cosine has mean \(1/s\). This proves existence of \(s_\delta(\kappa)\). If \(\kappa\to\infty\) and \(s/\kappa\to t\in(0,\infty)\), the spherical-coordinate central limit theorem gives \(\sqrt{s}\,U^{\mathsf T}V/(\|U\|_2\|V\|_2)\Rightarrow N(0,1)\), while the threshold multiplied by \(\sqrt{s}\) tends to \(2\sqrt t\). Therefore
\[
\mathbb P(\mathcal P_S)\longrightarrow 2\Phi(2\sqrt t)-1.
\]
Strict monotonicity in \(s\) sandwiches the smallest acceptable integer row count between any pair of slopes straddling \(\bigl[\Phi^{-1}(1-\delta/2)\bigr]^2/4\), proving its claimed limit. Finally, for fixed \(s\), the beta density at the origin has the integrable square-root singularity \(z^{-1/2}/B(1/2,(s-1)/2)\). As \(4\kappa/(\kappa+1)^2\sim4/\kappa\), integrating this density proves the exact \(\kappa^{-1/2}\) prefactor.

## Verification
The accompanying `verify.py` is executable with Python 3, NumPy, and SciPy: `python verify.py`. It checks 2,480 finite integer-sketch cases using exact rational determinants, constructs 624 explicit negative-harmonic witnesses, checks 1,800 direct Jordan eigensigns, compares the formula against six seeded Gaussian experiments with 50,000 trials each, and checks exact low-row beta identities and numerical limits. The analytic proof, not those finite experiments, establishes the probability for all admissible parameters and the asymptotic limits.

## Relationship to prior work
Güttel, Liu, and Nyman, *Sketch-and-Restart* (arXiv:2607.10354v1, 11 July 2026), Section 2.2 equation (2.13), define the sketched harmonic Petrov--Galerkin extraction; their Section 5 derives convergence conditions requiring the sketched harmonic Ritz spectrum to lie in the right half-plane. Those statements do not provide the exact simultaneous two-mode Gaussian positivity probability or its sharp row-budget constant. Grigori, Kressner, Shao, and Simunec (arXiv:2601.10248v1) instead restore similarity for randomized **ordinary** Arnoldi Ritz extraction. Jang and Grigori (DOI:10.1002/nla.70029), Section 5, discuss harmonic Ritz pairs under randomized reorthogonalization, not this shared-sketch positivity law.

Gaunt (arXiv:2408.04101) analyzes products of correlated Gaussian variables, covering a core distributional ingredient for a **single fixed direction**. The present simultaneous event has the quantifiers in the opposite order: one sketch must work for all starting directions, including a direction dependent on that sketch. The beta law for a Gaussian random spherical cosine and the Sylvester positivity criterion are classical facts, not claimed as new independently.

## Limitations
This is a sharp statement about the positive-real requirement of **one-dimensional** sketched harmonic extraction on a **fixed two-eigenmode plane**, not a convergence theorem for a restarted algorithm. A bad sketch guarantees a negative harmonic Ritz value for some potentially sketch-dependent direction; it does not assert that every independently preselected starting vector fails, or that a particular implementation will encounter that direction. It does not address complex sketches, sparse-sign embeddings, nonnormal operators, longer Krylov bases, floating-point effects, or positivity uniformly over a larger ambient space. Other equivalent treatments of Gaussian Jordan products may exist.

## References
1. S. Güttel, J. Liu, L. Nyman, *Sketch-and-Restart: Randomized Sketching in Quadrature-Based Restarting for Matrix Functions*, arXiv:2607.10354v1 (11 July 2026), https://arxiv.org/pdf/2607.10354.
2. L. Grigori, D. Kressner, N. Shao, I. Simunec, *Restoring Similarity in Randomized Krylov Methods with Applications to Eigenvalue Problems and Matrix Functions*, arXiv:2601.10248v1, https://arxiv.org/pdf/2601.10248.
3. Y. Jang, L. Grigori, *Randomized Orthogonalization Process With Reorthogonalization*, *Numerical Linear Algebra with Applications* (2025), DOI:10.1002/nla.70029, https://doi.org/10.1002/nla.70029.
4. R. E. Gaunt, *On the Product of Correlated Normal Random Variables and the Noncentral Chi-Square Difference Distribution*, arXiv:2408.04101, https://arxiv.org/pdf/2408.04101.
