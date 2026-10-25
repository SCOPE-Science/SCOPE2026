# Sharp monitoring edge-geodetic number of all rectangular discrete tori

## Finding
For every pair of integers \(5\le m\le n\), the Cartesian product of cycles satisfies
\[
\operatorname{meg}(C_m\square C_n)=3n=3\max\{m,n\}.
\]
Here \(\operatorname{meg}(G)\) is the least number of observation vertices such that deleting any edge of \(G\) increases the distance between some pair of observation vertices. An explicit optimal set uses exactly three observations in each of the \(n\) columns. This extends the previously proved square-torus equality to every rectangular torus with both cycle lengths at least five.

## Assumptions and scope
All graphs are finite, simple, undirected, connected, and unweighted. For \(r\ge5\), write \(C_r\) for the cycle with vertex set \(\mathbb Z/r\mathbb Z\), with adjacent residues differing by one. A pair \(u,v\) monitors an edge \(e\) if every shortest \(u\)-\(v\) path uses \(e\); equivalently, \(d_{G-e}(u,v)>d_G(u,v)\). A monitoring edge-geodetic (MEG) set monitors every edge. Let \(L_r=\lfloor(r-1)/2\rfloor\). A cyclic gap is the positive clockwise distance between consecutive selected residues, including the closing gap. Both cycle lengths are at least five; no claim is made for triangles or four-cycles.

## Proof
**1. Cycle characterization.** A subset \(U\subseteq V(C_r)\), for \(r\ge5\), is a MEG set if and only if all its cyclic gaps have length at most \(L_r\). If every gap is shorter than half the cycle, the arc between its consecutive selected endpoints is their unique shortest path, monitoring every edge of that arc. Conversely, if a selected-free gap has length at least half the cycle, no shortest path between selected vertices can traverse any edge of that gap: such a path would need to traverse the entire gap, which is longer than the other route or, at exact half-length, tied with it. Hence no edge of that gap is monitored. In particular, a cycle needs at least three selected vertices, since one pair cannot monitor both complementary routes; three approximately evenly spaced vertices suffice.

**2. Product criterion and lower bound.** Let \(S\) lie in the vertex set \(\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z\). An edge parallel to the first coordinate can be monitored only by a selected pair with the same second coordinate: if both coordinates differ, the two orders of traversing Cartesian factors give shortest paths with no common edge. When the second coordinate agrees, precisely the first-coordinate shortest paths are relevant. Thus \(S\) is a MEG set of \(C_m\square C_n\) exactly when every fixed-second-coordinate section is a MEG set of \(C_m\), and every fixed-first-coordinate section is a MEG set of \(C_n\). Because there are \(n\) second-coordinate sections and each requires at least three vertices, \(|S|\ge3n\).

**3. Balanced construction outside two small rectangles.** Put
\[
g=\left\lceil\frac m3\right\rceil,\qquad
T=\left\{0,\left\lceil\frac m3\right\rceil,\left\lceil\frac{2m}3\right\rceil\right\}\subset\mathbb Z/m\mathbb Z.
\]
The three positive cyclic gaps of \(T\) have maximum \(g\), and \(g\le L_m\). For each column \(j\in\{0,\ldots,n-1\}\), put \(a_j=\lfloor jm/n\rfloor\), and select exactly the three vertices
\[
(i,j)\quad\text{with}\quad i\equiv a_j+t\pmod m,\qquad t\in T.
\]
Every column is a rotation of \(T\), hence a cycle-MEG section. Fix a row \(i\). Its selected columns are exactly the indices \(j\) for which \(a_j\in i-T\pmod m\). Every label \(x\in\mathbb Z/m\mathbb Z\) occurs, since \(n\ge m\); its consecutive index block begins at \(\lceil xn/m\rceil\) and ends at \(\lceil(x+1)n/m\rceil-1\), interpreted cyclically. Consecutive relevant labels are separated by some positive label gap \(d\le g\). The index gap between the last occurrence of one and the first occurrence of the next is at most
\[
\left\lceil\frac{(d-1)n}{m}\right\rceil+1
\le B(m,n):=\left\lceil\frac{(g-1)n}{m}\right\rceil+1.
\]
To bound this by \(L_n\), first note \(B(m,m)=g\le L_m\). Also \(B(m,m+1)=g+1\le L_{m+1}\) for every \(m\ge6\) except \(m=7\). These inequalities follow directly from \(g=\lceil m/3\rceil\); the latter fails only for \(m=5,7\) among integers \(m\ge5\). Since \(2(g-1)<m\), one has \(B(m,n+2)\le B(m,n)+1\), whereas \(L_{n+2}=L_n+1\). The base cases therefore prove \(B(m,n)\le L_n\) for every \(m\ge6\), \(m\ne7\), and \(n\ge m\). For \(m=5\), the two bases \(n=7,8\) give \(B=3=L_n\); for \(m=7\), the bases \(n=9,10\) give \(B=4=L_n\). Induction in increments of two covers all subsequent \(n\). Consequently, outside \((m,n)=(5,6),(7,8)\), every row also meets the cycle gap criterion. The construction has exactly \(3n\) selected vertices.

