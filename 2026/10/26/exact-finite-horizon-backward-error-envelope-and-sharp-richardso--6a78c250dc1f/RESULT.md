# Exact finite-horizon backward-error envelope and sharp Richardson overrelaxation window

## Finding

Define the **matrix-only normwise relative backward error** of a nonzero vector \(x\) for \(Ax=b\), with \(A\ne0\), by
\[
\operatorname{berr}_{A,b}(x)=\frac{\|Ax-b\|_2}{\|A\|_2\|x\|_2}.
\]
For an arbitrary real symmetric positive-semidefinite \(n\times n\) matrix \(A\ne0\), any \(b\ne0\) (including inconsistent systems), and every integer \(k\ge1\), start Richardson iteration from \(x_0=0\) and use the constant step \(\eta=\alpha/\|A\|_2\), with \(0<\alpha<2\). Its **exact universal worst-case backward-error envelope** is
\[
\mathcal E_k(\alpha):=
\sup_{n\ge1}\sup_{\substack{A=A^\top\succeq0,\,A\ne0\\b\ne0}}
\operatorname{berr}_{A,b}(x_k)
=\max\left\{\frac{1}{\alpha k},
\frac{|1-\alpha|^k}{1-(1-\alpha)^k}\right\}.
\tag{1}
\]
The denominator in the second term is positive for the specified range. The supremum is actually attained in dimensions at most two.

For every fixed integer \(k\ge2\), the unique minimizer of (1) over \(0<\alpha<2\) is \(\alpha_k=1+u_k\), where \(u_k\in(0,1)\) is the unique solution of
\[
 u_k^k\big(k(1+u_k)+(-1)^k\big)=1,
 \qquad \min_{0<\alpha<2}\mathcal E_k(\alpha)
 =\frac{1}{k(1+u_k)}.
\tag{2}
\]
In particular, \(\alpha_2=3/2\) gives the optimal two-step bound \(\mathcal E_2(3/2)=1/3\). Moreover,
\[
 \alpha_k=2-\frac{\log(2k)+o(1)}{k},\qquad
 \mathcal E_k(\alpha_k)\sim\frac{1}{2k}
 \quad (k\to\infty).
\tag{3}
\]
For \(k=1\), \(\mathcal E_1(\alpha)=1/\alpha\), so its infimum is \(1/2\) as \(\alpha\uparrow2\), without an admissible minimizer.

The original condition-number-independent guarantee \(\operatorname{berr}_{A,b}(x_k)\le1/k\) holds **simultaneously for all positive integers \(k\) and all such PSD systems** if and only if
\[
\boxed{1\le\alpha\le1+\frac1{\sqrt3}.}
\tag{4}
\]
Thus the maximal certified factor exceeds the customary unit-normalized step by about \(57.7\%\); violation above the upper endpoint is already witnessed after two steps on a scalar system.

## Assumptions and scope

All arithmetic is exact. No positive definiteness or consistency is required. The dimension may vary in the supremum, but the same fixed scalar \(\alpha\) is used in every instance; the step size uses the **exact** spectral norm \(\|A\|_2\). The backward-error definition permits perturbations to \(A\) but not to \(b\). Matrix scale, right-hand-side scale, and dimension do not affect the envelope. The conclusions concern \(0<\alpha<2\); no statement of uniform behavior at or beyond the spectral stability endpoint is needed. A zero initial vector is essential to the exact formula.

## Proof

Let \(M=\|A\|_2>0\), \(\eta=\alpha/M\), and \(T=I-\eta A\). The iteration gives \(x_k=\eta\sum_{j=0}^{k-1}T^jb\) and \(Ax_k-b=-T^kb\). In an orthonormal eigenbasis, write \(\beta=\eta\lambda\in[0,\alpha]\) and \(q=1-\beta\in(-1,1]\). The component multiplier for \(x_k\) is \(\eta s_k(q)\), where \(s_k(q)=1+q+\cdots+q^{k-1}>0\): this is immediate for \(q\ge0\), and for \(-1<q<0\) it follows from \(s_k(q)=(1-q^k)/(1-q)>0\). Therefore \(x_k\ne0\) whenever \(b\ne0\).

The ratio of residual to solution in an eigendirection, after division by \(M\), equals
\[
 g_{k,\alpha}(\beta)=
 \begin{cases}
  1/(\alpha k),&\beta=0,\\
  \displaystyle\frac{\beta}{\alpha}\,
   \frac{|1-\beta|^k}{1-(1-\beta)^k},&0<\beta\le\alpha.
 \end{cases}
\tag{5}
\]
The quotient of the full Euclidean norms is at most \(\max_{\beta\in\sigma(\eta A)}g_{k,\alpha}(\beta)\), because each diagonal residual multiplier is bounded by that multiple of the corresponding strictly positive solution multiplier.

