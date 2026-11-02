# Conditional edge correlations in degree-constrained complete-bipartite spanning trees

## Finding
For a uniformly random spanning tree of a complete bipartite graph, conditioning on the **entire labeled degree sequence** need not preserve negative association of disjoint edges. There is an exact, universal pair-inclusion formula which implies that incident edge indicators remain nonpositively correlated, whereas disjoint edge indicators can be positively, negatively, or zero correlated.

Let \(A=\{1,\ldots,a\}\) and \(B=\{1,\ldots,b\}\), with integers \(a,b\ge2\), and let \(T\) be a uniformly random spanning tree of \(K_{a,b}\). Fix any feasible labeled degree vector \(d\) with positive entries, whose sums over each color class equal \(a+b-1\). Put
\[
m=b-1,\quad p=a-1,\quad \alpha_i=d_i-1\ (i\in A),\quad \beta_j=d_j-1\ (j\in B),
\]
so \(\sum_i\alpha_i=m\) and \(\sum_j\beta_j=p\). Define \(u_i=\alpha_i/m\) and \(v_j=\beta_j/p\), and the two-sample frequencies
\[
U_{ik}=\begin{cases}\frac{\alpha_i(\alpha_k-\mathbf1_{i=k})}{m(m-1)},&m\ge2,\\0,&m=1,\end{cases}\quad
V_{jl}=\begin{cases}\frac{\beta_j(\beta_l-\mathbf1_{j=l})}{p(p-1)},&p\ge2,\\0,&p=1.\end{cases}
\]
For an edge \(e=(i,j)\), where \(i\in A\), \(j\in B\), abbreviate \(P_e=\Pr(e\in T\mid d)\). For two *distinct* edges \(e=(i,j)\), \(f=(k,l)\), let \(Q_{ef}=\Pr(e,f\in T\mid d)\). Then
\[
P_e=u_i+v_j-u_iv_j
\]
and the **complete pair law** is
\[
Q_{ef}=\begin{cases}
U_{ii}(1-v_j-v_l)+u_i(v_j+v_l),&i=k,\ j\ne l,\\
V_{jj}(1-u_i-u_k)+v_j(u_i+u_k),&j=l,\ i\ne k,\\
U_{ik}(1-v_j-v_l)+V_{jl}(1-u_i-u_k)+u_iv_l+u_kv_j,&i\ne k,\ j\ne l.
\end{cases}
\]
In particular, \(\operatorname{Cov}(\mathbf1_e,\mathbf1_f\mid d)=Q_{ef}-P_eP_f\). For edges sharing their \(A\)-endpoint, this is
\[
(U_{ii}-u_i^2)(1-v_j-v_l)-(1-u_i)^2v_jv_l\le0,
\]
with the corresponding symmetric formula for a shared \(B\)-endpoint. For disjoint edges it is
\[
(U_{ik}-u_iu_k)(1-v_j-v_l)
+(V_{jl}-v_jv_l)(1-u_i-u_k)-u_iu_kv_jv_l.
\]
When \(m,p\ge2\), the disjoint-edge covariance consequently has the explicit sign of
\[
\frac{u_iu_k(1-v_j-v_l)}{m-1}
+\frac{v_jv_l(1-u_i-u_k)}{p-1}-u_iu_kv_jv_l.
\]
This expression is an exact classification, including zero and boundary cases with \(u_i=0\) or \(v_j=0\); for \(m=1\) or \(p=1\), use the preceding formula with \(U,V\) as defined.

A **sharp positive-correlation witness** occurs already for \(K_{2,3}\): take degrees \((2,2)\) in \(A\) and \((2,1,1)\) in \(B\), and take the disjoint edges \(e=(1,2)\) and \(f=(2,3)\). There are exactly two trees with that degree vector, and
\[
\Pr(e\in T\mid d)=\Pr(f\in T\mid d)=\Pr(e,f\in T\mid d)=\tfrac12,
\qquad \operatorname{Cov}(\mathbf1_e,\mathbf1_f\mid d)=\tfrac14.
\]
Thus the conditional covariance attains the largest possible Bernoulli pair covariance. \(K_{2,2}\) admits no positive example because its tree is fixed by its labeled degree vector.

