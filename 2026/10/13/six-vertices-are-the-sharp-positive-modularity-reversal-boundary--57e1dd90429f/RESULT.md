# Six vertices are the sharp positive-modularity reversal boundary for modularity and normalized cut
## Finding
Let \(G\) be a connected finite simple undirected graph with \(m\) edges. Consider bipartitions
\[
V(G)=A\sqcup B
\]
such that
\[
|A|\ge2,\qquad |B|\ge2.
\]

Write
\[
a=\operatorname{vol}(A),\qquad
b=\operatorname{vol}(B),\qquad
a+b=2m,
\]
and let \(c\) be the number of edges crossing from \(A\) to \(B\).

For a bipartition, Newman–Girvan modularity is
\[
Q(A,B)
=
\frac{a b}{2m^2}
-
\frac{c}{m},
\]
while normalized cut is
\[
\operatorname{Ncut}(A,B)
=
\frac{c}{a}
+
\frac{c}{b}.
\]

The comparison below is restricted to bipartitions with
\[
Q(A,B)>0,
\]
so both candidate splits have positive community structure relative to the configuration-model modularity baseline.

For every connected simple graph with at most
\[
5
\]
vertices, modularity and normalized cut never give opposite strict rankings to two such bipartitions.

At
\[
6
\]
vertices this fails. Across all connected labeled six-vertex graphs there are
\[
420
\]
strictly reversing unordered partition pairs. Up to simultaneous graph isomorphism, bipartition complementation, and exchange of the two candidate partitions, these collapse to exactly two classes.

The first graph is obtained from
\[
K_4
\]
by deleting one edge and attaching a pendant path of length \(2\) to one endpoint of the missing edge. A representative has edges
\[
\{03,05,12,13,14,23,24\}.
\]

Its first split is
\[
\{0,5\}\mid\{1,2,3,4\},
\]
with
\[
c=1,\qquad
\min(a,b)=3,
\]
and
\[
Q=\frac{19}{98},
\qquad
\operatorname{Ncut}=\frac{14}{33}.
\]

Its second split is
\[
\{0,3,5\}\mid\{1,2,4\},
\]
with
\[
c=2,\qquad
\min(a,b)=6,
\]
and
\[
Q=\frac{10}{49},
\qquad
\operatorname{Ncut}=\frac7{12}.
\]

Thus modularity prefers the second split because
\[
\frac{10}{49}>\frac{19}{98},
\]
whereas normalized cut prefers the first because
\[
\frac{14}{33}<\frac7{12}.
\]

The second graph is the union of
\[
K_4
\]
and
\[
K_3
\]
sharing exactly one vertex. A representative has edges
\[
\{01,02,03,04,05,15,23,24,34\}.
\]

Its first split is
\[
\{0,2,3,4\}\mid\{1,5\},
\]
with
\[
Q=\frac{10}{81},
\qquad
\operatorname{Ncut}=\frac9{14}.
\]

Its second split is
\[
\{0,1,5\}\mid\{2,3,4\},
\]
with
\[
Q=\frac16,
\qquad
\operatorname{Ncut}=\frac23.
\]

Again modularity prefers the second split, while normalized cut prefers the first.

## Assumptions and scope
Graphs are finite, simple, undirected, and connected.

Only bipartitions are compared. Each side must contain at least two vertices.

Only positive-modularity bipartitions are admitted. This excludes splits that modularity itself regards as no better than the configuration-model baseline and focuses the comparison on plausible two-community divisions.

Modularity is maximized; normalized cut is minimized.

The result concerns the exact combinatorial objectives, not their spectral relaxations or a particular optimization algorithm.

## Proof
For a bipartition \(A\mid B\), the total number of within-community edges is
\[
m-c.
\]

The standard modularity of the bipartition is
\[
Q
=
\frac{m-c}{m}
-
\left(\frac{a}{2m}\right)^2
-
\left(\frac{b}{2m}\right)^2.
\]

Since
\[
a+b=2m,
\]
this simplifies to
\[
Q
=
\frac{ab}{2m^2}
-
\frac{c}{m}.
\]

