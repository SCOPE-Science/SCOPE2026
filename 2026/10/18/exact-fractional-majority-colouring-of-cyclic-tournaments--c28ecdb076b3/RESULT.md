# Exact fractional majority colouring of cyclic tournaments

## Finding
For every odd integer \(n\geq 3\), let \(T_n\) be the standard cyclic (carousel) tournament on \(\mathbb Z/n\mathbb Z\), with arc \(i\to j\) exactly when \(1\leq (j-i)\bmod n\leq (n-1)/2\). Define \(k=\lfloor(n-1)/4\rfloor\). Then its largest majority-stable vertex-set has cardinality \(2k+1\), and its fractional majority colouring number is
\[
\chi^*_{\mathrm{maj}}(T_n)=\frac{n}{2\lfloor(n-1)/4\rfloor+1}=\begin{cases}(4k+1)/(2k+1),&n=4k+1,\\(4k+3)/(2k+1),&n=4k+3.\end{cases}
\]
Its ordinary majority chromatic number is \(2\) for \(n\equiv1\pmod4\) and \(3\) for \(n\equiv3\pmod4\). Thus the fractional optimum alternates strictly below and above \(2\) in the two residue classes (except neither class has equality), approaching \(2\) as \(n\) grows.

## Assumptions and scope
The digraph is loopless and has exactly one directed arc between each distinct vertex pair. The positive outdegree of every vertex of \(T_n\) equals \(m=(n-1)/2\). For any \(S\subseteq V(T_n)\), call \(S\) *majority-stable* when every \(v\in S\) has at most \(\lfloor m/2\rfloor\) outneighbours in \(S\). A fractional majority colouring assigns a nonnegative real weight \(w_S\) to every majority-stable set, covering each vertex with total weight at least one; its value is \(\sum_S w_S\), and \(\chi^*_{\mathrm{maj}}\) is the minimum value. The ordinary majority chromatic number is the least number of vertex classes in a partition into majority-stable sets. The result holds without a primality assumption and includes \(n=3\).

## Proof
Put \(k=\lfloor m/2\rfloor\). If \(S\) is a majority-stable set of size \(s>0\), every vertex in \(T_n[S]\) has internal outdegree at most \(k\). Since the subtournament contains exactly one arc per unordered vertex pair,
\[
\frac{s(s-1)}2=\sum_{v\in S}d^+_{T_n[S]}(v)\leq sk.
\]
Therefore \(s\leq2k+1\), regardless of the particular arcs between vertices of \(S\).

To attain the bound when \(n=4k+1\) (necessarily \(k\geq1\)), take the even residues \(S=\{0,2,4,\ldots,4k\}\). In their cyclic order there are \(2k+1\) successive gaps, all \(2\) except one gap \(1\). From each chosen vertex the first \(k\) chosen successors have clockwise distance at most \(2k=m\), while the \((k+1)\)-st chosen successor, if present, has distance at least \(2k+1>m\). Thus exactly \(k\) outneighbours of each selected vertex lie in \(S\). In particular \(S\) is majority-stable and has \(2k+1\) vertices.

When \(n=4k+3\) and \(k\geq1\), take the odd residues \(S=\{1,3,5,\ldots,4k+1\}\). Its \(2k+1\) cyclic gaps are all \(2\) except for one gap \(3\). The next \(k\) selected successors from any selected vertex have distance at most \(2k+1=m\), while the next \(k+1\) selected successors, if present, have distance at least \(2k+2>m\). Every chosen vertex therefore has exactly \(k\) outgoing arcs within \(S\). For \(n=3\) (\(k=0\)), a singleton is majority-stable. Hence for all odd \(n\geq3\), the maximum stable-set size is \(a=2k+1\).

Every fractional colouring has total weight at least \(n/a\): summing its vertex-cover constraints gives
\[
n\leq\sum_{v\in V(T_n)}\sum_{S\ni v}w_S=\sum_S |S|w_S\leq a\sum_Sw_S.
\]
Conversely, fixing a majority-stable set \(S\) of size \(a\), consider its \(n\) cyclic translates \(S+t\) for \(t\in\mathbb Z/n\mathbb Z\). Translation preserves the tournament and majority-stability. Each vertex occurs in exactly \(a\) of the translates (counting translates by their shift), so assigning weight \(1/a\) to every translate gives unit coverage and total weight \(n/a\); if any translated subsets coincide, their weights are summed. This achieves the lower bound and proves the fractional formula.