The effect persists **without leaf endpoints**. For each integer \(t\ge3\), in \(K_{t,t}\) prescribe on *each* side the labeled degree vector \((2,2,t-2,1,\ldots,1)\), which has \(t\) entries. For the disjoint edges joining the first and second vertices on the two sides, set \(h=t-1\). Their conditional covariance is exactly
\[
\frac{2h^2-5h+1}{h^4(h-1)}.
\]
It equals \(-1/16\) for \(t=3\), equals \(2/81\) for \(t=4\), and is strictly positive for all \(t\ge4\), even though all four endpoints have degree two.

## Assumptions and scope
All graphs are simple, vertex-labeled, and bipartite with the color classes fixed. The conditioning is on the full **labeled** degree sequence, not merely the unordered degree multiset and not solely the degrees of selected endpoints. Every feasible vector has exactly \(\frac{(b-1)!(a-1)!}{\prod_i\alpha_i!\prod_j\beta_j!}\) trees. Only distinct edge pairs are covered by the displayed joint formula; a single edge has its stated marginal. The expressions include all feasible boundary vectors without positivity assumptions on the excess degrees. The balanced nonleaf family uses exactly \(t\) entries \((2,2,t-2,1,\ldots,1)\) on each side.

## Proof
Give each possible edge \((i,j)\) the product conductance \(c_{ij}=x_i y_j\), with all formal parameters positive. Put \(X=\sum_i x_i\) and \(Y=\sum_j y_j\). The weighted matrix-tree theorem gives the spanning-tree partition function
\[
Z(\boldsymbol x,\boldsymbol y)=\sum_T\prod_{(i,j)\in E(T)}x_i y_j
=\left(\prod_{i\in A}x_i\right)\left(\prod_{j\in B}y_j\right)X^{b-1}Y^{a-1}.
\]
For completeness, the weighted Laplacian has diagonal blocks \(Y\operatorname{diag}(x_i)\) and \(X\operatorname{diag}(y_j)\), and off-diagonal block \(-\boldsymbol x\boldsymbol y^{\mathsf T}\). Deleting one row and column and applying the determinant lemma yields the displayed factorization. Its coefficient at the prescribed exponents \(x_i^{d_i}y_j^{d_j}\) is the class size in the statement.

For any vertices \(s,t\), write \(R_{st}\) for their weighted effective resistance. Solving the weighted Laplacian equations gives, for distinct endpoints within one side and for cross endpoints, respectively,
\[
R_{ik}=\frac1Y\left(\frac1{x_i}+\frac1{x_k}\right),\qquad
R_{jl}=\frac1X\left(\frac1{y_j}+\frac1{y_l}\right),\qquad
R_{ij}=\frac1{x_iY}+\frac1{y_jX}-\frac1{XY}.
\]
For oriented edges \(e=(i,j)\), \(f=(k,l)\) the transfer-current identity gives the cross term
\[
H_{ef}=\frac{R_{il}+R_{kj}-R_{ik}-R_{jl}}2.
\]
If \(i=k\), it is \((X-x_i)/(x_iXY)\); if \(j=l\), it is \((Y-y_j)/(y_jXY)\); if the edges are disjoint, it is \(-1/(XY)\). The weighted spanning-tree pair-inclusion identity is
\[
\Pr_{x,y}(e,f\in T)=c_e c_f\bigl(R_{ij}R_{kl}-H_{ef}^2\bigr),
\quad \Pr_{x,y}(e\in T)=c_e R_{ij}.
\]
Writing \(s_i=x_i/X\), \(t_j=y_j/Y\), the marginal is \(s_i+t_j-s_it_j\). Expanding the pair identity gives the three expressions for \(Q_{ef}\), *before conditioning*, with \(s_i\) in place of \(u_i\), \(t_j\) in place of \(v_j\), and \(s_i s_k\), \(t_jt_l\) in place of \(U_{ik}\), \(V_{jl}\), including repeated indices.

