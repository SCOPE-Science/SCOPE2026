# Sharp two-regime diagonal preconditioning for hub–exchangeable Stieltjes systems

## Finding

The smallest nonbipartite extension of a hub-and-leaf coupling model admits an exact, all-dimensional optimal diagonal preconditioner, including a sharp change in the active spectral constraints. Let \(m\ge3\) be an integer and let \(A=A_m(a,b)\) be the \((m+1)\times(m+1)\) symmetric matrix specified by
\[
A_{ii}=1,\qquad A_{0j}=A_{j0}=-a\ (1\le j\le m),\qquad
A_{ij}=-b\ (1\le i\ne j\le m).
\]
Define \(d=1-(m-1)b\). Under \(0<b<1/(m-1)\) and \(0<a<\sqrt{d/m}\), this matrix is positive definite. Its complete, unrestricted diagonal-congruence conditioning problem
\[
\kappa_* = \inf_{S\text{ positive diagonal}}\frac{\lambda_{\max}(SAS)}{\lambda_{\min}(SAS)}
\]
has an optimal representative \(S_* = \operatorname{diag}(\sqrt{u_*},1,\ldots,1)\), with
\[
\boxed{u_* = \max\left\{d,\frac{b(1+b)}{b+a^2}\right\}.}
\]
Writing \(a_c^2=mb^2/d\), the exact minimum is
\[
\boxed{\kappa_* = \begin{cases}
\dfrac{(1+b)(b+a^2)}{b(d-ma^2)},&a^2<a_c^2,\\
\dfrac{d+a\sqrt{md}}{d-a\sqrt{md}},&a^2\ge a_c^2.
\end{cases}}
\]
At equality the expressions agree. Among the exchangeable two-orbit diagonal scalings, \(u_*\) is unique. The ordinary Jacobi preconditioner, which leaves this unit-diagonal matrix unchanged, is optimal among *all* positive diagonal scalings exactly when \(a=b\).

In the lower-coupling branch the top eigenvalue \(1+b\) has multiplicity \(m\) at the optimum; in the strict upper-coupling branch it is simple. The upper-coupling branch is admissible for some \(a\) precisely when \(b<1/(2m-1)\).

A concrete six-dimensional example is \(m=5\), \(a=1/4\), \(b=1/8\). Then \(d=1/2\), \(u_*=3/4\), and the optimally preconditioned eigenvalues are \(1/8\) and \(9/8\) (the latter with multiplicity five), giving \(\kappa_*=9\). Jacobi instead has condition number \((3+\sqrt6)/(3-\sqrt6)>9\).

## Assumptions and scope

All parameters are real, with \(m\ge3\), \(0<b<1/(m-1)\), \(0<a<\sqrt{d/m}\), and \(d=1-(m-1)b\). The minimization permits **every** positive diagonal \((m+1)\times(m+1)\) matrix, not merely symmetric candidates; zero or infinite scale factors are excluded. Diagonal phases or signs are immaterial to the eigenvalues. No claim of uniqueness of *all* unrestricted optimizing scalings is needed or made. The class is irreducible and strictly positive definite, so its spectral condition number is well defined.

## Proof

**1. Positive definiteness.** The \(m\)-dimensional leaf block is \((1+b)I_m-b\mathbf1\mathbf1^T\), whose constant-vector eigenvalue is \(d=1-(m-1)b\) and whose other \(m-1\) eigenvalues equal \(1+b\). A Schur complement shows \(A\succ0\) precisely when \(d>ma^2\), together with \(b>0\), \(d>0\).

**2. Averaging certifies unrestricted globality.** Let \(S\succ0\) be any diagonal scale, and set \(\mu=\lambda_{\min}(SAS)\) and \(K=\lambda_{\max}(SAS)/\mu\). The diagonal matrix \(E=\mu S^{-2}\) satisfies the linear matrix inequalities \(E\preceq A\preceq KE\). Every permutation of the last \(m\) coordinates fixes \(A\). Average the leaf-permuted matrices \(E\) over the symmetric group; the averaged positive diagonal \(\bar E\) still obeys both inequalities, and has one common value on all leaves. Thus \(\bar S=\bar E^{-1/2}\) has condition number at most \(K\), and after removing an irrelevant positive scalar it is \(\operatorname{diag}(\sqrt u,1,\ldots,1)\). Consequently the unrestricted infimum equals the minimum in this single parameter \(u>0\).

**3. Exact eigenvalues.** In the \((m-1)\)-dimensional zero-sum leaf space, the scaled matrix has eigenvalue \(1+b\). On the span of the hub vector and the normalized constant leaf vector, it equals
\[
M(u)=\begin{pmatrix}u&-a\sqrt{m u}\\-a\sqrt{m u}&d\end{pmatrix}.
\]
Its eigenvalues are
\[
\lambda_\pm(u)=\frac{u+d\pm\sqrt{(u-d)^2+4ma^2u}}2.
\]
Since \(d<1+b\) and \(a>0\), \(\lambda_-(u)<1+b\) for all \(u>0\). Hence
\[
\kappa(u)=\frac{\max\{1+b,\lambda_+(u)\}}{\lambda_-(u)}.
\]
The derivative of \(\lambda_-(u)\) is strictly positive: writing \(c=ma^2<d\), the discriminant exceeds \((u-d+2c)^2\) by \(4c(d-c)>0\). Furthermore \(\lambda_+(u)\) is strictly increasing by its symmetric equivalent derivative or by the positive eigenvector of the nonnegative sign-flipped block.

