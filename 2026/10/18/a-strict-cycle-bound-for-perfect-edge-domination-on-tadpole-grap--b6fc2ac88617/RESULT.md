# A strict cycle bound for perfect edge domination on tadpole graphs

## Finding

Let \(T_{c,t}\) be the graph formed by adjoining to one vertex of a cycle \(C_c\) a pendant path consisting of \(t\) new vertices. For a finite simple graph \(G\), let \(p(G)\) be the number of **perfect edge dominating sets**: edge subsets \(P\subseteq E(G)\) for which every edge outside \(P\) is adjacent (shares an endpoint) to exactly one edge in \(P\). Then, for **every** pair of integers \(c\ge3\) and \(t\ge1\),

\[
p(T_{c,t})<p(C_{c+t}).
\]

The difference has an exact, positive, two-dimensional recurrence. Write
\[
d_{c,t}=p(C_{c+t})-p(T_{c,t}).
\]
Then
\[
\begin{aligned}
d_{c,t}&=d_{c-1,t}+d_{c-3,t} &&(c\ge6,\ t\ge1),\\
d_{c,t}&=d_{c,t-1}+d_{c,t-3} &&(c\ge3,\ t\ge4),
\end{aligned}
\]
with all nine initial values given exactly by
\[
\bigl(d_{c,t}\bigr)_{c=3,4,5;\,t=1,2,3}=
\begin{pmatrix}2&3&4\\2&5&7\\4&6&9\end{pmatrix}.
\]
Thus the formula determines the deficit for arbitrarily long cycles and tails, not merely finitely many orders.

## Assumptions and scope

Graphs are finite, undirected, simple and unweighted. The cycle has \(c\) distinct vertices and edges; the attached path has \(t\) new vertices and \(t\) edges, meeting the cycle only at its initial vertex. Consequently \(T_{c,t}\) has \(c+t\) vertices and is connected and unicyclic. The edge set itself counts as a perfect edge dominating set. The claim concerns **counts of all** such sets, not the smallest size of one and not perfect vertex domination. It does not claim the cycle bound for arbitrary connected or arbitrary unicyclic graphs.

## Proof

**1. Three-color encoding.** For any perfect edge dominating set \(P\) of a connected graph with at least two vertices, color each vertex \(W,Y,B\) according as it is incident with zero, one, or at least two edges of \(P\). No edge may have two white ends (it would be undominated), and no edge with two nonwhite ends may lie outside \(P\) (it would meet two distinct selected edges). Therefore \(P\) consists precisely of edges having both ends nonwhite. The coloring is valid precisely under the local rules

* \(W\): all neighbors have color \(Y\);
* \(Y\): exactly one neighbor is nonwhite;
* \(B\): every neighbor is nonwhite and the vertex has degree at least two.

Conversely these rules reconstruct a unique perfect edge dominating set. Indeed, each omitted edge has one white end, and its nonwhite end is yellow and is incident with exactly one selected edge. This proves the bijection.

**2. A fixed matrix controls the cycle length.** On degree-two vertices, adjacent colors belong to the ordered six-state set
\[
\mathcal S=((W,Y),(Y,W),(Y,Y),(Y,B),(B,Y),(B,B)).
\]
For states \((a,b)\) and \((b,d)\), permit the transition exactly when the degree-two rule holds for the middle vertex \(b\) with neighbors \(a,d\). The resulting transfer matrix (rows and columns indexed by \(\mathcal S\)) is
\[
M=\begin{pmatrix}
0&0&1&1&0&0\\
1&0&0&0&0&0\\
0&1&0&0&0&0\\
0&0&0&0&1&1\\
0&1&0&0&0&0\\
0&0&0&0&1&1
\end{pmatrix}.
\]
A direct integer matrix multiplication gives the exact identity
\[
M^5=M^4+M^2. \tag{1}
\]
In a cycle \(C_n\), each of its \(n\) vertices has degree two, so closed state walks are in bijection with valid colorings, and \(p(C_n)=\operatorname{tr}(M^n)\) for \(n\ge3\).

For the tadpole, enumerate valid colors on the \(t\)-vertex tail while retaining the colors at the two cycle neighbors of its attachment vertex. More precisely, let \(v_0,v_1,\ldots,v_{c-1}\) be the cyclic vertices and let \(H_t[j,i]\) count tail colorings which satisfy the three-neighbor rule at \(v_0\), all tail-vertex rules, and compatibility with \(i=(\operatorname{col}(v_0),\operatorname{col}(v_1))\), \(j=(\operatorname{col}(v_{c-1}),\operatorname{col}(v_0))\). This is a fixed nonnegative integer matrix for each \(t\), independent of \(c\). The remaining \(c-1\) degree-two vertices are counted by \(M^{c-1}\); thus
\[
p(T_{c,t})=\operatorname{tr}(M^{c-1}H_t). \tag{2}
\]
Identity (1), applied to (2), yields
\[
p(T_{c,t})=p(T_{c-1,t})+p(T_{c-3,t})\qquad(c\ge6).
\]
The same identity gives \(p(C_n)=p(C_{n-1})+p(C_{n-3})\) whenever \(n\ge6\). Subtracting proves the first recurrence for \(d_{c,t}\).

