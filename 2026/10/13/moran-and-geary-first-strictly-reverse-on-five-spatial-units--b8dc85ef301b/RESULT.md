# Moran and Geary first strictly reverse on five spatial units
## Finding
Let \(G\) be a connected simple undirected graph on \(n\) spatial units. Use its unstandardized symmetric adjacency matrix \(W\) as the spatial-weight matrix: \(w_{ij}=1\) when units \(i\) and \(j\) are neighbors and \(w_{ij}=0\) otherwise. Let
\[
S_0=\sum_{i,j}w_{ij}.
\]
For a nonconstant field \(x\), write \(z=x-\bar x\mathbf 1\). Moran's statistic is
\[
I=\frac{n}{S_0}\frac{z^{\mathsf T}Wz}{z^{\mathsf T}z},
\]
and Geary's statistic is
\[
C=\frac{n-1}{2S_0}
\frac{\sum_{i,j}w_{ij}(x_i-x_j)^2}{z^{\mathsf T}z}.
\]
Larger \(I\) and smaller \(C\) both indicate stronger positive spatial autocorrelation.

Restrict first to binary fields \(x_i\in\{0,1\}\). No two binary fields on any connected graph with at most \(4\) vertices receive opposite strict rankings from Moran \(I\) and Geary \(C\).

Five vertices are sharp. On the path
\[
P_5:1-2-3-4-5,
\]
compare the endpoint-singleton field
\[
A=(0,0,0,0,1)
\]
with the adjacent internal-pair field
\[
B=(0,0,1,1,0).
\]
Their exact values are
\[
(I(A),C(A))=\left(-\frac1{16},\frac58\right)
\]
and
\[
(I(B),C(B))=\left(\frac1{24},\frac56\right).
\]
Thus
\[
I(B)>I(A)
\]
but
\[
C(B)>C(A).
\]
Moran therefore ranks \(B\) as more positively autocorrelated, while Geary ranks \(A\) as more positively autocorrelated.

The boundary is not peculiar to one graph. Among the \(21\) connected unlabeled graphs on five vertices, exactly \(11\) admit at least one binary-field reversal.

There is also a clean structural obstruction. On every regular graph, for every nonconstant real field,
\[
C=\frac{n-1}{n}(1-I).
\]
Hence Moran and Geary have exactly opposite numerical direction but the same spatial-autocorrelation ordering, including all ties, on every regular spatial-neighbor graph.

Finally, the path witness persists. For every \(n\ge5\), on \(P_n\), let \(A_n\) be a singleton at an endpoint and let \(B_n\) consist of two adjacent internal vertices. Then
\[
I(A_n)=-\frac1{(n-1)^2},
\qquad
C(A_n)=\frac{n}{2(n-1)},
\]
while
\[
I(B_n)=\frac{n^2-4n-4}{2(n-1)(n-2)},
\qquad
C(B_n)=\frac{n}{2(n-2)}.
\]
For every \(n\ge5\),
\[
I(B_n)>I(A_n)
\]
and
\[
C(B_n)>C(A_n),
\]
so the strict ranking conflict persists indefinitely.

## Assumptions and scope
The spatial weights are the unstandardized symmetric adjacency weights of a connected simple undirected graph. Row-standardized or asymmetric spatial weights are not covered by the finite boundary statement.

The sharp order-five result concerns binary nonconstant fields. The regular-graph affine identity is stronger and holds for every nonconstant real-valued field.

A strict reversal means that one field has larger Moran \(I\) but also larger Geary \(C\), because larger \(I\) and smaller \(C\) represent the same positive-autocorrelation direction.

The graph is fixed within each pairwise comparison. The theorem does not compare statistic values across different weight matrices as though their numerical scales were universally commensurate.

## Proof
For symmetric \(W\), let \(d_i=\sum_jw_{ij}\). The weighted squared-difference identity is
\[
\sum_{i,j}w_{ij}(z_i-z_j)^2
=
2\sum_i d_i z_i^2-2z^{\mathsf T}Wz.
\]
Substituting this into Geary's definition yields
\[
C
=
\frac{n-1}{S_0}
\frac{\sum_i d_i z_i^2}{\sum_i z_i^2}
-
\frac{n-1}{n}I.
\]
This formula identifies degree heterogeneity as the only extra term separating the two rankings.

If \(G\) is \(r\)-regular, then \(S_0=nr\) and
\[
\frac{\sum_i d_i z_i^2}{\sum_i z_i^2}=r.
\]
Therefore
\[
C=\frac{n-1}{n}-\frac{n-1}{n}I
=
\frac{n-1}{n}(1-I).
\]
This proves exact ordering equivalence on regular graphs.

