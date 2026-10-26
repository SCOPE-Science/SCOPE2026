# A square-root price threshold for optimal spectral connectivity of star networks

## Finding
Let \(K_{1,m}\) be the star with \(m\ge2\) labeled leaves. Independently assign each spoke a nonnegative conductance \(w_i\), with strictly positive unit price \(c_i\), under \(\sum_{i=1}^m c_iw_i\le B\), where \(B>0\). Write \(L(w)\) for the usual combinatorial weighted Laplacian and \(\lambda_2(L(w))\) for its second-smallest eigenvalue. Define
\[
C=\sum_{i=1}^mc_i,\quad s_i=\sqrt{c_i},\quad s_{\max}=\max_i s_i,\quad
\delta=\max\{0,2s_{\max}-\textstyle\sum_i s_i\},\quad
T=C-\frac{\delta^2}{m+1}.
\]
Then \(T>0\), and the exact maximum and **unique** maximizing conductance vector are
\[
\lambda_*=\max_{w\ge0,\ \sum_i c_iw_i\le B}\lambda_2(L(w))=\frac BT.
\]
If \(\delta=0\), the optimizer is \(w_i^*=B/C\) for every spoke. If \(\delta>0\), there is a unique price-dominant index \(j\), satisfying \(s_j=\sum_{i\ne j}s_i+\delta\), and
\[
w_j^*=\frac BT\left(1-\frac{\delta}{(m+1)s_j}\right),\qquad
w_i^*=\frac BT\left(1+\frac{\delta}{(m+1)s_i}\right)\quad(i\ne j).
\]
Every displayed optimal conductance is strictly positive. At the sharp threshold \(s_{\max}=\sum_{i\ne j}s_i\), equal weights remain uniquely optimal. If \(m\ge3\), the optimal Fiedler eigenvalue has multiplicity \(m-1\) in the nondominant regime and multiplicity one in the dominant regime. For \(m=2\), its multiplicity is one throughout.

For \(m\ge3\), if one exceptional price is \(c_j=r\) and all other prices equal one, the optimal weights are equal if and only if \(r\le(m-1)^2\). For \(m=2\), this equality occurs only at \(r=1\). For fixed remaining prices and \(r\to\infty\), the ratio of the optimal gap to the gap under uniformly equal budget-feasible conductances tends to \((m+1)/m\).

## Assumptions and scope
The star has one hub and \(m\) distinct leaves; all costs are strictly positive real numbers, and conductances are nonnegative real numbers. The only constraint is total linear price-budget. The Laplacian uses ordinary unnormalized vertex counting measure: \(L_{00}=\sum_iw_i\), \(L_{0i}=L_{i0}=-w_i\), \(L_{ii}=w_i\), and all other entries zero. The eigenvalue \(\lambda_2\) is in the usual nondecreasing order including multiplicities. The optimization is over the entire labeled \(m\)-dimensional budget simplex; no equal-price, symmetry or fiber restriction is assumed.

## Proof
**1. Exact reduced eigenvalue constraint.** For a vertex potential \(x\) orthogonal to the all-ones vector, let \(y_i=x_i-x_0\) denote its leaf-to-hub differences and set \(\gamma=1/(m+1)\). From \(x_0=-\gamma\sum_i y_i\), one obtains
\[
x^{\mathsf T}L(w)x=\sum_i w_i y_i^2,\qquad
x^{\mathsf T}x=y^{\mathsf T}Hy,\qquad H=I_m-\gamma\mathbf1\mathbf1^{\mathsf T}.
\]
The positive-definite matrix \(H\) is fixed. Therefore \(\lambda_2(L(w))\ge\ell\) if and only if \(\operatorname{diag}(w)-\ell H\succeq0\). Since any optimal gap is positive and the objective is homogeneous, the original maximization is equivalent to minimizing \(\sum_i c_iv_i\) subject to \(\operatorname{diag}(v)\succeq H\). Its optimal value \(T_*\) satisfies \(\lambda_*=B/T_*\). Every feasible \(v\) automatically has \(v_i\ge H_{ii}>0\).

**2. Exact dual and polygon residual.** Strict primal feasibility (take all \(v_i\) large) gives strong semidefinite duality. The dual is
\[
\max_{Z\succeq0,\ Z_{ii}=c_i}\operatorname{tr}(HZ)
= C-\gamma\min_{Z\succeq0,\ Z_{ii}=c_i}\mathbf1^{\mathsf T}Z\mathbf1.
\]
Represent \(Z\) as the Gram matrix of vectors \(u_i\) with \(\|u_i\|=s_i\). The last quadratic form is \(\|\sum_i u_i\|^2\). The triangle inequality bounds this norm below by \(\delta\); equality is achieved by arranging the vectors head-to-tail in a plane if the lengths satisfy the polygon inequality, and otherwise by putting the uniquely longest vector opposite all remaining collinear vectors. The familiar polygon-closing fact also follows inductively because attainable lengths of the resultant of fixed-length planar vectors form an interval. Consequently \(T_*=C-\gamma\delta^2=T\). In particular \(T\ge C-C/(m+1)>0\).

