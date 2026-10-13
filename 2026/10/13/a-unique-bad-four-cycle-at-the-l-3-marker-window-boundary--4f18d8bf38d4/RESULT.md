# A unique bad four-cycle at the \(L=3\) marker-window boundary
## Finding

Extend Wang's one-dimensional marker-window graph to the first excluded parameter \(L=3\). Put
\[
Q=[-6,6]\cap\mathbb Z.
\]
A vertex is a subset \(D\subseteq Q\) such that distinct points of \(D\) have distance greater than \(3\), and every point of \([-3,3]\cap\mathbb Z\) is within distance \(3\) of \(D\). Two vertices are adjacent when, for some \(g\in\{-1,+1\}\),
\[
D\cap(g+Q)=(g+E)\cap Q.
\]
For an oriented edge \(D\to E\), call this \(g\) its canonical direction.

At \(L=3\), every edge still has a unique canonical direction. The graph has exactly \(59\) vertices, \(75\) edges, and \(4\) simple four-cycles. Exactly one simple four-cycle has nonzero total canonical direction:
\[
D_0=\{-5,-1,3\},
\quad
D_1=\{-4,0,4\},
\quad
D_2=\{-3,1,5\},
\quad
D_3=\{-6,-2,2,6\},
\]
with
\[
D_0\to D_1\to D_2\to D_3\to D_0
\]
having direction sequence
\[
(-1,-1,-1,-1)
\]
and total
\[
-4.
\]

The other three simple four-cycles have total direction \(0\). Any closed four-walk with a repeated vertex in a loopless simple graph contains immediate backtracking, and antisymmetry of edge directions makes its total \(0\). Hence this displayed cycle is the unique obstruction, up to rotation and reversal, to Wang's zero-sum four-walk property for the canonical \(L=3\) labeling.

Wang proves the same canonical marker-window labeling has the zero-sum property for every \(L\ge4\). Therefore the hypothesis \(L\ge4\) cannot be weakened to \(L\ge3\) for that canonical labeling.

## Assumptions and scope

The statement concerns the one-dimensional marker-window graph obtained by applying Wang's definition verbatim at \(L=3\), although Lemma 7.3 in the source is stated only for \(L\ge4\).

The conclusion is about the **canonical** direction of an edge, namely its translation witness \(g\in\{-1,+1\}\). It does not claim that the underlying graph \(M_{1,3}\) admits no other, noncanonical edge-direction assignment satisfying Wang's two abstract properties.

A simple four-cycle is counted up to cyclic rotation and reversal. The exact census is finite: \(Q\) has \(13\) points, so every possible vertex is among \(2^{13}\) subsets.

## Proof

First note that canonical directions are well-defined at \(L=3\). If \(g,h\in\{-1,+1\}\) both witness an oriented edge \(D\to E\), choose \(a\in D\cap[-3,3]\), which exists by coverage of \(0\). The overlap equations put both \(a-g\) and \(a-h\) in \(E\). Their distance is at most \(2\), while distinct points of \(E\) have distance greater than \(3\). Thus \(a-g=a-h\), so \(g=h\).

Now consider
\[
D_0=\{-5,-1,3\},\quad
D_1=\{-4,0,4\},\quad
D_2=\{-3,1,5\},\quad
D_3=\{-6,-2,2,6\}.
\]
Consecutive points in each set differ by \(4\), so each set is \(3\)-separated. Direct inspection of the radius-\(3\) intervals around their points shows that every integer from \(-3\) through \(3\) is covered. Hence all four sets are vertices.

For \(g=-1\), one has \(g+Q=[-7,5]\). The four overlap identities are
\[
D_0\cap[-7,5]=\{-5,-1,3\}=(-1+D_1)\cap[-6,6],
\]
\[
D_1\cap[-7,5]=\{-4,0,4\}=(-1+D_2)\cap[-6,6],
\]
\[
D_2\cap[-7,5]=\{-3,1,5\}=(-1+D_3)\cap[-6,6],
\]
and
\[
D_3\cap[-7,5]=\{-6,-2,2\}=(-1+D_0)\cap[-6,6].
\]
Thus each oriented edge in the displayed closed four-walk has canonical direction \(-1\). Its total is therefore
\[
-1-1-1-1=-4\neq0,
\]
so Wang's property that every closed four-walk has zero direction sum fails at \(L=3\).

For the exact census, the included verifier enumerates all \(2^{13}\) subsets of \(Q\), retains exactly those satisfying separation and coverage, tests every unordered pair against both possible witnesses, and then enumerates all simple four-cycles modulo rotation and reversal. It obtains
\[
|V|=59,\qquad |E|=75,\qquad N_4=4,
\]
with exactly one cycle having nonzero canonical direction sum. Because every repeated-vertex closed four-walk in a loopless simple graph reduces by backtracking, no omitted repeated walk can produce another obstruction.

Wang's proof of Lemma 7.3 establishes the zero-sum property for all \(L\ge4\). The explicit \(L=3\) obstruction therefore shows that the canonical-label bound cannot be lowered from \(4\) to \(3\).

## Verification

Running `verify.py` with the standard Python interpreter prints `VERIFY_OK` and independently reconstructs the finite graph from the definitions rather than relying on stored adjacency data. It checks all \(8192\) subsets of \(Q\), all unordered pairs of retained vertices, witness uniqueness, the complete simple-four-cycle census, and the exceptional cycle.

The hand proof above separately verifies the displayed four vertices and four overlap identities, so the central failure does not depend on the census program. The computation is used only for the exact statements that there are \(59\) vertices, \(75\) edges, \(4\) simple four-cycles, and exactly one bad simple four-cycle.

## Relationship to prior work

Wang's Lemma 7.3 constructs \(M_{d,L}\) for \(d\ge1\) and \(L\ge4\), with canonical directions given by the unique translation witnesses. The proof of the four-walk property uses both
\[
L+4\le2L
\]
and
\[
4\le L.
\]
The source does not discuss \(L=3\), does not state sharpness of the parameter \(4\), and does not give the boundary graph census above.

Earlier work of Gao, Jackson, Krohne, and Seward develops the continuous-combinatorial and tiling machinery that motivates finite target constructions for abelian group actions, but it does not contain Wang's marker-window graph \(M_{d,L}\) or this \(L=3\) boundary computation.

Wang's Proposition 7.7 uses Lemma 7.3 only in the stated regime \(L\ge4\), so the published adjacent-dimension separation theorem does not imply any behavior at the excluded value \(L=3\).

## Limitations

The result diagnoses the canonical witness labeling only. A different edge-direction assignment on the same underlying graph is not ruled out.

The result is one-dimensional. It does not classify the behavior of the analogous \(L=3\) construction in higher dimensions.

The exact census is finite and exhaustive, but it is not a claim about minimal graph size among all separators or marker constructions.

## References

Ruijun Wang, *Continuous graph homomorphisms of higher dimensional abelian group actions*, arXiv:2609.39824v1, 2026, especially Section 7.2 and Lemma 7.3.

Su Gao, Steve Jackson, Edward Krohne, and Brandon Seward, *Continuous Combinatorics of Abelian Group Actions*, arXiv:1803.03872v2, 2023.
