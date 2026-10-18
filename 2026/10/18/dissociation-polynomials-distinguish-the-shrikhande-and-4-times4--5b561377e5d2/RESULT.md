# Dissociation polynomials distinguish the Shrikhande and \(4\times4\) rook graphs

## Finding
Let \(R=K_4\square K_4\) be the rook graph and let \(S\) be the Shrikhande graph. Although these nonisomorphic graphs both have strongly regular parameters \((16,6,2,2)\), hence identical adjacency spectra, their complete dissociation polynomials are
\[
\begin{aligned}
D_R(z)&=1+16z+120z^2+384z^3+528z^4+144z^5,\\
D_S(z)&=1+16z+120z^2+384z^3+544z^4+240z^5+32z^6.
\end{aligned}
\]
Consequently
\[
D_S(z)-D_R(z)=16z^4(1+6z+2z^2),\quad D_R(1)=1193,\quad D_S(1)=1337.
\]
The dissociation numbers, namely the largest sizes of vertex subsets inducing maximum degree at most one, are \(5\) and \(6\) respectively, with \(144\) and \(32\) maximum sets. In particular, neither the dissociation polynomial nor the dissociation number is determined by the strongly regular parameter tuple or adjacency spectrum, even within this fixed pair. This is a distinction between two already known nonisomorphic graphs, not a claim that they were previously indistinguishable by all other invariants.

## Assumptions and scope
All graphs are finite, simple, undirected and loopless. Write \(V=(\mathbb Z/4\mathbb Z)^2\). The rook graph joins two distinct pairs \((a,b)\) and \((c,d)\) exactly when \(a=c\) or \(b=d\). The Shrikhande graph joins them when their difference belongs to
\[
\{(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)\}\pmod 4.
\]
A dissociation set \(X\subseteq V(G)\) satisfies \(\deg_{G[X]}(v)\leq1\) for each \(v\in X\). Define
\[
D_G(z)=\sum_{X\subseteq V(G):\,\Delta(G[X])\leq1}z^{|X|},
\]
including the empty set. All coefficients in the finding are exact counts of labeled vertex subsets for the stated two graphs on sixteen vertices; no assertion is made for arbitrary strongly regular graphs or larger Hamming/Doob families.

## Proof
**Common strongly regular data.** Both adjacency specifications have sixteen vertices and exactly six neighbors per vertex. The included reproducible checker verifies by exact comparison of every pair that any two distinct vertices have exactly two common neighbors (whether adjacent or nonadjacent). Therefore both graphs have parameters \((16,6,2,2)\), implying a common characteristic polynomial and eigenvalue multiset \(\{6^1,2^6,(-2)^9\}\). Their neighborhoods are two disjoint triangles in the rook case and a six-cycle in the Shrikhande case, so they are not isomorphic.

**Exhaustive finite recurrence.** For an arbitrary induced vertex set \(W\subseteq V(G)\), let \(F_G(W;z)\) enumerate dissociation sets contained in \(W\). For any \(v\in W\), write \(N_W(v)=N_G(v)\cap W\). Partition every allowed subset into the three mutually exclusive possibilities: \(v\) is absent; \(v\) is present and has no selected neighbor; or \(v\) is present and has precisely one selected neighbor \(u\in N_W(v)\). In the third case both \(u\) and \(v\) have exhausted their permitted selected degree. The resulting exact recurrence is
\[
\begin{aligned}
F_G(W;z)={}&F_G(W\setminus\{v\};z)
 +zF_G(W\setminus(\{v\}\cup N_W(v));z)\\
&+z^2\sum_{u\in N_W(v)}F_G\big(W\setminus(\{u,v\}\cup N_W(u)\cup N_W(v));z\big),
\end{aligned}
\]
with \(F_G(\varnothing;z)=1\). The partition is exhaustive and uniquely identifies \(u\), so the recurrence has no overcounting and uses only strictly smaller vertex sets. It constitutes a finite induction proof for every coefficient computed from the explicit graph adjacency specifications.

