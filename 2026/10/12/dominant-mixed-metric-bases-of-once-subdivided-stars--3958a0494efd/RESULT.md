# Dominant mixed metric bases of once-subdivided stars
## Finding
For every integer \(q\ge3\), let \(S_q\) be the once-subdivided star with center \(c\) and arms
\[
c-u_i-v_i,
\qquad 1\le i\le q.
\]
Then
\[
\gamma_{mr}(S_q)=q+1,
\]
where \(\gamma_{mr}\) is the dominant mixed metric dimension.

More strongly, the minimum mixed resolving dominating sets are exactly
\[
L\cup\{x\},
\qquad
L=\{v_1,\ldots,v_q\},
\qquad
x\in\{c,u_1,\ldots,u_q\}.
\]
Consequently \(S_q\) has exactly
\[
q+1
\]
dominant mixed metric bases.

## Assumptions and scope
For a vertex \(s\) and an edge \(xy\), define
\[
d(s,xy)=\min\{d(s,x),d(s,y)\}.
\]
A set \(W\subseteq V(G)\) is mixed resolving if every two distinct elements of \(V(G)\cup E(G)\) have distinct ordered distance vectors to \(W\). It is dominating if every vertex outside \(W\) has a neighbor in \(W\). A minimum set satisfying both conditions is a dominant mixed metric basis.

The graph \(S_q\) is obtained from \(K_{1,q}\) by subdividing every edge once. The theorem is stated for \(q\ge3\); the case \(q=2\) is the path \(P_5\), already belonging to the path family.

## Proof
Let
\[
L=\{v_1,\ldots,v_q\}.
\]
We first prove a forcing lemma.

Fix an arm \(c-u_i-v_i\), and consider the vertex \(u_i\) and the edge \(u_iv_i\). If \(s\ne v_i\), then every shortest path from \(s\) to \(v_i\) reaches \(u_i\) first. Hence
\[
d(s,u_i)=d(s,u_iv_i).
\]
For \(s=v_i\), however,
\[
d(v_i,u_i)=1,
\qquad
d(v_i,u_iv_i)=0.
\]
Thus \(v_i\) is the unique vertex that distinguishes the element pair \(u_i\) and \(u_iv_i\). Therefore every mixed resolving set contains \(v_i\). Since this holds for every arm,
\[
L\subseteq W
\]
for every mixed resolving set \(W\).

Next we verify that \(L\) itself is mixed resolving. Order the coordinates by \(v_1,\ldots,v_q\). The distance patterns are as follows:
\[
r(c\mid L)=(2,\ldots,2),
\]
while \(u_i\) has coordinate \(1\) at position \(i\) and coordinate \(3\) elsewhere, and \(v_i\) has coordinate \(0\) at position \(i\) and coordinate \(4\) elsewhere. The edge \(cu_i\) has coordinate \(1\) at position \(i\) and coordinate \(2\) elsewhere, whereas the edge \(u_iv_i\) has coordinate \(0\) at position \(i\) and coordinate \(3\) elsewhere. These five pattern types are pairwise different, and the distinguished coordinate \(i\) separates different arms. Hence every vertex and edge has a unique mixed representation to \(L\).

So the mixed metric dimension of \(S_q\) is \(q\), with \(L\) the unique mixed basis. However, \(L\) does not dominate the center \(c\), because every leaf is at distance \(2\) from \(c\). Therefore every mixed resolving dominating set must contain at least one additional vertex:
\[
\gamma_{mr}(S_q)\ge q+1.
\]

If the additional vertex is \(c\), then \(L\cup\{c\}\) dominates the whole graph. If the additional vertex is any \(u_i\), then \(u_i\) dominates \(c\), while each support vertex \(u_j\) is already adjacent to its selected leaf \(v_j\). Thus
\[
L\cup\{u_i\}
\]
is also dominating. Every superset of a mixed resolving set is mixed resolving, so all these \(q+1\) sets are mixed resolving dominating sets of size \(q+1\).

Finally, every minimum set has size \(q+1\) and must contain all of \(L\). Its sole remaining vertex must dominate \(c\), so it must be \(c\) or one of \(u_1,\ldots,u_q\). This proves both the value and the complete basis classification.

## Verification
The included checker constructs \(S_q\) for
\[
3\le q\le8
\]
and computes all vertex-to-vertex and vertex-to-edge distances directly. It exhausts every vertex subset of size at most \(q+1\), verifies the mixed-resolving and domination predicates independently, and compares all minima with the family stated above.

The checker also verifies the stronger structural statement that every mixed resolving set of minimum size is exactly the leaf set.

## Relationship to prior work
Dominant mixed metric dimension was introduced in 2024 as the minimum size of a vertex set that is simultaneously mixed resolving and dominating. The introducing primary paper establishes general bounds and exact values for paths, cycles, stars, wheels, friendship graphs, and complete graphs. Its inspected full text contains no occurrence of spider, subdivision, or tree.

For ordinary mixed metric dimension, trees satisfy the leaf-count formula. On \(S_q\), the theorem above identifies the exact obstruction created by adding domination: the unique mixed basis consists of all leaves, but those leaves miss the center. Exactly one additional center-or-support vertex is necessary and sufficient, and the complete optimum family has size \(q+1\).

Thus the result is not only the ordinary mixed-dimension value for a tree. It determines the effect of the new domination constraint and classifies every optimum combined set.

## Limitations
The theorem treats the once-subdivided star, equivalently the balanced spider with all arm lengths equal to \(2\). It does not give a formula for arbitrary spider arm lengths.

The exhaustive computation through \(q=8\) is corroborative only. The arbitrary-\(q\) theorem follows from the unique-leaf distinguisher lemma and the explicit leaf-set representations.

A differently phrased or non-indexed treatment of the same family may exist despite the targeted searches.

## References
1. R. Alfarisi, S. K. S. Husain, L. Susilowati, A. I. Kristiana, “Dominant Mixed Metric Dimension of Graph,” Statistics, Optimization & Information Computing 12(6) (2024), 1826–1833, DOI 10.19139/soic-2310-5070-1925.
2. A. Kelenc, D. Kuziak, A. Taranenko, I. G. Yero, “Mixed metric dimension of graphs,” Applied Mathematics and Computation 314 (2017), 429–438, DOI 10.1016/j.amc.2017.07.027.
3. A. Ghalavand, S. Klavžar, M. Tavakoli, I. G. Yero, “On mixed metric dimension in subdivision, middle, and total graphs,” Quaestiones Mathematicae 46(12) (2023), 2517–2527, DOI 10.2989/16073606.2023.2169206.
