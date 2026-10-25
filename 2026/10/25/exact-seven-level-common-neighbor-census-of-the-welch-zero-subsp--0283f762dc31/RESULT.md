# Exact seven-level common-neighbor census of the Welch zero-subspace graph over \(\mathbb F_{128}\)

## Finding
Let \(F=\mathbb F_{2}[t]/(t^{7}+t+1)\) and \(W(x)=x^{11}\). Write \(\mathcal Z\) for the three-dimensional \(\mathbb F_2\)-subspaces \(E\) of \(F\) with \(\sum_{x\in E}W(x)=0\). Form the simple graph \(\Gamma\) on \(\mathcal Z\), connecting distinct \(E,E'\) precisely when \(\dim_{\mathbb F_2}(E\cap E')=1\).

**Exact claim.** There are precisely 127 vertices, which form one orbit under scalar multiplication by \(F^{\times}\), and \(\Gamma\) is a 42-regular cyclic graph. The complete distribution of unordered pairs according to adjacency and number of common neighbors is:

| Pair type | Common neighbors | Unordered pairs |
|:--|--:|--:|
| Adjacent | 15 | 1778 |
| Adjacent | 21 | 889 |
| Nonadjacent | 8 | 889 |
| Nonadjacent | 10 | 889 |
| Nonadjacent | 12 | 1778 |
| Nonadjacent | 14 | 889 |
| Nonadjacent | 16 | 889 |

In particular, the graph has 2667 edges and 15113 triangles. These are finite, exact integer statements; no asymptotic or unverified extrapolation is made.

## Assumptions and scope
All field operations are in characteristic two. The binary word \(x=\sum_{j=0}^{6}x_jt^j\) is represented in `certificate_welch127.py` by the integer \(\sum_{j=0}^{6}x_j2^j\). The reduction polynomial is \(t^7+t+1\), encoded by hexadecimal `0x83`; addition is bitwise XOR. The polynomial is irreducible by the checked degree-seven Rabin criterion. The exponent is \(11=2^3+3\), the Welch exponent at extension degree seven. The object is the set of *linear* three-spaces, not all affine translates.

The seed space \(E_0=\langle1,t,t^3\rangle_{\mathbb F_2}\) has nonzero point set
\[D=\{1,t,1+t,t^3,1+t^3,t+t^3,1+t+t^3\}.\]
Here \(D\), in the integer encoding, is `(1,2,3,8,9,10,11)`.

## Proof
The included `certificate_welch127.py` is a finite proof certificate consisting solely of exact integer operations and exhaustive loops, and its completeness follows from the following arguments.

**1. Exhaustion of candidate spaces.** Every three-space has a basis of three \(\mathbb F_2\)-independent nonzero vectors. Enumerating unordered independent triples \(a,b,c\) and taking their seven distinct nonzero subset sums therefore includes every three-space. Removing duplicate seven-point bitmasks gives exactly 11811 spaces. Independently, the certificate enumerates every reduced-row-echelon 3-by-7 binary matrix: choose the three pivot columns, put arbitrary binary entries only in the nonpivot columns to the right of each pivot, and create the associated seven-point mask. Uniqueness of reduced-row-echelon form makes this exhaustive and injective; it also yields exactly 11811 masks, identical to the first enumeration. This equals the Gaussian binomial \(\left[\begin{smallmatrix}7\\3\end{smallmatrix}\right]_2=11811\).

**2. Exactly 127 zero sums.** For every enumerated mask, calculate the seven powers by repeated-squaring multiplication modulo \(t^7+t+1\) and XOR them. Exactly 127 masks have zero Welch sum. Independently, the seven powers of the explicitly displayed seed have XOR zero. Its scalar orbit contains exactly 127 distinct masks and agrees with the exhaustive set. Distinctness can also be seen without the loop: the multiplicative group \(F^\times\) has prime order 127, so the seed stabilizer is trivial (the seven-element set \(D\) cannot be invariant under all 127 nonzero scalars). Thus the zero-sum family is exactly \(\{uE_0:u\in F^\times\}\).

