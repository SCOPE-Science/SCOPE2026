# Sharp positivity budgets and inverse-gap moment barrier for Gaussian-sketched Ritz shifts

## Finding
Let \(A\in\mathbb R^{n\times n}\) be symmetric positive definite with at least two distinct eigenvalues, let \(u\ne0\) be deterministic and not an eigenvector, and let \(S\in\mathbb R^{s\times n}\) have independent \(N(0,1/s)\) entries for a finite integer \(s\ge2\). Define the one-direction sketched Galerkin Ritz shift
\[
\widehat\theta=\frac{(Su)^{\mathsf T}(SAu)}{\|Su\|_2^2},\qquad
\mu=\frac{u^{\mathsf T}Au}{u^{\mathsf T}u},\qquad
\sigma^2=\frac{u^{\mathsf T}A^2u}{u^{\mathsf T}u}-\mu^2>0.
\]
Then, with \(T_s\) a standard Student random variable with \(s\) degrees of freedom,
\[
\boxed{\widehat\theta\ \stackrel{\mathrm d}=\ \mu+\frac{\sigma}{\sqrt{s}}T_s},
\quad
f_{s,\mu,\sigma}(x)=\frac{\Gamma((s+1)/2)\sigma^s}{\sqrt\pi\,\Gamma(s/2)[\sigma^2+(x-\mu)^2]^{(s+1)/2}}.
\]
For every prescribed spectral ratio \(\kappa>1\), the sharp supremum, over all real positive-definite matrices with minimum eigenvalue \(m>0\), maximum eigenvalue \(L=m\kappa\), and all fixed noneigenvectors, of the probability that this positive-definite matrix produces a nonpositive sketched Ritz shift is
\[
\boxed{p_s(\kappa)=\frac12 I_{((\kappa-1)/(\kappa+1))^2}\left(\frac{s}{2},\frac12\right)},
\]
where \(I\) is the regularized incomplete beta function. Every \(\kappa>1\) and integer \(s\ge2\) attains this bound in dimension two. Its sharp large-sketch asymptotic is
\[
p_s(\kappa)\sim \frac{\kappa+1}{2\sqrt{2\pi s\kappa}}\left(\frac{\kappa-1}{\kappa+1}\right)^s\qquad(s\to\infty,\ \kappa\text{ fixed}>1).
\]
Let \(s_\delta(\kappa)\) be the least integer \(s\ge2\) such that \(p_s(\kappa)\le\delta\). Then, for \(0<\delta<1/2\),
\[
\boxed{\lim_{\delta\downarrow0}\frac{s_\delta(\kappa)}{\log(1/\delta)}=\frac{1}{\log((\kappa+1)/(\kappa-1))}},\quad
\boxed{\lim_{\kappa\to\infty}\frac{s_\delta(\kappa)}{\kappa}=\frac{[\Phi^{-1}(1-\delta)]^2}{4}}.
\]
Most notably, let \(\Lambda\) be the set of distinct eigenvalues of \(A\) and let
\[
K=\kappa_2(A-\widehat\theta I)=\frac{\max_{\lambda\in\Lambda}|\lambda-\widehat\theta|}{\min_{\lambda\in\Lambda}|\lambda-\widehat\theta|}
\]
(which is finite almost surely). **For every finite sketch dimension**, its absolute moments satisfy
\[
\boxed{\mathbb E[K^p]<\infty\ \Longleftrightarrow\ 0<p<1}.
\]
For the spectral-gap safeguard \(h>0\), define
\[
K_h=\frac{\max_{\lambda\in\Lambda}|\lambda-\widehat\theta|}{\max\{h,\min_{\lambda\in\Lambda}|\lambda-\widehat\theta|\}}.
\]
Its regularized mean diverges at the exact logarithmic rate
\[
\boxed{\mathbb E[K_h]=2\sum_{\lambda\in\Lambda}d_\lambda f_{s,\mu,\sigma}(\lambda)\log(1/h)+O(1)},\quad
 d_\lambda=\max_{\nu\in\Lambda}|\nu-\lambda|>0,
\]
as \(h\downarrow0\), with \(A,S,u\) otherwise fixed. Thus increasing a **finite** sketch width can reduce the probability of a nonpositive Ritz value exponentially without making the expected condition number of the resulting shift-invert matrix finite.

