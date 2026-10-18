# A sharp graph-Gram frontier and a residual-consistency barrier for row-split least squares

## Finding

An approximate trailing-row factor in a row-split least-squares problem has two qualitatively distinct uses: as a **positive-definite Gram preconditioner applied to the true normal residual**, or as a **substitute for the trailing-row factor inside the residual itself**. The first admits an exact sharp, dimension-free convergence guarantee. The second need not preserve the least-squares stationary point, however small the factor error.

**Theorem (sharp approximation-error frontier, including attainability).** Let \(n,k\geq1\), \(A_1\in\mathbb R^{n\times n}\) be nonsingular, \(A_2\in\mathbb R^{k\times n}\), and \(A=[A_1^{\mathsf T},A_2^{\mathsf T}]^{\mathsf T}\). Define the true trailing-row factor \(Y=A_2A_1^{-1}\). Suppose that the available factor \(W\in\mathbb R^{k\times n}\) satisfies \(\|Y-W\|_2\leq\varepsilon\), where \(\varepsilon\geq0\). Set

\[
C=I+Y^{\mathsf T}Y,\qquad M=I+W^{\mathsf T}W,\qquad
\phi=\frac{\sqrt{4+\varepsilon^2}+\varepsilon}{2}.
\]

Every generalized eigenvalue of \((C,M)\), and equivalently of \((A^{\mathsf T}A,A_1^{\mathsf T}MA_1)\), belongs to the **optimal common enclosure**

\[
\boxed{\phi^{-2}\leq\lambda\leq\phi^2.}
\]

In particular, the preconditioned spectral condition number is at most \(\phi^4\). For every \(\varepsilon>0\), the two spectral endpoints and the condition-number bound are attained **simultaneously** with \(n=k=2\); when \(\varepsilon=0\), both matrices coincide and the bounds equal one.

Write \(G=A_1^{\mathsf T}MA_1\) and \(F(x)=\tfrac12\|Ax-b\|_2^2\). The iteration that keeps the exact normal residual,

\[
\boxed{x_{j+1}=x_j+\tau G^{-1}A^{\mathsf T}(b-Ax_j),}
\]

has \(G\)-energy error contraction factor no greater than

\[
R_\varepsilon(\tau)=
\max\bigl\{|1-\tau\phi^{-2}|,\,|1-\tau\phi^2|\bigr\}.
\]

This worst-case contraction factor is attained for **each** real \(\tau\). Thus the iteration converges geometrically for every admissible problem, right-hand side and starting point if and only if \(0<\tau<2\phi^{-2}\). Among constant stepsizes, the exact and unique minimax choice is

\[
\boxed{\tau_*=\frac{2}{2+\varepsilon^2},\qquad
R_\varepsilon(\tau_*)=
\frac{\varepsilon\sqrt{4+\varepsilon^2}}{2+\varepsilon^2}.}
\]

For \(\varepsilon=0\), this says \(\tau_*=1\) and gives the exact one-step least-squares solution. For \(\varepsilon>0\), this is a positive rate strictly below one. These constants require **no a priori bound** on \(\kappa_2(A_1)\) or \(\kappa_2(A)\).

**Residual-consistency clause.** Define the idealized row-split residual correction

\[
H_W(r_1,r_2)=A_1^{-1}M^{-1}(r_1+W^{\mathsf T}r_2).
\]

It factors through the exact normal residual \(A^{\mathsf T}r\) by a fixed linear map for every residual \(r=(r_1,r_2)\) **if and only if \(W=Y\)**. For \(W\ne Y\), there is a true normal-residual-zero vector \(r\) for which \(H_W(r)\ne0\). Indeed, even with \(n=k=1\), positive \(A_2\) and positive \(W\), arbitrarily small nonzero \(\|W-Y\|_2\) permits an inconsistent least-squares instance and points arbitrarily close to its unique minimizer at which \(H_W\) is a **strict ascent direction for every positive step length**. This clause describes an exact-top-block specialization of the algebraic residual form; it is not a claim about every implementation of incomplete factorization.

## Assumptions and scope

All matrices are real, all inverse operations are exact, and the error model controls the absolute operator two-norm \(\|W-Y\|_2\), not a relative entrywise or factorwise error. The split has a square nonsingular upper block, so \(A\) has full column rank and \(F\) has a unique least-squares minimizer \(x_*\), even if the equations are inconsistent. There is no distributional or sparsity assumption on \(W\); it need not arise from a particular factorization algorithm. The interval is a universal *a priori* spectral enclosure, not a claim that every fixed pair has endpoint eigenvalues. The uniform iteration guarantee is in the norm \(\|v\|_G=(v^{\mathsf T}Gv)^{1/2}\).

