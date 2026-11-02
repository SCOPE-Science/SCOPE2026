# Exact potential and a sharp vacancy boundary for single-peaked jump games on complete multipartite graphs

## Finding
For a complete multipartite graph with exactly one unoccupied vertex, the self-inclusive, occupied-closed-neighborhood version of a Schelling jump game has an **exact potential for arbitrary type- and part-dependent payoff functions of the same-type fraction**. Consequently every strictly improving jump sequence terminates. For fixed numbers of parts and types, the length of every such sequence is polynomial in the number of vertices; on a complete bipartite graph with two types, it is at most \(2(\min\{a,b\}+1)-1\). This theorem includes single-peaked and other nonmonotone preferences.

The one-vacancy condition is sharp as a uniform guarantee: on \(K_{3,3}\), with **two** vacancies, three agents of one type, one agent of another type, and the *same* single-peaked utility \(p(f)=1-|2f-1|\) for every agent, four strictly improving jumps return to the identical position profile.

## Assumptions and scope
Fix integers \(m\ge2\) and \(a_1,\ldots,a_m\ge1\), and let \(G=K_{a_1,\ldots,a_m}\) have \(V=\sum_i a_i\) vertices partitioned into independent parts \(P_i\). There are \(V-1\) agents and one vacant vertex. Each agent has one of \(k\ge1\) fixed types, and the total number of type-\(c\) agents is \(C_c\), with \(\sum_c C_c=V-1\). All agents may jump to the vacancy. The utility of a type-\(c\) agent at a vertex of part \(P_i\) is \(u_{i,c}(f)\), where \(u_{i,c}:[0,1]\to\mathbb R\) is **arbitrary** and \(f\) is the fraction of agents of type \(c\) among the occupied closed neighborhood (the moving agent is included in numerator and denominator). Other agents in the same part are not neighbors. No monotonicity, continuity, or common payoff function is required.

Write \(n_{i,c}\) for the number of type-\(c\) agents occupying \(P_i\). For \(1\le h\le C_c\), let
\[
q_{i,c}(h)=\min\left\{1,\frac{C_c-h+1}{V-a_i}\right\},\qquad
\Phi=\sum_{i=1}^m\sum_{c=1}^k\sum_{h=1}^{n_{i,c}}u_{i,c}\bigl(q_{i,c}(h)\bigr).
\]
The denominators are strictly positive since \(m\ge2\). The truncation to \(1\) only defines harmless values for combinatorially unreachable marginal levels; at each actual cross-part move no truncation occurs.

## Proof
**Exact change for cross-part jumps.** Suppose the vacancy lies in part \(P_j\) and a type-\(c\) agent jumps from a different part \(P_i\) to it. The source part \(P_i\) is full before the move and the destination part \(P_j\) is full afterwards. Just before the move, the moving agent has \(V-a_i-1\) occupied neighbors outside its part, and its occupied closed neighborhood has size \(V-a_i\). Precisely \(C_c-n_{i,c}\) of those neighbors share its type. Its old utility is therefore
\[
u_{i,c}\left(\frac{C_c-n_{i,c}+1}{V-a_i}\right)=u_{i,c}\bigl(q_{i,c}(n_{i,c})\bigr).
\]
After the move, the agent has \(V-a_j-1\) occupied neighbors outside its new part. The old count of type \(c\) in the destination part was \(n_{j,c}\), so its new utility is
\[
u_{j,c}\left(\frac{C_c-n_{j,c}}{V-a_j}\right)=u_{j,c}\bigl(q_{j,c}(n_{j,c}+1)\bigr).
\]
The two count changes are \(n_{i,c}\mapsto n_{i,c}-1\) and \(n_{j,c}\mapsto n_{j,c}+1\). All other counts are unchanged. The displayed expressions are exactly the single term removed from and single term added to \(\Phi\), respectively. Hence **the moving agent's utility change equals \(\Phi\)'s change**.

**Within-part jumps.** If an agent jumps to the vacancy in its own part, all part-type counts are unchanged. Its set of occupied neighbors outside the part is unchanged, and it remains its own occupied closed-neighborhood member; its utility does not change. Thus the exact-potential equality also holds with both changes zero.

**Termination and move bound.** Strict improvement strictly increases \(\Phi\). Each count matrix determines its potential, so a strict improvement path never repeats a count matrix. Order the part sizes so that \(a_{(1)}\le\cdots\le a_{(m)}\). Given the index of the part containing the vacancy, the occupancy total is fixed in each part. For each of the first \(m-1\) parts, specifying the counts of the first \(k-1\) types determines its final type count; the counts in the remaining part then follow from the fixed global type totals. Thus the number of feasible count matrices is at most
\[
 m\prod_{i=1}^{m-1}(a_{(i)}+1)^{k-1}.
\]
Every strict improvement path consequently has at most this number minus one moves. In particular, if \(m=k=2\), only the smaller part's count of the first type and the vacancy part need be specified: the bound is \(2(\min\{a,b\}+1)-1\).

