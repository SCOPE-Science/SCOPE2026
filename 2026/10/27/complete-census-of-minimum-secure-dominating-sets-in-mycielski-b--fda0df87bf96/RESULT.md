# Complete census of minimum secure dominating sets in Mycielski bicliques

## Finding

For integers \(m,n\ge5\), let \(G_{m,n}=\mu(K_{m,n})\) be the ordinary Mycielskian of the complete bipartite graph. A secure dominating set is a dominating vertex set \(D\) such that for every \(u\notin D\) there exists \(v\in D\cap N(u)\) for which \((D\setminus\{v\})\cup\{u\}\) is still dominating. This is the standard single-guard-swap notion of secure domination.

The minimum secure dominating sets have five vertices. Their complete classification, by their numbers of vertices in the five independent classes \((A,B,A',\{w\},B')\), is
\[
(1,1,1,1,1),\quad (1,2,1,1,0),\quad (2,1,0,1,1),\quad
(2,2,0,0,1),\quad (2,2,0,1,0),\quad (2,2,1,0,0).
\]
Every selection of the indicated numbers of labelled vertices is secure dominating, and no other five-vertex selection is secure dominating. Therefore the exact number of minimum secure dominating sets is
\[
\boxed{N_{m,n}=m^2n^2+m^2\binom n2+n^2\binom m2
 +(m+n+1)\binom m2\binom n2.}
\]
In particular \(N_{5,5}=2225\), \(N_{5,6}=3435\), and \(N_{6,6}=5301\).

## Assumptions and scope

All graphs are finite, simple, and labelled. The ordinary Mycielskian of \(K_{m,n}\) consists of original bipartition classes \(A,B\), corresponding shadow classes \(A',B'\), and an apex \(w\). Its only class-to-class adjacencies are between consecutive classes in the cycle
\[
A-B-A'-\{w\}-B'-A.
\]
Every one of these five classes is independent; adjacency between consecutive classes is complete. Their sizes, in this cyclic order, are \((m,n,m,1,n)\). Distinct choices of labelled vertices are counted separately; exchanging the two sides of the original biclique is not used to identify selections.

## Proof

**Exact finite-state reduction.** Let \(a_i\) be the size of cyclic class \(i\), and let \(s_i\) be the number of its selected guards. Indices are taken modulo five. Write \(e_i\) for the coordinate vector. Every vertex omitted from class \(i\) sees exactly the selected vertices of classes \(i-1\) and \(i+1\). Consequently a profile \(s\), satisfying \(0\le s_i\le a_i\), dominates if and only if
\[
\operatorname{Dom}_a(s)\iff
\bigwedge_{i=0}^4\left(s_i=a_i\ \lor\ s_{i-1}+s_{i+1}>0\right).
\]
For each omitted vertex in class \(i\), a defending guard must belong to one of those two adjacent classes. Removing a guard from class \(j\) and placing it in \(i\) changes the profile to \(s+e_i-e_j\), and every choice of the particular guard and omitted vertex from their respective classes is equivalent. Hence security holds if and only if
\[
\operatorname{Sec}_a(s)\iff\operatorname{Dom}_a(s)\ \land\
\bigwedge_{\substack{0\le i\le4\\s_i<a_i}}
\left(\bigvee_{\substack{j\in\{i-1,i+1\}\\s_j>0}}
\operatorname{Dom}_a(s+e_i-e_j)\right).
\]
These equivalences include all guards, all omitted vertices, and all legal single-guard swaps, with no probabilistic or asymptotic step.

**Uniformity in the parameters.** At most five guards cannot saturate a nonsingleton class of size at least five unless there are exactly five guards and they occupy that class alone. Such a set cannot dominate: a class at cyclic distance two has no selected neighbour. Thus no dominating or secure profile of size at most five saturates any of the four nonsingleton classes. A successful single-guard swap of a profile of total size at most five also cannot introduce a dominating profile concentrated entirely in one such class. Therefore, for the entire calculation up to size five, every nonsingleton capacity may be replaced by six without altering the list of secure profiles or the proof of minimality. The singleton apex retains capacity one. Use the fixed capacity vector \(a=(6,6,6,1,6)\).

**Complete finite enumeration.** For each total guard count \(t\) from zero to five, enumerate each integer profile \(s=(s_0,s_1,s_2,s_3,s_4)\) with \(s_3\in\{0,1\}\), nonnegative other coordinates, and \(\sum_i s_i=t\). For each profile evaluate the two displayed Boolean formulas, testing at most two adjacent defending classes for each omitted class. The complete table is:

