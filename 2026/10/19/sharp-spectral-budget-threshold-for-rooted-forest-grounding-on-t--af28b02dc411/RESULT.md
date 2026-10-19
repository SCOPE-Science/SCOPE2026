# Sharp spectral budget threshold for rooted-forest grounding on transitive coronas

## Finding

**Theorem.** Let \(H\) be any connected, finite, simple, vertex-transitive graph on \(m\ge3\) vertices, with every original edge of unit conductance. Construct the one-leaf corona \(G=H\circ K_1\) by adjoining one private leaf to every core vertex, also by a unit-conductance edge. Under an arbitrary positive budget \(B\), assign an independent nonnegative grounding conductance \(g_v\) to each of the \(2m\) vertices, with \(\sum_v g_v=B\). Maximize the rooted-forest determinant
\[
\Delta(g)=\det\!\bigl(L_G+\operatorname{diag}(g)\bigr).
\]

Write the Laplacian eigenvalues of \(H\), with multiplicities, as \(0=\lambda_0<\lambda_1\le\cdots\le\lambda_{m-1}\), and define on \(0<a<1\)
\[
R_H(a)=(2-a)\sum_{j=1}^{m-1}\frac{\lambda_j}{\lambda_j+a}.
\]
There is exactly one \(a_H\in(0,1)\) with \(R_H(a_H)=m\). Put \(B_H=m a_H/(1-a_H)\). The unique **unrestricted** optimal gain vector assigns one gain \(x\) to every core vertex and another gain \(y\) to every private leaf, with \(m(x+y)=B\). Its support undergoes a sharp phase transition:
\[
\begin{cases}
x=0,\quad y=B/m,&0<B\le B_H,\\
x>0,\quad y>0,&B>B_H.
\end{cases}
\]
For the second regime set \(s=B/m\). The unique optimal \(y\in(0,s)\) solves
\[
\frac{m}{1+y}+\left(\frac{1}{(1+y)^2}-1\right)
\sum_{j=0}^{m-1}\frac{1}{\lambda_j+s-y+y/(1+y)}=0,
\qquad x=s-y.
\]
At every budget the optimum has \(y>0\): grounding only the core is never optimal.

