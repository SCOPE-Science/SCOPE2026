# A balanced–unbalanced transition in the Hilbert snowflakes of fully subdivided bicliques

## Finding

Let \(m,n\ge2\) be integers. Replace **every** edge of the complete bipartite graph \(K_{m,n}\) by a path of two unit edges, using a different new midpoint for every original edge. Write \(S_{m,n}\) for the resulting graph, \(d\) for its shortest-path metric on **all** \(N=mn+m+n\) vertices, and \(\wp(S_{m,n})\) for the supremum of all \(p\ge0\) such that
\[
\sum_{x,y\in S_{m,n}}\xi_x\xi_y d(x,y)^p\le0
\quad\text{whenever }\sum_x\xi_x=0.
\]
For \(p>0\), introduce
\[
 a=4^p,\quad b=2^p,\quad c=3^p,\qquad
 \sigma=\frac1m+\frac1n,\quad\tau=\frac1{mn},\quad\delta=\frac1m-\frac1n,
\]
\[
 K(p)=\frac{a(2-\sigma)-2b}{4},\qquad
 J(p)=\delta\left(\frac a2+1-c\right),
\]
\[
 R(p)=a\left(\frac{6-5\sigma}{4}+\tau\right)
 +b\left(\frac12+\sigma-2\tau\right)-2c-(1-c)\sigma,
 \qquad H(p)=\begin{pmatrix}K(p)&J(p)/2\\J(p)/2&R(p)\end{pmatrix},
\]
and \(p_K=\log_2\!\bigl(2/(2-\sigma)\bigr)\), the known sharp exponent of \(K_{m,n}\).

**Exact classification.** If \(m=n=r\ge3\), then
\[
\boxed{\wp(S_{r,r})=\log_2\frac r{r-1}=\wp(K_{r,r}).}
\]
If \(m\ne n\), there is exactly one \(p_{m,n}\in(0,p_K)\) satisfying
\[
\boxed{\bigl[a(2-\sigma)-2b\bigr]R(p)
=\delta^2\bigl(a/2+1-c\bigr)^2,\qquad \wp(S_{m,n})=p_{m,n}.}
\]
Thus full edge subdivision preserves the sharp exponent **exactly** in the balanced bicliques but strictly reduces it for every unequal pair of part sizes. The boundary \((m,n)=(2,2)\) is the eight-cycle: its exponent is one.

For \((m,n)\ne(2,2)\), the metric has strict \(p\)-negative type for \(0\le p<\wp(S_{m,n})\), nonstrict \(p\)-negative type at the endpoint with exactly one independent zero-sum equality direction, and fails \(p\)-negative type for every larger exponent. The minimum affine dimension of an isometric Euclidean embedding of \(d^{p/2}\) is \(N-1\) below the positive endpoint and \(N-2\) at the endpoint. In the eight-cycle exception, the endpoint equality space is three-dimensional and the endpoint affine embedding dimension is four.

For any fixed \(m\ge2\), as \(n\to\infty\),
\[
\boxed{p_{m,n}=\frac{1+1/m}{(4-1/m)\log 2-2\log 3}\,\frac1n+O_m(n^{-2}).}
\]
In particular, for a fixed smaller part, the subdivided exponent tends to zero, whereas the unsubdivided biclique exponent tends to the **positive** constant \(\log_2(2/(2-1/m))\).

## Assumptions and scope

All edges are unweighted, every original edge is subdivided exactly once, and the new midpoint vertices **are included** in the metric. No graph with multiple edges, arbitrary partial subdivision, or arbitrary edge weights is claimed. In the exceptional eight-cycle case, \(S_{2,2}\cong C_8\) and the endpoint is a known even-cycle phenomenon, not a novel subcase.

For a finite metric \((X,d)\) with at least two points, \(p\)-negative type is equivalent to conditional negative semidefiniteness of the powered-distance matrix. By the classical Schoenberg criterion, it is equivalent to a Hilbert-space isometric realization of \(d^{p/2}\). The dimension follows from the rank of \(-\tfrac12 P D_p P\), where \(P=I-|X|^{-1}\mathbf1\mathbf1^{\mathsf T}\).

## Proof

**1. All pairwise distances.** Denote the original part vertices by \(A_i\) for \(1\le i\le m\) and \(B_j\) for \(1\le j\le n\), and the new edge midpoint by \(E_{ij}\). Distinct vertices inside either original part are distance four, and \(d(A_i,B_j)=2\). One has \(d(A_i,E_{k\ell})=1\) for \(i=k\), otherwise three, and symmetrically \(d(B_j,E_{k\ell})=1\) for \(j=\ell\), otherwise three. Distinct midpoint vertices are distance two when they share an index and distance four otherwise. These statements follow directly by alternating the two incidence types in the subdivided graph; independent breadth-first search verifies them for the sampled instances in the accompanying program.