| Guard count | Profiles tested | Dominating profiles | Secure profiles |
| ---: | ---: | ---: | ---: |
| 0 | 1 | 0 | 0 |
| 1 | 5 | 0 | 0 |
| 2 | 14 | 0 | 0 |
| 3 | 30 | 6 | 0 |
| 4 | 55 | 19 | 0 |
| 5 | 91 | 41 | 6 |

The six passing profiles are exactly those displayed in the Finding. The exhaustive enumerator is embedded as `verify_profiles.py`. It implements only the two proved Boolean equivalences, iterates over the entire finite profile domain, and asserts both the table and the complete set of six profiles. Thus the finite enumeration is exhaustive; it is not an extrapolation from checking finitely many values of \(m\) and \(n\).

**Exact labelled count.** A fixed occupancy profile \(s\) can be realised in precisely \(\prod_i\binom{a_i}{s_i}\) ways because the classes consist of labelled twin vertices. Summing over the six profiles yields terms
\[
m^2n^2,\quad m^2\binom n2,\quad n^2\binom m2,\quad
n\binom m2\binom n2,\quad\binom m2\binom n2,\quad
m\binom m2\binom n2,
\]
which add to the claimed polynomial. Since no secure profile has cardinality at most four and at least one secure profile has cardinality five, five is the minimum secure domination number.

## Verification

The embedded `verify_profiles.py` checks all \(1+5+14+30+55+91=196\) integer profiles of size at most five, verifies every dominating and secure profile count, lists the six secure profiles, and checks the polynomial algebra on six sample parameter pairs. It prints `PROFILE_VERIFY_OK` on success.

Independently, `verify_graph.py` constructs the actual adjacency lists of each Mycielskian graph and enumerates every vertex subset of cardinality three, four, or five for \((m,n)\) equal to \((5,5)\), \((5,6)\), \((6,6)\), \((5,7)\), and \((6,7)\). Each candidate is tested by individual guard swaps on the explicit graph, without using the profile formulas. This separately verifies the predicted counts \(2225,3435,5301,4970,7665\), respectively, and the absence of smaller secure sets. It prints `DIRECT_VERIFY_OK` on success. These finite graph tests are corroboration; the infinite assertion follows from the proven profile equivalences and exhaustive fixed-state classification.

Reproduce with Python 3 by running `python3 verify_profiles.py` and `python3 verify_graph.py` in the extracted package directory. No external Python dependencies are used.

## Relationship to prior work

Bhutani, Christiana, and Ulrickson (2026, arXiv:2603.17897v1, initially available March 18, 2026) studied secure domination in Mycielskian graphs and determined secure-domination cardinalities for several families, including complete bipartite hosts. Their result gives the cardinality for the family here. The assertion newly examined here is the complete classification **and exact labelled number of all minimum sets**, not the already-known value of that cardinality.

Nayana and Iyer (first online December 16, 2022, DOI 10.3233/JIFS-223326) studied generalized Mycielskians of paths and cycles and obtained broader parameter bounds. Their accessible abstract does not state a labelled minimum-set census for \(\mu(K_{m,n})\). Results about secure domination polynomials of complete multipartite graphs do not directly imply this theorem: \(\mu(K_{m,n})\) contains an induced five-cycle, so it is not complete multipartite.

## Limitations

The classification is for ordinary one-step Mycielskians of complete bipartite hosts with both part sizes at least five. It does not enumerate all larger secure dominating sets, extend to generalized higher-level Mycielskians or arbitrary host graphs, or classify small part sizes. Exhaustive fixed-profile verification is a finite certificate for the proved reduction, while the direct graph-level experiments alone would not establish an infinite theorem. Independent proof review and complete historical-priority assessment have not occurred.

## References

1. K. R. Bhutani, A. Christiana, and P. Ulrickson, *On The Secure Domination of Mycielskian Graphs*, arXiv:2603.17897v1 (March 18, 2026). https://arxiv.org/abs/2603.17897
2. P. G. Nayana and R. R. Iyer, *On secure domination number of generalized Mycielskian of some graphs*, *Journal of Intelligent & Fuzzy Systems* 44 (2023), 4831–4841; first online December 16, 2022. https://doi.org/10.3233/JIFS-223326
3. E. J. Cockayne, P. J. P. Gobler, W. R. Grundlingh, J. Munganga, and J. H. van Vuuren, *Protection of a Graph*, *Utilitas Mathematica* 67 (2005). The secure guard-swap definition originates in this literature.
