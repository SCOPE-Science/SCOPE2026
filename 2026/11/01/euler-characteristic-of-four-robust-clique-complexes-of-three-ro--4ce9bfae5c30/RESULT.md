# Euler characteristic of four-robust clique complexes of three-row grids

## Finding
For each integer \(n\ge2\), let \(G_n=P_3\square P_n\) be the graph on the \(3\times n\) rectangular nearest-neighbor grid. Define the four-robust clique complex
\[
K_n=\{S\subseteq V(G_n):\alpha(G_n[S])\le3\},
\]
including the empty face. Then its **reduced integral Euler characteristic** is
\[
\boxed{\widetilde\chi(K_n)=-\binom{2n-2}{3}.}
\]
In particular, for widths \(n=2,3,4,5,6\), the respective values are \(0,-4,-20,-56,-120\). Equivalently the complete alternating face count satisfies
\[
\sum_{S\in K_n}(-1)^{|S|}=\binom{2n-2}{3}.
\]
The assertion is an exact all-width characteristic formula, **not** a claim that \(K_n\) is a wedge of five-spheres. If that conjectured wedge homotopy holds at any width, the formula forces its number of five-sphere summands to be \(\binom{2n-2}{3}\).

## Assumptions and scope
The paths have respectively three and \(n\) vertices, with Cartesian adjacency and no wraparound. An independent set in an induced graph contains no edge; \(\alpha\) is the maximum size of such a set. Every subset \(S\) of the grid vertices is considered, and its sign is \((-1)^{|S|}\), including \(S=\varnothing\). No assumption about shellability, torsion, or homotopy type is made.

## Proof
**Exact column states.** Encode the three vertices in one column by bits \(1,2,4\), with row-adjacency \(1\)--\(2\)--\(4\). The possible independent masks in a column are
\[
T=(0,1,2,4,5).
\]
A selected subset of the first \(j\) columns is represented by a tuple \(d=(d_t)_{t\in T}\). Here \(d_t\) is the largest cardinality of an independent set contained in the selected vertices, with *exactly* mask \(t\) in its final column, truncated at \(4\); it is \(-1\) if no such set exists. Initially \(d=(0,-1,-1,-1,-1)\) for the empty grid. Truncation is sound because extending a grid cannot decrease the independence number, and selected subsets with independence number at least four are excluded from \(K_n\).

**Transition and signed sum.** Append a selected-column mask \(s\in\{0,\ldots,7\}\). For \(t\in T\), put \(d'_t=-1\) when \(t\not\subseteq s\); otherwise set
\[
d'_t=\min\bigl(4,\,|t|+\max\{d_u:u\in T,\ d_u\ge0,\ u\cap t=\varnothing\}\bigr),
\]
with value \(-1\) if the maximization set is empty. The disjointness condition is exactly the horizontal edge restriction on independent sets in consecutive columns, so the formula follows by separating an independent set at its last column. Reject the transition if \(\max_t d'_t\ge4\). Each surviving transition carries sign \((-1)^{|s|}\), and the signed product along a length-\(n\) path is exactly \((-1)^{|S|}\) for its unique selected grid subset \(S\).

**Finite integer certificate for all widths.** The complete breadth-first reachability calculation from the initial state produces exactly \(54\) states and \(260\) surviving unaggregated transitions; these counts are not input assumptions, but are enumerated by `verify_transfer.py`. Let \(A\) be the resulting \(54\times54\) integer signed transition matrix, let \(e\) select the initial state, and let \(\mathbf1\) be the all-ones vector. By the bijection above,
\[
t_n:=\sum_{S\in K_n}(-1)^{|S|}=e^\mathsf{T}A^n\mathbf1.
\]
The standalone exact-integer calculation constructs \(A\) from the displayed rules and verifies **each of the 54 integer components** of the identity
\[
\boxed{A(A-I)^{4}\mathbf1=0.}
\]
This is a finite, exhaustive algebraic identity; the source program verifies its full vector, not merely values of \(t_n\) for a finite sample of widths. Consequently, for every \(n\ge1\), the fourth forward difference of \(t_n\) is zero. The exact initial values are \(t_1=0\), \(t_2=0\), \(t_3=4\), and \(t_4=20\). The unique polynomial of degree at most three agreeing with these four values is \(\binom{2n-2}{3}\). Therefore the asserted formula holds for all \(n\ge2\).

**Euler sign.** For a finite complex including the empty face, \(\widetilde\chi(K_n)=-\sum_{S\in K_n}(-1)^{|S|}\); this proves the boxed result. The proof uses only exact integers, finite state enumeration, and an algebraic annihilation identity.

## Verification
Run `python3 verify_transfer.py` from the directory containing this result. It constructs the full automaton, asserts the state/transition counts, evaluates all \(54\) components of \(A(A-I)^4\mathbf1\), checks the initial values, and independently propagates signed forward counts for widths \(1\) through \(30\). Run `python3 verify_direct.py` for an independent direct grid-vertex subset enumeration at widths \(2\) through \(6\), using recursive independence numbers rather than the column automaton. Both scripts require only Python 3 with a standard-library integer `bit_count` method.

## Relationship to prior work
Filakovský, *The Topology of \(k\)-Robust Clique Complexes in Grid-like Graphs* (first posted February 11, 2026), proves the wedge homotopy classification of rectangular-grid robust complexes for \(k=2\) and \(k=3\). Its arbitrary-\(k\) theorem concerns square sequences built exclusively by edge gluing; its discussion explicitly leaves \(k>3\) with corner gluing unresolved. Three-row rectangular grids with multiple squares use corner gluing. The present result computes a distinct missing topological invariant at the first unresolved parameter, \(k=4\), for all widths, without asserting a stronger homotopy type.

Kim and Lew introduced this complex in the notation \(I_k(G)\) and studied collapsibility bounds; those results do not provide this enumerative formula. Chandrakar, Hazra, Rout and Singh's total-cut results concern the \(k=3\) three-row grid and other restricted cases. The current computation can equally be interpreted as information about the Alexander-dual total-four-cut complexes, but no homotopy equivalence is inferred from Euler characteristic alone.

## Limitations
The assertion is specialized to three rows and \(k=4\). The exact fourth-difference certificate proves Euler characteristic only: it does **not** determine Betti numbers separately, integral torsion, attaching maps, shellability, or the full conjectured wedge decomposition. The electronic enumeration is a finite exact identity used in an all-width proof, not an attempt to infer the infinite theorem from finite experiments. An equivalent unindexed derivation may exist; independent external mathematical review has not been performed.

## References
1. M. Filakovský, *The Topology of \(k\)-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365, first public posting 2026-02-11; Theorem 1, Corollary 3 and Conjecture 5, and Section 3. https://arxiv.org/abs/2602.11365
2. M. Kim and A. Lew, *Complexes of graphs with bounded independence number*, arXiv:1912.12605; Israel Journal of Mathematics 249 (2022), 83–120. https://arxiv.org/abs/1912.12605
3. H. Chandrakar, N. R. Hazra, D. Rout and A. Singh, *Topology of total cut and cut complexes of grid graphs*, arXiv:2408.07646. https://arxiv.org/abs/2408.07646
