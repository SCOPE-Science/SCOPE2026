# A single extra sensor connects identifying codes of the Pappus graph

## Finding

Let \(P\) denote the eighteen-vertex Pappus graph, viewed as the point-line incidence graph of the biaffine plane of order three described below. A closed-neighborhood identifying code \(C\subseteq V(P)\) meets every closed neighborhood and distinguishes every pair of closed neighborhoods through their intersections with \(C\). The identifying-code number is

\[\gamma_{\mathrm{ID}}(P)=9.\]

There are precisely \(1028\) identifying codes with nine vertices. For an integer \(k\) between nine and eighteen inclusive, define \(R_k(P)\) to have the identifying codes of size \(k\) as vertices, with an edge if one code is changed to another by deleting one sensor and installing one sensor at a different vertex (a token jump, with no physical-adjacency restriction).

The minimum-code graph \(R_9(P)\) has \(1028\) vertices, \(3780\) edges, and exactly **two** connected components, each containing \(514\) codes. One component consists exactly of codes with zero through four selected point-vertices of the incidence graph; the other has five through nine selected point-vertices. The all-line code and the all-point code are the respective centers; each component has radius four and diameter eight. The full within-component eccentricity distribution is \(4:2,\ 5:54,\ 6:162,\ 7:486,\ 8:324\).

In sharp contrast, \(R_k(P)\) is connected **for every** \(10\le k\le18\). Thus one additional sensor beyond the minimum is necessary and sufficient for connectedness of the fixed-cardinality token-jumping graph. This does not assert connectivity under the stricter edge-adjacent token-sliding rule.

The complete enumerated sizes and numbers of exchange edges are as follows:

| \(k\) | identifying codes | exchange edges | component sizes |
| ---: | ---: | ---: | --- |
| 9 | 1028 | 3780 | 514, 514 |
| 10 | 8640 | 128700 | 8640 |
| 11 | 16524 | 413586 | 16524 |
| 12 | 14505 | 437184 | 14505 |
| 13 | 7938 | 242145 | 7938 |
| 14 | 3015 | 83160 | 3015 |
| 15 | 816 | 18360 | 816 |
| 16 | 153 | 2448 | 153 |
| 17 | 18 | 153 | 18 |
| 18 | 1 | 0 | 1 |

## Assumptions and scope

All graphs are finite, undirected and simple. Set \(\mathbb F_3=\{0,1,2\}\) with arithmetic modulo three. Take nine point vertices \(p_{x,y}\), one for each \((x,y)\in\mathbb F_3^2\), and nine line vertices \(\ell_{m,b}\), one for each \((m,b)\in\mathbb F_3^2\), joining \(p_{x,y}\) to \(\ell_{m,b}\) precisely when \(y=mx+b\) in \(\mathbb F_3\). This is the ordinary 18-vertex Pappus graph, also the LCF graph given by the repeated step sequence \((5,7,-7,7,-7,-5)\) three times; the package verifies the vertex isomorphism explicitly.

For each vertex \(v\), denote by \(N[v]\) its closed neighborhood. A set \(C\) is an identifying code if \(C\cap N[v]\ne\varnothing\) for every vertex and \(C\cap N[u]\ne C\cap N[v]\) whenever \(u\ne v\). The threshold concerns exactly this closed-neighborhood notion, not open-neighborhood identification or locating-domination. In a fixed-cardinality exchange, any selected vertex may be replaced by any unselected vertex, including a nonneighbor.

## Proof

The theorem follows from the exhaustive, independently cross-checked finite certificate supplied as `verify_incidence.cpp`, `verify_lcf.py` and the two captured outputs. Below is a precise explanation of why this finite computation is exhaustive and proves every stated assertion.

**(1) Exact identifying predicate.** For the eighteen vertices form the eighteen closed-neighborhood bitsets \(B_v=N[v]\). The identifying-code condition is equivalent to meeting the following \(171\) nonempty bitsets:

\[\mathcal H=\{B_v:v\in V(P)\}\cup\{B_u\mathbin\triangle B_v:u<v\}.\]

Indeed, \(C\cap B_v\ne\varnothing\) is the domination condition; equality of the signatures \(C\cap B_u\) and \(C\cap B_v\) is equivalent to \(C\cap(B_u\triangle B_v)=\varnothing\). Thus a candidate code is valid if and only if its bit mask hits every member of \(\mathcal H\). The second implementation tests this condition; the first independently constructs and compares all eighteen nonempty signatures.

**(2) Exhaustiveness of the vertex search.** Index the nine points by \(3x+y\) and the nine lines by \(9+3m+b\). Every vertex subset is uniquely encoded by an integer mask in \(\{0,\dots,2^{18}-1\}\). Both programs iterate over **every one of the \(262144\) masks**, with no sampling or pruning. They find no identifying codes of cardinality less than nine, exactly \(1028\) of cardinality nine and \(8640\) of cardinality ten. The remaining entries in the table arise from the same exhaustive search. Because the graph itself is fully specified, this proves optimality and the complete state counts.

