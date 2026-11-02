# Critical-group fingerprints of all three \((9_3)\) Levi graphs

## Finding
A combinatorial \((9_3)\) configuration consists of nine points and nine distinct three-point lines, with each point on exactly three lines and no pair of points on two different lines. Its *Levi graph* has one vertex for every point and every line, joined across the bipartition when incident. The critical group of a connected graph is the finite abelian group presented by any reduced integer Laplacian.

There are exactly three isomorphism classes of such configurations. Classify them by \(t\), the number of triangles in the point-collinearity graph (two points adjacent when sharing a line). The three possible values and the complete critical groups are
\[
\begin{array}{c|l|r}
t&K(\mathrm{Levi})&\tau(\mathrm{Levi})\\\hline
27&\mathbb Z/2\oplus(\mathbb Z/6)^2\oplus(\mathbb Z/18)^2\oplus\mathbb Z/54&1{,}259{,}712\\
29&\mathbb Z/2\oplus\mathbb Z/6\oplus\mathbb Z/48\oplus\mathbb Z/2160&1{,}244{,}160\\
30&\mathbb Z/214\oplus\mathbb Z/5778&1{,}236{,}492
\end{array}
\]
where \(\tau\) denotes the number of spanning trees. The class \(t=27\) is the classical Pappus configuration, whose critical group was already recorded by Joyner and Melles (2017); it serves as the **known comparison**, not as a newly determined group. The two non-Pappus decompositions, together with their exhaustive classification context, are the substantive result. In particular the two non-Pappus classes have respectively \(5\)-primary and \(107\)-primary torsion, while the Pappus group has neither.

## Assumptions and scope
The claim applies to **all** simple combinatorial \((9_3)\) point-line incidence structures, allowing non-geometric realizations and identifying structures under arbitrary relabelling of points and lines. Point-collinearity counts use three *distinct* points and ignore which line, if any, realizes each collinear pair. No result about other \((n_3)\) families, weighted Laplacians, or geometric realizability is claimed.

Representatives are provided explicitly as unordered line triples on points \(\{0,1,\ldots,8\}\). The order of the nine displayed lines is immaterial.

\(t=27\): `036 147 258 048 156 237 057 138 246`.

\(t=29\): `247 148 367 358 025 157 068 126 034`.

\(t=30\): `018 136 568 238 257 345 147 067 024`.

The last two representatives are the non-Pappus classes. All have nine lines, three points per line, and point-degree three.

## Proof
**Classification by finite exhaustion.** Every permitted line is one of the \(\binom{9}{3}=84\) triples. To list each **point-labelled, line-unlabelled** configuration once, process the point labels in increasing order. At point \(i\), choose the required additional triples *having least point \(i\)*, in increasing lexicographic order. Reject a choice if any point would occur more than three times or any unordered point pair would recur. Every valid configuration arises uniquely: all lines with least point below \(i\) were necessarily chosen earlier, and all lines with least point \(i\) are an unordered subset uniquely listed in increasing order. At the final point all degrees must equal three. The complete executable `verify_census93.cpp` implements this argument, visits exactly 1,690,154 recursive states, and finds exactly 73,920 point-labelled configurations. Their collinearity-triangle counts are
\[
N_{27}=3360,\qquad N_{29}=30240,\qquad N_{30}=40320.
\]
The same program directly tests all \(9!\) point permutations of each explicit representative. Their numbers of point automorphisms are, respectively, \(108,12,9\). The orbit-stabilizer formula therefore gives point-labelled orbit sizes
\[
9!/108=3360,\qquad9!/12=30240,\qquad9!/9=40320.
\]
These match the complete census in each distinct triangle stratum. Thus every stratum is a single isomorphism class, and no fourth class exists. The first representative is obtained from the nine points of the ternary affine plane by retaining the nine lines of three of its four directions; hence it is Pappus.