For the ordinary chromatic number when \(n=4k+1\), the complement \(U\) of the even-residue set consists of the \(2k\) odd residues. In cyclic order its gaps are all \(2\) except one gap \(3\). A vertex in \(U\) can have at most its first \(k\) successors within clockwise distance \(m=2k\), because any \((k+1)\)-st successor is at distance at least \(2k+2\). Therefore \(U\) is also majority-stable. These two classes give a majority \(2\)-colouring. A single colour cannot work, because every vertex has \(m>\lfloor m/2\rfloor\) outneighbours in the full graph.

When \(n=4k+3\), every majority-stable set has at most \(2k+1\) vertices, and two such sets cannot cover \(4k+3>4k+2\) vertices. At least three colours are required. After choosing the exhibited majority-stable \(S\) with \(2k+1\) vertices, partition its \(2k+2\)-vertex complement into two parts of size \(k+1\). Each part is automatically majority-stable because its internal outdegrees are at most \(k\). This is a \(3\)-colouring, completing the proof.

## Verification
The companion Python 3 program `check_majority.py` uses the explicit arc rule independently of the counting proof. It exhaustively examines \(174{,}760\) vertex subsets for the eight odd orders from \(3\) through \(17\), checks the proposed maximum size, verifies the rotational incidence certificate, and tests the ordinary-colouring witnesses. It also checks the constructive witnesses for all \(250\) odd orders from \(3\) through \(501\). A separate numerical linear-programming calculation on all majority-stable sets confirmed the fractional value for each odd order from \(3\) through \(13\). These finite calculations are corroboration; the all-order assertions follow from the counting and constructive arguments above. Run the embedded checker as `python3 check_majority.py`.

## Relationship to prior work
Kreutzer, Oum, Seymour, van der Zypen and Wood introduced majority colouring of directed graphs and its fractional version, obtaining a general four-colour theorem. Anastos, Lamaison, Steiner and Szabó gave general fractional bounds and a probabilistic treatment of majority-stable sets; neither their statements nor their mechanisms evaluate this cyclic-tournament family. Ben-Ameur and Maddaloni established improved universal and tournament bounds, together with approximation and hardness results; the inspected text concerns these general classes rather than the present exact vertex-transitive calculation. Gacitúa Fuentes and coauthors proved integral colouring results for concave-round digraphs. This paper's new claim is the exact fractional optimum and explicit optimal orbit-weight certificate on all odd standard cyclic tournaments, not priority over prior general or integral-colouring theorems. A related previously published cyclic-tournament result on *acyclic dichromatic number* concerns transitive colour classes and does not imply the asserted majority-stable fractional optimum.

## Limitations
The result concerns the standard consecutive-outneighbour cyclic tournament, not arbitrary circulant tournaments, round digraphs or general vertex-transitive tournaments. The integer chromatic number is included as a proved consequence, but the principal novelty assertion concerns the fractional calculation. Only published and accessible sources could be compared: a potentially relevant 2025 concave-round-tournament article was identifiable bibliographically, but its complete text could not be inspected. An independently discovered equivalent formula under alternative terminology remains a residual priority risk. No claim of independent validation or optimality of algorithms for arbitrary digraphs is made.

## References
1. W. Ben-Ameur and A. Maddaloni, *Fractional majority coloring of digraphs: bounds and inapproximability*, arXiv:2610.11997v1 (publicly posted 2026-10-08), https://arxiv.org/abs/2610.11997.
2. M. Anastos, A. Lamaison, R. Steiner and T. Szabó, *Majority Colorings of Sparse Digraphs*, arXiv:1911.01954, https://arxiv.org/abs/1911.01954.
3. S. Kreutzer, S. Oum, P. Seymour, D. van der Zypen and D. R. Wood, *Majority colourings of digraphs*, arXiv:1608.03040, https://arxiv.org/abs/1608.03040.
4. C. Gacitúa Fuentes, N. Jara Cádiz, P. Opazo Salazar, N. Sanhueza-Matamala and C. Thraves Caro, *Partitioning problems in concave-round digraphs and tournaments*, Procedia Computer Science 273 (2025), 117–124, DOI:10.1016/j.procs.2025.10.288 (complete text not inspected).