The critical budget has a sharp universal extremum:
\[
0<B_H\le\frac{m(m-2)}{2},
\quad\text{with equality precisely when }H=K_m.
\]
If \(H\) and \(H'\) are connected vertex-transitive graphs on the same labelled vertex set and \(E(H)\subsetneq E(H')\), then \(B_H<B_{H'}\). In particular, adding edges while retaining vertex-transitivity strictly enlarges the low-budget leaf-only regime.

For the clique, \(a_{K_m}=(m-2)/m\) and \(B_{K_m}=m(m-2)/2\). For the four-cycle, the spectral equation yields \(a_{C_4}=(-4+2\sqrt7)/3\) and \(B_{C_4}=8\sqrt7/7\), strictly below \(B_{K_4}=4\).

## Assumptions and scope

The core \(H\) is simple, undirected, connected, vertex-transitive and has at least three vertices. Every original or pendant graph edge has fixed, equal conductance one; **only** the diagonal grounding gains are decision variables. Their prices are all one. The budget equality has \(B>0\) and gains may be zero. No fixed number of grounded vertices is stipulated. The determinant is strictly positive for every feasible vector: for a nonzero vector \(z\), the quadratic form equals the sum of squared edge differences and nonnegative grounded squares; connectedness and a positive gain force strict positivity. Thus logarithms and derivatives are defined throughout the feasible simplex, including its boundary.

The claim is a theorem about a determinant (equivalently the weighted total of rooted spanning forests with vertex-dependent root weights). It is not a claim that the same allocation minimizes trace of an inverse, maximizes the smallest grounded eigenvalue, or optimizes edge conductances.

## Proof

**1. Unrestricted uniqueness and symmetry.** Set \(M(g)=L_G+\operatorname{diag}(g)\). Along any nonzero real diagonal perturbation \(D=\operatorname{diag}(d)\),
\[
\frac{d^2}{d\epsilon^2}\log\det(M(g)+\epsilon D)\bigg|_{\epsilon=0}
=-\operatorname{tr}(M(g)^{-1}D M(g)^{-1}D)
=-\|M(g)^{-1/2}D M(g)^{-1/2}\|_F^2<0.
\]
Therefore \(\log\det M\) is strictly concave on the entire feasible simplex, and compactness gives a unique maximizer. Every automorphism of \(H\) induces an automorphism of its corona preserving the budget and determinant; uniqueness forces its optimal gains to be invariant. Vertex-transitivity makes the core vertices one orbit and the leaves another. Hence the unrestricted optimizer has equal core gains \(x\) and equal leaf gains \(y\).

**2. Exact determinant and one-variable reduction.** Write \(s=B/m\), so \(x=s-y\) and \(0\le y\le s\). In the core-then-leaf vertex order,
\[
M(x,y)=\begin{pmatrix}L_H+(1+x)I&-I\\-I&(1+y)I\end{pmatrix}.
\]
Taking the Schur complement of the leaf block gives
\[
\Delta(x,y)=(1+y)^m
\prod_{j=0}^{m-1}\left(\lambda_j+x+\frac{y}{1+y}\right).
\]
Define \(A(y)=s-y+y/(1+y)\) and \(F_s(y)=\log\Delta(s-y,y)\). Then
\[
F_s'(y)=\frac{m}{1+y}
+\left(\frac{1}{(1+y)^2}-1\right)
\sum_{j=0}^{m-1}\frac{1}{\lambda_j+A(y)}.
\]
The strict concavity proved in Step 1 implies \(F_s\) is strictly concave. At the core-only endpoint, \(F_s'(0)=m>0\), so the optimizer has \(y>0\) for all \(s>0\).

**3. The sharp transition.** At the leaf-only endpoint \(y=s\), put \(a=s/(1+s)\in(0,1)\). Substituting \(A(s)=a\), \(1/(1+s)=1-a\), and separating the zero eigenvalue yields
\[
F_s'(s)=m(1-a)-a(2-a)\left(\frac1a+
\sum_{j=1}^{m-1}\frac1{\lambda_j+a}\right)
=(2-a)\sum_{j=1}^{m-1}\frac{\lambda_j}{\lambda_j+a}-m
=R_H(a)-m.
\]
Each summand \((2-a)\lambda_j/(\lambda_j+a)\) is strictly decreasing in \(a\in(0,1)\). Furthermore \(R_H(0)=2(m-1)>m\) and \(R_H(1)<m-1<m\). Thus a unique \(a_H\in(0,1)\) solves \(R_H(a_H)=m\). Since \(a=s/(1+s)\) is strictly increasing in \(B=ms\), strict concavity implies: when \(B\le B_H\), the right-end derivative is nonnegative and the unique maximum is \(y=s\); when \(B>B_H\), this derivative is negative while \(F_s'(0)>0\), so exactly one interior stationary point is the global maximum. The equality case belongs to the leaf-only regime, including uniqueness.

**4. Extremal graph and monotonicity.** For every simple \(m\)-vertex graph, \(L_{K_m}-L_H=L_{\overline H}\succeq0\). On the orthogonal complement of the constant vector, this bounds each positive eigenvalue of \(L_H\) by \(m\). Consequently, for \(0<a<1\),
\[
R_H(a)\le (2-a)\frac{m(m-1)}{m+a}=R_{K_m}(a).
\]
The inequality is strict for every noncomplete \(H\), because at least one positive eigenvalue is strictly below \(m\). Direct substitution shows \(R_{K_m}((m-2)/m)=m\), giving \(a_H\le(m-2)/m\), with equality only for the clique. The map \(a\mapsto m a/(1-a)\) is strictly increasing, proving the sharp budget bound.

Finally, suppose \(H'\) is formed by adding at least one edge to \(H\). For \(a>0\), matrix-inverse order and the identity
\[
L(L+aI)^{-1}=I-a(L+aI)^{-1}
\]
show that \(\operatorname{tr}(L_{H'}(L_{H'}+aI)^{-1})>\operatorname{tr}(L_H(L_H+aI)^{-1})\). The strict inequality follows because the added-edge Laplacian is a nonzero positive-semidefinite matrix; the two positive-definite resolvents have a nonzero positive-semidefinite difference. The constant eigenvalue contributes zero to both traces. Thus \(R_{H'}(a)>R_H(a)\) throughout \(0<a<1\). Both functions decrease through the level \(m\), so their roots and critical budgets satisfy \(a_{H'}>a_H\) and \(B_{H'}>B_H\).

## Verification

The standalone program `verify_corona.py` constructs original-core and full-corona Laplacians independently for complete graphs, cycles, hypercubes and balanced complete bipartite cores. It checks Schur-complement determinants against full matrix determinants, reduced first derivatives, optimum boundary/interior conditions, unrestricted Karush–Kuhn–Tucker gradients, graph-extremal bounds, numerical maximization, and independently sampled asymmetric alternatives. Its SymPy checks include the exact clique threshold and the four-cycle resolvent identity. The program reports `VERIFY_OK 1216` when executed with NumPy, SciPy and SymPy. This is supporting finite validation; the preceding argument proves the universal result.

## Relationship to prior work

Chebotarev and Shamis, *Matrix-Forest Theorems*, arXiv:math/0602575 (initial arXiv public date 25 February 2006), provide the weighted matrix-forest framework and determinant interpretation. Their theorems do not optimize arbitrary vertex-root conductances under a budget or identify a vertex-transitive corona threshold.

Khosoussi and collaborators, arXiv:1604.01116, optimize weighted spanning-tree counts primarily through edge selection and graph synthesis. Their edge-design results do not imply the vertex-diagonal allocation theorem. Du and collaborators, *Consensus analysis of the weighted corona networks* (2022), derive corona spectral/first-order coherence formulas with fixed edge parameters, not D-optimal diagonal grounding. Liu and collaborators, arXiv:1804.10818, optimize pinning based on the smallest eigenvalue of a grounded Laplacian obtained by deleting selected rows and columns; that is neither a log-determinant objective nor a continuous allocation of all vertex gains.

Existing complete-bipartite D-optimal grounding classifications address another family and do not imply the corona result: the \(m\)-leaf corona of a connected \(m\)-vertex core, \(m\ge3\), is not a complete bipartite graph. Its exact Schur-reduced grounded Laplacian and the graph-uniform extremal threshold have different content. Searches of relevant published finding records found no equivalent theorem, but search absence is not a proof of novelty.

## Limitations

The base must be connected and vertex-transitive, and its graph edges must be unit weighted. Arbitrary unequal vertex prices and nontransitive core graphs are not covered. The mixed-phase gain is specified uniquely by a scalar equation, not generally by radicals. The universal critical-budget bound concerns this forest determinant only; it does not transfer automatically to other pinning objectives. No independent mathematical audit has been performed. The mathematical originality assessment is limited by available indexed literature, which may omit a stronger or equivalent result.

## References

1. P. Chebotarev and E. Shamis, *Matrix-Forest Theorems*, arXiv:math/0602575, first publicly posted 2006-02-25, https://arxiv.org/abs/math/0602575.
2. K. Khosoussi et al., *Maximizing the Weighted Number of Spanning Trees: Near-t-Optimal Graphs*, arXiv:1604.01116, 2016, https://arxiv.org/abs/1604.01116.
3. W. Du, J. Zhu, H. Gao and X. Li, *Consensus analysis of the weighted corona networks*, Frontiers in Physics 10 (2022), article 948247, https://doi.org/10.3389/fphy.2022.948247.
4. H. Liu, X. Xu, J.-A. Lu, G. Chen and Z. Zeng, *Optimizing Pinning Control of Complex Dynamical Networks Based on Spectral Properties of Grounded Laplacian Matrices*, arXiv:1804.10818, https://arxiv.org/abs/1804.10818.
