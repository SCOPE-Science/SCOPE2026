# Affine centers and sharp four-cycle trade diameter for labelled one-factorizations of \(K_8\)

## Finding

Let \(\mathcal F\) be the set of decompositions of the edges of the labelled complete graph \(K_8\) into seven **unordered** perfect matchings. Make a simple graph \(\mathcal T\) on \(\mathcal F\) by joining two factorizations if one can be obtained from the other by exchanging the ownership of the four edges along one alternating four-cycle between two constituent matchings (a *four-cycle factor-switch* or *intercalate switch*). Vertex labels are fixed during every switch; names of the seven matchings are not retained.

**Theorem.** The graph \(\mathcal T\) contains \(6{,}240\) vertices and \(17{,}640\) edges. Exactly \(960\) vertices are isolated, namely all the perfect one-factorizations. All other \(5{,}280\) vertices form one connected component \(\mathcal G\), with
\[
\operatorname{rad}(\mathcal G)=9,\qquad \operatorname{diam}(\mathcal G)=11.
\]
The complete degree/eccentricity census is

| Degree | Number of factorizations | Eccentricity in the nontrivial component |
| ---: | ---: | ---: |
| \(0\) | \(960\) | not applicable (isolated) |
| \(3\) | \(1{,}680\) | \(11\) |
| \(7\) | \(2{,}520\) | \(10\) |
| \(9\) | \(420\) | \(10\) |
| \(13\) | \(630\) | \(10\) |
| \(21\) | \(30\) | \(9\) |

In particular, the **entire center of \(\mathcal G\)** consists precisely of the \(30\) relabelled copies of the affine translation factorization on \(\mathbb F_2^3\): for every nonzero \(a\in\mathbb F_2^3\), one factor is the matching of pairs \(\{x,x+a\}\). Every non-perfect labelled factorization can be reached from every other in at most \(11\) four-cycle switches, and every such factorization lies within \(9\) switches of any affine center.

## Assumptions and scope

The vertex set is the fixed eight-element set \(\{0,1,\ldots,7\}\). A one-factorization is a set of seven pairwise edge-disjoint perfect matchings covering all \(28\) edges. Matchings are unlabelled but the original eight vertices are labelled. A perfect one-factorization is one in which the union of any two distinct factors is a Hamiltonian eight-cycle. No edge move involving a cycle longer than four is allowed. Connectivity and eccentricity are interpreted componentwise; isolated vertices are not assigned distance to the large component.

## Proof

**1. Finite complete domain.** There are \((8-1)!!=105\) perfect matchings. Give each of the \(28\) edges its own bit. To enumerate all decompositions, select the smallest still-uncovered edge and recursively choose each perfect matching containing that edge and lying wholly in the still-uncovered edge set. Continue until all edges are used. Choosing the least uncovered edge ensures each unordered factorization appears once, and every factorization must follow a branch of the recursion. The exhaustive result is \(6{,}240\) states. An independent enumeration by normalized symmetric proper seven-edge-colorings also gives \(6{,}240\).

**2. Exhaustive transition characterization.** The union of two disjoint perfect matchings on eight vertices is either one alternating eight-cycle or two alternating four-cycles. Only the second case admits a nontrivial four-cycle factor-switch. Switching either of the complementary four-cycles produces the same unordered pair of new factors, since the two choices differ by a global interchange of the two factors. Different pairs of factors cannot yield the same neighboring factorization: the two removed factors are recoverable from the difference between the original and resulting factor sets. Thus the degree equals the number of unordered factor pairs having two four-cycles, and is at most \(\binom72=21\). Enumerating these pairs over every factorization produces \(17{,}640\) unordered edges and the six degree classes displayed above. The first checker visits all \(5{,}280\) nonisolated vertices from each of those vertices in turn, obtaining eccentricities \(9\), \(10\), or \(11\), as specified. The other \(960\) states have degree zero, exactly the perfect one-factorizations by the two possible union-cycle types.

