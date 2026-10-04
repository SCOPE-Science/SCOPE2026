# Exact rainbow connection of Dirac cycle powers
## Finding
Let \(C_n^k\) denote the \(k\)-th power of the cycle with vertex set \(\mathbb Z_n\): distinct vertices are adjacent exactly when their cyclic distance is at most \(k\). A noncomplete cycle power is Dirac exactly when
\[
\left\lceil \frac n4\right\rceil\le k<\left\lfloor\frac n2\right\rfloor.
\]
For every such pair \((n,k)\),
\[
\operatorname{rc}(C_n^k)=\operatorname{src}(C_n^k)=2.
\]
There is also a sharp generator-based dichotomy. If \(n<4k\), color every edge of cyclic distance \(k\) red and every edge of smaller cyclic distance blue; this is a strongly rainbow-connecting coloring. If \(n=4k\), no red-blue coloring depending only on cyclic distance can rainbow-connect \(C_{4k}^k\). Nevertheless a non-generator-based red-blue coloring does strongly rainbow-connect it: represent each edge uniquely as \(\{i,i+r\}\), with \(1\le r\le k\) modulo \(4k\), and color the edge by the parity of \(\lfloor i/k\rfloor\).

Complete cycle powers have \(\operatorname{rc}=\operatorname{src}=1\).

## Assumptions and scope
Graphs are finite, simple, and undirected. A rainbow path has pairwise distinct edge colors. The rainbow connection number \(\operatorname{rc}(G)\) is the minimum number of edge colors needed so that every vertex pair has a rainbow path. The strong rainbow connection number \(\operatorname{src}(G)\) additionally requires a rainbow geodesic for every pair.

For a noncomplete cycle power \(C_n^k\), every vertex has degree \(2k\), so the Dirac condition \(2k\ge n/2\) is equivalent to \(4k\ge n\). Noncompleteness is equivalent to \(k<\lfloor n/2\rfloor\).

A generator-based coloring here means that the color of an edge depends only on its cyclic distance \(r\in\{1,\ldots,k\}\). This is the natural undirected specialization of coloring by the Cayley generator class.

## Proof
First suppose \(n<4k\). Let red be the color assigned to edges of cyclic distance exactly \(k\), and blue the color assigned to edges of cyclic distance less than \(k\). Consider nonadjacent vertices \(u,v\). Orient the shorter arc so that \(v=u+d\pmod n\) with
\[
k<d\le\left\lfloor\frac n2\right\rfloor<2k.
\]
Set \(w=u+k\pmod n\). Then \(uw\) has cyclic distance \(k\), while \(wv\) has cyclic distance \(d-k\), which lies in \(\{1,\ldots,k-1\}\). Thus \(u-w-v\) is a red-blue path. Since \(u,v\) are nonadjacent and have a two-edge path, this path is a geodesic. Adjacent pairs use their single edge, so the coloring is strongly rainbow connecting.

Now suppose \(n=4k\). Every edge has a unique clockwise representation \(\{i,i+r\}\) with \(1\le r\le k\). Partition \(\mathbb Z_{4k}\) into the four consecutive blocks
\[
B_j=\{jk,jk+1,\ldots,(j+1)k-1\},\qquad j\in\{0,1,2,3\}.
\]
Color \(\{i,i+r\}\) red when \(i\in B_0\cup B_2\) and blue when \(i\in B_1\cup B_3\). For a nonadjacent pair, orient a shortest arc as \(v=u+d\pmod{4k}\) with \(k<d\le2k\), and again put \(w=u+k\). The edge \(uw\) starts at \(u\), whereas \(wv\) starts at \(u+k\); adding \(k\) moves to a block of opposite parity, including across the wrap from \(B_3\) to \(B_0\). Hence the two edges receive opposite colors. The path is a rainbow geodesic.

For the generator-based obstruction at \(n=4k\), examine the antipodal pair \(0,2k\). Its only common neighbors are \(k\) and \(3k\). Each resulting two-edge path consists of two edges of cyclic distance \(k\). In a coloring depending only on cyclic distance these two edges have the same color. A rainbow path using only two colors has length at most two, so no generator-based red-blue coloring can rainbow-connect this pair.

Finally, every noncomplete \(C_n^k\) has diameter two under the Dirac hypothesis: the construction above supplies a two-edge path for each nonadjacent pair. Therefore \(2\le\operatorname{rc}\le\operatorname{src}\le2\), proving equality. Complete cycle powers require one color.

## Verification
The accompanying verifier independently constructs the claimed colorings for every noncomplete Dirac cycle power with \(5\le n\le80\), checks the prescribed rainbow geodesic for every nonadjacent pair, and brute-force searches all possible intermediate vertices for every such pair when \(n\le30\). It also checks, for \(1\le k\le30\), that the antipodal pair in \(C_{4k}^k\) has exactly the two common neighbors \(k\) and \(3k\), with both incident edge distances equal to \(k\). The replay output is:

`ALL CHECKS PASSED; constructive_nonadjacent_pairs=312398; boundary_cases=30; independent_bruteforce_nonadjacent_pairs=5850`

These finite checks are stress tests only; the theorem for all \((n,k)\) follows from the proof above.

## Relationship to prior work
Barát, Boyadzhiyska, and Freschi introduced the current Dirac-threshold problem for rainbow connection and explicitly asked whether every Dirac circulant or Cayley graph admits an rc2-coloring. Their concluding discussion singles out the cyclic graph on \(\mathbb Z_{4k}\) with edges at cyclic distance at most \(k\): a coloring based only on the generator distance cannot guarantee a rainbow path between antipodal vertices. The theorem above resolves that highlighted family by giving a non-generator-based two-coloring at the boundary and shows that the generator obstruction disappears immediately when \(n<4k\).

Earlier work of Basavaraju, Chandran, Rajendraprasad, and Ramaswamy treats graph powers in general and proves radius-based bounds such as \(\operatorname{rc}(G^k)\le2r(G^k)+1\). That theorem does not imply the exact value two for this cycle-power family, nor the strong rainbow statement or the generator-based boundary dichotomy.

Targeted searches for exact rainbow or strong-rainbow connection formulas for cycle powers and for the boundary family \(C_{4k}^k\) did not locate a covering theorem. The closest indexed results concern general graph powers, ordinary cycles, unrelated circulant invariants, and rainbow notions different from rainbow connection.

## Limitations
The result covers powers of a single cycle, not arbitrary Dirac circulant or Cayley graphs, so the general circulant/Cayley question remains open. The non-generator obstruction is proved specifically at the exact Dirac boundary \(n=4k\); it does not rule out other restricted coloring schemes. Literature searches cannot certify absolute novelty, and an obscure special-family treatment not surfaced by the checked sources remains a residual risk.

## References
1. J. Barát, S. Boyadzhiyska, A. Freschi, *Rainbow connecting 2-colorings of super-Dirac graphs*, arXiv:2609.11437v1, 2026. Primary MSC 05C15; secondary MSC 05C40.
2. M. Basavaraju, L. S. Chandran, D. Rajendraprasad, A. Ramaswamy, *Rainbow Connection Number of Graph Power and Graph Products*, arXiv:1104.4190v2; Graphs and Combinatorics 30 (2014), 1363–1382.
3. G. Chartrand, G. L. Johns, K. A. McKeon, P. Zhang, *Rainbow connection in graphs*, Mathematica Bohemica 133 (2008), 85–98, doi:10.21136/MB.2008.133947.
