# An isolated adaptive-shattering gap for rank-two Kneser neighborhoods

## Finding
For each integer \(n\ge2\), let \(G_n=\operatorname{KG}(n,2)\) have as vertices the two-element subsets of \([n]=\{0,\ldots,n-1\}\), with adjacency exactly when the subsets are disjoint. Let \(\mathcal N_n=\{N_{G_n}(c):c\in\binom{[n]}2\}\) be its *open*-neighborhood Boolean concept class, queried at two-element subsets. Then
\[
\operatorname{VCdim}(\mathcal N_n)=
\begin{cases}
0,&2\le n\le3,\\
1,&n=4,\\
2,&n=5,\\
3,&n=6,7,\\
4,&n\ge8,
\end{cases}
\quad
\operatorname{Ldim}(\mathcal N_n)=
\begin{cases}
0,&2\le n\le3,\\
1,&n=4,\\
2,&n=5,\\
3,&n=6,\\
4,&n\ge7.
\end{cases}
\]
In particular, \(\operatorname{Ldim}(\mathcal N_n)>\operatorname{VCdim}(\mathcal N_n)\) holds **exactly at \(n=7\)**, where the graph has 21 vertices. At that order the dimensions are 4 and 3, respectively.

## Assumptions and scope
All graphs are finite, simple, and undirected; the concept associated with center \(c\) is the Boolean function \(h_c(q)=1\) precisely when \(c\cap q=\varnothing\). The center and query are always *two-element* sets, and \(h_c(c)=0\). The VC dimension is the maximum cardinality of a fixed shattered query set. The Littlestone dimension is the maximum depth of a complete binary adaptive query tree whose every root-to-leaf answer sequence is realized by at least one center. Distinct centers are allowed to define identical concepts in the low-order degenerate cases; this does not affect either dimension. An empty or singleton concept family has dimension zero. Our theorem covers every integer \(n\ge2\), including the edgeless cases \(n=2,3\).

## Proof
**A counting restriction on VC shattering.** Fix a set \(Q\) of \(d\) distinct query pairs that is shattered, and write \(S=\bigcup_{q\in Q}q\) and \(t=|S|\). The answer pattern identically one has a witness center \(c\subseteq[n]\setminus S\), hence
\[
t\le n-2.\tag{1}
\]
The pattern identically zero has a center \(\{a,b\}\) meeting each \(q\in Q\). Thus the graph on vertex set \(S\) with edge set \(Q\) has a vertex cover of cardinality at most two. Each of its \(d\) edges contributes at most one vertex other than \(a,b\), giving
\[
t\le d+2.\tag{2}
\]
For any center \(c\), the zero-query trace on \(Q\) is the union of the incidence stars of the at most two vertices in \(c\cap S\). Consequently the total number of possible zero traces is at most
\[
1+t+\binom t2.\tag{3}
\]
For \(d=5\), equations (2) and (3) yield at most \(1+7+21=29<32\) traces, excluding a shattered five-set. Since shattering is hereditary, \(\operatorname{VCdim}\le4\) for all \(n\).

To exclude a shattered four-set when \(n\le7\), use (1). For \(n\le6\), \(t\le4\), and (3) gives at most \(1+4+6=11<16\) traces. For \(n=7\), a four-set would require \(t=5\), since smaller \(t\) again gives at most 11 traces. Its four-edge query graph on five nonisolated vertices has total degree eight, so some vertex \(v\) has degree one, with unique neighbor \(u\). The zero traces from choosing the two active centers \(\{u,v\}\) and \(\{u,z\}\), where \(z\notin S\), coincide, because every query containing \(v\) also contains \(u\). There are two vertices outside \(S\), so every choice of zero, one or two active vertices is realizable by a two-element center. The collision makes the bound of 16 in (3) strict. Hence four queries are not shattered at \(n=7\).

For \(n=5\), any shattered three-set has \(t\le3\) by (1), hence at most \(1+3+3=7<8\) traces. For \(n=4\), two distinct query edges have at least three endpoints, whereas a witness to the all-one pattern would require at least two unused vertices, which is impossible. For \(n\le3\), no two pairs are disjoint, so every concept is empty.

**Matching VC witnesses.** At \(n=4\), one query \(\{0,1\}\) is shattered. At \(n=5\), the queries \(\{0,1\},\{0,2\}\) are shattered. At \(n=6\), the queries \(\{0,1\},\{0,2\},\{0,3\}\) are shattered. For the last two assertions, a desired zero set of queries is realized by selecting the common hub when all queried edges should receive zero, the one or two appropriate leaves when one or two should receive zero, and unused vertices to complete the center when needed. At \(n=8\), four queries
\[
\{0,1\},\ \{0,2\},\ \{3,4\},\ \{3,5\}
\]
are shattered. To realize arbitrary patterns, independently choose one center point from each of the two disjoint three-vertex stars: the hub to make both local answers zero, a chosen leaf to make exactly its incident query zero, or one of the two distinct outside vertices \(6,7\) to make both local answers one. These two selections form a valid center. Monotonicity under increasing \(n\) completes the VC classification.

