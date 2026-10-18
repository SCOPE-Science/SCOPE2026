# Sharp two-parameter preconditioned SOR convergence for complex conjugate modes

## Finding
Consider the real block formulation of a nonsingular complex linear system \(W+iT\), where \(W,T\in\mathbb R^{n\times n}\), \(W\) is invertible, and the real matrix \(S=W^{-1}T\) has spectrum exactly \(\{u+iv,u-iv\}\), for \(u\in\mathbb R\), \(v>0\), with arbitrary multiplicities and possible Jordan blocks. Assume \(u^2+(v-1)^2>0\), which excludes the singular complex system. The dimension \(n\) is necessarily even.

For each real nonzero preconditioning parameter \(\theta\), set \(W_\theta=\theta W+T\), \(T_\theta=\theta T-W\), and \(Z_\theta=W_\theta^{-1}T_\theta\). The real block preconditioner is \(P_\theta=\begin{psmallmatrix}\theta I&I\\-I&\theta I\end{psmallmatrix}\); \(W_\theta\) is invertible because \(S\) has no real eigenvalues. The block SOR iteration with real relaxation \(\omega\), in error coordinates, has matrix
\[
L_{\theta,\omega}=\begin{pmatrix}(1-\omega)I&\omega Z_\theta\\-\omega(1-\omega)Z_\theta&(1-\omega)I-\omega^2 Z_\theta^2\end{pmatrix}.
\]
Define the Cayley-invariant spectral parameter and its associated rate by
\[
c=\sqrt{\frac{u^2+(v-1)^2}{u^2+(v+1)^2}},\qquad
q=\frac{1-c}{1+c}\in(0,1),\qquad
R_* =\frac{1-\sqrt{1-q^2}}{1+\sqrt{1-q^2}}.
\]
Then the **exact global two-parameter infimum**, with no restriction to a neighborhood of a candidate optimum, is
\[
\boxed{\inf_{\theta\in\mathbb R\setminus\{0\},\;\omega\in\mathbb R}\rho(L_{\theta,\omega})=R_*<1.}
\]
If \(u\ne0\), the infimum is **attained uniquely** at
\[
\boxed{\theta_* =\frac{2u}{u^2+v^2-1+\sqrt{(u^2+v^2-1)^2+4u^2}},\qquad
\omega_*=1+R_* =\frac{2}{1+\sqrt{1-q^2}}.}
\]
At this pair, the two transformed eigenvalues of \(Z_{\theta_*}\) are \(\pm iq\), and every characteristic root of the block SOR iteration equals \(R_*\) (possibly with nontrivial Jordan structure). The expression \(q\) can equivalently be evaluated as
\[
q=\frac{2v}{u^2+v^2+1+\sqrt{(u^2+v^2-1)^2+4u^2}}.
\]
If \(u=0\) and \(0<v<1\), the same infimum is approached only as \(|\theta|\to\infty\), the unpreconditioned block-SOR limit. If \(u=0\) and \(v>1\), it is approached only as \(\theta\to0\); it is not attained in the prescribed nonzero-\(\theta\) family. In both boundary regimes \(q=\min\{v,v^{-1}\}\).

The result includes a convergence-restoration phenomenon: if \(v\ge1\) and \(u\ne0\), **no real relaxation parameter can make the unpreconditioned block SOR converge**, yet the uniquely tuned block-preconditioned iteration converges with factor \(R_*<1\).

## Assumptions and scope
All matrices are finite-dimensional and real except the original complex coefficient \(W+iT\). The spectral hypothesis is one nonreal complex-conjugate pair, possibly with algebraic multiplicity greater than one; diagonalizability and symmetry of \(S\) are not assumed. The nonzero real \(\theta\) convention follows the specified BPSOR formulation. Spectral radius is an asymptotic convergence measure and is not the one-step Euclidean operator norm. Exact arithmetic is assumed. The source date of the motivating BPSOR paper is 2026-02-24.

## Proof
**1. Spectral reduction.** Put \(a=1-\omega\). Since \(Z_\theta=(\theta I+S)^{-1}(\theta S-I)\), its eigenvalues are
\[
\tau_\theta=\frac{\theta\mu-1}{\theta+\mu},\quad
\overline{\tau_\theta},\qquad \mu=u+iv.
\]
The block determinant identity gives
\[
\det(\lambda I_{2n}-L_{\theta,\omega})
=\det\!\left((\lambda-a)^2I_n+\omega^2\lambda Z_\theta^2\right).
\]
Thus, for each \(\tau\in\sigma(Z_\theta)\), the corresponding iteration roots satisfy
\[
(\lambda-a)^2=-\omega^2\tau^2\lambda.
\]
Both conjugate modes have the same maximal root modulus. The polynomial identity is valid without diagonalizability.

