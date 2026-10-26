# Hamiltonian-cycle incidence closure: exact closed sets and optimal one-round Horn bases

## Finding
For every integer \(n\ge4\), let \(E_n=\binom{[n]}2\), and let \(\mathcal H_n\) be the family of edge sets of all undirected Hamiltonian cycles of \(K_n\). Define
\[
\Phi_n(S)=\bigcap\{H\in\mathcal H_n:S\subseteq H\},\qquad S\subseteq E_n,
\]
where an intersection over no cycles equals \(E_n\). This is the attribute closure of the formal context with Hamiltonian cycles as objects, edges as attributes, and containment as incidence.

**Exact structural theorem.** A closed set is precisely one of the following: \(E_n\); a Hamiltonian-cycle edge set; or a spanning linear forest (isolated vertices allowed) with either at least four components, exactly three components of which at most one is a singleton, or exactly two components both having at least two vertices. In particular, a spanning linear forest with three components and exactly two isolated vertices forces the edge joining those isolated vertices; a path on \(n-1\) vertices plus one isolated vertex forces its unique Hamiltonian cycle; and a spanning Hamiltonian path forces its closing edge. All other consistent linear forests force no further edges.

**Sharp direct-implication theorem.** A *simultaneous one-round Horn base* is a family of implications \(A\to B\) with nonempty conclusions such that, for every \(S\subseteq E_n\),
\[
\Phi_n(S)=S\cup\bigcup_{A\to B,\ A\subseteq S}B.
\]
Conclusions may contain several edges, and the objective counts implications, not individual consequent edges. The exact minimum number of implications is
\[
b_n=\begin{cases}
6,&n=4,\\[2pt]
\displaystyle \frac{n!}{4}+n\binom{n-1}{3}+\frac12\sum_{k=3}^{n-1}\binom nk(k-1)!,&n\ge5.
\end{cases}
\]
For \(n\ge5\), one optimal direct base contains exactly three kinds of implications: (i) the edges of each unoriented path on \(n-2\) vertices imply the edge joining the two unused vertices; (ii) each three-edge star implies all of \(E_n\); (iii) each proper simple cycle (length between \(3\) and \(n-1\)) implies all of \(E_n\). For \(n=4\), only the six path implications of type (i) are needed. This is a minimum *one-round* cardinality; no assertion is made that it minimizes the number of rules among bases permitted to iterate through multiple rounds.

**Exact lattice cardinality.** Let \(f_{n,k}\) count all labeled spanning linear forests of \(K_n\) with \(k\) edges. These numbers have the explicit bivariate exponential generating function
\[
\sum_{n\ge0}\sum_{k\ge0}f_{n,k}\,t^k\frac{z^n}{n!}
=\exp\!\left(z+\frac{z^2t}{2(1-zt)}\right).
\]
The number of elements in the closed-set lattice is
\[
|\mathcal L_n|=1+\frac{(n-1)!}{2}+\sum_{k=0}^{n-2}f_{n,k}-\frac{3n!}{4}.
\]
For \(n=4,5,6,7,8\), respectively, these counts are \(8,69,647,6473,69813\).

## Assumptions and scope
All graphs are finite, labeled, undirected, loopless and simple. A linear forest is a disjoint union of ordinary paths, including isolated vertices as paths of order one. All components are counted on the full ground set \([n]\). A proper cycle has fewer than \(n\) vertices. A Hamiltonian cycle is identified with its edge set, so reversal and rotation are not distinguished. The conclusions to \(E_n\) use the usual formal-context convention that an inconsistent premise has closure equal to the full attribute set, not that an inconsistent edge set extends to a Hamiltonian cycle. The direct-basis extremum allows aggregated, multi-edge conclusions; no restriction to unit implications is made.

## Proof
**1. Extendibility and the block lemma.** An edge set contained in a Hamiltonian cycle has maximum degree two and no cycle smaller than \(n\). Thus it is either a Hamiltonian cycle or a linear forest. Conversely, every spanning linear forest extends to a Hamiltonian cycle in \(K_n\): orient each path component, arrange the components cyclically, and join successive endpoints. For a single spanning path join its two endpoints. If a chosen edge set violates these conditions, no Hamiltonian extension exists and its closure is \(E_n\).

