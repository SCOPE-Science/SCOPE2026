# Exact color-refinement depth of almost-equilateral subdivided stars

## Finding

For integers \(d\ge 3\) and \(1\le a\le c\), let \(S_d(a,c)\) be the tree obtained from \(K_{1,d}\) by giving \(d-1\) arms length \(a\) and the remaining arm length \(c\), where arm lengths are counted in edges from the center to a leaf. Let \(C^0\) be the uniform vertex coloring and define ordinary color refinement by
\[
C^{r+1}(v)=\left(C^r(v),\{\!\{C^r(w):w\sim v\}\!\}\right).
\]
Write \(\operatorname{Stab}(G)\) for the least \(s\) for which \(C^{s+1}\) and \(C^s\) induce the same partition of \(V(G)\).

Then
\[
\operatorname{Stab}(S_d(a,c))=
\begin{cases}
\lceil a/2\rceil,&c=a,\\
\max\{a+1,\lceil c/2\rceil\},&c>a.
\end{cases}
\]

There is also an exact description of every intermediate partition. For \(r\ge1\), the center has its own type. A leaf on an arm of length \(L\) has descriptor
\[
\bigl(\mathrm{leaf},\min\{L,r\}\bigr),
\]
and an internal vertex at distance \(x\) from the center on an arm of length \(L\) has descriptor
\[
\bigl(\mathrm{internal},\min\{x,r\},\min\{L-x,r\}\bigr).
\]
Two vertices have the same round-\(r\) color if and only if these typed descriptors agree.

## Assumptions and scope

Graphs are finite, simple, undirected, and uncolored at the start. The parameter \(d\) is at least \(3\), so the center is the unique vertex of degree \(d\). The family \(S_d(a,c)\) is an almost-equilateral subdivided star: all but at most one arm have the same length.

The statement concerns the ordinary one-dimensional Weisfeiler--Leman procedure, also called vertex color refinement. It does not claim an analogous formula for arbitrary subdivided stars with several distinct arm lengths.

## Proof

Krebs and Verbitsky show that the round-\(r\) color of a vertex is exactly the isomorphism type of the universal cover rooted at that vertex and truncated at depth \(r\). On a tree the universal cover is the tree itself, so equality of round-\(r\) colors is equality of rooted radius-\(r\) truncations.

Fix a vertex on an arm of length \(L\). If the vertex is internal and lies \(x\) edges from the center, then its two special endpoints are the center, at distance \(x\), and the leaf of its own arm, at distance \(L-x\). At round \(r\), an endpoint type affects the rooted truncation exactly when its distance is strictly below \(r\); if its distance is at least \(r\), the truncation ends before the endpoint's degree can be seen. Consequently the only information carried by the two directions along the arm is the ordered pair
\[
\bigl(\min\{x,r\},\min\{L-x,r\}\bigr).
\]
The order matters because the center has degree \(d\) whereas a leaf has degree \(1\). The center and leaves themselves are already separated from internal vertices in the first refinement by degree, and a leaf's round-\(r\) color is determined by \(\min\{L,r\}\).

It remains to check that seeing through the center does not create an earlier distinction than these descriptors record. Suppose two internal vertices have the same descriptor while lying on arms of different lengths. Their distances from the center agree, say \(x\), and both leaf distances are at least \(r\). Hence \(r\le a-x\). Any difference between the other arms beyond the center would require looking more than \(a\) edges past the center, which from the rooted vertex requires depth greater than \(x+a\), impossible under \(r\le a-x\). Thus the descriptor is both necessary and sufficient.

Now assume first that \(c=a\). All arms are equivalent under automorphisms, so stabilization is reached exactly when the map
\[
x\longmapsto \bigl(\min\{x,r\},\min\{a-x,r\}\bigr)
\]
is injective for the internal positions \(1\le x\le a-1\). The only possible collision consists of positions with both coordinates equal to \(r\), namely
\[
r\le x\le a-r.
\]
There are at most one such positions exactly when \(a-2r+1\le1\), equivalently \(r\ge a/2\). Therefore the least stable round is \(\lceil a/2\rceil\).

Now assume \(c>a\). The short and long leaves remain the same color through round \(a\), because their descriptors are both \((\mathrm{leaf},a)\), and split in round \(a+1\). Hence
\[
\operatorname{Stab}(S_d(a,c))\ge a+1.
\]
Within the long arm, the internal descriptors are injective exactly when the interval of positions with both coordinates clipped to \(r\) has size at most one. This gives the second lower bound
\[
r\ge \lceil c/2\rceil.
\]
Conversely, once \(r\ge a+1\), every vertex on a short arm has its full distance to the short leaf visible, so short-arm positions and the long arm are separated correctly; and once \(r\ge\lceil c/2\rceil\), the long-arm descriptor is injective by position. The center is already unique. Therefore the stable partition has been reached at
\[
r=\max\{a+1,\lceil c/2\rceil\},
\]
which proves the formula.

## Verification

A standalone checker implements color refinement directly and also computes the predicted descriptor partition. It exhaustively verified the depth formula for
\[
3\le d\le8,\qquad 1\le a\le20,\qquad a\le c\le50,
\]
covering \(4860\) parameter triples. It also compared every intermediate color partition against the descriptor formula for
\[
3\le d\le7,\qquad 1\le a\le10,\qquad a\le c\le25,
\]
for \(10650\) round-level checks. The checker returned:

`VERIFY_OK depth_cases=4860 profile_checks=10650 d_depth=3..8 a_depth=1..20 c_depth=a..50 d_profile=3..7 a_profile=1..10 c_profile=a..25`

The computation is only a finite consistency check; the proof above establishes the statement for all permitted parameters.

## Relationship to prior work

Krebs and Verbitsky formalize color refinement, define \(\operatorname{Stab}(G)\), and prove that round-\(r\) colors coincide exactly with depth-\(r\) truncations of universal covers. They also study worst-case linear stabilization depth and note paths as simple examples producing linear logical depth. Their paper supplies the general local-view mechanism used here, but it does not state the closed formula above for almost-equilateral subdivided stars.

Targeted searches under the terms “subdivided star,” “spider tree,” “color refinement,” “Weisfeiler--Leman,” “equitable partition,” and “stabilization” did not locate an exact formula matching this family. A semantic search result about spider trees concerned a different invariant, curvature distortion, and does not imply the refinement-depth statement.

## Limitations

The theorem treats exactly one exceptional arm length. With two or more distinct exceptional arm lengths, viewing through the center can couple several branch-length signals, so the same two-parameter formula need not hold.

The originality assessment is based on targeted searches and inspection of the most directly relevant color-refinement source, not on a proof that no equivalent statement occurs anywhere in the literature.

## References

1. Andreas Krebs and Oleg Verbitsky, “Universal covers, color refinement, and two-variable counting logic: Lower bounds for the depth,” arXiv:1407.3175, first submitted 11 July 2014; LICS 2015, pp. 689–700.
