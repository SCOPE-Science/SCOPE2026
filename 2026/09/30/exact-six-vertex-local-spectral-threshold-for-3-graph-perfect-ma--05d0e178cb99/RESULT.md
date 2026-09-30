# Exact six-vertex local spectral threshold for 3-graph perfect matchings
## Finding
Let \(H\) be a 3-uniform hypergraph on six vertices. For each vertex \(v\), let \(L_H(v)\) be the ordinary graph on the other five vertices whose edges are the pairs \(xy\) with \(vxy\in E(H)\), and define
\[
\sigma(H)=\min_{v\in V(H)}\rho(L_H(v)),
\]
where \(\rho\) denotes adjacency spectral radius.

If \(H\) has no perfect matching, then
\[
\sigma(H)\le 2.
\]
The bound is sharp. Moreover, equality \(\sigma(H)=2\) occurs in exactly five isomorphism types.

For a partition \(V=X\sqcup Y\) with \(|X|=|Y|=3\), let \(F(X,Y)\) consist of all nine triples having exactly two vertices in \(X\) and one in \(Y\). Up to relabeling, the five equality types are:

1. \(F(X,Y)\);
2. \(F(X,Y)\cup\{X\}\), where \(X\) itself is regarded as a triple;
3. \(F(X,Y)\cup\{Y\}\);
4. the full 3-uniform star on six vertices;
5. the unique \(2\text{-}(6,3,2)\) design.

Thus the local spectral perfect-matching condition \(\sigma(H)>2\) is exact already at the first nontrivial order divisible by three.

## Assumptions and scope
Hypergraphs are finite, simple, and 3-uniform. A perfect matching on six vertices consists of two disjoint triples. The spectral radius is the largest eigenvalue of the adjacency matrix of an ordinary simple graph. The statement is only for order six; it makes no claim for order nine or larger finite orders not covered by existing asymptotic theorems.

## Proof
On six vertices, two disjoint triples are necessarily complementary and together form a perfect matching. Hence a 3-graph has no perfect matching exactly when it is intersecting. The twenty possible triples split into ten complementary pairs, so every intersecting family is obtained by choosing, independently in each pair, the first triple, the second triple, or neither. There are therefore exactly \(3^{10}=59049\) labeled intersecting families.

The first verifier enumerates precisely these \(59049\) families. For every vertex \(v\), it forms the five-vertex link adjacency matrix \(A_v\). The comparison with the threshold is exact: \(\rho(L_H(v))\le2\) if and only if \(2I-A_v\) is positive semidefinite. Because the matrix is real symmetric, positive semidefiniteness is certified by the nonnegativity of all principal minors, computed by exact integer Bareiss elimination. Positive definiteness distinguishes \(\rho<2\) from \(\rho=2\). No intersecting family has all six link radii larger than \(2\).

Exactly 78 labeled families have \(\sigma(H)=2\). Canonicalization under all \(6!\) vertex permutations yields five orbits, of labeled sizes \(20,20,6,20,12\). Their sorted degree sequences are respectively \((3,3,3,6,6,6)\), \((3,3,3,7,7,7)\), \((4,4,4,4,4,10)\), \((4,4,4,6,6,6)\), and \((5,5,5,5,5,5)\), which also separates the five isomorphism types.

A second implementation independently enumerates all \(2^{20}\) labeled 3-graphs and filters those containing no complementary edge pair. It computes every five-vertex link characteristic polynomial exactly by the Faddeev--LeVerrier recurrence. After shifting the variable by \(2\), the polynomial remains real-rooted because it is the characteristic polynomial of a real symmetric matrix; after removing any zero root, Descartes sign variation therefore counts the positive roots exactly. This gives an independent exact comparison of each link spectral radius with \(2\). The second enumeration again finds \(59049\) matching-free families, 78 labeled equality cases, five isomorphism types, and orbit sizes \(6,12,20,20,20\).

For the five representatives, the link-radius multisets are, respectively,
\[
\{2,2,2,\sqrt6,\sqrt6,\sqrt6\},\quad
\{2,2,2,3,3,3\},\quad
\{2,2,2,2,2,4\},\quad
\{2,2,2,\sqrt6,\sqrt6,\sqrt6\},\quad
\{2,2,2,2,2,2\}.
\]
Hence every listed type attains equality.

## Verification
Two complete exact enumerations are included. `artifacts/verify_psd.py` uses the complementary-pair parameterization and exact principal-minor tests. `artifacts/verify_charpoly.py` scans all labeled 3-graphs and uses exact characteristic polynomials with a shifted-root count. The two methods agree on the threshold, the 78 labeled equality cases, the five isomorphism types, and their orbit sizes. `artifacts/equality_types.json` records canonical representatives and invariants.

## Relationship to prior work
Liu and O introduced the local parameter \(\sigma(H)\) in this perfect-matching setting and proved that, for sufficiently large order \(n\) divisible by three, the condition \(\sigma(H)>\frac{2n}{3}-2\) forces a perfect matching. At \(n=6\), that threshold is exactly \(2\). Their preprint is the literature source motivating the present finite-order question.

Polcyn and Ruciński previously classified maximal intersecting triple systems, including 13 maximal isomorphism types on six vertices. That structural classification is compatible with the exhaustive search here, but the present statement concerns the local spectral parameter across all intersecting six-vertex triple systems, including a nonmaximal equality family.

## Limitations
The proof is finite and computer-assisted. It does not establish the corresponding exact threshold at \(n=9\), does not provide a purely human classification proof of the five equality types, and does not imply a stability theorem near \(\sigma(H)=2\). The exhaustive certificates are exact, but no independent external audit or formal proof assistant verification is claimed.

## References
1. P. Liu and S. O, *Exact local spectral thresholds for perfect matchings in 3-graphs and 3-partite 3-graphs*, arXiv:2609.26832, first submitted 2026-09-21. MSC 05C50, 05C65, 05C70, 05D05.
2. J. Polcyn and A. Ruciński, *A hierarchy of maximal intersecting triple systems*, Opuscula Mathematica 37 (2017), 597--608, DOI 10.7494/OpMath.2017.37.4.597.