**2. Exhaustive invariant decomposition.** The permutation action of \(S_m\times S_n\) decomposes the real coefficient space into the following mutually orthogonal sectors, and their zero-total subspace has the indicated dimensions: paired \(A\)-contrasts with midpoint row-contrasts (dimension \(2(m-1)\)); paired \(B\)-contrasts with midpoint column-contrasts (dimension \(2(n-1)\)); doubly centered midpoint contrasts (dimension \((m-1)(n-1)\)); and vectors constant on the three vertex types and having zero total sum (dimension two). The dimensions add to \(mn+m+n-1\), so no coefficient direction is omitted. Symmetry makes distinct sectors orthogonal for every powered-distance quadratic form.

**3. Strict negativity of the nonconstant sectors.** Let \(0<p<1\). For every zero-sum coefficient vector \(\xi\), the Bernstein formula gives
\[
\xi^{\mathsf T}D_p\xi
=-\frac{p}{\Gamma(1-p)}\int_0^\infty
  \xi^{\mathsf T}[e^{-t d(x,y)}]_{x,y}\xi\,t^{-p-1}\,dt.
\]
Write \(q=e^{-t}\in(0,1)\). On each normalized \(A\)-contrast/row-contrast pair the exponential-distance kernel is
\[
\begin{pmatrix}
1-q^4 &\sqrt n(q-q^3)\\
\sqrt n(q-q^3)&(1-q^2)(1+(n-1)q^2)
\end{pmatrix}.
\]
Its first principal minor is positive and its determinant is exactly
\[
(1-q^2)^2(1+(n-1)q^4)>0.
\]
For the \(B\)-contrast block replace \(n\) with \(m\). The doubly centered midpoint sector has strictly positive exponential-kernel eigenvalue \((1-q^2)^2\). All these sectors are therefore **strictly negative** for the powered distance \(D_p\). At \(p=1\), the row and column blocks are still strictly negative (their determinants are \(4n\) and \(4m\)); the doubly centered midpoint sector becomes zero.

**4. The entire remaining obstruction is a two-by-two form.** Let the total masses on the \(A\), \(B\), and midpoint classes be \(u,v,w\) respectively, with \(u+v+w=0\). Set \(s=u-v\); then \(u=(s-w)/2\) and \(v=(-s-w)/2\). Constant coefficients within each class are respectively \(u/m\), \(v/n\), and \(w/(mn)\). Directly summing all six distance types from Step 1 gives
\[
\xi^{\mathsf T}D_p\xi=K(p)s^2+J(p)sw+R(p)w^2
=\begin{pmatrix}s&w\end{pmatrix}H(p)\begin{pmatrix}s\\w\end{pmatrix}.
\]
Consequently, for \(0<p<1\), \(p\)-negative type holds **if and only if** \(H(p)\) is negative semidefinite. At \(p\downarrow0\), its entries tend to \(K=-\sigma/4\), \(J=\delta/2\), and \(R=-\sigma/4-\tau\), yielding
\[
\det H(0)=\frac{\tau(1+\sigma)}4>0,
\]
so \(H(0)\) is strictly negative definite.

**5. Balanced classes.** For \(m=n=r\), one has \(J\equiv0\) and \(K(p_K)=0\). If \(r\ge3\) then \(0<p_K<1\), and substitution of \(2^{p_K}=r/(r-1)\) gives
\[
R(p_K)=\frac{4^{p_K}+2^{p_K}-2\cdot3^{p_K}}{2^{p_K}}<0,
\]
where the inequality is the strict concavity of \(x\mapsto x^{p_K}\) at the midpoint \(3=(2+4)/2\). Step 3 then gives endpoint negative type with a one-dimensional equality space. For \(p>p_K\), choosing \(w=0\) yields \(K(p)>0\) and failure. Therefore the claimed balanced formula and endpoint nullity hold. For \(r=2\) the graph is \(C_8\); at \(p_K=1\) the global matrix is zero and the doubly centered sector contributes one further equality direction, so the nullity is three. A four-point isometric square inside \(C_8\) prohibits every exponent above one.

**6. Unequal classes.** For \(m\ne n\), the cap \(p_K\) lies strictly below one. The function \(\phi(p)=1+4^p/2-3^p\) is positive for \(0\le p<1\): its derivative is negative on this interval because \((4/3)^p\le4/3<2\log3/\log4\), while \(\phi(1)=0\). Hence \(J(p_K)\ne0\), and since \(K(p_K)=0\),
\[
\det H(p_K)=-J(p_K)^2/4<0.
\]
Continuity and Step 4 imply at least one determinant zero inside \((0,p_K)\). Throughout that open interval, \(K(p)<0\). Thus at any determinant zero the global form is negative semidefinite with **exactly one** null direction; Step 3 shows the complete distance form is negative semidefinite with exactly one equality direction. To rule out two distinct determinant zeros, use the strict-interior property: if a finite metric has \(q\)-negative type for some \(q>0\), it has strict \(p\)-negative type for every \(0\le p<q\). A direct proof integrates the positive-semidefinite matrices \(e^{-tD_q}\), which converge to the identity as \(t\to\infty\). Two distinct determinant zeros would contradict strictness at the smaller exponent. Thus the root is unique and is the supremal exponent. At the root, a null vector in global coordinates is \((s,w)=(-J/(2K),1)\), giving a concrete equality vector via the formulas in Step 4.

