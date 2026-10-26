# Exact D-optimal conductances on heterogeneously priced unicyclic graphs

## Finding

Let \(G\) be any connected simple unicyclic graph on \(N\ge3\) vertices. Each edge \(e\) has an independently chosen nonnegative conductance \(w_e\), a positive price \(c_e\), and a common budget \(B>0\). The unique allocation maximizing the determinant of any grounded weighted Laplacian, subject to \(\sum_e c_e w_e\le B\), has the complete explicit characterization below.

Write \(C\) for the unique cycle, of length \(k\ge3\), and \(F\) for the set of \(N-k\) bridges. Put \(a=B/(N-1)\). Every bridge receives
\[
w_e^*=a/c_e\qquad(e\in F).
\]
Thus each bridge spends exactly \(a\), regardless of cycle prices or the shapes of the attached trees.

If a cycle edge \(j\) has price \(c_j\ge\sum_{i\in C\setminus\{j\}}c_i\), it is uniquely determined, and the unique optimum **deletes precisely that edge**:
\[
w_j^*=0,\qquad w_i^*=a/c_i\quad (i\in C\setminus\{j\}).
\]
Conversely, no cycle edge is deleted unless this inequality holds. The boundary equality is included in the deletion regime.

If no such dominant price exists, **all edges receive positive conductance**. Define \(t_{\max}=1/(4c_{\max})\), and, for \(0\le t\le t_{\max}\),
\[
m_i(t)=\frac{1-\sqrt{1-4tc_i}}2.
\]
Choose an index \(j\) of maximum cycle price. If \(\sum_{i\in C}m_i(t_{\max})\ge1\), there is exactly one \(t\in(0,t_{\max}]\) with \(\sum_{i\in C}m_i(t)=1\), and set \(x_i=m_i(t)\) for all cycle edges. Otherwise, \(j\) is the unique maximum-price edge, and exactly one \(t\in(0,t_{\max})\) satisfies
\[
\sum_{i\in C\setminus\{j\}}m_i(t)=m_j(t).
\]
Set \(x_j=1-m_j(t)\) and \(x_i=m_i(t)\) otherwise. In either case the unique optimum is
\[
w_i^*=\frac{a(1-x_i)}{c_i}\qquad(i\in C).
\]
These formulas require only a monotone scalar root solve. The cycle budget is always \((k-1)B/(N-1)\), independent of how many trees are attached.

In particular, if one cycle edge costs \(r>0\) per unit and the other \(k-1\) cycle edges cost one, write \(B_C=(k-1)B/(N-1)\). For \(0<r<k-1\), all cheap edges have conductance
\[
y=\frac{B_C(k-2)}{(k-1)^2-r},
\]
and the exceptional edge has conductance
\[
z=\frac{B_C(k-1-r)}{r((k-1)^2-r)}.
\]
For \(r\ge k-1\), the exceptional edge instead has zero conductance and every cheap cycle edge has conductance \(B/(N-1)\). The **exact edge-deletion threshold \(r=k-1\)** does not depend on the trees attached to the cycle.

## Assumptions and scope

The graph is finite, undirected, connected, simple, and has exactly one graph-theoretic cycle. All edge prices are strictly positive, conductances may vanish, and the budget is strictly positive. The reduced Laplacian \(L^{(v)}(w)\) is obtained by deleting the same row and column corresponding to any vertex \(v\) of the conductance-weighted combinatorial Laplacian. Maximize \(\tau(w)=\det L^{(v)}(w)\), equivalently the weighted spanning-tree enumerator, not the ordinary minimum-cost spanning-tree objective. The nonzero weighted-Laplacian eigenvalue product equals \(N\tau(w)\); therefore this is also the Laplacian D-optimal design objective. The theorem does not concern other optimality criteria such as minimizing effective resistance or maximizing algebraic connectivity.

## Proof

