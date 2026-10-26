# Three locating-code exchange regimes in the Pappus graph

## Finding

For the Pappus graph \(P\), the minimum locating-dominating (LD), identifying (ID), and open locating-dominating (OLD) codes have sizes \(6\), \(9\), and \(10\), respectively. Under one-vertex exchange (replace exactly one code vertex without increasing code size), the three families exhibit **three distinct connectivity regimes**:

| Code notion | Minimum size | Number of minimum codes | Exchange edges | Exchange components |
| --- | ---: | ---: | ---: | ---: |
| LD | \(6\) | \(18\) | \(0\) | \(18\) isolated vertices |
| ID | \(9\) | \(1028\) | \(3780\) | Two components of \(514\) vertices |
| OLD | \(10\) | \(2025\) | \(13770\) | One component |

The ID components are exactly the codes having, respectively, at most four and at least five vertices in a chosen nine-vertex bipartition class. They each contain \(1890\) exchange edges.

More strongly, the OLD exchange graph is \(F\square F\), where \(F\) is a connected \(45\)-vertex, \(153\)-edge graph. Its \(27\) vertices of degree \(6\) have eccentricity \(3\); its \(18\) vertices of degree \(8\) have eccentricity \(4\). Hence the OLD exchange graph has radius \(6\), diameter \(8\), and both degree enumerator and eccentricity enumerator determined as follows:
\[
\sum_{C} t^{\deg(C)}=729t^{12}+972t^{14}+324t^{16},
\qquad
\sum_{C} t^{\operatorname{ecc}(C)}=729t^{6}+972t^{7}+324t^{8}.
\]

In particular, there are at most eight single-vertex exchanges between any two minimum OLD codes, whereas no exchanges are available between distinct minimum LD codes and no ID exchange crosses the two majority classes.

## Assumptions and scope

All graphs are finite, undirected, simple, and labeled as defined here. The nine points are \(p_0,\ldots,p_8\) and the nine lines are \(\ell_0,\ldots,\ell_8\). A point \(p_i\) is incident with \(\ell_j\) exactly when \(i\) appears in the following line triples in order:

```
L0=(0,8,2)   L1=(0,1,6)   L2=(1,2,7)
L3=(2,3,5)   L4=(3,4,0)   L5=(4,5,1)
L6=(5,6,8)   L7=(6,7,3)   L8=(7,8,4)
```

Each vertex has degree three. This is the eighteen-vertex Pappus graph, equivalent to the LCF model consisting of the cycle \(0,1,\ldots,17,0\) and chords prescribed by the repeated shifts \((5,7,-7,7,-7,-5)\), with \(p_i\) corresponding to \(2i+1\) and \(\ell_j\) to \(2j\).