**3. Attainment in the nondominant regime.** For \(\delta=0\), set \(v_i=1\). The semidefinite slack is \(\operatorname{diag}(v)-H=\gamma\mathbf1\mathbf1^{\mathsf T}\succeq0\), and its cost is \(C=T\). For uniqueness, choose any optimal dual Gram matrix \(Z\) with diagonal \(c_i>0\) and \(Z\mathbf1=0\). Every optimal primal slack \(D\succeq0\) satisfies \(\operatorname{tr}(DZ)=0\) by complementary slackness, hence \(DZ=0\). As \(DZ=\operatorname{diag}(v-1)Z\), taking the \(i\)-th diagonal entry yields \((v_i-1)c_i=0\). Therefore each \(v_i=1\).

**4. Attainment and uniqueness in the dominant regime.** Suppose \(\delta>0\), with dominant index \(j\). Let \(a_j=s_j\) and \(a_i=-s_i\) for \(i\ne j\), so \(\sum_i a_i=\delta\) and \(Z=aa^{\mathsf T}\) is dual-optimal. Complementary slackness for any optimum gives \((\operatorname{diag}(v)-H)a=0\), namely
\[
(v_i-1)a_i+\gamma\delta=0\quad\text{for every }i.
\]
Thus the only possible optimizer is \(v_j=1-\gamma\delta/s_j\) and \(v_i=1+\gamma\delta/s_i\) for \(i\ne j\). Its slack is positive semidefinite: the \(i\ne j\) diagonal excesses are positive, and the Schur complement of their principal block vanishes, because
\[
\frac{\gamma}{1+\gamma\sum_{i\ne j}(v_i-1)^{-1}}
=\frac{\gamma}{1+(\sum_{i\ne j}s_i)/\delta}
=\frac{\gamma\delta}{s_j}=1-v_j.
\]
The corresponding total cost is \(C-\gamma\delta(\sum_i a_i)=C-\gamma\delta^2=T\). This proves attainment and uniqueness. The slack kernel is one-dimensional in this regime; in the nondominant regime it has dimension \(m-1\). By the generalized eigenvalue characterization in step 1 these are exactly the Fiedler eigenvalue multiplicities.

**5. Budget and asymptotic boundaries.** Rescaling \(v\) by \(B/T\) gives the unique original optimizer. Each component is positive because \(0<\delta<s_j\) in the dominant case and \(0<\gamma<1\). If \(m\ge3\), \(c_j=r\), and the other prices equal one, the condition \(\delta=0\) becomes \(\sqrt r\le m-1\). If \(m=2\), the two square-root prices must be equal, so \(r=1\). Finally, as \(r\to\infty\), \(T\sim mr/(m+1)\), while the uniform-weight gap is \(B/C\sim B/r\), yielding the stated limiting ratio.

## Verification
The accompanying `verify_star.py` independently reconstructs the exact normalized semidefinite slack and tests all principal minors with rational arithmetic over 3,601 integer-square price vectors. It verifies the conductance budget and compares the predicted gap with a separately assembled Laplacian eigensolver. Further deterministic tests cover 770 real-price configurations, 11,550 asymmetric budget allocations, and both sides of the threshold. See `verification_output.txt` and `VERIFICATION.md` for the exact replay statement. These finite checks corroborate; the preceding dual proof is what establishes the universally quantified theorem.

## Relationship to prior work
Fiedler's absolute-algebraic-connectivity problem and the general semidefinite/embedding duality are classical. In particular, Göring, Helmberg and Wappler (2005), Section 2, optimize the Laplacian spectral gap under the **uniform sum-of-conductances budget**, and present an optimal graph embedding and general results for trees. Boyd (2006) develops related graph-eigenvalue optimization. Shakeri and collaborators (2015) study maximizing connectivity in two-layer interconnection networks. The novel assertion assessed here is the explicit, complete, **heterogeneous edge-price** solution on a fixed star, including its square-root polygon criterion, unique individual conductances, and eigenvalue-multiplicity switch. The prior general SDP methods support the derivation but do not state the price-dependent star classification in the inspected material.

## Limitations
This theorem concerns combinatorial, not normalized or mass-weighted, Laplacians, positive linear prices, and fixed star topology. It does not assert analogous formulas for paths, arbitrary trees, edge-selection problems, or nonlinear budgets. The conclusion is a same mathematical model proof and literature assessment rather than independently validated mathematical research. Possible historical coverage by specialized work on priced fastest-consensus stars or implicit corollaries of broad embedding theory remains a residual originality risk; literature searches cannot prove novelty.

## References
1. F. Göring, C. Helmberg and M. Wappler, *Embedded in the Shadow of the Separator*, Preprint 2005-12 (posted 2005-09-02), Optimization Online, https://optimization-online.org/2005/09/1202/ .
2. S. Boyd, *Convex Optimization of Graph Laplacian Eigenvalues*, Proceedings of the International Congress of Mathematicians, 2006, https://www-leland.stanford.edu/~boyd/papers/pdf/cvx_opt_graph_lapl_eigs.pdf .
3. H. Shakeri and collaborators, *Maximizing Algebraic Connectivity in Interconnected Networks*, arXiv:1510.06785v1 (2015-10-22), https://arxiv.org/abs/1510.06785 .
