# All error-detecting identifying codes of matching-deleted complete bipartite graphs

## Finding

Let \(a,b\ge 2\) and \(0\le t\le\min(a,b)\) be integers. Start with the labelled complete bipartite graph \(K_{a,b}\), and delete an arbitrary matching of exactly \(t\) edges. Write the resulting graph as \(G_{a,b,t}\). An error-detecting identifying code is a vertex subset \(S\) satisfying the two-dominating and asymmetric distinguishing conditions specified below. Let
\[
F_{a,b,t}(z)=\sum_{S\text{ an error-detecting identifying code of }G_{a,b,t}} z^{|S|}.
\]
Write \(p=a-t\) and \(q=b-t\), the numbers of vertices not incident with deleted edges in the two shores. Then the **complete labelled-code enumerator** is
\[
F_{a,b,t}(z)=\begin{cases}
z^{2t}+2t z^{2t-1}+t(t-1)z^{2t-2},&p=q=0,\ t\ge5,\\
z^8+8z^7,&p=q=0,\ t=4,\\
z^{2t+1}+t z^{2t},&p+q=1,\ t\ge4,\\
z^7,&p+q=1,\ t=3,\\
z^{2t+2},&p=q=1,\ t\ge3,\\
0,&\text{otherwise}.
\end{cases}
\]
Each nonzero term enumerates all possible codes; no graph automorphisms or relabellings are factored out. Thus the graph admits such a code precisely for the nonzero parameter cases displayed.

In particular, for the crown graph \(G_{t,t,t}=K_{t,t}-M_t\), the minimum cardinality is \(2t-1\) with exactly eight optimal codes at \(t=4\), and \(2t-2\) with exactly \(t(t-1)\) optimal codes for every \(t\ge5\). The complete code census changes from quadratic to linear to a single mandatory full code as one unmatched vertex is introduced on one shore and then on both shores.

## Assumptions and scope

All graphs are finite, simple and labelled. The left shore is \(A=\{a_1,\ldots,a_t\}\cup A_0\), with \(|A_0|=p\), and the right shore is \(B=\{b_1,\ldots,b_t\}\cup B_0\), with \(|B_0|=q\). Every edge between \(A\) and \(B\) is present except \(a_i b_i\) for \(1\le i\le t\). Choice of the deleted matching does not affect the formula because relabelling within shores induces an isomorphism.

