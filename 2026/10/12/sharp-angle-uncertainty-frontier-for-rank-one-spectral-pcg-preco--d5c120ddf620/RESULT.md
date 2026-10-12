# Sharp angle-uncertainty frontier for rank-one spectral PCG preconditioning

## Finding

For every real symmetric positive-definite matrix of order two with distinct eigenvalues \(L>\mu>0\), write \(r=\mu/L\in(0,1)\), and let \(u_L\) be a unit eigenvector for \(L\). Suppose a preconditioning direction \(v\) is only known to be a unit vector with
\[
0\le t:=1-|u_L^{\mathsf T}v|^2\le T,\qquad 0\le T\le1.
\]
Choose one positive scalar \(q\), *without knowing the actual direction inside that angular uncertainty set*, and apply one exact preconditioned conjugate-gradient (PCG) step to \(Ax=b\) with inverse preconditioner
\[
F_q=I+(q-1)vv^{\mathsf T},\qquad q>0.
\]
For a nonzero initial error \(e_0=x_\star-x_0\), let \(e_1=x_\star-x_1\) and \(\|e\|_A^2=e^{\mathsf T}Ae\). The exact worst-case squared-energy contraction for fixed \(q,t\) is
\[
\mathcal Q(q,t):=\sup_{e_0\ne0}\frac{\|e_1\|_A^2}{\|e_0\|_A^2}
=1-\frac{4rq}{\bigl[q+r+(1-q)(1-r)t\bigr]^2}.
\]
The optimization \(\inf_{q>0}\sup_{0\le t\le T}\mathcal Q(q,t)\) has a **unique** minimizer:
\[
q_\star(r,T)=
\begin{cases}
\dfrac{r+(1-r)T}{1-(1-r)T},&0\le T<\tfrac12,\\[5pt]
1,&\tfrac12\le T\le1.
\end{cases}
\]
Its exact minimized contraction factor is
\[
\mathcal Q_\star(r,T)=
\begin{cases}
\dfrac{(1-r)^2T(1-T)}{r+(1-r)^2T(1-T)},&0\le T<\tfrac12,\\[5pt]
\left(\dfrac{1-r}{1+r}\right)^2,&\tfrac12\le T\le1.
\end{cases}
\]
Consequently, an angular guarantee strictly below \(45^\circ\) is **necessary and sufficient** for a nontrivial uniform improvement over unpreconditioned one-step CG by some rank-one multiplier in this uncertainty model. If \(T\ge\frac12\), the unique robust optimizer is to make **no correction**, \(q=1\).

The nominal exact-eigenvector choice \(q=r\) has a much more restrictive sharp improvement frontier:
\[
\sup_{0\le t\le T}\mathcal Q(r,t)
<\mathcal Q(1,0)
\quad\Longleftrightarrow\quad
T<\frac{\sqrt r}{(1+\sqrt r)^2}.
\]
At equality its worst-case loss equals that of unpreconditioned CG, and above equality it is strictly worse. For fixed \(c>0\), if \(T=cr\), then
\[
\lim_{r\downarrow0}\mathcal Q_\star(r,cr)=\frac{c}{1+c}.
\]
Thus uniform contraction bounded away from one as \(r\downarrow0\) is equivalent, for a family of admissible uncertainties \(T(r)\in[0,1]\), to \(T(r)=O(r)\). The fourth-root accuracy threshold for the *nominal* parameter is different from this square-root angular accuracy scale for *robust, well-conditioned convergence*.

## Assumptions and scope

The model uses real matrices of size exactly \(2\times2\), exact arithmetic, one PCG step, and a single preconditioning multiplier chosen before observing the direction \(v\). The direction can be any unit vector satisfying \(0\le t\le T\). The scalar \(r\in(0,1)\) is known; the signs of eigenvectors are immaterial. A positive inverse preconditioner \(F_q\) is assumed, with **no restriction** to multipliers below one. The worst case includes every nonoptimal initial iterate and, equivalently, every nonzero error, for each admissible \(v\). The optimization is on the squared energy ratio, not the Euclidean error, residual norm, or runtime. A first PCG step coincides with preconditioned steepest descent, with search direction \(p_0=F_q(b-Ax_0)\) and exact line search.

Both eigenvalues may be rescaled by their common factor; this is why only their ratio \(r\) appears. No estimate for larger matrices or for repeated iterations is claimed.

## Proof

