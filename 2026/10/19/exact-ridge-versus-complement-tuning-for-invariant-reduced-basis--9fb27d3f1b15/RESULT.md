# Exact ridge-versus-complement tuning for invariant reduced-basis preconditioners

## Finding

For a real symmetric positive-definite matrix \(A\in\mathbb R^{n\times n}\) and a nonzero proper invariant subspace \(U\), the two additive reduced-basis inverse preconditioners of Fan, Hu, and Zhang have a complete, dimension-independent scalar-tuning classification. Write \(P\) for any orthonormal basis of \(U\), \(\Pi=PP^{\mathsf T}\), and \(S=P(P^{\mathsf T}AP)^{-1}P^{\mathsf T}\). For \(\alpha>0\), define
\[
B_{\rm I}(\alpha)=S+\alpha I,\qquad B_{\rm II}(\alpha)=S+\alpha(I-\Pi).
\]
Let \(a\le b\) and \(c\le d\) be the respective extreme eigenvalues of the restrictions of \(A\) to \(U\) and \(U^\perp\), each nonempty. Set \(\kappa_j(\alpha)=\kappa_2(B_j(\alpha)^{1/2}A B_j(\alpha)^{1/2})\), where \(j\) is I or II. Then
\[
\inf_{\alpha>0}\kappa_{\rm I}(\alpha)=
\begin{cases}
\dfrac{\max\{b,d\}}{c},&c\le a,\\[4pt]
\dfrac{\max\{d,b+c-a\}}{c},&c>a,
\end{cases}
\qquad
\min_{\alpha>0}\kappa_{\rm II}(\alpha)=\frac dc.
\]
**In particular, Type I admits a strict condition-number improvement over unpreconditioned \(A\) for some positive \(\alpha\) if and only if \(c>a\).** If \(c\le a\), no \(\alpha>0\) improves the condition number, although the preconditioner is positive definite; the first displayed infimum then equals \(\kappa_2(A)\). The optimizers are explicit: when \(c>a\), every Type-I optimal reciprocal parameter \(s=1/\alpha\) belongs exactly to
\[
[c-a,\;\max\{c-a,d-b\}].
\]
When \(c\le a\), the infimum is reached precisely when \(d>b\) and \(0<s\le d-b\), otherwise only as \(s\downarrow0\) (equivalently \(\alpha\to\infty\)). Every Type-II minimizer satisfies \(1/d\le\alpha\le1/c\).

The distinction can be arbitrarily large: for \(A=\operatorname{diag}(K,1)\), \(K>1\), and \(U=\operatorname{span}\{e_1\}\), every Type-I preconditioned matrix has condition number greater than \(K\), approaching \(K\) as \(\alpha\to\infty\), whereas Type II at \(\alpha=1\) gives the identity matrix.

## Assumptions and scope

Here \(n\ge2\), \(A=A^{\mathsf T}\succ0\), and \(1\le\dim U<n\). Invariance means \(AU\subseteq U\); since \(A\) is self-adjoint, \(U^\perp\) is invariant as well. The endpoints \(a,b,c,d\) are positive and satisfy \(a\le b\), \(c\le d\). Repeated eigenvalues, single-dimensional subspaces, and endpoint equalities are included. No assertion is made when the reduced subspace is not invariant, when the matrix is indefinite/nonsymmetric, or when the objective is FGMRES wall-clock performance rather than spectral condition number.

## Proof

Since the subspaces reduce \(A\), simultaneous orthogonal block diagonalization yields \(S|_U=(A|_U)^{-1}\) and \(S|_{U^\perp}=0\). Hence \(B_{\rm I}(\alpha)A\) has eigenvalues \(1+\alpha\lambda\) for \(\lambda\in\sigma(A|_U)\) and \(\alpha\mu\) for \(\mu\in\sigma(A|_{U^\perp})\). Because \(A\) and \(B_{\rm I}\) commute, these are also the eigenvalues of the SPD symmetrically preconditioned matrix. Set \(s=1/\alpha\). Division by the positive \(\alpha\) gives the exact finite-dimensional formula
\[
\kappa_{\rm I}(1/s)=\frac{\max\{b+s,d\}}{\min\{a+s,c\}},\qquad s>0.
\tag{1}
\]
For Type II the corresponding spectral values are \(1\) on \(U\) and \(\alpha\mu\) on \(U^\perp\), giving
\[
\kappa_{\rm II}(\alpha)=\frac{\max\{1,\alpha d\}}{\min\{1,\alpha c\}}\ge d/c.
\tag{2}
\]
Equality in (2) is equivalent to \(\alpha c\le1\le\alpha d\), i.e. \(1/d\le\alpha\le1/c\).

