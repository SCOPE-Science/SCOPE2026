# Exact endpoint-enhanced D-optimal rung allocation on finite ladders

## Finding

Let \(n\ge 2\) be an integer and \(B>0\). Consider the two-rail ladder \(P_n\square K_2\). Every rail edge has fixed conductance \(1\); its \(n\) rungs have independently adjustable nonnegative conductances \(w_1,\ldots,w_n\), constrained by \(\sum_{i=1}^n w_i\le B\). The objective is the **weighted spanning-tree sum**
\[
\tau_n(w)=\sum_{T\text{ spanning tree}}\prod_{e\in T}c_e,
\]
where \(c_e=1\) on rail edges and \(c_e=w_i\) on rung \(i\). Equivalently, this is the determinant-based (D-optimal) connectivity objective, not the largest individual spanning-tree weight.

Define
\[
u=\frac{B-1+\sqrt{(B-1)^2+2nB}}n>0.
\]
The **unique global maximizer** among all independent nonnegative rung allocations is
\[
\boxed{w_1^*=w_n^*=\frac u2,\qquad
 w_i^*=\frac{u^2}{2(1+u)}\quad(2\le i\le n-1).}
\]
The interior range is empty for \(n=2\). The exact optimal value is
\[
\boxed{\max_{w_i\ge0,\ \sum w_i\le B}\tau_n(w)
=\frac{u(u+2)(1+u)^{n-2}}2.}
\]
Every optimum rung has positive conductance, despite allowing zero weights. For \(n\ge3\), each endpoint receives strictly more conductance than any interior rung:
\[
w_1^*-w_i^*=\frac{u}{2(1+u)}>0.
\]
For fixed \(n\ge3\) and \(B\downarrow0\), the endpoint conductances are \(B/2+O_n(B^2)\) and each interior conductance is \(B^2/2+O_n(B^3)\). For fixed \(B>0\) and \(n\to\infty\),
\[
w_1^*\sim\sqrt{\frac B{2n}},\qquad
w_i^*\sim\frac Bn\ (2\le i\le n-1),\qquad
\max\tau_n\sim\sqrt{\frac{2B}{n}}\,e^{\sqrt{2Bn}-1}.
\]
Thus the boundary premium per rung grows as a square root relative to an interior rung in long ladders at fixed budget.

## Assumptions and scope

The graph has two disjoint length-\((n-1)\) rails and a rung joining the corresponding vertices at each of the \(n\) columns. All rail conductances are fixed to \(1\), the rung conductances can vary independently, and their common unit price is \(1\). The budget is positive and finite. The weights enter the spanning-tree polynomial multiplicatively. No stationarity or stochastic-transition row-sum normalization is imposed.

## Proof

**1. An exact determinant reduction.** Let \(L_P\) be the combinatorial Laplacian of the unit-edge path \(P_n\), and \(D=\operatorname{diag}(w_1,\ldots,w_n)\). The weighted ladder Laplacian is
\[
\mathcal L=\begin{pmatrix}L_P+D&-D\\-D&L_P+D\end{pmatrix}.
\]
The orthogonal rail-symmetric/antisymmetric change of basis splits it into \(L_P\) and \(A(w)=L_P+2D\). For \(\sum_i w_i>0\), \(A(w)\) is positive definite: its quadratic form is \(\sum_{i=1}^{n-1}(x_i-x_{i+1})^2+2\sum_iw_ix_i^2\), whose kernel is trivial. The nonzero eigenvalues of \(L_P\) have product \(n\). Kirchhoff's weighted matrix-tree theorem on the \(2n\)-vertex ladder therefore yields
\[
\tag{1}\tau_n(w)=\frac12\det A(w).
\]
If all rungs vanish, the ladder is disconnected and \(\tau_n=0\).

**2. Constructing the candidate.** The defining \(u\) is the unique positive solution of
\[
\tag{2}n u^2+2(1-B)u-2B=0.
\]
Indeed, the left side is negative at zero and is a quadratic with positive leading coefficient and negative product of its two roots. For the proposed allocation, its budget is exactly
\[
2\frac u2+(n-2)\frac{u^2}{2(1+u)}
=\frac{nu^2+2u}{2(1+u)}=B.
\]
All its coordinates are strictly positive. Put \(\rho=(1+u)^{-1}\in(0,1)\). The candidate's reduced matrix \(A_*\) is tridiagonal, has off-diagonal entries \(-1\), and has diagonal entries
\[
(A_*)_{ii}=\begin{cases}
\rho^{-1},&i=1\text{ or }i=n,\\
\rho+\rho^{-1},&2\le i\le n-1.
\end{cases}
\]
An entrywise multiplication (including both boundary rows) shows that
\[
\tag{3}(A_*^{-1})_{ij}
=\frac{\rho^{|i-j|+1}}{1-\rho^2},\qquad 1\le i,j\le n.
\]
This is the covariance of a finite stationary first-order autoregressive chain, up to its scalar variance. Crucially, its diagonal is constant: \((A_*^{-1})_{ii}=\rho/(1-\rho^2)\), independent of \(i\).

