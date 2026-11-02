# Local zero-forcing mobility separates the Pappus and Desargues incidence graphs

## Finding

Let \(P\) be the eighteen-vertex Pappus point–line incidence graph and let \(D\) be the twenty-vertex Desargues graph. Both graphs are cubic, bipartite, and have girth six. Ordinary zero forcing uses the rule that a blue vertex with exactly one white neighbor turns that neighbor blue. Write \(Z(G)\) for the smallest number of initially blue vertices that eventually turn the whole graph blue.

For each graph, form the **token-sliding graph** \(\mathcal S(G)\): its vertices are all zero-forcing sets of size \(Z(G)\), and two such sets are adjacent precisely when one can be obtained from the other by removing one chosen vertex and selecting an **adjacent** previously unchosen vertex of \(G\). Form the **token-jumping graph** \(\mathcal J(G)\) by dropping the adjacency restriction on the exchanged vertices.

**Theorem (exact finite classification).** The Pappus graph has \(Z(P)=7\) and exactly \(6912\) minimum zero-forcing sets. Its token-sliding graph is connected, has \(10962\) edges, radius \(16\), and diameter \(18\). Its vertex-degree distribution is \(1080\) of degree \(2\), \(3564\) of degree \(3\), and \(2268\) of degree \(4\). Its eccentricity distribution is \(648\) vertices of eccentricity \(16\), \(4968\) of eccentricity \(17\), and \(1296\) of eccentricity \(18\).

The Desargues graph has \(Z(D)=8\) and exactly \(13520\) minimum zero-forcing sets, **none of which admits a legal token slide**: \(\mathcal S(D)\) consists of \(13520\) isolated vertices. Yet \(\mathcal J(D)\) is connected and has exactly \(178560\) edges. Consequently, cubic bipartiteness and girth six do not determine whether minimum zero-forcing sets admit global mobility by adjacent replacements.

The already published value \(Z(D)=8\) is not asserted as new; the claimed comparison concerns the configuration counts, exact local reconfiguration graphs, and Pappus sliding metric.

## Assumptions and scope

Every graph is finite, simple, and undirected. The Pappus graph is presented with point vertices numbered \(0,\ldots,8\) and line vertices numbered \(9,\ldots,17\). The nine line triples, in line-vertex order, are:

```text
(0,1,2), (3,4,5), (6,7,8),
(0,4,6), (3,1,6), (0,5,7),
(3,2,7), (1,5,8), (4,2,8).
```

A point is adjacent to the line vertex containing it. An equivalent LCF presentation is the shift list `[5,7,-7,7,-7,-5]` repeated three times on an eighteen-cycle. An explicit relabeling between these representations is verified in `verify_alt.cpp`.

For the Desargues graph, use vertices \(u_i,v_i\) for \(i\in\mathbb Z/10\mathbb Z\) and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\) (the generalized Petersen graph \(GP(10,3)\)). Equivalently, it is the bipartite double cover of the Petersen graph \(KG(5,2)\): the two layers comprise the ten two-element subsets of a fixed five-element set, with cross-layer adjacency exactly for disjoint subsets. The two definitions are checked by an explicit permutation in `verify_alt.cpp`.

A blue set is *zero forcing* when there exists a finite sequence of legal forces ending with every vertex blue. The transition rules preserve both the set cardinality and the zero-forcing property at every intermediate step. Radius, diameter, and eccentricity statements apply only to the connected Pappus sliding graph. Graph vertices in the reconfiguration graphs are labeled subsets, not isomorphism classes.

## Proof

**1. An exact closure test.** For a selected set \(B\), let \(F(B)\) add every white vertex that is the unique white neighbor of some vertex of \(B\). Repeat until the increasing sequence stabilizes. Then \(B\) is zero forcing if and only if the stable set equals \(V(G)\). Indeed, each simultaneous batch of additions can be implemented as legal sequential forces: coloring other vertices blue cannot invalidate the acquisition of an originally uniquely white neighbor, although it can make another proposed force redundant. Conversely, if the process has stabilized with uncolored vertices, no legal sequential force exists, so no order of legal moves can succeed. At most \(|V(G)|\) strict enlargement rounds occur. The C++ verifier independently applies one legal force at a time, restarting the scan after each force.

**2. Exhaustive minimum search.** Encode subsets as distinct bit masks, with the bit at vertex \(v\) indicating membership. Enumerate every mask through size \(7\) for \(P\), and through size \(8\) for \(D\), applying the closure test. The complete search spaces contain respectively

\[
\sum_{j=0}^{7}\binom{18}{j}=63004,
\qquad
\sum_{j=0}^{8}\binom{20}{j}=263950
\]

masks. The supplied independent programs both find zero successful masks below the displayed minima and respectively \(6912\) and \(13520\) successful masks at those minima. Thus the minima and all their equality cases are exact. This part independently recovers the previously known Desargues optimum.

