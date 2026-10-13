# Regular Cartesian factors preserve color refinement and yield an exact orbit-refinability criterion

## Finding
For nonempty finite simple undirected graphs \(G,H\), assume that \(H\) is \(d\)-regular, where \(d\ge0\). Write \(P_t(G)\) for the vertex partition obtained after \(t\) ordinary one-dimensional color-refinement rounds, starting from the uniform vertex coloring. Then for every integer \(t\ge0\),
\[
P_t(G\square H)=\{C\times V(H):C\in P_t(G)\}.
\]
Thus the first stable round satisfies \(\operatorname{Stab}(G\square H)=\operatorname{Stab}(G)\).

If in addition \(G,H\) are connected and share no nontrivial Cartesian-prime factor, then \(G\square H\) is **refinable** (its stable partition equals its full automorphism-orbit partition) if and only if \(G\) is refinable and \(H\) is vertex-transitive.

For \(m\ge2\), \(n\ge6\), the connected cylindrical grid \(P_m\square C_n\) is refinable but not amenable to color refinement. Its stabilization round is exactly \(\lfloor(m-1)/2\rfloor\), and the nonisomorphic graph \(P_m\square(C_3\sqcup C_{n-3})\) is indistinguishable from it by color refinement on their disjoint union.

## Assumptions and scope
The Cartesian product \(G\square H\) has vertex set \(V(G)\times V(H)\); two vertices are adjacent if exactly one coordinate moves along an edge of its factor. Color refinement at round \(t+1\) records the previous color and the multiset of previous colors of all neighbors. The stabilization round is the least \(t\ge0\) for which the induced vertex partitions at \(t,t+1\) coincide. The term *refinable* concerns equality of stable color classes with automorphism orbits, not the stronger property *amenable*, which means that color refinement identifies the whole graph against every nonisomorphic graph. These notions are distinct [1]. The relative-primality condition excludes any nontrivial connected graph appearing as a Cartesian-prime factor of both connected graphs; it is needed only for the reverse implication in the orbit criterion [2].

## Proof
**Roundwise lifting.** At round zero both graphs have a single vertex-color class. Suppose that the round-\(t\) partition on the product consists of the fibers \(C\times V(H)\) above classes \(C\in P_t(G)\). Let \(g\in C\). At any \((g,h)\), the multiset of neighbors' round-\(t\) colors equals the multiset contributed by neighbors of \(g\) in \(G\), with exactly \(d\) additional copies of the color of \(C\). The extra multiset does not depend on \(h\) or on the choice of \(g\in C\), and is the same for every element of \(C\). Because the refinement signature includes the old color, two vertices of the product are in the same new class precisely when their \(G\)-coordinates are in the same new class in \(P_{t+1}(G)\). Induction proves the partition identity for all \(t\), and hence the stabilization-time identity.

**Orbit criterion.** By the classical Cartesian prime-factor theorem, for connected relatively prime factors every automorphism of \(G\square H\) preserves both factor-layer systems, and the full automorphism group acts coordinatewise as \(\operatorname{Aut}(G)\times\operatorname{Aut}(H)\) [2]. Thus product orbits have the form \(O_G\times O_H\), for factor automorphism orbits \(O_G,O_H\). The stable color classes, as proved above, are precisely \(C_G\times V(H)\). They are all product orbits exactly when \(H\) has one automorphism orbit and all classes \(C_G\) are automorphism orbits of \(G\). This is the stated equivalence. No prime-factor hypothesis is required for the forward construction: when \(G\) is refinable and \(H\) is vertex-transitive, the coordinatewise subgroup is already transitive on each lifted color class, so the product is refinable.

**Cylinders and nonamenability.** On a path \(P_m\), endpoint degree information propagates one step inward at each refinement round. The stable classes are exactly the pairs of vertices equidistant from their nearer endpoint (or the central singleton), and stabilization occurs at round \(\lfloor(m-1)/2\rfloor\), including the case \(m=2\). The cycle \(C_n\) is \(2\)-regular and vertex-transitive. By the preceding sufficient condition, \(P_m\square C_n\) is refinable and has the same stabilization round as \(P_m\). When \(n\ge6\), the graphs \(C_n\) and \(C_3\sqcup C_{n-3}\) are both \(2\)-regular on \(n\) vertices. Their products with \(P_m\) consequently have identical color-class multiplicities at every round, by the lifting identity (or by running refinement on their disjoint union). The first product is connected and the second disconnected, so they are nonisomorphic. Therefore the connected cylinder is not amenable.

## Verification
The accompanying standalone standard-library script `verify.py` checks the partition-lifting and exact-stabilization formulas on \(405\) graph pairs with regular factors, and confirms the cylinder counterexamples on \(80\) parameter pairs. It checks the equality of color partitions, not just their numbers of blocks. These finite checks are supplementary; the statements for all admissible parameters follow from the preceding induction and product-factor argument.

## Relationship to prior work
Arvind, Köbler, Rattan and Verbitsky [1], especially Sections 2 and 8, define color refinement, *refinable* and *amenable* and prove the surrounding hierarchy. They do not state a roundwise regular-factor lifting law or this Cartesian-product orbit criterion. The classical Sabidussi–Vizing uniqueness theorem, as used explicitly in [2, Section 2], supplies the factor-preserving automorphism statement needed for the reverse orbit implication; it does not control the refinement process. The present theorem links these two otherwise separate structures and yields the connected refinable-but-nonamenable cylinder family with unbounded stabilization depth.

## Limitations
The orbit criterion's **only-if** direction is stated only for connected, relatively prime Cartesian factors. The roundwise lifting law and stabilization identity do not need these hypotheses but do require a regular second factor. The theorem does not say that color refinement distinguishes the graph itself up to isomorphism; the cylinders show that orbit refinement and graph identification differ. Finite script checks cannot replace the infinite proof. Prior-art searching cannot establish absolute priority; an unlocated earlier product-refinement statement remains possible.

## References
[1] V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first publicly posted 2015-02-04, https://arxiv.org/pdf/1502.01255 . Sections 2 and 8.

[2] W. Imrich and S. Klavžar, *Distinguishing Cartesian Powers of Graphs*, Journal of Graph Theory **53** (2006), 250–260, https://doi.org/10.1002/jgt.20190 ; and the accessible extension discussing factor layers in *Cartesian powers of graphs can be distinguished by two labels*, European Journal of Combinatorics **28** (2007), 303–310, https://doi.org/10.1016/j.ejc.2005.07.001 , Section 2 (Sabidussi–Vizing decomposition and automorphism layer preservation).