**2. An invariant of the allowed preconditioner.** For every real \(\theta\),
\[
\frac{\tau_\theta-i}{\tau_\theta+i}
=\frac{\theta-i}{\theta+i}\,\frac{\mu-i}{\mu+i}.
\]
Therefore \(\left|(\tau_\theta-i)/(\tau_\theta+i)\right|=c\). Also \(\operatorname{Im}\tau_\theta=v(1+\theta^2)/|\theta+\mu|^2>0\). Since \(\mu\ne i\), \(0<c<1\).

**3. The universal lower bound.** Suppose \(r=\rho(L_{\theta,\omega})<1\). Because the transformed eigenvalue has positive imaginary part, \(r>0\). The product of the two scalar characteristic roots is \(a^2\), so \(|a|\le r\). Consequently \(0<\omega<2\), and in fact \(1-r\le\omega\le1+r\). Choose square roots \(t,t'\) of the two characteristic roots satisfying \(t^2-i\omega\tau t-a=0\), so \(t'=-a/t\). If \(a=0\), take the nonzero root. The two modulus constraints give
\[
\frac{|a|}{\sqrt r}\le |t|\le\sqrt r.
\]
Writing \(t=h e^{i\phi}\) and \(\tau=(t-a/t)/(i\omega)\), we obtain
\[
0<\operatorname{Im}\tau
\le\frac{1}{\omega}\max_{|a|/\sqrt r\le h\le\sqrt r}\left|h-\frac{a}{h}\right|
=\frac{r-a}{\omega\sqrt r}=:B_r.
\]
The maximum is at an endpoint: for \(a\ge0\) the interior expression is increasing before taking absolute values; for \(a<0\), \(h+|a|/h\) is convex and is largest at an endpoint. The \(a=0\) case follows directly. Because \(\omega\le1+r\),
\[
B_r=\frac{1-(1-r)/\omega}{\sqrt r}
\le\frac{2\sqrt r}{1+r}<1.
\]
For any \(\tau=x+iy\), with \(0<y\le B_r<1\), direct comparison of squared moduli gives
\[
\left|\frac{\tau-i}{\tau+i}\right|
=\sqrt{\frac{x^2+(1-y)^2}{x^2+(1+y)^2}}
\ge\frac{1-y}{1+y}\ge\frac{1-B_r}{1+B_r}.
\]
Using the invariant and solving for \(q\) yields
\[
q=\frac{1-c}{1+c}\le B_r\le\frac{2\sqrt r}{1+r}.
\]
The last function increases strictly on \((0,1)\); inversion gives \(r\ge R_*\). If \(r\ge1\), this lower bound is automatic. Therefore the lower bound holds for every real admissible parameter pair.

**4. Attainment and uniqueness away from the imaginary axis.** Solving \(\operatorname{Re}\tau_\theta=0\) is equivalent to
\[
u\theta^2+(u^2+v^2-1)\theta-u=0.
\]
For \(u\ne0\), its two nonzero real roots map \(\mu\) to the two positive imaginary points \(iq\) and \(i/q\), respectively. The displayed \(\theta_*\) is the former root. Set \(\omega_*=1+R_*\). The identity \(q=2\sqrt{R_*}/(1+R_*)\) turns the modal polynomial into
\[
(\lambda+R_*)^2-\omega_*^2q^2\lambda=(\lambda-R_*)^2.
\]
Hence \(\rho(L_{\theta_*,\omega_*})=R_*\). Conversely, equality throughout the lower-bound chain forces \(\omega=1+R_*\), \(\operatorname{Re}\tau=0\), and \(\operatorname{Im}\tau=q\). These conditions uniquely fix \(\theta=\theta_*\) when \(u\ne0\), and therefore uniquely fix \(\omega\).

**5. Purely imaginary limiting cases.** If \(u=0\), the condition \(\operatorname{Re}\tau_\theta=0\) for \(v\ne1\) forces either \(\theta=0\) or the limit \(|\theta|\to\infty\). The images are, respectively, \(i/v\) and \(iv\); the one of modulus below one is \(iq\), with \(q=\min\{v,v^{-1}\}\). Continuity of the spectral roots proves the stated infima and nonattainment in the finite nonzero-\(\theta\) family.

