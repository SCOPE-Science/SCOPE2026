# Three independent Gaussian Ritz sketches recover the exact residual mean-square scale

## Finding

A square Gaussian Petrov–Galerkin Rayleigh–Ritz pencil can contain a randomized Ritz value with **infinite squared error** even for a finite-dimensional Hermitian eigenproblem with an almost exact trial vector. When the other trial directions form a known invariant subspace, three **independent** square sketches and a componentwise complex sample median repair the integrability defect, with an exact identity for every matrix dimension:

\[
\mathbb{E}|M_3-\lambda|^2=\|(A-\lambda I)w\|_2^2.
\]

In contrast, the single-sketch non-spectator Ritz value \(Y\) obeys \(\mathbb{E}|Y-\lambda|^2=\infty\) whenever \(\|(A-(w^{\mathsf H}Aw)I)w\|_2>0\). More generally, for odd \(k=2h+1\), the componentwise complex median \(M_k\) has finite absolute moments **exactly** of orders \(0<q<k+1\); at and above \(k+1\) those moments diverge. Thus three is the smallest odd replication count that gives finite mean-square error.

The result is for the mathematically distinguished non-spectator generalized eigenvalue of each square pencil, not for an arbitrary practical rule that selects the Ritz value closest to a requested shift. The median is taken over independent repetitions of the original square procedure, not an enlarged rectangular least-squares sketch.

## Assumptions and scope

Let \(2\le m<n\), let \(A=A^{\mathsf H}\in\mathbb C^{n\times n}\), and let \(V\in\mathbb C^{n\times(m-1)}\) have orthonormal columns spanning an \(A\)-invariant subspace. Then \(AV=VD\) for a Hermitian \((m-1)\)-square matrix \(D\). Choose a unit vector \(w\in(\operatorname{range}V)^\perp\) and set

\[
W=[w,V],\qquad \rho=w^{\mathsf H}Aw\in\mathbb R,\qquad
r=Aw-\rho w,\qquad \sigma=\|r\|_2.
\]

Assume \(\sigma>0\). Choose any real comparison value \(\lambda\), particularly an eigenvalue of \(A\) whose eigenvector is orthogonal to \(\operatorname{range}V\). There is no restriction on how close \(w\) is to that eigenspace. Each sketch \(\Omega\in\mathbb C^{n\times m}\) has independent standard circular complex Gaussian entries, with independent real and imaginary parts distributed as \(N(0,1/2)\). Sketches are mutually independent across repetitions. Form the square generalized eigenproblem

\[
\Omega^{\mathsf H}AWy=\mu\,\Omega^{\mathsf H}Wy.
\]

Almost surely it has the \(m-1\) eigenvalues of \(D\) (with their multiplicities) and one additional eigenvalue \(Y\), called the **non-spectator root**. Since \(\sigma>0\), that extra root almost surely does not coincide with a fixed spectator eigenvalue. For an odd number \(k\) of independent sketches with extra roots \(Y_1,\ldots,Y_k\), define

\[
M_k=\operatorname{med}(\operatorname{Re}Y_1,\ldots,\operatorname{Re}Y_k)
+i\,\operatorname{med}(\operatorname{Im}Y_1,\ldots,\operatorname{Im}Y_k),
\]

where \(\operatorname{med}\) is the ordinary real sample median. This estimator depends on the fixed choice of real and imaginary axes; no rotational optimality is asserted.

## Proof

**1. Exact spectral separation.** Hermiticity and invariance imply \(V^{\mathsf H}r=0\); the definition of \(\rho\) also gives \(w^{\mathsf H}r=0\). Thus \(w\), \(r/\sigma\), and the columns of \(V\) form an orthonormal family. Put

\[
g=\Omega^{\mathsf H}w,\qquad h=\Omega^{\mathsf H}r/\sigma,\qquad B=\Omega^{\mathsf H}V.
\]

Their columns are mutually independent standard circular complex Gaussian vectors, by Gaussian invariance. Multilinearity of the determinant gives, identically as a polynomial in \(z\),

\[
\det\bigl(\Omega^{\mathsf H}(A-zI)W\bigr)
=\det(D-zI)\bigl[(\rho-z)\det[g,B]+\sigma\det[h,B]\bigr].
\]