**Universal Littlestone upper bound.** Fix any initial query \(q=\{a,b\}\). In the zero-answer branch, centers must intersect \(q\); call this restricted family \(D_q\). Consider any next query \(f\). If \(f=q\), its one-answer branch is empty. If \(f\cap q=\varnothing\), then the zero-answer branch of \(D_q\) has at most four centers, namely the pairs formed by one endpoint of \(q\) and one endpoint of \(f\). A family of at most four concepts has Littlestone dimension at most two. If \(f\cap q\) consists of one point, say \(f=\{a,x\}\), then the one-answer branch of \(D_q\) is a subfamily of the star of pairs \(\{b,y\}\) with fixed \(b\). Any such fixed-center star family has Littlestone dimension at most two: for a query containing \(b\), all answers are zero; for any other query, at most two centers answer zero, leaving a child of dimension at most one. Thus every possible second query has at least one branch of Littlestone dimension at most two. No complete depth-four tree is shattered by \(D_q\), so \(\operatorname{Ldim}(D_q)\le3\). Every initial query has its zero branch inside \(D_q\), and hence no complete depth-five tree exists for \(\mathcal N_n\). Therefore
\[
\operatorname{Ldim}(\mathcal N_n)\le4\quad\text{for all }n.\tag{4}
\]

**Sharp adaptive lower bound.** The file `DEPTH4_TREE.json` contains a complete depth-four binary tree with 15 internal pair queries and 16 terminal center pairs, all on \([7]\). At every internal node `no` means the disjointness answer zero and `yes` means one. Every path's labels agree with the center at its leaf, as checked in `verify_kneser.py`. This is a finite *exhaustively checkable witness*, not an extrapolation. It proves \(\operatorname{Ldim}(\mathcal N_7)\ge4\), and the same tree works for every \(n\ge7\).

At \(n=6\), the 15 available centers preclude a depth-four tree, whose 16 leaves require different concepts; the VC lower bound gives dimension three. At \(n=5\), any first query has only \(\binom32=3\) centers giving answer one, which precludes a depth-three tree, while VC dimension two supplies the lower bound. At \(n=4\), the one-answer branch has only \(\binom22=1\) center, ruling out depth two; dimension one follows from VC shattering. The edgeless cases have dimension zero. This completes the proof. \(\square\)

## Verification
Execute `python3 verify_kneser.py DEPTH4_TREE.json` with Python 3 and no third-party packages. The checker independently enumerates every concept and query pair, calculates VC shattering by the complete trace-partition recurrence for \(2\le n\le10\), computes Littlestone dimension from all version-space splits for \(2\le n\le14\), checks the explicit VC witnesses, and traverses all 16 paths of the depth-four certificate. Its complete successful output ends with `ALL_RANK_TWO_KNESER_CHECKS_PASS`. The finite checks corroborate the all-size proofs above; only the explicit 7-point decision tree relies on finite certification, and the full certificate is supplied.

## Relationship to prior work
Benediktsson, Macpherson, and Adler [1] prove that the *open* neighborhoods of Johnson graphs have VC dimension at most four (sharp across the family), and note boundedness for *closed* neighborhoods. At rank two, the open neighborhoods of \(\operatorname{KG}(n,2)\) are complements of the **closed**, not the open, neighborhoods of the triangular/Johnson graph \(J(n,2)\). Complementing each concept preserves both VC and Littlestone dimensions, but the published open-Johnson result is not an exact closed-Johnson formula. Therefore it does not by itself supply the per-order VC table or the adaptive dimension table above. Coudert and collaborators [2] present algorithms and bounds for graph closed-neighborhood VC dimension, not this exact all-order adaptive calculation. Manurangsi [3] analyzes complexity of computing the two dimensions for general explicit concept families, not this rank-two neighborhood class. The complement duality and the earlier universal Johnson bound are credited rather than presented as new.

## Limitations
This statement concerns rank-two Kneser graphs and their **open** neighborhoods only. It does not claim the same formulas for rank-three or higher Kneser graphs, arbitrary Johnson graphs, closed Kneser neighborhoods, or general graph neighborhoods. The historical-priority comparison is a best-knowledge literature assessment and does not constitute independent certification of novelty. The paper [1] is particularly close under Johnson complementation; if an equivalent closed-neighborhood specialization exists elsewhere, priority would need re-evaluation. The seven-point adaptive tree is fully finite and reproducible, and the global upper bounds are mathematical, not experimental.

## References
[1] B. G. Benediktsson, D. Macpherson, and I. Adler, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042, first posted 2020-07-31; Discrete Applied Mathematics 312 (2022), 29–44. https://arxiv.org/abs/2007.16042

[2] D. Coudert, M. Csikós, G. Ducoffe, and L. Viennot, *Practical Computation of Graph VC-Dimension*, arXiv:2405.07588, first posted 2024-05-13; SEA 2024. https://arxiv.org/abs/2405.07588

[3] P. Manurangsi, *Improved Inapproximability of VC Dimension and Littlestone's Dimension via (Unbalanced) Biclique*, arXiv:2211.01443, first posted 2022-11-02; ITCS 2023. https://arxiv.org/abs/2211.01443
