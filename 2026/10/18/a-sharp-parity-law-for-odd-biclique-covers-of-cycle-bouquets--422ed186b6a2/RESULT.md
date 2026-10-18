# A sharp parity law for odd biclique covers of cycle bouquets

## Finding

Let \(G=C_{\ell_1}\vee\cdots\vee C_{\ell_t}\) be the one-vertex union of \(t\ge1\) simple cycles, with \(\ell_i\ge3\): all cycles have one common vertex \(h\), and no two share any other vertices or edges. Let \(o\) be the number of odd lengths among \(\ell_1,\ldots,\ell_t\), and put
\[
s=\sum_{i=1}^t\left\lfloor\frac{\ell_i-1}{2}\right\rfloor.
\]
Then
\[
\boxed{\operatorname{rank}_{\mathbf F_2} A(G)=2s,\qquad b_2(G)=s+(o\bmod 2).}
\]
In particular, the odd-cover rank bound is attained exactly when \(o\) is even. For the friendship graph \(F_t\), obtained by identifying one vertex in \(t\) triangles, the formula becomes \(b_2(F_t)=t+(t\bmod 2)\).

## Assumptions and scope

All graphs are finite and simple. An *odd biclique cover* of \(G\) is a family of pairs of disjoint nonempty vertex sets \((X_j,Y_j)\); the complete bipartite edge sets \(X_j\times Y_j\), interpreted as undirected edges, have symmetric difference precisely \(E(G)\). Edges of \(G\) must therefore occur an odd number of times, and nonedges an even number of times. \(b_2(G)\) is the least family size. Bicliques may contain edges outside \(G\) provided that these cancel modulo two. No two petals of the bouquet share any vertex except \(h\). Every integer \(t\ge1\) and every sequence \(\ell_i\ge3\) is covered; no regularity or parity condition is assumed.

## Proof

**Binary adjacency rank.** Delete the common vertex \(h\). What remains is a disjoint union of paths on \(N_i=\ell_i-1\) vertices. Over \(\mathbf F_2\), write the adjacency matrix as
\[
A(G)=\begin{pmatrix}0&b^{\mathsf T}\\b&D\end{pmatrix},\quad
D=\bigoplus_i A(P_{N_i}),
\]
where on each path \(b\) has ones precisely at its two endpoints. The path adjacency matrix \(A(P_N)\) has rank \(2\lfloor N/2\rfloor\): for even \(N\) its determinant is one modulo two by the continuant recurrence, whereas for odd \(N\) its kernel is spanned by the vector with ones at the odd-numbered path positions and zeros elsewhere. In the odd case the endpoint vector is orthogonal to this kernel, since both endpoints occupy odd-numbered positions. In the even case the matrix is invertible. Consequently, on every path the endpoint vector belongs to the column space, and \(b=Dy\) for some peripheral vector \(y\).

Replacing the hub basis vector by its sum with the peripheral vector \(y\) is an invertible congruence operation. It kills the hub-to-periphery entries; its hub diagonal entry remains zero because symmetric adjacency matrices with zero diagonal are alternating over \(\mathbf F_2\). Thus \(A(G)\) is congruent to \(0\oplus D\), which has rank \(2s\). Every biclique adjacency matrix has rank at most two, so \(b_2(G)\ge s\).

**Parity obstruction at equality.** The bouquet is Eulerian: every non-hub vertex has degree two and the hub degree is \(2t\). Hence the all-ones vector \({\bf1}\) satisfies \(A(G){\bf1}=0\). Assume an odd cover of size exactly \(s\) exists. Form its vertex-versus-partite-set incidence matrix \(M\), with \(2s\) columns (one column for each side of each biclique), and let \(J\) be the invertible block diagonal matrix with \(s\) copies of \(\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\). Then \(A(G)=MJM^{\mathsf T}\). Rank \(A(G)=2s\) implies that \(M\) has full column rank. From \(0=A(G){\bf1}=MJ(M^{\mathsf T}{\bf1})\), injectivity of \(M\) and invertibility of \(J\) imply \(M^{\mathsf T}{\bf1}=0\). Thus **both sides of every biclique have even cardinality**. Such a biclique has an even number of edges, and the symmetric difference of all of them must also have an even number of edges. Yet \(|E(G)|=\sum_i\ell_i\equiv o\pmod2\). If \(o\) is odd, this is impossible; hence \(b_2(G)\ge s+1\).

