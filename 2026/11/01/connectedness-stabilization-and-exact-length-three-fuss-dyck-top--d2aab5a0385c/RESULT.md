# Connectedness stabilization and exact length-three Fuss–Dyck topology

## Finding
Let \(\Delta_{n,b}=\Delta_{\mathrm{Dyck}_n}^{(1,b)}\) be the simplicial complex whose faces are valley-position sets of rational Dyck words with \(nb\) up-steps and \(n\) down-steps, subject at every prefix to \(\#U\ge b\,\#D\). For every pair of positive integers \(n\ge2\), \(b\ge1\), its number of vertices is \(b\binom n2\), and its number of connected components is
\[
\#\pi_0(|\Delta_{n,b}|)=\begin{cases}b,&n=2,\\2,&n\ge3.\end{cases}
\]
For \(n\ge3\), exactly one vertex is isolated, namely the valley immediately after the first down-step when \(nb-1\) up-steps have occurred. Every other vertex lies in one connected component. In particular \(\widetilde H_0(\Delta_{n,b};\mathbb Z)\cong\mathbb Z\) for \(n\ge3\), whereas \(\widetilde H_0(\Delta_{2,b};\mathbb Z)\cong\mathbb Z^{b-1}\).

For \(n=3\), the entire complex is a graph. Put \(\beta_b=(3b-4)(b-1)/2\). Then
\[
|\Delta_{3,b}|\simeq\bigl(\bigvee^{\beta_b}S^1\bigr)\sqcup\{\mathrm{pt}\},\qquad
\widetilde H_1(\Delta_{3,b};\mathbb Z)\cong\mathbb Z^{\beta_b}.
\]
The reduced integral homology vanishes in every other degree except degree zero, in which it equals \(\mathbb Z\). A wedge of zero circles is interpreted as a point.

With the nonpure \(f\)- and \(h\)-polynomial conventions of Mu--Welker, the exact polynomials for every \(b\ge1\) are
\[
\mathfrak f_{3,b}(x,y)=x^2y^2+(3b-1)x^2y+\frac{b(3b-1)}2x^2+x,
\]
\[
\mathfrak h_{3,b}(x,y)=x^2y^2+(3b-3)x^2y+\frac{(3b-4)(b-1)}2x^2+x.
\]
Thus the nonzero \(h\)-triangle coefficients are \(h_{2,0}=1\), \(h_{2,1}=3b-3\), \(h_{2,2}=\beta_b\), and \(h_{1,1}=1\); coincident zero entries at \(b=1\) are understood.

## Assumptions and scope
Throughout \(n\ge2\) and \(b\ge1\) are integers. A valley is an adjacent \(DU\) in a word. In the source's coordinate convention its position is the pair consisting of its index after the \(D\) and the height \(\#U-\#D\) at that point. This is the same as recording \((k,u)\), the number \(k\) of down-steps and \(u\) of up-steps before the following \(U\): the source position is \((u+k,u-k)\), so the two descriptions are bijectively equivalent. A face is precisely the valley set of one admissible word (not an arbitrary multiset of valley labels). The empty face is included. The geometric realization is used in the component and homotopy assertions.

## Proof
**Vertex classification.** Every valley is just after the \(k\)-th down-step, with \(1\le k\le n-1\). If the number of up-steps before that down-step is \(u\), admissibility forces \(u\ge kb\), while existence of the following up-step forces \(u\le nb-1\). Conversely every such \((k,u)\) is realizable: take a word \(U^uD^kU^{nb-u}D^{n-k}\). Its early down-step prefixes are admissible because \(u\ge kb\), and all remaining down-steps occur after all \(nb\) up-steps. This word contains the valley immediately after the \(k\)-th down-step. Hence the complete vertex set is \(\{(k,u):1\le k\le n-1,\ kb\le u\le nb-1\}\), with cardinality \(\sum_{k=1}^{n-1}(nb-kb)=b\binom n2\).

**Connectivity for \(n\ge3\).** Denote \(A_u=(1,u)\) and \(B_u=(2,u)\). The vertex \(A_{nb-1}\) is isolated: a different valley cannot occur before the first down-step, and any later valley would require at least one additional up-step strictly beyond \(nb-1\) before the subsequent down-step, leaving none for its following up-step. Every vertex \((k,u)\) with \(k\ge2\) is adjacent to \(A_b\), because the word
\[
U^bD\,U^{u-b}D^{k-1}U^{nb-u}D^{n-k}
\]
is admissible and displays both valleys \(A_b\) and \((k,u)\). Indeed \(u\ge kb\), and all steps after the last indicated up-run are down-steps. Every remaining \(A_u\) satisfies \(b\le u\le nb-2\) and is adjacent to \(B_{nb-1}\), by the admissible word
\[
U^uD\,U^{nb-1-u}D\,UD^{n-2}.
\]
Here \(nb-1\ge2b\) since \(n\ge3\). The vertex \(B_{nb-1}\) is itself adjacent to \(A_b\) by the preceding \(k=2\) construction. Thus the graph on all vertices except \(A_{nb-1}\) is connected, and there are precisely two components. For \(n=2\) only vertices \((1,u)\), \(b\le u\le2b-1\), occur, and there cannot be two valleys with only two down-steps; hence all \(b\) are isolated. The degree-zero integral homology assertions follow from the component counts.

**Exact length-three graph.** When \(n=3\), write \(A_u=(1,u)\) with \(b\le u\le3b-1\), and \(B_v=(2,v)\) with \(2b\le v\le3b-1\). Each word has at most two valleys. Two vertices span an edge if and only if they are \(A_u,B_v\) with \(u<v\). Necessity comes from increasing up-step counts between successive valleys. For sufficiency use \(U^uDU^{v-u}DU^{3b-v}D\), which satisfies the prefix condition because \(u\ge b\) and \(v\ge2b\). No edge connects vertices of the same type. This gives \(3b\) vertices and
\[
E=\sum_{v=2b}^{3b-1}(v-b)=\frac{b(3b-1)}2
\]
edges. The connected nonisolated component has \(3b-1\) vertices, so its cycle rank is \(E-(3b-1)+1=(3b-4)(b-1)/2\). Every connected finite graph has the homotopy type of a wedge of as many circles as its cycle rank, establishing the homotopy and homology classification.

**Nonpure face triangles.** The isolated singleton has degree one, all other vertices have degree two, and the empty face has degree two because edges exist for every \(b\ge1\). The edges have degree two. Thus \(f_{2,0}=1\), \(f_{2,1}=3b-1\), \(f_{1,1}=1\), and \(f_{2,2}=E\). In Mu--Welker's convention \(\mathfrak f(x,y)=\sum_{i\ge j}f_{i,j}x^iy^{i-j}\) and \(\mathfrak h(x,y)=\mathfrak f(x,y-1)\). Substitution and expansion give precisely the two claimed polynomial formulas.

## Verification
An independently structured finite-word enumeration in `verify_dyck_n3.py` checks the complete vertex/edge sets and both component counts without using the proof's proposed edge rule. The standalone program exhaustively checks \(n=3\) for \(1\le b\le10\), and component structure for several higher parameters: \((n,b)=(4,1),(4,2),(4,3),(4,4),(5,1),(5,2),(5,3),(6,1),(6,2)\). These are finite corroborations; the unrestricted statements follow from the constructions above.

## Relationship to prior work
Mu and Welker (2026, arXiv:2609.14054) introduce the rational Dyck valley simplicial complexes, prove their shellability, and explicitly ask for interpretations of their \(f\)- and \(h\)-triangle statistics. Their appendix tabulates selected short parameters, including the reversed-and-swapped counterpart of the \(b=2,3\) cases. Neither those finite tables nor shellability itself determines the stated all-parameter component formula or the closed length-three \(f\)- and \(h\)-triangles. The involution reversing a Dyck word while interchanging \(D\) and \(U\) identifies the \((1,b)\) and \((b,1)\) valley complexes and is taken into account when comparing finite tables. Armstrong, Rhoades and Williams (2013) define rational associahedra using Dyck paths, but their faces and homotopy objects are different; their general enumeration does not imply this theorem.

## Limitations
The explicit circle-wedge and two-variable face-polynomial formulas are proved only at rational Dyck length three. For lengths at least four, the result determines components and reduced degree-zero homology, not higher integral homology, geometric realizations, or the full nonpure \(f\)- and \(h\)-triangles. The published tables already cover small special parameters up to their stated word reversal symmetry; those individual finite entries are not presented as new. This is not an independent mathematical validation, and unindexed or implicitly formulated equivalent prior results cannot be ruled out completely.

## References
1. L. Mu and V. Welker, *Simplicial Complexes of Antichains in Root Posets and Related Combinatorics of Dyck Paths*, arXiv:2609.14054, first submitted September 12, 2026; Sections 2--3, Question 3.0, Appendix. https://arxiv.org/abs/2609.14054
2. D. Armstrong, B. Rhoades and N. Williams, *Rational associahedra and noncrossing partitions*, Electron. J. Combin. 20 (2013), Paper 54, arXiv:1305.7286. https://arxiv.org/abs/1305.7286
