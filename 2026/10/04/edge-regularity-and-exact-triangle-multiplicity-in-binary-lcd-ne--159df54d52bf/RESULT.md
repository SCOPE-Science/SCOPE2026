# Edge-regularity and exact triangle multiplicity in binary LCD neighbor graphs

## Finding
Let \(\Gamma_{n,k}\) be the graph whose vertices are the \(k\)-dimensional binary linear complementary dual (LCD) subspaces of \(\mathbb F_2^n\), with two vertices adjacent when their intersection has dimension \(k-1\). For every \(n\ge2\) and \(1\le k\le n-1\), every edge of \(\Gamma_{n,k}\) has exactly
\[
\lambda_{n,k}=2^k+2^{{n-k}}-4
\]
common neighbors. Thus \(\Gamma_{n,k}\) is edge-regular.

Its degree is
\[
d_{n,k}=(2^k-1)(2^{{n-k}}-1),
\]
so every vertex belongs to exactly
\[
\frac12(2^k-1)(2^{{n-k}}-1)(2^k+2^{{n-k}}-4)
\]
triangles, and the total number of triangles is
\[
\frac{{|V(\Gamma_{{n,k}})|}}6(2^k-1)(2^{{n-k}}-1)(2^k+2^{{n-k}}-4).
\]

## Assumptions and scope
The ambient space is \(V=\mathbb F_2^n\) with the standard Euclidean bilinear form \(B(x,y)=x\cdot y\). A subspace \(C\le V\) is LCD exactly when the restriction of \(B\) to \(C\) is nondegenerate, equivalently \(C\cap C^\perp=0\). The neighbor relation is the usual Grassmann relation \(\dim(C\cap D)=k-1\), restricted to LCD subspaces.

The theorem concerns the binary Euclidean LCD graph only. It does not assert the same common-neighbor parameter over odd fields, for Hermitian LCD codes, or for the associated-neighbor subgraph.

## Proof
We first need an extension count.

**Extension lemma.** Let \(H\le V\) have dimension \(k-1\), and suppose that \(H\) is contained in at least one LCD \(k\)-subspace. Then exactly \(2^{{n-k}}\) LCD \(k\)-subspaces contain \(H\).

Because \(H\) is a hyperplane of a nondegenerate \(k\)-space, its radical has dimension at most one.

If \(\operatorname{{rad}}H=0\), then \(V=H\perp H^\perp\). Every \(k\)-space containing \(H\) is uniquely \(H\perp\langle x\rangle\) for a nonzero \(x\in H^\perp\), and it is nondegenerate exactly when \(B(x,x)=1\). In characteristic two, \(x\mapsto B(x,x)\) is a linear functional. The assumed LCD extension makes this functional nonzero on the \(n-k+1\)-dimensional space \(H^\perp\), so exactly \(2^{{n-k}}\) vectors satisfy \(B(x,x)=1\).

If \(\operatorname{{rad}}H=\langle r\rangle\), choose a complement \(K\) of \(\langle r\rangle\) in \(H\). Then \(B|_K\) is nondegenerate. For an extension \(E=H+\langle x\rangle\), replace \(x\) by the unique representative \(x'\in x+K\) orthogonal to \(K\). On \(\langle r,x'\rangle\) the Gram matrix is
\[
\begin{{pmatrix}}0&B(r,x')\\ B(r,x')&B(x',x')\end{{pmatrix}},
\]
which is nonsingular exactly when \(B(r,x)=1\). The functional \(x+H\mapsto B(r,x)\) on the \(n-k+1\)-dimensional quotient \(V/H\) is nonzero because an LCD extension exists; hence exactly \(2^{{n-k}}\) extension cosets give LCD spaces. This proves the lemma.

Now fix an edge \(CD\) of \(\Gamma_{n,k}\) and put \(H=C\cap D\) and \(W=C+D\). Thus \(\dim H=k-1\) and \(\dim W=k+1\). Let \(E\) be a common neighbor of \(C\) and \(D\). If \(E\cap C=E\cap D\), that common hyperplane is \(H\), so \(H\subset E\). Otherwise the two distinct hyperplanes \(E\cap C\) and \(E\cap D\) span \(E\), and both lie in \(W\), so \(E\subset W\). Hence every common neighbor is of one of two types:

