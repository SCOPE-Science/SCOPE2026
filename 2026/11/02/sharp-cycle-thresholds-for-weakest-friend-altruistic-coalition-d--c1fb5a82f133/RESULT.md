# Sharp cycle thresholds for weakest-friend altruistic coalition dynamics

## Finding

For the globally altruistic coalition-formation model with a symmetric network of friends, summing friends' valuations has the finite-improvement property for every network, at all three standard degrees of altruism. In contrast, equal-treatment **minimum-based** aggregation already admits strict single-player improvement cycles on four agents. An exhaustive classification at this sharp threshold shows that exactly \(16\) of the \(64\) labeled four-agent friendship graphs admit an improvement cycle, namely the \(12\) copies of \(P_3\sqcup K_1\) and the \(4\) copies of \(K_3\sqcup K_1\); every graph of order at most three has acyclic improvement dynamics. All graphs admitting cycles at order four are disconnected. Among connected graphs, the first obstruction occurs at five agents, and a specified connected tree family admits a strict four-move cycle for every number \(n\ge5\) of agents.

The statement concerns **strict unilateral improvements**, not necessarily best responses, and does not assert that a Nash-stable partition fails to exist.

## Assumptions and scope

Let \(G=(V,E)\) be a finite simple undirected friendship graph with \(|V|=n\ge1\). Distinct nonadjacent vertices are enemies. In partition \(\pi\), write \(\pi(i)\) for player \(i\)'s coalition and \(F_i=\{j:\{i,j\}\in E\}\). The underlying friend-oriented valuation is
\[
 v_i(\pi)=n\,|F_i\cap\pi(i)|-|(V\setminus(F_i\cup\{i\}))\cap\pi(i)|.
\]

**Global minimum-based equal treatment** is the utility
\[
 U_i^{\mathrm{minEQ}}(\pi)=\min_{j\in F_i\cup\{i\}}v_j(\pi).
\]
Crucially, a friend \(j\) contributes its valuation even when \(j\notin\pi(i)\); this is a coalition-formation game, not the coalition-local minimum-based hedonic game.

A unilateral move changes only the moving player's coalition membership, to an existing other coalition or to a singleton. It is a *strict improvement* when the mover's utility increases. The improvement digraph has one vertex per set partition, with an arc for every possible strict unilateral improvement. The finite-improvement property (FIP) means this digraph is acyclic; because it is finite, every improvement path then terminates.

For comparison, fix \(M=n^3\) and let \(S_i(\pi)=\sum_{j\in F_i}v_j(\pi)\), with an empty sum equal to zero. The globally sum-based degrees of altruism are
\[
 U_i^{\mathrm{sumSF}}=M v_i+S_i,\qquad
 U_i^{\mathrm{sumEQ}}=v_i+S_i,\qquad
 U_i^{\mathrm{sumAL}}=v_i+M S_i.
\]

## Proof

**1. Exact potentials for summation.** Consider a unilateral move by player \(i\). Let \(\Delta f_i\) and \(\Delta e_i\) be the change in the number of friends and enemies of \(i\) in its coalition. Then
\[
 \Delta v_i=n\Delta f_i-\Delta e_i.
\]
Only friends entering or leaving the mover's coalition change their own valuation, and each such friend's valuation changes by \(+n\) or \(-n\) accordingly. Thus
\[
 \Delta S_i=n\Delta f_i.
\]
Consequently,
\[
 \begin{aligned}
 \Delta U_i^{\mathrm{sumSF}}&=n(M+1)\Delta f_i-M\Delta e_i,\\
 \Delta U_i^{\mathrm{sumEQ}}&=2n\Delta f_i-\Delta e_i,\\
 \Delta U_i^{\mathrm{sumAL}}&=n(M+1)\Delta f_i-\Delta e_i.
 \end{aligned}
\]
For \(a,b>0\) define
\[
 \Phi_{a,b}(\pi)=\sum_{\{i,j\}\subseteq V\, :\,\pi(i)=\pi(j)}
 \bigl(a\,\mathbf1_{\{i,j\}\in E}-b\,\mathbf1_{\{i,j\}\notin E}\bigr).
\]
A unilateral move changes \(\Phi_{a,b}\) by precisely \(a\Delta f_i-b\Delta e_i\). Hence \(\Phi_{n(M+1),M}\), \(\Phi_{2n,1}\), and \(\Phi_{n(M+1),1}\) are **exact potentials** for the three respective sum-based models. Every strict improvement raises its potential and the finite state space makes cycling impossible, for every \(G\).