**3. The pendant-tail recurrence.** For an arbitrary graph \(H\) with a leaf \(x\), attach three new vertices \(a,b,z\) in the order \(x-z-b-a\). Let \(G'\) be the full extension and \(G=G'-a\). Partition valid three-colorings of \(G'\) by the colors near the new leaf. The exhaustive cases are: \(a=W,b=Y\), which are in bijection with valid colorings of \(G\) having \(b=Y\); \(a=Y,b=Y,z=W\), corresponding to valid colorings of \(H\) with \(x=Y\); \(a=Y,b=B,z=Y\), corresponding to colorings of \(H\) with \(x=W\); and \(a=Y,b=B,z=B\), corresponding to colorings of \(G\) with \(b=W\), by recoloring \(b\) white and \(z\) yellow. All transformations are reversible under the local rules. Since \(x\) and \(b\) are leaves of \(H\) and \(G\), respectively, neither can be black. Hence
\[
p(G')=p(G)+p(H). \tag{3}
\]
Taking \(H=T_{c,t-3}\) (which has a leaf for \(t\ge4\)) makes \(G'=T_{c,t}\) and \(G=T_{c,t-1}\), proving
\[
p(T_{c,t})=p(T_{c,t-1})+p(T_{c,t-3})\qquad(t\ge4).
\]
The cycle recurrence and \(c+t\ge7\) then imply the second deficit recurrence.

**4. Complete finite bases and positivity.** Direct evaluation of the same local coloring rules for \(c=3,4,5\) and \(t=1,2,3\) gives
\[
\bigl(p(T_{c,t})\bigr)=\begin{pmatrix}
3&3&6\\4&5&8\\6&9&12
\end{pmatrix}.
\]
The corresponding cycle counts \(p(C_n)\) for \(n=4,5,6,7,8\) are \(5,6,10,15,21\). These yield exactly the nine positive deficit values in the statement. For each \(t=1,2,3\), strong induction on \(c\), using the first recurrence and these three cycle-length bases, proves \(d_{c,t}>0\) for all \(c\ge3\). Now fix any such \(c\). Strong induction on \(t\ge4\), using the second recurrence and the already-positive three tail-length bases, proves \(d_{c,t}>0\) for every \(t\ge1\). This completes both the exact recurrence classification and the strict inequality.

## Verification

The attached standalone `verify.py` uses only Python's standard library. It independently constructs the six-state matrix, multiplies the integer matrices to check (1), explicitly enumerates valid tail colorings for (2), reconstructs the nine bases, and exhaustively enumerates **edge subsets** (rather than vertex colorings) for cycles of lengths \(3\) through \(10\) and tadpoles with those cycle lengths and tails of lengths \(1\) through \(5\). It also tests both recurrences on wider finite ranges. Execution exits with assertion failure on any discrepancy. Its last line reports success; see `VERIFICATION.md` for the precise replay statement. Finite checks are corroboration; the all-parameter proof is the bijection, exact matrix identity, tail-extension bijection and two inductions above.

## Relationship to prior work

Grippo, Lin, Moyano and Vera (2026, arXiv:2607.03894v1) define the same perfect-edge-domination count, prove its path recurrence and a cycle recurrence, and explicitly conjecture that the cycle maximizes this count among **all connected graphs** on a fixed number of vertices (Conjecture 5.1). They establish the relevant comparison for trees, but not for arbitrary connected unicyclic graphs. Their general counting algorithm for generalized series-parallel graphs, a class containing tadpoles, does not itself provide the strict two-parameter inequality or the exact deficit recurrences shown here. The elementary pendant-path extension in step 3 is a reconstructed form of their Proposition 2.5, not claimed as a new lemma in isolation. Their source date is 2026-07-04 UTC.

Grippo, Lin and Vera (arXiv:2509.04598, first version 2025-09-04) provide algorithms for perfect edge domination in \(P_6\)-free graphs; they do not give this infinite-family inequality for pendant paths of unbounded length. The originality claim is restricted to this explicit tadpole specialization of the 2026 open conjecture, and the bivariate deficit determination.

## Limitations

The proof treats a single pendant path, not arbitrary rooted trees attached to a cycle, multiple pendant paths, or all unicyclic and connected graphs. The general extremal conjecture remains open. The provenance comparison is literature/database based rather than a proof of global uniqueness in all unpublished or unindexed materials.

## References

1. L. N. Grippo, M. C. Lin, V. Moyano, C. Vera, *Counting perfect edge dominating sets: extremal results and linear-time algorithms*, arXiv:2607.03894v1 (2026-07-04), Sections 2.2–2.3 and 5; https://arxiv.org/html/2607.03894v1 .
2. L. N. Grippo, M. C. Lin, C. Vera, *Perfect Edge Domination in \(P_6\)-free Graphs and in Graphs Without Efficient Edge Dominating Sets*, arXiv:2509.04598v1 (2025-09-04); https://arxiv.org/html/2509.04598v2 .
