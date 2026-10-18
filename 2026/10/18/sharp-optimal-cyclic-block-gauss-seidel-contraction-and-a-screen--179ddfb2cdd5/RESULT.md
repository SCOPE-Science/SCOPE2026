# Sharp optimal cyclic-block Gauss–Seidel contraction and a screened-Poisson crossover

## Finding

For every integer \(n\ge3\), interval length \(1\le q<n\), and coupling \(0<t<1/2\), let \(C\) be the cyclic right-shift permutation of order \(n\) and let
\[
G=I_n-t(C+C^{\mathsf T}).
\]
Consider an exact block-coordinate minimization step on the quadratic \(f(x)=\tfrac12(x-x_*)^{\mathsf T}G(x-x_*)\), in which an interval of \(q\) consecutive cyclic coordinates is selected according to **any fixed probability distribution** over the \(n\) possible starting locations. Define \(\Lambda(p)\) as the worst-case conditional expected relative drop of the squared \(G\)-energy in that one step, infimized over all nonzero current errors.

Put \(\alpha=\operatorname{arcosh}(1/(2t))>0\). The exact optimum over all probability distributions is
\[
\boxed{\max_p\Lambda(p)=\Lambda_*=
\frac1n\left[q-\frac{\sinh(q\alpha/2)}{\sinh(\alpha/2)\cosh((q+1)\alpha/2)}\right].}
\]
Uniform interval sampling attains this sharp bound. For **every** sampling distribution, the constant-error vector has exactly this expected relative energy reduction, so no distribution can improve the worst-case factor. In particular, the optimal worst-case one-step expected squared-energy contraction is \(1-\Lambda_*\).

For any sequence of admissible dimensions and lengths with \(q\to\infty\), \(t\uparrow1/2\), \(q\alpha\to s\in(0,\infty)\), and \(q<n\), the exact formula gives the crossover
\[
\boxed{\frac{n\Lambda_*}{q}\longrightarrow F(s):=1-\frac{2\tanh(s/2)}s.}
\]
The profile increases strictly from zero to one, has \(F(s)\sim s^2/12\) for small positive \(s\), and \(F(s)=1-2/s+o(1/s)\) at large \(s\). The effective transition length is of order \((1-2t)^{-1/2}\).

## Assumptions and scope

Indices are taken modulo \(n\). Denote by \(E_j\in\mathbb R^{n\times q}\) the selection matrix for the contiguous cyclic interval \(B_j=(j,j+1,\dots,j+q-1)\), ordered consecutively, with \(j=0,\dots,n-1\). The update is the **exact minimization**
\[
e^+=e-E_j(E_j^{\mathsf T}GE_j)^{-1}E_j^{\mathsf T}Ge,
\qquad e=x-x_*.
\]
The index \(j\) is selected with fixed probabilities \(p_j\ge0\), \(\sum_jp_j=1\), independently of the present error; probabilities may be zero. Because \(0<t<1/2\), the eigenvalues of \(G\) are at least \(1-2t>0\); every principal block is positive definite.

Use the squared energy \(\|e\|_G^2=e^{\mathsf T}Ge\). The precise quantity is
\[
\Lambda(p):=\inf_{e\ne0}\frac{\|e\|_G^2-\mathbb E_p[\|e^+\|_G^2\mid e]}{\|e\|_G^2}.
\]
The theorem does not allow changing the distribution after observing the error and does not assert that the one-step worst-case error direction remains the worst case at every future iteration.

## Proof

**1. Exact block projection and expected decrease.** Each block principal matrix is the same strictly diagonally dominant tridiagonal matrix
\[
T_q=\operatorname{tridiag}(-t,1,-t).
\]
Set
\[
B_p=\sum_{j=0}^{n-1}p_jE_jT_q^{-1}E_j^{\mathsf T}.
\]
The block normal equation and Pythagorean identity give
\[
\|e\|_G^2-\mathbb E_p\|e^+\|_G^2=(Ge)^{\mathsf T}B_p(Ge),
\qquad
\Lambda(p)=\lambda_{\min}(G^{1/2}B_pG^{1/2}).
\]
No independence across future iterations is needed for this conditional calculation.

**2. A distribution-independent obstruction.** Write \(c=1-2t\) and \({\bf1}=(1,\dots,1)^{\mathsf T}\). Because \(G{\bf1}=c{\bf1}\) and \(E_j^{\mathsf T}{\bf1}={\bf1}_q\), every probability vector satisfies
\[
\frac{(G{\bf1})^{\mathsf T}B_p(G{\bf1})}{{\bf1}^{\mathsf T}G{\bf1}}
=\frac{c}{n}{\bf1}_q^{\mathsf T}T_q^{-1}{\bf1}_q=:\ell_q.
\]
Therefore \(\Lambda(p)\le\ell_q\) for **all** distributions \(p\), even ones omitting some intervals.

**3. Uniform sampling saturates the obstruction.** For each interval put \(L_j=I-E_jT_q^{-1}E_j^{\mathsf T}G\). Rows outside \(B_j\) equal corresponding rows of the identity. On rows inside \(B_j\) the within-block entries of \(L_j\) vanish, while its coefficients on exterior coordinates are \(-T_q^{-1}G_{B_j,B_j^c}\). Since \(T_q\) is an irreducible nonsingular \(M\)-matrix, \(T_q^{-1}\) is entrywise nonnegative, and the exterior coupling entries of \(G\) are nonpositive. Thus **every entry of \(L_j\) is nonnegative**.

