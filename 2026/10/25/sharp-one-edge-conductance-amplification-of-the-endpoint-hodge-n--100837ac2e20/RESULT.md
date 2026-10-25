# Sharp one-edge conductance amplification of the endpoint Hodge norms on \(K_{r,r}\)

## Finding

Let \(r\ge29\) be an integer. Orient every edge of the complete bipartite graph \(K_{r,r}\) from its first class to its second, and distinguish an edge \(e_*\). Give \(e_*\) conductance \(t>0\), all other edges conductance \(1\). Write \(D\) for the oriented vertex-by-edge incidence matrix and \(W_t\) for the diagonal matrix of conductances. On the **unweighted-coordinate** real edge space \(\ell_1^{r^2}\), consider the Euclidean-orthogonal cut projector and its cycle complement
\[
 Q_r(t)=W_t^{1/2}D^{\mathsf T}(D W_tD^{\mathsf T})^+D W_t^{1/2},
 \qquad P_r(t)=I-Q_r(t).
\]
Here the superscript \(+\) denotes the Moore–Penrose pseudoinverse; conductance enters the projection through the square roots in this definition, while the endpoint norm is the ordinary, **not conductance-weighted**, coordinate \(\ell_1\) norm.

Put
\[
 k_r=\frac{(r-1)^2}{2r-1}, \qquad
 L_r=\frac{1+\sqrt{1+9k_r}}2.
\]
Then both sharp, globally conductance-optimized endpoint norms are equal:
\[
 \boxed{\sup_{t>0}\|Q_r(t)\|_{1\to1}
 =\sup_{t>0}\|P_r(t)\|_{1\to1}=L_r.}
\]
The cut supremum is attained **uniquely in the conductance** at
\[
 t_Q=\left(\frac{1+\sqrt{1+9k_r}}3\right)^2,
\]
whereas the cycle supremum is attained uniquely at
\[
 t_P=\left(\frac{\sqrt{1+9k_r}-1}3\right)^2.
\]
In each case the unique maximizing column is the distinguished edge \(e_*\). The two maximizing conductances are distinct and obey the exact duality \(t_Qt_P=k_r^2\).

In contrast, at uniform conductance the endpoint norms are bounded independently of \(r\):
\[
 \|Q_r(1)\|_{1\to1}=3-\frac4r+\frac2{r^2},
 \qquad
 \|P_r(1)\|_{1\to1}=4-\frac8r+\frac4{r^2}.
\]
Thus changing **only one conductance** can yield sharp unbounded amplification. Quantitatively,
\[
 L_r=\frac{3}{2\sqrt2}\sqrt r+\frac12+O(r^{-1/2}),
 \qquad
 \lim_{r\to\infty}\frac{L_r}{\sqrt r}=\frac3{2\sqrt2}.
\]
By symmetry, the same formulas hold for the induced \(\ell_\infty\) norms. The explicit sufficient threshold \(r\ge29\) is *not claimed optimal*.

## Assumptions and scope

All graphs are finite, simple, connected and bipartite with both vertex classes of cardinality \(r\). Every conductance is strictly positive; exactly one edge is allowed to vary. Edge-coordinate norms use the ordinary counting measure. The symbols \(\|Q\|_{1\to1}\) and \(\|P\|_{1\to1}\) refer to these specific orthogonal projections, **not** minima over all linear projections onto the same subspaces. Because the matrices are real symmetric, their \(\ell_1\) and \(\ell_\infty\) operator norms coincide and are maximum absolute column sums.

## Proof

**1. The unperturbed projection.** Label edges by ordered pairs \((i,j)\), \(1\le i,j\le r\), and take \(e_*=(1,1)\). Direct orthogonal projection of an \(r\)-by-\(r\) matrix onto the subspace of row-plus-column arrays gives
\[
 Q_r(1)_{(i,j),(a,b)}
 =\frac{\mathbf1_{i=a}}r+\frac{\mathbf1_{j=b}}r-\frac1{r^2}.
\]
This formula is also verified by symmetry, idempotence and the fact that its range consists of row-plus-column arrays (the cut space). Set \(Q_0=Q_r(1)\), \(h=(2r-1)/r^2\), and \(v_f=(Q_0)_{f,e_*}\). Then \((Q_0)_{e_*,e_*}=h\); for \(f\ne e_*\), precisely \(2(r-1)\) of the values \(v_f\) equal \((r-1)/r^2\) and precisely \((r-1)^2\) equal \(-1/r^2\). Therefore
\[
 S:=\sum_{f\ne e_*}|v_f|=\frac{3(r-1)^2}{r^2},
 \qquad 1-h=\frac{(r-1)^2}{r^2}.
\]