**3. Cyclic graph and common-neighbor formula.** Compute the ratio set
\[R=\{a/b:a,b\in D,\ a\ne b\}\subset F^\times.\]
Exact enumeration shows all 42 ratios are distinct and \(1\notin R\). Therefore distinct scalar translates \(uE_0\) and \(vE_0\) have a one-dimensional intersection precisely when \(v/u\in R\): each ratio records one common nonzero point, and uniqueness of the 42 ratios rules out a second. Consequently \(\Gamma\) is the undirected Cayley graph of the cyclic group \(F^\times\) with symmetric connection set \(R=R^{-1}\), so it is 42-regular.

For each \(s\in F^\times\setminus\{1\}\), the number of common neighbors of the vertices \(E_0\) and \(sE_0\) is exactly
\[c(s)=|R\cap sR|.\]
The certificate enumerates each of the 126 possible multipliers using exact field multiplication and checks the full table of `(pair type, common neighbors, number of multipliers)`:

| Pair type | Common neighbors | Multipliers |
|:--|--:|--:|
| Adjacent | 15 | 28 |
| Adjacent | 21 | 14 |
| Nonadjacent | 8 | 14 |
| Nonadjacent | 10 | 14 |
| Nonadjacent | 12 | 28 |
| Nonadjacent | 14 | 14 |
| Nonadjacent | 16 | 14 |

The multiplicative action is regular on vertices, so each multiplier type contributes \(127/2\) times its number of multipliers to the number of unordered pairs. This gives exactly the first table and exhausts \(\binom{127}{2}=8001\) unordered pairs.

**4. Triangles.** Each triangle appears three times in the sum, over unordered edges, of the number of common neighbors. Hence the number of triangles is
\[\frac{1778\cdot15+889\cdot21}{3}=15113.\]

## Verification
Execute `python3 certificate_welch127.py` in a standard Python 3 environment. It uses no third-party modules. It verifies irreducibility by the degree-seven Rabin criterion, checks field inverses, independently enumerates all 11811 three-spaces in two ways, identifies all 127 zero-sum spaces, checks the entire 126-multiplier intersection table, and confirms the triangle count. A second independent direct 127-by-127 graph implementation is supplied as `crosscheck_intersection.py` and checks the pair table without the ratio-set formula. Both scripts use exact bit operations, not floating-point thresholds.

As an external numerical consistency check only, the Kloosterman sum \(\mathrm{Kl}_7=-13\) obtained by exact trace enumeration gives \(127(129-3(-13))/168=127\), consistent with the Cheng–Hu total-count formula. That formula alone does not yield the common-neighbor distribution.

## Relationship to prior work
Cheng and Hu, *Counting subspaces with prescribed Welch sums*, arXiv:2610.15694v1 (first publicly posted 2026-10-11), prove a formula for the **number** of Welch-zero three-spaces in odd binary extension degree and the number through each nonzero field element, and study Kloosterman and Dickson-determinant reductions. Their full accessible text, Sections 1–4, gives neither an intersection graph nor a common-neighbor census. At extension degree seven their counting theorem yields 127 spaces, agreeing with the count here; the present claim concerns the additional and distinct seven-level pair-intersection codegree invariant. Hou and Zhao's related 2026 paper studies sum-freedom and Dickson-matrix criteria; its full text was not available in this comparison. Classical constant-dimension subspace codes and packing designs motivate the intersection viewpoint, and an implicit equivalent in that literature remains possible.

## Limitations
The statement is for one natural first positive nontrivial Welch degree, \(n=7\), over \(\mathbb F_2\), with exponent \(11\). It does not assert the graph profile for other extension degrees or exponents and does not classify graph automorphisms or spectra. The numerical certificate is exhaustive only because the finite field and all of its three-spaces are completely enumerated. No independent mathematical audit has been performed. A coincidentally equivalent intersection graph in previous cyclic subspace-code literature is a residual originality risk.

## References
1. K. Cheng and J. Hu, *Counting subspaces with prescribed Welch sums*, arXiv:2610.15694v1, first public 2026-10-11. https://arxiv.org/abs/2610.15694
2. X. Hou and J. Zhao, *Further results on sum-freedom of binary and \(q\)-ary functions*, arXiv:2609.31489v1 (related work; full text unavailable in this comparison). https://arxiv.org/abs/2609.31489
3. M. Braun and A. Reichelt, *q-Analogs of Packing Designs* (2012), background context; not used in the certificate.
