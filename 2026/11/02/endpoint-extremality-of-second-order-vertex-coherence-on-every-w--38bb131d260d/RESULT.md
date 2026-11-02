# Endpoint extremality of second-order vertex coherence on every weighted path

## Finding
For every path \(P_n\), \(n\ge3\), equipped with arbitrary strictly positive undirected edge conductances \(w_k\), set \(L=\sum_{k=1}^{n-1}w_k(e_k-e_{k+1})(e_k-e_{k+1})^{\mathsf T}\) and let \(H=L^\dagger\). The **second-order vertex coherence** at vertex \(v\) is
\[
F(v)=(H^2)_{vv}=\sum_{u=1}^n H_{vu}^2=\|He_v\|_2^2.
\]
Then
\[
\boxed{\max_{1\le v\le n}F(v)=\max\{F(1),F(n)\}},
\]
and the inequality is **strict at every interior vertex**:
\[
1<v<n\quad\Longrightarrow\quad F(v)<\max\{F(1),F(n)\}.
\]
Both endpoints may tie, as happens with reflection-symmetric conductance assignments. The result is uniform in the number of vertices and the entire positive weight vector. It identifies the worst vertex for a second-order noise/coherence metric without requiring individual vertexwise evaluation of the pseudoinverse square.

## Assumptions and scope
The graph is the connected undirected simple path on labeled vertices \(1,\ldots,n\), \(n\ge3\). Edge \(k\), connecting vertices \(k\) and \(k+1\), has any conductance \(w_k>0\). The Laplacian uses the unnormalized combinatorial convention, and \(H=L^\dagger\) is the symmetric Moore–Penrose pseudoinverse satisfying \(H\mathbf1=0\). Because \(L\) is real symmetric and positive semidefinite,
\[
(L^2)^\dagger=(L^\dagger)^2=H^2.
\]
This identifies the metric with squared-Laplacian or biharmonic vertex coherence, distinct from first-order coherence \(H_{vv}\) and from whole-network coherence \(\operatorname{tr}(H^2)\). No optimality over choices of conductance is asserted; the theorem precisely optimizes the **vertex location** of maximum second-order coherence for every fixed positive conductance vector.

## Proof
**1. Centered Green-column embedding.** Put \(z_v=He_v\in\mathbf1^\perp\) and, for \(1\le k\le n-1\), let \(s_k=z_{k+1}-z_k=H(e_{k+1}-e_k)\). The equation
\[
L s_k=e_{k+1}-e_k,
\qquad \mathbf1^{\mathsf T}s_k=0
\]
has an explicit solution. Indeed, since the graph is a tree, a unit source at \(k+1\) and a unit sink at \(k\) send current only across the intervening edge. The potential is constant on each side of that edge and jumps by \(1/w_k\). Centering its mean gives, for every coordinate \(j\),
\[
(s_k)_j=\frac1{w_k}
\begin{cases}-(n-k)/n,&j\le k,\\ k/n,&j>k.\end{cases}
\tag{1}
\]
For \(1\le i<j\le n-1\), the centered step functions in (1) have inner product
\[
\langle s_i,s_j\rangle=
\frac{i(n-j)}{n\,w_iw_j}>0.
\tag{2}
\]
For \(i=j\), the corresponding norm square is \(i(n-i)/(n w_i^2)>0\). Equivalently, for all edge indices,
\[
\langle s_i,s_j\rangle=
\frac{\min(i,j)[n-\max(i,j)]}{n\,w_iw_j}>0.
\tag{3}
\]
Thus any two nonzero positive linear combinations of nonempty collections of the increments have strictly positive inner product, and adding a positive increment strictly increases the squared norm of any nonzero positive combination.

**2. Express all columns through the increments.** Since \(H\mathbf1=0\), the column vectors satisfy \(\sum_{v=1}^n z_v=0\). Also \(z_v=z_1+\sum_{k<v}s_k\). Summing this identity over all \(v\) yields
\[
z_1=-\sum_{k=1}^{n-1}\frac{n-k}{n}s_k,
\qquad
z_n=\sum_{k=1}^{n-1}\frac{k}{n}s_k,
\tag{4}
\]
and, for every \(v\),
\[
z_v=\underbrace{\sum_{k<v}\frac{k}{n}s_k}_{P_v}
-\underbrace{\sum_{k\ge v}\frac{n-k}{n}s_k}_{Q_v}.
\tag{5}
\]
Write additionally
\[
V_v=\sum_{k<v}\frac{n-k}{n}s_k,
\qquad
U_v=\sum_{k\ge v}\frac{k}{n}s_k.
\]
Then \(z_1=-(V_v+Q_v)\), \(z_n=P_v+U_v\), and \(z_v=P_v-Q_v\). Every displayed coefficient is nonnegative.

**3. Interior vertices in the left half.** Suppose \(1<v<n\) and \(v\le(n+1)/2\). For every \(k<v\), one has \(k\le n/2\), hence \((n-k)/n\ge k/n\). Therefore \(V_v-P_v\) is a nonnegative linear combination of \(s_k\). Using (3),
\[
\|V_v\|_2^2-\|P_v\|_2^2
=\langle V_v-P_v,V_v+P_v\rangle\ge0.
\]
Now
\[
\begin{aligned}
F(1)-F(v)
&=\|V_v+Q_v\|_2^2-\|P_v-Q_v\|_2^2\\
&=\|V_v\|_2^2-\|P_v\|_2^2
  +2\langle V_v+P_v,Q_v\rangle>0.
\end{aligned}
\tag{6}
\]
The final inequality is strict because an interior \(v\) makes both the earlier- and later-edge sets nonempty, so \(V_v+P_v\) and \(Q_v\) are nonzero positive combinations of increments, whose inner product is positive by (3). Hence every vertex in the left half has strictly smaller second-order coherence than the left endpoint.

