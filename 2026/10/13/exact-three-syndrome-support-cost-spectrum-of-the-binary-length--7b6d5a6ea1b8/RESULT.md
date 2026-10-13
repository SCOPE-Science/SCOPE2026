# Exact three-syndrome support-cost spectrum of the binary length-fifteen Melas code

## Finding

The binary length-fifteen Melas code has precisely \(97155\) three-dimensional syndrome subspaces. For each such subspace \(W\), the least number \(c(W)\) of coordinate positions needed to span every syndrome in \(W\) has generating polynomial

\[\sum_{\dim W=3}z^{c(W)}=330z^3+6510z^4+39885z^5+49230z^6+1200z^7.\]

Thus exactly \(1200\) three-dimensional syndrome subspaces require seven positions; all others require at most six. This is a complete finite-code *distribution*, not a new assertion about the already-known maximum generalized covering radius.

## Assumptions and scope

Use the binary field \(\mathbb F_2\) and the extension \(\mathbb F_{16}=\mathbb F_2[t]/(t^4+t+1)\). Let \(\alpha\) be the image of \(t\); it has multiplicative order \(15\). For \(0\le i<15\), let \(h_i=(\alpha^i,\alpha^{-i})\in\mathbb F_{16}^2\cong\mathbb F_2^8\). Let \(H\) be the eight-by-fifteen binary matrix with these columns, and \(C=\ker H\). This is the binary Melas code at extension degree four. The columns span all eight syndrome dimensions.

For a three-dimensional binary subspace \(W\le\mathbb F_2^8\), define

\[c(W)=\min\{|J|:J\subseteq\{0,\ldots,14\},\ W\subseteq\operatorname{span}_{\mathbb F_2}\{h_j:j\in J\}\}.\]

This is the minimum simultaneous coordinate-support size for any choice of three linearly independent prescribed syndromes spanning \(W\). It depends only on the subspace, not on the chosen ordered basis. All statements are restricted to this one code, with the displayed fixed parity-check representation.

## Proof

Field multiplication in the chosen polynomial basis reduces modulo \(t^4+t+1\). The fifteen successive powers of \(\alpha\) enumerate the nonzero extension-field elements, so the fifteen check columns are explicitly and uniquely defined by the pairs of four-bit words \((\alpha^i,\alpha^{-i})\). Represent any syndrome by an integer from zero through \(255\), encoding the first field element in the high four bits and the second in the low four bits.

Every three-dimensional subspace of \(\mathbb F_2^8\) has exactly one reduced-row-echelon ordered basis with pivot positions \(0\le b_0<b_1<b_2\le7\). Row \(r\) has a one in pivot column \(b_r\), zeros in the other pivot columns and in columns preceding \(b_r\), and arbitrary entries only in nonpivot columns greater than \(b_r\). Iterating all pivot choices and all remaining free bits visits each three-space exactly once. Their count is the Gaussian coefficient

\[{8\brack3}_2=\frac{(2^8-1)(2^8-2)(2^8-4)}{(2^3-1)(2^3-2)(2^3-4)}=97155.\]

For each coordinate subset \(J\), form the full binary span of its check columns by repeated XOR closure. Store that span as a 256-bit incidence mask. For a three-space \(W\), form its eight-element incidence mask from the XOR combinations of its three echelon basis rows. Then \(W\) lies in the coordinate span for \(J\) **if and only if** each set bit of the mask for \(W\) is a set bit of the mask for \(J\). The program `verify.cpp` tests exactly this condition for every coordinate subset of cardinality three through seven in increasing cardinality, assigning the first feasible cardinality as \(c(W)\). A rank-three subspace cannot be spanned by fewer than three columns, so the initial cardinality is sharp; the program also explicitly checks that no three-space remains without a containing subset of size at most seven.

The complete executable enumeration gives precisely \(330,6510,39885,49230,1200\) three-spaces of costs \(3,4,5,6,7\), respectively. Their sum is the theoretical Gaussian count \(97155\). The basis represented by integers \((81,2,4)\) furnishes a concrete cost-seven example. The program checks its cost using the same exhaustive subset containment criterion.

No inference from partial experiments or a timeout is used: finite exhaustive enumeration over all echelon bases and all relevant coordinate subsets proves the claimed fixed-parameter identity.

## Verification

Compile the accompanying standard-library C++ source using `g++ -O2 -std=c++17 verify.cpp -o verify`, then run `./verify`. Its deterministic output contains `COUNT 97155`, `HIST 3:330 4:6510 5:39885 6:49230 7:1200`, `WITNESS 81,2,4`, and `VERIFY_OK`. The program checks field order, all echelon bases, containment by explicit XOR spans, the number of subspaces and the five bin counts. All arithmetic is exact integer and binary-field arithmetic.

A separate subset-first enumeration also produced the same cost histogram, based on the number of three-spaces contained in spans of coordinate subsets of cardinalities three through seven. The row-echelon program is the complete standalone reproducibility artifact.

## Relationship to prior work

Li and Xiong's 2026 generalized-covering study supplies the binary Melas check matrix and studies generalized covering radii. Prior work, including Luo, Yang, Ye, Cao and Özbudak and the later account of generalized covering radii at \(t\ge3\), already establishes maximum three-syndrome cost seven. This work does **not** claim that radius as new. The contribution is the entire distribution by cost: a maximum alone specifies only that the last coefficient is positive and the polynomial degree is seven, not that the last coefficient equals \(1200\) or that any of the other four coefficients have the stated values.

The definition admits the equivalent description as the access cost of a three-dimensional subspace of cosets, or as the minimum support size for a matrix of three independent syndrome columns. Counting ordered independent syndrome triples instead would multiply each enumerator coefficient by \(168\). Thus the polynomial fixes the normalization explicitly.

## Limitations

The numerical distribution is proved only for the binary Melas code with \(m=4\), length \(15\). Nothing here establishes the distribution for other extension degrees, independence from arbitrary unrelated column families, or a symbolic formula across an infinite family. The result uses exhaustive finite computation; scientific originality remains subject to independent historical verification, especially against earlier coset-leader tables or equivalent projective-geometry classifications. Independent audit has not been performed.

## References

- S. Li and M. Xiong, *The generalized covering radii of Melas codes*, arXiv:2608.29906 (first public 2026-08-30), https://arxiv.org/abs/2608.29906.
- Luo, Yang, Ye, Cao and Özbudak, *Generalized Covering Radius of Binary Melas Codes*, IEEE Transactions on Information Theory, DOI:10.1109/TIT.2026.3733076.
- *The generalized covering radii of Melas codes at \(t\ge3\): exact values and finite geometric structure* (2026), https://ideosphere.ai/papers/melas-covrad.