**4. Two exceptional construction templates.** For \((m,n)=(5,6)\) or \((7,8)\), use the following explicitly labeled binary matrices, with rows indexed by the first cyclic coordinate, columns by the second, and `X` indicating selection:

```
(5,6):
.X.X.X
XXX.X.
X.XXXX
.X.X.X
X.X.X.

(7,8):
X.X..X..
.X.XX..X
X.X..XX.
.X..X..X
X..X..X.
..XX.X.X
.X..X.X.
```
Each column contains three selected cells and its three cyclic row gaps are at most \(L_m\). The selected column positions of each row have cyclic gaps at most \(L_n\). Both statements are finite direct checks; the separate verifier repeats them and independently tests the original shortest-path definition. These matrices have exactly \(3n\) selected cells.

By the product criterion, all constructed sets monitor every edge. The lower bound \(3n\) proves equality for every stated pair of dimensions. \(\square\)

## Verification
The standalone file `verify_rectangular_torus.py` checks the constructed cyclic-gap certificates on 1,936 parameter pairs with \(5\le m\le36\) and \(m\le n\le80\). Independently, it compares the gap characterization with the original edge-deletion distance definition for all 4,064 cycle subsets with \(5\le r\le11\). Finally, it directly verifies 1,422 distinct edges across 14 rectangular tori under shortest-path distance changes. The recorded output is in `verification_output.txt`. These finite checks test the proof and exceptions but do not replace the infinite argument.

## Relationship to prior work
Haslegrave [1, Theorem 1] proved the Cartesian-product section criterion and sharp universal upper and lower bounds. In [1, Theorem 4], he proved the special square case \(\operatorname{meg}(C_m\square C_m)=3m\) for \(m\ge5\) using three diagonal stripes. The general bounds alone leave a gap of \(3m-9\) between the lower and upper bounds when \(m\le n\); the square construction does not directly address unequal cycle lengths. The balanced-floor placement above closes this gap for every rectangle. Dev et al. [2] analyze cycles and ordinary grids and supply related monitoring foundations, but the inspected relevant sections do not state this rectangular-torus equality. A separate product-networks article [3] advertises other graph-product types; its full text was not available for checking, so literature-priority uncertainty remains.

## Limitations
Only the cardinality of an optimal MEG set and one explicit construction are established; the number or structure of **all** optimal placements is not determined. The statement assumes two ordinary cycles of lengths at least five and applies to the Cartesian product, not the strong product. The proof does not claim independent validation or exhaustive bibliographic priority.

## References
[1] J. Haslegrave, *Monitoring edge-geodetic sets: hardness and graph products*, arXiv:2210.08955 (first posted 2022-10-17), especially Theorems 1 and 4; Discrete Applied Mathematics 340 (2023), 79–84. https://arxiv.org/abs/2210.08955

[2] S. R. Dev, S. Dey, F. Foucaud, K. Narayanan and L. R. Sulochana, *Monitoring edge-geodetic sets in graphs*, Discrete Applied Mathematics 377 (2025), 598–610. https://doi.org/10.1016/j.dam.2025.08.041

[3] X. Xu, C. Yang, G. Bao, A. Zhang and X. Shao, *Monitoring-edge-geodetic sets in product networks*, International Journal of Parallel, Emergent and Distributed Systems 39 (2024), 264–277. https://doi.org/10.1080/17445760.2024.2301929
