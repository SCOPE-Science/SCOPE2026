# Maximum Grundy total dominating sequences of heterogeneous windmills
## Finding
Let
\[
W(m_1,\ldots,m_r)=K_1\vee\bigl(K_{m_1}\cup\cdots\cup K_{m_r}\bigr),
\]
where \(r\ge 2\) and every \(m_i\ge 2\). Write \(c\) for the universal center and \(B_i\) for the vertex set of the \(i\)-th peripheral clique. A Grundy total dominating sequence is a longest legal sequence for open neighborhoods.

The scalar equality
\[
\gamma_{\mathrm{gr}}^t\bigl(W(m_1,\ldots,m_r)\bigr)=2r
\]
is already implied by the published modular-decomposition rules for Grundy total domination and is not claimed as new here. The new statement is a complete classification and enumeration of the maximum sequences and their underlying vertex sets.

Every maximum sequence is exactly one of the following two types.

1. **Peripheral type.** It contains no center and contains exactly two vertices from every \(B_i\). Every ordering of those \(2r\) vertices is legal.
2. **Center-terminal type.** It contains \(c\) as its last term. For one unique index \(j\), it contains exactly one vertex from \(B_j\), and it contains exactly two vertices from every \(B_i\) with \(i\ne j\). Every ordering of the \(2r-1\) peripheral terms, followed by \(c\), is legal.