**3. Exhaustive transitions.** Index the complete families of minimum masks. For each indexed mask \(B\), each selected vertex \(a\), and each unselected vertex \(b\), form \((B\setminus\{a\})\cup\{b\}\); a sliding move is legal precisely when \(ab\) is an edge of the base graph and the resulting mask is in the indexed minimum family. Each undirected edge appears twice in the resulting directed transition table. The Python verifier generates this table by member lookup; the C++ verifier generates sliding transitions from the independently specified LCF and generalized Petersen graphs. These yield exactly \(10962\) Pappus sliding edges, with the degree distribution stated in the theorem, and zero Desargues sliding edges. The degree sum for \(P\) supplies an additional numerical check:

\[
1080\cdot2+3564\cdot3+2268\cdot4=21924=2\cdot10962.
\]

For unrestricted one-vertex exchanges in \(D\), the Python verifier tests all selected/unselected replacements; the C++ verifier independently tests unordered pairs of minimum masks for symmetric difference of size two. Both yield \(178560\) undirected jumping edges.

**4. Components and distances.** Breadth-first search on the fully generated Pappus sliding graph visits all \(6912\) states. Running breadth-first search from **each** of these states computes every graph eccentricity and produces the exact multiplicities \(648,4968,1296\) at distances \(16,17,18\). Therefore the radius is \(16\), the diameter is \(18\), and these bounds are attained. Breadth-first search on the Desargues jumping graph reaches all \(13520\) minimum masks, establishing its connectivity. Desargues sliding has no edges, so all \(13520\) components are singletons. Both verifiers reproduce these findings with different base-graph presentations and different forcing-update conventions.

Each proof step reduces to a finite, explicitly bounded search whose source code is included; neither nontermination nor a partial random sample is used as evidence. The graph-presentation isomorphism certificates are checked edge by edge, before any enumeration in the C++ verifier.

## Verification

Run the two standalone scripts, with no optional third-party Python packages:

```sh
python3 verify.py
c++ -O3 -std=c++17 verify_alt.cpp -o verify_alt
./verify_alt
```

`verify.py` constructs the point–line incidence and Petersen-double-cover descriptions, performs simultaneous closure, enumerates all minimum states, generates transitions, and computes all Pappus sliding eccentricities. `verify_alt.cpp` constructs the LCF and generalized Petersen descriptions, verifies explicit relabelings, performs sequential closure, exhausts the bounded mask sets, and independently computes all components, edges, and eccentricities.

The completed runs reported `FULL_CERTIFICATE_OK` and `INDEPENDENT_CERTIFICATE_OK`, after checking every numerical assertion in the theorem. The binaries are not required artifacts; compiling the supplied source reproduces the certificate.

## Relationship to prior work

Butler, Grout, and Hall, *Zero forcing for inertia sets*, arXiv:1211.4618 (first publicly submitted 2012-11-19), Section 5, explicitly states \(Z(D)=8\) for the Desargues graph. It studies variants of forcing and inertia constraints, not the minimum-state sliding graph, the minimum-state count, or the Pappus exchange diameter.

Geneson, Haas, and Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220 (first publicly submitted 2020-09-01), introduces and studies the **unrestricted token-jumping** graph of minimum zero-forcing sets. Its results on forests and other graph families do not determine the token-sliding Pappus or Desargues classifications; the accessible complete arXiv manuscript does not discuss these two named graphs. Token jumping and token sliding are different transition relations, and connectivity of one does not imply connectivity of the other.

Krishnan, Ma, and Zhang, *Sharp zero forcing numbers for the generalized Petersen graphs P(n,3) and P(n,4)*, arXiv:2610.24059v1 (first public 2026-10-16), Theorem 1.1, likewise reports the scalar value \(Z(D)=8\) as the \(n=10\) case. Its full accessible manuscript studies forcing-number bounds by boundary and fort methods; it does not give the minimum-state token-sliding classification. This recent source has been considered as a possible dominating result, and its scalar optimum is excluded here.

The local mobility comparison is also different from zero forcing on the Möbius–Kantor graph and from locating or perfect-matching reconfiguration on the Pappus and Desargues graphs: those are different underlying graphs or different feasibility conditions, and none of their statements implies the results established here. Relevant indexed results about Pappus and Desargues concern other graph invariants. This comparison does not constitute a guarantee that no equivalent prior work exists.

## Limitations

This is a theorem about exactly two finite labeled graphs, not an assertion for all cubic bipartite graphs of girth six. The eccentricity census uses an exhaustive finite program, not a short symbolic closed formula. No causal classification of which larger incidence graphs have mobile minimum zero-forcing sets is claimed. Although the cited accessible manuscripts and indexed mathematical records did not disclose a covering result, equivalent work in unpublished databases or other unindexed literature remains possible. The submitted computations and arguments have not received an independent scholarly audit.

## References

1. Steve Butler, Jason Grout, H. Tracy Hall, *Zero forcing for inertia sets*, arXiv:1211.4618, first submitted 2012-11-19. https://arxiv.org/abs/1211.4618
2. Jesse Geneson, Ruth Haas, Leslie Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220, first submitted 2020-09-01. https://arxiv.org/abs/2009.00220
3. Arnav Krishnan, Haobo Ma, Wenlin Zhang, *Sharp zero forcing numbers for the generalized Petersen graphs P(n,3) and P(n,4)*, arXiv:2610.24059v1, first submitted 2026-10-16. https://arxiv.org/abs/2610.24059