1. **Star type:** \(H\subset E\). By the extension lemma there are \(2^{{n-k}}\) LCD extensions of \(H\); after removing \(C,D\), this gives \(2^{{n-k}}-2\) candidates.
2. **Top type:** \(E\subset W\). Orthogonal complementation sends these to LCD \(n-k\)-subspaces containing \(W^\perp=C^\perp\cap D^\perp\). Applying the extension lemma in dimension \(n-k\) gives \(2^k\) such spaces; after removing \(C,D\), this gives \(2^k-2\) candidates.

It remains to show that the two candidate sets do not overlap. In the two-dimensional quotient \(W/H\), there are exactly three one-dimensional subspaces. Two correspond to \(C/H\) and \(D/H\); let \(E_0/H\) be the third.

If \(H\) is nondegenerate, choose \(x,y\in H^\perp\) with \(C=H\perp\langle x\rangle\) and \(D=H\perp\langle y\rangle\). Since \(C,D\) are LCD, \(B(x,x)=B(y,y)=1\). The third extension is \(E_0=H\perp\langle x+y\rangle\), but in characteristic two
\[
B(x+y,x+y)=B(x,x)+B(y,y)=0,
\]
so \(E_0\) is degenerate.

If \(\operatorname{{rad}}H=\langle r\rangle\), write \(C=H+\langle x\rangle\) and \(D=H+\langle y\rangle\). The extension lemma criterion gives \(B(r,x)=B(r,y)=1\). Hence \(B(r,x+y)=0\), so \(r\) lies in the radical of the third extension \(E_0=H+\langle x+y\rangle\). Again \(E_0\) is not LCD.

Therefore the star and top common-neighbor sets are disjoint, and
\[
|N(C)\cap N(D)|=(2^{{n-k}}-2)+(2^k-2)=2^k+2^{{n-k}}-4.
\]
This proves edge-regularity.

Finally, an LCD \(k\)-space has \(2^k-1\) hyperplanes. For each hyperplane, the extension lemma supplies \(2^{{n-k}}-1\) other LCD extensions, and each neighbor has a unique intersection hyperplane. Thus
\[
d_{{n,k}}=(2^k-1)(2^{{n-k}}-1).
\]
Every triangle containing a fixed vertex is counted twice by its two incident edges, giving \(d_{{n,k}}\lambda_{{n,k}}/2\) triangles through each vertex. Dividing the vertex-incidence count by three gives the total-triangle formula.

## Verification
The accompanying `verify_lcd_triangles.py` exhaustively enumerates every subspace of \(\mathbb F_2^n\) for \(2\le n\le6\), filters LCD subspaces by exact Gram-matrix rank, constructs every neighbor graph, and checks the claimed degree, the common-neighbor count on every edge, and the resulting total triangle count. It ends with `VERIFY_OK`.

The finite enumeration is corroborative only; the proof above establishes the theorem for all \(n\) and \(k\) in the stated range.

## Relationship to prior work
De la Cruz, Horlemann, Newman, Vela Cabello, and Willems introduced and analyzed the LCD neighbor graph. Their 2026 preprint proves the number of LCD neighbors of a fixed LCD code, regularity and connectedness of the graph, and regularity or biregularity of its main orthogonal-group orbit subgraphs. Its conclusion summarizes those results without a triangle-count or adjacent-common-neighbor theorem.

An earlier public presentation of the same project on 5 June 2025 explicitly listed “Count triangles” as ongoing work after giving regularity, connectedness, diameter, and girth results. The theorem above supplies an exact all-parameter answer for the binary Euclidean LCD graph: not only the global triangle count but the stronger edge-regularity statement from which that count follows.

## Limitations
The argument uses characteristic two in the crucial cancellation \(B(x+y,x+y)=B(x,x)+B(y,y)\). No claim is made here for odd \(q\), where square classes and the two orthogonal orbits affect extension counts. The result also does not determine common-neighbor structure for nonadjacent LCD codes, so it does not assert strong regularity.

## References
1. J. de la Cruz, A.-L. Horlemann, M. Newman, C. Vela Cabello, W. Willems, “The Neighbor Graph of Linear Complementary Dual (LCD) Codes,” arXiv:2609.07580v1, 2026. https://arxiv.org/abs/2609.07580
2. C. Vela, “The Neighbor Graph of Linear Complementary Dual Codes,” 5th Pythagorean Conference, 5 June 2025. https://cargo.wlu.ca/5thPythagorean/talks/Carlos_Vela.pdf