**3. Global optimality and uniqueness without a symmetry assumption.** On the positive-definite domain, \(\log\det A(w)\) is differentiable with
\[
\frac{\partial}{\partial w_i}\log\det A(w)=2(A(w)^{-1})_{ii}.
\]
At \(w^*\), these derivatives all equal \(2\rho/(1-\rho^2)\). Consequently, for any other feasible \(z_i\ge0\), concavity gives
\[
\log\det A(z)-\log\det A(w^*)
\le\frac{2\rho}{1-\rho^2}\Bigl(\sum_i z_i-B\Bigr)\le0.
\]
The feasible \(A(z)\) is positive definite whenever \(\sum_i z_i>0\); the disconnected zero allocation is not optimal. Strict concavity follows because for any nonzero real vector \(v\),
\[
\frac{d^2}{dt^2}\log\det\bigl(A(w)+2t\operatorname{diag}v\bigr)\Big|_{t=0}
=-4\operatorname{tr}\bigl(A(w)^{-1}\operatorname{diag}v\,A(w)^{-1}\operatorname{diag}v\bigr)<0.
\]
The trace is strictly positive since it is the squared Frobenius norm of \(A(w)^{-1/2}\operatorname{diag}v\,A(w)^{-1/2}\). This establishes a unique global optimum over **all** rung vectors, including asymmetric and boundary allocations.

**4. Evaluating the optimum.** The matrix \(R=(\rho^{|i-j|})_{i,j=1}^n\) has determinant \((1-\rho^2)^{n-1}\), as seen by subtracting \(\rho\) times the preceding row from each row in descending order. From (3),
\[
\det A_*^{-1}
=\Bigl(\frac\rho{1-\rho^2}\Bigr)^n(1-\rho^2)^{n-1}
=\frac{\rho^n}{1-\rho^2}.
\]
Combining this with (1) proves the claimed optimal value:
\[
\tau_n(w^*)=\frac{1-\rho^2}{2\rho^n}
=\frac{u(u+2)(1+u)^{n-2}}2.
\]

**5. Boundary regimes.** Equation (2) gives \(u=B+O_n(B^2)\) for fixed \(n\) at small budget, which proves the endpoint/interior expansions. For fixed positive \(B\) and growing \(n\), its explicit root yields \(u=\sqrt{2B/n}+(B-1)/n+O_B(n^{-3/2})\). Substitution in the weight formulas gives the stated conductance scales. Further,
\[
(n-2)\log(1+u)=\sqrt{2Bn}-1+o(1),\qquad
\frac{u(u+2)}2\sim\sqrt{2B/n},
\]
which yields the asymptotic optimal tree weight.

## Verification

The attached standalone `verify.py` uses only Python's standard library. It performs 793 exact-rational tests of the budget identity, the autoregressive inverse (3), constant inverse diagonals, the determinant value, independent full-ladder Laplacian cofactors for small sizes, and domination of reproducible alternative feasible allocations. Run with `python3 verify.py`.

These are finite checks. The all-\(n\), all-\(B>0\), strict-uniqueness, and asymptotic assertions are proved analytically above and are not inferred from finite experiments.

## Relationship to prior work

Khosoussi, Sukhatme, Huang and Dissanayake (2016) explain why the weighted spanning-tree objective measures connectivity and develops approximate edge-selection methods with a convex log-determinant relaxation; see their Sections 1 and 4.4. That general formulation does not supply the exact optimum for independently adjustable rungs on a fixed-rail finite ladder. Boyd (2006) reviews convex Laplacian-weight optimization, while Gantert and Klenke (2023) analyze spanning-tree measures on ladders with **uniform** rung weight. A published finite-volume rung-kernel theorem also studies **fixed uniform** rung weights and boundary-versus-bulk inclusion effects, using the exact inverse of a fixed tridiagonal precision matrix. These provide methodology and structural motivation but not, in the material available, the all-budget variable-rung allocation and optimum established here.

A related problem with independently adjustable edges on a **cyclic** two-rail prism differs: it has periodic rails and a separate rail-edge investment budget, so its symmetry and admissible set do not imply this free-boundary fixed-rail result. The full finite-volume rung-kernel statement and proof were inspected: they assume a common rung conductance \(c>0\) and explicitly identify nonuniform rung weights as outside that theorem’s scope. They therefore do not imply a unique price-budget allocation for independent nonuniform weights. General D-optimal design literature could still contain an equivalent optimization statement.

## Limitations

The theorem does not optimize the rail-edge conductances, account for different rung prices, impose upper bounds on individual weights, or address more than two rails. The tree sum is a determinant-based connectivity surrogate; the statement does not by itself optimize reliability under arbitrary edge-failure probabilities, mixing time, or effective resistance. Priority has been assessed against the sources inspected, not independently certified by an external referee. Numerical verification does not replace the mathematical proof.

## References

1. Khosoussi, K., Sukhatme, G. S., Huang, S., and Dissanayake, G., *Maximizing the Weighted Number of Spanning Trees: Near-\(t\)-Optimal Graphs*, arXiv:1604.01116 (first public version 2016-04-05), https://arxiv.org/abs/1604.01116.
2. Boyd, S., *Convex Optimization of Graph Laplacian Eigenvalues*, Proceedings of the International Congress of Mathematicians (2006), https://www-leland.stanford.edu/~boyd/papers/cvx_opt_graph_lapl_eigs.html.
3. Gantert, N., and Klenke, A., *Biased Random Walk on Spanning Trees of the Ladder Graph*, Journal of Statistical Physics 190, 83 (2023), https://doi.org/10.1007/s10955-023-03091-w.
4. *Exact finite-volume rung kernel and boundary-bulk split for weighted ladder spanning trees*, public research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-finite-volume-rung-kernel-and-boundary-bulk-split-for-weig--647fc3f7ee8c (full `RESULT.md` inspected).
5. A. Klenke, *The Random Spanning Tree on Ladder-like Graphs* (2017), arXiv:1704.00182, https://arxiv.org/abs/1704.00182.
