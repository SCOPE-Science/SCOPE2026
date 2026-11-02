# Seven-vertex obstruction and sharp negative-type gap of complete split graph metrics

## Finding
For integers \(m\ge1\), \(n\ge2\), let \(G_{m,n}=K_m\vee\overline{K_n}\) be the join of an \(m\)-vertex clique and an \(n\)-vertex independent set, equipped with its unit-edge shortest-path metric \(d\). Its supremal negative-type exponent (maximal generalized roundness) is
\[
\wp(G_{m,n})=\log_2\!\left(\frac{n(m+1)}{m(n-1)}\right).
\]
For \(p\ge0\), let \(D_p=(d(v,w)^p)_{v,w}\) with diagonal entries zero, and let \(H=\{z\in\mathbb R^{m+n}:\sum_v z_v=0\}\). The *exact*, attained normalized negative-type gap for every \(p\ge0\) is
\[
\inf_{z\in H\setminus\{0\}}\frac{-z^{\mathsf T}D_pz}{\lVert z\rVert_2^2}=
\frac{1+1/m-2^p(1-1/n)}{1/m+1/n}.
\]
Thus strict negative type holds below \(\wp\), endpoint negative type is non-strict with precisely one null direction, and negative type fails above \(\wp\). In particular, \(G_{m,n}\) has \(1\)-negative type if and only if \(n(m-1)\le2m\). All such graphs with at most six vertices have \(1\)-negative type. At seven vertices the *only* failing parameter pairs are \((m,n)=(2,5),(3,4),(4,3)\).

The least Euclidean dimension in which the snowflaked metric \(d^{p/2}\) embeds is \(m+n-1\) for \(0\le p<\wp\) and \(m+n-2\) at \(p=\wp\). These statements concern isometric finite point embeddings, not graph drawings or low-distortion embeddings.

## Assumptions and scope
The graph is simple, finite, connected, with exactly \(m\ge1\) mutually adjacent clique vertices and \(n\ge2\) mutually nonadjacent vertices each connected to every clique vertex. Distances between distinct clique vertices and between the parts are \(1\); distances between distinct independent vertices are \(2\). The exponent \(p\) is real and nonnegative; the convention at \(p=0\) is \(d(v,w)^0=1\) for distinct vertices and zero on the diagonal. Negative type means \(z^{\mathsf T}D_pz\le0\) for every real zero-sum coefficient vector \(z\).

## Proof
Fix \(m,n,p\), put \(q=2^p\ge1\), and write \(z=(a_1,\ldots,a_m,b_1,\ldots,b_n)\in H\), \(A=\sum_i a_i\), \(B=\sum_j b_j=-A\). Expanding all ordered pairs gives the *exact identity*
\[
\begin{aligned}
 z^{\mathsf T}D_pz
 &=\left(A^2-\sum_i a_i^2\right)
 +q\left(B^2-\sum_j b_j^2\right)+2AB\\
 &=(q-1)A^2-\sum_i a_i^2-q\sum_j b_j^2.
\end{aligned}
\]
Cauchy--Schwarz yields \(\sum_i a_i^2\ge A^2/m\) and \(\sum_j b_j^2\ge A^2/n\), with simultaneous equality precisely when all \(a_i=A/m\) and all \(b_j=-A/n\). Consequently,
\[
 z^{\mathsf T}D_pz\le\left[q\left(1-\frac1n\right)-1-\frac1m\right]A^2.
\]
If the bracket is negative then every nonzero \(z\in H\) has a strictly negative quadratic value (including \(A=0\), by the exact identity). If the bracket is zero, the equality space is exactly the one-dimensional span of the block-constant vector
\[
 b_*=(\underbrace{1/m,\ldots,1/m}_{m},\underbrace{-1/n,\ldots,-1/n}_{n}).
\]
If the bracket is positive, \(b_*\) is a strict positive-quadratic witness. Since the bracket is strictly increasing in \(q\), the unique endpoint is \(q_*=n(m+1)/[m(n-1)]>1\), giving the claimed critical exponent and endpoint nullity.

