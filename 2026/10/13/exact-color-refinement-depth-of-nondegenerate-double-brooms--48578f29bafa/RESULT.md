# Exact color-refinement depth of nondegenerate double brooms
## Finding
For integers \(p,q\ge 2\) and \(L\ge 1\), let \(D(p,q;L)\) be the tree obtained from a path
\[
v_0v_1\cdots v_L
\]
by adjoining \(p\) new leaves to \(v_0\) and \(q\) new leaves to \(v_L\). Run ordinary color refinement from the uniform coloring, and let \(\operatorname{Stab}(G)\) be the least round at which the induced vertex partition is stable. Then
\[
\operatorname{Stab}(D(p,q;L))=
\begin{cases}
\max\{1,\lfloor L/2\rfloor\},&p=q,\\[1mm]
\max\{2,\lceil L/2\rceil\},&p\ne q.
\end{cases}
\]

Moreover, the stable color partition is exactly the automorphism-orbit partition. In the balanced case \(p=q\), all pendant leaves lie in one orbit and the spine positions are paired by reflection \(v_i\leftrightarrow v_{L-i}\), so the stable partition has
\[
1+\left\lceil\frac{L+1}{2}\right\rceil
\]
classes. In the unbalanced case \(p\ne q\), the two leaf sets are distinct orbits and every spine vertex is a singleton orbit, so the stable partition has \(L+3\) classes.

## Assumptions and scope
Graphs are finite, simple, undirected, and initially uncolored. The parameters \(p,q\ge2\) make both ends genuine branching vertices; this is the nondegenerate double-broom subfamily. The spine length \(L\) is the number of edges joining the two branching vertices. Round \(0\) is the uniform coloring. Each later round replaces the color of a vertex by its previous color together with the multiset of previous colors of its neighbors. Stabilization refers to the induced partition, not to the literal color labels.

## Proof
Suppose first that \(p=q\). In round \(1\), the pendant leaves, the two branching vertices, and—when present—the internal degree-\(2\) spine vertices are separated by degree. The reflection of the whole tree interchanging the two ends is an automorphism, so \(v_i\) and \(v_{L-i}\) can never be separated.

For \(r\ge1\), refinement propagates from both branching vertices one spine edge per round. Inductively, after round \(r\), every spine vertex whose distance from the nearer branching vertex is less than \(r\) has its final reflection-orbit color, while any still-unresolved central block is monochromatic up to the forced reflection symmetry. Hence the last possible strict split occurs when the two refinement fronts meet. For \(L\ge2\), this happens in round \(\lfloor L/2\rfloor\). For \(L=1\), the degree partition from round \(1\) is already stable. Thus
\[
\operatorname{Stab}(D(p,p;L))=\max\{1,\lfloor L/2\rfloor\}.
\]
At stability, the only equal-colored spine positions are reflection pairs, and all leaves are in one orbit under end-swapping together with permutations within each leaf set. This proves both the balanced depth formula and the orbit statement.

Now suppose \(p\ne q\). The branching vertices have distinct degrees \(p+1\) and \(q+1\), so round \(1\) distinguishes the two ends. In round \(2\), the two pendant-leaf sets split because their unique neighbors already have different colors. From the same point onward, the two colored ends of the spine act as distinct boundary conditions.

For each \(r\ge1\), an induction along the path shows that round \(r\) has propagated the left-end color information through the first \(r-1\) spine edges and the right-end information through the last \(r-1\) spine edges. Since the two boundary colors differ, no nontrivial reflection can preserve colors. The remaining unresolved central interval shrinks by two vertices per round, and the last strict spine split occurs in round \(\lceil L/2\rceil\). Independently, the pendant leaves cannot reach their final two-orbit partition before round \(2\). Therefore
\[
\operatorname{Stab}(D(p,q;L))
=\max\left\{2,\left\lceil\frac L2\right\rceil\right\}
\qquad(p\ne q).
\]
After these two processes finish, each spine position is uniquely determined by its ordered distances from the two differently colored ends, while each leaf set is internally transitive under permutations. Thus the stable partition is exactly the automorphism-orbit partition.

## Verification
The accompanying standalone program `verify.py` constructs the full graph and implements ordinary color refinement without graph-library dependencies. It checks every
\[
2\le p,q\le20,\qquad 1\le L\le40.
\]
For each of the \(14{,}440\) parameter triples it verifies both the exact stabilization formula and equality of the stable partition with the explicit automorphism-orbit partition.

It returns:

`VERIFY_OK depth_checks=14440 orbit_checks=14440 p,q=2..20 L=1..40`

The finite computation is corroborative only. The all-parameter theorem rests on the propagation argument above.

## Relationship to prior work
Double brooms are a standard named tree family. Tiner defines a double broom as two stars connected by a path and studies the family in the Erdős--Sós problem. A 2015 reconstruction paper by Ma, Shi, and West likewise treats double brooms as a named parameterized family. These sources establish that the object is independently motivated by extremal and reconstruction questions; they do not study color-refinement iteration depth.

Krebs and Verbitsky formalize color-refinement stabilization depth and its relation to truncated universal covers. Their general framework explains the local propagation mechanism used here but does not give a double-broom formula.

Targeted searches using double-broom, bistar, two stars joined by a path, color refinement, \(1\)-WL, Weisfeiler--Leman, equitable partitions, stabilization depth, and automorphism orbits did not locate an equivalent exact formula.

## Limitations
The theorem assumes \(p,q\ge2\). Degenerate cases with one pendant leaf at an end interact with the degree-\(2\) spine and require separate boundary formulas. The result concerns ordinary one-dimensional color refinement from the uniform coloring only; it does not address irregular caterpillars, higher-dimensional Weisfeiler--Leman refinement, or graph-pair distinguishing depth. The literature search was targeted rather than exhaustive, and no independent literature audit has been performed.

## References
1. G. Tiner, *On the Erdős--Sós Conjecture and Double-brooms*, Journal of Combinatorial Mathematics and Combinatorial Computing 93 (2015), 291--296, published 31 May 2015.
2. M. Ma, H. Shi, and D. B. West, *The adversary degree-associated reconstruction number of double-brooms*, Journal of Discrete Algorithms 33 (2015), DOI: 10.1016/j.jda.2015.03.008.
3. A. Krebs and O. Verbitsky, *Universal covers, color refinement, and two-variable counting logic: Lower bounds for the depth*, arXiv:1407.3175, first posted 11 July 2014.
