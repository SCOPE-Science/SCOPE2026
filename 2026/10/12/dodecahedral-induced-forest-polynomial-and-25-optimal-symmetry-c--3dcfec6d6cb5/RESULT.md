# Dodecahedral induced-forest polynomial and 25 optimal symmetry classes

## Finding
Let \(D\) be the 20-vertex dodecahedral graph. For every integer \(0\leq k\leq20\), let \(f_k\) count vertex subsets \(S\subseteq V(D)\) of cardinality \(k\) such that the *induced* graph \(D[S]\) is acyclic; the empty set counts. Then the complete polynomial is
\[
\begin{aligned}
F_D(z)={}&1+20z+190z^2+1140z^3+4845z^4+15492z^5\\
&+38580z^6+76260z^7+120540z^8+151920z^9\\
&+150480z^{10}+113400z^{11}+60620z^{12}\\
&+19600z^{13}+2520z^{14}.
\end{aligned}
\]
All remaining coefficients vanish. In particular \(F_D(1)=755608\), and there are \(2520\) maximum induced forests, each of order \(14\). Under the full graph automorphism group of order \(120\), they form exactly \(25\) orbits, of sizes \(120\) (18 orbits), \(60\) (5), \(40\) (one) and \(20\) (one).

Of those maximum forests, \(1860\) are trees. The other \(660\) have exactly two components, with sizes \((1,13)\) for \(280\) subsets, \((2,12)\) for \(180\), \((4,10)\) for \(120\), \((6,8)\) for \(60\), and \((7,7)\) for \(20\). There are exactly \(1120\) inclusion-maximal induced forests of order \(13\), exactly \(2520\) of order \(14\), and none of another order. Thus the graph's inclusion-minimal feedback vertex sets have sizes \(7\) and \(6\), respectively, with those counts.

## Assumptions and scope
All graphs are finite, simple, and undirected. Use the explicit generalized Petersen representation \(D=GP(10,2)\). Its vertex set is \(\{u_i,v_i:0\leq i<10\}\), with all subscripts read modulo \(10\). Its \(30\) edges are exactly \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\), for each \(i\in\{0,\ldots,9\}\). This is the ordinary dodecahedral graph, with \(20\) vertices and degree \(3\). The bit position for \(u_i\) is \(i\), and that for \(v_i\) is \(10+i\). Each subset is counted once, with no quotient by graph symmetry in \(F_D\). An induced forest includes disconnected forests and the empty graph; inclusion-maximal means maximal under adding a vertex, not maximum cardinality.

## Proof
**Finite exhaustiveness and the polynomial.** Every vertex subset has exactly one binary encoding \(m\in\{0,\ldots,2^{20}-1\}\). For each \(m\), the C++ verifier constructs the induced edge set by testing both endpoints against \(m\). It inserts those edges in a disjoint-set union data structure starting from isolated vertices. An edge whose endpoints already have the same representative closes a cycle. Conversely, any cycle causes such a failed union when its final edge is inserted, so acceptance is equivalent to acyclicity. There are exactly \(2^{20}=1048576\) masks; the program checks every one and increments the coefficient for the exact population count. Its enumerated coefficients are exactly those displayed above, including six trailing zeros, and sum to \(755608\).

**Independent acyclicity test and component structure.** A second, independent Python verifier reconstructs all connected components of each induced subset by breadth-first search. A finite simple undirected graph with \(k\) vertices, \(e\) edges and \(c\) components is a forest if and only if \(e=k-c\). Its complete set of accepted masks agrees with the displayed coefficient vector. The verifier records all \(2520\) masks of weight \(14\) and independently determines their component-size spectrum.

For any six-vertex deleted set \(T=V(D)\setminus S\), cubic degree-sum counting gives \(|E(D[S])|=30-3|T|+|E(D[T])|=12+|E(D[T])|\). For a 14-vertex induced forest with \(c\) components, the forest identity gives \(|E(D[S])|=14-c\), hence \(c=2-|E(D[T])|\). In particular, \(T\) has no edges when there are two forest components and exactly one edge when the forest is connected. The verifier tests this equality for every optimum mask: \(660\) have no deleted-set edges and \(1860\) have exactly one. The recorded component sizes sum to the full count and exhaust all possibilities in this graph.