If \(c\le a\), the denominator of (1) is constantly \(c\) and the numerator is nondecreasing in \(s\). Its limit as \(s\downarrow0\) is \(\max\{b,d\}/c\), which is also the original matrix condition number because \(c\) is its smallest eigenvalue. The numerator is constant at \(d\) on a nonempty positive interval exactly when \(d>b\), in which case the optimizers are \(0<s\le d-b\); otherwise the bound is approached but not attained.

If \(c>a\), put \(s_*=c-a>0\). For \(0<s\le s_*\), (1) is the maximum of \(d/(a+s)\) and \((b+s)/(a+s)\), both nonincreasing, and the maximum is strictly decreasing until \(s_*\): if the second term is constant, then \(b=a\), and \(d\ge c>a\) forces the strictly decreasing first term to dominate. For \(s\ge s_*\), the denominator is \(c\) and the numerator is nondecreasing. Thus the optimum occurs for \(s\in[s_*,\max\{s_*,d-b\}]\), where the numerator equals \(\max\{b+s_*,d\}\). This proves the second branch. Strict improvement over \(\kappa(A)=\max\{b,d\}/a\) follows from strict decrease immediately to the right of \(s=0\). Conversely when \(c\le a\) no improvement occurs, establishing the stated if-and-only-if criterion.

Finally in the displayed two-dimensional example the Type-I spectrum is \(\{1+\alpha K,\alpha\}\), whose ratio is \(K+1/\alpha>K\). The Type-II spectrum is \(\{1,\alpha\}\), giving unit condition number at \(\alpha=1\). Every extremum is therefore realizable by concrete SPD matrices.

## Verification

The companion `verify.py` checks the exact spectrum formulas and analytical minimizers against independently computed matrix eigenvalues for deterministic random positive diagonal systems, including repeated and interlaced spectra; it also verifies the unbounded separation family. The proof above is universal; finite numerical tests do not establish the theorem independently.

## Relationship to prior work

Fan, Hu, and Zhang, *Additive reduced basis preconditioners for large-scale parametrized PDEs* (arXiv:2609.11097, first posted 2026-09-10), define these Type-I and Type-II operators (their Equations (4) and (7)) and establish nonsingularity conditions and Richardson error bounds. The present finding does not claim these operators, reduced-basis projection, or the block decomposition as new. It identifies the exact optimal scalar regularization and a strict-improvement threshold on invariant SPD subspaces, an idealized test case for practical tuning. Pasetto et al. (2017) study another reduced-order-model preconditioner and condition numbers empirically, not the same two tuning laws. Existing approximate-inverse and deflation literature provides the broader conceptual context; a preexisting equivalent exact parameter classification in that literature remains a possibility.

## Limitations

Invariance makes the full operator spectrum explicitly decomposable; no unconditional noninvariant result is implied. The condition-number-optimal scalar may not minimize finite-precision cost, FGMRES iterations, or convergence for a particular right-hand side. The construction presumes exact reduced solves and exact arithmetic. The Type-I infimum is not always attained by a finite admissible scalar. Bibliographic nonuniqueness cannot be excluded merely from failed searches.

## References

1. X. Fan, Q. Hu, S. Zhang, *Additive reduced basis preconditioners for large-scale parametrized PDEs*, arXiv:2609.11097 (first public version 2026-09-10), Section 3.1, Eq. (4), Eq. (7), Section 3.4.
2. D. Pasetto et al., *A reduced order model-based preconditioner for the efficient solution of transient diffusion equations*, International Journal for Numerical Methods in Engineering (2017), DOI:10.1002/nme.5320, Sections 4–5.
3. L. González, *Orthogonal Projections of the Identity: Spectral Analysis and Applications to Approximate Inverse Preconditioning*, SIAM Review 48 (2006), 66–75, DOI:10.1137/S0036144504431905.
