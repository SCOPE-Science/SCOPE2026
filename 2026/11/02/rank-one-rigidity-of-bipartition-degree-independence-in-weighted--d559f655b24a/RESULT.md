# Rank-one rigidity of bipartition degree independence in weighted spanning trees

## Finding

Let \(a,b\ge 2\) be integers and let \(W=(w_{ij})\) be any strictly positive real \(a\)-by-\(b\) matrix. Choose a spanning tree \(T\) of \(K_{a,b}\) with probability proportional to the product of its edge weights \(w_{ij}\). Let \(D^A=(\deg_T(A_i))_{i=1}^a\) and \(D^B=(\deg_T(B_j))_{j=1}^b\) be the vectors of **ordinary (unweighted) degrees** in the sampled tree.

**Theorem.** The random vectors \(D^A\) and \(D^B\) are independent **if and only if** the strictly positive matrix \(W\) has rank one, equivalently if and only if there exist positive vectors \(u,v\) such that \(w_{ij}=u_i v_j\) for every \(i,j\).

The converse has a constructive refinement. For \(j=1,\ldots,b\), let \(E_j\) be the positive-probability event that \(B_j\) has degree \(a\) and every other vertex in part \(B\) has degree one. Put \(m_{ij}=\mathbb E[D^A_i\mid E_j]\) and \(p_{ij}=w_{ij}/\sum_{r=1}^a w_{rj}\). Then, for every \(i,j\),
\[
m_{ij}=1+\sum_{k\ne j}p_{ik},\qquad
p_{ij}=\frac{1}{b-1}\sum_{h=1}^{b}(m_{ih}-1)-(m_{ij}-1).
\]
Thus the collection of \(ab\) conditional **degree means** recovers the entire column-normalized weight matrix. In particular, independence forces these normalized columns to coincide.

For \(w_{ij}=u_i v_j\), the independent vectors have the explicit laws
\[
D^A\stackrel{d}{=}\mathbf1_a+\operatorname{Multinomial}\left(b-1;\frac{u_1}{\sum_r u_r},\ldots,\frac{u_a}{\sum_r u_r}\right),\qquad
D^B\stackrel{d}{=}\mathbf1_b+\operatorname{Multinomial}\left(a-1;\frac{v_1}{\sum_s v_s},\ldots,\frac{v_b}{\sum_s v_s}\right).
\]

## Assumptions and scope

The underlying graph is the complete bipartite graph with labeled parts \(A_1,\ldots,A_a\) and \(B_1,\ldots,B_b\), where \(a,b\ge2\). All \(ab\) edge probability weights are finite and strictly positive. The tree is sampled according to \(\Pr(T)=Z^{-1}\prod_{A_iB_j\in T}w_{ij}\), where \(Z\) is the sum over all spanning trees. Graph degrees count incident edges, **not** their numerical weights. Neither non-complete bipartite graphs nor matrices with zero entries are included.

## Proof

**1. A high-degree witness event.** Fix \(j\). The degree sum on the \(B\)-side is \(a+b-1\) in every tree. Event \(E_j\) requires degrees \((1,\ldots,1,a,1,\ldots,1)\), which indeed sum to \(a+b-1\). On that event, \(B_j\) is adjacent to **all** \(a\) vertices in part \(A\), while each other \(B_k\) is a leaf attached to precisely one \(A_i\). Conversely every such choice of attachments gives a tree. Its probability weight factors as
\[
\left(\prod_{i=1}^a w_{ij}\right)\prod_{k\ne j}w_{I_k,k},
\]
where \(I_k\in\{1,\ldots,a\}\) is the parent of leaf \(B_k\). Consequently \(E_j\) has strictly positive total weight
\[
\left(\prod_{i=1}^a w_{ij}\right)\prod_{k\ne j}\sum_{r=1}^a w_{rk}.
\]
Conditional on \(E_j\), the variables \(I_k\), for \(k\ne j\), are independent with \(\Pr(I_k=i\mid E_j)=p_{ik}\). Hence
\[
D^A_i=1+\sum_{k\ne j}\mathbf1\{I_k=i\},
\]
which gives \(m_{ij}=1+\sum_{k\ne j}p_{ik}\).

**2. Recovery and necessity.** Sum the last identity over \(j\), observing that each \(p_{ik}\) appears exactly \(b-1\) times:
\[
\sum_{j=1}^b (m_{ij}-1)=(b-1)\sum_{k=1}^b p_{ik}.
\]
Subtract the original equation for a given \(j\), obtaining the claimed formula for \(p_{ij}\). If \(D^A\) and \(D^B\) are independent, then \(\mathbb E[D^A_i\mid E_j]=\mathbb E D^A_i\) is independent of \(j\), because \(E_j\) is measurable with respect to \(D^B\) and has positive probability. The recovery formula shows \(p_{ij}\) is independent of \(j\) for every \(i\). Denote this common value by \(u_i>0\). With \(v_j=\sum_r w_{rj}>0\), obtain \(w_{ij}=u_i v_j\), proving the only-if implication.