Normalized cut is
\[
\operatorname{Ncut}
=
\frac{c}{a}+\frac{c}{b}
=
\frac{2mc}{ab}.
\]

Therefore
\[
\frac{c}{m}
=
\frac{ab}{2m^2}\operatorname{Ncut},
\]
and hence
\[
Q
=
\frac{ab}{2m^2}
\left(1-\operatorname{Ncut}\right).
\]

This identity has two immediate consequences.

First,
\[
Q>0
\quad\Longleftrightarrow\quad
\operatorname{Ncut}<1.
\]

Second, among bipartitions with the same volume product
\[
ab,
\]
maximizing modularity is exactly equivalent to minimizing normalized cut. Any reversal must therefore be driven by different volume balance.

For the sharp finite statement, every labeled simple graph through six vertices is enumerated. Connectivity is checked directly. For each connected graph, one representative of each complementary bipartition is generated, partitions with a side of size less than two are discarded, and only positive-modularity partitions are retained.

The connected labeled graph counts are
\[
1,\ 4,\ 38,\ 728,\ 26704
\]
for orders
\[
2,\ 3,\ 4,\ 5,\ 6.
\]

Every unordered pair of retained bipartitions is then compared by exact rational arithmetic. There are no strict reversals through five vertices. At six vertices there are exactly
\[
420
\]
labeled reversing pairs.

Canonicalization over all
\[
6!
\]
vertex permutations, together with partition complementation and exchange of the two candidate splits, yields exactly two isomorphism classes. Their representatives and exact objective values are the two classes stated above.

## Verification
The embedded `verify_modularity_ncut_boundary.py` uses only the Python standard library and exact rational arithmetic.

It enumerates every connected labeled graph through six vertices, reproduces the standard connected labeled counts
\[
1,\ 4,\ 38,\ 728,\ 26704,
\]
checks every admissible bipartition pair, and verifies zero strict reversals through five vertices and exactly
\[
420
\]
labeled strict reversals at six vertices.

It then canonically quotients the six-vertex reversal records under every vertex permutation, bipartition complementation, and exchange of candidate partitions, obtaining exactly two classes.

Run:

`python3 verify_modularity_ncut_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Shi and Malik introduced normalized cut as a graph-partitioning objective that balances cross-group dissimilarity against within-group association.

Newman and Girvan introduced modularity as an objective measure of community structure relative to a degree-preserving null model.

Newman later compared modularity maximization and normalized-cut graph partitioning directly and showed that suitable spectral relaxations can lead to identical spectral algorithms. That result concerns the relaxed optimization procedures, not equality of the original discrete objective orderings.

The exact identity
\[
Q
=
\frac{ab}{2m^2}
\left(1-\operatorname{Ncut}\right)
\]
makes the distinction transparent for bipartitions: the objectives agree whenever the volume product \(ab\) is fixed, while changing balance can alter the ordering.

Targeted searches using modularity, normalized cut, bipartition, ranking reversal, volume balance, smallest graph, and exact small-graph language did not locate the six-vertex positive-modularity boundary or the two complete first-layer classes.

## Limitations
The theorem is restricted to two-way partitions. Multiway modularity and multiway normalized cut have additional structure.

The positive-modularity condition is intentional. If negative-modularity candidate splits are allowed, reversal occurs earlier.

The theorem classifies only the first strict-reversal layer. It does not enumerate all larger graphs or all larger reversing partition pairs.

The original normalized-cut article was inspected through its publisher abstract and metadata rather than a complete open full text. The later full-text comparison by Newman was therefore used to assess the relationship between the two methods.

## References
1. J. Shi and J. Malik, “Normalized Cuts and Image Segmentation,” *IEEE Transactions on Pattern Analysis and Machine Intelligence* 22(8), 888–905, 2000. DOI: 10.1109/34.868688. Date of publication: 31 August 2000.
2. M. E. J. Newman and M. Girvan, “Finding and evaluating community structure in networks,” *Physical Review E* 69, 026113, 2004. DOI: 10.1103/PhysRevE.69.026113; arXiv:cond-mat/0308217.
3. M. E. J. Newman, “Spectral methods for network community detection and graph partitioning,” *Physical Review E* 88, 042822, 2013. arXiv:1307.7729.
