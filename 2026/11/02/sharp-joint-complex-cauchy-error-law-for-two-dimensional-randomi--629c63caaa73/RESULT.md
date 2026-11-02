# Sharp joint complex-Cauchy error law for two-dimensional randomized Rayleigh–Ritz

## Finding

In the square, complex-Gaussian randomized Rayleigh–Ritz procedure for a two-dimensional trial subspace approaching any simple eigenvector of a Hermitian matrix, the *joint*, properly normalized first-order Ritz-value and Ritz-vector errors have the universal density

\[
 f(x_1,x_2)=\frac{2}{\pi^2(1+|x_1|^2+|x_2|^2)^3},\qquad (x_1,x_2)\in\mathbb C^2.
\]

In particular, their exact joint exceedance probability is

\[
 \Pr\{|X_1|>r,\ |X_2|>t\}=\frac{1}{1+r^2+t^2},\qquad r,t\ge0.
\]

The errors are individually complex-Cauchy but *dependent*. This identifies sharp numerical-reliability constants and an exact simultaneous-failure law beyond separate high-probability bounds. The limits for the angle and the refined Rayleigh quotient follow from the same joint pair.

## Assumptions and scope

Fix an integer \(n\ge3\) and a Hermitian \(A\in\mathbb C^{n\times n}\) with a simple eigenpair \((\lambda,v)\), \(\lambda\in\mathbb R\), \(\|v\|_2=1\). Fix orthonormal vectors \(u,w\in v^\perp\). All three vectors and \(A\) are deterministic. Set \(H=A-\lambda I\), \(a=Hu\), and \(b=Hw\); define

\[
 \tau=\|b\|_2,\quad s=\frac{b^*a}{\tau^2},\quad a_\perp=a-sb,\quad \sigma=\|a_\perp\|_2.
\]

Simplicity of \(\lambda\) implies that \(H\) is invertible on \(v^\perp\), so \(\tau,\sigma>0\). For \(0<\varepsilon<1\) use the orthonormal two-column trial matrix

\[
 W_\varepsilon=\big[\sqrt{1-\varepsilon^2}\,v+\varepsilon u,\ w\big].
\]

Draw one \(\Omega\in\mathbb C^{n\times2}\) with independent standard circular complex-normal entries (each real and imaginary part has variance \(1/2\)) and retain this same realization while \(\varepsilon\downarrow0\). The compressed generalized eigenproblem is

\[
 \Omega^*AW_\varepsilon y=\mu\,\Omega^*W_\varepsilon y.
\]

Almost surely a unique simple eigenvalue branch \(\mu_\varepsilon\to\lambda\) exists for all sufficiently small \(\varepsilon>0\), and its eigenvector can be written \(y_\varepsilon=(1,\beta_\varepsilon)^T\). Define finite almost-sure derivatives

\[
 M=\lim_{\varepsilon\downarrow0}\frac{\mu_\varepsilon-\lambda}{\varepsilon},\qquad
 B=\lim_{\varepsilon\downarrow0}\frac{\beta_\varepsilon}{\varepsilon},
\]

and \(X_1=-M/\sigma\), \(X_2=\tau(B+s)/\sigma\). Then the joint density above holds. Each coordinate has density \(\pi^{-1}(1+|z|^2)^{-2}\) on \(\mathbb C\) and satisfies \(\Pr(|X_j|>r)=(1+r^2)^{-1}\). The squared joint radius has tail

\[
 \Pr(|X_1|^2+|X_2|^2>t)=\frac{1+2t}{(1+t)^2},\qquad t\ge0.
\]

Writing \(\theta_\varepsilon=\angle(v,W_\varepsilon y_\varepsilon)\) and \(\rho_\varepsilon=(W_\varepsilon y_\varepsilon)^*A(W_\varepsilon y_\varepsilon)/\|W_\varepsilon y_\varepsilon\|_2^2\), the same coupling implies

