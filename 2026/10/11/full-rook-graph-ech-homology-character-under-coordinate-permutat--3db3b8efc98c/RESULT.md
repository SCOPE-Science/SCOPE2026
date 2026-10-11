# Full rook-graph Čech homology character under coordinate permutations and interchange

## Finding
For each integer \(q\geq3\), put \(G_q=K_q\square K_q\), with vertices \((a,b)\in[q]^2\), and let \(X_q=\mathcal N(G_q,2)\) denote the graph-geometric Čech complex of radius-one balls, equivalently the closed-neighborhood complex \(\mathcal N[G_q]\). Let \(W_q=(S_q\times S_q)\rtimes C_2\) act on the two coordinates and interchange them. Write \(f(\sigma)\) and \(t(\sigma)\) for the numbers of fixed points and two-cycles of \(\sigma\in S_q\). Let \(\iota(a,b)=(b,a)\).

**Theorem.** The only nonzero reduced rational homology of \(X_q\) is in degree \(2\), and its complete \(W_q\)-character is
\[
\begin{aligned}
\operatorname{tr}((\sigma,\tau)\mid\widetilde H_2(X_q;\mathbb Q))
 &=2\binom{f(\sigma)}2\binom{f(\tau)}2+2t(\sigma)t(\tau)
   -(f(\sigma)-1)(f(\tau)-1),\\
\operatorname{tr}((\sigma,\tau)\iota\mid\widetilde H_2(X_q;\mathbb Q))
 &=-\bigl(f(\sigma\tau)-1\bigr)^2.
\end{aligned}
\]
The \(S_q\times S_q\)-fixed subspace has dimension \(1\), coordinate interchange acts on this line by \(-1\), and consequently the full \(W_q\)-fixed subspace is zero. In particular, the homology dimension is \((q-1)^2(q^2-2)/2\); that **nonequivariant** dimension and homotopy type were already known and are not asserted to be new.

## Assumptions and scope
All graphs are finite, simple, and undirected; the distance on \(G_q\) is its shortest-path metric, extended to unit edges. The parameter \(q\) is an arbitrary integer at least \(3\). The group element \((\sigma,\tau)\iota\) sends \((a,b)\mapsto(\sigma(b),\tau(a))\), and products of permutations mean function composition. Homology is reduced over \(\mathbb Q\); the result is a complete rational character, not a claim about integral equivariant representations. The case \(q=2\) also satisfies the formulas but is outside the new family assertion.

## Proof
**1. A natural relative complex.** Write \(R_a=\{(a,b):b\in[q]\}\) and \(C_b=\{(a,b):a\in[q]\}\). Radius-one neighborhoods are exactly \(R_a\cup C_b\), and no new nerve simplices arise solely from points in the interiors of edges. Thus
\[
X_q=\bigcup_{a,b\in[q]}\Delta(R_a\cup C_b).
\]
Let \(A=\bigcup_a\Delta(R_a)\cup\bigcup_b\Delta(C_b)\), which is invariant under \(W_q\). Distinct row simplices are disjoint, distinct column simplices are disjoint, and each row simplex meets each column simplex in exactly one vertex, with no triple intersections. The nerve is the complete bipartite graph \(K_{q,q}\), so \(A\simeq K_{q,q}\), and \(H_1(A;\mathbb Q)\cong U\otimes U\) for the two coordinate permutation actions, where \(U=\{(x_i)\in\mathbb Q^q:\sum_i x_i=0\}\). Coordinate interchange reverses the row-to-column orientation of the nerve edges, so it acts on this tensor product by the **negative tensor flip**.

For a face of \(X_q\) outside \(A\), call its vertices **mixed**. A mixed face of size at least \(3\) not containing the intersection \((a,b)\) of its unique supporting row \(R_a\) and column \(C_b\) is paired with the face formed by adjoining \((a,b)\). Such a mixed face has a unique supporting cross \(R_a\cup C_b\): at least two of its vertices determine one coordinate and another determines the other coordinate. A matched upper face has the same unique support. This is an acyclic, group-equivariant discrete-Morse pairing: an alternating path cannot change its unique support; within each support all upward steps adjoin its fixed center, which cannot be followed by a distinct unmatched downward step that admits another upward match. The resulting subcomplex \(L\) consists of \(A\) and, for every unordered pair of cells \(e=\{(a,b),(c,d)\}\) with \(a\ne c\), \(b\ne d\), the mixed edge \(e\) and the two triangles
\[
T_e^+=\{(a,b),(c,d),(a,d)\},\qquad
T_e^-=\{(a,b),(c,d),(c,b)\}.
\]
(The signs here are labels for the two other rectangle corners, not fixed orientations.) In particular the equivariant relative chain complex \(C_*(L,A;\mathbb Q)\) is concentrated in degrees \(1\) and \(2\); each triangle maps to its associated edge with coefficient \(\pm1\). There are exactly two triangles over each mixed edge, so the relative boundary is surjective and
\[
H_1(L,A;\mathbb Q)=0,\qquad
H_2(L,A;\mathbb Q)=\bigoplus_{e}\mathbb Q\,z_e,
\]
where \(z_e\) is the difference of the two oriented triangles, with their mixed-edge coefficients normalized equal.