**1. Tree polynomial and existence.** Every spanning tree contains all bridges and all but one cycle edge. By the weighted matrix-tree theorem,
\[
\tau(w)=\prod_{e\in F}w_e\sum_{j\in C}\prod_{i\in C\setminus\{j\}}w_i.
\]
All costs are positive, so the budget polytope is compact. There are feasible allocations with positive determinant, so an optimum has a connected positive-weight support. All bridges are therefore positive and at most one cycle edge can be zero. Strictly increasing the weight of a positive edge increases \(\tau\), so the budget is fully spent.

**2. Strict concavity and uniqueness.** The reduced Laplacian is a positive-definite linear matrix pencil in conductances on every connected support. The function \(\log\det\) is strictly concave on positive-definite matrices. Moreover, the map from the edge-conductance vector to the reduced Laplacian is injective for simple graphs: knowing all entries of the reduced matrix gives the omitted row and column by zero row sums, and each off-diagonal full-Laplacian entry determines its unique edge weight. Hence \(\log\tau\) is strictly concave on the convex feasible set where \(\tau>0\). Any feasible KKT solution is globally optimal and unique.

**3. The common dual multiplier.** The tree polynomial is homogeneous of degree \(N-1\). The KKT equations for maximizing \(\log\tau\) have \(\partial\log\tau/\partial w_e=\lambda c_e\) for every positive edge and a \(\le\lambda c_e\) inequality for a zero edge. Euler's homogeneous identity multiplied by conductances gives \(N-1=\lambda\sum c_e w_e=\lambda B\), so \(\lambda=(N-1)/B=1/a\). Every bridge has derivative \(1/w_e\), yielding \(w_e=a/c_e\).

**4. Exact deletion criterion.** Suppose a single cycle edge \(j\) has zero conductance. The remaining cycle edges are bridges in the supported tree and must satisfy \(w_i=a/c_i\). Differentiating the polynomial in step 1 at the deleted edge gives
\[
\frac{\partial\log\tau}{\partial w_j}=\sum_{i\in C\setminus\{j\}}\frac1{w_i}=\frac1a\sum_{i\ne j}c_i.
\]
The KKT inequality is therefore exactly \(c_j\ge\sum_{i\ne j}c_i\). Conversely, when this inequality holds, the displayed tree allocation satisfies all KKT equations and inequalities. Strict concavity proves global optimality and uniqueness, including at equality. Since there are at least two other cycle edges of positive price, at most one cycle edge satisfies it.

**5. Positive-cycle equations.** With every cycle conductance positive, put \(r_i=1/w_i\), \(S=\sum_{i\in C}r_i\), and \(x_i=r_i/S\). Then \(x_i>0\) and \(\sum x_i=1\). Factoring the cycle polynomial as \(\prod_i w_i\sum_i r_i\) yields
\[
\frac{\partial\log\tau}{\partial w_i}=r_i(1-x_i).
\]
KKT thus gives \(w_i=a(1-x_i)/c_i\), whence
\[
x_i(1-x_i)=t c_i,\qquad t=1/(aS)>0.
\]
At most one \(x_i\) exceeds \(1/2\), and if it does then \(c_i\) is strictly the greatest cycle price: on \((0,1/2]\), the function \(x(1-x)\) is strictly increasing and the complementary root has the same price. The formula for the smaller root is \(m_i(t)\).

**6. Scalar-root existence and uniqueness.** The functions \(m_i(t)\) are continuous and strictly increasing from zero on \([0,t_{\max}]\). When their sum at the endpoint is at least one, it has a unique root equal to one and yields feasible positive \(x_i\). Otherwise there must be one larger root; its index is the unique maximum-price edge \(j\). No dominant-price deletion condition means \(c_j<\sum_{i\ne j}c_i\), so
\[
\lim_{t\downarrow0}\frac{\sum_{i\ne j}m_i(t)}{m_j(t)}=\frac{\sum_{i\ne j}c_i}{c_j}>1.
\]
At \(t=t_{\max}\), the ratio is below one because \(m_j(t_{\max})=1/2\) and \(\sum_i m_i(t_{\max})<1\). For each \(c_i<c_j\), the ratio
\[
\frac{m_i(t)}{m_j(t)}=\frac{c_i}{c_j}\frac{1+\sqrt{1-4tc_j}}{1+\sqrt{1-4tc_i}}
\]
is strictly decreasing in \(t\), as follows by logarithmic differentiation. Their sum therefore crosses one exactly once. Setting \(x_j=1-m_j(t)\) completes the solution. For either branch, using \(c_i/(1-x_i)=x_i/t\) proves that \(x_i=r_i/\sum r_\ell\) as required. Consequently the resulting positive weights satisfy all KKT equations, are feasible, and are uniquely optimal by step 2. Summing \(c_iw_i=a(1-x_i)\) gives the stated cycle budget.

