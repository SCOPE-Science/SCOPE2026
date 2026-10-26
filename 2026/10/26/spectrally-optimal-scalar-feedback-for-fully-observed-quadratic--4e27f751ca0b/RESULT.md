# Spectrally optimal scalar feedback for fully observed quadratic control

## Finding

**Theorem.** Let \(A\in\mathbb R^{n\times n}\) be real symmetric and positive semidefinite, with \(n\ge2\) and distinct extremal eigenvalues \(0\le a=\lambda_{\min}(A)<b=\lambda_{\max}(A)\). Fix \(\alpha>0\). For \(k>0\), put

\[
H_k=(A+kI)^{-1}(I+\alpha A^2)(A+kI)^{-1},\qquad
w_t=\sqrt{1+\alpha t^2}.
\]

The spectral condition number \(\kappa_2(H_k)\) has exactly one minimizer over all \(k>0\):

\[
k_* = \frac{w_a+w_b}{\alpha(bw_a+aw_b)}.
\]

Define \(c_*=1/(\alpha k_*)=(bw_a+aw_b)/(w_a+w_b)\), which lies strictly between \(a\) and \(b\). At the optimum the two endpoint Hessian eigenvalues coincide. For every permitted matrix,

\[
1\le\kappa_2(H_{k_*})
=\frac{(1+\alpha a^2)/(a+k_*)^2}
{\min_{\lambda\in\sigma(A)}(1+\alpha\lambda^2)/(\lambda+k_*)^2}
\le\sec^2\!\left(\frac{\arctan(\sqrt\alpha b)-\arctan(\sqrt\alpha a)}2\right)<2.
\]

The upper bound is **sharp at each fixed pair of endpoints**: the diagonal matrix with spectrum \(\{a,c_*,b\}\) attains it. Conversely, a matrix with spectrum \(\{a,b\}\) has condition number exactly one at \(k_*\). The classical matched gain \(k=1/\sqrt\alpha\) equals \(k_*\) if and only if \(\alpha ab=1\).

## Assumptions and scope

Consider arbitrary vectors \(f,x_d\in\mathbb R^n\) and the finite-dimensional linear-quadratic problem

\[
\min_{x,u}\ \tfrac12\|x-x_d\|_2^2+\tfrac\alpha2\|u\|_2^2
\quad\text{subject to}\quad Ax-u=f.
\]

Use full state observation, full distributed control, Euclidean norms and a common scalar feedback \(u=v-kx\) with \(k>0\). The map \(v\mapsto x=(A+kI)^{-1}(v+f)\) is a bijection onto feasible state/control pairs, including for singular \(A\). Since \(u=v-kx\), the derivative of the original control with respect to \(v\) is \(A(A+kI)^{-1}\). Therefore the transformed reduced Hessian is precisely \(H_k\) above. The result concerns this Hessian, not a nonnormal state operator or a general matrix-valued feedback.

## Proof

**1. Exact scalar eigenvalues and endpoint maxima.** Orthogonal diagonalization yields eigenvalues

\[
h_k(t)=\frac{1+\alpha t^2}{(t+k)^2}=g_k(t)^2,\qquad
 g_k(t)=\frac{\sqrt{1+\alpha t^2}}{t+k},\quad t\in\sigma(A).
\]

For every \(k>0\), differentiation on the nonnegative half-line gives

\[
g_k'(t)=\frac{\alpha kt-1}{\sqrt{1+\alpha t^2}\,(t+k)^2}.
\]

Thus \(g_k\) first decreases and then increases, with its unique minimum at \(t=1/(\alpha k)\). Its maximum on \([a,b]\), and hence on the finite spectrum containing both endpoints, occurs at \(a\) or \(b\).

**2. Uniqueness of the optimal feedback.** The endpoint ratio is

\[
\frac{g_k(a)}{g_k(b)}=\frac{w_a}{w_b}\,\frac{b+k}{a+k}.
\]

It decreases strictly with \(k\), starts above one as \(k\downarrow0\) (also when \(a=0\)), and tends to \(w_a/w_b<1\) as \(k\to\infty\). Its unique equality point is the displayed \(k_*\). Indeed, the equality equation gives \(k_*=(bw_a-aw_b)/(w_b-w_a)\), and rationalizing with \(w_b^2-w_a^2=\alpha(b^2-a^2)\) yields the stated stable positive formula.

For any \(0<k<k_*\), the largest scalar eigenvalue is \(g_k(a)^2\). For each spectral value \(t>a\), the ratio

\[
\frac{g_k(a)}{g_k(t)}=\frac{w_a}{w_t}\,\frac{t+k}{a+k}
\]

is strictly decreasing in \(k\). The maximum over the finitely many nontrivial ratios, which equals \(\sqrt{\kappa_2(H_k)}\), is therefore strictly decreasing. For \(k>k_*\), the largest scalar eigenvalue is \(g_k(b)^2\), and every nontrivial ratio \(g_k(b)/g_k(t)=(w_b/w_t)(t+k)/(b+k)\), \(t<b\), is strictly increasing. Thus the condition number decreases strictly before \(k_*\) and increases strictly afterward: \(k_*\) is its unique global minimizer.