Consider a spanning linear forest with \(r\) components. Every containing Hamiltonian cycle consists of the fixed path edges and links between path endpoints, corresponding exactly to the cyclic arrangements and path orientations just described. This exhausts extensions, since a vertex already of degree two in the forest cannot acquire another edge. We can therefore determine the links common to *all* extensions:

* If \(r=1\), the forest is a spanning path and the link between its endpoints is compulsory.
* If \(r=2\) and one component is an isolated vertex, the two links from that singleton to both endpoints of the other path are compulsory. If both components are nontrivial, reversing the orientation of one path produces two different pairings, with no compulsory link.
* If \(r=3\) and two components are singleton vertices, those vertices are adjacent in the cyclic order of the three blocks, giving exactly one compulsory link between them. If there is at most one singleton, independently reversing a nontrivial block rules out every particular candidate interblock edge; there is no compulsory link.
* If \(r\ge4\), any specified two components can be arranged nonadjacently in a cyclic order of the blocks, so no intercomponent edge is compulsory. (An internal edge not in the forest cannot occur in any extension, since that would raise an internal vertex degree or close one component prematurely.)

The two-block and three-block cases also show that the forced-edge result is itself a closed linear forest unless it is a Hamiltonian cycle. This proves the structural theorem, including the complete closed-set list.

**2. The direct construction.** A path on \(n-2\) vertices, with the two complementary vertices isolated, has exactly three path components and hence forces the edge joining the complement. An occupied three-edge star cannot extend to any Hamiltonian cycle because its center has degree three. Likewise a proper cycle is already a premature cycle. Each proposed implication is therefore valid.

If \(S\) is inconsistent, it contains a three-edge star or a proper cycle: any set with a vertex of degree at least three contains the star, and a maximum-degree-two set with a proper cycle contains that cycle. The corresponding implication yields all of \(E_n\) in one round. For a consistent forest, the block lemma gives only three possible nontrivial completions. The three-component/two-singleton case triggers its full \(n-2\)-vertex path premise. In the two-component/one-singleton case, the two subpaths obtained by deleting respectively either endpoint of the large path each contain \(n-2\) vertices, forcing the two edges incident to the singleton. For a spanning path, the interior \(n-2\)-vertex subpath forces the edge between the two endpoint vertices. Hence all compulsory edges appear simultaneously in a single round. For a Hamiltonian cycle all rule conclusions are already present, by soundness. The same path-only construction works for \(n=4\); the six singleton-edge premises collectively complete both any three-edge star and any triangle to all six edges. Thus the stated systems are direct.

**3. Exact minimality among one-round systems.** For an arbitrary one-round base, if some \(e\in\Phi_n(A)\) lies outside
\[
A\cup\bigcup_{B\subsetneq A}\Phi_n(B),
\]
then at least one implication must have *exactly* \(A\) as its premise and include \(e\) in its consequent: no rule with a strictly smaller premise can supply \(e\) in the round started from \(A\).

For the \(n-2\)-vertex path premises, all proper subsets are closed, so their unique missing forced edge establishes the criterion. For \(n\ge6\), all proper subsets of a three-edge star are closed; for \(n=5\), the extra edges forced by proper two-edge subpaths do not include the edge from the star center to the one vertex outside the star. Thus every three-edge star demands its own premise. For a proper cycle on \(k\) vertices, if \(k\le n-3\), all proper subsets are closed. If \(k=n-2\), the only new edge obtainable from its proper subpaths is the edge joining the two outside vertices; an edge from the cycle to an outside vertex remains missing. If \(k=n-1\), the only new edges obtainable from proper subpaths link the one outside vertex to cycle vertices; a chord between nonconsecutive vertices of the cycle remains missing because \(k\ge4\). Consequently each proper cycle demands its own premise for \(n\ge5\). The critical premises are pairwise distinct. Their number is the displayed \(b_n\): there are \(\binom n2 (n-2)!/2=n!/4\) unoriented paths on \(n-2\) vertices, \(n\binom{n-1}3\) three-edge stars, and \(\binom nk(k-1)!/2\) undirected cycles of length \(k\). For \(n=4\), the six singleton premises are indispensable because the empty set is closed and each singleton has a compulsory opposite edge. Hence the one-round cardinality is sharp in every case.