**Sharp vacancy-boundary cycle.** On \(K_{3,3}\), denote the two parts by vertical bars. Write \(A\) for the majority type, \(B\) for the minority type, and \(\circ\) for a vacancy. There are three \(A\) agents, one \(B\) agent, and two vacancies. Consider the following four jumps, where \(p(f)=1-|2f-1|\) is applied to each agent's own-type fraction in its occupied closed neighborhood:
\[
\begin{array}{rcll}
(A,\circ,A\mid B,A,\circ)&\longrightarrow&(A,B,A\mid\circ,A,\circ)& B:\;2/3\to1,\\
(A,B,A\mid\circ,A,\circ)&\longrightarrow&(\circ,B,A\mid\circ,A,A)& A:\;0\to2/3,\\
(\circ,B,A\mid\circ,A,A)&\longrightarrow&(\circ,\circ,A\mid B,A,A)& B:\;2/3\to1,\\
(\circ,\circ,A\mid B,A,A)&\longrightarrow&(A,\circ,A\mid B,A,\circ)& A:\;0\to2/3.
\end{array}
\]
The moving agents are, in order, the \(B\) agent, the left part's first \(A\) agent, that same \(B\) agent, and the same \(A\) agent. Every improvement is strict and all agents return to their original vertices. A repeated strict improvement cycle precludes a strictly increasing ordinal potential or the finite-improvement property for this two-vacancy model.

## Verification
The standalone standard-library script `verify.py` reconstructs the potential from its definition, uses exact rational arithmetic, and independently evaluates utility changes for every legal directed move across six complete-multipartite test cases with two or three types. It verifies \(2{,}556\) equality identities (including \(1{,}024\) strict improving moves) for deliberately heterogeneous nonlinear, sometimes nonmonotone rational utilities. It then checks all four jumps in the displayed two-vacancy cycle with exact fractions and confirms full return to the initial profile. Run `python3 verify.py` from the extracted package directory.

These finite tests are checks of the implementation and of the explicit cycle; the universal one-vacancy statement and move bounds are established by the preceding algebraic proof, not by enumeration.

## Relationship to prior work
Friedrich, Lenzner, Molitor and Seifert introduced and analyzed single-peaked jump Schelling games, including the convention that an agent counts itself in the occupied closed neighborhood. Their results exhibit improving cycles on some regular graphs and prove equilibrium existence in several other families. The present theorem identifies **complete multipartite graphs with one vacancy** as a different exact-potential class, permits arbitrary part- and type-dependent nonlinear utility functions, and supplies explicit improvement-length bounds. The two-vacancy example concerns the sharp boundary of this graph-family guarantee; it is not a minimum-vertex classification.

Kanellopoulos, Kyropoulou and Voudouris study modified Schelling games with a different normalization and self-treatment, so their conclusions do not automatically cover arbitrary nonlinear utilities evaluated on the present occupied closed-neighborhood fraction. The homophilic resource-selection framework of Gadea Harder and collaborators has a different feasible resource-allocation mechanism and does not force the stated exact potential for injective vertex placements. The marginal-sum construction is conceptually related to congestion-game potentials, but the vacancy geometry and changing closed-neighborhood denominators require the actual move identity above. No claim is made of priority over every possible unindexed general potential-game treatment.

## Limitations
The exact potential requires a complete multipartite graph, one vacancy, **part-and-type** payoff homogeneity (not arbitrary individual payoffs), and closed-neighborhood self-inclusion. It does not imply uniqueness of a Nash equilibrium, a unique outcome, or convergence under neutral moves. The bound on improving moves is polynomial only for fixed numbers of parts and types. The two-vacancy cycle shows that the finite-improvement property does not extend without qualification to two vacancies, not that every two-vacancy instance cycles. The one-vacancy theorem does not imply finite improvement on arbitrary regular graphs or for games with swaps instead of jumps.

## References
1. T. Friedrich, P. Lenzner, L. Molitor, L. Seifert, *Single-Peaked Jump Schelling Games*, arXiv:2302.12107v1, first posted 2023-02-23, https://arxiv.org/html/2302.12107v1.
2. P. Kanellopoulos, M. Kyropoulou, A. Voudouris, *Modified Schelling Games*, arXiv:2005.12149, first posted 2020-05-25, https://arxiv.org/abs/2005.12149.
3. J. Gadea Harder, S. Krogmann, P. Lenzner, L. Skopalik, *Strategic Resource Selection with Homophilic Agents*, IJCAI 2023, https://www.ijcai.org/proceedings/2023/0301.pdf.
4. R. W. Rosenthal, *A Class of Games Possessing Pure-Strategy Nash Equilibria*, International Journal of Game Theory 2 (1973), 65–67, doi:10.1007/BF01737559.