**2. Sharp four-agent counterexample.** Let \(V=\{0,1,2,3\}\), with friendship edges \(\{0,1\}\) and \(\{0,2\}\), so vertex \(3\) is isolated. Consider the four coalition partitions
\[
 \begin{aligned}
 A&=\{\{0,1,3\},\{2\}\}, & B&=\{\{0,1\},\{2,3\}\},\\
 C&=\{\{0,2,3\},\{1\}\}, & D&=\{\{0,2\},\{1,3\}\}.
 \end{aligned}
\]
Directly applying the definition gives min-EQ utility vectors, indexed \((0,1,2,3)\),
\[
 U(A)=(0,3,0,-2),\quad U(B)=(-1,4,-1,-1),
\]
\[
 U(C)=(0,0,3,-2),\quad U(D)=(-1,-1,4,-1).
\]
The strict improvement cycle is \(A\xrightarrow{3}B\xrightarrow{0}C\xrightarrow{3}D\xrightarrow{0}A\), where the arrow labels are the moving players. The mover's utility changes \(-2\to-1\), \(-1\to0\), \(-2\to-1\), \(-1\to0\), respectively.

**3. Complete sharp small-order classification.** The standalone program `verify.py` is an exhaustive finite certificate for every labeled simple graph on \(n\in\{1,2,3,4\}\). It enumerates all \(2^{\binom n2}\) graphs by independent edge bits and all \(B_n\) set partitions by canonical restricted-growth strings; for each graph and each partition it enumerates every relocation of every player to every other existing block or a new singleton. It evaluates all personal valuations, then the minimum of the mover's own and *all* friends' valuations before and after each relocation. It puts an arc in the finite improvement digraph exactly when that mover improves strictly, and applies a three-color directed depth-first search for any cycle. There are respectively \(1,2,8,64\) graphs and \(1,2,5,15\) partitions. The output is \(0,0,0,16\) cyclic friendship graphs, with all sixteen classified by degree multiset: twelve have \((0,1,1,2)\), which necessarily determines \(P_3\sqcup K_1\), and four have \((0,2,2,2)\), which necessarily determines \(K_3\sqcup K_1\). Thus the finite certificate exhausts every graph on up to four vertices, rather than sampling graph instances; it proves the sharp lower bound and the connected lower bound.

**4. Connected tree counterexamples for every larger order.** For each \(n\ge5\), take vertex set \(\{0,1,\ldots,n-1\}\) and the tree with edges
\[
 \{\{0,4\},\{1,3\},\{2,3\},\{3,4\}\}\ \cup\ \{\{2,k\}:5\le k<n\}.
\]
For core vertices \(0,\ldots,4\), use the partitions
\[
 \begin{aligned}
 A&=\{\{0,2,3\},\{1\},\{4\}\},
 &B&=\{\{0,1\},\{2,3\},\{4\}\},\\
 C&=\{\{0,1,3\},\{2\},\{4\}\},
 &D&=\{\{0,2\},\{1,3\},\{4\}\}.
 \end{aligned}
\]
All additional vertices \(5,\ldots,n-1\) form separate singleton coalitions in all four states. In the exact global-minimum utility, the mover utilities on successive states are
\[
 U_0(A)=-2,\quad U_0(B)=-1,\quad
 U_3(B)=-1,\quad U_3(C)=0,
\]
\[
 U_0(C)=-2,\quad U_0(D)=-1,\quad
 U_3(D)=-1,\quad U_3(A)=0.
\]
These eight values follow directly from the four displayed local coalitions. The extra pendant vertices have valuation zero as singletons and never lower the relevant minima below the indicated values; therefore the equations hold for **every** \(n\ge5\). Moving successively players \(0,3,0,3\) yields the strict improvement cycle \(A\to B\to C\to D\to A\). The graph is connected and acyclic since it is the tree on the path \(0-4-3-2\), the pendant vertex \(1\) at \(3\), and additional pendant vertices attached to \(2\). Together with step 3, this proves that five agents are necessary and sufficient for a connected obstruction.