**Exact evaluation certificate.** Evaluate that recurrence on all sixteen vertices of each specified graph using bit masks and integer polynomial arrays, with pivot the least indexed remaining vertex. The exact outputs are the two polynomials displayed above. For an independent calculation, enumerate every integer mask \(0\le m<2^{16}\); accept \(m\) exactly when each selected vertex has at most one selected neighbor, and increment the bin indexed by its selected-vertex count. This second, definition-based algorithm returns the same coefficient arrays. The full source of both algorithms, graph constructors and equality checks is supplied as `verify_dissociation.py`; it takes no data files and uses only the Python standard library. The reproducible output is in `verification_output.txt`.

**Extremal and first-disparity consequences.** The computed arrays have last nonzero terms \(144z^5\) and \(32z^6\), respectively, proving the claimed maxima and multiplicities. In the rook graph every size-five dissociation set contains exactly two induced disjoint edges and one isolated vertex; in the Shrikhande graph every size-six dissociation set contains three induced disjoint edges, as verified exhaustively. Explicit maximum-size witnesses, with coordinate representatives \(0,1,2,3\), are
\[
\begin{aligned}
X_R&=\{(0,2),(0,3),(1,1),(2,0),(3,0)\},\\
X_S&=\{(0,2),(0,3),(1,1),(2,0),(2,2),(3,0)\}.
\end{aligned}
\]
The coefficients agree in degrees \(0\) through \(3\) and first diverge at degree \(4\). Specifically, any graph with sixteen vertices, degree six, and two common neighbors per adjacent pair has exactly \(16\cdot6\cdot2/6=32\) triangles. Its size-three dissociation-set count equals \(\binom{16}{3}-16\binom62+2(32)=384\): each vertex-centered three-vertex path is excluded, and the triangle correction accounts for the three possible centers. Size-one and size-two coefficients depend only on the order. Thus the initial agreement follows from shared strongly regular data; the degree-four difference exhibits genuinely finer information.

## Verification
Run `python3 verify_dissociation.py` using Python 3.8 or later; it needs no nonstandard dependencies or downloads. The implementation checks all \(65536\) vertex subsets of **each** graph, independently evaluates the exact recursive polynomial, checks the common strongly regular parameters, and verifies an alternative Shrikhande coordinate presentation by an invertible transformation of \((\mathbb Z/4\mathbb Z)^2\). The terminal line is `VERIFICATION_OK masks_per_graph=65536 methods=brute_and_recurrence graphs=rook_shrikhande`. The recorded output contains both complete coefficient arrays and the counts of large admissible sets grouped by induced-edge number. The recurrence proves the correctness of the finite exhaustive computation; no inference from a limited sample to an infinite graph family is made.

## Relationship to prior work
Tu, Xiao and Lang's 2023 research article establishes dissociation-polynomial terminology and upper bounds for **cubic** graphs. The two graphs here are both **six-regular**, so that article's cubic bound cannot imply their coefficients. An accessible calculation of the **ordinary independence complexes** of the same two graphs gives distinct independent-set polynomials and sphere-wedge homotopy types, but the independent-set condition \(\Delta=0\) and independence-complex homotopy type do not determine the present counts with \(\Delta\leq1\). Familiar results on the Shrikhande/rook strongly regular pair establish shared spectral data but not these dissociation arrays. Consequently the asserted addition is a distinct two-polynomial exact comparison, not a discovery of the graph pair, their spectra, their ordinary independence polynomials, or a general strongly-regular-graph characterization.

## Limitations
This is a fully finite theorem for two specific sixteen-vertex graphs. All claims of exact coefficients are reproducible via complete enumeration and independent recurrence, not through a closed form valid for all graph orders. An equivalent calculation might exist in an unindexed table or earlier article; the searches performed cannot prove absolute literature uniqueness. The scientific assessment is not independent external peer review.

## References
1. J. Tu, J. Xiao and R. Lang, *Counting the number of dissociation sets in cubic graphs*, AIMS Mathematics **8** (2023), 10021–10032; first available on the publisher's site 23 February 2023; DOI: 10.3934/math.2023507, https://www.aimspress.com/article/doi/10.3934/math.2023507.
2. A. E. Brouwer and W. H. Haemers, *Spectra of Graphs*, Springer, 2012. Standard strongly regular graphs and the Shrikhande/rook example.
3. E. W. Weisstein, *Shrikhande Graph*, MathWorld, https://mathworld.wolfram.com/ShrikhandeGraph.html (graph identity and classical properties).
