# Homotopy classification of all Latin-square graph clique complexes

## Finding
Let \(M\) be **any** Latin square of order \(n\ge5\). The vertices of its Latin-square graph \(L(M)\) are the \(n^2\) cells \((i,j)\); distinct cells are adjacent precisely when they share a row, a column, or a symbol. Let \(I(M)\) be the number of intercalates: pairs of distinct rows and distinct columns whose resulting \(2\)-by-\(2\) submatrix has the form \(\begin{psmallmatrix}a&b\\b&a\end{psmallmatrix}\), where \(a\ne b\). Then the *full* flag (clique) complex satisfies
\[
\boxed{\ |\operatorname{Cl}(L(M))|\simeq\bigvee^{(n-1)^3-I(M)}S^2\ }.
\]
In particular, its fundamental group is trivial for every such Latin square. The sphere count was established previously as the second Betti number over every field; the new topological assertion is simple connectivity for **all** Latin squares and the resulting integral homotopy classification, not a new numerical Betti formula.

For instance, Latin squares from the cyclic group of order six and from the nonabelian group of order six have respectively \(9\) and \(27\) intercalates, hence their clique complexes are wedges of \(116\) and \(98\) two-spheres. The theorem covers arbitrary Latin squares, whether or not they arise from a group.

## Assumptions and scope
A Latin square of order \(n\) has exactly one occurrence of each of \(n\) symbols in every row and column. The complex contains a simplex on each complete subgraph, with no truncation of dimension. All conclusions are ordinary nonequivariant integral homotopy statements. The explicit geometric proof of simple connectivity works under weaker size assumptions, but the combined homotopy classification is asserted here only for \(n\ge5\), precisely where the all-field homology theorem of Cioabă and Mim applies.

## Proof
**1. The rook subcomplex carries all fundamental-group generators.** Let \(R\) be the clique complex of the rook graph on the same cells, with edges only between cells sharing a row or column. It is the union of \(n\) full row simplices and \(n\) full column simplices. A row simplex meets a column simplex in one vertex, while distinct simplices of the same kind do not intersect; no intersection of three distinct members is nonempty. The simplicial nerve lemma therefore gives
\[
|R|\simeq |K_{n,n}|.
\]
The fundamental group of \(K_{n,n}\) is freely generated, relative to the evident two-star spanning tree, by its four-edge rectangles. Equivalently, the loops around all cell rectangles
\[
(i,j)\to(i,\ell)\to(k,\ell)\to(k,j)\to(i,j),
\quad i\ne k,\ j\ne\ell,
\]
normally generate \(\pi_1(|R|)\).

Now let \(X=\operatorname{Cl}(L(M))\). Every edge of \(X\setminus R\) joins two cells \(u=(i,j)\) and \(v=(k,\ell)\) having the same symbol, necessarily with \(i\ne k\) and \(j\ne\ell\). The intermediary \(w=(i,\ell)\) is row-adjacent to \(u\), column-adjacent to \(v\), and together \(u,w,v\) span a triangle of \(X\). Thus every extra edge is homotopic relative endpoints to a two-edge rook path. Any simplicial edge loop in \(X\) can consequently be moved into \(R\). This proves that \(\pi_1(|R|)\to\pi_1(|X|)\) is surjective.

**2. Every rook rectangle bounds an actual simplicial disk.** Fix different rows \(i,k\) and columns \(j,\ell\). Write its corners in cyclic order as
\[
a=(i,j),\quad b=(i,\ell),\quad c=(k,\ell),\quad d=(k,j).
\]
If opposite corners \(a,c\) share a symbol, the diagonal \(ac\) gives two triangles \((a,b,c)\) and \((a,c,d)\), filling the rectangle. The same holds with diagonal \(bd\) if \(b,d\) share a symbol.

In the remaining case neither diagonal pair shares a symbol. Put \(s=M[i,\ell]\), the symbol at \(b\). There are unique \(h,m\) with
\[
M[k,h]=s,\qquad M[m,j]=s.
\]
The Latin condition and the absence of a diagonal edge imply \(h\notin\{j,\ell\}\) and \(m\notin\{i,k\}\). Set \(e=(k,h)\) and \(f=(m,j)\). All six vertices \(a,b,c,d,e,f\) are distinct. The following six *genuine* clique triangles form an embedded triangulated disk:
\[
(a,b,f),\quad(b,f,e),\quad(b,e,c),\quad(c,e,d),\quad(d,e,f),\quad(d,f,a).
\]
Indeed, in each triple every pair agrees in a row, column, or the symbol \(s\). Their only boundary edges are \(ab,bc,cd,da\): every other edge belongs to two triangles; the links of the two interior vertices \(e,f\) are four-cycles, and the links of the four boundary vertices are paths. Hence their union is a disk with exactly the required rectangular boundary, *not merely a two-chain with that boundary*. This proves that each rectangle generator of \(\pi_1(|R|)\) becomes nullhomotopic in \(X\). Surjectivity from step 1 implies
\[
\pi_1(|X|)=1.
\]

