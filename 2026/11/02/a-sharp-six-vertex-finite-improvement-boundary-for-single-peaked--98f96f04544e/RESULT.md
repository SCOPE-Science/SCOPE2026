# A sharp six-vertex finite-improvement boundary for single-peaked jump Schelling games

## Finding

**Theorem (complete six-vertex boundary).** Let \(G=K_{s,t}\) be a connected complete bipartite graph with \(s,t\ge1\) and \(s+t\le6\). Place \(r\ge b\ge1\) red and blue agents at distinct vertices, leaving \(e=s+t-r-b\ge1\) vacancies. Agents make unilateral jumps to vacant vertices only when their own utilities strictly increase. Each agent values the fraction of her color in her occupied *closed* neighborhood according to any common single-peaked function from the class defined below, with peak \(0<\Lambda<1\).

The game **fails the finite improvement property if and only if**
\[
\{s,t\}=\{3,3\},\qquad (r,b,e)=(3,1,2),\qquad \Lambda>\frac25.
\]
In every other admissible case with at most six vertices, every sequence of strictly improving jumps terminates. The critical value \(2/5\) is strict: convergence holds at equality. In the exceptional case there is a four-jump cycle that returns every moving agent to her original vertex. Thus six vertices, with two occupied colors and two vacancies, are necessary and sufficient for nonconvergent improvement dynamics within connected complete bipartite graphs of order at most six. The result is uniform over the permitted utility shapes, not just linear utility functions.

## Assumptions and scope

