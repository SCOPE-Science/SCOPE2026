# Exact diagonal-scaling transition in a three-variable correlation block

## Finding

Let \(0<t<1\) and \(0<s<\sqrt{(1+t)/2}\), and define the positive-definite three-variable correlation matrix
\[
C_{t,s}=\begin{pmatrix}1&t&s\\t&1&s\\s&s&1\end{pmatrix}.
\]
For a real symmetric positive-definite matrix, let \(\kappa_2\) mean the quotient of the largest and smallest eigenvalues. Among **all** positive diagonal congruences \(D C_{t,s}D\), an optimum is attained by
\[
D_* =\operatorname{diag}(\sqrt{u_*},\sqrt{u_*},1)
\]
up to a common positive scalar. Set \(q=2t^2/(1+t)\). The optimal symmetric scaling is unique up to a common scalar, with
\[
u_*=
\begin{cases}
\dfrac{t-s^2}{t(1-t)},&0<s^2<q,\\[2mm]
\dfrac{1}{1+t},&q\le s^2<\dfrac{1+t}{2},
\end{cases}
\]
and its globally optimal spectral condition number is
\[
K_*=
\begin{cases}
\dfrac{t(1+t-2s^2)}{(1-t)(t-s^2)},&0<s^2<q,\\[2mm]
\dfrac{1+\sqrt{2}s/\sqrt{1+t}}{1-\sqrt{2}s/\sqrt{1+t}},&q\le s^2<\dfrac{1+t}{2}.
\end{cases}
\]
The formulas agree continuously at the transition. In the first regime the two **smallest** scaled eigenvalues coincide; in the second regime the symmetric two-by-two spectral block has equal diagonal entries.

Because the original correlation matrix already has unit diagonal, Jacobi preconditioning corresponds to \(D=I\). It attains the globally optimal condition number **if and only if** \(s=t\). In particular, unit diagonal alone does not make a symmetric positive-definite system optimally conditioned by diagonal scaling.

There are explicit nearly singular systems with an asymptotic 50% Jacobi penalty. For \(0<\varepsilon<1/4\), put \(t=1-\varepsilon^2\) and \(s=\sqrt{1-\varepsilon}\). Then
\[
K_* = \frac{2+\varepsilon-\varepsilon^2}{\varepsilon^2},
\qquad
\lim_{\varepsilon\downarrow0}\frac{\kappa_2(C_{t,s})}{K_*}=\frac32.
\]
This limit is **not** asserted to be a universal worst-case approximation constant outside this family or even a proved upper bound inside it.

## Assumptions and scope

All matrices are real. Both correlations \(t,s\) are strictly positive; the parameter bounds are strict and ensure \(C_{t,s}\succ0\). The optimization permits any diagonal matrix with three strictly positive entries, and no other preconditioners. Multiplying \(D\) by a positive scalar leaves \(\kappa_2(D C_{t,s}D)\) invariant. An optimal *symmetric* representative has its first two entries equal. The theorem asserts uniqueness only within this two-equal-entry representative class; it does not claim uniqueness of every nonsymmetric minimizing diagonal scaling.

This is **symmetric congruence preconditioning** of an SPD system, not arbitrary independent left-right scaling and not a statement about algorithmic iteration counts. The dimensions and two-parameter correlation structure are essential to the closed forms.

## Proof

**1. Positive definiteness and existence.** In the orthogonal basis \((e_1+e_2)/\sqrt2,e_3,(e_1-e_2)/\sqrt2\), \(C_{t,s}\) is the direct sum of
\[
\begin{pmatrix}1+t&\sqrt2s\\\sqrt2s&1\end{pmatrix}
\quad\text{and}\quad 1-t.
\]
The determinant of the displayed block is \(1+t-2s^2>0\), so all eigenvalues are positive. For any \(K\ge1\), a positive diagonal congruence of condition number at most \(K\) exists if and only if there is a positive diagonal \(W\) satisfying
\[
W\preceq C_{t,s}\preceq K W.
\]
Indeed, choose \(W=\lambda_{\min}(D C_{t,s}D)D^{-2}\) in one direction and \(D=W^{-1/2}\) in the other. Taking \(D=I\) gives finite feasible \(K\); at bounded \(K\), every feasible diagonal entry satisfies \(C_{ii}/K\le W_{ii}\le C_{ii}\), so compactness yields attainment of the minimal \(K\).

