# Dominant edge metric bases of square-page book graphs
## Finding
For every integer \(r\ge2\), let \(B_r\) be the book graph formed from \(r\) copies of \(C_4\) sharing the common edge \(xy\), with page \(i\) equal to \(x a_i b_i y x\). Then
\[
\operatorname{Ddim}_e(B_r)=r+1.
\]
Moreover, the only dominant edge metric bases are
\[
X=\{x,b_1,\ldots,b_r\}
\qquad\text{and}\qquad
Y=\{y,a_1,\ldots,a_r\}.
\]

## Assumptions and scope
All graphs are finite, simple, and connected. For a vertex \(v\) and an edge \(e=uw\),
\[
d(v,e)=\min\{d(v,u),d(v,w)\}.
\]
An edge metric generator distinguishes all edges by their distance vectors. A dominant edge metric generator is an edge metric generator that is also a vertex cover.

The graph \(B_r\) is bipartite with parts
\[
X=\{x,b_1,\ldots,b_r\},
\qquad
Y=\{y,a_1,\ldots,a_r\}.
\]

## Proof
The edges
\[
xy,a_1b_1,\ldots,a_rb_r
\]
form a perfect matching of size \(r+1\). Hence every vertex cover, and therefore every dominant edge metric generator, has size at least \(r+1\).

We show that \(X\) resolves all edges. Order its landmarks as \(x,b_1,\ldots,b_r\), and write
\[
s=xy,\qquad p_i=xa_i,\qquad q_i=a_ib_i,\qquad t_i=b_iy.
\]
Their edge-distance representations are
\[
r^e(s\mid X)=(0;1,\ldots,1),
\]
\[
r^e(p_i\mid X)=(0;2,\ldots,2,\overset{i}{1},2,\ldots,2),
\]
\[
r^e(q_i\mid X)=(1;2,\ldots,2,\overset{i}{0},2,\ldots,2),
\]
and
\[
r^e(t_i\mid X)=(1;1,\ldots,1,\overset{i}{0},1,\ldots,1).
\]
For \(r\ge2\) these vectors are pairwise distinct. Thus \(X\) is an edge metric generator. Since \(X\) is a bipartition class, it is also a vertex cover. Hence \(X\) is a dominant edge metric generator of size \(r+1\). By symmetry, so is \(Y\), proving
\[
\operatorname{Ddim}_e(B_r)=r+1.
\]

Now let \(S\) be any dominant edge metric basis. Since \(|S|=r+1\) and the displayed matching has \(r+1\) edges, \(S\) contains exactly one endpoint of each matching edge. If \(x\in S\), then \(y\notin S\). Every edge \(yb_i\) must then be covered by \(b_i\), so \(b_i\in S\) for all \(i\). Hence \(S=X\). Similarly, if \(y\in S\), then \(S=Y\). Therefore the two bipartition classes are exactly all dominant edge metric bases.

## Verification
The included checker constructs \(B_r\), computes all-pairs vertex distances by breadth-first search, evaluates the vertex-cover condition and the edge-distance vectors directly, and exhaustively tests all candidate sets.

For every \(2\le r\le9\), every set smaller than \(r+1\) fails, and the successful sets of size \(r+1\) are exactly the two bipartition classes.

## Relationship to prior work
The paper introducing dominant edge metric dimension defines the parameter as the minimum size of a set that is simultaneously a vertex cover and an edge metric generator. Its exact product results concern corona products, edge-corona products, and joins, together with a caterpillar construction. The accessible primary text contains no square-page book theorem and no Cartesian-product theorem.

The book graph here is also
\[
K_{1,r}\square K_2.
\]
Targeted searches under book, square-page book, generalized-theta, and Cartesian-product descriptions did not locate an equivalent dominant edge metric theorem for this family. The closest same-invariant comparison found was an exact theorem for hypercubes, a different bipartite Cartesian family.

## Limitations
The theorem covers square-page books with \(r\ge2\). The boundary graph \(B_1=C_4\) has dominant edge metric dimension \(3\) but four minimum bases, so the two-basis classification begins at \(r=2\). No claim is made for triangular books, longer-cycle books, or arbitrary generalized theta graphs. The finite exhaustive verification is corroborative only.

## References
1. M. Tavakoli, M. Korivand, A. Erfanian, G. Abrishami, E. T. Baskoro, “The dominant edge metric dimension of graphs,” Electronic Journal of Graph Theory and Applications 11(1) (2023), 197–208, DOI 10.5614/ejgta.2023.11.1.16.
2. A. Kelenc, N. Tratnik, I. G. Yero, “Uniquely identifying the edges of a graph: the edge metric dimension,” Discrete Applied Mathematics 251 (2018), 204–220, DOI 10.1016/j.dam.2018.05.052.