**1. Reduction to trace and determinant.** Orthogonally change basis and divide \(A\) by \(L\). We may assume \(A=\operatorname{diag}(1,r)\). A representative admissible direction is \(v=(\sqrt{1-t},\sqrt t)^{\mathsf T}\), because all signs disappear from the spectrum. Put \(U_q=F_q^{1/2}\) and \(B=U_qAU_q\). Then \(F_q\) has eigenvalues \(q\) and \(1\), so \(\det B=rq\); and a direct trace calculation yields
\[
\operatorname{tr}B=q+r+(1-q)(1-r)t.
\]
These two invariants determine the ordered eigenvalues \(0<\alpha\le\beta\) of \(B\).

**2. Exact worst first-step energy ratio.** Transform the error via \(e=U_q y\). The original energy is \(\|e\|_A^2=y^{\mathsf T}By\), and the first PCG update becomes exact steepest descent for \(B\). In the eigenbasis of \(B\), define nonnegative energy weights \(w_\alpha=\alpha y_\alpha^2\) and \(w_\beta=\beta y_\beta^2\). The exact line search yields
\[
\frac{\|e_1\|_A^2}{\|e_0\|_A^2}
=1-\frac{(\alpha w_\alpha+\beta w_\beta)^2}
{(\alpha^2w_\alpha+\beta^2w_\beta)(w_\alpha+w_\beta)}.
\]
The elementary two-point Kantorovich inequality bounds the subtracted fraction below by \(4\alpha\beta/(\alpha+\beta)^2\). Equality is achieved by weights proportional to \(w_\alpha=\beta\), \(w_\beta=\alpha\). Hence the actual supremum, with no looseness, is
\[
\left(\frac{\beta-\alpha}{\beta+\alpha}\right)^2
=1-\frac{4\det B}{(\operatorname{tr}B)^2},
\]
proving the displayed formula for \(\mathcal Q(q,t)\). If \(\alpha=\beta\), the first step solves exactly and the same formula gives zero.

**3. Worst direction and minimax multiplier.** For fixed \(q>0\), the positive trace \(d(q,t)=q+r+(1-q)(1-r)t\) is increasing in \(t\) when \(q<1\), constant when \(q=1\), and decreasing when \(q>1\). Since \(\mathcal Q(q,t)=1-4rq/d(q,t)^2\), the worst direction is \(t=T\) if \(q<1\), and \(t=0\) if \(q>1\). At \(q=1\), every direction is equivalent.

For \(q\in(0,1]\), the relevant denominator is
\[
d(q,T)=a_Tq+b_T,
\quad a_T=1-(1-r)T>0,
\quad b_T=r+(1-r)T>0.
\]
Minimizing \(\mathcal Q(q,T)\) amounts to maximizing \(q/(a_Tq+b_T)^2\); differentiating gives the unique unrestricted maximizer \(q=b_T/a_T\). The condition \(b_T/a_T<1\) is exactly \(T<\frac12\). When \(T\ge\frac12\), this objective improves throughout \((0,1]\) and is minimized as a loss at \(q=1\). On \(q\in[1,\infty)\), the worst loss is \(\mathcal Q(q,0)\), and \(q/(q+r)^2\) strictly decreases for \(q>1\) since \(r<1\). Thus \(q=1\) uniquely minimizes that branch. Combining the branches proves uniqueness globally and the sharp \(45^\circ\) frontier.

For \(T<\frac12\), substitute \(q=b_T/a_T\) into the expression: since \(a_Tb_T=r+(1-r)^2T(1-T)\),
\[
1-\mathcal Q_\star(r,T)=\frac{r}{r+(1-r)^2T(1-T)}.
\]
For \(T\ge\frac12\), use \(q=1\) and obtain the ordinary CG factor.

**4. The nominal-multiplier hazard.** With \(q=r<1\), the worst angle is \(t=T\), with trace \(2r+(1-r)^2T\). Compare its factor against \(\mathcal Q(1,0)=((1-r)/(1+r))^2\). Taking the positive square roots of the equivalent trace inequalities yields
\[
2r+(1-r)^2T<\sqrt r\,(1+r),
\]
which rearranges exactly to \(T<\sqrt r/(1+\sqrt r)^2\). Equality and reversal give the remaining cases. This threshold is asymptotically \(T\asymp\sqrt r\), i.e., an angular-error scale \(r^{1/4}\), and is not the minimax robust threshold.

