# A sharp row-coherence obstruction in PDNQP diagonal step initialization

## Summary

PDNQP (Chen--Lu, 2026) proposes diagonal primal and dual masses for its inner primal--dual iteration. Its dual mass has the form
\[
 m_{y,j}=\sum_i \frac{B_{ji}^2}{m_{w,i}},
\]
where \(B\) is the residual-form constraint matrix and \(m_w\) is the primal mass. This normalization gives every row of
\[
K=M_y^{-1/2}BM_w^{-1/2}
\]
unit Euclidean norm, but it does not control the operator norm of \(K\). The missing quantity is the coherence among the normalized constraint rows.

The observation is sharp. If \(m\) constraint rows have positive mass, then
\[
1\le \|K\|_2\le \sqrt m,
\]
and the upper bound can be approached by full-row-rank residual-form instances that are already equilibrated in the infinity-norm sense used by standard Ruiz scaling. For the source step sizes, the free balancing parameter cancels from the normalized coupling, so the factor \(0.99\) multiplies \(\|K\|_2\) but does not remove this possible \(\sqrt m\) amplification.

A concrete family also gives an explicit direction that violates the source acceptance inequality. Thus the adaptive acceptance/reduction mechanism is not merely guarding against poor outer scaling or redundant constraint rows: coherent but linearly independent rows can make the initial diagonal steps too large.

## 1. Source setup

For the inner residual-form convex quadratic problem, write
\[
M_w=\operatorname{diag}(m_w),\qquad M_y=\operatorname{diag}(m_y),
\]
and suppose all considered dual masses are positive. The PDNQP diagonal initialization defines
\[
m_{y,j}=\sum_i\frac{B_{ji}^2}{m_{w,i}}.
\]
The corresponding initial primal and dual step matrices are
\[
T=c\,\omega^{-1}M_w^{-1},\qquad
S=c\,\omega M_y^{-1},\qquad c=0.99,
\]
with a positive balancing parameter \(\omega\).

The source accepts a trial step only if its metric energy dominates a componentwise-absolute quadratic/coupling expression. In particular, for increments \((\Delta w,\Delta y)\), its right-hand side contains
\[
\sum_i\left|\Delta w_i(B^T\Delta y)_i\right|.
\]

## 2. Row normalization theorem

Define
\[
K=M_y^{-1/2}BM_w^{-1/2}.
\]
For every row \(j\),
\[
\|K_{j:}\|_2^2
=\frac{1}{m_{y,j}}\sum_i\frac{B_{ji}^2}{m_{w,i}}
=1.
\]
Consequently,
\[
\|K\|_F^2=m.
\]
Since \(\operatorname{rank}(K)\le m\),
\[
\boxed{1\le \|K\|_2\le\sqrt m.}
\]
The lower bound follows from \(\|K\|_F^2\le m\|K\|_2^2\); the upper bound follows from \(\|K\|_2\le\|K\|_F\).

For the source steps,
\[
S^{1/2}BT^{1/2}
=c\,M_y^{-1/2}BM_w^{-1/2}
=cK.
\]
Hence
\[
\boxed{\|S^{1/2}BT^{1/2}\|_2=c\|K\|_2,}
\]
so \(\omega\) cancels exactly. Balancing primal against dual steps cannot repair coherent normalized rows.

## 3. A full-row-rank sharp family

Fix integers \(m\ge2\) and \(p\ge1\). Consider the equality-constraint matrix
\[
A_{m,p}=\begin{bmatrix}\mathbf 1_{m\times p}&I_m\end{bmatrix}
\]
and its residual-form matrix
\[
B_{m,p}=\begin{bmatrix}\mathbf 1_{m\times p}&I_m&-I_m\end{bmatrix}.
\]
The original constraint matrix \(A_{m,p}\) has full row rank because of the \(I_m\) block. All nonzero entries have magnitude one. Therefore row and column infinity norms are already one; standard infinity-norm Ruiz equilibration leaves this matrix unchanged.

Choose the admissible scaled Hessian and residual penalty
\[
H=I_{p+2m},\qquad \sigma_j=1.
\]
The PDNQP primal masses become
\[
m_{w,i}=\begin{cases}
m+1,&i\text{ in a shared column},\\
2,&i\text{ in a private }I_m\text{ column},\\
2,&i\text{ in a residual }-I_m\text{ column}.
\end{cases}
\]
Every dual row has the same mass
\[
m_y=\frac{p}{m+1}+1.
\]
Set
\[
a=\frac{p}{m+1}.
\]
A direct block multiplication gives
\[
KK^T=\frac{a}{a+1}\mathbf1\mathbf1^T+\frac1{a+1}I_m.
\]
Therefore
\[
\boxed{
\|K\|_2^2=\frac{ma+1}{a+1}
}
\]
and the remaining \(m-1\) squared singular values are \(1/(a+1)\). At fixed \(m\),
\[
\boxed{\|K\|_2\longrightarrow\sqrt m\qquad(p\to\infty).}
\]
Thus the general \(\sqrt m\) bound is sharp even with nonredundant original constraints and after infinity-norm equilibration.

## 4. Exact failure direction for the PDNQP acceptance test

Let \(u,v\) be unit left and right singular vectors corresponding to \(\|K\|_2\), with the top left singular vector chosen as the positive constant vector. Define
\[
\Delta w=T^{1/2}v,\qquad
\Delta y=S^{1/2}u.
\]
Then the metric part of the source acceptance left-hand side is exactly
\[
\frac12\|v\|_2^2+\frac12\|u\|_2^2=1.
\]

