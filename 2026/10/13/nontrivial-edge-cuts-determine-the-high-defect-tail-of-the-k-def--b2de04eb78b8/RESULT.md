# Nontrivial edge cuts determine the high-defect tail of the \(k\)-defect number
## Finding
Let \(G\) be a finite connected simple graph with \(N\ge4\) vertices and \(m\) edges. For \(S\subseteq V(G)\), let \(\delta(S)\) be the set of edges with exactly one endpoint in \(S\), and define
\[
\eta(G)=\min\{|\delta(S)|:2\le |S|\le N-2\}.
\]
For \(0\le k\le m\), let \(\phi_k(G)\) denote the least number of colors in a vertex coloring having exactly \(k\) monochromatic edges, with \(\phi_k(G)=0\) when no such coloring exists. Then, for every integer \(k\) satisfying
\[
m-\eta(G)<k\le m,
\]
one has
\[
\phi_k(G)=
\begin{cases}
1,&k=m,\\
2,&k=m-d(v)\text{ for some }v\in V(G)\text{ with }d(v)<\eta(G),\\
0,&\text{otherwise.}
\end{cases}
\]

For the crown graph \(\operatorname{Cr}_n=K_{n,n}-M_n\), \(n\ge4\),
\[
\eta(\operatorname{Cr}_n)=2n-4.
\]
Hence, throughout the exact high-defect range
\[
n^2-3n+4<k\le n(n-1),
\]
\[
\phi_k(\operatorname{Cr}_n)=
\begin{cases}
1,&k=n(n-1),\\
2,&k=(n-1)^2,\\
0,&\text{otherwise.}
\end{cases}
\]
The lower endpoint is sharp: \(\phi_{n^2-3n+4}(\operatorname{Cr}_n)=2\).

## Assumptions and scope
All graphs are finite, simple, and connected. The general theorem assumes \(N\ge4\), solely so that a union of two singleton color classes can have a complement of size at least two. The crown specialization assumes \(n\ge4\). No assertion is made here about \(\phi_k\) below the displayed high-defect threshold, except for the sharp endpoint.

A monochromatic edge has endpoints of the same color. If a coloring has \(k\) monochromatic edges, write \(b=m-k\) for its number of bichromatic edges.

## Proof
Consider first an arbitrary \(G\). Suppose a coloring is not monochromatic and has \(b<\eta(G)\) bichromatic edges. For any color class \(C\), every edge of \(\delta(C)\) is bichromatic. Therefore \(|\delta(C)|\le b<\eta(G)\). By the definition of \(\eta(G)\), no color class can have size between \(2\) and \(N-2\). Thus every color class has size \(1\) or \(N-1\).