For a binary field, let \(k\) be the number of ones, let \(q\) be the number of graph edges crossing from a one to a zero, let \(s\) be the sum of the graph degrees over the one-vertices, and let \(m\) be the number of edges. Direct simplification gives
\[
C=\frac{n(n-1)q}{2mk(n-k)}
\]
and
\[
I=
\frac{2k^2m+n(n-2k)s-n^2q}{2km(n-k)}.
\]
These exact rational forms permit a finite complete comparison without numerical tolerance.

An independent canonicalization of all connected simple graphs gives \(1,2,6,21\) unlabeled connected graphs on \(2,3,4,5\) vertices. Exhausting every nonconstant binary field on every graph gives reversal-class counts
\[
0,0,0,11.
\]
This proves the sharp order-five boundary and the count of five-vertex graph classes that admit a reversal.

For the path family, the endpoint singleton has \(k=1\), \(q=1\), \(s=1\), and \(m=n-1\), giving
\[
I(A_n)=-\frac1{(n-1)^2}
\]
and
\[
C(A_n)=\frac{n}{2(n-1)}.
\]
The adjacent internal pair has \(k=2\), \(q=2\), \(s=4\), and \(m=n-1\), giving
\[
I(B_n)=\frac{n^2-4n-4}{2(n-1)(n-2)}
\]
and
\[
C(B_n)=\frac{n}{2(n-2)}.
\]
Clearly \(C(B_n)>C(A_n)\). Moreover,
\[
I(B_n)-I(A_n)
=
\frac{n(n^2-5n+2)}{2(n-2)(n-1)^2},
\]
which is positive for every integer \(n\ge5\). This proves the persistent reversal family.

## Verification
The embedded `verify_moran_geary_minimal_reversal.py` uses only the Python standard library and exact rational arithmetic.

For each \(n\le5\), it generates every labeled simple graph, retains the connected graphs, and independently quotients them by all vertex permutations. It recovers the known connected-unlabeled counts
\[
1,2,6,21.
\]
For every retained graph it evaluates every nonconstant binary field directly from the original Moran and Geary definitions and independently from the closed \((k,q,s,m)\) formulas. These computations agree exactly.

The checker confirms zero reversal-admitting connected graph classes on \(2,3,4\) vertices and exactly \(11\) on five vertices. It also verifies the general degree-weighted identity on every checked graph and the regular-graph affine identity on every checked regular graph.

The path witness is checked directly at \(n=5\), and the symbolic path-family formulas are checked for every \(5\le n\le500\) as a finite consistency test. The all-\(n\) statement is proved algebraically above.

Run:

`python3 verify_moran_geary_minimal_reversal.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Moran's classical 1950 paper is the foundational source for the spatial autocorrelation statistic now bearing his name. Geary subsequently introduced the contiguity ratio that became Geary's \(C\).

de Jong, Sprenger and van Veen study extreme values of Moran's \(I\) and Geary's \(C\) for a given spatial network. Their analysis emphasizes that extrema depend on the weight matrix and that structural differences in the network, including differences in neighborhood structure, affect the coefficients. This is the closest inspected primary work to the graph-structural mechanism used here.

The literature also treats Moran and Geary as related but differently sensitive spatial autocorrelation statistics. The result here isolates a sharper finite phenomenon under one fixed, transparent weight convention: regular graphs force an exact affine equivalence, irregularity permits disagreement, and five vertices are the exact first order at which a binary field can produce a strict ranking reversal.

Targeted searches using both statistic names, graph and lattice language, binary fields, regular-graph relations, five-site examples, and the exact witness values did not locate the affine regular-graph identity together with the sharp five-vertex reversal boundary or the \(11\)-of-\(21\) five-vertex census.

## Limitations
The order-five minimum is specific to unstandardized symmetric adjacency weights and binary fields.

Row standardization changes the weight matrix and generally destroys the simple regular-versus-irregular reduction used here.

The \(11\)-of-\(21\) count records whether a graph admits at least one reversal; it does not count all fields or assign a probability to encountering a reversal.

The theorem is a structural statement about the indices, not a recommendation that one statistic should replace the other in empirical spatial analysis.

An unindexed exercise, software test suite, or specialized graph-spatial note could contain the same five-vertex witness even if the complete sharp boundary is absent.

## References
1. P. A. P. Moran, “Notes on Continuous Stochastic Phenomena,” *Biometrika* 37(1–2), 17–23, published 1 June 1950. DOI: 10.1093/biomet/37.1-2.17.
2. R. C. Geary, “The Contiguity Ratio and Statistical Mapping,” *The Statistician* 5(3), 115–146, 1954. DOI: 10.2307/2986645.
3. P. de Jong, C. Sprenger and F. van Veen, “On Extreme Values of Moran's I and Geary's c,” *Geographical Analysis* 16(1), 17–24, 1984. DOI: 10.1111/j.1538-4632.1984.tb00797.x.