## Assumptions and scope
The direction \(u\) is chosen independently of \(S\); this statement does not apply to sketch-adaptive directions. All matrices, sketches, shifts and eigenvalues are real. The rank-one quotient is the eigenvalue of the sketched one-dimensional Galerkin pencil \((Su)^{\mathsf T}S(A-\theta I)u\), not the true Rayleigh quotient and not the harmonic or refined Ritz quotient. Invertibility of the shifted matrix holds almost surely because the shift density is continuous. The condition number is the exact spectral 2-norm condition number of the **full** shifted operator, not the condition of a computed Krylov basis or a claim about elapsed algorithmic time. In the sharp positivity assertion \(m,L\) are the actual least and greatest eigenvalues; the same sharp bound holds if they are only spectral enclosures. No eigenvector case (\(\sigma=0\)) is claimed.

## Proof
**1. Exact sketched law.** Set \(v=(Au-\mu u)/(\sigma\|u\|_2)\). Then \(u/\|u\|_2\) and \(v\) are orthonormal, so \(g=\sqrt s\,Su/\|u\|_2\) and \(h=\sqrt s\,Sv\) are independent standard normal vectors in \(\mathbb R^s\). The quotient reduces exactly to \(\widehat\theta=\mu+\sigma(g^{\mathsf T}h)/(g^{\mathsf T}g)\). Conditional on \(g\), the normalized numerator \(g^{\mathsf T}h/\|g\|_2\) is standard normal with a conditional law independent of \(g\); hence it is independent of \(\|g\|_2^2\sim\chi_s^2\). This proves the Student law and density by the Gaussian/chi-square representation, including every scale factor.

**2. Sharp positivity envelope.** With \(m\le\lambda\le L\), the elementary pointwise inequality \(\lambda^2\le(m+L)\lambda-mL\) implies \(\sigma^2\le(m+L)\mu-mL-\mu^2\). Maximizing \(\sigma^2/\mu^2\) over \(m\le\mu\le L\) gives \((L-m)^2/(4mL)\), uniquely at \(\mu=2mL/(m+L)\). Equality uses only eigenvalues \(m,L\), with squared weights \(L/(m+L)\) and \(m/(m+L)\). The Student tail identity \(\Pr(T_s\le-t)=\tfrac12 I_{s/(s+t^2)}(s/2,1/2)\) for \(t>0\) yields the announced probability and two-dimensional sharpness.

**3. Exact budgets.** Let \(r=(\kappa-1)/(\kappa+1)\in(0,1)\). The beta integral at a fixed upper endpoint, combined with \(\Gamma(a+1/2)/\Gamma(a)\sim\sqrt a\), gives \(\tfrac12 I_{r^2}(s/2,1/2)\sim r^s/[\sqrt{2\pi s}\sqrt{1-r^2}]\). Since \(\sqrt{1-r^2}=2\sqrt\kappa/(\kappa+1)\), this is the stated prefactor. The beta laws \(\operatorname{Beta}(s/2,1/2)\) increase strictly in stochastic order as \(s\) increases, so \(p_s\) decreases and a smallest admissible \(s\) exists. Taking logarithms proves the small-failure budget. For fixed \(0<\delta<1/2\), take \(s/\kappa\to c\in(0,\infty)\). The exact Student expression is \(p_s(\kappa)=\Pr(T_s\le-2\sqrt{s\kappa}/(\kappa-1))\to\Phi(-2\sqrt c)\). Strict monotonicity and squeezing between two such ratios establish the second budget limit.