**2. Exact rank-one conductance update.** On the mean-zero vertex subspace, the Laplacian changes from \(DD^{\mathsf T}\) to \(DD^{\mathsf T}+(t-1)d_*d_*^{\mathsf T}\), where \(d_*\) is the incidence column of \(e_*\). Applying the ordinary rank-one inverse identity on this invertible subspace and restoring the two external factors \(W_t^{1/2}\) yields, with \(H=1+(t-1)h>0\),
\[
 (Q_r(t))_{fg}=(Q_0)_{fg}-\frac{(t-1)v_fv_g}{H}
 \quad(f,g\ne e_*),
\]
\[
 (Q_r(t))_{e_*f}=(Q_r(t))_{fe_*}=\frac{\sqrt t\,v_f}{H}
 \quad(f\ne e_*),
 \qquad (Q_r(t))_{e_*e_*}=\frac{th}{H}.
\]
These identities hold for all \(t>0\), including \(t<1\), because \(H=(1-h)+th>0\).

**3. The exceptional column.** Define \(k_r=(1-h)/h=(r-1)^2/(2r-1)\). Since \(H=h(t+k_r)\), the absolute column sums at \(e_*\) are exactly
\[
 c_Q(t)=\frac{t+3k_r\sqrt t}{t+k_r},
 \qquad c_P(t)=\frac{k_r+3k_r\sqrt t}{t+k_r}.
\]
Indeed the diagonal of \(P\) is \(1-th/H=(1-h)/H\), and its off-diagonal absolute entries equal those of \(Q\).

Set \(u=\sqrt{t/k_r}\). The expressions become
\[
 c_Q(t)=\frac{u^2+3\sqrt{k_r}u}{1+u^2},
 \qquad c_P(t)=\frac{1+3\sqrt{k_r}u}{1+u^2}.
\]
Each is a Rayleigh quotient of the symmetric two-by-two matrix
\[
 \begin{pmatrix}1&3\sqrt{k_r}/2\\3\sqrt{k_r}/2&0\end{pmatrix},
\]
using respectively the vectors \((u,1)\) and \((1,u)\). Its larger eigenvalue is \(L_r\), and its positive maximizing eigenvector is unique up to scale. Equivalently, differentiating the two rational functions in \(y=\sqrt t\) shows that their unique positive critical points are \((1+\sqrt{1+9k_r})/3\) and \((\sqrt{1+9k_r}-1)/3\), respectively. This proves their exact maxima \(L_r\), the formulas for \(t_Q,t_P\), and \(t_Qt_P=k_r^2\).

**4. No other column dominates for \(r\ge29\).** For every ordinary edge \(f\ne e_*\), the unperturbed absolute column sum equals
\[
 q_0=3-\frac4r+\frac2{r^2}<3,
 \qquad |v_f|\le\frac{r-1}{r^2}.
\]
For every \(r\ge3\) and every \(t>0\), the elementary bounds
\[
 \frac{|t-1|\,|v_f|}{H}
 \le\max\left\{\frac{r-1}{2r-1},\frac1{r-1}\right\}\le\frac12,
\]
\[
 \frac{\sqrt t\,|v_f|}{H}
 \le\frac1{2\sqrt{2r-1}}<\frac14
\]
follow respectively by separating \(t\le1\) from \(t\ge1\), and by maximizing \(y/((1-h)+hy^2)\) for positive \(y\). Applying the triangle inequality to the update in step 2, and summing over all rows except \(e_*\), yields
\[
 \|Q_r(t)\mathbf e_f\|_1
 \le q_0+\tfrac12 S+\frac1{2\sqrt{2r-1}}<5.
\]
Since \(P=I-Q\), the corresponding ordinary column of \(P_r(t)\) has norm less than \(6\). Finally \(k_r\) increases with \(r\), and \(k_{29}=784/57>40/3\), so \(L_r>6\) for all \(r\ge29\). The exceptional column can reach \(L_r\), whereas every other column is strictly below \(6<L_r\) for all positive conductances. Consequently both global supremum statements, their uniqueness assertions, and their maximizing column statements follow.