\[
 \lim_{\varepsilon\downarrow0}\frac{\theta_\varepsilon}{\varepsilon}=\sqrt{1+|B|^2},\quad
 \lim_{\varepsilon\downarrow0}\frac{\rho_\varepsilon-\lambda}{\varepsilon^2}=(u+Bw)^*H(u+Bw).
\]

For the interior-eigenvalue example \(A=\operatorname{diag}(-1,0,1)\), \(v=e_2\), \(u=(e_1+e_3)/\sqrt2\), \(w=(e_1-e_3)/\sqrt2\), one has \(\lambda=s=0\) and \(\sigma=\tau=1\). The three sharp marginal tails therefore are

\[
 \begin{aligned}
 \Pr(|M|>r)&=\frac{1}{1+r^2}, &&r\ge0,\\
 \Pr(\sqrt{1+|B|^2}>t)&=t^{-2}, &&t\ge1,\\
 \Pr(|-2\operatorname{Re}B|>t)&=1-\frac{t}{\sqrt{t^2+4}}, &&t\ge0.
 \end{aligned}
\]

The limiting normalized Ritz-value error, centered vector coefficient, and angle coefficient have finite absolute moments exactly for orders \(0<p<2\); the refined coefficient in this example has the same threshold. These moment statements apply to the *limiting coefficients*, not to bounded finite-\(\varepsilon\) angle or Rayleigh-quotient random variables.

## Proof

**Local branch.** At \(\varepsilon=0\), the two columns of \(\Omega^*HW_0\) are \(0\) and \(\Omega^*b\). The derivative of the characteristic determinant with respect to \(\mu\) at \((\lambda,0)\) is \(-\det[\Omega^*v,\Omega^*b]\), nonzero almost surely: \(v\perp b\), \(b\ne0\), and independent nondegenerate complex-Gaussian columns have a nonsingular square matrix almost surely. The analytic implicit-function theorem furnishes the claimed simple eigenbranch; its eigenvector has first coordinate nonzero near zero. The derivatives \(M\) and \(B\) exist almost surely.

**First-order equation.** Differentiating the compressed pencil at \(\varepsilon=0\) gives exactly

\[
 \Omega^*\big(a-Mv+Bb\big)=0.
\]

Since \(a=sb+\sigma r\) with \(r=a_\perp/\sigma\) a unit vector perpendicular to both \(v\) and \(b\), the three vectors \(v,b/\tau,r\) are orthonormal. Consequently

\[
 G=\big[\Omega^*v,\Omega^*(b/\tau)\big],\qquad h=\Omega^*r
\]

have independent standard complex-Gaussian columns; \(G\) is a complex \(2\times2\) Ginibre matrix and \(h\in\mathbb C^2\) is independent of \(G\). Rearrangement of the derivative equation yields the exact joint representation

\[
 X=\binom{X_1}{X_2}=-G^{-1}h.
\]

**Density and sharp tails.** For a fixed \(x\in\mathbb C^2\), make the change of variables \(h=-Gx\). Its real four-dimensional Jacobian is \(|\det G|^2\). With \(D=I_2+xx^*\), right-multiply \(G\) by \(D^{1/2}\). The four complex coordinates contribute a Jacobian \(\det(D)^{-2}\), and the determinant factor contributes \(\det(D)^{-1}\). The standard complex-Gaussian normalization and \(\mathbb E|\det G|^2=2\) give

\[
 f(x)=\frac{\mathbb E|\det G|^2}{\pi^2\det(I_2+xx^*)^3}
      =\frac{2}{\pi^2(1+\|x\|_2^2)^3}.
\]

For \(S=|X_1|^2\) and \(T=|X_2|^2\), polar integration shows that their joint density on the positive quadrant is \(2(1+S+T)^{-3}\). Integrating over \(S>r^2\), \(T>t^2\) gives \((1+r^2+t^2)^{-1}\). Integrating one coordinate gives the asserted complex-Cauchy marginal, and integrating over \(S+T>t\) gives \((1+2t)/(1+t)^2\). At equal thresholds \(r=t=1\) the simultaneous exceedance probability is \(1/3\), rather than the independent-product value \(1/4\).