## Verification

Run `python3 verify.py` using Python 3 with only the standard library. It performs exhaustive finite graph/partition/relocation enumeration on \(n\le4\), checks the two degree-multiset classes and their counts, verifies both explicitly displayed improvement cycles, checks the connected-tree cycle at six sizes through fifty vertices, and independently compares the proposed exact-potential changes with direct personal-and-global utility changes for all unilateral moves of all graphs of order at most four.

The exhaustive output gives \(1+2+8+64=75\) graph instances, \(3{,}068\) strictly improving transition evaluations (counting graphs separately), and the precise cyclic-graph vector \((0,0,0,16)\). Finite checks are used to prove only the finite classification. The all-size results rely on the symbolic exact-potential calculation and the explicit arbitrary-order tree construction.

## Relationship to prior work

Kerkmann, Cramer and Rothe introduce globally altruistic coalition-formation games with the six sum/min and SF/EQ/AL aggregations. Their Nash-stability existence result guarantees a stable partition but does **not** assert that arbitrary sequences of strict improvements converge. The four-agent classification and arbitrary-size tree cycles concern a distinct dynamic question, as does the exact-potential contrast. The 2020 conference predecessor describes the globally sum-based model but not the minimum-based extension.

Wiechers and Rothe's 2020 minimum-based altruistic *hedonic* model considers friends in the player's coalition, rather than all friends globally, so neither its Nash-stability arguments nor its utility definitions cover these cycles. Boehmer, Bullinger and Kerkmann study path dynamics in history-dependent cardinal hedonic games with resent or appreciation, rather than static global minimum-EQ utilities. A potential function for the sum-based network game is closely related to the familiar exact-potential principle for symmetric pair interactions; the main new structural boundary is the failure of this property under weakest-friend aggregation, including the sharp small-graph and connected-tree thresholds.

## Limitations

No assertion is made about shortest **best-response** cycles, all connected graphs with more than four vertices, complexity of recognizing cycle existence, or failure of Nash-equilibrium existence. The finite classification uses the included exhaustive checker, so an independent manual proof not relying on complete finite enumeration is not provided for its sixty-four four-agent graph cases. The all-order tree cycle is proved symbolically. Possible coverage by further specialist literature remains a publication-priority risk; independent external assessment has not been performed.

## References

1. A. M. Kerkmann, S. Cramer, J. Rothe, *Altruism in Coalition Formation Games*, arXiv:2301.05674v1, first posted 2023-01-13. https://arxiv.org/abs/2301.05674
2. A. M. Kerkmann, J. Rothe, *Altruism in Coalition Formation Games*, IJCAI 2020 conference version. https://www.ijcai.org/Proceedings/2020/0049.pdf
3. C. Wiechers, J. Rothe, *Stability in Minimization-Based Altruistic Hedonic Games*, 2020. https://ceur-ws.org/Vol-2655/paper3.pdf
4. N. Boehmer, M. Bullinger, A. M. Kerkmann, *Causes of Stability in Dynamic Coalition Formation*, arXiv:2211.17169, 2022. https://arxiv.org/abs/2211.17169
