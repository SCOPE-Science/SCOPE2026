# Exact minimal cut and cycle projections on pair-Kneser graphs

## Finding
For every integer \(n\ge5\), let \(G_n=KG(n,2)\) have as vertices the two-element subsets of \([n]\), with two vertices adjacent exactly when they are disjoint. Give the unoriented edges one fixed orientation each, and let \(B_n\) and \(Z_n\) be the real cut and cycle spaces inside the edge coordinate space \(\mathbb R^{E(G_n)}\). Then the Euclidean orthogonal projections \(Q_n\) onto \(B_n\) and \(P_n=I-Q_n\) onto \(Z_n\) are norm-minimal among **all real linear projections onto their respective spaces** in \(\ell_p(E(G_n))\), for each \(1\le p\le\infty\).

At both endpoint exponents the exact minimum norms are
\[
\begin{aligned}
\lambda_1(B_n)&=\lambda_\infty(B_n)=\frac{2(n-3)(n+6)}{n(n-1)},\\
\lambda_1(Z_n)&=\lambda_\infty(Z_n)=1+\frac{2(n-3)(n+6)}{n(n-1)}-\frac{8(n+1)}{n(n-1)(n-3)}.
\end{aligned}
\]
Here \(\lambda_p(Y)=\inf\{\|T\|_{\ell_p(E)\to\ell_p(E)}:T^2=T,\operatorname{ran}T=Y\}\); this is a relative projection constant in the *specified edge space*.

The cut constant increases up to \(n=8\), equals \(5/2\) at both \(n=8,9\), and strictly decreases thereafter. The cycle constant has its unique integer maximum \(1000/297\) at \(n=12\). As \(n\to\infty\), the respective constants tend to \(2\) and \(3\). The Petersen graph \(KG(5,2)\) gives the concrete values \(11/5\) and \(2\).

## Assumptions and scope
All scalar spaces, projections, and functionals are **real**. For an arbitrary choice of reference orientation let \(D:\mathbb R^{E}\to\mathbb R^V\) be the incidence map, with column \(\mathbf 1_A-\mathbf 1_B\) for an oriented edge from \(A\) to \(B\). Thus \(B_n=\operatorname{ran}D^{\mathsf T}\), \(Z_n=\ker D\), and the graph Laplacian is \(L=DD^{\mathsf T}\). The vertex graph is connected for \(n\ge5\): two intersecting two-subsets have a common disjoint neighbor. Changing orientations only conjugates all edge operators by a signed coordinate permutation and does not affect any of the assertions.

For the endpoint formulas, the projection norms mean the induced operator norms in real \(\ell_1^E\) and \(\ell_\infty^E\). For intermediate exponents only the **minimality** of these projections, not the numerical value of their norms, is asserted. No assertion concerns absolute projection constants into unrelated superspaces or Kneser graphs \(KG(n,k)\) with \(k>2\).

## Proof
**1. A universal Poisson column.** Fix an oriented graph edge \(e=(A,B)\), where \(A,B\subset[n]\) are disjoint two-subsets. Write \(R=[n]\setminus(A\cup B)\), \(r=n-4\ge1\), and \(d=\binom{n-2}{2}\), the graph degree. Partition the vertex set into the singleton classes \(\{A\}\), \(\{B\}\), the \(2r\) vertices \(U\) meeting \(A\) and \(R\) once each, the \(2r\) vertices \(V\) meeting \(B\) and \(R\) once each, the four cross-pairs meeting \(A\) and \(B\), and the \(\binom r2\) pairs inside \(R\).