**2. The connecting map.** Each rectangle on distinct rows \(a,c\) and columns \(b,d\) has its boundary four-cycle in \(A\). It is the boundary of the two triangles associated to either diagonal mixed edge. Rectangle four-cycles generate \(H_1(K_{q,q};\mathbb Q)\): the edges of any bipartite spanning tree reduce an arbitrary cycle to these four-cycles. Therefore \(H_1(L;\mathbb Q)=0\). The equivariant long exact sequence of the pair gives the short exact sequence
\[
0\longrightarrow\widetilde H_2(X_q;\mathbb Q)
\longrightarrow H_2(L,A;\mathbb Q)
\longrightarrow H_1(A;\mathbb Q)\longrightarrow0.
\]
Also \(H_i(A;\mathbb Q)=0\) for \(i\ge2\), and \(H_i(L,A;\mathbb Q)=0\) for \(i\ge3\); hence all other reduced homology of \(X_q\) vanishes. Over characteristic zero the above sequence splits as representations, so its character is the **difference** of the two displayed characters.

**3. Character of the relative degree-two module.** For \(g=(\sigma,\tau)\), the mixed edges fixed as unordered pairs are exactly (i) the two diagonals of each rectangle with both rows and both columns fixed individually, and (ii) the two diagonals arising from one two-cycle of \(\sigma\) and one two-cycle of \(\tau\). Thus there are \(2\binom{f(\sigma)}2\binom{f(\tau)}2+2t(\sigma)t(\tau)\) fixed relative generators. Each carries **positive** sign: if \(g\) exchanges the endpoints of its diagonal, it also exchanges the two complementary corners, making the two orientation reversals cancel; otherwise both are fixed. These are the complete contributions to the relative trace.

For \(g=(\sigma,\tau)\iota\), conjugating by a permutation acting on one coordinate reduces its action to \((a,b)\mapsto(\kappa(b),a)\), where \(\kappa=\sigma\tau\). A mixed edge fixed by \(g\) consists of vertices individually fixed by \(g^2\), and so both coordinates must be among the \(f(\kappa)\) fixed symbols. On these symbols the action is coordinate interchange. Fixed diagonals are either two distinct diagonal cells fixed separately or a transpose pair of distinct off-diagonal cells, giving \(2\binom{f(\kappa)}2=f(\kappa)(f(\kappa)-1)\) fixed edges. Every associated relative generator acquires **negative** sign: it reverses either the diagonal's oriented endpoints or the two complementary corners, but not both. Therefore its relative trace is \(-f(\kappa)(f(\kappa)-1)\).

**4. Subtraction and invariants.** The pure character of \(H_1(A)\cong U\otimes U\) is \((f(\sigma)-1)(f(\tau)-1)\), while the interchanging character is \(-\operatorname{tr}(U(\sigma\tau))=-(f(\kappa)-1)\). Subtraction gives both formulas. Finally, the relative generators form one transitive signed-permutation orbit under \(S_q\times S_q\), with positive stabilizer action, so their invariant subspace is one-dimensional. The representation \(U\otimes U\) has no invariants under this subgroup. The one-dimensional invariant line in \(H_2(L,A)\) is reversed by coordinate interchange (every fixed-edge sign under swapping is negative), and so is its canonically isomorphic line in \(H_2(X_q)\). It follows that the full \(W_q\)-fixed subspace is zero.

## Verification
The standalone file `verify.py`, using only the Python standard library, constructs all nonempty faces directly from the \(q^2\) closed neighborhoods for \(q=2,3,4\). For every one of the \(2(q!)^2\) elements of \(W_q\), it computes the reduced alternating signed fixed-face trace and compares it against the stated complete character formula. Since all reduced homology is concentrated in degree \(2\), the signed Lefschetz number is the trace there. In total it verifies \(8+72+1152=1232\) elements and outputs `VERIFY_OK`. This is a finite sanity test of the independently proved all-parameter result, not an attempt to extrapolate finite data to infinity.

## Relationship to prior work
Adams–Shukla–Singh (arXiv:2212.05871, Sections 3–4) introduce and compute radius-one Čech complexes for **binary** hypercube graphs, not the full \(S_q\wr C_2\) action for general \(q\)-ary rook graphs. Antolín Camarena–Carnero Bravo (arXiv:2307.12401, Section 4) establish nonequivariant sphere-wedge topology for a related categorical-product independence complex; their Section 4 determines no full automorphism character. Matsushita (arXiv:2511.12608, Example 3.5 and Example 5.7) already identifies exactly the same closed-neighborhood object and its nonequivariant sphere-wedge rank and simple connectivity. Those established results are **not** presented as novel here. Neither inspected treatment determines the two explicit character formulas or the distinction between the invariant lines under the index-two subgroup and the full group.

## Limitations
This is a rational, not integral, representation statement; it does not classify extension classes over finite-characteristic coefficient fields. An equivariant homotopy decomposition is not claimed. Equivariant character identities can in principle be equivalent to unindexed calculations; no claim of exhaustive literature coverage or independent audit is made.

## References
1. Henry Adams, Samir Shukla, and Anurag Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871v2 (first public 2022-12-12), especially Sections 3–4. https://arxiv.org/html/2212.05871v2
2. Omar Antolín Camarena and Andrés Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401v2 (first public 2023-07-23), especially Section 4. https://arxiv.org/html/2307.12401v2
3. Takahiro Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608v2 (first public 2025-11-16), especially Examples 3.5 and 5.7. https://arxiv.org/html/2511.12608v2
