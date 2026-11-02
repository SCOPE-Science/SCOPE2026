# Collective negative-type thresholds for complete multipartite metric graphs

## Finding
Let \(r\ge 2\) and let \(G=K_{n_1,\ldots,n_r}\) be a complete multipartite graph, with integers \(n_i\ge 1\), total order \(N=\sum_i n_i\), and the unit-edge shortest-path metric \(d\). Set \(a_i=1-1/n_i\), \(H=\{u\in\mathbb R^r:\sum_i u_i=0\}\), and
\[
\Lambda=\max_{u\in H\setminus\{0\}}\frac{\sum_{i=1}^r a_i u_i^2}{\sum_{i=1}^r u_i^2}.
\]
For every real \(p\ge0\), \(G\) has \(p\)-negative type (equivalently, \((V(G),d^{p/2})\) embeds isometrically into real Hilbert space) exactly when \(2^p\Lambda\le1\). Thus its maximal generalized-roundness exponent is \(\wp(G)=\log_2(1/\Lambda)\) when \(\Lambda>0\), and \(\wp(G)=+\infty\) when \(\Lambda=0\) (equivalently, all parts are singletons).

The threshold is explicit from the part sizes. Arrange \(a_1\ge a_2\ge\cdots\ge a_r\). If \(a_1=a_2\), then \(\Lambda=a_1\). If \(a_1>a_2\), then \(\Lambda\) is the unique number in \((a_2,a_1)\) satisfying
\[
\sum_{i=1}^r\frac1{a_i-\Lambda}=0.
\]
For \(\Lambda>0\), the metric has strict \(p\)-negative type for all \(p<\wp(G)\) and non-strict negative type at \(p=\wp(G)\). The space \((V(G),d^{p/2})\) requires affine Hilbert dimension \(N-1\) for \(p<\wp(G)\), and at the finite threshold it requires dimension \(N-1-\kappa\), where \(\kappa=1\) if \(a_1>a_2\), and \(\kappa=k-1\) if \(a_1\) has multiplicity \(k\ge2\).

**Collective obstruction.** For every integer \(m>2\) and \(r\ge3\), the graph with part sizes \((m,2,\ldots,2)\), containing \(r-1\) parts of size two, has
\[
\wp(G)=\log_2\!\frac{r}{(r-1)(1-1/m)+1/2}
<\log_2\!\frac{2}{3/2-1/m}.
\]
The right-hand side is the smallest supremal exponent of all the induced two-part subgraphs. Consequently, for every exponent in this nonempty open interval, **every two-part induced subgraph has \(p\)-negative type but the full graph does not**. At \(m=r=4\), this holds for the exact exponent \(p=\log_2(3/2)\). In fact, for \(K_{4,2,2,2}\), giving each vertex of the size-four part coefficient \(3/4\) and each of the other six vertices coefficient \(-1/2\) yields a zero-sum vector \(\alpha\) with
\[
\sum_{x,y\in V(G)}\alpha_x\alpha_y d(x,y)^p=3/8>0,
\]
although each two-part subgraph has strict \(p\)-negative type.

## Assumptions and scope
All graphs are finite, simple and unweighted, and \(r\ge2\) ensures the cross-part distance is one. Within a part, distinct vertices have distance two; singletons have no within-part pairs. The notion of \(p\)-negative type means
\[
\sum_{x,y\in V(G)}\alpha_x\alpha_y d(x,y)^p\le0
\quad\text{whenever }\sum_x\alpha_x=0.
\]
At \(p=0\), the off-diagonal distances are conventionally raised to the zeroth power while the diagonal remains zero. Statements about Hilbert dimensions mean the smallest dimension of a real affine Euclidean space containing an isometric image of \((V(G),d^{p/2})\). No assertion about Hilbert embeddability is made beyond the threshold.

## Proof
For any zero-sum coefficient vector \(\alpha\), let \(u_i=\sum_{x\in V_i}\alpha_x\), where \(V_i\) is part \(i\), and decompose \(\alpha_x=u_i/n_i+v_x\) on \(V_i\), with \(\sum_{x\in V_i}v_x=0\). Then \(u\in H\). Writing \(t=2^p\) and separating intra-part and inter-part pairs, exact algebra gives
\[
\begin{aligned}
\sum_{x,y}\alpha_x\alpha_y d(x,y)^p
&=t\sum_i\left(u_i^2-\sum_{x\in V_i}\alpha_x^2\right)+\sum_{i\ne j}u_i u_j\\
&=t\sum_i a_i u_i^2-\sum_i u_i^2-t\sum_{i}\sum_{x\in V_i}v_x^2.
\end{aligned}
\]
The supremum of this expression over zero-sum \(\alpha\) is nonpositive if and only if \(t\sum_i a_i u_i^2\le\sum_i u_i^2\) for every \(u\in H\); for the reverse implication, take each \(\alpha_x=u_i/n_i\) to make all residuals vanish. This proves the threshold and the strictness assertion. For the all-singleton graph, all \(a_i=0\), and strictness holds for all finite \(p\).

For the closed threshold description, let \(P\) be orthogonal projection in \(\mathbb R^r\) onto \(H\). Then \(\Lambda\) is the largest eigenvalue of the restriction of \(P\operatorname{diag}(a_i)P\) to \(H\). If two or more \(a_i\) equal the maximum, a difference vector supported on two corresponding indices attains \(a_1\), the global upper bound. Its eigenspace has dimension exactly \(k-1\) for multiplicity \(k\). Otherwise, a maximizing vector satisfies \((a_i-\Lambda)u_i=c\) for a nonzero common constant \(c\), so \(u_i=c/(a_i-\Lambda)\) and the zero-sum constraint yields the displayed secular equation. Its left side is strictly increasing on \((a_2,a_1)\), with limits \(-\infty\) and \(+\infty\), proving uniqueness. The top eigenvalue is then simple.