**7. One exceptional price.** If costs are \((r,1,\ldots,1)\), uniqueness forces the last \(k-1\) conductances to equal \(y\); call the first \(z\). The cycle polynomial is \(y^{k-1}+(k-1)zy^{k-2}\). Differentiating its logarithm under \(rz+(k-1)y=B_C\) gives the displayed rational formulas for \(0<r<k-1\). The general deletion criterion completes the \(r\ge k-1\) case. These formulas agree at the boundary.

## Verification

Run \(\texttt{python3 verify.py}\) from the directory containing the accompanying standalone source. It uses only the Python standard library and deterministic seed 20261024. Four exact-rational five-vertex reduced-Laplacian determinants independently match the polynomial formula in the uniform, interior, equality-boundary, and strict-deletion cases. The script also checks 168 additional randomly generated unicyclic instances, their budgets and KKT equations, and 6,720 randomly generated feasible competing allocations. This finite testing validates implementations and examples, **not** the universal proof; the preceding seven analytic steps establish the infinite-family statement.

## Relationship to prior work

The weighted matrix-tree theorem, general log-determinant concavity, and KKT optimality conditions are established mathematical tools, not claimed as new. Boyd's 2006 work studies convex spectral optimization of weighted graph Laplacians. Osting, Brune, and Osher identify determinant optimality for graph-Laplacian information matrices (Proposition 4.2, D-optimality), primarily in an integer edge-sampling model. Bailey and Cameron's *Combinatorics of optimal designs*, Theorem 4.1, shows that the unweighted cycle maximizes the spanning-tree count **among unweighted unicyclic graph topologies**; this is a different design variable. Sagnol and Harman's general D-optimality formulation covers constrained numerical optimization but does not, in the inspected publicly available description, supply a unicyclic heterogeneous-price closed form.

Previously investigated equal-price cyclic networks and general log-determinant design formulations already imply or treat restricted instances. The contribution assessed here is the simultaneous arbitrary positive edge-price classification on every fixed unicyclic topology, including attached trees, its exact edge-deletion threshold, its unique optimum, and a constructive scalar-root formula. An exhaustive historical priority claim is not made.

## Limitations

The theorem assumes one cycle, positive linear prices, nonnegative freely chosen conductances, and an unrestricted continuous budget. It does not cover graphs with two or more independent cycles, integer comparison counts, nonzero lower bounds on every edge, multiobjective designs, or nonlinear construction costs. Existing design theory may contain related reformulations; a literature search is not a proof that no equivalent result was previously published. Independent verification beyond the analytical reconstruction and the supplied computations has not been performed.

## References

1. S. Boyd, *Convex Optimization of Graph Laplacian Eigenvalues*, International Congress of Mathematicians (2006), https://web.stanford.edu/~boyd/papers/pdf/cvx_opt_graph_lapl_eigs.pdf.
2. B. Osting, C. Brune, and S. Osher, *Optimal Data Collection for Informative Rankings Expose Well-Connected Graphs*, arXiv:1207.6430 (initial posting 2012-07-26), https://arxiv.org/abs/1207.6430; full text https://ww3.math.ucla.edu/camreport/cam12-32.pdf.
3. R. A. Bailey and P. J. Cameron, *Combinatorics of Optimal Designs*, Theorem 4.1 and §4.2, https://webspace.maths.qmul.ac.uk/l.h.soicher/designtheory.org/library/preprints/optimal.pdf.
4. G. Sagnol and R. Harman, *Computing Exact D-optimal Designs by Mixed Integer Second-Order Cone Programming*, arXiv:1307.4953, https://arxiv.org/abs/1307.4953.
