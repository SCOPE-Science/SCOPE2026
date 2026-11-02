# Exact three-dynamic chromatic numbers of Möbius ladders

## Finding
For every integer \(m\ge3\), let \(M_{2m}\) be the Möbius ladder with vertex set \(\mathbb Z_{2m}\), where vertices at cyclic differences \(\pm1\) and \(m\) are adjacent. Let \(\chi_3^d\) denote the three-dynamic chromatic number: the least number of colors in a proper vertex coloring in which every vertex has three differently colored neighbors. Then
\[
\chi_3^d(M_{2m})=\chi(M_{2m}^{2})=
\begin{cases}
8,&m=4,\\
6,&m\in\{3,8\},\\
4,&m\equiv2\pmod4,\\
5,&\text{otherwise}.
\end{cases}
\]
The residue-class case includes \(m=6,10,14,\ldots\); the final case includes \(m=5,7,9,11,12,\ldots\) but not \(m=8\). In particular, the sixteen-vertex Möbius ladder requires six colors even though the neighboring residue classes admit five.

## Assumptions and scope
Graphs are finite, simple, undirected, and their colors are ordinary named integers. The graph square \(G^2\) joins distinct vertices whenever their distance in \(G\) is at most two. As \(M_{2m}\) is cubic, a proper coloring is three-dynamic precisely when every vertex and its three neighbors receive distinct colors. Every pair of vertices at distance two shares a neighbor, so this is equivalent to a proper coloring of \(M_{2m}^2\).

For a second model, arrange the vertices as two rows of \(m\) columns, \(u_0,\ldots,u_{m-1}\) and \(v_0,\ldots,v_{m-1}\). There are rungs \(u_i v_i\), horizontal edges \(u_i u_{i+1}\) and \(v_i v_{i+1}\) for \(0\le i<m-1\), and twisted closing edges \(u_{m-1}v_0\), \(v_{m-1}u_0\). This is isomorphic to the stated circulant model: identify \(u_i=i\) and \(v_i=i+m\).

## Proof
**1. Local square-coloring constraints.** For \(m\ge5\), write \(c_i=(a_i,b_i)\) for the colors of \(u_i,v_i\), and extend the column sequence to every integer using the twisted-periodic rule
\[
c_{i+m}=\widetilde c_i,\qquad \widetilde{(a,b)}=(b,a).
\]
A coloring is proper on the square if and only if, for every integer \(i\), all of the following hold:

* \(a_i\ne b_i\);
* the four entries of \(c_i,c_{i+1}\) are pairwise distinct;
* \(a_i\ne a_{i+2}\) and \(b_i\ne b_{i+2}\).

Indeed, the first condition treats each rung; the second treats the horizontal edges and all length-two paths traversing one horizontal edge and one rung; the third treats the length-two paths using two horizontal edges. These are all possibilities for a distance-at-most-two pair. The twisted extension encodes both seam edges and the two-step paths across the seam.

**2. Lower bound four and exact four-color rigidity.** Two consecutive columns form a four-clique in the square, hence at least four colors are required. In a four-coloring, the unordered two-color supports of consecutive columns are complementary. It follows that the supports of \(c_i\) and \(c_{i+2}\) coincide. The third local condition then forces
\[
c_{i+2}=\widetilde c_i
\]
for every \(i\). This recurrence has period four, with \(c_{i+4}=c_i\). Since the twisted closure instead requires \(c_{i+m}=\widetilde c_i\), a four-coloring forces \(m\equiv2\pmod4\). Conversely, when \(m\equiv2\pmod4\), the repeated four-column pattern
\[
(0,1),\ (2,3),\ (1,0),\ (3,2)
\]
obeys all local conditions and the twisted closure. Thus the square is four-colorable exactly for that congruence class.

**3. The small complete squares.** For \(m=3\), the graph is \(K_{3,3}\); its diameter is two, so its square is \(K_6\). For \(m=4\), cyclic differences \(1,2,3,4\) all correspond to paths of length at most two, using the generators \(\pm1,4\); hence its square is \(K_8\). These give six and eight colors, respectively.

**4. A sixteen-vertex obstruction.** Put \(m=8\). The local constraints imply that an independent set of the square has at most one vertex in each column and cannot use consecutive columns, including the twisted closing pair. Any independent set of four vertices would therefore use either the four even columns \(0,2,4,6\) or the four odd columns \(1,3,5,7\). In three consecutive two-column steps, the third local condition forces the chosen row to alternate. The fourth step, across the twisted seam, forbids *opposite* chosen rows instead, and thus requires equal chosen rows. Three alternations cannot return to the original row. Consequently \(\alpha(M_{16}^2)\le3\), so \(\chi(M_{16}^2)\ge\lceil16/3\rceil=6\). The following six-color assignment attains this value (the top and bottom words list the eight consecutive column colors):