To condition, multiply the weighted inclusion probabilities by \(Z\) and extract the coefficient at the prescribed degree monomial. The factor \(X^m\) has multinomial coefficient proportional to \(m!/\prod_i\alpha_i!\). Consequently the coefficient-extraction ratios for \(x_i/X\) and \(x_ix_k/X^2\) equal \(u_i\) and \(U_{ik}\), respectively, including the repeated-index falling factorial. The \(Y^p\) extraction analogously yields \(v_j,V_{jl}\). Independence of the two formal variable sets makes mixed products factor. This gives the claimed exact finite pair law, including \(m=1\) and \(p=1\).

For two distinct \(B\)-endpoints, \(v_j+v_l\le1\). Sampling two positions without replacement gives \(U_{ii}\le u_i^2\), so the displayed shared-\(A\) covariance is nonpositive. The shared-\(B\) case is symmetric. For disjoint edges and \(m\ge2\), one has \(U_{ik}-u_iu_k=u_iu_k/(m-1)\) for \(i\ne k\), and the analogous identity for \(V\), proving the exact sign expression. Substitution of the two exhibited degree vectors yields \(1/4\) and \((2h^2-5h+1)/(h^4(h-1))\); elementary algebra gives the strict signs for \(h=2\) versus \(h\ge3\). No asymptotic extrapolation is required.

## Verification
The accompanying `conditional_bipartite_edge_verifier.py` uses only the Python standard library, independently enumerates spanning trees by acyclic edge subsets, conditions on all labeled degree vectors, and compares exact rational marginal and pair probabilities against the formulas. Run `python3 conditional_bipartite_edge_verifier.py`. It passed 231,113 exact assertions over \(K_{2,2}\), \(K_{2,3}\), \(K_{2,4}\), \(K_{2,5}\), \(K_{3,3}\), \(K_{3,4}\), and \(K_{4,4}\), including all pairs for every feasible degree class, the class-size formula, the sharp \(1/4\) witness, and the \(2/81\) nonleaf witness. These finite tests corroborate, but do not replace, the algebraic proof for all sizes.

## Relationship to prior work
The weighted spanning-tree determinant and transfer-current determinantal measure are classical; see Lyons (2002) and Grimmett–Winkler (2003) on the unconditioned negative-association theory. Their edge negative-association results do **not** state that negative association survives conditioning on the complete degree vector. Martin–Reiner (2003) provide further weighted spanning-tree polynomial methodology but not this conditioned pair law. Dong–Ge (2021) count complete-bipartite spanning trees containing a specified forest **without simultaneously prescribing every vertex degree**. The present statement uses those established ingredients but adds the full conditional pair law, sign classification, and sharp reversal examples. The theorem makes no claim that the determinant or transfer-current method is new.

## Limitations
The results concern complete bipartite host graphs, exact uniform spanning trees, and conditioning on a feasible *labeled* degree vector; arbitrary bipartite host graphs or degree-multiset conditioning are not covered. The claim proves pairwise correlation properties, not positive association of arbitrary increasing events. Publicly available relevant sources were inspected, but the possibility of an equivalent earlier specialization of a broader weighted enumeration or a different encoding of degree-conditioned trees cannot be excluded without independent historical assessment.

## References
- R. Lyons, *Determinantal Probability Measures*, arXiv:math/0204325, first posted 2002-04-26. https://arxiv.org/abs/math/0204325
- G. R. Grimmett and M. Winkler, *Negative Association in Uniform Forests and Connected Graphs*, arXiv:math/0302185, first posted 2003-02-17. https://arxiv.org/abs/math/0302185
- J. L. Martin and V. Reiner, *Factorizations of Some Weighted Spanning Tree Enumerators*, arXiv:math/0302213, first posted 2003-02-18. https://arxiv.org/abs/math/0302213
- F. Dong and J. Ge, *Counting Spanning Trees in a Complete Bipartite Graph Which Contain a Given Spanning Forest*, arXiv:2103.05294, first posted 2021-03-09. https://arxiv.org/abs/2103.05294