**6. Failure of unpreconditioned stabilization.** The classical complex-spectrum SOR disk criterion has an ellipse with real semi-axis \(1\) in the Jacobi spectral plane. Since the unpreconditioned Jacobi eigenvalues are \(\pm i\mu\) and \(\pm i\overline\mu\), their real parts have magnitude \(v\). Thus \(v\ge1\) prohibits convergence for every real \(\omega\), whereas the explicit tuned pair has spectral radius \(R_*<1\) when \(u\ne0\). This comparison uses a previously known SOR criterion, not a new claim about that criterion.

## Verification
The accompanying standalone `reproduce.py` program uses Python and NumPy to check the exact transformations, scalar quadratic and direct real block-iteration eigenvalues, a nonorthogonal similarity family, the specified closed-form optimum, and 8,000 nonoptimal parameter comparisons. It reports 9,209 successful finite numerical and identity checks under a fixed deterministic random seed. These tests are supporting diagnostics only; steps 1–6 provide the proof of the universal minimum, boundary assertions and uniqueness.

For an explicit well-conditioned input, take \(W=I_2\) and \(T=\begin{psmallmatrix}1&-2\\2&1\end{psmallmatrix}\). Then \(\mu=1+2i\), \(\theta_*=\sqrt5-2\), \(q=(3-\sqrt5)/2\), and \(R_*\approx0.03940575785027\). The original complex system is nonsingular, the unpreconditioned real block SOR cannot converge, and the tuned BPSOR iteration has the stated spectral factor.

## Relationship to prior work
Louka and Missirlis (2026) define this BPSOR transformation and optimize its parameters assuming that \(\sigma(W^{-1}T)\) is real; their Section 3.2 explicitly identifies the complex-spectral case as a further question. Their real-spectrum formulas and original preconditioner are credited.

The complex-Jacobi-spectrum SOR ellipse and its fixed-spectrum relaxation analysis are classical, including Botta and Veldman (1982), Section 2, equations (4)–(8). Hocking and Greif (2025) analyze optimal SOR rates for complex line-segment Jacobi spectra without optimizing this real BPSOR preconditioner. Hezari, Edalatpour and Salkuyeh (2015) study PGSOR for complex symmetric systems under restrictive real-spectrum structural assumptions. None of those inspected results states or directly implies the globally sharp **joint** preconditioner-plus-relaxation optimum on the nonreal conjugate-pair class. The Cayley-invariant bound, matched construction and attainment classification are the proposed addition. This comparison is not a claim of exhaustive bibliographic uniqueness.

## Limitations
The exact optimization applies to a *single* complex-conjugate generalized spectral pair; arbitrary finite spectra with several distinct pairs require a separate minimax analysis. The spectral statement does not bound transient errors for nonnormal or defective iteration matrices, and does not establish iteration-count savings under finite-precision stopping tests or account for factorization costs of \(W_\theta\). The formulas assume exact real arithmetic and ideal solves. Earlier complex-SOR ellipse results must not be counted as new. Unindexed and inaccessible preconditioning literature may contain equivalent joint-optimization conclusions.

## References
1. M. A. Louka and N. M. Missirlis, *The Block Preconditioned SOR Method for Solving Indefinite Complex Linear Systems*, *Numerical Linear Algebra with Applications* 33 (2026), e70068. DOI: 10.1002/nla.70068. First publicly verified 2026-02-24. https://onlinelibrary.wiley.com/doi/full/10.1002/nla.70068
2. E. F. F. Botta and A. E. P. Veldman, *On Local Relaxation Methods and Their Application to Convection-Diffusion Equations*, *Journal of Computational Physics* 48 (1982), 127–149. https://pure.rug.nl/ws/files/3427889/1981JCompPhysBotta.pdf
3. L. R. Hocking and C. Greif, *Convergence Analysis of Optimal SOR for a Class of Consistently Ordered 2-Cyclic Matrices with Complex Spectra*, arXiv:2508.02052v1 (2025-08-04). https://arxiv.org/html/2508.02052v1
4. D. Hezari, V. Edalatpour and D. K. Salkuyeh, *Preconditioned GSOR Iterative Method for a Class of Complex Symmetric System of Linear Equations*, *Numerical Linear Algebra with Applications* 22 (2015), 761–776. DOI: 10.1002/nla.1987.