**3. Sharp finite-spectrum envelope.** Set \(\theta_t=\arctan(\sqrt\alpha\,t)\) and \(\phi=\arctan(\sqrt\alpha\,k_*)\). One has the exact identity

\[
g_{k_*}(t)=\frac{\sqrt\alpha}{\sqrt{1+\alpha k_*^2}\,\sin(\theta_t+\phi)}.
\]

The equality \(g_{k_*}(a)=g_{k_*}(b)\) forces
\(2\phi+\theta_a+\theta_b=\pi\), since both angles \(\theta_a+\phi\) and \(\theta_b+\phi\) lie in \((0,\pi)\). Hence the endpoint sine equals \(\cos((\theta_b-\theta_a)/2)\), while the maximum sine on the intervening angle interval is one, attained at \(\theta_{c_*}=(\theta_a+\theta_b)/2\). Consequently the ratio of the squared endpoint maximum to the continuous-interval minimum equals precisely

\[
\sec^2\!\left(\tfrac12(\theta_b-\theta_a)\right).
\]

Minimizing over a finite subset can only increase the denominator relative to the interval minimum, proving the inequality. Including \(c_*\) as a third eigenvalue realizes equality; omitting all interior eigenvalues gives the two-point equality \(\kappa_2(H_{k_*})=1\). Because \(0\le\theta_a<\theta_b<\pi/2\), the universal upper bound is strictly below two.

**4. Exact condition for the standard matched shift.** The equation \(k_*=1/\sqrt\alpha\) is equivalent to \(\phi=\pi/4\), or \(\theta_a+\theta_b=\pi/2\), which for positive \(b\) and nonnegative \(a\) is equivalent to \(\alpha ab=1\). This completes the proof.

## Verification

The included standalone `verify_feedback_shift.py` evaluates the closed-form gain, its extremizing interior eigenvalue, endpoint equality, the sharp envelope and strict off-optimum comparisons, for seven parameter combinations (including a zero eigenvalue). It additionally tests 500 deterministic pseudo-random finite spectra. Run with Python 3 and no third-party packages; the recorded output is `verification_output.txt`. These finite computations serve only as diagnostics: the derivative, monotonicity, and angle identities above establish the all-dimensions theorem.

As a concrete singular example, \(\alpha=1\), \(a=0\), \(b=3\) give \(k_*\approx1.38742588672\), \(c_*\approx0.72075922006\), and a sharp optimal condition number \(1.51949385330\). For the same three-eigenvalue matrix, the classical matched gain \(k=1\) gives approximately \(1.94868329805\). The respective values follow directly by evaluating the displayed eigenvalue formula.

## Relationship to prior work

Preuster, Schaller, Schiela and Stoll (2026), Section 3.1 and the elliptic example in Section 4.2, derive a general condition-number **bound** under feedback transformations and optimize that bound in a limiting Neumann example; their estimate is not the exact scalar spectral minimizer above. The feedback/reduced-Hessian equivalence used here is consistent with their formulation.

Pearson and Wathen (2012) introduce a matching-style Schur-complement preconditioner, and Wang, Chen and Sun (2023), Section 2, explicitly write its shift as the regularization-determined matched value and its spectral containment in \([1/2,1]\). Those results already yield a uniform factor-two-type bound for the corresponding commuting/whitened model and are **not** claimed as new. The additional assertions here are uniqueness of the optimal freely tuned scalar gain for every given spectrum, its endpoint formula, the strict optimality criterion versus the matched shift, and the sharp endpoint-angle envelope with equality examples. No claim of uniqueness relative to all conceivable external publications is made.

## Limitations

The theorem requires a real symmetric positive semidefinite matrix, full observation/control and Euclidean coefficient spaces. Arbitrary finite-element mass matrices, nonsymmetric convection, partial observations, general feedback operators and floating-point application costs are outside its scope. Only the conditioning of the transformed reduced Hessian is optimized, not the total cost of state solves. The classical matched-preconditioner literature may contain an equivalent optimal-shift parameterization under different terminology; the full older Pearson–Wathen article was not accessible during the literature comparison. Independent validation has not been carried out.

## References

1. T. Preuster, M. Schaller, A. Schiela, M. Stoll, *Stabilize-then-optimize: Feedback transformations as preconditioners in optimal control*, arXiv:2607.11835v1 (first public 13 July 2026), https://arxiv.org/abs/2607.11835.
2. C. Wang, J. Chen, S. Sun, *A Matching-Strategy-Inspired Preconditioning for Elliptic Optimal Control Problems*, Mathematics 11 (2023), 2599, https://doi.org/10.3390/math11122599.
3. J. W. Pearson, A. J. Wathen, *A new approximation of the Schur complement in preconditioners for PDE-constrained optimization*, Numer. Linear Algebra Appl. 19 (2012), 816–829, https://doi.org/10.1002/nla.814.