For \(0<\beta<1\), put \(q=1-\beta\in(0,1)\). After cancellation,
\[
 \alpha g_{k,\alpha}(\beta)
 =\frac{q^k}{1+q+\cdots+q^{k-1}}
 =\left(\sum_{j=1}^kq^{-j}\right)^{-1}.
\tag{6}
\]
This expression increases with \(q\); hence it decreases with \(\beta\), and its limit as \(\beta\downarrow0\) is \(1/k\). At \(\beta=1\), it is zero. For \(1<\beta<2\), put \(u=\beta-1\in(0,1)\). Then
\[
 g_{k,\alpha}(\beta)=\frac{1+u}{\alpha}\,
 \frac{u^k}{1-(-1)^ku^k}.
\tag{7}
\]
Both factors are strictly increasing in \(u\), whether \(k\) is odd or even. Thus the supremum of the spectral ratios is the larger of the zero-eigenvalue limit \(1/(\alpha k)\) and the top-eigenvalue value \(|1-\alpha|^k/[1-(1-\alpha)^k]\); for \(\alpha\le1\) the latter does not exceed the former. This proves the upper bound (1). The first branch is **attained** by \(A=\operatorname{diag}(1,0)\), \(b=(0,1)^\top\), for which \(x_k=(0,k\alpha)^\top\). The second branch is **attained** by the scalar \(A=(1)\), \(b=(1)\). Consequently the upper bound is exact, including the inconsistent case that enforces its low-frequency term.

To optimize for fixed \(k\ge2\), first note that \(\alpha\le1\) cannot improve on \(1/k\). On \(1<\alpha<2\), the first branch \(1/(\alpha k)\) decreases strictly, whereas by (7) the second branch increases strictly from zero to a value exceeding \(1/(2k)\). Their unique intersection minimizes the maximum. Writing \(\alpha=1+u\) and cross-multiplying yields (2). The equation has exactly one root in \((0,1)\), since its left-hand side is strictly increasing from zero to \(2k+(-1)^k>1\). For \(k=2\), \(u=1/2\) solves \(u^2(3+2u)=1\), giving \(1/3\). For \(k=1\), (1) reduces to \(1/\alpha\) on \(0<\alpha<2\). As \(k\to\infty\), the root must satisfy \(u_k\to1\): any subsequence bounded away from one contradicts (2). Therefore \(u_k^k=(2k+o(k))^{-1}\). Taking logarithms gives \(k\log u_k=-\log(2k)+o(1)\), whence \(1-u_k=[\log(2k)+o(1)]/k\), proving (3).

For the all-horizon threshold, the zero-eigenvalue example forces \(\alpha\ge1\). Write \(u=\alpha-1\ge0\). If the bound \(1/k\) is to hold at \(k=2\) for the scalar top-eigenvalue witness, then \(u^2/(1-u^2)\le1/2\), equivalently \(u\le1/\sqrt3\). Conversely assume \(0\le u\le1/\sqrt3\). The low branch obeys \(1/(\alpha k)\le1/k\). For even \(k\ge2\), the upper branch satisfies \(u^k/(1-u^k)\le1/k\) precisely when \((k+1)u^k\le1\); this follows from \((k+1)3^{-k/2}\le1\), with equality at \(k=2\), and the left side decreases when \(k\) advances by two. For odd \(k\ge1\), the corresponding condition is \((k-1)u^k\le1\), guaranteed by \((k-1)3^{-k/2}\le1\) (trivial at \(k=1\), strictly decreasing over odd \(k\ge3\)). This proves (4), including both sharp boundary witnesses.

## Verification

The self-contained script `check.py` tests the precise endpoint examples, the optimal two-step value, root uniqueness numerically for selected horizons, spectral-envelope inequalities over finite grids and randomized diagonal PSD systems, and the exact transition at \(1+1/\sqrt3\). These computations corroborate the formula; the infinite-dimensional-uniform supremum and the all-integer statement are proved analytically above.

## Relationship to prior work

Dereziński, Nakatsukasa, and Rebrova (2026, arXiv:2604.16075, Section 3.2) establish a condition-number-free \(1/k\) backward-error guarantee for unit-normalized Richardson and more conservative steps. The new statement optimizes a **different, unaddressed parameter range** \(1<\eta\|A\|_2<2\): it determines the exact worst-case envelope at each horizon, its unique horizon-optimal stepsize, and the maximal overrelaxation retaining the original all-horizon \(1/k\) bound. The spectral-polynomial manipulation is related, but the oscillating negative Richardson modes and sharp competing null/top spectral witnesses are essential here.

Classical Richardson tuning minimizes the spectral radius of \(I-\eta A\) on a specified **positive-definite spectral interval**, and therefore depends on the smallest positive eigenvalue. The present minimax objective instead measures matrix-only backward error across all PSD matrices, including singular inconsistent systems, so the classical forward-error optimality formula does not imply (1)–(4).

## Limitations

The result uses the matrix-only normwise backward error; allowing perturbations of \(b\) changes the objective. It assumes exact spectral norm knowledge, fixed steps, zero initialization, exact arithmetic, and real symmetric PSD matrices. It does not imply a corresponding worst-case constant for nonsymmetric matrices, finite-precision implementations, forward error, or a fixed prescribed positive spectral gap. Existing larger-step analyses specialized to other metrics may provide partial intuition but do not by themselves settle this minimax criterion. Full bibliographic exclusion of every historical equivalent formulation has not been independently certified.

## References

1. M. Dereziński, Y. Nakatsukasa, and E. Rebrova, *Towards Universal Convergence of Backward Error in Linear System Solvers*, arXiv:2604.16075, first version 17 April 2026. https://arxiv.org/abs/2604.16075 ; Section 3.2 (Richardson) and Section 3.1 (backward-error definition).
2. D. Bindel, *CS 6210: Matrix Computations — Stationary iterations*, Cornell University lecture notes, 10 November 2025. https://www.cs.cornell.edu/courses/cs6210/2025fa/lec/2025-11-10.html ; the Richardson spectral-radius tuning section.
3. N. J. Higham, *Accuracy and Stability of Numerical Algorithms*, 2nd edition, SIAM, 2002; standard matrix-only normwise backward-error identity (cited by Reference 1).