**4. The two competing spectral barriers.** The ratio \(\lambda_+(u)/\lambda_-(u)\) is minimized uniquely at \(u=d\). Indeed its monotonicity is equivalent to that of
\[
F(u)=\frac{(u-d)^2+4ma^2u}{(u+d)^2},\quad
F'(u)=\frac{4(u-d)(d-ma^2)}{(u+d)^3},
\]
and \(d-ma^2>0\). At \(u=d\), \(\lambda_+(d)=d+a\sqrt{md}\). This exceeds or equals \(1+b\) exactly when \(a^2\ge mb^2/d\). In that case \(\kappa(u)\ge\lambda_+(u)/\lambda_-(u)\ge\lambda_+(d)/\lambda_-(d)=\kappa(d)\), proving the upper-coupling branch and the uniqueness of its orbit-invariant minimizer.

Otherwise \(\lambda_+(d)<1+b\). The strictly increasing function \(\lambda_+(u)\) crosses \(1+b\) exactly once at
\[
u_0=\frac{b(1+b)}{b+a^2}>d.
\]
For \(u\le u_0\), \(\kappa(u)=(1+b)/\lambda_-(u)\) decreases strictly with \(u\). For \(u\ge u_0>d\), \(\kappa(u)=\lambda_+(u)/\lambda_-(u)\) increases strictly with \(u\). Therefore the unique orbit-invariant optimum is \(u_0\). At this crossing, the second block eigenvalue is \(\lambda_-=u_0-mb=b(d-ma^2)/(b+a^2)>0\), proving the lower-coupling formula.

**5. Jacobi rigidity and phase existence.** Here all original diagonal entries are one. Since the orbit-invariant optimizer \(u_*\) is unique, Jacobi is globally optimal only if \(u_*=1\). In the upper-coupling branch \(u_*=d<1\); in the lower-coupling branch \(u_*=b(1+b)/(b+a^2)=1\) exactly when \(a=b\). Conversely \(a=b\) satisfies the positive-definiteness assumptions only when \(b<1/m\), and lies in the lower-coupling branch; thus Jacobi is indeed optimal there. A nonempty strict upper-coupling region requires \(mb^2/d<d/m\), equivalent to \(b<1/(2m-1)\).

**6. Large systems.** With \(b=\beta/m\) and \(a=\alpha/\sqrt m\), take fixed \(0<\beta<1\), \(\alpha>0\), \(\alpha^2<1-\beta\). For sufficiently large \(m\) the hypotheses hold. Then \(u_*\) tends to \(\max\{1-\beta,\,\beta/(\beta+\alpha^2)\}\), and the upper branch is realized if \(\alpha^2>\beta^2/(1-\beta)\); the strict lower branch occurs for the reverse inequality. The limiting optimal condition numbers follow by direct substitution in the formulas above. Thus the two-regime transition persists at macroscopic dimension, rather than being an artifact of a small matrix.

## Verification

The bundled `verify.py` constructs the actual full matrices and independently checks their eigenvalues against the two-block representation, the exact formulas, positive definiteness, and numerous asymmetric diagonal competitors for \(3\le m\le11\). It additionally checks exact fractional arithmetic for the six-dimensional example and a rational equality case, plus the homogeneous Jacobi line through \(m=29\). Run with Python and NumPy: `python verify.py`. The finite checks supplement, not replace, the proof for every admissible \(m,a,b\).

## Relationship to prior work

The general positive-definite diagonal condition-number minimization problem and its convex formulation predate this result; see Lu–Pong (2011), especially its exact diagonal-preconditioner convex formulation. Kolotilina (2006) gives a complete solution for general quasireal positive-definite **three-by-three** matrices, and therefore already covers the two-leaf member \(m=2\) excluded from the new claim. Shapiro (1985) gives general necessary and sufficient optimal-scaling conditions and special block cases; these are not claimed as new here. The asserted addition is the explicit unrestricted optimizer, sharp eigenmode switching rule, and Jacobi if-and-only-if characterization for every \(m\ge3\) in the hub–exchangeable nonbipartite class. Prior general optimization frameworks alone do not supply these displayed parameter formulas.

## Limitations

This is a structured two-coupling matrix family, not an algorithm for arbitrary positive definite matrices. The theorem constructs a globally optimal diagonal preconditioner and proves uniqueness only within the two-orbit subclass, not among all nonsymmetric diagonal scalings. General optimal-scaling criteria in older literature could imply further corollaries, and a closed-form identical specialization may remain unindexed. Literature checking was not an independent validation. Numerical tests are finite and do not establish the universal claim by themselves.

## References

- Z. Lu and T. K. Pong, "Minimizing Condition Number via Convex Programming," *SIAM Journal on Matrix Analysis and Applications* 32 (2011), 1193–1211. DOI: `10.1137/100795097`. First posted online 1 November 2011 (publisher record).
- L. Yu. Kolotilina, "Solution of the Problem of Optimal Diagonal Scaling for Quasireal Hermitian Positive-Definite 3×3 Matrices," *Journal of Mathematical Sciences* 132 (2006), 190–213. DOI: `10.1007/s10958-005-0488-1`.
- A. Shapiro, "Optimal Block Diagonal \(\ell_2\)-Scaling of Matrices," *SIAM Journal on Numerical Analysis* 22 (1985), 81–94. DOI: `10.1137/0722005`.