Under uniform sampling, write \(B_u=n^{-1}\sum_j E_jT_q^{-1}E_j^{\mathsf T}\) and \(L_u=I-B_uG=n^{-1}\sum_jL_j\). Both \(B_u\) and \(G\) are real symmetric circulant, so they commute; hence \(L_u\) is symmetric. It is also entrywise nonnegative and circulant. Its constant row sum is \(1-\ell_q\), as follows from the preceding Rayleigh calculation and cyclic symmetry. For any nonnegative matrix, the spectral radius cannot exceed its maximum row sum; the constant vector is an eigenvector attaining that row sum. Thus \(\lambda_{\max}(L_u)=1-\ell_q\). Similarity of \(B_uG\) to \(G^{1/2}B_uG^{1/2}\) now yields \(\Lambda(u)=\ell_q\). This proves global minimax optimality and attainment of the worst-case direction \({\bf1}\).

**4. Explicit Dirichlet Green sum.** Put \(\cosh\alpha=(2t)^{-1}\). Solve \(T_qz={\bf1}_q\) with artificial boundary values \(z_0=z_{q+1}=0\). The unique solution is
\[
z_i=\frac{1}{1-2t}\left[1-\frac{\cosh\bigl(\alpha(i-(q+1)/2)\bigr)}{\cosh(\alpha(q+1)/2)}\right],\quad 1\le i\le q.
\]
Indeed, the constant part solves the inhomogeneous difference equation and the hyperbolic-cosine part solves its homogeneous recurrence; the displayed expression vanishes at both boundaries. Summing the finite hyperbolic-cosine progression gives
\[
(1-2t)\sum_{i=1}^q z_i=q-\frac{\sinh(q\alpha/2)}{\sinh(\alpha/2)\cosh((q+1)\alpha/2)}.
\]
Substitution into \(\ell_q=(1-2t)\sum_i z_i/n\) proves the stated closed formula for all \(n\ge3\) and \(1\le q<n\). In particular \(q=1\) gives \(\Lambda_*=(1-2t)/n\); \(q=2\) gives \(\Lambda_*=2(1-2t)/(n(1-t))\).

**5. Critical crossover.** Divide the exact expression for \(n\Lambda_*\) by \(q\), then let \(q\alpha\to s\) and \(\alpha\to0\). The factors satisfy \(q\sinh(\alpha/2)\to s/2\), \(\sinh(q\alpha/2)\to\sinh(s/2)\), and \(\cosh((q+1)\alpha/2)\to\cosh(s/2)\), proving \(F(s)\). Its derivative is positive because, with \(y=s/2>0\), \(\tanh y-y\operatorname{sech}^2y>0\), equivalent to \(\sinh(2y)>2y\). Taylor expansion and \(\tanh(s/2)\to1\) yield the two endpoint laws. Finally \(\alpha\sim\sqrt{2(1-2t)}\) as \(t\uparrow1/2\), giving the stated block-length scale. For fixed \(t\) and growing \(q<n\), the boundary loss also satisfies \(q-n\Lambda_*\to2e^{-\alpha}/(1-e^{-\alpha})\).

## Verification

The accompanying `verify.py` uses only the Python 3 standard library and can be executed with `python3 verify.py`. It checks exact rational block inverses, nonnegative symmetric mean update matrices, the constant-vector obstruction under nonuniform probabilities, block energy identities, special block lengths, and the critical/fixed-coupling limits. These tests check finite instances and numerical approximations only; the proof above establishes the universal finite-size and asymptotic claims. For reproduction, extract this file and `verify.py` from the same packaged finding.

## Relationship to prior work

Xie and Yang (arXiv:2610.04685v1, first public 2026-10-03) develop general randomized batch-coordinate sampling rules and convergence estimates for least squares. Their analysis motivates optimization of a fixed sampling law; their relevant mathematical sections and examples do not give the exact minimax contraction for every cyclic interval size of a periodic screened Laplacian, nor the critical hyperbolic crossover.

Tu and collaborators (arXiv:1701.03863) analyze accelerated block Gauss–Seidel and compare random and partition-based selection. Their full-text methods and numerical structured examples include circulant and tridiagonal families separately but do not supply the matched exact cyclic-contiguous Green-function law developed here. Wu (DOI:10.1137/17S015860) establishes general block Gauss–Seidel convergence under suitable block pavings; only accessible abstract-level material was inspected, so possible undiscovered equivalent coverage remains a bibliographic risk. General sketch-and-project identities are standard prior mathematics, not presented as new.

The new contribution is the complete explicit optimization over **all static distributions on overlapping consecutive cyclic blocks** and the accompanying universal transition in the block-length-to-correlation-length ratio, rather than the existence of randomized block contraction itself.

## Limitations

Only the real, nearest-neighbor, periodic screened-Poisson matrix family is covered. Intervals are contiguous, all have equal length, and local minimization is exact. The objective concerns the worst-case *one-step conditional expected squared-energy reduction*. No optimality is claimed for adaptive, error-dependent policies, nonconsecutive or irregular blocks, generalized Hessians, finite-precision updates, or wall-clock cost. The bound can be iterated to obtain an expected-energy upper bound, but an exact multistep worst-case rate is not asserted. No claim of bibliographic exhaustiveness or independent verification is made.

## References

1. D.-Y. Xie and X. Yang, *On randomized batch-sampling coordinate descent methods for solving linear least-squares problems*, arXiv:2610.04685v1 (2026-10-03), https://arxiv.org/abs/2610.04685.
2. S. Tu, S. Venkataraman, A. C. Wilson, A. Gittens, M. I. Jordan, and B. Recht, *Breaking Locality Accelerates Block Gauss-Seidel*, arXiv:1701.03863 (2017), https://arxiv.org/abs/1701.03863.
3. W. Wu, *Convergence of the Randomized Block Gauss-Seidel Method*, SIAM Undergraduate Research Online 11 (2018), DOI:10.1137/17S015860.
4. R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, SIAM J. Matrix Anal. Appl. 36 (2015), 1660–1690, arXiv:1506.03296.
