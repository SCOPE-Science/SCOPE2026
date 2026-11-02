# Critical group of the McGee \((3,7)\)-cage

## Finding

The McGee graph \(G\), the unique cubic graph of girth seven on twenty-four vertices, has integral critical (Jacobian or sandpile) group
\[
K(G)\cong \mathbb Z/11\mathbb Z\ \oplus\ \mathbb Z/44\mathbb Z\ \oplus\ \mathbb Z/132\mathbb Z\ \oplus\ \mathbb Z/2640\mathbb Z.
\]
In particular, its minimal number of generators is four, its exponent is \(2640\), and its \(11\)-primary part is \((\mathbb Z/11\mathbb Z)^4\). The group order, equivalently the spanning-tree count, is \(168{,}664{,}320\); that count is already listed by House of Graphs and is not asserted to be new. The contribution is the full integral invariant-factor decomposition.

## Assumptions and scope

The graph is simple and undirected. To make its coordinates unambiguous, take \(V(G)=\mathbb Z/24\mathbb Z\). Include all edges \(\{i,i+1\}\) and the chords \(\{i,i+s_i\}\), with indices reduced modulo \(24\), where
\[
(s_0,s_1,s_2)=(-12,7,-7),\qquad s_{i+3}=s_i.
\]
Treat unordered duplicate edge descriptions as one edge. This is the conventional \(\operatorname{LCF}([-12,7,-7]^8)\) presentation of the McGee graph. It has \(24\) vertices, \(36\) edges, degree three at every vertex, and girth seven. The original graph and its girth-extremal role were described by McGee in May 1960; the standard LCF representation appears in MathWorld.

For the combinatorial Laplacian \(L=3I-A\), delete row and column labelled \(23\), obtaining \(M\in\mathbb Z^{23\times23}\). Define
\[
K(G)=\mathbb Z^{23}/M\mathbb Z^{23}.
\]
For a connected graph, this finite abelian group is canonically independent of the deleted root up to isomorphism. All claimed invariants refer to this integral cokernel, not merely to the rational Laplacian spectrum.

## Proof

The complete integer proof is an explicit elementary-operation certificate. Construct \(M\) from the stated edges: diagonal entries are the original vertex degrees \(3\), and off-diagonal entries are \(-1\) precisely at adjacent retained vertices and \(0\) otherwise. The companion `certificate.json` lists \(471\) operations of the following five types on this exact matrix: interchange two rows; interchange two columns; add an integer multiple of one row to another; add an integer multiple of one column to another; negate a row. Each operation is multiplication by an integer matrix of determinant \(\pm1\), and therefore preserves the integral cokernel up to isomorphism.

The script `verify_certificate.py` independently constructs the stated graph and reduced Laplacian, replays every certificate operation with exact Python integers, and checks that the resulting matrix has zero off-diagonal entries and the diagonal
\[
\operatorname{diag}(\underbrace{1,\ldots,1}_{19},11,44,132,2640).
\]
The positive diagonal entries form a divisibility chain because \(11\mid44\mid132\mid2640\). Thus this diagonal is the Smith normal form, proving the displayed isomorphism. The determinant of the reduced Laplacian, which may change sign under elementary operations but not magnitude, is
\[
\lvert\det M\rvert=11\cdot44\cdot132\cdot2640=168{,}664{,}320.
\]
By the matrix-tree theorem this equals the number of spanning trees. The nonunit invariant factors establish the four-generator claim and exponent.

A separate verification does not use the elementary-operation certificate. The script `verify_independent.py` constructs a differently labelled \(24\)-vertex, \(36\)-edge cubic graph of girth seven from an explicit independent edge list. The classical uniqueness of the \((3,7)\)-cage identifies its isomorphism type with \(G\). It computes \(\det M\) via exact fraction-free elimination. It also diagonalizes each reduced Laplacian modulo a sufficiently high prime power, recording the exponents of its elementary divisors. For primes \(2,3,5,11\) the nonzero exponent lists are, respectively,
\[
(2,2,4),\quad (1,1),\quad(1),\quad(1,1,1,1).
\]
These yield the same invariant factors after aligning primary factors in increasing divisibility order; the determinant has no other prime factors. This is a second, algorithmically different check of the integral conclusion.

## Verification

Run, from a folder containing the three companion files:

```
python3 verify_certificate.py
python3 verify_independent.py
```

Both programs require only the Python 3 standard library. They independently check the graph order, degree, connectivity and girth; the first checks all \(471\) unimodular steps and the exact Smith diagonal; the second checks the determinant and complete primary Smith exponents by modular elimination. The computation uses exact integers throughout. The supplied matrix-operation list, rather than an unsupported numerical report, is the finite certificate for the critical nonstandard computation.

## Relationship to prior work

McGee (1960) constructs a minimal cubic graph of girth seven, and later literature identifies the unique cage. MathWorld provides its LCF representation and adjacency spectrum. House of Graphs lists its spanning-tree count as \(168{,}664{,}320\); this agreement is a consistency check, not a new spanning-tree enumeration. Bacher, de la Harpe and Nagnibeda (1997) establish general integral cut/flow lattice and graph Jacobian theory. None of these accessible descriptions supplies the stated McGee-specific invariant factors.

Existing critical-group formulas for complete multipartite graphs, products of complete graphs or Cayley graphs are not automatically applicable: the McGee graph is neither complete multipartite nor vertex-transitive. A later paper on spectral polynomials and graph descriptors of cages discusses closely related spectral data, but its complete publisher text was not accessible here; the available abstract does not claim Smith invariant factors. Since a spectral polynomial determines the spanning-tree number but does not in general determine the integral Smith form, knowing the former is not enough to infer the displayed decomposition. An equivalent calculation in other literature may exist.

## Limitations

This is a single-graph exact invariant, not a formula for all cubic cages, and it does not determine dynamics of individual sandpile configurations. The uniqueness identification of the two graph presentations relies on established cage classification; the two programs themselves also verify the required graph properties. The result gives a reproducible calculation of the finite abelian group, not a claim of first-ever computation beyond the literature actually inspected. An older unindexed graph-invariant table could contain the same decomposition.

## References

1. W. F. McGee, “A Minimal Cubic Graph of Girth Seven,” *Canadian Mathematical Bulletin* **3** (1960), 149–152. DOI: 10.4153/CMB-1960-018-1. Original May 1960 article.
2. E. W. Weisstein, “McGee Graph,” *MathWorld*, https://mathworld.wolfram.com/McGeeGraph.html. Graph identification and LCF representation.
3. *House of Graphs*, graph 1223, https://houseofgraphs.org/graphs/1223. Known spanning-tree count.
4. R. Bacher, P. de la Harpe and T. Nagnibeda, “The lattice of integral flows and the lattice of integral cuts on a finite graph,” *Bull. Soc. Math. France* **125** (1997), 167–198, DOI: 10.24033/bsmf.2303.
5. K. Balasubramanian, “Spectral polynomials, graph descriptors, spectra, and entropies of cage graphs,” *J. Math. Chem.* **63** (2025), 1949–1988, DOI: 10.1007/s10910-025-01747-4. Accessible abstract only.