**Integral critical groups.** For each explicit incidence matrix \(B\) (nine rows for points, nine columns for lines), its Levi graph has Laplacian
\[
L=\begin{pmatrix}3I_9&-B\\-B^\mathsf T&3I_9\end{pmatrix}.
\]
All three graphs are connected, as checked directly by breadth-first search in `verify_smith93.py`. Delete the final row and column to obtain an integral \(17\times17\) reduced Laplacian \(R\). Exact integer Smith reduction gives nonunit invariant factors, in ascending divisibility order,
\[
\begin{array}{c|l|r}
t&\text{nonunit Smith factors}&\text{unit Smith factors}\\\hline
27&(2,6,6,18,18,54)&11\\
29&(2,6,48,2160)&13\\
30&(214,5778)&15.
\end{array}
\]
The standalone `verify_smith93.py` constructs \(R\) from the stated nine triples, computes Smith normal form over \(\mathbb Z\), checks the divisibility chain, and independently computes the positive determinant by exact fraction-free Bareiss elimination. The products of the Smith factors equal the Bareiss determinants, as the algorithm checks. Therefore the displayed direct sums are precisely \(\mathbb Z^{17}/R\mathbb Z^{17}\). By the matrix-tree theorem, the determinants are exactly the displayed spanning-tree counts. Their prime factorizations are
\[
\tau_{27}=2^6 3^9,\qquad \tau_{29}=2^{10}3^5 5,\qquad \tau_{30}=2^2 3^3 107^2.
\]
Every critical-group and spanning-tree statement follows from these exact computations. They are finite exhaustive calculations, not statistical or extrapolated evidence.

## Verification
Compile and execute `verify_census93.cpp` with `c++ -O2 -std=c++17 verify_census93.cpp -o census93 && ./census93`. Install the single documented Python dependency with `python -m pip install -r requirements.txt`, then execute `python verify_smith93.py`. Expected terminal markers are `NINE_THREE_CLASSIFICATION_PASS` and `THREE_CONFIGURATIONS_EXACT_SANDPILE_PASS`. The first establishes exhaustive incidence-structure coverage and orbit matching; the second checks independently encoded incidences, connectedness, exact Smith factors, exact determinants, and prime factors. Actual executed results are recorded in `VERIFICATION.md`.

## Relationship to prior work
The general language of combinatorial configurations and their point-line realizations is classical; see Bokowski, Kovič, Pisanski and Žitnik (arXiv:1410.2350, first public October 9, 2014). Critical groups of graphs are classical; Bond and Levine (arXiv:1409.0170, first public August 30, 2014) give a general treatment in the broader abelian-network setting. Joyner and Melles, *Adventures in Graph Theory* (Springer, 2017, §5.18), **explicitly report the Pappus Smith factors** \((2,6,6,18,18,54)\). This already-published row is not new. The comparison here determines the integral critical groups for the other two combinatorial \((9_3)\) types and embeds them in an exhaustive three-class arithmetic fingerprint. In particular, neither the general critical-group definition nor the Pappus row implies the two non-Pappus Smith decompositions.

## Limitations
The classification and Smith decompositions are computer-assisted exact finite proofs with inspectable small standalone source files. They depend on faithful execution of integer arithmetic and the SymPy Smith-normal-form implementation; the determinant products and two independent representations of incidence data provide crosschecks, but they do not constitute external independent audit. No claim of mathematical novelty is made for the previously published Pappus critical group. Unindexed configuration tables or non-English treatments may contain one or both other groups; this residual originality risk remains. A complete survey of every published table is not claimed.

## References
1. J. Bokowski, J. Kovič, T. Pisanski and A. Žitnik, *Combinatorial configurations, quasiline arrangements, and systems of curves on surfaces*, arXiv:1410.2350 (first posted 2014-10-09), https://arxiv.org/abs/1410.2350.
2. B. Bond and L. Levine, *Abelian Networks III. The Critical Group*, arXiv:1409.0170 (first posted 2014-08-30), https://arxiv.org/abs/1409.0170.
3. W. D. Joyner and C. G. Melles, *Adventures in Graph Theory*, Springer, 2017, §5.18, ISBN 978-3-319-68383-6 (known Pappus row).
4. B. Grünbaum, *Configurations of Points and Lines*, AMS Graduate Studies in Mathematics 103, 2009 (general classical theory of configurations).