**3. Sufficiency by an exact tree generating polynomial.** Suppose \(w_{ij}=u_i v_j\). For positive indeterminates \(x_i,y_j\), set \(z_i=u_i x_i\), \(t_j=v_j y_j\), \(U=\sum_i z_i\), \(V=\sum_j t_j\). Kirchhoff's weighted matrix-tree theorem gives
\[
\sum_T\prod_{A_iB_j\in T}z_i t_j
=\left(\prod_{i=1}^a z_i\right)\left(\prod_{j=1}^b t_j\right)U^{b-1}V^{a-1}.
\]
For completeness, the weighted graph Laplacian has diagonal blocks \(V\operatorname{diag}(z_i)\), \(U\operatorname{diag}(t_j)\) and off-diagonal block \(-zt^\mathsf T\). Delete the row and column for \(B_b\) and take the Schur complement of the positive diagonal block \(V\operatorname{diag}(z_i)\). The remaining block is \(U[\operatorname{diag}(t_1,\ldots,t_{b-1})-tt^\mathsf T/V]\), where in this block \(t=(t_1,\ldots,t_{b-1})^\mathsf T\). The matrix-determinant lemma gives its determinant as \(U^{b-1}\prod_{j=1}^b t_j/V\). Multiplying by \(V^a\prod_i z_i\) yields the displayed enumerator. The identity holds for positive arguments and hence as a polynomial identity.

Substitute \(z_i=u_i x_i\), \(t_j=v_j y_j\) and divide by the same expression at \(x_i=y_j=1\). The joint probability-generating function is
\[
\mathbb E\!\left[\prod_i x_i^{D^A_i}\prod_j y_j^{D^B_j}\right]
=\left(\prod_i x_i\right)\left(\frac{\sum_i u_i x_i}{\sum_i u_i}\right)^{b-1}
\left(\prod_j y_j\right)\left(\frac{\sum_j v_j y_j}{\sum_j v_j}\right)^{a-1}.
\]
It factors into the marginal generating functions, establishing independence and the stated multinomial laws. Together with step 2, this proves the equivalence.

## Verification

The proof is valid for **every** pair of integers \(a,b\ge2\) and all strictly positive real weights. `check.py` supplies separate exact finite tests: it enumerates every spanning tree and evaluates the weight and degree vectors using rational arithmetic for fourteen weighted cases with \((a,b)\in\{(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,3)\}\), using one rank-one and one heterogeneous weight matrix at each size. It verifies the event-conditional means, reconstruction, equivalence of rank-one and observed independence, and the entire product-multinomial joint mass function in rank-one cases. All fourteen cases pass with `python check.py` (Python standard library only). Finite enumeration is corroboration; the unrestricted theorem rests on the preceding proof.

As a boundary witness, the positive matrix \(W=\bigl(\begin{smallmatrix}1&1\\1&2\end{smallmatrix}\bigr)\) has unequal normalized columns. In \(K_{2,2}\), the conditional expected degree of \(A_1\) is \(4/3\) given \(E_1\) and \(3/2\) given \(E_2\), so independence fails.

## Relationship to prior work

Fita Sanmartín, Schnörr and Hamprecht (first posted 2024-09-20, arXiv:2409.13472) developed general expectation, variance and covariance formulas for degrees in weighted spanning-tree Gibbs laws, and explained how to obtain a single-vertex degree polynomial. This supplies the motivating probability model but not the present cross-bipartition independence characterization or conditional recovery identity. Dong and Ge (2021, arXiv:2103.05294) provided exact counts for **unweighted** complete-bipartite spanning trees containing prescribed forests; these counts do not supply a rank-one-only classification for arbitrary positive matrix weights. Fischer and Fischer (2019, DOI 10.1002/jgt.22449) studied equality of the numbers of attainable degree sequences on two parts of a general bipartite graph, a different enumeration property. The standard bipartite Prüfer formula implies the rank-one **sufficiency** direction; the classification's independent content is the converse for all positive weights, witnessed by conditional means and the explicit identifiability map.

## Limitations

Strictly positive edge weights and two parts of size at least two are essential hypotheses. If one part has a single vertex, all degree vectors are deterministic even for arbitrary weights. Permitting zero weights admits graphs with only one spanning tree, again producing deterministic independent degree vectors without rank-one weights. The theorem concerns independence of entire partwise degree vectors, not just a single pair of vertex degrees. Conditional recovery identifies \(p_{ij}\), not each absolute column scale \(\sum_r w_{rj}\). It does not claim to characterize general weighted bipartite graphs or other tree measures. Literature searches do not establish definitive historical priority, and independent validation has not been performed.

## References

- Enrique Fita Sanmartín, Christoph Schnörr and Fred A. Hamprecht, *Expectation and Variance of the Degree of a Node in Random Spanning Trees*, arXiv:2409.13472v1, 2024-09-20. https://arxiv.org/abs/2409.13472
- Fengming Dong and Jun Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest*, arXiv:2103.05294v1, 2021-03-09. https://arxiv.org/abs/2103.05294
- Anja Fischer and Frank Fischer, *Counting degree sequences of spanning trees in bipartite graphs: A graph-theoretic proof*, J. Graph Theory 92 (2019), 230–236. https://doi.org/10.1002/jgt.22449
- Kirchhoff's weighted matrix-tree theorem and the classical bipartite spanning-tree enumerator, as described in the cited literature.