There cannot be three or more color classes. Indeed, then two singleton classes \(\{u}\) and \(\{v}\) exist. Their union has size \(2\), its complement has size at least \(2\), and every edge of \(\delta(\{u,v}\) is bichromatic. Hence
\[
b\ge |\delta(\{u,v})|\ge\eta(G),
\]
a contradiction. Consequently there are exactly two color classes, one singleton \(\{v}\) and its complement. The bichromatic edges are precisely the edges incident with \(v\), so \(b=d(v)\). Conversely, coloring one vertex \(v\) with one color and every other vertex with a second color produces exactly \(m-d(v)\) monochromatic edges. The all-one-color coloring gives \(k=m\). This proves the general formula.

Now let \(G=\operatorname{Cr}_n\) with bipartition \(A\cup B\), where \(|A|=|B|=n\), and the deleted perfect matching pairs corresponding indices. Let \(S\) satisfy \(2\le |S|\le2n-2\). Replacing \(S\) by its complement if necessary, put \(s=|S|\le n\), \(a=|S\cap A|\), and \(b=|S\cap B|\), so \(s=a+b\). In \(K_{n,n}\), the cut has
\[
a(n-b)+b(n-a)=ns-2ab
\]
edges. Passing to the crown deletes at most \(s\) matching edges from this cut. Therefore
\[
|\delta_{\operatorname{Cr}_n}(S)|\ge(n-1)s-2ab\ge(n-1)s-\frac{s^2}2.
\]
For \(n\ge4\) and \(2\le s\le n\), the concave quadratic on the right is minimized at an endpoint, where its values are \(2n-4\) and \(n(n-2)/2\), respectively. Both are at least \(2n-4\). Thus \(\eta(\operatorname{Cr}_n)\ge2n-4\).

Equality is attained by taking \(S\) to be the endpoints of any crown edge. Both vertices have degree \(n-1\), and their common internal edge is counted twice in the degree sum, so
\[
|\delta(S)|=2(n-1)-2=2n-4.
\]
Hence \(\eta(\operatorname{Cr}_n)=2n-4\). Since every crown vertex has degree \(n-1<2n-4\), the general theorem gives the stated high-defect classification. Finally, a two-coloring whose smaller color class consists of the endpoints of one crown edge has exactly \(n(n-1)-(2n-4)=n^2-3n+4\) monochromatic edges, proving sharpness of the threshold.

## Verification
The proof is symbolic and covers every admissible graph in the general theorem and every \(n\ge4\) in the crown specialization. The included `verify.py` is corroborative rather than foundational. It exhaustively checks the nontrivial cut minimum for crowns of orders \(2n\) with \(4\le n\le9\), enumerates every unlabeled vertex-color partition for \(n=4,5\) and verifies the claimed high-defect values, and checks the algebraic identities for \(4\le n\le100\).

The replay result is:

`ALL CHECKS PASSED; restricted_cut_orders=4..9; subset_checks=349272; partition_orders=4,5; set_partitions=120115; symbolic_orders=4..100`

## Relationship to prior work
Mphako-Banda, Kriel, and Alochukwu introduced the k-defect number and explicitly observed the known edge-connectivity gap \(\phi_k(G)=0\) for \(|E(G)|-\lambda(G)<k<|E(G)|\). Their paper gives exact values for trees, cycles, and wheels and asks for graph parameters that force more zero values of \(\phi_k\). The present theorem refines the edge-connectivity observation: the larger nontrivial cut threshold \(\eta(G)\) controls a longer high-defect interval, with the only possible interior exceptions coming from singleton cuts and hence from vertex degrees.

The 2019 survey on \(k\)-defect polynomials relates them to Tutte and coboundary polynomials. A 2012 survey of Tutte-polynomial techniques gives a bad-coloring polynomial formula for complete bipartite graphs, but that formula concerns \(K_{m,n}\), not the one-factor-deleted crown graph. Searches under the crown aliases \(K_{n,n}-M_n\), \(K_{n,n}-I\), and bipartite Kneser \(H(n,1)\), together with k-defect, bad-coloring, Tutte, coboundary, edge-cut, and restricted-connectivity terminology, did not locate a statement implying the theorem above.

## Limitations
The theorem determines only the high-defect tail. It does not classify the lower values of \(\phi_k(\operatorname{Cr}_n)\), where several color classes and more complicated cut partitions can occur. The literature search cannot exclude an older poorly indexed formulation of the same cut argument, especially through Tutte/coboundary-polynomial coefficients or restricted edge-connectivity language. The originality assessment therefore concerns the explicit theorem and implication comparison against the sources inspected, not a claim of exhaustive bibliographic impossibility.

## References
1. E. Mphako-Banda, C. Kriel, A. Alochukwu, *A note on the k-defect number: Vertex Coloring with a Fixed Number of Monochromatic Edges*, arXiv:2510.00712. Earliest public version: 2025-10-01.
2. E. Mphako-Banda, *An introduction to the k-defect polynomials*, Quaestiones Mathematicae 42 (2019), 207-216. DOI: 10.2989/16073606.2018.1443168.
3. C. Merino, C. Ramírez-Ibáñez, G. Rodríguez-Sánchez, *The Tutte Polynomial of Some Matroids*, International Journal of Combinatorics (2012), Article 430859. DOI: 10.1155/2012/430859.
4. C. Kriel, E. Mphako-Banda, *Sizes of flats of cycle matroids of complete graphs*, Revista Colombiana de Matemáticas 56 (2022), 63-75. DOI: 10.15446/recolma.v56n1.105617.