**Vector angle and refined quotient.** Orthogonality of \(v,u,w\) and \(W_\varepsilon^*W_\varepsilon=I_2\) imply the exact identities

\[
 \sin^2\theta_\varepsilon=\frac{\varepsilon^2+|\beta_\varepsilon|^2}{1+|\beta_\varepsilon|^2},\qquad
 \rho_\varepsilon-\lambda=\frac{\varepsilon^2\,(u+(\beta_\varepsilon/\varepsilon)w)^*H(u+(\beta_\varepsilon/\varepsilon)w)}{1+|\beta_\varepsilon|^2}.
\]

Divide by the indicated powers of \(\varepsilon\) and use \(\beta_\varepsilon/\varepsilon\to B\). In the specific three-dimensional example, \(Hu=-w\) and \(Hw=-u\), whence the refined coefficient is \(-2\operatorname{Re}B\). Integrating the circular complex-Cauchy marginal over its imaginary coordinate gives the real density \(\{2(1+x^2)^{3/2}\}^{-1}\), and then its two-sided tail is \(1-t/\sqrt{t^2+4}\). The same complex-Cauchy tail establishes the stated moment boundary. This completes the proof.

## Verification

The standalone `VERIFY.py` uses deterministic seed 20261025 and independently compares the first-order derivatives with direct generalized-eigenvalue calculations for a Hermitian three-mode example and rotated four-mode examples having nonzero complex coupling \(s\). It also samples the joint Gaussian ratio to compare marginals, simultaneous exceedance events, refined coefficients, and joint-radius tails against the analytical laws. Run `python VERIFY.py` with Python, NumPy and SciPy installed. Numerical experiments are supporting checks, not a replacement for the all-dimensional probability-density proof.

## Relationship to prior work

Nian Shao's randomized Rayleigh–Ritz framework (arXiv:2604.01037, initial public version April 1, 2026, especially Example 1, Algorithm 1, Theorems 2–3, and the failure-probability experiment) proves non-asymptotic high-probability rates for simple eigenpairs and a quadratic refined Rayleigh quotient for Hermitian problems. The present result does **not** claim novelty for those rates or for the use of random Gaussian pencils. It identifies their exact two-mode first-order *joint* error distribution, with a sharp parameter-dependent centering and scaling and explicit simultaneous extreme-event probabilities. The proof specializes a standard complex-Gaussian inverse-ratio mechanism to the algorithm's perturbation equation.

Nakatsukasa and Tropp's earlier sketched Rayleigh–Ritz framework (arXiv:2111.00113, §§1.3 and 6) develops fast subspace embeddings and algorithms. That setting and its guarantees do not state the two-mode first-order joint complex-Cauchy law. The known use of Gaussian ratios and complex matrix-variate Cauchy densities is acknowledged as the probabilistic ingredient; historical-priority uncertainty remains regarding any prior numerical-eigenpair formulation of this exact identity.

## Limitations

Only simple Hermitian eigenpairs, fixed two-dimensional trial subspaces of the specified form, square independent complex-Gaussian compression, exact arithmetic, and the \(\varepsilon\downarrow0\) limit are covered. Real-Gaussian sketches, oversampling, higher-dimensional trial subspaces, nonnormal problems, and uniform finite-tolerance bounds are not established here. No independent mathematical audit has been performed. Failure to identify an earlier identical law in the checked sources is not a proof of historical priority.

## References

1. Nian Shao, *Stabilizing the Rayleigh–Ritz procedure by randomization*, arXiv:2604.01037v1 (April 1, 2026), v3 (September 8, 2026). https://arxiv.org/html/2604.01037v3
2. Yuji Nakatsukasa and Joel A. Tropp, *Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, arXiv:2111.00113v2 (2022). https://arxiv.org/html/2111.00113v2