**Inclusion-maximal configurations.** A forest mask \(m\) is inclusion-maximal precisely when, for every vertex \(w\) not in it, the graph obtained by adding \(w\) is cyclic. Since both programs have recorded the forest status of *every* mask, checking all at most \(20\) one-vertex extensions for each accepted mask is exhaustive. The result is \(1120\) maximal masks of weight \(13\) and \(2520\) of weight \(14\), with none at another weight. Complementation exchanges these with inclusion-minimal cycle-hitting vertex sets, without changing their distinctness.

**Complete symmetry classification.** The Python verifier constructs all automorphisms as bijections on the \(20\) labelled vertices preserving both edges and nonedges. Its backtracking algorithm assigns vertices one at a time and prunes an assignment only if it disagrees with a previously assigned adjacency, so every adjacency-preserving permutation remains in its search tree; at a complete assignment all pairs have been checked. It finds exactly \(120\) permutations. For each of the \(25\) representatives in `orbit_certificates.csv`, it computes all images under these permutations, checks the asserted orbit size, checks the vertex and component certificates, and subtracts the orbit from the set of all \(2520\) optimum masks. The orbits are disjoint and exhaust that set. Their total \(18\cdot120+5\cdot60+40+20=2520\) proves the asserted orbit census; \(17\) of the orbits consist of trees and \(8\) of two-component forests.

## Verification
The package contains **two standalone implementations** and a machine-readable orbit certificate. Run in a directory containing the three files:

```sh
c++ -O2 -std=c++17 verify_census.cpp -o verify_census
./verify_census
python3 verify_orbits.py orbit_certificates.csv
```

The C++ program exhausts all vertex masks using cycle-detecting union/find. The Python program independently exhausts masks using component search and the Euler forest identity, and checks every complete automorphism and certified orbit. Both test against explicit expected totals and terminate with assertions if a check fails. Success markers include `CENSUS_OK`, `FORESTS_OK`, `AUT_OK`, and `ORBITS_OK`.

## Relationship to prior work
Bau's survey [1] defines decycling sets and their equivalence to complements of induced forests. Kowalik, Lužar and Škrekovski [2] explicitly use the dodecahedron's \(14\)-vertex induced forest and \(7/10\) forest ratio as a sharpness example motivating girth-five planar forest bounds (their introduction and Figure 1). Thus neither the extremal forest order \(14\) nor the resulting minimum deletion cardinality \(6\) is new. Wei and Li [3], and Gao and collaborators [4], study the decycling *number* of generalized Petersen graphs, a scalar invariant. The new claim here is the entire induced-forest polynomial, the inclusion-maximal profile, component types of all optimum forests, and the exhaustive \(25\)-orbit classification. The accessible passages of [1] and [2] do not state these refined results. The full texts of [3] and [4] could not be inspected; their possible additional statements remain a priority risk, despite abstracts and bibliographies emphasizing the scalar invariant.

## Limitations
This is an exact finite classification only of the specified \(20\)-vertex graph, not a theorem about all generalized Petersen graphs or all planar girth-five graphs. The computer-assisted proof depends on the independently supplied exhaustive checkers and the stated bit labelling; finite enumerations should not be extrapolated to infinite families. No independent external mathematical audit has been performed. Searches and accessible literature do not establish absolute historical novelty; especially [3] and [4] remain incompletely accessible. The optimum order and decycling number were already known.

## References
[1] S. Bau, *The Decycling Number of Graphs*, arXiv:math/0703544v1, first posted 2007-03-19. https://arxiv.org/pdf/math/0703544

[2] Ł. Kowalik, B. Lužar and R. Škrekovski, *An improved bound on the largest induced forests for triangle-free planar graphs*, Discrete Mathematics and Theoretical Computer Science 12(1) (2010), 87–100, DOI 10.46298/dmtcs.487. https://dmtcs.episciences.org/487/pdf

[3] E.-L. Wei and Y.-F. Li, *Decycling Number and Upper-Embeddibility of Generalized Petersen Graphs*, Acta Mathematica Sinica, Chinese Series 56(2) (2013), 211–216, DOI 10.12386/A2013sxxb0022. Abstract and bibliographic page inspected; full text unavailable.

[4] L. Gao, X. Xu, J. Wang, D. Zhu and Y. Yang, *The decycling number of generalized Petersen graphs*, Discrete Applied Mathematics 181 (2015), 297–300, DOI 10.1016/j.dam.2014.09.005. Bibliographic and abstract evidence inspected; full text unavailable.
