# Four majority colours in the ternary Hamming three-cube and a bound in every odd dimension

## Finding

Let \(H_d=K_3^{\square d}\) be the Cartesian product of \(d\) triangles. A **majority C-colouring** is a surjective assignment of colours to vertices in which at least half the neighbours of each vertex have its own colour. Let \(\overline\chi_{\ge}(G)\) denote the maximum number of colours in such an assignment.

**Theorem.** The ternary Hamming three-cube has
\[
\overline\chi_{\ge}(H_3)=4.
\]
Moreover, for every integer \(r\ge0\),
\[
\overline\chi_{\ge}(H_{2r+3})\ge4\cdot3^r.
\]
For every odd \(d\ge3\), this improves the previously available general lower bound \(3^{\lfloor d/2\rfloor}\) for the ternary Hamming graph by a factor of \(4/3\). The second inequality is not asserted to be sharp when \(r>0\).

## Assumptions and scope

All graphs are finite, undirected, and simple. The vertex set of \(H_d\) is \(\{0,1,2\}^d\); two distinct vertices are adjacent if and only if they differ in precisely one coordinate. Each vertex has degree \(2d\), so the majority condition is that its colour class contain at least \(d\) of its neighbours. Colours are distinguishable only through their partition classes; the number of colours means the number of nonempty classes.

The exact assertion concerns only \(d=3\). The infinite-dimensional assertion is a constructive lower bound for \(d=2r+3\), \(r\ge0\).

## Proof

**Lower bound of six vertices per colour class in dimension three.** Let \(S\subseteq V(H_3)\) be a nonempty set such that the induced graph \(H_3[S]\) has minimum degree at least \(3\). We show \(|S|\ge6\).

For \(|S|\le3\), no induced vertex has three neighbours. If \(|S|=4\), the minimum-degree condition would force a four-clique; however, every clique of \(H_3\) is contained in one coordinate line, which has just three vertices. Indeed, two vertices adjacent to a fixed vertex in distinct coordinate directions are not adjacent to one another.

Suppose \(|S|=5\). The open neighbourhood of any vertex of \(H_3\) is the disjoint union of three edges, one for each coordinate direction. If \(v\in S\) had degree four in \(H_3[S]\), its four neighbours would be all other vertices of \(S\); each such neighbour would have at most one neighbour among those four, and hence degree at most two in \(H_3[S]\), a contradiction. Therefore every vertex of \(H_3[S]\) would have degree exactly three. That is impossible: an odd number of vertices cannot all have odd degree, by the handshaking lemma. This proves \(|S|\ge6\).

Every colour class of a majority C-colouring of \(H_3\) has induced minimum degree at least three. Since \(|V(H_3)|=27\), there are at most \(\lfloor27/6\rfloor=4\) colour classes.

**A four-colour construction.** Write a vertex as \((a,b,c)\in\{0,1,2\}^3\). Partition the \(27\) vertices into the following four nonempty classes:
\[
\begin{aligned}
A&=\{(a,b,2):a,b\in\{0,1,2\}\},\\
B&=\{(a,b,0):a\in\{0,1,2\},\ b\in\{0,1\}\},\\
C&=\{(a,b,1):a\in\{0,1,2\},\ b\in\{0,1\}\},\\
D&=\{(a,2,c):a\in\{0,1,2\},\ c\in\{0,1\}\}.
\end{aligned}
\]
The class \(A\) induces \(K_3\square K_3\), with internal degree four at every vertex. Each of \(B,C,D\) induces \(K_3\square K_2\), with internal degree three. Thus every vertex has at least three monochromatic neighbours, proving \(\overline\chi_{\ge}(H_3)\ge4\). Together with the preceding upper bound, this proves the exact equality.

**Odd-dimensional lifting.** Given \(r\ge0\), write every vertex of \(H_{2r+3}\) as
\[
(a,b,c,u_1,v_1,\ldots,u_r,v_r),
\]
with all coordinates in \(\{0,1,2\}\). Assign to this vertex the colour
\[
(\varphi(a,b,c),u_1,\ldots,u_r),
\]
where \(\varphi\) is the four-colour assignment just defined. All \(4\cdot3^r\) colour tuples occur. Each vertex has at least three same-coloured neighbours within its first three coordinates and exactly two same-coloured neighbours from varying each freely coloured \(v_i\). Thus it has at least \(3+2r=2r+3\) monochromatic neighbours. Its total degree is \(2(2r+3)\), so the majority condition holds. The stated lower bound follows. \(\square\)

## Verification

Run `python3 checker.py` in the package directory. This standalone Python 3 script builds the graph from the Hamming-distance-one definition, exhaustively checks that none of the \(101583\) vertex subsets of sizes one through five has induced minimum degree three, confirms the four explicit classes have respective sizes \(9,6,6,6\) and minimum internal degrees \(4,3,3,3\), and independently verifies the lifted colourings for dimensions \(3,5,7,9\). The script prints `VERIFY_OK` on success. The infinite-dimensional assertion and the sharp upper bound do not depend on the finite verification; they are proved above.

## Relationship to prior work

Bujtás, Dettlaff, Furmańczyk, and Laskowska introduced majority C-colouring in April 2026. Their subsequent work on Cartesian products (first public version August 27, 2026) determines the invariant for two-dimensional Hamming graphs and even-dimensional balanced Hamming graphs, and for odd-dimensional ternary Hamming graphs gives the general lower bound \(3^{\lfloor d/2\rfloor}\). Its stronger odd-dimensional construction assumes alphabet sizes five or at least seven, and it explicitly asks for the missing cases in odd dimensions. The exact ternary three-dimensional value and the bound above are not consequences of those statements without the new four-class construction and six-vertex obstruction.

The 2010 article by Bujtás, Sampathkumar, Tuza, Pushpalatha, and Vasundhara R. C. identifies the equivalent improper C-colouring formalism and proves general Cartesian-product bounds, together with exact binary-hypercube values. That article does not present this ternary three-cube value. More general product inequalities explain how the dimension-three construction can be lifted, but they do not supply the needed four-colour base case.

## Limitations

The exact answer is proved only for dimension three. In higher odd dimensions the theorem proves a lower bound, not its optimality, and it does not classify or enumerate all optimal colourings. Searches of accessible literature and mathematical finding records did not locate the same exact ternary case or its resulting infinite lower bound, but absence from such searches is not proof of historical novelty; independent priority assessment remains outstanding.

## References

1. C. Bujtás, M. Dettlaff, H. Furmańczyk and A. Laskowska, *Majority C-coloring in Cartesian products*, arXiv:2608.27669, first posted 2026-08-27, Sections 1.2, 2.3, 4. https://arxiv.org/abs/2608.27669
2. C. Bujtás, M. Dettlaff, H. Furmańczyk and A. Laskowska, *Majority C-coloring of graphs*, arXiv:2604.20752, first posted 2026-04-22. https://arxiv.org/abs/2604.20752
3. C. Bujtás, E. Sampathkumar, Z. Tuza, L. Pushpalatha and R. C. Vasundhara, *Improper C-colorings of graphs*, Discrete Applied Mathematics 159 (2011), 174–186. https://doi.org/10.1016/j.dam.2010.11.004