Write \(N(v)\) for the open neighborhood, \(N[v]=N(v)\cup\{v\}\), and \(C\) for a code. An LD code satisfies domination and has distinct nonempty \(N(v)\cap C\) over all \(v\notin C\). An ID code has distinct nonempty \(N[v]\cap C\) over all vertices. An OLD code has distinct nonempty \(N(v)\cap C\) over **all** vertices. A minimum code has smallest cardinality for its own notion, and the exchange graph on that notion's minimum codes joins \(C\) and \(C'\) exactly when \(|C\triangle C'|=2\). The result concerns only these three definitions, the specified graph, and minimum-cardinality exchanges.

## Proof

**The graph model and finite certification.** The exact incidence list above determines all \(27\) graph edges. An independent representation uses the stated LCF cycle and chords; mapping point and line labels to odd and even cycle labels gives the same \(27\) unordered edges, checked explicitly in `verify_incidence.py`. The two verifiers implement different signature tests (bit-masked closed/open neighborhoods versus finite sets) and different descriptions of the graph. Both enumerate every candidate cardinality up to and including the optimum, rather than extrapolating from a sample. Their complete executable sources and actual results are included.

**LD lower bound.** Suppose \(|C|=k\le5\) and all \(18-k\) outside vertices have different nonempty open signatures. At most \(k\) such signatures can be singletons. Thus the sum of their cardinalities is at least \(k+2(18-2k)=36-3k\) (when \(k\le5\), there are more than \(k\) outside vertices). Yet the sum is at most \(3k\), because each of the \(k\) selected vertices has degree three. For \(k\le5\), \(36-3k>3k\), a contradiction. At \(k=6\), the chosen set
\[
\{\ell_0,\ell_1,\ell_2,p_3,p_4,p_5\}
\]
indeed has twelve distinct nonempty outside signatures, proving the minimum. Enumerating the \(\binom{18}{6}=18564\) six-sets by the stated predicate yields exactly \(18\) valid sets. Every one is independent, as the equality condition also forces: all \(18\) incidences from selected vertices must go outside \(C\). Testing each possible replacement among the \(18\) sets yields no exchange edge, so the LD exchange graph has \(18\) isolated vertices.

**ID exact minimum and two components.** Apply the closed-signature predicate to all subsets of cardinalities less than nine, as specified in the verification scripts; no valid ID code occurs. The entire nine-point bipartition class is a valid ID code: selected points are uniquely recognized by their own selected vertex, and the nine unselected line-vertices by their distinct three-point neighborhoods. Thus the minimum is nine. Complete enumeration of the \(\binom{18}{9}=48620\) candidates yields \(1028\) valid codes. The numbers with \(a\) selected point-vertices, for \(a=0,1,\ldots,9\), are respectively
\[
1,\ 27,\ 81,\ 243,\ 162,\ 162,\ 243,\ 81,\ 27,\ 1.
\]
Build the exchange graph by generating every one-vertex deletion and insertion, retaining only verified codes. Its edge count is \(3780\). No edge joins the \(514\) codes having \(a\le4\) to the \(514\) having \(a\ge5\). A complete graph search from one representative of each class visits every code of that class, proving each class connected. The two components therefore have \(514\) vertices and, by symmetry, \(1890\) edges each. This is not a parity-of-a-numerical-counter inference: absence of crossing edges and both component searches are exact tests in the displayed graph.

**OLD lower bound and two-factor theorem.** Since the graph is bipartite, the open signatures of point-vertices lie in the selected lines and those of line-vertices lie in the selected points. Once all signatures are nonempty, there can be no cross-part collisions. Thus a choice \(C_P\) of selected points and a choice \(C_L\) of selected lines together form an OLD code precisely when each independently gives nine distinct nonempty signatures on the opposite side. If only \(t\le4\) points were selected, the nine line signatures would have at most \(t\) singleton values, forcing an incidence-weight sum at least \(t+2(9-t)=18-t>3t\), contradicting cubic degree. The same bound holds for selected lines. Hence every OLD code needs at least five vertices from each side. The two lists of \(\binom95=126\) five-element subsets contain exactly \(45\) valid choices each, so the minimum equals ten and the number of minimum codes is \(45^2=2025\).

There is also a small exact geometric classification of those \(45\) point choices. Among all \(126\) five-point subsets, let \(m_r\) count the number of the nine incidence lines meeting the subset in exactly \(r\) points. The distribution of the four occupancy patterns \((m_0,m_1,m_2,m_3)\) is
\[
(1,2,5,1):54,\quad (0,4,4,1):27,\quad
(0,5,2,2):27,\quad (0,3,6,0):18.
\]
Precisely the last two patterns give nine nonempty, distinct line signatures. In each case the code is valid; this is checked by all \(126\) explicit subsets, not inferred from occupancy sums alone. Under the duality \(p_i\mapsto\ell_{\alpha(i)}\), where
\[
(\alpha(0),\ldots,\alpha(8))=(0,3,4,8,6,5,2,7,1),
\]
the same \(45\)-set family and exchange graph occurs on the line side (the corresponding map on lines is also verified in the second program).

Let \(F\) be the exchange graph of valid five-point selections. It has \(45\) vertices and \(153\) edges. Under single-vertex exchanges of ten-element OLD codes, each step changes exactly one of the two sides; it cannot change both while preserving five selections in each side. The OLD exchange graph therefore is exactly \(F\square F\). The finite factor graph is connected. Its \(27\) subsets with two fully selected lines have exchange degree \(6\) and eccentricity \(3\); its \(18\) subsets with no fully selected line have exchange degree \(8\) and eccentricity \(4\), as reproduced by shortest-path searches from all forty-five vertices. In a Cartesian product, distances are sums of factor distances. The displayed OLD counts and its radius \(6\) and diameter \(8\) follow, with \(2\cdot45\cdot153=13770\) edges.

**Finite completeness of computational steps.** In `verify_lcf.py`, the outer loops range over every subset of each cardinality and all possible deleted/inserted vertices; breadth-first searches visit all exchange neighbors. In `verify_incidence.py`, independently constructed incidence signatures enumerate the same candidates and exchange components, while its \(126\) five-point checks determine the factor and its shortest paths. Since the vertex sets and all loops are finite and explicit, these are exhaustive proofs for this fixed graph. No infinite extrapolation or external oracle is used.

## Verification

Run, from the directory containing the embedded files:

```
python3 verify_lcf.py
python3 verify_incidence.py
```

The recorded output files `verify_lcf.out` and `verify_incidence.out` give the executed results. The scripts use only Python's standard library, test the graph degree/edge model, all minimum-cardinality predicates, the exchange edges/components, and the factor-graph eccentricities. The incidence checker additionally checks the explicit point-line duality and enumerates all occupancy types. Both programs completed with their respective `ALL_LCF_CHECKS_PASS` and `ALL_INCIDENCE_CHECKS_PASS` markers. The exact byte-level artifacts are included with this result; no previously generated program is a dependency.

## Relationship to prior work

Seo and Slater (2010) introduced OLD codes and proved, for a regular graph of degree \(r\), the general bound \(\operatorname{OLD}(G)\ge 2|V(G)|/(r+1)\). For this cubic graph it gives only nine, rather than the sharp ten, and says nothing about the \(45\)-vertex factor or exchange geometry. Their bipartite-grid examples use independent choices on the two sides, an elementary aspect retained but not claimed as new here. Balbuena, Foucaud and Hansberg (arXiv:1407.7263, first released 2014-07-27) give general bounds for LD and ID codes in graphs of girth at least five; their cubic estimates do not imply the Pappus code counts or components. Foucaud and Henning (arXiv:1412.2865, first released 2014-12-09) prove a cubic location-domination bound, not the exact Pappus family. Kovács, Kutnar, Marušič and Wilson (2012) establish the Pappus graph's role among cubic symmetric tricirculants but do not classify these codes.

Published Pappus graph independence-complex and matching-complex calculations concern topological invariants of independent sets and matchings, not the three separating-code families or their minimum-code exchange graphs. Published exact results about locating domination in threshold or chain graphs also do not subsume this result: the Pappus graph belongs to neither of those classes. No directly covering published statement was found in the recorded searches, but lack of a search result is not proof of priority.

## Limitations

The theorem is exactly about the finite eighteen-vertex Pappus graph and the specified three code notions; it makes no claim for all cubic symmetric graphs, all configurations, nonminimum codes, or other reconfiguration operations. The identifying-code connectivity and minimum size rely on exhaustive finite computation with complete disclosed programs. Generalizing these computations without proof would be invalid. A 2015 study by Arti Pandey on OLD codes in bipartite graphs was located, but its full primary text was unavailable after open-access and institutional-access attempts; its accessible abstract emphasizes complexity and chain graphs. Unindexed combinatorial tables or alternative terminology could still contain overlapping values, so publication priority and independent validation remain open. The included review is a self-review only; no independent external audit was performed.

## References

1. S. J. Seo and P. J. Slater, *Open neighborhood locating-dominating sets*, Australasian Journal of Combinatorics **46** (2010), 109–119. https://ajc.maths.uq.edu.au/pdf/46/ajc_v46_p109.pdf
2. C. Balbuena, F. Foucaud and A. Hansberg, *Locating-dominating sets and identifying codes in graphs of girth at least 5*, arXiv:1407.7263 (first posted 2014-07-27). https://arxiv.org/abs/1407.7263
3. F. Foucaud and M. A. Henning, *Location-domination and matching in cubic graphs*, arXiv:1412.2865 (first posted 2014-12-09). https://arxiv.org/abs/1412.2865
4. I. Kovács, K. Kutnar, D. Marušič and S. Wilson, *Classification of cubic symmetric tricirculants*, Electronic Journal of Combinatorics **19** (2012), #P24 (published 2012-05-31). https://doi.org/10.37236/2371
5. A. Pandey, *Open Neighborhood Locating-Dominating Set in Graphs: Complexity and Algorithms*, ICIT 2015, DOI:10.1109/ICIT.2015.14 (full text not inspected).