**2. Symmetry reduction without restricting the global search.** Let \(P\) exchange coordinates one and two. Since \(P C_{t,s}P=C_{t,s}\), whenever \(W\preceq C_{t,s}\preceq K W\), also \(PWP\) is feasible at the same \(K\). Averaging the two feasible diagonal matrices preserves both Loewner inequalities. Thus an optimal diagonal \(W\) with equal first two entries exists, hence an optimal congruence has the form \(D(u)=\operatorname{diag}(\sqrt u,\sqrt u,1)\) up to scale. This proves that minimizing over \(u>0\) determines the unrestricted optimum.

**3. Reduction to two competing eigenvalue ratios.** For \(u>0\), the scaled spectrum comprises
\[
a(u)=(1-t)u
\]
and the two eigenvalues \(\lambda_-(u)<\lambda_+(u)\) of
\[
B(u)=\begin{pmatrix}(1+t)u&\sqrt2s\sqrt u\\\sqrt2s\sqrt u&1\end{pmatrix}.
\]
Because \(t,s>0\), \(\lambda_+(u)>(1+t)u>a(u)\), and consequently
\[
\kappa_2(D(u)C_{t,s}D(u))
=\max\left\{\frac{\lambda_+(u)}{a(u)},\frac{\lambda_+(u)}{\lambda_-(u)}\right\}.
\]
The first ratio is strictly decreasing with \(u\). To see this, \(\lambda_+(u)/u\) is the largest eigenvalue of the positive-entry symmetric matrix
\[
\begin{pmatrix}1+t&\sqrt2s/\sqrt u\\\sqrt2s/\sqrt u&1/u\end{pmatrix};
\]
as \(u\) increases, its entries decrease, with strict decrease in an entry touched by the positive Perron eigenvector. The second ratio has its unique minimum at
\[
u_0=\frac1{1+t}.
\]
Indeed, for a positive-definite two-by-two matrix, the eigenvalue ratio is strictly increasing in \((\operatorname{tr} B)^2/\det B\), and here this quantity is
\[
\frac{((1+t)u+1)^2}{u(1+t-2s^2)},
\]
whose unique minimum occurs at \((1+t)u=1\). The second ratio strictly decreases before \(u_0\) and increases after it.

**4. Unique crossing and phase transition.** The relevant eigenvalue-order determinant is
\[
\det(B(u)-a(u)I)=2u\,[t-s^2-t(1-t)u].
\]
Because \(a(u)<\lambda_+(u)\), when this determinant is positive, \(a(u)<\lambda_-(u)\); when negative, \(a(u)>\lambda_-(u)\). If \(s^2\ge t\), there is no positive crossing and the second ratio controls the condition number at all \(u\). If \(s^2<t\), there is one crossing
\[
u_c=\frac{t-s^2}{t(1-t)}.
\]
For \(u<u_c\) the first ratio controls, and for \(u>u_c\) the second. Their monotonicities imply that the unique minimizer is \(u_0\) if \(u_c\le u_0\), and \(u_c\) if \(u_c>u_0\). Since
\[
u_c>u_0\quad\Longleftrightarrow\quad s^2<\frac{2t^2}{1+t},
\]
this is precisely the two-regime formula for \(u_*\). At the first-regime crossing, \(\lambda_-=a(u_c)\) and, by taking the two-by-two trace, \(\lambda_+=1+2tu_c\). Their quotient simplifies to the first formula for \(K_*\). At \(u=u_0\), the two diagonal entries of \(B(u_0)\) are both one, with eigenvalues \(1\pm\sqrt2s/\sqrt{1+t}\), giving the second formula. This establishes existence, global optimality and uniqueness within the symmetric scaling class.