**7. Dimension and fixed-part asymptotics.** Strict negative type means the centered Euclidean Gram matrix has full rank \(N-1\); a single critical equality direction lowers it to \(N-2\). For fixed \(m\), write \(q=1/m\), \(h=1/n\), and \(F(p,h)=\det H(p)\). Direct differentiation of the exact entries at \((p,h)=(0,0)\) yields
\[
F(0,0)=0,\quad
\partial_hF(0,0)=\frac{q(1+q)}4,
\qquad
\partial_pF(0,0)=-\frac q4[(4-q)\log2-2\log3].
\]
The bracket is strictly positive for \(0<q\le1/2\). The analytic implicit-function theorem produces the positive root
\[
p=\frac{1+q}{(4-q)\log2-2\log3}\,h+O(h^2).
\]
For small positive \(h\), this root lies below \(p_K\) and hence equals the unique exponent from Step 6. This proves the asymptotic claim.

## Verification

The accompanying `check_incidence.py` is a standalone numerical cross-check requiring Python 3, NumPy and SciPy. Run it as `python check_incidence.py`. It rebuilds every graph from its incidence adjacency lists, computes all-pairs distances by independent breadth-first search, checks the distance-case formula, compares the complete centered powered-distance spectra with the derived thresholds and equality vectors, checks the eight-cycle exception, and tests the fixed-part asymptotic. In the completed replay it printed `CHECK_OK 86 assertion groups`. All quantifiers over infinitely many part sizes and all real exponents are proved in Steps 1–7; the finite checker does not certify them.

Illustrative thresholds: \((m,n)=(2,3)\) gives \(0.771279384452\); \((2,4)\) gives \(0.652288422426\); \((3,4)\) gives \(0.490455881212\). The balanced cases \((3,3)\), \((4,4)\) give \(0.584962500721\), \(0.415037499279\), respectively. The upper bound from the unmodified \(K_{m,n}\) is strictly larger in each unequal case.

## Relationship to prior work

Sánchez (arXiv:1108.0451, 2011) proved the general finite-metric criterion and the explicit supremal exponent for the **unsubdivided** complete bipartite graph. The latter provides the comparison \(p_K\), not the powered-distance spectrum of the added midpoint vertices. Lou–Obata–Huang (arXiv:2001.06752, first posted 2020-01-19) treat quadratic embedding constants for joins, double graphs, and related graph products; their formulas concern the \(p=1\) invariant and different constructions. Młotkowski–Skrzypczyk–Wojtylak (arXiv:2409.17662, first posted 2024-09-26) investigate deletion of disjoint edges from bipartite graphs and three-path theta graphs at the ordinary quadratic-embedding exponent. In particular, **removing** edges from \(K_{m,n}\) is not **subdividing every edge** and retaining the midpoint vertices. Their paper's result-family descriptions and relevant sections do not supply the present two-parameter powered-distance formula or the fixed-part asymptotic. The classical strict-interior and Schoenberg criteria are used as proof ingredients, not claimed as new.

## Limitations

This is an exact classification for the stated finite family, not a result about continuum metric realizations of the graph edges, partial subdivision, or general incidence hypergraphs. The eight-cycle boundary is already known. The formula for unequal parts is an implicit uniquely specified root, not an elementary closed form. Historical priority is qualified: equivalent older work using an incidence-graph or generalized-roundness description could be missed by textual retrieval. Numerical checks cover only finite selected parameters and do not replace the analytic proof. No independent audit has been performed.

## References

1. W. Młotkowski, M. Skrzypczyk, M. Wojtylak, *On quadratic embeddability of bipartite graphs and theta graphs*, arXiv:2409.17662, first public version 2024-09-26. https://arxiv.org/abs/2409.17662
2. Z. Lou, N. Obata, Q. Huang, *Quadratic Embedding Constants of Graph Joins*, arXiv:2001.06752, first public version 2020-01-19. https://arxiv.org/abs/2001.06752
3. S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451, first public version 2011-08-02. https://arxiv.org/abs/1108.0451
4. I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the AMS, 1938; classical Hilbert embedding and exponential-kernel criteria.
5. H. Li and A. Weston, *Strict p-negative type of a metric space*, classical strict-interior theorem; the needed finite-metric implication is also proved in Step 6.