**3. Pass from the all-field homology calculation to the integral homotopy type.** Cioabă and Mim [1, Theorem 3.12] prove for every Latin square of order \(n\ge5\) and every field \(F\) that its clique complex has \(H_1(X;F)=0\), \(H_i(X;F)=0\) for \(i\ge3\), and \(\dim_F H_2(X;F)=(n-1)^3-I(M)\). Because \(X\) is a finite simplicial complex, the universal coefficient theorem over \(\mathbb Q\) and all prime fields, together with the fact that \(H_2(X;\mathbb Z)\) is a subgroup of the free simplicial two-chain group, gives
\[
\widetilde H_i(X;\mathbb Z)=
\begin{cases}\mathbb Z^{(n-1)^3-I(M)},&i=2,\\0,&i\ne2.\end{cases}
\]
The preceding paragraphs establish simple connectivity, which does *not* follow from vanishing first homology alone. Integral Hurewicz gives \(\pi_2(X)\cong H_2(X;\mathbb Z)\). Choose based maps from that many copies of \(S^2\) representing an integral basis and wedge them to a map into \(X\). It induces an isomorphism on all integral homology groups. Both spaces are simply connected CW complexes, so the homology form of Whitehead's theorem makes this map a homotopy equivalence, proving the boxed result.

## Verification
The accompanying standalone Python file `latin_square_checker.py` uses only the standard library. It independently enumerates all maximal cliques using Bron--Kerbosch, checks their entire face closures against a separate line-and-exception enumeration, computes exact mod-two boundary ranks, and checks **every** rectangle disk and every symbol-edge triangle. It verifies cyclic Latin squares of orders \(5,6,7\) and the multiplication table of the nonabelian group of order \(6\). The four respective second Betti ranks were \(64,116,216,98\), with no other positive-degree homology, and the checker returned `VERIFY_OK`. These finite computations corroborate the uniform proof, not replace it. The six-triangle disk proof, the surjectivity of the rook inclusion on \(\pi_1\), and the Whitehead step hold for arbitrary \(M\).

## Relationship to prior work
The exact same-object primary source [1] determines **all-field homology groups**, including the numerical rank \((n-1)^3-I(M)\), and its Proposition 3.3 exhibits the same six triangles as the support of a signed bounding two-chain. Such a chain identity, and indeed homology vanishing over every field, cannot in general prove triviality of a nonabelian fundamental group. The added geometric observation that these triangles form an *embedded disk*, combined with a rook-subcomplex nerve calculation and edge-by-edge elimination of symbol edges, establishes the missing \(\pi_1\)-statement. This upgrades the original numerical homology theorem to a complete integral homotopy classification for **arbitrary** Latin squares. A previously obtained classification for the restricted family of odd cyclic Latin squares does not cover even orders or non-group Latin squares; this theorem genuinely enlarges its quantified domain.

Searches for aliases including quasigroup Latin squares, row--column--symbol graphs, fundamental groups of flag complexes, and clique homotopy classifications yielded no stronger theorem for the same arbitrary-Latin-square objects. This bounded comparison does not prove global uniqueness. General literature on fundamental groups of clique graphs [2] deals with a different graph construction and does not imply this result. The partition-transfer clique-complex sphere theorem [3] concerns another graph family.

## Limitations
The sphere decomposition is **nonequivariant** and does not identify preferred explicit integral homology generators or their automorphism representations. It relies on the all-field homology computation of [1], rather than independently reproving those Betti ranks, and it does not assert a simplicial collapse. The six bounding triangles are already explicitly enumerated as a *homology chain* in [1]; the distinction claimed here is the topological disk and its consequences. An implicit equivalent geometric argument in unindexed literature remains a residual originality risk. No independent mathematical audit has been performed.

## References
[1] Sebastian M. Cioabă and Mutasim Mim, *On the homology groups of clique complexes of strongly regular graphs*, arXiv:2606.27328, first public posting 2026-06-25; relevant Proposition 3.3 and Theorem 3.12. https://arxiv.org/abs/2606.27328

[2] F. Larrión, M. A. Pizaña, and R. Villarroel-Flores, *The Fundamental Group of the Clique Graph*, European Journal of Combinatorics 30 (2009), 288--294. https://uaeh.edu.mx/investigacion/productos/3921/

[3] Fedor B. Lyudogovskiy, *The homotopy type of the clique complex of the partition graph*, arXiv:2603.14370, first posted 2026-03-15. https://arxiv.org/abs/2603.14370
