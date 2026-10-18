# Sharp half-probability spectral-escape barrier for Gaussian-sketched one-dimensional Ritz values

## Finding

For a real symmetric matrix, the ordinary Euclidean one-dimensional Rayleigh quotient lies inside its eigenvalue interval. Its one-dimensional **Gaussian-sketched Rayleigh--Ritz** counterpart need not. The precise escape law is Student, and the sharp escape probability over all starting vectors is \(1/2\) for **every finite sketch dimension**, even when the matrix is positive definite. The bound is achieved for one sketch row and approached, but not attained, for two or more sketch rows.

More precisely, let \(A=A^{\mathsf T}\in\mathbb R^{n\times n}\) with distinct extreme eigenvalues \(m<M\); let \(S\) be an independent real Gaussian \(s\times n\) sketch, \(s\ge1\). For a deterministic nonzero vector \(v\), write
\[
\mu=\frac{v^{\mathsf T}Av}{\|v\|_2^2},\qquad
\sigma=\frac{\|(A-\mu I)v\|_2}{\|v\|_2},\qquad
\widehat\lambda=\frac{(Sv)^{\mathsf T}SAv}{\|Sv\|_2^2}.
\]
When \(\sigma>0\), the **exact law** is
\[
\widehat\lambda\ \overset d=\ \mu+\frac{\sigma}{\sqrt{s}}T_s,\qquad T_s\sim t_s.
\]
Here the law of \(T_s\) is the usual Student law with \(s\) degrees of freedom. In particular, \(\mathbb E|\widehat\lambda-\mu|^q<\infty\) exactly when \(0<q<s\); \(\mathbb E\widehat\lambda=\mu\) when \(s>1\), and \(\operatorname{Var}(\widehat\lambda)=\sigma^2/(s-2)\) when \(s>2\).

For any prescribed interior Rayleigh quotient \(m<\mu<M\), define \(p=(\mu-m)/(M-m)\), and let \(Q_s(x)=\Pr\{Z/\chi_s>x\}\) for independent standard normal \(Z\) and chi variable \(\chi_s\). The **sharp fixed-mean escape envelope** is
\[
\max_{\|v\|_2=1,\ v^{\mathsf T}Av=\mu}
\Pr\{\widehat\lambda\notin[m,M]\}
=F_s(p):=Q_s\!\left(\sqrt{\frac{p}{1-p}}\right)+Q_s\!\left(\sqrt{\frac{1-p}{p}}\right).
\]
Equality holds exactly for vectors having nonzero spectral components only in the eigenspaces of \(m\) and \(M\). For \(s=1\), \(F_1(p)=1/2\) for every \(0<p<1\). For each integer \(s\ge2\), \(F_s\) is symmetric around \(p=1/2\), strictly decreases to its unique minimum as \(p\) rises to \(1/2\), and strictly increases thereafter. The balanced value is
\[
F_s(1/2)=I_{1/2}(s/2,1/2)
\sim\frac{2^{1-s/2}}{\sqrt{\pi s}}\qquad(s\to\infty).
\]
For every finite \(s\ge1\),
\[
\sup_{v:\ \sigma(v)>0}\Pr\{\widehat\lambda\notin[m,M]\}=\frac12.
\]
For \(s\ge2\), this supremum is not attained, but is approached by two-endpoint spectral mixtures with \(p\downarrow0\) or \(p\uparrow1\). For \(s=1\), every nontrivial two-endpoint mixture attains it. At any actual eigenvector \(\sigma=0\), the value is exactly the corresponding eigenvalue and its escape probability is zero.

## Assumptions and scope

