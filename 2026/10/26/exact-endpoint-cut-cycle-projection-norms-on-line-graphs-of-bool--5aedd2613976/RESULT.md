# Exact endpoint cut–cycle projection norms on line graphs of Boolean cubes

## Finding
For every integer \(n\ge 3\), let \(Q_n\) be the unweighted Boolean cube on \(\{0,1\}^n\), and let \(H_n=L(Q_n)\) be its line graph. Denote by \(C_n\) the Euclidean-orthogonal projection onto the cut space of \(H_n\), and by \(Z_n=I-C_n\) the complementary cycle-space projection, acting on the real edge-coordinate space of \(H_n\). Put
\[
T_n=\frac{n^2+11n-14}{4n}-\frac{2}{n(n-1)}\left(1-\frac{n}{2^{n-1}}\right).
\]
The exact induced endpoint norms, identical for \(\ell_1\) and \(\ell_\infty\), are
\[
\boxed{\|C_n\|_{1\to1}=\|C_n\|_{\infty\to\infty}=T_n},
\]
\[
\boxed{\|Z_n\|_{1\to1}=\|Z_n\|_{\infty\to\infty}=T_n+1-\frac{2}{n-1}\left(1-\frac{1}{n2^{n-1}}\right)}.
\]
Every edge column has the indicated absolute column sum. In particular,
\[
\|C_n\|=\frac n4+\frac{11}{4}-\frac{7}{2n}+O(n^{-2}),\qquad
\|Z_n\|=\frac n4+\frac{15}{4}-\frac{11}{2n}+O(n^{-2}).
\]
The corresponding cut-projection norm of the original cube is \((n+1)/2\) [1]. Thus passing to its line graph halves the leading growth slope with respect to cube dimension, from \(1/2\) to \(1/4\), although the line graph remains connected and highly symmetric.

## Assumptions and scope
Every edge has unit conductance. The line graph has one vertex per cube edge; two such vertices are adjacent precisely when their cube edges meet. Its vertex and edge counts are \(N=n2^{n-1}\) and \(M=N(n-1)\), respectively. Fix an arbitrary orientation of its \(M\) edges and let \(D\) be the signed vertex–edge incidence matrix. The real cut and cycle subspaces of \(\mathbb R^M\) are \(\mathrm{im}(D^\top)\) and \(\ker D\). Accordingly \(C_n=D^\top(DD^\top)^+D\) and \(Z_n=I-C_n\). The formula concerns these canonical Euclidean-orthogonal projections measured in the ambient real \(\ell_1^M\) or \(\ell_\infty^M\) norms; it is not a claim about all possible nonorthogonal projections. Graph edge orientations do not affect the norms.

## Proof
**1. Incidence reduction.** Let \(B\) be the unsigned incidence matrix of the ordinary cube (rows are cube vertices, columns are cube edges), and \(\Delta_Q\) its ordinary vertex Laplacian. Because the cube is \(n\)-regular,
\[
BB^\top=nI+A_Q=2nI-\Delta_Q,\qquad
\Delta_H=2nI-B^\top B,
\]
where \(\Delta_H\) is the line-graph vertex Laplacian. The cube automorphism group acts transitively on pairs of its incident edges, hence on edges of \(H_n\). Fix its line-graph edge formed by the cube edges \(E_1=\{0,e_1\}\) and \(E_2=\{0,e_2\}\), with unit source vector \(b=\delta_{E_1}-\delta_{E_2}\). Define \(g=\Delta_Q^+(\delta_{e_1}-\delta_{e_2})\). Direct substitution using \(B b=\delta_{e_1}-\delta_{e_2}\) gives
\[
\Delta_H\left[\frac{b+B^\top g}{2n}\right]=b.
\]
Thus the line-graph source potential, up to an additive constant, is \((b+B^\top g)/(2n)\). At a cube vertex \(v\), two line-graph vertices corresponding to the cube edges \(vv^i\) and \(vv^j\) have potential difference
\[
\frac1{2n}\{b_{vv^i}-b_{vv^j}+g(v^i)-g(v^j)\}.
\]
Every line-graph edge occurs exactly once as such a pair at a cube vertex, so its cut-projector column norm is the sum of these absolute differences over all cube vertices and all unordered directions \(i,j\).

**2. Exact Green levels and their order.** Write a cube vertex as \((x_1,x_2,w)\), with \(j=|w|\) and \(m=n-2\). The continuous-time cube heat kernel has one-coordinate flip probability \(p(t)=(1-e^{-2t})/2\). Integrating the difference between heat kernels started at \(e_1\) and \(e_2\) yields
\[
g(1,0,w)=h_j,\quad g(0,1,w)=-h_j,\quad
 g(0,0,w)=g(1,1,w)=0,\qquad
h_j=\int_0^{1/2}p^j(1-p)^{m-j}\,dp.
\]
For \(0\le j<m\), the ratio of the integrands for consecutive levels is \(p/(1-p)<1\) away from the endpoint. Hence \(h_j>h_{j+1}>0\). Also \(h_1<1\), which fixes all signs of the exceptional current changes below.