A placement is a function assigning each vertex one of three states: vacant, red, or blue. Every red and blue agent is individually distinguishable although the payoff function is common. For an occupied vertex \(v\), let \(N_\sigma[v]\) consist of \(v\) itself and its **occupied** adjacent vertices. Put
\[
f_\sigma(v)=\frac{\#\{w\in N_\sigma[v]:\operatorname{color}(w)=\operatorname{color}(v)\}}{|N_\sigma[v]|}.
\]
The payoff is \(p(f_\sigma(v))\), where \(p\) is strictly increasing on \([0,\Lambda]\), has \(p(0)=0\), and satisfies
\[
p(x)=p\!\left(\frac{\Lambda(1-x)}{1-\Lambda}\right)\quad(\Lambda\le x\le1).
\]
This is the normalized single-peaked class used in the initiating article. Multiplication of the payoff by a positive constant does not change improvement dynamics; an arbitrary strictly increasing transformation on the increasing branch also preserves the relevant order. The jump of an agent from occupied vertex \(u\) to vacant vertex \(v\) is evaluated by comparing that agent's own utility at \(u\) before and at \(v\) after the move, with the original position then vacant. An improving response cycle is a finite sequence of such strict jumps returning the same labeled placement, and the finite improvement property (FIP) means that no such cycle exists.

## Proof

**Lemma 1 (ordinal reduction).** For every allowed payoff function \(p\), the strict ordering of attainable payoffs is the same as that induced by the tent function
\[
T_\Lambda(x)=\min\!\left\{\frac{x}{\Lambda},\frac{1-x}{1-\Lambda}\right\}.
\]
Indeed, for \(x\le\Lambda\) the utility is evaluated at \(x\), while for \(x\ge\Lambda\) it is evaluated at \(\Lambda(1-x)/(1-\Lambda)\). Since \(p\) is strictly increasing on the former interval, ordering either side or across the peak is exactly ordering \(T_\Lambda\). This also preserves ties. Hence all possible strict improvement edges can be computed with exact rational arithmetic using \(T_\Lambda\).

**Lemma 2 (finite exact peak partition).** On a graph of \(n\le6\) vertices every realized own-color fraction belongs to
\[
F_n=\left\{\frac{k}{j}:1\le k\le j\le n\right\}.
\]
For two distinct values \(f<g\) from this finite set, the sign of \(T_\Lambda(f)-T_\Lambda(g)\) can change only at
\[
\Lambda=\frac{f}{1+f-g},\qquad 0<f<g<1.
\]
For \(\Lambda\le f\) both fractions lie on the decreasing branch and the smaller fraction is preferred; for \(\Lambda\ge g\) both lie on the increasing branch and the larger fraction is preferred. When \(f<\Lambda<g\), the equality \(f/\Lambda=(1-g)/(1-\Lambda)\) has the unique root above. Distinct fractions cannot tie elsewhere. Therefore evaluating every interior root in the displayed finite set and one rational midpoint between each consecutive pair of roots (including endpoints \(0,1\)) proves the answer for **all real** \(0<\Lambda<1\). This is a finite *exhaustive* reduction of an infinite parameter range, not sampling evidence.

**Lemma 3 (complete finite-state check).** At each such representative peak, construct the directed graph on all vertex-colorings using exactly \(r\) red agents, \(b\) blue agents and \(e\) vacancies. Add a directed edge for every strict improvement jump computed from Lemma 1. Exhaustively test directed acyclicity for every \(s\le t\), every \(3\le s+t\le6\), and every positive color composition with at least one vacancy. The standalone script `verify_jump_bipartite_cutoff.py` performs exactly that exhaustive procedure and asserts that a directed cycle occurs precisely in the stated exceptional instance and peak range. It visits 3,079 graph/composition/peak cases, representing 140,610 state/parameter pairs and 216,828 improving directed edges, all computed with exact rational arithmetic. The graph orders 3, 4, 5 and 6 contribute respectively 7, 114, 708 and 2,250 cases; the peak grids contain respectively 7, 19, 59 and 75 rational representatives. For each instance, a DFS detects a cycle if and only if one exists in the entire finite color-state graph. A directed cycle in the labeled-placement graph would project to a directed cycle in this color-state graph, so acyclicity certifies FIP for distinguishable agents as well. There are no two-color cases with fewer than three vertices and at least one vacancy.

**Explicit sharp witness.** Fix \(G=K_{3,3}\) with ordered parts \(A=(A_0,A_1,A_2)\) and \(B=(B_0,B_1,B_2)\). Use three red agents, one blue agent and two vacancies. The four distinct color placements, where \(\circ\) means vacant, are
\[
(R,B,R)\mid(\circ,\circ,R)
\ \longrightarrow\
(\circ,B,R)\mid(R,\circ,R)
\ \longrightarrow\
(\circ,\circ,R)\mid(R,B,R)
\ \longrightarrow\
(R,\circ,R)\mid(\circ,B,R)
\ \longrightarrow\
(R,B,R)\mid(\circ,\circ,R).
\]
The first and third moves belong to the same red agent, jumping from \(A_0\) to \(B_0\) and back. Its own-color fraction changes \(1\to2/3\) in both moves, always a strict improvement because \(p(1)=0<p(2/3)\). The second and fourth moves belong to the same blue agent, jumping from \(A_1\) to \(B_1\) and back. Its fraction changes \(1/3\to1/2\) on each move. By Lemma 1, the latter is strictly beneficial exactly when \(\Lambda>2/5\): for \(1/3<\Lambda<1/2\) the comparison becomes \((1/2)/(1-\Lambda)>(1/3)/\Lambda\), or \(5\Lambda>2\); on either side the monotone branches give the same overall threshold. This establishes the exceptional nonconvergence and sharpness. Combined with Lemma 3, the theorem follows.

## Verification

Run from a directory containing the attached standalone program:

```bash
python3 verify_jump_bipartite_cutoff.py
```

The code needs only Python's standard library. It prints a PASS assertion and exact case, configuration and edge totals. It independently checks the labeled-agent four-move witness's vertex transfers and fraction changes. The proof's only computational step is a complete finite directed-cycle test after Lemma 2 reduces the continuum of peaks to finite rational representatives. In particular, no finite random experiment is used to infer an unverified infinite-network claim.

## Relationship to prior work

Friedrich, Lenzner, Molitor and Seifert [1] introduce this exact jump model and utility symmetry. Their Section 2 gives improvement cycles on paths and rings (including a five-vertex example) and on certain regular graphs, and records that induced-subgraph embeddings preserve such cycles when additional vertices remain vacant. Their results do not state the complete classification of all complete bipartite instances through six vertices or the sharp \(2/5\) peak boundary for \(K_{3,3}\). In particular, an existence construction at any one fixed peak does not imply FIP over the entire interval below the transition. Bilò and collaborators [2] analyze the related swap-action model, in which both agents must benefit from an exchange; its stability results do not determine unilateral-jump improvement cycles. The novel assertion here is the simultaneous sharp graph-size, color-composition and peak classification for the jump game, not the general possibility of improvement cycles.

## Limitations

The positive FIP classification is established **only** for connected complete bipartite graphs with at most six vertices. It does not assert that any particular larger complete bipartite graph is acyclic. The concrete four-jump witness embeds into \(K_{s,t}\) for \(s,t\ge3\) when all additional vertices are vacant; this embedding observation already follows from the source article's general induced-subgraph principle and is not claimed as a new theorem. The utility assumption includes the source paper's specific symmetry across the peak; arbitrary nonsymmetric unimodal preferences, different utility functions per agent, swaps and multi-color variants are outside scope. The exhaustive program certifies precisely the stated finite graph-order range; no separate formal-machine or external review is claimed.

## References

[1] Tobias Friedrich, Pascal Lenzner, Louise Molitor and Lars Seifert, *Single-Peaked Jump Schelling Games* (2023), arXiv:2302.12107v1, publicly posted February 23, 2023. https://arxiv.org/abs/2302.12107

[2] Davide Bilò, Vittorio Bilò, Pascal Lenzner and Louise Molitor, *Tolerance is Necessary for Stability: Single-Peaked Swap Schelling Games* (2022), arXiv:2204.12599. https://arxiv.org/abs/2204.12599