Put
\[
 t=\frac{2(n+1)}{n(n-1)(n-3)},\qquad
 u=\frac{4}{(n-4)(n-3)(n-1)n}.
\]
Define the mean-zero potential \(h_e\) to take the values \(t,-t,-u,u,0,0\) on the six classes in that order. At \(A\), direct neighbor counting gives
\[
 (Lh_e)(A)=(d+1)t-2ru=1.
\]
At any vertex of \(U\), the corresponding identity is
\[
 (Lh_e)(U)=t-(d+r-1)u=0.
\]
By swapping \(A\) and \(B\), the values at \(B\) and \(V\) are \(-1\) and \(0\); the remaining classes are fixed by a sign-reversing swap, so their Laplacian values are zero. Both displayed identities follow on substitution from \(d=(r+1)(r+2)/2\). Consequently \(Lh_e=\mathbf1_A-\mathbf1_B\). As \(h_e\) has mean zero and \(L\) is invertible on mean-zero vertex vectors, \(h_e=L^+(\mathbf1_A-\mathbf1_B)\), where \(L^+\) denotes the Moore–Penrose inverse. Therefore the Euclidean orthogonal cut projection is \(Q_n=D^{\mathsf T}L^+D\), whose column at \(e\) is \(D^{\mathsf T}h_e\); the cycle projection is \(P_n=I-Q_n\).

**2. Uniqueness of invariant projections.** The symmetric group \(S_n\) acts on vertices by permuting \([n]\) and on the oriented edge-coordinate space by signed coordinate permutations. Both \(B_n\) and \(Z_n\) are invariant. Suppose that \(Q\) is an \(S_n\)-equivariant projection onto \(B_n\). The isomorphism from mean-zero vertex vectors to \(B_n\) induced by \(D^{\mathsf T}\) factors it uniquely as \(Q=D^{\mathsf T}H\), where \(H\) has mean-zero columns and is equivariant. The stabilizer of \(e\) acts transitively on each of the six classes above; swapping the endpoint two-subsets reverses the signed edge coordinate. Hence \(H\mathbf1_e\) necessarily has the six class values \(\alpha,-\alpha,\beta,-\beta,0,0\), in that order. This is the *entire* space of equivariant column possibilities, including the boundary case \(r=1\).

Because \(Q\) fixes the cut space pointwise, \(HD^{\mathsf T}=I-\mathbf1\mathbf1^{\mathsf T}/v\), where \(v=\binom n2\), on the vertex space. The three possible matrix entries of \(HD^{\mathsf T}\), according as its row vertex equals, meets in one point, or is disjoint from its column vertex, are respectively
\[
 d\alpha,\qquad c\beta,\qquad -\alpha-2r\beta,
 \quad c=\binom{n-3}{2}>0.
\]
In particular \(c\beta=-1/v\) and \(-\alpha-2r\beta=-1/v\) determine \(\alpha,\beta\) uniquely. Since \(Q_n\) itself is invariant, every invariant projection onto \(B_n\) equals \(Q_n\).

For completeness, consider a hypothetical nonzero invariant projection correction \(T:B_n\to Z_n\). As the group action is orthogonal, the adjoint \(T^{\mathsf T}:Z_n\to B_n\) is another nonzero intertwining map. Extending it by zero on \(B_n\), the operator \(Q_n+T^{\mathsf T}P_n\) would be a *different* invariant projection onto \(B_n\), a contradiction. Thus the invariant projection onto \(Z_n\) is also unique, namely \(P_n\). Averaging an arbitrary projection onto either target over the finite group \(S_n\) does not increase its operator norm on any \(\ell_p(E)\), because the group acts by signed coordinate isometries. The averaged projection is invariant and therefore orthogonal. This proves simultaneous global norm minimality for all \(1\le p\le\infty\).

**3. Exact endpoint column sums.** The potential values are \(t,-t,-u,u,0,0\), with \(t>u>0\). In the fixed column of \(Q_n\), the graph-edge types with nonzero difference contribute to the absolute column sum as follows: an \(A\)-to-\(B\) edge contributes \(2t\); the \(4r\) edges of types \(A\)-to-\(V\) and \(B\)-to-\(U\) contribute \(t-u\) each; the \(2\binom r2\) edges of types \(A\)-to-\(W\) and \(B\)-to-\(W\) contribute \(t\) each; the \(8r\) cross-pair-to-\(U/V\) edges contribute \(u\) each; the \(4r(r-1)\) edges of type \(U\)-to-\(V\) contribute \(2u\) each; and the \(4r\binom{r-1}{2}\) edges of types \(U/V\)-to-\(W\) contribute \(u\) each. Here \(W\) denotes pairs inside \(R\); a binomial count vanishes when its lower index exceeds its upper index. All omitted types have zero difference.

