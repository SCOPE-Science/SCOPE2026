# Fort hypergraph and fractional zero forcing of double stars
## Finding
Let \(D_{a,b}\), with \(a,b\ge2\), be the double star with adjacent centers \(u,v\), leaf set \(A\) of size \(a\) adjacent to \(u\), and leaf set \(B\) of size \(b\) adjacent to \(v\). The minimal forts of \(D_{a,b}\) are exactly the two-element subsets of \(A\) and the two-element subsets of \(B\). Hence its fort hypergraph is the disjoint union \(K_a\sqcup K_b\), \[\operatorname{ft}(D_{a,b})=\left\lfloor\frac a2\right\rfloor+\left\lfloor\frac b2\right\rfloor,\qquad Z^*(D_{a,b})=\frac{a+b}{2},\qquad Z(D_{a,b})=a+b-2.\] Every optimal fractional zero-forcing weighting gives both centers weight \(0\); on a leaf class of size at least three every leaf has weight \(1/2\), while on a leaf class of size two the two weights may be any complementary pair \(t,1-t\) with \(0\le t\le1\). Thus \(Z(D_{a,b})/Z^*(D_{a,b})=2-4/(a+b)\), so the fort-cover integrality gap approaches \(2\) already within diameter-three trees.

## Assumptions and scope
All graphs are finite, simple, and undirected. For integers \(a,b\ge2\), the double star \(D_{a,b}\) has adjacent centers \(u,v\), a set \(A\) of \(a\) leaves adjacent only to \(u\), and a set \(B\) of \(b\) leaves adjacent only to \(v\).

A nonempty set \(F\subseteq V(G)\) is a fort if every vertex outside \(F\) has either zero or at least two neighbors in \(F\). A fort is minimal if it contains no proper fort. The fort hypergraph has the minimal forts as hyperedges. Its matching number is the fort number \(\operatorname{ft}(G)\), its fractional transversal number is the fractional zero forcing number \(Z^*(G)\), and its transversal number is the ordinary zero forcing number \(Z(G)\).

## Proof
Every two-element subset of \(A\) is a fort: the center \(u\) has two neighbors in it, while every other vertex outside the pair has zero neighbors in it. The same holds for every two-element subset of \(B\).

We now prove these are all minimal forts. Let \(F\) be a fort. If \(u\in F\), then every leaf in \(A\) must also lie in \(F\), because any omitted leaf of \(A\) would be outside \(F\) with exactly one neighbor, namely \(u\), in \(F\). Since \(a\ge2\), such an \(F\) contains a two-leaf fort from \(A\) as a proper subset, so it is not minimal. The same argument excludes \(v\) from every minimal fort.

Therefore a minimal fort contains neither center. For a center outside \(F\), the fort condition becomes
\[
|F\cap A|\ne1,\qquad |F\cap B|\ne1.
\]
Since \(F\) is nonempty, at least one of these two intersections has size at least two. Hence \(F\) contains a two-element fort from one leaf class. Minimality forces \(F\) to equal that pair. Thus
\[
\mathcal F_{D_{a,b}}\cong K_a\sqcup K_b.
\]

The fort number is the matching number of this disjoint union:
\[
\operatorname{ft}(D_{a,b})
=
\left\lfloor\frac a2\right\rfloor+
\left\lfloor\frac b2\right\rfloor.
\]

For the fractional transversal problem, the two leaf classes separate. On a class of size \(m\), the constraints are
\[
x_i+x_j\ge1
\]
for every pair of distinct leaves. Summing all \(\binom m2\) inequalities yields
\[
(m-1)\sum_i x_i\ge\binom m2,
\]
so \(\sum_i x_i\ge m/2\). Equality is attained by assigning weight \(1/2\) to every leaf. Therefore
\[
Z^*(D_{a,b})=\frac a2+\frac b2=\frac{a+b}2.
\]
No minimal-fort constraint contains a center, so an optimum gives both centers weight zero.

When \(m\ge3\), equality in the summed lower bound forces equality in every pair constraint, and the equations \(x_i+x_j=1\) imply \(x_i=1/2\) for all leaves. When \(m=2\), the sole constraint is \(x_1+x_2\ge1\), so the optimal face is exactly \(x_1+x_2=1\). This proves the stated optimizer classification.

Finally, the ordinary zero forcing number is the transversal number of \(K_a\sqcup K_b\). A vertex cover of \(K_m\) has minimum size \(m-1\), hence
\[
Z(D_{a,b})=(a-1)+(b-1)=a+b-2.
\]
Consequently
\[
\frac{Z(D_{a,b})}{Z^*(D_{a,b})}
=
2-\frac4{a+b},
\]
which approaches \(2\).

## Verification
The included checker constructs \(D_{a,b}\) directly for every \(2\le a,b\le6\). It enumerates all vertex subsets to identify forts from the defining neighborhood condition, extracts inclusion-minimal forts, and independently simulates the ordinary zero forcing color-change rule.

It also solves the fractional fort-cover linear program and optimizes every coordinate over the optimum face. The computed minimal forts, optimum values, optimizer coordinate ranges, and ordinary zero forcing numbers agree with the theorem in every tested case.

## Relationship to prior work
The 2023 paper introducing the fort hypergraph, fort number, and this linear-programming fractional zero forcing number proves that \(Z^*(T)\le\ell(T)/2\) for every tree \(T\), where \(\ell(T)\) is the number of leaves, and characterizes the trees for which \(Z^*(T)=Z(T)\). It also determines \(Z^*\) for several standard families and explains that the fort-cover relaxation is governed by minimal forts.

For \(D_{a,b}\), the general tree bound gives only \(Z^*(D_{a,b})\le(a+b)/2\). The present result identifies the entire fort hypergraph, proves equality in that bound for every double star, classifies every fractional optimizer, and simultaneously gives the exact fort number and the integral gap. Exact-phrase and semantic searches for fractional zero forcing, forts, double stars, and bistars did not locate this specialization.

## Limitations
The theorem is restricted to proper double stars with at least two leaves at each center. The finite computations are corroborative only; the all-parameter statement follows from the structural proof. The result concerns the fort-cover fractional zero forcing number introduced via the LP relaxation, not the older three-color forcing parameter with the same descriptive phrase. Search coverage cannot exclude a differently named or non-indexed treatment of double stars.

## References
1. T. R. Cameron, L. Hogben, F. H. J. Kenter, S. A. Mojallal, H. Schuerger, “Forts, (fractional) zero forcing, and Cartesian products of graphs,” arXiv:2310.17904v1, 27 October 2023; Australasian Journal of Combinatorics 95 (2026), 214–247.
2. T. R. Cameron, J. Pulaj, “IP Models for Minimum Zero Forcing Sets, Forts, and Related Graph Parameters,” arXiv:2508.07293v1, 10 August 2025.