All spaces, sketches and matrix entries are **real**. The matrix \(A\) is symmetric with at least two distinct eigenvalues; no positive definiteness is needed. A fixed vector \(v\ne0\) is chosen independently of the Gaussian sketch, whose entries are mutually independent \(N(0,1/s)\). The random quantity is the one-dimensional Galerkin/sRR compression obtained by enforcing \((Sv)^{\mathsf T}S(Av-\widehat\lambda v)=0\); since \(Sv\ne0\) almost surely, its denominator is almost surely nonzero. The stochastic statements do not assume the sketch is conditioned to satisfy a subspace embedding bound. For eigenvectors, \(\sigma=0\) is handled separately. The sharp spectral envelopes range over deterministic directions in the same fixed matrix, not over different matrices.

## Proof

**Exact law.** Normalize \(v\) to unit norm. If \(\sigma>0\), let \(w=(A-\mu I)v/\sigma\). The vectors \(v,w\) are orthonormal and \(Av=\mu v+\sigma w\). By rotational invariance of the independent Gaussian rows, \(X=\sqrt{s}\,Sv\) and \(Y=\sqrt{s}\,Sw\) are independent standard Gaussian vectors in \(\mathbb R^s\). Therefore
\[
\widehat\lambda=\mu+\sigma\frac{X^{\mathsf T}Y}{X^{\mathsf T}X}
=\mu+\sigma\frac{Z}{R},\qquad R=\|X\|_2\sim\chi_s,
\]
where \(Z=X^{\mathsf T}Y/\|X\|_2\sim N(0,1)\) is independent of \(R\). Conditional normality given \(X\) proves independence, not merely zero correlation. Since \(\sqrt{s}Z/R\) has the Student \(t_s\) law, the displayed formula and the usual Student moment thresholds follow. If \(\sigma=0\), \(Av=\mu v\), hence \(\widehat\lambda=\mu\) identically.

**Variance extremizer.** Spectral calculus gives the identity
\[
(M-\mu)(\mu-m)-\sigma^2
=\frac{v^{\mathsf T}(M I-A)(A-m I)v}{\|v\|_2^2}\ge0.
\]
Every factor is nonnegative on the spectrum. Equality holds precisely when \(v\) has no components in eigenspaces with eigenvalues strictly between \(m\) and \(M\). For fixed interior \(\mu\), both tail thresholds \((\mu-m)/\sigma\) and \((M-\mu)/\sigma\) decrease as \(\sigma\) increases. Since the density of \(Z/\chi_s\) is everywhere positive, the escape probability is strictly increasing in \(\sigma\). The maximizer is therefore exactly an extreme-eigenspace mixture with \(\sigma=\sqrt{(M-\mu)(\mu-m)}\). Such a mixture exists for every interior \(\mu\). Substitution yields \(F_s(p)\) and the equality classification.

**Optimal orientation.** Direct integration of independent Gaussian and chi densities gives the positive density of \(Z/\chi_s\),
\[
f_s(z)=c_s(1+z^2)^{-(s+1)/2},\qquad
c_s=\frac{\Gamma((s+1)/2)}{\sqrt{\pi}\Gamma(s/2)}.
\]
Put \(q=\sqrt{p/(1-p)}\), so \(F_s(p)=Q_s(q)+Q_s(1/q)\). Differentiating exactly,
\[
\frac{d}{dq}\bigl[Q_s(q)+Q_s(1/q)\bigr]
=c_s\frac{q^{s-1}-1}{(1+q^2)^{(s+1)/2}}.
\]
This derivative vanishes identically for \(s=1\), and is negative on \((0,1)\), positive on \((1,\infty)\) for every \(s\ge2\). The \(s=1\) constant is \(Q_1(q)+Q_1(1/q)=(\arctan(1/q)+\arctan q)/\pi=1/2\). For \(s\ge2\), the strict minimum is balanced, while each endpoint limit equals \(1/2\), because \(Q_s(0)=1/2\) and \(Q_s(+\infty)=0\). These facts and the fixed-mean variance bound prove the asserted sharp universal supremum and nonattainment. At balance, \(F_s(1/2)=2\Pr\{Z>\chi_s\}\); the ratio of independent chi-square variables has a beta law, yielding \(I_{1/2}(s/2,1/2)\). Standard beta-integral endpoint asymptotics, \(B(s/2,1/2)\sim\sqrt{2\pi/s}\), yield \(F_s(1/2)\sim2^{1-s/2}/\sqrt{\pi s}\). This is an asymptotic as the **sketch dimension** increases, not a statement about iterative convergence.