**4. Interior vertices in the right half.** Suppose \(1<v<n\) and \(v\ge(n+1)/2\). For each \(k\ge v\), one has \(k\ge n/2\), so \(k/n\ge(n-k)/n\) and \(U_v-Q_v\) is a nonnegative combination of increments. By the same positivity,
\[
\begin{aligned}
F(n)-F(v)
&=\|P_v+U_v\|_2^2-\|P_v-Q_v\|_2^2\\
&=\|U_v\|_2^2-\|Q_v\|_2^2
+2\langle P_v,U_v+Q_v\rangle>0.
\end{aligned}
\tag{7}
\]
Again, strictness uses positive conductances and nonempty earlier- and later-edge sets. Each integer \(1<v<n\) belongs to at least one of the two halves, so (6) or (7) proves the theorem for all such vertices.

**5. Exact normalization and interpretation.** Because \(H^2=(L^2)^\dagger\), the same conclusion can be stated in terms of the squared-Laplacian Green operator. Defining biharmonic squared distance as \(d_B(a,b)^2=(e_a-e_b)^{\mathsf T}H^2(e_a-e_b)\), direct expansion and \(H^2\mathbf1=0\) yield
\[
F(v)=\frac1n\sum_{u=1}^n d_B(v,u)^2
-\frac1{2n^2}\sum_{u,t=1}^n d_B(u,t)^2.
\tag{8}
\]
The common correction is independent of \(v\), so the theorem also asserts that the largest mean-squared biharmonic distance from a path vertex occurs at a path endpoint. No assumption that \(v\mapsto F(v)\) is convex, monotone on each half, or unimodal entered the proof.

## Verification
Equation (1) is independently checkable by evaluating the centered step potential and substituting it into \(Ls_k=e_{k+1}-e_k\). Its pairwise inner product (3) is an elementary three-interval calculation. Equations (4)–(5) follow from telescoping and zero column sums, and inequalities (6)–(7) use only strictly positive pairwise inner products, so this is a complete analytic proof for every permitted dimension and conductance vector.

Additional computational stress tests conducted prior to the review constructed weighted Laplacians, formed their full symmetric pseudoinverses, and compared the squared row norms at every vertex for \(26{,}000\) randomly weighted paths of orders \(3\) through \(15\). No interior maximizer appeared. These finite checks are corroboration, not the basis of the proof or evidence of exhaustive enumeration. The formulas above give independent reproducibility without any external certificate.

## Relationship to prior work
Sun, Ding, Zhang and Chen (2014) study first- and second-order **network-average** coherence through sums of inverse Laplacian eigenvalues, including squared inverses, for recursive tree families; the relevant result is a trace quantity, not the maximum **individual diagonal** of \(H^2\) over all arbitrarily weighted paths. Summers, Shames, Lygeros and Dörfler (2014) study trace-based network coherence and graph-topology design; this again does not imply the vertexwise squared-pseudoinverse extremality statement. Ghosh, Boyd and Saberi (2008) optimize total effective resistance and discuss maximum pairwise effective resistance, not the individual squared-Green diagonal. Later work on approximating biharmonic vertex coherence confirms this is a natural separately computed local quantity but does not, from its inspected abstract, state the universal weighted-path endpoint principle.

The proof here uses a quantitative positivity of centered cut potentials that is not a corollary of first-order endpoint formulas or trace bounds alone. Nevertheless, comparison with obscure historical work remains incomplete; these observations do not certify worldwide novelty.

## Limitations
The theorem requires a connected **undirected path**, strictly positive edge conductances, the unnormalized symmetric combinatorial Laplacian, and exactly the squared-pseudoinverse diagonal metric. It does not assert the same extremal rule for graphs with cycles, directed networks, arbitrary noise covariance, or higher inverse powers. It locates the worst vertex but does **not** solve a conductance-allocation optimization or prescribe optimal prices. An unknown published theorem about biharmonic vertex centrality may imply the present claim; that residual priority risk is acknowledged. Independent mathematical validation has not been performed.

## References
1. W. Sun, Q. Ding, J. Zhang and F. Chen, “Coherence in a family of tree networks with an application of Laplacian spectrum,” *Chaos* 24 (2014), 043112, first published online October 20, 2014, DOI: 10.1063/1.4897568. https://doi.org/10.1063/1.4897568 .
2. T. H. Summers, I. Shames, J. Lygeros and F. Dörfler, “Topology Design for Optimal Network Coherence,” preprint first posted November 18, 2014, arXiv:1411.4884. https://arxiv.org/abs/1411.4884 .
3. A. Ghosh, S. Boyd and A. Saberi, “Minimizing Effective Resistance of a Graph,” *SIAM Review* 50 (2008), 37–66, DOI: 10.1137/050645452. https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf .
4. Z. Zhang, W. Xu, Y. Yi and Z. Zhang, “Fast Approximation of Coherence for Second-Order Noisy Consensus Networks,” *IEEE Transactions on Cybernetics* (online 2020; print 2022), DOI: 10.1109/TCYB.2020.2965586. Only the publicly accessible abstract was examined for the cited comparison.