The residual-consistency comparison holds the upper-block factor exact while perturbing the trailing-row factor. It analyzes algebraic correction vectors, not the complete, possibly flexible, inner-outer Krylov algorithm.

## Proof

**Step 1: exact normalization.** From \(A_2=YA_1\) and \(A=[A_1^{\mathsf T},A_2^{\mathsf T}]^{\mathsf T}\),

\[
A^{\mathsf T}A=A_1^{\mathsf T}(I+Y^{\mathsf T}Y)A_1=A_1^{\mathsf T}CA_1.
\]

Both \(C\) and \(M\) are positive definite. Changing variables by the invertible \(A_1\) preserves generalized eigenvalues, so it suffices to bound the Rayleigh ratio for \((C,M)\).

**Step 2: the exact scalar envelope.** Put \(p=\phi\), so \(p-p^{-1}=\varepsilon\) and \(p\geq1\). For every \(t\geq0\), the following identity holds *exactly*:

\[
\boxed{p^2(1+t^2)-\bigl(1+(t+\varepsilon)^2\bigr)
=\varepsilon p(t-p^{-1})^2\geq0.}
\]

For nonzero \(v\), put \(a=\|Yv\|_2/\|v\|_2\) and \(t=\|Wv\|_2/\|v\|_2\). The reverse triangle inequality implies \(|a-t|\leq\varepsilon\). Consequently,

\[
\frac{v^{\mathsf T}Cv}{v^{\mathsf T}Mv}
=\frac{1+a^2}{1+t^2}
\leq\frac{1+(t+\varepsilon)^2}{1+t^2}\leq p^2.
\]

Interchanging \(Y\) and \(W\) gives the reverse bound \(p^{-2}\). Extremizing Rayleigh quotients gives the complete generalized spectral interval. Its condition-number bound is the ratio of the endpoints, at most \(p^4\).

**Step 3: simultaneous endpoint construction.** For \(\varepsilon>0\) take \(n=k=2\), \(A_1=I\), and

\[
Y=\operatorname{diag}(p,p^{-1}),\qquad
W=\operatorname{diag}(p^{-1},p).
\]

Then \(\|Y-W\|_2=p-p^{-1}=\varepsilon\) and the generalized eigenvalues are exactly \(p^2,p^{-2}\). Both interval endpoints, the condition-number bound, and the worst-case Richardson factor are therefore attained by this one fixed pair.

**Step 4: sharp iteration threshold and step choice.** Subtract the normal equations at \(x_*\) from the proposed update. The error \(e_j=x_j-x_*\) satisfies

\[
e_{j+1}=(I-\tau G^{-1}A^{\mathsf T}A)e_j.
\]

The matrix \(G^{1/2}(I-\tau G^{-1}A^{\mathsf T}A)G^{-1/2}\) is the symmetric matrix \(I-\tau G^{-1/2}A^{\mathsf T}AG^{-1/2}\), whose eigenvalues are \(1-\tau\lambda\) with \(\lambda\in[p^{-2},p^2]\). Hence the induced \(G\)-norm is bounded by \(R_\varepsilon(\tau)\). The endpoint construction attains this bound for every \(\tau\) upon choosing an eigenvector of the worse endpoint. All such linear iterations converge for every admissible matrix exactly when both endpoint factors lie strictly inside the unit circle: \(0<\tau<2p^{-2}\). Otherwise that same construction has a noncontracting or divergent eigenmode, establishing necessity. The minimax positive \(\tau\) equates the absolute endpoint factors with opposite signs, yielding \(\tau_*=2/(p^2+p^{-2})\) and \((p^2-p^{-2})/(p^2+p^{-2})\). Since \(p^2+p^{-2}=2+\varepsilon^2\) and \(p^2-p^{-2}=\varepsilon\sqrt{4+\varepsilon^2}\), the displayed formulas follow. Equality of affine endpoint magnitudes characterizes the unique minimizer, also at \(\varepsilon=0\).

**Step 5: residual-consistency characterization.** By Woodbury's identity, the exact-top-block specialization of a correction based on \(I+WW^{\mathsf T}\) simplifies algebraically to \(H_W\) as defined above. The true gradient residual is \(A^{\mathsf T}r=A_1^{\mathsf T}(r_1+Y^{\mathsf T}r_2)\). If \(W=Y\), then \(H_Y(r)=G^{-1}A^{\mathsf T}r\), a linear function of the normal residual. Conversely, if \(W\ne Y\), choose \(u\in\mathbb R^k\) with \((W-Y)^{\mathsf T}u\ne0\). For

\[
r_2=u,\qquad r_1=-Y^{\mathsf T}u,
\]