**3. Independent symmetry-and-distance verification.** In the second enumeration, fix the seven edge colours at vertex \(0\) by requiring colour \(j-1\) on edge \(\{0,j\}\), for \(1\le j\le7\). Each unordered one-factorization has exactly one normalized proper colouring. Backtracking assigns the remaining \(21\) edge colours, each constrained to occur once at every endpoint. A four-cycle move is detected as a four-vertex component of the subgraph of two colour classes, and colour labels are canonically restored at vertex \(0\). The program constructs the same full graph and checks that **each of its six degree classes is one orbit under relabeling by \(S_8\)**. One breadth-first search from a representative of each of the five nontrivial orbits gives the same eccentricity table. Transitivity of each orbit and invariance of graph distances under relabeling make those representative searches exhaustive. This independently proves that the large component has radius \(9\) and diameter \(11\).

**4. Classification of the centers.** Regard a perfect matching as a fixed-point-free involution on eight vertices. Two factors have a union of two alternating four-cycles exactly when their involutions commute. Thus a degree-\(21\) factorization has seven pairwise commuting involutions. These generate an abelian permutation group \(H\) which is transitive: applying the seven involutions to any vertex produces its seven other possible neighbours. Every abelian transitive *faithful* permutation group is regular, because an element fixing one vertex fixes every vertex. Thus \(|H|=8\). It is generated by involutions, so \(H\cong(\mathbb Z/2\mathbb Z)^3\), and its seven nonidentity elements are exactly the factors. Hence every degree-\(21\) factorization is an affine translation factorization on \(\mathbb F_2^3\). Conversely, all nonzero translations commute, so every affine factorization has degree \(21\). Its automorphism group is the normalizer of the regular translation subgroup, namely \(\operatorname{AGL}(3,2)\), of order \(8\cdot168=1{,}344\); hence precisely \(8!/1{,}344=30\) distinct labelled affine factorizations exist. The verified degree/eccentricity census shows exactly these \(30\) vertices have minimum eccentricity \(9\).

## Verification

The standalone programs `verify_matching.py` and `verify_coloring.py` use different complete representations: exact-cover partitions of the \(28\) edges into perfect matchings, and normalized seven-edge-colouring backtracking. Run each with Python 3:

```sh
python verify_matching.py
python verify_coloring.py
```

The first checks the entire all-roots metric using \(5{,}280\) breadth-first searches and verifies the affine center orbit. The second independently reconstructs the edges, components and all six relabeling orbits and checks all five nontrivial orbit eccentricities. Both programs run to successful completion without third-party packages. An executed run of the packaged scripts produced all expected PASS assertions; results depend only on finite integer combinatorics. Scripts are part of this result rather than external dependencies.

## Relationship to prior work

Kaski, de Souza Medeiros, Östergård and Wanless (2014) systematically defined factor-switching, intercalate switching and vertex-switching of one-factorizations. Their \(K_8\) graph for four-cycle switches has **six vertices representing the six isomorphism classes**, five edges between distinct classes, one isolated perfect class, and a connected non-perfect quotient; they explain the perfect-factorization obstruction and its parity. Those established statements are not presented as new here. In particular, the well-known total of \(6{,}240\) labelled one-factorizations is used as a completeness check, not claimed as a discovery.

The present graph instead retains **all \(6{,}240\) labelled structures as separate vertices**. Connectivity of an isomorphism-class quotient is not connectivity of its labelled lift, and distances in that quotient do not determine any fixed-label switching distance. The contribution is the full labelled connectivity/metric census and the intrinsic description of its \(30\) optimal centers as affine translation factorizations. The six degree classes also give a complete transitive-symmetry stratification of the labelled graph.

## Limitations

This is an exact finite statement only for eight labelled vertices and four-cycle switches, with the seven factors unlabelled. No uniform diameter bound for larger complete graphs is asserted. Both verification programs are exhaustive programs rather than formal proofs in a proof assistant; the proof of completeness relies on the explained canonical recursion and legal-move characterization. The primary literature establishes several component and parity facts only on isomorphism-class quotients; unindexed earlier computations or independent supplementary datasets might contain some of the labelled metrics. Independent scholarly assessment has not been performed.

## References

1. P. Kaski, A. de Souza Medeiros, P. R. J. Östergård, I. M. Wanless, “Switching in One-Factorisations of Complete Graphs,” *Electronic Journal of Combinatorics* **21** (2014), P2.49, DOI: 10.37236/3606. Publisher PDF: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v21i2p49/pdf/ (especially §§2–4, 6, 8).
2. W. D. Wallis, *Introduction to Combinatorial Designs*, 2nd ed. (2007), Chapter 10 (the six isomorphism types and labelled count of one-factorizations of \(K_8\); book reference used for background only).
