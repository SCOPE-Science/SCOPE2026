# Minimum maximal matchings of the Nauru graph and a sharp four-edge reconfiguration threshold

## Finding

Let \(N=\operatorname{GP}(12,5)\) be the Nauru graph. Let \(\mathcal M\) denote its smallest inclusion-maximal edge matchings. For an integer \(t\geq1\), define the graph \(\mathcal R_t\) on \(\mathcal M\) by joining distinct matchings \(M,M'\) exactly when \(|M\setminus M'|=|M'\setminus M|\leq t\). Thus one step replaces at most \(t\) matching edges simultaneously, with both endpoint states required to be minimum maximal matchings; intermediate partial matchings are not required to be maximal.

The smallest maximal matching has eight edges, and there are precisely 90 such matchings. The exact reconfiguration classification is:

| Maximum replaced edges \(t\) | Edges of \(\mathcal R_t\) | Connected component orders | Additional structure |
| --- | ---: | --- | --- |
| \(1\) | 0 | 90 singletons | Every optimum is frozen. |
| \(2\) | 180 | \(30,30,30\) | Three isomorphic four-regular components, each of radius and diameter five. |
| \(3\) | 180 | \(30,30,30\) | Exactly the same graph as for \(t=2\). |
| \(4\) | 522 | \(90\) | Connected, radius three, diameter four; 18 vertices of eccentricity three and 72 of eccentricity four. |

The 30-vertex components of \(\mathcal R_2\) each have 60 edges. The natural cyclic rotation of the two twelve-vertex layers permutes these components cyclically; reflection interchanges two of them, so the three components are genuinely isomorphic, not just equal in size. The degrees in \(\mathcal R_4\) are fourteen at 18 configurations and eleven at 72 configurations.

In particular, the sharp bound for reconfiguring **every** minimum maximal matching while preserving optimality after each operation is **four simultaneous matching-edge substitutions**. Three are insufficient, while four suffice.

## Assumptions and scope

Work with a finite, simple, undirected graph. Its vertex set is \(\{u_i,v_i: i\in\mathbb Z/12\mathbb Z\}\) and its edge set is
\[
\{u_i u_{i+1},\;u_i v_i,\;v_i v_{i+5}:i\in\mathbb Z/12\mathbb Z\}.
\]
Indices are modulo twelve, and each undirected edge occurs once. A matching is a family of pairwise vertex-disjoint edges. It is inclusion-maximal exactly when the vertices left unmatched form an independent set. *Minimum maximal* concerns minimum cardinality among inclusion-maximal matchings, not maximum-cardinality matchings or perfect matchings.

For the finite certificates, label \(u_i=i\), \(v_i=12+i\), sort each edge as an increasing vertex pair, and sort the 36 distinct edge pairs lexicographically. A matching is encoded as eight increasing edge indices from zero to 35. Certificates refer exclusively to this ordering. The result does not concern token addition/removal moves that temporarily permit fewer matching edges, or paths through non-maximal states.

## Proof

**Minimum cardinality.** The Nauru graph is cubic with 36 edges. Any matching edge meets at most four other edges; counting itself, it can dominate at most five graph edges. A maximal matching dominates every graph edge, so every maximal matching \(M\) satisfies \(5|M|\geq36\) and consequently \(|M|\geq8\). The explicit 90-element certificate includes eight-edge maximal matchings, establishing equality. The existence of an eight-edge maximal matching was already known (Brazil, da Fonseca, de Figueiredo and Sasaki, 2012); no new claim is made for the scalar minimum alone.

**Exhaustive eight-edge classification.** For any eight-edge matching, exactly eight of the 24 vertices remain unmatched, and this set must be independent for maximality. Conversely, any independent eight-set whose 16-vertex complement admits a perfect matching produces an eight-edge maximal matching, and every such matching arises this way.

The standalone `verify_by_unmatched.py` loops over all \(\binom{24}{8}\) potential omitted sets, filters by the explicitly constructed adjacency masks, and recursively enumerates *every* perfect matching of the induced complement by fixing the least remaining vertex and trying each currently available neighbor. Exactly 2,964 omitted eight-sets are independent. Of these, 2,874 admit no perfect matching on their complement and 90 admit exactly one. This produces exactly 90 distinct eight-edge maximal matchings.

Independently, the C++17 `verify_by_matching.cpp` visits the 24 vertices in a canonical decision tree. The least undecided vertex is either declared unmatched (only if it has no previously unmatched neighbor), or matched to one of its currently available neighbors. All choices are exhaustive, mutually exclusive and terminate with each vertex decided. Filtering leaves to eight selected edges yields exactly 90 distinct maximal matchings. Its sorted list `matchings_cpp.txt` equals the independently enumerated 90-element Python list *entry by entry*. Coupled with the proven lower bound, either complete enumeration certifies the minimum-optimum classification.

**Exchange graphs.** For equal-size matchings \(M\) and \(M'\), the number of replaced matching edges is exactly \(8-|M\cap M'|\). Accordingly, the certificate forms each possible unordered pair from the 90 distinct matchings (4,005 pairs), computes this integer, and includes the pair in \(\mathcal R_t\) exactly when the integer does not exceed \(t\). The complete transition lists are included for \(t=1,2,3,4\). There are respectively 0, 180, 180 and 522 edges. Breadth-first traversal finds 90, three, three and one connected components, with sizes as in the table. All-source breadth-first distances certify that every \(\mathcal R_2\) vertex has eccentricity five within its component, and that the 90 \(\mathcal R_4\) vertices have eccentricity counts \(18\) at three and \(72\) at four. The stated radius and diameter follow.

**Isomorphism of the three components.** Rotation \(u_i\mapsto u_{i+1}\), \(v_i\mapsto v_{i+1}\), and reflection \(u_i\mapsto u_{-i}\), \(v_i\mapsto v_{-i}\) preserve the graph's edge set and therefore preserve maximality and pairwise edge-replacement counts. On the three components of \(\mathcal R_2\), ordered by their smallest canonical state index, rotation induces the permutation \((0,1,2)\mapsto(1,2,0)\) and reflection induces \((0,1,2)\mapsto(0,2,1)\). The certificate checker verifies these actions on all 90 states and all transitions. Hence the three components are mutually isomorphic.

The strict equality \(\mathcal R_2=\mathcal R_3\), together with connectivity of \(\mathcal R_4\), proves the sharp threshold.

## Verification

Three standalone source files, `verify_by_unmatched.py`, `verify_by_matching.cpp` and `check_certificate.py`, plus `certificate.json`, `matchings_cpp.txt` and recorded outputs, are provided. They use no external data. Only the C++17 standard library and Python 3 standard library are needed. From a directory containing all files, execute:

```sh
python3 verify_by_unmatched.py
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_by_matching.cpp -o verify_by_matching
./verify_by_matching
python3 check_certificate.py
```

The final checker reconstructs the graph, verifies every matching and its maximality, compares the two independent enumerations, independently regenerates every exchange list, traverses all connected components and shortest paths, and verifies the two graph automorphisms and their induced actions. All commands completed successfully on the packaged source files. The certificate SHA-256 is `4fdad93ab72e812b23de4ffe5e1b1bf818cd8b849b96c19d79f88112306c5a6b`.

## Relationship to prior work

The foundational edge-domination literature establishes the equivalence of minimum edge domination and minimum-cardinality maximal matching as optimization *values*, but does not thereby determine the family of optimal maximal matchings. Brazil, da Fonseca, de Figueiredo and Sasaki exhibit an eight-edge maximal matching in the Nauru graph (arXiv:1204.2727, first submitted 2012-04-11); their objective is a weighted perfect-matching ratio, not the enumerated optimal-state space or its exchange graph. Thus the scalar eight is explicitly prior work.

Solomon and Solomon (2021) study gradual transformation of general matchings using bounded changes with an allowed cardinality deficit of one. Their guarantee does not require every intermediate state to remain a *minimum maximal matching* and does not imply the threshold here. Joffard's discussion of edge-dominating-set token sliding likewise permits edge sets that are not matchings; it does not furnish the stated finite-state classification. The exact count of 90, its three-component two-exchange geometry, and the sharp no-slack four-exchange threshold are the claims assessed here. Public mathematical searches did not locate an equivalent classification; see the detailed comparison and residual risks in `AUDIT.json`.

## Limitations

This is a theorem about the single 24-vertex Nauru graph, not a general statement about generalized Petersen graphs, arbitrary cubic graphs, or maximum matchings. The cardinality bound is elementary and previously attained; its value alone is not new. Component counts, eccentricity values and the bound four depend on complete finite enumeration, and their proof is only as strong as the independently replayable algorithms and certificate supplied. The result does not assert connectivity under edge swaps with nonoptimal intermediate states, nor any complexity or mixing-time consequence. Unknown equivalent calculations in unindexed papers, databases or supplementary materials remain a publication-priority risk. No independent external audit has been performed.

## References

1. M. Yannakakis and F. Gavril, *Edge Dominating Sets in Graphs*, SIAM Journal on Applied Mathematics 38 (1980). DOI: 10.1137/0138030.
2. E. Vital Brazil, G. D. da Fonseca, C. M. H. de Figueiredo and D. Sasaki, *The Cost of Perfection for Matchings in Graphs*, arXiv:1204.2727 (first version released 2012-04-11); revised paper DOI: 10.1016/j.dam.2014.12.006. https://arxiv.org/abs/1204.2727
3. N. Solomon and S. Solomon, *A Generalized Matching Reconfiguration Problem*, ITCS 2021, LIPIcs 185, article 57, DOI: 10.4230/LIPIcs.ITCS.2021.57. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2021.57
4. A. Joffard, doctoral thesis, chapter 6, *Reconfiguration of Dominating Sets under the Token Sliding Rule* (2020), sections dealing with edge-dominating sets. https://perso.liris.cnrs.fr/ajoffard/manuscript.pdf