**5. Small-curvature boundary.** For fixed \(c>0\) and sufficiently small \(r\), \(T=cr<\frac12\); direct substitution gives \(\mathcal Q_\star(r,cr)\to c/(1+c)\). Conversely, when \(T(r)/r\to\infty\), the formula on \(T<\frac12\), or the unpreconditioned formula on \(T\ge\frac12\), forces \(\mathcal Q_\star\to1\). For a family with \(T(r)\le Cr\) and sufficiently small \(r\), monotonicity of the explicit loss in \(T\in[0,\frac12]\) yields an upper limit \(C/(1+C)<1\). This proves the stated equivalence.

## Verification

Execute `python verify.py` from the directory containing `verify.py`, with NumPy installed (see `requirements.txt`). It separately reconstructs the preconditioned matrix spectrum and first PCG step, including explicitly constructed worst-case errors, rather than simply reevaluating the scalar formula. It also checks thousands of exact-rational trace, determinant, and minimax relations against independent algebraic representations; samples nonoptimal competing multipliers; and evaluates the nominal-angle and small-curvature boundaries.

The packaged run printed:

```
VERIFY_OK rational_matrix_and_minimax_identities= 15444
VERIFY_OK independent_eigensystem_and_worst_PCG_cases= 2400
VERIFY_OK robust_minimax_sample_cases= 850
VERIFY_OK exact_nominal_safety_threshold_and_small_curvature_limits=1
```

The exact analytical arguments above establish all quantified statements. The tests are supplementary checks, not proofs by enumeration. All code uses deterministic random seeds.

## Relationship to prior work

Diouane, Gürol, Mouhtal, and Orban (2026, arXiv:2603.28969v1) study eigenvalue-clustering inverse preconditioners for CG with a prescribed iteration budget. Their Section 3 studies exact eigenvector directions, optimal spectral placement, and an energy-error guarantee under that exact-eigendirection model. Their 2024 precursor (arXiv:2410.02204v1, Section 4) already introduced scaled spectral preconditioning with exact eigenvectors. Both are credited for the inverse-preconditioner construction and the short-budget objective; the exact-versus-inexact distinction is material.

Kahl and Rittich (2016, *The Deflated Conjugate Gradient Method: Convergence, Perturbation and Accuracy*) analyze how approximate deflation subspaces affect *projective deflated CG* and give an angle-dependent effective-condition estimate. Projective deflation is not the positive-definite rank-one spectral multiplier considered here; the cited bound does not itself yield this minimax multiplier or the \(45^\circ\) frontier. Classic Kantorovich/steepest-descent estimates supply the well-known two-eigenvalue one-step error formula; that formula itself is not claimed as new. The contribution is the complete, uncertainty-aware optimizing classification, together with the separate nominal-scaling boundary and small-curvature scaling regime.

## Limitations

This is a sharp model result for one exact-arithmetic step in dimension two, not a universal high-dimensional PCG guarantee. It controls the worst initial error and the worst unit direction in a prescribed angular cap, and so may be pessimistic for particular right-hand sides, stochastic direction distributions, or restarted solvers. The direction angle and spectral ratio must be bounded to choose the robust parameter. No claims are made about reliably estimating those quantities, full PCG iteration counts, finite precision, or operation cost. The connection with existing angle-perturbation preconditioning literature leaves a residual risk of an equivalent older two-mode specialization; searches and primary-source comparisons are not a proof of exhaustive priority.

## References

1. Y. Diouane, S. Gürol, O. Mouhtal, and D. Orban, *A Spectral Preconditioner for the Conjugate Gradient Method with Iteration Budget*, arXiv:2603.28969v1, first submitted 2026-03-30. https://arxiv.org/html/2603.28969v1
2. Y. Diouane, S. Gürol, O. Mouhtal, and D. Orban, *An Efficient Scaled Spectral Preconditioner for Sequences of Symmetric Positive Definite Linear Systems*, arXiv:2410.02204v1, first submitted 2024-10-03. https://arxiv.org/html/2410.02204v1
3. K. Kahl and H. Rittich, *The Deflated Conjugate Gradient Method: Convergence, Perturbation and Accuracy*, 2016. https://www.imacm.uni-wuppertal.de/fileadmin/imacm/preprints/2016/imacm_16_27.pdf
4. L. Bergamaschi, *A Survey of Low-Rank Updates of Preconditioners for Sequences of Symmetric Linear Systems*, Algorithms 13 (2020), article 100. https://www.mdpi.com/1999-4893/13/4/100 (survey consulted via indexed excerpts; full text not independently reviewed).