```
top:    02130425
bottom: 13021534
```

**5. Five-color seeds and a length-four insertion.** For all remaining \(m\ge5\), the four-color rigidity gives the lower bound five. Here are three directly verifiable proper five-color square-colorings; the two words are the top and bottom rows:

| \(m\) | top | bottom |
| ---: | :--- | :--- |
| 5 | `02104` | `13423` |
| 7 | `0213024` | `1302413` |
| 12 | `021302140324` | `130214032413` |

All three begin with the same two columns \(A=(0,1)\), \(B=(2,3)\). Suppose a valid twisted column word starts with \(A,B\). Replace its beginning
\[
(A,B,c_2,\ldots,c_{m-1})
\]
by
\[
(A,B,\widetilde A,\widetilde B,A,B,c_2,\ldots,c_{m-1}).
\]
This adds four columns, retains the original first two and last columns, and preserves all local constraints. The inserted triples belong to the four-color pattern \(A,B,\widetilde A,\widetilde B,A,B\); the triple \(A,B,c_2\) is an original valid triple. All other triples, including those using the twisted seam, remain unchanged. Repeating this insertion produces five-colorings for all lengths \(m\equiv1\pmod4\) with \(m\ge5\), for all \(m\equiv3\pmod4\) with \(m\ge7\), and for all \(m\equiv0\pmod4\) with \(m\ge12\). Together with the four-color construction, the exceptional cases \(m=3,4,8\), and the lower bounds, these exhaust every \(m\ge3\). \(\square\)

## Verification
The attached standalone `verify.py` reconstructs the Möbius ladder directly on \(\mathbb Z_{2m}\), computes graph squares by two-step neighbor expansion, and checks the three seed assignments, their length-four extensions, and the four-color periodic construction against every square edge. It checks \(m\equiv2\pmod4\) through \(m=202\), and 30 successive four-column insertions in each of the three five-color residue families. It separately verifies that the squares for \(m=3,4\) are complete and exhaustively checks all four-element vertex subsets for independence in \(M_{16}^2\). These finite tests corroborate the explicit constructions and the exceptional lower bound; the proof above establishes the universal statement.

Run with `python3 verify.py` using the standard Python library. A successful check ends with `VERIFY_OK`.

## Relationship to prior work
Gutiérrez and Ugarte (first public 2026-10-07) connect three-dynamic coloring of cubic graphs to graph-square coloring, and determine bounds for claw-free cubic graphs and exact values for a distinct family of four-regular circulants. Their inspected paper does not treat Möbius ladders. Madaras and Šurimová give the full three-homogeneous color range for ordinary prism graphs \(C_m\square K_2\); twisted Möbius closure is a different graph and changes the congruence obstruction. Yao and Ma determine the *strong edge chromatic index* of Möbius ladders; its domain is colorings of edges (equivalently, squares of line graphs), not colorings of vertices of \(M_{2m}^2\), so its numeric values do not imply the present theorem. MathWorld gives the squared Möbius ladder as a circulant with generating distances \(1,2,m-1,m\) but does not evaluate its chromatic number. These sources provide context, not a claim of certified historical novelty.

## Limitations
The theorem is restricted to simple Möbius ladders, with at least six vertices, and to ordinary three-dynamic/square vertex coloring. It does not classify all optimal colorings, strong edge colorings, arbitrary twisted cylinder graphs, or other dynamic parameters. A complete historical-priority determination, especially under older circulant-distance-coloring terminology, remains open to independent literature review. No independent mathematical audit has been performed.

## References
1. J. Gutiérrez and G. Ugarte, *Dynamic Coloring and Graph Squares of Regular Graphs*, arXiv:2610.09565, first submitted 2026-10-07, https://arxiv.org/abs/2610.09565.
2. T. Madaras and M. Šurimová, *Homogeneous colourings of graphs*, *Mathematica Bohemica* 148 (2023), 105–115; published online 2022-04-28, https://doi.org/10.21136/MB.2022.0007-21.
3. S. Yao and D. Ma, *The strong chromatic index of Möbius ladder \(C(2n,n)\)*, *Journal of Mathematics* 38 (2018), 497–501, https://sxzz.whu.edu.cn/html/2018/3/20180313.htm.
4. E. W. Weisstein, *Möbius Ladder* and *Graph Square*, MathWorld, https://mathworld.wolfram.com/MoebiusLadder.html and https://mathworld.wolfram.com/GraphSquare.html.