For the family above, the signs of \(v\) agree blockwise with those of \(B^Tu\): positive on the shared and private primal columns and negative on the residual columns. Hence there is no cancellation inside the componentwise absolute values, and
\[
\sum_i\left|\Delta w_i(B^T\Delta y)_i\right|
=u^TS^{1/2}BT^{1/2}v
=c\|K\|_2.
\]
The Hessian term appearing on the source right-hand side is nonnegative. Consequently,
\[
\boxed{c\|K\|_2>1\quad\Longrightarrow\quad
\text{the source acceptance inequality fails for these increments}.}
\]
Already at \((m,p)=(2,1)\),
\[
\|K\|_2=\sqrt{5/4},\qquad
0.99\|K\|_2\approx1.10685>1.
\]
The obstruction therefore does not require a large matrix.

If both primal and dual trial steps are additionally multiplied by a common scalar \(s\), the normalized coupling becomes \(sc\|K\|_2\). Uniform control of this worst singular direction requires
\[
s\le \frac1{c\|K\|_2},
\]
which approaches \(1/(0.99\sqrt m)\) on the sharp family.

## 5. A coupling-safe comparison scale

This section is a comparison with standard diagonal primal--dual scaling, not a new general convergence theorem.

The source primal mass obeys
\[
m_{w,i}\ge \sum_j|B_{ji}|
\]
for the relevant blocks. Define instead the row-\(\ell_1\) dual mass
\[
f_j=\sum_i|B_{ji}|,
\qquad F=\operatorname{diag}(f).
\]
Then
\[
\boxed{\|F^{-1/2}BM_w^{-1/2}\|_2\le1.}
\]
Indeed, for arbitrary vectors \(x,y\), weighted AM--GM gives
\[
\begin{aligned}
\left|y^TF^{-1/2}BM_w^{-1/2}x\right|
&\le \sum_{j,i}|B_{ji}|\frac{|y_j|}{\sqrt{f_j}}\frac{|x_i|}{\sqrt{m_{w,i}}}\\
&\le\frac12\sum_{j,i}|B_{ji}|\left(\frac{y_j^2}{f_j}+\frac{x_i^2}{m_{w,i}}\right)\\
&\le\frac12(\|y\|_2^2+\|x\|_2^2),
\end{aligned}
\]
which yields the claimed operator bound by homogeneity. This is the familiar Schur-type mechanism behind coupling-safe diagonal primal--dual preconditioners.

On the sharp family, retaining the PDNQP primal mass but replacing the dual row-\(\ell_2\) mass by this row-\(\ell_1\) mass gives a coupling norm below one; it tends to \(\sqrt{m/(m+1)}\) as the number of shared columns grows.

This comparison controls the \(B\)-coupling only. It is not claimed to replace the full PDNQP acceptance test, which also contains the Hessian contribution and other algorithmic considerations.

## 6. Interpretation

The dual formula \(m_y=\operatorname{diag}(BM_w^{-1}B^T)\) removes rowwise scale but discards the off-diagonal entries of the same Gram matrix. Those off-diagonal entries are precisely normalized row correlations. The sharp family makes them almost one, so the Gram matrix approaches \(\mathbf1\mathbf1^T\), producing the \(\sqrt m\) singular-value amplification.

This gives a structural explanation for why an adaptive acceptance/reduction safeguard can remain important after equilibration: row norm normalization and global coupling control are different tasks. It is also consistent with the source's empirical observation that instances with strongly coupled constraints can be less favorable.

## 7. Limitations and scope

- The construction is a worst-case structured family; it does not assert that typical benchmark instances attain the \(\sqrt m\) regime.
- The result concerns the initial diagonal scaling and an explicit rejected trial direction. It does not show that PDNQP diverges or fails after its adaptive step reduction.
- No iteration-complexity or end-to-end computational-cost lower bound is claimed.
- The row-\(\ell_1\) comparison is only a coupling bound, not a drop-in proof of the full source acceptance condition.
- Standard operator-norm conditions for primal--dual hybrid gradient methods, Schur tests, Ruiz equilibration, and classical diagonal preconditioning are prior knowledge. The contribution here is the source-specific row-coherence classification, sharp residual-form family, and explicit acceptance-failure certificate for the 2026 PDNQP initialization.

## 8. Reproducibility

`artifacts/verify_row_coherence.py` constructs finite members of the family, checks unit normalized row norms, compares the numerical singular value with the closed form, evaluates the source acceptance inequality on the top singular direction, and evaluates the row-\(\ell_1\) comparison scale. `artifacts/verification_output.txt` contains the resulting values. The verification was executed successfully.

## References

1. Z. Chen and H. Lu, *PDNQP: A GPU-based Factorization-free Method for Large-scale Nonconvex Quadratic Programming*, arXiv:2609.19557 (2026). https://arxiv.org/abs/2609.19557
2. T. Pock and A. Chambolle, *Diagonal Preconditioning for First Order Primal-Dual Algorithms in Convex Optimization*, ICCV 2011. https://doi.org/10.1109/ICCV.2011.6126441
3. D. Ruiz, *A Scaling Algorithm to Equilibrate Both Rows and Columns Norms in Matrices*, RAL-TR-2001-034 (2001). http://purl.org/net/epubs/work/29557
4. D. Applegate et al., *Practical Large-Scale Linear Programming using Primal-Dual Hybrid Gradient*, arXiv:2106.04756 (2021). https://arxiv.org/abs/2106.04756