For the gap formula, decompose \(H\) orthogonally into clique-internal zero-sum vectors (dimension \(m-1\)), independent-set-internal zero-sum vectors (dimension \(n-1\)), and the line through \(b_*\). On the first two subspaces the compressed quadratic form has eigenvalues \(-1\) and \(-q\), respectively. On the third it has eigenvalue
\[
 \lambda_*=\frac{q(1-1/n)-1-1/m}{1/m+1/n},
\]
because \(b_*^{\mathsf T}D_pb_*=q(1-1/n)-1-1/m\) and \(\lVert b_*\rVert_2^2=1/m+1/n\). These spaces are mutually orthogonal and cross terms vanish, so the smallest eigenvalue of \(-D_p\) restricted to \(H\) is \(\min\{1,q,-\lambda_*\}\). For \(q\ge1\), \(-\lambda_*\le1\le q\). This proves the exact gap for all \(p\ge0\), even when it is negative. It is attained by \(b_*\).

At \(p=1\), \(q=2\), so nonnegative type is equivalent to \(2(1-1/n)\le1+1/m\), or \(n(m-1)\le2m\). For total vertex count at most six, this inequality holds for every admissible integer pair. At total count seven, direct integer rearrangement identifies precisely \((2,5),(3,4),(4,3)\) as failures.

Finally Schoenberg's finite-distance criterion identifies the Gram matrix of any Euclidean embedding of \(d^{p/2}\) with \(-\frac12P D_pP\) on \(H\), where \(P\) projects orthogonally onto \(H\). Its rank is \(m+n-1\) below the endpoint and \(m+n-2\) at the endpoint, by the just-proved eigenspace decomposition. Gram rank equals the minimal affine dimension of an isometric Euclidean realization.

## Verification
Run `python3 verify_split_graph.py` using Python 3 with no external dependencies. The checker constructs the graph distance-power matrix and uses exact rational arithmetic to test its three invariant subspaces, the quadratic identity and Cauchy bound on independently chosen zero-sum vectors, the one-dimensional critical witnesses, and the complete small-order integer classification. The recorded run passed 4,788 exact-action checks, 6,048 zero-sum-vector checks, and 504 critical-witness checks. These finite tests provide reproducibility and error detection, not an exhaustive proof of the infinite integer and real-exponent statements.

## Relationship to prior work
Sanchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451v1 (2 August 2011), establishes the general finite-distance criterion and evaluates complete bipartite graph metrics. Its complete-bipartite model has two independent vertex classes; the present split graph has one independent class and one clique, with a different quadratic form. The general finite-distance test is a framework for the present calculation, not an explicit all-parameter split-graph gap or seven-vertex classification. Deza and Maehara, *Metric Transforms and Euclidean Embeddings* (1990), develop older two-distance embedding methods and may give a route to related facts; an accessible full-text comparison of its specific examples was not possible. The explicit split-graph formula, the sharp normalized spectral gap, and the seven-vertex failure classification are the scope of this finding.

## Limitations
No claim is made for arbitrary split graphs, weighted edges, different metrics, infinite graphs, or nonisometric approximations. The seven-vertex minimality assertion is *within the complete split-graph family*, not among all graph metrics. General two-distance matrix criteria predate this calculation; a hidden equivalent specialization in older embedding literature remains an originality risk. Independent scientific validation has not been performed.

## References
1. Stephen Sanchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451v1 (2011-08-02), https://arxiv.org/abs/1108.0451.
2. M. Deza and H. Maehara, *Metric Transforms and Euclidean Embeddings*, *Transactions of the American Mathematical Society* **317** (1990), 661–671, DOI:10.1090/S0002-9947-1990-0974513-6.
3. I. J. Schoenberg, *Metric spaces and positive definite functions*, *Transactions of the American Mathematical Society* **44** (1938), 522–536.
