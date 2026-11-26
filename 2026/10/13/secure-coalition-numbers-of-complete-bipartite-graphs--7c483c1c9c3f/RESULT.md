# Secure coalition numbers of complete bipartite graphs

## Finding
For every integer \(t\ge2\), the secure coalition number on the minimum-degree-two complete bipartite family is
\[
\mathrm{SEC}(K_{2,t})=4.
\]
Thus the general lower bound \(\mathrm{SEC}(G)\ge\delta(G)+2\) is attained on this whole family, independently of the size of the larger shore. The retained claim is this exact branch; other shore sizes below locate it in the full classification and are not claimed as new here.

## Assumptions and scope
All graphs are finite and simple. A secure dominating set is a dominating set in which each outside vertex can replace an adjacent member while leaving a dominating set. A secure coalition consists of two disjoint sets, neither secure dominating, whose union is secure dominating. A secure-coalition partition requires each block to have a partner, except that singleton secure dominating sets may stand alone. A secure dominating singleton requires a complete graph: after exchanging the singleton vertex for any other vertex, the latter must itself dominate the graph. This exception therefore does not arise for \(K_{s,t}\) other than \(K_{1,1}\). The secure coalition number is the maximum number of blocks.

## Proof of the retained branch
Write \(A,B\) for the shores of sizes \(s,t\) and \((x,y)\) for the numbers selected in them. Ordinary domination requires \((x=s\text{ or }y>0)\) and \((y=t\text{ or }x>0)\). A defender for an outside vertex of \(A\) must be a selected vertex of \(B\). If one exists, the exchange leaves the \(B\) side dominated by the newly selected vertex of \(A\). The \(A\) side is dominated after the exchange exactly when there was only one outside vertex there or at least two \(B\) vertices were selected originally. The symmetric condition holds on \(B\). Thus secure domination is equivalent to the two domination requirements and
\[
(x\ge s-1\text{ or }y\ge2),\qquad (y\ge t-1\text{ or }x\ge2).
\]

For \(s=2\), a block containing all of \(A\) would already be secure dominating and is forbidden. Consequently there are exactly two blocks meeting \(A\). If there were at least five blocks, there would be at least three \(B\)-only blocks. Fix one of them, \(W\). Its union with another \(B\)-only block cannot cover \(B\), so does not dominate. Its union with either of the two blocks meeting \(A\) leaves at least two \(B\) vertices outside. This union has just one selected vertex in \(A\); by the exchange criterion it is not secure dominating. Thus \(W\) has no partner, a contradiction.

For \(t=2\), the singleton partition works by partnering across the shores. For \(t\ge3\), choose disjoint blocks of occupancies \((1,t-2),(1,0),(0,1),(0,1)\) covering all vertices. None is secure dominating. The first block partners with the second by producing a set containing all of \(A\), and with each of the remaining blocks by producing occupancy \((1,t-1)\). Thus four blocks are attained, proving the finding. Alternatively, existence of four blocks follows from Shetty–Udupa–Rakshith's general lower bound (Theorem 2.4).

## Context: the other shore sizes
The complete graph \(K_2\) has value two, and stars with at least two leaves have value three by the tree and small-order results of Shetty–Udupa–Rakshith. For \(3\le s\le t\) the classification takes the form
\[
\mathrm{SEC}(K_{s,t})=\max\{t+2,s+t-4\}.
\]
The following comparison with the known double-coalition theorem makes explicit which part of this formula is inherited.

A double dominating set requires at least two selected neighbors for each outside vertex and at least one selected neighbor for each selected vertex. On \(K_{s,t}\), for any set of size strictly less than \(s\), double and secure domination are both equivalent to \(x,y\ge2\): both shores have outside vertices; if \(x=s-1\), domination needs \(y\ge1\), already giving size at least \(s\); the symmetric exceptional occupancy is excluded in the same way. For a partition with \(k\) blocks put \(E=s+t-k\). Every single block and every union of two blocks has size at most \(E+2\). Hence if a secure-coalition partition has \(k>t+2\), then \(E+2<s\), so that very partition is a double-coalition partition. Henning–Mojdeh's Theorem 6 gives \(\mathrm{DC}(K_{s,t})=\max\{t+1,s+t-4\}\) when \(2\le s\le t\). Thus \(\mathrm{SEC}(K_{s,t})\le\max\{t+2,s+t-4\}\) for \(s\ge3\).

For the lower bound \(t+2\), take a block of \(s-1\) vertices from \(A\) and leave every other vertex singleton. The large block is not dominating; its unions with the omitted \(A\) vertex and with any \(B\) vertex are secure by the exchange test. To realize \(s+t-4\) when \(s\ge6\), use Henning–Mojdeh's two blocks of occupancies \((1,2)\) and \((2,1)\), leaving the other vertices singleton. The two blocks are not secure dominating, their union has occupancy \((3,3)\), and each remaining singleton is partnered with the block that makes a union of occupancy \((2,2)\). This gives the same deficit-four value and the same witness as in the double-coalition theorem. These contextual deductions are not an originality claim for the stabilized regime.

## Relationship to prior work and limitations
The initiating secure-coalition paper supplies the definition and the general lower bound, giving the lower bound of four for \(K_{2,t}\) but not the upper bound in the inspected results. The classification of individual secure dominating sets on complete multipartite graphs likewise gives the shore-occupancy test, not the limit on partition blocks. The double-coalition classification does not give the same bound on the retained family: it gives \(\mathrm{DC}(K_{2,t})=t+1\), and its construction with a block equal to the two-vertex shore cannot be used for secure coalitions because that block is itself secure dominating. The new upper bound relies on this obstruction and on the lack of any partner for a third \(B\)-only block.

This is a classification on the complete bipartite family, not on all graphs of minimum degree two or all complete multipartite graphs. A differently indexed secure-coalition bound for this special family may exist; the inspected statements do not supply its exact upper bound. Exhaustive finite checks are supplemental to the proof.

## References
1. S. Shetty, S. Udupa N. V., and B. R. Rakshith, *Secure coalitions in graphs*, arXiv:2511.21170v2, especially Theorems 2.4, 2.6, 2.8 and the tree section. https://arxiv.org/html/2511.21170v2
2. M. A. Henning and D. A. Mojdeh, *Double Coalitions in Graphs*, Bulletin of the Malaysian Mathematical Sciences Society **48**, article 51 (2025), Theorem 6. https://doi.org/10.1007/s40840-025-01831-7
3. *Secure-domination polynomial of complete multipartite graphs*, Resultary record `2026/10/4/SCOPE-secure-domination-polynomial-of-complete-multipartite-graphs--0ae94d81bd3c`.