The square Gaussian matrix \([g,B]\) is nonsingular almost surely, so the extra root is well-defined and uniquely determined:

\[
Y=\rho+\sigma\frac{\det[h,B]}{\det[g,B]}.
\]

Conditional on \(B\), choose a unit \(u\) orthogonal to its column space. Both determinants are nonzero multiples of the corresponding projections onto \(u\); their common factor cancels. Therefore

\[
Y\ \stackrel{\mathrm d}=\ \rho+\sigma\frac{Z_1}{Z_0},
\qquad Z_0,Z_1\ \text{independent standard circular complex Gaussians}.
\]

This holds for all allowed \(n,m,A,V,w\), and the distribution does not depend on the spectator eigenvalues.

**2. Exact law and raw moments.** The quotient \(Z=Z_1/Z_0\) has the circular complex-Cauchy density and radial tail

\[
p_Z(z)=\frac{1}{\pi(1+|z|^2)^2},\qquad
\mathbb P\{|Z|>t\}=\frac{1}{1+t^2}\quad(t\ge0).
\]

For \(q>0\), polar integration gives

\[
\mathbb E|Y-\rho|^q
=\sigma^q\Gamma(1+q/2)\Gamma(1-q/2)
\quad\text{for }0<q<2,
\]

and the expectation is infinite for \(q\ge2\). A fixed finite translation from \(\rho\) to \(\lambda\) does not alter moment finiteness, so \(\mathbb E|Y-\lambda|^2=\infty\). The ordinary complex mean exists and equals \(\rho\), but its second absolute moment does not.

**3. Three-repetition exact risk.** The real marginal of \(Z\) has distribution function \(F\) and density \(f\):

\[
F(x)=\frac12\left(1+\frac{x}{\sqrt{1+x^2}}\right),\qquad
f(x)=\frac{1}{2(1+x^2)^{3/2}}.
\]

The middle order statistic of three independent such coordinates has density

\[
g_3(x)=6F(x)(1-F(x))f(x)
=\frac{3}{4(1+x^2)^{5/2}}.
\]

It is centered by symmetry, and its second moment is exactly

\[
\int_{\mathbb R}x^2g_3(x)\,dx=\frac12.
\]

Hence the real and imaginary coordinate medians each have mean zero and second moment \(\sigma^2/2\). No independence between the two coordinate medians is needed, because the squared complex modulus is the sum of their two squared coordinates. Consequently,

\[
\mathbb EM_3=\rho,\qquad
\mathbb E|M_3-\rho|^2=\sigma^2,
\qquad \mathbb E|M_3-\lambda|^2=(\rho-\lambda)^2+\sigma^2.
\]

The orthogonal decomposition \((A-\lambda I)w=(\rho-\lambda)w+r\) completes the announced identity.

**4. Sharp odd-replication moment threshold.** For a coordinate \(X=\operatorname{Re}Z\), the exact survival function obeys

\[
\mathbb P(X>t)
=\frac12\left(1-\frac{t}{\sqrt{1+t^2}}\right)
\sim\frac{1}{4t^2}\quad(t\to\infty).
\]

For \(k=2h+1\), the event that the sample median exceeds \(t\) is the event that at least \(h+1\) independent observations exceed \(t\). Its probability is therefore asymptotic to

\[
{2h+1\choose h+1}\,4^{-(h+1)}t^{-2(h+1)}.
\]

The negative-coordinate tail has the same asymptotics. Thus the sample median's absolute \(q\)-moment is finite exactly when \(q<2(h+1)=k+1\). Both real and imaginary coordinate medians have that threshold; the complex modulus inherits it by elementary comparisons with its two coordinates. A deterministic shift and nonzero scaling leave the threshold unchanged. In particular, \(k=1\) lacks a second moment and \(k=3\) has one, while \(k=3\) still lacks a fourth moment. This proves sharpness *within the odd-sample componentwise-median family*, not among all conceivable robust estimators.

**5. Concrete diagonal Hermitian family.** Take \(A=\operatorname{diag}(0,1,2,\ldots,n-1)\), \(V=[e_3,\ldots,e_{m+1}]\), \(2\le m<n\), and