**(3) Exact exchange graph.** For each valid mask \(s\) of weight \(k\), enumerate all \(k(18-k)\) possible pairs consisting of a selected bit \(a\) and an unselected bit \(b\), and test whether \(s\mathbin\triangle\{a,b\}\) is among the already enumerated valid weight-\(k\) masks. Every legal move is of exactly this form, and each such form changes precisely one sensor, so there can be no omitted or extraneous edge. Standard exhaustive breadth-first search on every exchange graph returns the component sizes in the table. It returns two components of sizes \(514\) and \(514\) at size nine, one component at each larger size, and the listed exact edge counts.

**(4) Component geometry.** The second program uses an LCF construction of the Pappus graph and an explicit tested eighteen-vertex isomorphism to the point-line model. Independent enumeration and breadth-first search show that the two size-nine components are precisely the two stated point-count ranges. A complete shortest-path search from **every** size-nine code, restricted to its connected component, gives the eccentricity histogram stated above. It implies radius four and diameter eight *within either component*; disconnected cross-component pairs have no finite exchange distance. It also verifies the degree-frequency polynomial \(108t^2+216t^4+216t^5+108t^7+270t^{11}+108t^{15}+2t^{27}\).

The exhaustive searches, the isomorphism certificate and the trivial bitset-hitting equivalence jointly establish the exact finite theorem; no empirical extrapolation or unverified infinite step is used.

## Verification

Compile and execute `verify_incidence.cpp` with `c++ -std=c++17 -O2 -Wall -Wextra verify_incidence.cpp -o verify_incidence && ./verify_incidence`; independently run `python3 verify_lcf.py` with a Python interpreter supporting `int.bit_count()`. Both use standard libraries only and construct the graph internally. Their recorded outputs are `incidence_output.txt` and `lcf_output.txt`, respectively. The C++ program verifies all ten exchange graphs; the independent LCF Python program verifies all code counts, the size-nine and size-ten exchange graphs, the explicit graph isomorphism and the size-nine shortest-path profile. Checks were replayed against the delivered standalone sources.

## Relationship to prior work

Kovács, Kutnar, Marušič and Wilson classified cubic symmetric tricirculants, explicitly including the Pappus graph. Their 2012 paper gives the classical graph context but not identifying-code reconfiguration. Balbuena, Foucaud and Hansberg investigate identifying codes for graphs of girth at least five, including general bounds for cubic graphs; their primary article contains no Pappus-specific minimum-code exchange computation. Earlier and later general identifying-code theory and Teshima's identifying-code reconfiguration dissertation use different scopes; the latter's reconfiguration notion restricts a replacement to adjacent vertices, and its realizability theorem constructs other host graphs. These works do not logically imply the exact fixed-graph token-jumping threshold here.

The concept of identifying codes, the Pappus graph, and general exchange-graph constructions are all preexisting. The retained claim is the **exact Pappus code census and sharp one-extra-sensor token-jumping transition**, not these definitions or general background bounds. Targeted exact-object and alias searches did not locate an equivalent table, but search incompleteness does not establish publication priority.

## Limitations

The proof is a complete finite computation for the specified eighteen-vertex graph, not a formula for general biaffine incidence graphs or other cubic symmetric graphs. The \(k\ge10\) connectivity statement is limited to \(k\le18\), and disconnected size-nine pairs have no finite exchange distance. The result does not cover token sliding or nonfixed-cardinality moves. Results in unindexed books, code tables or computer-search archives could duplicate the finding; an independent scientific audit and priority determination have not been performed. Recorded outputs alone are not treated as proof: all source code, the exhaustive search range and the mathematical equivalence are part of the certificate.

## References

1. I. Kovács, K. Kutnar, D. Marušič, and S. Wilson, *Classification of Cubic Symmetric Tricirculants*, Electronic Journal of Combinatorics **19** (2012), #P24, published 2012-05-31. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v19i2p24/pdf/
2. C. Balbuena, F. Foucaud, and A. Hansberg, *Locating-Dominating Sets and Identifying Codes in Graphs of Girth at least 5*, Electronic Journal of Combinatorics **22** (2015), #P2.15; earlier arXiv:1407.7263 (2014-07-27). https://arxiv.org/abs/1407.7263 ; https://perso.limos.fr/ffoucaud/Publications/Papers/J13_ID-LD-girth5_ElJC_2015.pdf
3. L. E. Teshima, *The i-Graph and Other Variations on the gamma-Graph*, University of Victoria dissertation (2022; publicly catalogued 2023-01-03), Chapter 2, identifying-code reconfiguration section. https://dspace.library.uvic.ca/items/740e5c10-d1aa-4992-970b-3711b397f7f5