**Optimal construction.** Start with a triangle for every odd petal and a square for every even petal, all sharing hub \(h\). Pair up the odd triangles. For each paired pair with peripheral vertices \(a,b\) on one triangle and \(c,d\) on the other, take exactly two bicliques with sides \((\{b,d\},\{h,c\})\) and \((\{a,c\},\{h,b\})\). Their edge sets differ symmetrically exactly on the six edges of the two triangles: the unwanted edge \(bc\) appears twice and cancels. If one odd triangle is left unpaired, cover it with the two bicliques \((\{h\},\{a,b\})\) and \((\{a\},\{b\})\). Cover each square \(h,a,b,d,h\) with a single biclique \((\{h,b\},\{a,d\})\).

To extend any base petal, replace a peripheral-rim edge \(uv\) by the path \(u,x,y,v\), with \(x,y\) new vertices, and add one biclique with sides \((\{u,y\},\{x,v\})\). Its four edges are \(ux,xy,yv,uv\): the old \(uv\) cancels and the three new edges appear, leaving the rest of the graph unchanged. Repeating this two-vertex expansion creates any prescribed length of the same parity, with one extra biclique per expansion. An odd petal of length \(\ell\) needs \((\ell-3)/2\) expansions; an even petal needs \((\ell-4)/2\). The base costs and expansions total precisely
\[
2\lfloor o/2\rfloor+2(o\bmod2)+(t-o)
+\sum_{\ell_i\text{ odd}}\frac{\ell_i-3}{2}
+\sum_{\ell_i\text{ even}}\frac{\ell_i-4}{2}
=s+(o\bmod2).
\]
This matches the lower bounds in both parity cases and proves the theorem. \(\square\)

## Verification

The standalone `verify_bouquets.py` creates the asserted biclique families, reconstructs the symmetric-difference edge set, and independently computes binary adjacency ranks. It verified 1,484 bouquets with up to four petals, individual lengths between three and eight, and at most 24 vertices. A separate exhaustive enumeration of all bicliques on up to seven vertices checks the exact optimum on ten small bouquets; it directly rules out covers with fewer than four bicliques when the mathematical lower bound is four. The finite computations are supporting tests; the proof above is for the entire infinite family. Run `python verify_bouquets.py` with Python 3 and no third-party packages.

## Relationship to prior work

Buchanan, Clifton, Culver, Nie, O'Neill, Rombach, and Yin introduced the binary-rank lower bound and studied even cores and odd covers of cycles [1]. Buchanan et al. [2, §2–3] obtained a parity obstruction via even cores and an exact formula for **disjoint unions** of cycles (Theorem 8). They also noted the butterfly (two triangles sharing a vertex) as a smallest strict example of an odd-cover advantage over biclique partitioning [2, §1]. Neither that isolated butterfly nor their disjoint-union theorem determines the optimum for arbitrary one-vertex unions; identifying all cycle hubs changes the graph and the parity obstruction. Specifically, their disjoint-union formula incurs one extra biclique whenever there is at least one odd cycle, whereas a cycle bouquet incurs the extra biclique **only if the number of odd petals is odd**. The congruence-based rank computation and the paired-petal construction together establish this distinction.

## Limitations

The result concerns a single common articulation vertex shared by all cycles; general cactus graphs whose cycles meet at different articulation vertices are not classified. The exact formula counts minimum **bicliques**, not the number of distinct minimum covers. Related or later unindexed publications may exist; absence of a match in searched literature alone is not a proof of uniqueness.

## References

[1] C. Buchanan, A. Clifton, E. Culver, J. Nie, J. O'Neill, P. Rombach, M. Yin, *Odd Covers of Graphs*, arXiv:2202.09822 (first public 20 February 2022). https://arxiv.org/abs/2202.09822

[2] C. Buchanan, A. Clifton, E. Culver, P. Frankl, J. Nie, K. Ozeki, P. Rombach, M. Yin, *On odd covers of cliques and disjoint unions*, arXiv:2408.08598 (first public 16 August 2024). https://arxiv.org/abs/2408.08598