Schoenberg's finite-distance Gram construction is \(B=-\tfrac12 JD_pJ\), with \(J=I_N-N^{-1}\mathbf1\mathbf1^{\mathsf T}\) and \((D_p)_{xy}=d(x,y)^p\). On the zero-sum space, its nullity is exactly the nullity of the negative-type quadratic form. At subcritical exponents the quadratic form is negative definite, so \(\operatorname{rank}B=N-1\). At the finite threshold its kernel consists precisely of block-constant vectors corresponding to the top eigenspace in \(H\), so \(\operatorname{rank}B=N-1-\kappa\). The rank of this positive semidefinite Gram matrix is the least possible affine Hilbert dimension.

For the collective example, put \(a=1-1/m>1/2\). The compressed diagonal form on \(H\) has eigenvalue \(1/2\) with multiplicity \(r-2\) on differences among the size-two parts and one more eigenvalue \(\Lambda=((r-1)a+1/2)/r\), attained by the vector \((r-1,-1,\ldots,-1)\). The latter is strictly greater than \(1/2\), and therefore determines the full threshold. For a two-part induced subgraph involving the large part, the corresponding top eigenvalue is \((a+1/2)/2\); for any two size-two parts it is \(1/2\). Their maximum is strictly smaller than \(\Lambda\), since
\[
\Lambda-\frac{a+1/2}{2}=\frac{(r-2)(a-1/2)}{2r}>0.
\]
At \(m=r=4\), the two critical values of \(t\) are respectively \(16/11\) and \(8/5\). The choice \(t=3/2\) lies strictly between them. The displayed explicit coefficients have part sums \((3,-1,-1,-1)\), zero within-part residuals, and the quadratic form equals \((3/2)(33/4)-12=3/8\). Every induced two-part graph, on the other hand, has top eigenvalue at most \(5/8\) and hence strict negative type because \((3/2)(5/8)=15/16<1\).

## Verification
A standalone exact-rational checker is supplied as `checker.py`. It expands the full pairwise quadratic form and verifies the block-sum identity on a fixed collection of nontrivial part profiles and deterministic pseudorandom rational zero-sum vectors. It also verifies the critical witness for \(K_{4,2,2,2}\), the two threshold ratios, and the strict induced-two-part inequalities without floating-point error. The infinite-dimensional quantifiers, the spectral maximum, and the Hilbert-rank conclusion are established by the proof above, not by finite testing.

## Relationship to prior work
Sánchez's 2011 finite-metric criterion expresses supremal negative type through general distance-matrix determinants and explicitly evaluates bipartite graphs. Obata's 2022 theorem determines the quadratic-embedding constant and the complete multipartite classification at the fixed exponent \(p=1\), by a related adjacency secular equation; that fixed-exponent classification is **known**, not claimed here. Robertson's 2023 work derives the bipartite Hilbert-distortion threshold and optimal embeddings. The block matrices of Das and Mohanty's 2020 and 2023 studies concern squared-distance spectra and inverses for complete multipartite graphs at the fixed exponent two. The present statement evaluates the **entire real exponent threshold** in terms of a small part-size spectral problem, describes the exact loss of affine Hilbert dimension, and demonstrates a strict collective obstruction invisible on every two-part induced subgraph. The cited general finite-metric algorithms and Obata's compression technique may be specialized or adapted to these objects; they are not claimed to be new here. The distinguishing assertions are the all-exponent sharp family law, critical embedding dimension, and explicit subcritical collective obstruction.

## Limitations
The theorem does not determine optimal Hilbert distortion above the threshold, nor does it address weighted, directed, or non-complete multipartite graphs. The exact root may be algebraic rather than expressible by elementary radicals for many distinct part sizes. A universal priority claim is not made: equivalent explicit multipartite negative-type thresholds or the collective-obstruction example might appear under distance-matrix, Euclidean-distance-matrix, or generalized-roundness terminology outside the checked literature. The fixed-exponent \(p=1\) case is already characterized by Obata; the present claim does not include priority for that special case.

## References
- Nobuaki Obata, *Complete Multipartite Graphs of Non-QE Class*, arXiv:2206.05848v1, first submitted 2022-06-12, Sections 1 and 3–4. https://arxiv.org/abs/2206.05848
- Gavin Robertson, *Negative Type and Bi-lipschitz Embeddings Into Hilbert Space*, arXiv:2309.16070v1, publicly submitted 2023-09-27, especially Section 4.1. https://arxiv.org/html/2309.16070v1
- Stephen Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1, publicly submitted 2011-08-02, Sections 2–3. https://arxiv.org/html/1108.0451v1
- Joyentanuj Das and Sumit Mohanty, *On Squared Distance Matrix of Complete Multipartite Graphs*, arXiv:2012.04341, first submitted 2020-12-08. https://arxiv.org/abs/2012.04341
- Joyentanuj Das and Sumit Mohanty, *Inverse of the Squared Distance Matrix of a Complete Multipartite Graph*, arXiv:2311.01069v1, first submitted 2023-11-02, Sections 1–4. https://arxiv.org/abs/2311.01069