Consequently the number of distinct maximum Grundy total dominating sets is
\[
M(W)=
\prod_{i=1}^r\binom{m_i}{2}
+
\sum_{j=1}^r m_j\prod_{\substack{i=1\\i\ne j}}^r\binom{m_i}{2},
\]
and the number of ordered maximum Grundy total dominating sequences is
\[
Q(W)=
(2r)!\prod_{i=1}^r\binom{m_i}{2}
+
(2r-1)!\sum_{j=1}^r m_j\prod_{\substack{i=1\\i\ne j}}^r\binom{m_i}{2}.
\]
For the equal-blade windmill \(K_1\vee rK_m\), these specialize to
\[
M(W)=\binom{m}{2}^{r}+rm\binom{m}{2}^{r-1}
\]
and
\[
Q(W)=(2r)!\binom{m}{2}^{r}+(2r-1)!rm\binom{m}{2}^{r-1}.
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. The parameters satisfy \(r\ge2\) and \(m_i\ge2\). A sequence \((v_1,\ldots,v_k)\) is legal for open neighborhoods when, for each \(i\),
\[
N(v_i)\setminus\bigcup_{h<i}N(v_h)\ne\varnothing.
\]
It is total dominating when the union of the open neighborhoods of all selected vertices is the whole vertex set. The result concerns sequences of maximum possible length and the vertex sets supporting them; it does not enumerate shorter legal or total dominating sequences.

## Proof
For a peripheral vertex \(x\in B_i\),
\[
N(x)=\{c\}\cup(B_i\setminus\{x\}).
\]
If \(x,y\in B_i\) are distinct, then
\[
N(x)\cup N(y)=\{c\}\cup B_i.
\]
Hence after two vertices from the same blade have appeared, no third vertex of that blade can footprint a new vertex. Every legal sequence therefore contains at most two vertices from each \(B_i\).

Suppose the center \(c\) appears after at least one peripheral vertex. Any earlier peripheral vertex already totally dominates \(c\). When \(c\) is selected, its open neighborhood is the entire peripheral vertex set, so all vertices are then totally dominated. Thus no later term can be legal. In a maximum sequence of length at least four, the center, if present, must therefore be last. If the center is first, one peripheral vertex can subsequently footprint \(c\), after which the graph is totally dominated, so such a sequence has length only two and is not maximum because \(r\ge2\).

A center-free legal sequence has at most \(2r\) terms. This bound is attained by choosing two vertices from every blade. Indeed, before the first chosen vertex of \(B_i\) appears, no earlier term from another blade has totally dominated any vertex of \(B_i\). The first chosen vertex of \(B_i\) therefore footprints the other chosen vertex (and possibly further vertices of the blade). The second chosen vertex of \(B_i\) footprints the first, because a vertex does not belong to its own open neighborhood and vertices from other blades are nonadjacent to it. This argument is independent of the interleaving of the blades, so every ordering of the selected \(2r\) vertices is legal. Two selected vertices in every blade mutually totally dominate one another and dominate the rest of their blade, while every selected peripheral vertex dominates \(c\); hence the resulting sequence is total dominating.

Now consider a maximum sequence containing \(c\). The center is last, so there are \(2r-1\) peripheral terms before it. Since at most two can come from each of the \(r\) blades, exactly one blade contributes one vertex and every other blade contributes two. Conversely, choose such a set. Any ordering of its peripheral vertices is legal by the same first/second-vertex argument. In the unique one-vertex blade, that selected vertex is still not totally dominated before the last step: vertices from other blades are nonadjacent to it, and there is no second selected vertex in its blade. The terminal center therefore footprints that vertex and completes total domination. This proves the classification.

For peripheral type, the selected set can be chosen in \(\prod_i\binom{m_i}{2}\) ways, and each supports all \((2r)!\) orderings. For center-terminal type, choosing the deficient blade \(j\), its single peripheral vertex, and two vertices from every other blade gives
\[
\sum_j m_j\prod_{i\ne j}\binom{m_i}{2}
\]
sets, and each supports all \((2r-1)!\) peripheral orderings followed by \(c\). Summing gives the two formulas.

## Verification
A standalone verifier exhaustively constructs the graph and, for each vertex subset, counts legal open-neighborhood orderings by subset dynamic programming. A subset is accepted as a maximum set only when one of its legal orderings totally dominates the graph. The verifier compares the exhaustive maximum length, the complete maximum-set classification, the number of maximum sets, the per-set ordering multiplicities, and the total number of maximum sequences against the formulas above.

The checked profiles comprise all \(m_i\in\{2,3\}\) for \(2\le r\le4\), together with several profiles containing a blade of size \(4\). Replay output was:

`VERIFY_OK profiles=33 subset_masks=49151 append_checks=278544 classification_checks=5633 maximum_set_checks=2130 sequence_checksum=17321556 max_order=13`

The finite replay is a boundary and implementation check; the all-parameter statement is established by the proof above.

## Relationship to prior work
Brešar, Henning, and Rall introduced Grundy total domination in 2016. Brešar, Kos, Nasini, and Torres subsequently gave exact disjoint-union and join rules and a modular-decomposition algorithm. Their Proposition 4.1 makes the parameter additive over disjoint union, and Proposition 4.2 determines it under graph join. Applied to
\[
K_1\vee\bigl(K_{m_1}\cup\cdots\cup K_{m_r}\bigr),
\]
those rules already imply the scalar value \(2r\). Accordingly, the scalar is treated here as covered prior work.

The inspected foundational and modular-decomposition texts do not give the two-type classification above, do not count the maximum vertex sets, and do not count their legal orderings. Searches using the aliases “windmill,” “friendship graph,” “clique bouquet,” “Grundy total domination,” and “total dominating sequences” did not locate an equivalent same-object enumeration. Later work on graphs whose total dominating sequences all have the same length studies a different question and does not supply these formulas.

## Limitations
The theorem requires at least two blades and at least two peripheral vertices in every blade. Stars, the one-blade complete-graph boundary, shorter total dominating sequences, and graph families obtained by attaching nonclique blocks are outside the claim. The scalar maximum length is prior-implied; only the structural classification and exact extremizer counts are asserted as new. As with any literature search, a poorly indexed equivalent enumeration under different terminology remains a residual originality risk.

## References
1. B. Brešar, M. A. Henning, and D. F. Rall, “Total Dominating Sequences in Graphs,” arXiv:1601.07525, first submitted 2016-01-27; Discrete Mathematics 339 (2016), 1665–1676, DOI 10.1016/j.disc.2016.01.017.
2. B. Brešar, T. Kos, G. Nasini, and P. Torres, “Total dominating sequences in trees, split graphs, and under modular decomposition,” arXiv:1608.06804, first submitted 2016-08-24.
3. S. Bahadır, D. Gözüpek, and O. Doğan, “On graphs all of whose total dominating sequences have the same length,” Discrete Mathematics 344 (2021), 112492, DOI 10.1016/j.disc.2021.112492.