**5. Jacobi criterion.** Since the unscaled diagonal entries all equal one, Jacobi gives \(u=1\). In the second regime the unique symmetric optimizer is \(u_0<1\). In the first regime, \(u_c=1\) if and only if \(t-s^2=t(1-t)\), equivalently \(s=t\) (both positive); this parameter choice lies strictly in the first regime because \(t<1\). Therefore Jacobi is globally optimal exactly at \(s=t\).

**6. Concrete and asymptotic examples.** At \(t=9/10\), \(s=4/5\), the weak-coupling branch applies, \(u_*=26/9\) and \(K_*=279/13\). The unit-diagonal condition number is
\[
\kappa_2(C_{9/10,4/5})=\frac{29+\sqrt{593}}{2}>\frac{279}{13}.
\]
For \(t=1-\varepsilon^2\), \(s=\sqrt{1-\varepsilon}\), with sufficiently small \(\varepsilon>0\), the first regime holds and the exact optimal quotient becomes \((2+\varepsilon-\varepsilon^2)/\varepsilon^2\). The antisymmetric unscaled eigenvalue equals \(\varepsilon^2\), and the other two eigenvalues tend to \(3\) and \(0\), the smaller being of order \(\varepsilon\). Consequently \(\kappa_2(C_{t,s})\sim3/\varepsilon^2\), yielding the displayed limit \(3/2\).

## Verification

The standalone \(\texttt{verify.py}\) checks the orthogonal block, crossing determinant, regime boundary and analytic formulas using exact symbolic arithmetic; checks the rational example and limit exactly; and compares the proposed global optimum to four numerical unrestricted two-variable minimizations for each of 160 reproducibly generated SPD parameter pairs. The successful output is

```text
VERIFY_OK symbolic=8 exact_example=1 asymptotic=1 global_numeric_cases=160 minimizations=640
```

Run \(\texttt{python verify.py}\) after installing the packages listed in \(\texttt{requirements.txt}\). These tests corroborate calculations but do **not** certify the infinite parameter domain; the proof above is the justification of global optimality.

## Relationship to prior work

Qu, Gao, Hinder, Ye and Zhou (arXiv:2209.00809, first submitted 2022-09-02) developed general quasiconvex and semidefinite formulations of optimal diagonal preconditioning. Jambulapati, Li, Musco, Sidford and Tian (arXiv:2008.01722, first submitted 2020-08-04) studied approximate optimal scaling and bounds for Jacobi. Ghadimi and collaborators (arXiv:2509.23439, first submitted 2025-09-27) established general optimality conditions, with the inspected version revised in 2026. These are the overarching methods, not claims of newness here. The contribution assessed here is the exact **two-parameter three-variable classification**, with its eigenvalue-collision transition, necessary-and-sufficient Jacobi optimality criterion, and explicit near-singular Jacobi comparison. Those formulas require special-case analysis beyond stating general convex optimization formulations.

## Limitations

No claim is made that all optimal diagonal matrices are symmetric, that the ratio \(3/2\) is a universal maximum, or that optimal condition-number scaling necessarily yields the fewest numerical iterations or best numerical stability in finite precision. The restriction \(t,s>0\) excludes negative-correlation phase geometry and boundary singularities. General optimal diagonal preconditioning is already studied extensively; this exact special-family calculation may overlap with unlocated specialized literature. Priority and independent validation have not been established.

## References

1. Z. Qu, W. Gao, O. Hinder, Y. Ye, Z. Zhou, *Optimal Diagonal Preconditioning*, arXiv:2209.00809 (2022). https://arxiv.org/abs/2209.00809
2. A. Jambulapati, J. Li, C. Musco, A. Sidford, K. Tian, *Fast and Near-Optimal Diagonal Preconditioning*, arXiv:2008.01722 (2020). https://arxiv.org/abs/2008.01722
3. S. Ghadimi, W. L. Jung, A. Sujanani, D. Torregrosa-Belén, H. Wolkowicz, *Optimal Diagonal Preconditioning Beyond Worst-Case Conditioning: Theory and Practice of Omega Scaling*, arXiv:2509.23439 (2025, revised 2026). https://arxiv.org/abs/2509.23439