**4. Enumerating the lattice.** A path component of order \(m\ge2\) has \(m!/2\) undirected labeled orientations, whereas an isolated vertex has one. By the labeled exponential formula, the forest EGF equals
\[
\exp\!\left(z+\sum_{m\ge2}\frac{z^m t^{m-1}}2\right)=\exp\!\left(z+\frac{z^2t}{2(1-zt)}\right).
\]
All forests with at most \(n-2\) edges are counted by the coefficient sum in the theorem. Exactly \(n!/4\) of them are an \(n-2\)-vertex path plus two singleton components; exactly \(n!/2\) are an \(n-1\)-vertex path plus one singleton. These disjoint families are precisely the nonclosed forests in that range. Every spanning path has \(n-1\) edges and is not closed, so it was never included. Add the \((n-1)!/2\) Hamiltonian cycles and the single inconsistent top \(E_n\). This gives the cardinality formula.

## Verification
Run `python verify.py` with Python 3. The code computes the closure independently by intersecting the actual Hamiltonian-cycle models, compares it with the block classification, and separately tests the one-round implications. It exhausts all \(2^{\binom n2}\) edge sets for \(n=4,5,6\), and checks reproducibly sampled and all critical-premise cases for \(n=7\). It also independently tests that every proposed critical premise for \(n=5,6\) has a target edge unavailable from closures of proper subpremises. The recorded output is:

```
EXHAUSTIVE n=4 subsets=64 hamilton_cycles=3 closed=8 direct_rules=6 PASS
EXHAUSTIVE n=5 subsets=1024 hamilton_cycles=12 closed=69 direct_rules=75 PASS
EXHAUSTIVE n=6 subsets=32768 hamilton_cycles=60 closed=647 direct_rules=377 PASS
SAMPLED n=7 subsets=4211 hamilton_cycles=360 direct_rules=2212 PASS
VERIFY_OK checked_inputs=38067 exact_closure=PASS closed_count=PASS one_round=PASS sharp_direct_premises=PASS
```

## Relationship to prior work
Formal-context concept lattices are intersection closures of column sets as described generally by Rawson, Myers, Green, Robinson and Joslyn (2023). The distinction between direct implication bases and globally minimum bases is developed by Adaricheva, Nation and Rand (2011), and revisited empirically by Baixeries and Napoli (2024). These prior results provide framework and terminology, not the Hamiltonian-cycle-specific forced-link classification, optimal direct-premise count, or forest enumeration above. Unlike graphic-matroid edge closure, this system is induced by intersections of *Hamiltonian cycles*. For instance, an \(n-2\)-vertex path forces an edge joining its two outside vertices even though those vertices are outside the path's graphic-matroid span.

## Limitations
The minimum in the theorem is among simultaneous one-round bases **counted by implications** with aggregated conclusions; it is not a statement about all iterative bases, minimum total number of literal occurrences, or unit-conclusion bases. The EGF and lattice count are exact, but no general Möbius-function or topological classification is claimed. Computations were finite verification, not substitutes for the all-parameter proof. Although targeted comparison did not uncover an equivalent published theorem, unnoticed equivalent work under set-intersection or Hamiltonian-tour inference terminology remains possible.

## References
- M. G. Rawson, A. Myers, R. Green, M. Robinson and C. Joslyn, *Formal Concept Lattice Representations and Algorithms for Hypergraphs*, arXiv:2307.11681, first public 2023-07-21. https://arxiv.org/abs/2307.11681
- J. Baixeries and A. Napoli, *A minimal base or a direct base? That is the question!*, arXiv:2404.12229, first public 2024-04-18. https://arxiv.org/abs/2404.12229
- K. Adaricheva, J. B. Nation and R. Rand, *Ordered direct implicational basis of a finite closure system*, arXiv:1110.5805 (2011). https://arxiv.org/abs/1110.5805