The sum simplifies exactly to
\[
\|Q_n\mathbf1_e\|_1=(r+1)(r+2)t+2r^2(r+1)u
=\frac{2(n-3)(n+6)}{n(n-1)}.
\]
The diagonal entry of \(Q_n\) in column \(e\) is \(2t<1\), and that of \(P_n\) is \(1-2t\). All off-diagonal entries of \(P_n\) are negatives of those of \(Q_n\), whence
\[
\|P_n\mathbf1_e\|_1=1+\|Q_n\mathbf1_e\|_1-4t.
\]
Transitivity of \(S_n\) on graph edges makes these column sums independent of \(e\). Because both orthogonal projections are self-adjoint, the maximum row sums equal the maximum column sums. Thus the two endpoint norms are exactly the displayed constants, which are already globally minimal by Step 2.

**4. Sharp integer maxima.** Write \(b_n=\|Q_n\|_1\), \(z_n=\|P_n\|_1\). Direct subtraction of the rational formulas yields
\[
 b_{n+1}-b_n=-\frac{8(n-8)}{n(n-1)(n+1)},\quad
 z_{n+1}-z_n=-\frac{8(n^3-15n^2+44n-40)}{n(n-3)(n-2)(n-1)(n+1)}.
\]
The cubic in the latter numerator is negative at every integer \(5\le n\le11\) and positive at every integer \(n\ge12\): its derivative is negative between its two real critical points (one below \(2\), the other between \(8\) and \(9\)) and positive from \(9\) onward; direct endpoint evaluations handle the short initial segment. This gives the asserted maxima and the limits follow immediately from the formulas.

## Verification
The accompanying `check.py` uses only exact integer and rational arithmetic in the Python standard library. Executing `python3 check.py` constructs the Kneser graph and, for every oriented edge separately, verifies the exact Poisson equation, all stated cut/cycle endpoint column sums, and elementary graph parameters for each \(n=5,6,7,8,9,10\). Its 652346 deterministic assertions all passed. The checker also evaluates the two maximizing cut cases and the maximizing cycle case exactly. These finite tests check the formulas and catch counting/sign errors; they are **not** an exhaustive proof over all \(n\). The group argument and symbolic counting in Steps 1–4 provide the infinite-family proof.

## Relationship to prior work
Dilworth, Kutzarova, and Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost* (first arXiv version, 2023), establish general invariant-projection techniques and work explicitly with discrete tori and Hamming graphs. In particular their general representation criterion for uniqueness is consistent with Step 2, but their inspected paper does not give this pair-Kneser evaluation. Their earlier *Lipschitz free spaces on finite metric spaces* (2018) and *Analysis on Laakso graphs with application to the structure of transportation cost spaces* (2020) treat different graph families and more general transportation geometry. The Kneser graphs are complements of triangular Johnson graphs on the same vertex sets, but complementing the graph changes the edge coordinate space and neither family's cut/cycle projection constants follow from those of the other by a linear-complement argument. No uniqueness claim about the broader mathematical literature is made.

## Limitations
The claimed minima are relative to the standard real \(\ell_p\) **edge-coordinate ambient space**. No intermediate-exponent numerical formulas, no complex-scalar assertion, and no extension to higher-order Kneser graphs are established. The work is analytically proved and computationally checked on a finite sample, but independently verified scientific originality in all published or unindexed sources is not guaranteed; specifically an equivalent expression via generalized Johnson association schemes or electrical transfer-current tables is a residual literature risk. Independent third-party audit has not been performed.

## References
1. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582v1, posted 2023-05-21, especially Section 1.4 and Section 2. [https://arxiv.org/abs/2305.12582](https://arxiv.org/abs/2305.12582).
2. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814v1, posted 2018-07-10. [https://arxiv.org/abs/1807.03814](https://arxiv.org/abs/1807.03814).
3. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Analysis on Laakso graphs with application to the structure of transportation cost spaces*, arXiv:2007.07949, first posted 2020-07-15. [https://arxiv.org/abs/2007.07949](https://arxiv.org/abs/2007.07949).