\[
w=\cos\theta\,e_1+\sin\theta\,e_2,
\qquad 0<\theta<\pi/2.
\]

Here the desired eigenvalue is \(\lambda=0\), the one-dimensional trial-angle error is \(\theta\), and \(\rho=\sin^2\theta\), \(\sigma=\sin\theta\cos\theta\). A single non-spectator randomized Ritz value has infinite mean-square error at **every** positive angle, whereas

\[
\mathbb E|M_3|^2=\sin^2\theta.
\]

Thus the repaired squared error tends to zero at exactly the squared subspace-angle scale, independently of \(m\) and \(n\). This statement concerns **unrefined** Ritz values, not the bounded Hermitian Rayleigh-quotient refinement.

## Verification

The accompanying standalone file `verify.py` uses Python 3 and NumPy. It compares determinant-based non-spectator generalized eigenvalues with the projected complex-Gaussian quotient on 585 generated square pencils, including larger ambient spaces and three-mode complex trial vectors. Independent Monte Carlo checks evaluate the radial tail at the scale, the three-median second moment, and the illustrative angle-specific mean-square error. A gamma-function evaluation checks the exact middle-order-statistic second-moment integral. These are finite reproducibility checks; the preceding analytic argument proves the unbounded-dimensional and infinite-moment assertions.

## Relationship to prior work

Shao, *Stabilizing the Rayleigh--Ritz procedure by randomization*, arXiv:2604.01037 (first posted 2026-04-01), introduces the square complex-Gaussian Petrov–Galerkin pencil and establishes high-probability spectral extraction, with a \(\delta^{-1/2}\)-type factor. Its refined Ritz values are a **different output statistic** from the unrefined generalized eigenvalues studied here. The paper's unsuccessful rectangular oversampling test concerns a different procedure from repetition of independent square sketches followed by a coordinatewise median.

Nakatsukasa and Tropp, *Fast and Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems* (SIAM J. Matrix Anal. Appl., 2024, DOI 10.1137/23M1565413), analyze a sketched Rayleigh–Ritz problem using a larger subspace embedding and a pseudoinverse. This does not imply the distribution or exact median risk of the present square generalized eigenvalue.

Complex-Gaussian quotient distributions and sample-median/order-statistic identities are classical tools, **not claimed as newly discovered probability laws**. Gu, *On the Quotient of a Centralized and a Non-centralized Complex Gaussian Random Variable* (J. Res. NIST, 2020, DOI 10.6028/jres.125.030), explicitly surveys quotient distributions and moments in signal processing. The claimed contribution here is their exact application to an invariant-spectator generalized Ritz pencil, the dimension-free residual mean-square identity after three independent sketches, and the exact odd-replication integrability budget.

## Limitations

The exact reduction requires an \(A\)-invariant spectator subspace, a Hermitian \(A\), square independent complex-Gaussian sketches, and separation of the non-spectator root. It does not characterize arbitrary trial spaces, real Gaussian sketches, non-Hermitian matrices, numerical rounding, adaptive Ritz-root selection, or correlated sketch reuse. The median is coordinatewise, not a complex geometric median. The proof does not show the median improves on the ordinary deterministic Hermitian Rayleigh quotient: in this invariant-spectator model the latter can already be computed from \(w\). The role of the median theorem is to characterize and repair the **unrefined randomized Ritz-value** mean-square pathology, not to establish an optimal overall eigensolver. A relevant equivalence may exist in unindexed sketching or robust-estimation literature; independent verification is not asserted.

## References

1. Nian Shao, *Stabilizing the Rayleigh--Ritz procedure by randomization*, arXiv:2604.01037, initial version posted 2026-04-01, https://arxiv.org/abs/2604.01037.
2. Yuji Nakatsukasa and Joel A. Tropp, *Fast and Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, SIAM J. Matrix Anal. Appl. 45 (2024), 1183–1214, https://doi.org/10.1137/23M1565413.
3. Dazhen Gu, *On the Quotient of a Centralized and a Non-centralized Complex Gaussian Random Variable*, J. Res. NIST 125 (2020), article 125030, https://doi.org/10.6028/jres.125.030.