one has \(A^{\mathsf T}r=0\) but \(H_W(r)=A_1^{-1}M^{-1}(W-Y)^{\mathsf T}u\ne0\). Thus no fixed linear map of \(A^{\mathsf T}r\) can produce \(H_W(r)\) for every residual unless \(W=Y\).

**Step 6: arbitrarily small error yields ascent.** Set \(n=k=1\), \(A_1=1\), \(A_2=a>0\), \(W=w=a+\delta>0\), and choose any \(R\ne0\) and nonzero \(\delta\) as small as desired. Take \(b_1=-aR\) and \(b_2=R\). The exact least-squares minimizer is \(x_*=0\), and for \(x=e\) the true normal residual and the mismatched correction are

\[
z(e)=-(1+a^2)e,\qquad
h(e)=H_w(b-Ae)=\frac{\delta R-(1+aw)e}{1+w^2}.
\]

Choose \(e\) with the sign of \(\delta R\) and \(0<|e|<|\delta R|/(1+aw)\). Then \(e\) and \(h(e)\) have the same sign, while \(z(e)\) has the opposite sign. For every \(\tau>0\), the objective change is

\[
F(e+\tau h(e))-F(e)
=-\tau z(e)h(e)+\frac{\tau^2}{2}(1+a^2)h(e)^2>0.
\]

The mismatched stationary point is \(e_{\mathrm{bias}}=\delta R/(1+aw)\); its excess objective is \((1+a^2)e_{\mathrm{bias}}^2/2\). Sending \(\delta\) and then \(e\) to zero completes the claim.

## Verification

The included standalone script `verify_row_split.py` checks the two-sided generalized eigenvalue enclosure, the endpoint construction, condition-number and optimal-step identities, and the mismatched-residual ascent and stationary-bias formulas. The script completed **15,198 deterministic numerical assertions** using NumPy; a separate symbolic expansion also verified the completed-square identity exactly. These finite checks are reproducibility aids. All universal quantifiers, simultaneous sharpness and convergence statements follow from the preceding algebraic argument, not from finite sampling.

Run `python3 verify_row_split.py` with NumPy installed. The script uses a fixed pseudo-random seed and reports `PASSED 15198 checks` when successful.

## Relationship to prior work

Scott and Tůma (2026, arXiv:2603.28642v1, Sections 3.1–3.2, Algorithm 3) formulate the row-splitting factor \(Y\), its incomplete analogue, and a correction calculated from the two residual blocks. Those constructions are prior work. The present statement examines the exact-upper-block specialization under a directly measurable operator-norm error in the trailing factor; it does not claim their preconditioning construction as new.

The column-space preservation condition for non-normal least-squares equations is classical; Wathen (2025, DOI:10.1137/23M161851X, Section 2) establishes it explicitly. In particular, the necessity of preserving the normal-residual kernel is not itself claimed as an original general observation. Garrison and Ipsen (2026, arXiv:2603.16644v1, Sections 3–5) prove perturbation bounds for mixed-precision preconditioned normal and not-normal equations with different perturbation models. The result here instead supplies simultaneous optimal, absolute-error-controlled graph-Gram eigenvalue endpoints, their exact scalar minimax fixed-step consequence, and a matched residual-channel contrast for the row-split construction. No coverage from these three inspected texts of that combined exact statement was identified. Equivalent formulations through standard shear-matrix norm inequalities remain a significant prior-work risk.

## Limitations

The result is **not** a convergence analysis of every ILU or flexible Krylov implementation. It assumes the upper block is solved exactly, fixed \(W\), an absolute norm bound on the trailing-factor error, and exact arithmetic. Applying the true normal residual costs an evaluation of \(A^{\mathsf T}r\); the theorem does not compare wall-clock time, memory, fill levels, or floating-point backward error. The uniformly optimal step minimizes a worst-case one-step \(G\)-norm bound, not the iteration count of conjugate gradients or the cost of obtaining \(W\). The column-space obstruction is classical, and the sharp spectral calculation may have an equivalent formulation in older perturbation literature not located here.

## References

1. J. Scott and M. Tůma, *Row-Splitting ILU Preconditioners for Sparse Least-Squares Problems*, arXiv:2603.28642v1, first posted 2026-03-30; especially Sections 3.1–3.2 and Algorithm 3. https://arxiv.org/html/2603.28642v1
2. A. J. Wathen, *Least Squares and the Not-Normal Equations*, SIAM Review, DOI:10.1137/23M161851X; especially Section 2, equations (2.2)–(2.3). https://epubs.siam.org/doi/10.1137/23M161851X
3. J. E. Garrison and I. C. F. Ipsen, *Perturbation Analysis for Preconditioned Normal Equations in Mixed Precision*, arXiv:2603.16644v1, 2026; especially Sections 3–5. https://arxiv.org/html/2603.16644v1