Write \(N[v]\) for the closed neighborhood of vertex \(v\). Following the standard error-detecting identifying-code characterization, a code is a set \(S\subseteq V(G)\) such that (i) \(|N[v]\cap S|\ge2\) for every vertex \(v\), and (ii) for every pair \(u\ne v\), at least one of
\[
|(N[u]\setminus N[v])\cap S|\ge2
\quad\text{or}\quad
|(N[v]\setminus N[u])\cap S|\ge2
\]
holds. This is the \(2^{\#}\)-distinguishing criterion for tolerating one false-negative detector transmission; the characterization, not a stronger error-correction condition, is used throughout.

## Proof

**1. The unmatched-vertex obstruction.** If \(p\ge2\), two unmatched vertices in \(A\) have the same open neighborhood \(B\); their closed neighborhoods differ only in their own vertices. Consequently neither exclusive closed-neighborhood difference contains two vertices, and no code exists. The same argument gives impossibility when \(q\ge2\). Hence only \(p,q\in\{0,1\}\) can contribute.

**2. The matching-index restriction.** For distinct indices \(i,j\in\{1,\ldots,t\}\), the two exclusive closed-neighborhood differences of matched vertices \(a_i\) and \(a_j\) are precisely
\[
N[a_i]\setminus N[a_j]=\{a_i,b_j\},\qquad
N[a_j]\setminus N[a_i]=\{a_j,b_i\}.
\]
The same two-element alternatives, reversed, distinguish \(b_i\) from \(b_j\). Thus either \(\{a_i,b_j\}\subseteq S\) or \(\{a_j,b_i\}\subseteq S\), for every pair \(i\ne j\). It follows that at most one matched vertex from \(A\), and at most one matched vertex from \(B\), may be omitted. Furthermore, the two ends \(a_i,b_i\) of a deleted matching edge can never both be omitted, because they prevent distinction between matched vertices at indices \(i\) and \(j\ne i\).

**3. Unmatched vertices force detectors.** Suppose \(p=1\), with unmatched left vertex \(a_*\). Comparing \(a_*\) with a matched \(a_i\) yields
\[
N[a_*]\setminus N[a_i]=\{a_*,b_i\},\qquad
N[a_i]\setminus N[a_*]=\{a_i\}.
\]
Therefore every code contains \(a_*\) and all matched right vertices \(b_i\). Likewise, if \(q=1\), every code contains the unmatched right vertex \(b_*\) and all matched left vertices \(a_i\). Accordingly, when \(p=q=1\), only the full vertex set can possibly be a code. When \(p+q=1\), the only candidates are the full vertex set and sets omitting exactly one matched vertex from the shore with an unmatched vertex. When \(p=q=0\), the only candidates are the full set, one omitted vertex, and one omitted vertex from each shore at distinct matched indices.

**4. The remaining pairwise obstruction.** For an adjacent matched pair \(a_i,b_j\), where \(i\ne j\), the two exclusive closed-neighborhood differences are
\[
N[a_i]\setminus N[b_j]=B\setminus\{b_i,b_j\},\qquad
N[b_j]\setminus N[a_i]=A\setminus\{a_i,a_j\}.
\]
A nonadjacent deleted pair \(a_i,b_i\) has disjoint closed neighborhoods, so two-domination already distinguishes it. All remaining pairs fall into the matched same-shore or unmatched-versus-matched comparisons already addressed, or involve unmatched vertices on opposite shores; those latter pairs are distinguished when their possible codes satisfy the parameter bounds below.

If \(p=q=0\), the full code fails for \(t=3\), since each difference in the last display has size \(t-2=1\). For \(t=4\), the full code and every one-vertex deletion work: on an adjacent matched pair, one shore retains all four vertices, giving an exclusive difference of two. Any candidate with one omitted vertex on each shore fails: there are two distinct matching indices outside the two omitted indices, and the corresponding adjacent pair has exactly one selected vertex in each exclusive difference. If \(t\ge5\), each surviving candidate leaves at least \(t-1\) selected vertices in each shore, so both exclusive differences for every adjacent matched pair have size at least \(t-3\ge2\). These candidates also satisfy two-domination and the remaining pair distinctions. This proves the first two nonzero lines of the formula.

If \(p+q=1\), use symmetry to take \(p=1\). The necessary candidate sets contain \(a_*\) and all of \(B\), and omit at most one matched left vertex. The full set works for \(t\ge3\): adjacent matched pairs have at least \(t-1\) selected vertices on the left exclusive difference, and pairs involving \(a_*\) have at least \(t-1\) selected vertices in the right exclusive difference. Omitting one matched left vertex fails for \(t=3\), because the adjacent matched pair on the other two indices has only one selected vertex in each exclusive difference. For \(t\ge4\), all adjacent matched pairs have \(t-2\ge2\) selected vertices in the complete right-shore exclusive difference, and all pairs involving \(a_*\) remain distinguished. Two-domination holds throughout. Thus the full set and exactly \(t\) one-vertex deletions work for \(t\ge4\), while only the full set works when \(t=3\).

If \(p=q=1\), the forcing argument leaves only the full set. It works for \(t\ge3\): every adjacent matched pair has \(t-1\ge2\) exclusive neighbors on either side, and comparisons involving unmatched vertices have at least two exclusive vertices. Every vertex is at least two-dominated. For \(t\le2\), no code exists: at \(t=1\), the graph has an edge whose endpoints have degrees at most two (or a degenerate isolated vertex), while at \(t=2\), an adjacent matched pair has both degrees two. In a triangle-free graph, an edge whose endpoints each have degree at most two has at most one vertex in either exclusive closed-neighborhood difference, so it cannot be distinguished. The same degree argument rules out \(p=q=0\) and \(p+q=1\) at \(t=2\); cases at smaller \(t\) contain a vertex that cannot be two-dominated or such an edge.

**5. Enumeration.** In the crown case, the permitted omissions give respectively one complete set, \(2t\) single-vertex omissions, and \(t(t-1)\) pairs consisting of an omitted left and an omitted right vertex with unequal deleted-edge indices (when \(t\ge5\)). The one-unmatched-shore case gives one full set and \(t\) single omissions when \(t\ge4\); the two-unmatched-shore case gives only the full set. Substituting their cardinalities proves every coefficient in the stated polynomial.

## Verification

The accompanying standalone source file `verify.py` constructs every closed neighborhood directly from the graph's bipartite adjacency relation and exhaustively tests the two-domination and asymmetric distinguishing conditions, without using the proof's intermediate pair classification. It compares all code cardinalities with the theorem for 155 finite parameter triples with \(2\le a,b\le7\) and \(a+b\le13\). It separately verifies all structurally listed candidate sets and checks 32 larger parameter families, including matching sizes 12, 20 and 50. Run `python3 verify.py`; the observed output was `VERIFY_OK: 155 full exhaustive parameter cases; 32 larger witness families`.

The finite computation checks examples only; the deductions in the Proof establish the theorem for all integers in scope.

## Relationship to prior work

Jean and Seo (first public preprint 11 August 2022) introduced and studied error-detecting identifying codes, stated the precise two-domination and \(2^{\#}\)-distinguishing criterion in their Theorem 2.1, and investigated hardness and special classes including cubic graphs and infinite grids. Their inspected original manuscript does not classify the matching-deleted bicliques or provide these code enumerators. Seo and Slater (2018) provided an earlier generalized separating-systems framework underlying the same detection criterion. Related work on redundant identifying codes studies detector removal rather than this one-sided false-negative model. A crown graph is a dense bipartite example, not one of the cubic or infinite-grid families covered by the cited source's exact computations. The claimed contribution here is the complete special-family classification and multiplicities, not the general criterion or NP-hardness.

## Limitations

The theorem concerns only error-detecting identifying codes with one allowed false-negative transmission, not one-error correction, redundant identifying codes, or unrelated locating-dominating notions. Code counts distinguish labelled vertex subsets, not isomorphism orbits. Source comparison is best-knowledge; no worldwide publication-priority guarantee or independent mathematical review is claimed. The 2024 journal version of the principal 2022 manuscript was accessible at abstract level, not independently read in full, although the original full manuscript was inspected. The earlier 2018 generalized separating-systems paper was assessed through its statement as cited by Jean and Seo and bibliographic descriptions, not its complete text.

## References

1. D. Jean and S. Seo, *Optimal Error-detection system for Identifying Codes*, arXiv:2208.06052, publicly posted 2022-08-11. https://arxiv.org/abs/2208.06052 . Published as *Optimal error-detection system for identifying codes*, *Networks* **85** (2025), 61–75, first online 2024-10-01, https://doi.org/10.1002/net.22254 .
2. S. J. Seo and P. J. Slater, *Generalized set dominating and separating systems*, *Journal of Combinatorial Mathematics and Combinatorial Computing* **104** (2018), 15–29.
3. D. Jean and S. Seo, *Fault-tolerant Identifying Codes in Special Classes of Graphs*, arXiv:2112.01685, first posted 2021-12-03, https://arxiv.org/abs/2112.01685 . Studies the distinct redundant-detector model.