**5. Uniform-weight comparison and limit.** The uniform cut column has absolute sum \(h+S=q_0\); the uniform cycle column has absolute sum \(1-h+S=4-8/r+4/r^2\). Every column is equivalent by graph automorphisms. As \(r\to\infty\), \(k_r=r/2-3/4+O(r^{-1})\), giving the claimed asymptotic expansion of \(L_r\). No finite computation is needed for the all-parameter theorem.

## Verification

The standalone file `weighted_edge_checker.py` uses only the Python standard library. It independently constructs reduced weighted incidence matrices, exactly inverts their rational Laplacians, and compares each entry with the derived rank-one formula. Run `python3 weighted_edge_checker.py`. It verifies **38,124 matrix entries**, across five graph orders and six positive rational square-root conductances, plus exact exceptional column sums and the uniform-weight formulas. A separate numerical step evaluates the closed-form optimizers at 71 larger graph orders; this numerical step is corroborative only. The script prints `WEIGHTED_BIPARTITE_CERTIFICATE_OK` on success. The proof above, not finite testing, covers all \(r\ge29\) and all real \(t>0\).

## Relationship to prior work

Schild–Rao–Srivastava (2017) develop electrical-flow localization and a spectral-norm estimate for the **entrywise absolute** weighted transfer-impedance projector. Their Example 1.1 shows high \(\ell_1\) currents on an unweighted parallel-path construction, but does not assert this single-conductance sharp endpoint optimization for complete bipartite graphs. Dilworth–Kutzarova–Ostrovskii (2023) study cycle projections mainly on unweighted tori and Hamming graphs, often optimizing among invariant projections rather than changing conductances. Gurel-Gurevich–Nachmias–Sachdeva (2026) sharpen spectral localization estimates for weighted networks; their spectral norm of the entrywise absolute matrix is **not** its maximum absolute column sum. In contrast, this finding addresses the maximum column-sum norm, its sharp conductance optimization, and a dense graph family with a bounded uniform-weight baseline.

An earlier unweighted calculation on complete bipartite graphs determines the constant-conductance endpoint norms, and deleting an edge is a different limiting perturbation. Neither special case implies the conductance-optimized, order-\(\sqrt r\) endpoint amplification or the distinct optimal conductances. The rank-one update itself is classical linear algebra; originality is assessed only for its particular sharp projection-norm consequence, not for the update identity.

## Limitations

The theorem optimizes only the **canonical Euclidean-orthogonal** weighted cut and cycle projections, not all possible projections. The first graph size \(r\ge29\) is a sufficient bound derived from uniform control of ordinary columns, not a claim about the smallest size where the exact formula holds. It treats one varying edge on balanced complete bipartite graphs and ordinary edge-coordinate \(\ell_1/\ell_\infty\) norms. It does not automatically apply to multiple varying edges, arbitrary bipartite part sizes, nonsymmetric transfer-current matrices, or conductance-weighted endpoint norms. The non-exhaustiveness of bibliographic searches is a residual originality risk.

## References

1. A. Schild, S. Rao, N. Srivastava, *Localization of Electrical Flows*, arXiv:1708.01632, first posted 2017-08-04, especially Example 1.1 and Theorem 1.5.
2. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle Spaces: Invariant Projections and Applications to Transportation Cost*, arXiv:2305.12582, first posted 2023-05-21, especially Sections 1 and 2.
3. O. Gurel-Gurevich, A. Nachmias, S. Sachdeva, *A Tight Bound on Localization of Electrical Flows*, arXiv:2605.24130, first posted 2026-05-22, especially Theorem 1.3 (related spectral-norm estimate).