## Verification

The accompanying standalone `verify_ritz.py` uses Python, NumPy and SciPy. Running `python verify_ritz.py` checks the density and CDF conventions, the exact \(s=1\) half-escape identity, the fixed-mean symmetry and minimizer, the beta representation and its asymptotic scaling, and direct Gaussian sketch-versus-analytical escape probabilities for \(A=\operatorname{diag}(1,3)\) over six sketch sizes and five spectral mixtures. The fixed random seed is 240703. It completed 115 assertions in the recorded run. These finite numerical checks are corroboration only: the general conclusions above follow from Gaussian invariance, the spectral variance identity, and exact calculus.

For a concrete case, \(A=\operatorname{diag}(1,3)\), \(v=(1,1)^{\mathsf T}/\sqrt2\), and \(s=4\) give \(\Pr\{\widehat\lambda\notin[1,3]\}=I_{1/2}(2,1/2)=0.11611652351681556\ldots\), despite the original symmetric positive-definite matrix having eigenvalues only at \(1\) and \(3\).

## Relationship to prior work

De Damas and Grigori introduce sketch-orthogonal Arnoldi and randomized implicit restarting; their random compression motivates understanding the behavior of Ritz-like values with a finite sketch. Nakatsukasa and Tropp's randomized Rayleigh--Ritz framework supplies the general compressed operator \((SB)^\dagger SAB\), whose one-vector specialization is analyzed here. Güttel and Simunec study sketch-and-select Arnoldi and sketched orthogonalization. None of these algorithmic frameworks is claimed to be new. The present result isolates a sharp **probability of leaving the exact spectral interval**, its fixed-Rayleigh-value extremizers, and its universal half-probability obstruction.

The Student-ratio identity alone is a standard Gaussian fact; its use here is not claimed as a new distribution. Classical spectral variance bounds are likewise prior mathematics. The combined sharp, matrix-uniform spectral-escape extremal law is the assessed contribution. Earlier related analyses of a **reciprocal harmonic Ritz value** and of **two-dimensional nonreal sketched Ritz pairs** do not give this one-dimensional ordinary Ritz escape envelope.

## Limitations

The theorem concerns only a single sketched projection onto a fixed one-dimensional space, not a full Arnoldi or restarted eigensolver, and makes no conditional guarantee under a successful subspace embedding. The worst-case half-probability uses directions approaching an eigenvector; at the eigenvector the event has probability zero, and the **magnitude** of an escaping Ritz error shrinks with the residual norm. No statement is made about practical typical-case failure rates or the attainable accuracy of embedding-safeguarded iterations. The exact equivalence between this one-dimensional projection and the initial projected scalar in particular implementation variants should be checked against their normalization choices. Publication-priority uncertainty remains for any specialized result in partially accessible literature; no independent audit has been performed.

## References

1. J.-G. de Damas and L. Grigori, *Randomized Implicitly Restarted Arnoldi method for the non-symmetric eigenvalue problem*, first arXiv submission 2024-07-03, arXiv:2407.03208, https://arxiv.org/abs/2407.03208.
2. Y. Nakatsukasa and J. A. Tropp, *Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, first arXiv submission 2021-10-29, arXiv:2111.00113, https://arxiv.org/abs/2111.00113.
3. S. Güttel and I. Simunec, *A sketch-and-select Arnoldi process*, first arXiv submission 2023-06-06, arXiv:2306.03592, https://arxiv.org/abs/2306.03592.
4. R. Bhatia and C. Davis, *A Better Bound on the Variance*, American Mathematical Monthly 107 (2000), 353--357. The classical interval-variance inequality is used with equality characterized spectrally.