**3. All unsigned line-edge currents.** First omit the two nonzero entries of \(b\). At a cube vertex with \(x_1=x_2\) and \(|w|=j\), the values of \(g\) on its \(n\) neighbors are \(h_j,-h_j,0,\ldots,0\); the sum over unordered neighbor pairs of absolute differences equals \(2(n-1)h_j\). At a vertex with \(x_1\ne x_2\), those neighbor values, up to common sign, are two zeros, \(j\) copies of \(h_{j-1}\), and \(m-j\) copies of \(h_{j+1}\). Its pairwise absolute-difference sum is
\[
D_j=2jh_{j-1}+2(m-j)h_{j+1}
+j(m-j)(h_{j-1}-h_{j+1}),
\]
where terms with zero multiplicity are omitted at the endpoints. The following exact sums follow by interchanging a finite binomial sum with the integral and applying the binomial theorem:
\[
\begin{aligned}
\sum_{j=0}^m\binom mjh_j&=\tfrac12,\\
\sum_{j=0}^m\binom mj jh_{j-1}&=\tfrac{3m}{8},\\
\sum_{j=0}^m\binom mj(m-j)h_{j+1}&=\tfrac m8,\\
\sum_{j=0}^m\binom mjj(m-j)(h_{j-1}-h_{j+1})&=\tfrac{m(m-1)}4.
\end{aligned}
\]
There are two cube vertices for each \(w\) in each of the classes \(x_1=x_2\) and \(x_1\ne x_2\). The total baseline absolute current sum, prior to including \(b\), is therefore
\[
4(n-1)\cdot\tfrac12+2\left[2\left(\tfrac{3m}{8}+\tfrac m8\right)+\tfrac{m(m-1)}4\right]
=\frac{n^2+3n-6}{2}.
\]
The only changes from \(b_{E_1}=1\) and \(b_{E_2}=-1\) occur at the cube vertices \(0,e_1,e_2\). At \(0\) the absolute current sum increases by \(2(n-1)\). At each of \(e_1,e_2\) it increases by \(1+(n-2)(1-2h_1)\). Thus the total numerator becomes
\[
\frac{n^2+11n-14}{2}-4(n-2)h_1.
\]
An elementary integral gives
\[
h_1=\int_0^{1/2}p(1-p)^{n-3}\,dp
=\frac{1-n2^{-(n-1)}}{(n-1)(n-2)}.
\]
Division by \(2n\) gives the asserted \(T_n\). By line-graph edge transitivity, every column has this absolute sum, so it is the exact induced \(\ell_1\) norm. Symmetry of \(C_n\) makes its \(\ell_\infty\) norm the same.

**4. Complementary cycle norm.** The cut space of a connected graph on \(N\) vertices has dimension \(N-1\). By edge transitivity, all diagonal entries of \(C_n\) are equal to \((N-1)/M\). Because it is an orthogonal projector, these entries lie in \([0,1]\), and for any column of \(Z_n=I-C_n\), off-diagonal absolute values coincide with those of \(C_n\), while the diagonal absolute value changes from \((N-1)/M\) to \(1-(N-1)/M\). Hence its column sum is exactly
\[
T_n+1-2\frac{N-1}{M}
=T_n+1-\frac2{n-1}\left(1-\frac1{n2^{n-1}}\right).
\]
Again every column has this sum and symmetry gives the \(\ell_\infty\) formula. The displayed asymptotics follow by expanding the rational terms; the powers of two are exponentially small. \(\square\)

## Verification
The accompanying standard-library-only script `check_line_cube.py` independently constructs line graphs and solves their grounded vertex Laplacian systems by exact Gaussian elimination, verifying 124 edge columns across dimensions \(n=3,4,5,6\). It also recomputes the Green-level beta integrals from exact binomial tails and independently checks all four summation identities and the claimed column formula for every \(3\le n\le40\). Successful output: `LINE_HYPERCUBE_HODGE_EXACT_OK integral_dimensions=38 grounded_graphs=4 grounded_columns=124 line_edges=1400`. These finite checks are not substituted for the all-dimensional proof above.

## Relationship to prior work
Dilworth, Kutzarova and Ostrovskii [1], Theorem 45, establish the cut-space endpoint norm \((n+1)/2\) for the ordinary Boolean cube and develop the cycle-space projection framework. The line graph is a distinct graph: for \(n\ge3\) it contains triangles, whereas the ordinary cube is bipartite. Their cube norm therefore does not determine either of the two norms calculated here. Liu, Cao, Pan and Elaiw [2], Theorem 11, determine the Kirchhoff index of this exact line-graph family from its Laplacian spectrum. That trace-of-inverse invariant does not provide the full absolute electrical-current column sums computed here. Searches did not identify an explicit prior endpoint projection-norm classification of this line-graph family; this is a bounded originality assessment, not a uniqueness certificate.

## Limitations
Only real, unweighted line graphs of Boolean cubes in dimensions \(n\ge3\) and their canonical Euclidean-orthogonal cut/cycle projections are covered. The formulas do not assert minimal projection norms among arbitrary nonorthogonal projections, weighted generalizations, arbitrary line graphs, or intermediate \(\ell_p\) operator norms. Bibliographic coverage may be incomplete; independently checked novelty and an independent mathematical audit are not claimed.

## References
[1] S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582, first posted 21 May 2023, especially Section 2.7 and Theorem 45. https://arxiv.org/pdf/2305.12582

[2] J. Liu, J. Cao, X.-F. Pan, A. Elaiw, *The Kirchhoff Index of Hypercubes and Related Complex Networks*, Discrete Dynamics in Nature and Society (2013), article 543189, especially Theorem 11. https://doi.org/10.1155/2013/543189