**4. Sharp inverse-gap moments.** For any \(\lambda\in\Lambda\), distinctness gives \(d_\lambda>0\). In a sufficiently short interval around \(\lambda\), the unique nearest eigenvalue is \(\lambda\) and the continuous numerator \(\max_{\nu\in\Lambda}|\nu-x|\) is \(d_\lambda+O(|x-\lambda|)\). Since the density is smooth and strictly positive at \(\lambda\), \(\mathbb E K^p\) has precisely the same local integrability as \(\int_0^\epsilon t^{-p}\,dt\). Away from all eigenvalues the ratio is bounded, including at infinity, proving the if-and-only-if statement. The regularized local contribution is \(2d_\lambda f(\lambda)\int_0^\epsilon dt/\max(h,t)=2d_\lambda f(\lambda)\log(1/h)+O(1)\). Lipschitz estimates for the numerator and density control the remainder; other regions contribute \(O(1)\). Summing over distinct eigenvalues proves the exact coefficient.

## Verification
Run `python verify.py` after installing the two dependencies listed in `requirements.txt`. The bundled script uses exact rational arithmetic for the extremal two-eigenvalue configuration, independently computes Student and regularized beta tails, tests the gamma-normalized density, reconstructs Gaussian sketches directly rather than sampling a precomputed Student variable, compares the large-sketch and large-condition-number budgets, and independently numerically integrates the safeguarded inverse-gap condition number. It returned `VERIFY_OK` for 74 numerical/algebraic checks. These finite checks do **not** certify all-parameter inequalities or asymptotic limits; the foregoing proof supplies them. For an exact check at \(A=\operatorname{diag}(1,9)\), \(u=(3,1)^{\mathsf T}/\sqrt{10}\) and \(s=2\), the probability of a nonpositive sketched shift is \(1/5\).

## Relationship to prior work
Grigori, Park and Simunec (2026, arXiv:2609.29651v1) define randomized Jacobi–Davidson and its sketched Rayleigh–Ritz extraction and investigate convergence under embedding/separation hypotheses. Shao (2026, arXiv:2604.01037v3), particularly Sections 4.2–4.3, proves high-probability condition-number bounds for a **different, square complex-Gaussian Petrov–Galerkin pencil** and discusses subsequent unsketched Rayleigh refinement. Nakatsukasa and Tropp (2021, arXiv:2111.00113v2, Section 6.8) examine stability issues for randomized projected eigenvalue calculations. Those results do not directly give the distribution, sharp SPD positivity envelope or regularized inverse-gap coefficient for the present fixed-direction **tall real-Gaussian, two-sided sketched quotient**. The Student representation and elementary spectral-interval inequality are classical ingredients, not individually asserted to be new. A failure to locate another equivalent derivation is not a proof of novelty.

## Limitations
This is one fixed direction and one independent Gaussian sketch, not a uniform statement over an adaptive Krylov subspace. It applies to exactly shifted full matrices and not to finite-precision numerical conditioning, total algorithm cost or practical safeguarding guarantees. No conclusions are claimed for CountSketch, SRHT, complex Gaussian sketch distributions, harmonic shifts, or nonlinear eigenproblems. The expected-condition divergence may coexist with extremely small failure probabilities and hence does not imply typical numerical failure.

## References
1. L. Grigori, T. Park, I. Simunec, “Randomized Jacobi-Davidson method,” arXiv:2609.29651v1 (first submitted 2026-09-01), https://arxiv.org/abs/2609.29651.
2. N. Shao, “Stabilizing the Rayleigh–Ritz procedure by randomization,” arXiv:2604.01037v3 (first submitted 2026-04-01), https://arxiv.org/abs/2604.01037.
3. Y. Nakatsukasa and J. A. Tropp, “Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems,” arXiv:2111.00113v2 (2021 first submission), https://arxiv.org/abs/2111.00113.
4. Student's \(t\)-distribution and the regularized incomplete beta identity (standard distribution theory).
