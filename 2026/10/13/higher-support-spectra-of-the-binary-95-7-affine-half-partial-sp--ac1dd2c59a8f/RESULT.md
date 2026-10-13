# Higher-support spectra of the binary \([95,7]\) affine-half partial-spread codes

## Finding

Let \(V=\mathbb F_2^6\), let \(E_1,E_2\) be three-dimensional subspaces satisfying \(V=E_1\oplus E_2\), and set \(f(0)=0\) and \(f(x)=1\) precisely for nonzero \(x\in E_1\cup E_2\). For nonzero \(a\in V\), define the binary code

\[
C_a=\Big\{\big(uf(x)+v\cdot x\big)_{x\in V\setminus\{0\}}\ \Vert\ \big(uf(x)+v\cdot x\big)_{x\in V:a\cdot x=1}:u\in\mathbb F_2,\ v\in V\Big\}.
\]

The first block has \(63\) coordinates and the second has \(32\). With the standard nondegenerate dot product, the two normal types are \(a\in(E_1^\perp\cup E_2^\perp)\setminus\{0\}\) (inside) and \(a\notin E_1^\perp\cup E_2^\perp\) (outside). All choices in either type give permutation-equivalent codes. For \(1\le r\le7\), let \(d_r(C_a)\) be the minimum cardinality of the support of an \(r\)-dimensional subcode and let \(M_r(C_a)\) count the subcodes attaining it.

| \(r\) | Inside \(d_r\) | Inside \(M_r\) | Outside \(d_r\) | Outside \(M_r\) |
|---:|---:|---:|---:|---:|
|1|18|1|22|1|
|2|54|7|56|12|
|3|74|126|74|36|
|4|84|168|84|144|
|5|90|280|90|256|
|6|93|32|93|32|
|7|95|1|95|1|

In particular the two normal types differ in their first two generalized Hamming weights, while their weights of order \(3\) through \(7\) agree; their numbers of minimum-support subcodes differ at orders \(2\) through \(5\).

## Assumptions and scope

All operations are over \(\mathbb F_2\). A finite-dimensional subcode is counted once, regardless of the number of ordered bases. No assertion about partial-spread codes of other lengths or more than two spread members is made. The generator matrix is constructed by including, for every \(x\ne0\), the column \(g_x=(f(x),x)^{\mathsf T}\in\mathbb F_2^7\), and then adding a second copy for each \(x\) with \(a\cdot x=1\).

## Proof

**Two classes.** Any pair of complementary three-spaces in \(V\) can be carried to \(E_1=\mathbb F_2^3\times\{0\}\) and \(E_2=\{0\}\times\mathbb F_2^3\) by a linear change of variables. After this change, the stabilizer contains independent invertible changes of coordinates in the two three-blocks, together with their interchange. Its induced contragredient action on nonzero normal covectors is transitive separately on normals with exactly one nonzero block and on those with both blocks nonzero. These are precisely the inside and outside cases. Such changes merely relabel the evaluation positions, so one representative of each type suffices.

**Injectivity.** For \(x\) with both coordinate blocks nonzero we have \(f(x)=0\). A linear functional constant on all nonzero vectors of a three-dimensional binary vector space is zero (a nonzero functional assumes both values there). Therefore if \(uf(x)+v\cdot x=0\) for all nonzero \(x\), restriction to mixed-block positions forces both components of \(v\) to vanish. Restriction to \(E_1\setminus\{0\}\) then forces \(u=0\). Hence the message-to-codeword map is injective and \(\dim C_a=7\).

**Support-annihilator identity.** For an \(r\)-space \(U\le\mathbb F_2^7\) of messages, its common zero coordinates are exactly the columns \(g\) satisfying \(u\cdot g=0\) for every \(u\in U\), i.e. the columns in \(W=U^\perp\), where \(\dim W=7-r\). With \(\mu_a(g)\in\{0,1,2\}\) the multiplicity of column \(g\), this proves

\[
d_r(C_a)=95-\max_{\substack{W\le\mathbb F_2^7\\ \dim W=7-r}}\sum_{g\in W}\mu_a(g),
\qquad
M_r(C_a)=\#\Big\{W:\dim W=7-r,\ \sum_{g\in W}\mu_a(g)=95-d_r(C_a)\Big\}.
\]

Orthogonal complementation is bijective, so the last count contains neither duplicate subcodes nor missing ones.

**Exhaustive finite evaluation.** Write \(x\) as an integer from \(1\) through \(63\), with its three low bits and three high bits representing the two factors, and use the column integer \(x+64f(x)\). A normal represented by integer \(1\) is inside; a normal represented by integer \(9\) is outside. In either case, enumerate every reduced-row-echelon basis of every \((7-r)\)-space of \(\mathbb F_2^7\). For ordered pivots \(p_1<\cdots<p_k\), each row has its pivot bit, zeros in the other pivot columns, zeros left of its own pivot, and arbitrary bits in each nonpivot column strictly to its right. These choices are exactly and uniquely the RREF matrices. Enumerating all \(2^k\) elements of their spans gives the sums in the displayed formula.

The numbers of \(k\)-spaces for \(k=0,1,\ldots,7\) are \((1,127,2667,11811,11811,2667,127,1)\); the program checks every one. The resulting maximum column multiplicities in the two types are respectively \((77,41,21,11,5,2,0)\) and \((73,39,21,11,5,2,0)\), with counts \((1,7,126,168,280,32,1)\) and \((1,12,36,144,256,32,1)\). Subtracting from \(95\) gives the table. The attached checker also performs a separate direct-support census of all message subspaces and requires exact agreement at every support size, not merely at the maxima. This proves all finite assertions.

## Verification

Run `python3 verify.py` with Python \(3\). The standard-library-only program constructs both complete generator-column multisets, verifies that each has exactly \(31\) single columns and \(32\) doubled columns, and enumerates all subspaces by their unique RREF matrices. One computation unions the bitset supports of basis codewords; the other counts zero columns in orthogonal complements. Their complete subcode-support histograms agree, and the computed hierarchies and minimizer counts match the table. The successful program terminates with `VERIFY_OK`.

## Relationship to prior work

Chung, Jin, and Kim (2026, Example 1 and Equations (38)–(39)) give these two \([95,7]\) codes, their ordinary Hamming-weight enumerators, and their minimum distances \(18\) and \(22\). Those results and the coordinate-duplication construction are **not** claimed here. The result above determines their complete *higher-subcode* support hierarchies and the multiplicities of subcodes attaining every generalized weight; ordinary word-weight multiplicities do not record these incidence counts. Ding, Heng, and Zhou (2018) introduced the underlying partial-spread minimal-code family. General characterizations of generalized Hamming weights via code matroids are also known; the finite numerical and orbit-type conclusions are the claimed additions.

## Limitations

This is an exact result for the first \(m=6,r=2\) affine-half benchmark, not a formula for all even dimensions or all numbers of spread members. Its proof of the numerical values is exhaustive and finite, backed by the included checker; it should not be described as an infinite-family enumeration. The publisher's entire article was not accessible in a single direct download at the time of comparison; indexed publisher sections including the source's construction, first example, main formulas, and conclusions were inspected. Possible previously published, indirectly equivalent higher-weight spectra remain an originality risk. No independent audit was performed.

## References

1. J.-H. Chung, D. Jin, and D. Kim, “Affine-Half Extensions of Partial-Spread Minimal Binary Linear Codes with Explicit Weight Distributions,” *Mathematics* **14** (2026), 3152, published 2 September 2026, DOI: 10.3390/math14173152.
2. C. Ding, Z. Heng, and Z. Zhou, “Minimal Binary Linear Codes,” *IEEE Transactions on Information Theory* **64** (2018), 6536–6545, DOI: 10.1109/TIT.2018.2819196.
3. I. García-Marco, I. Márquez-Corbella, E. Martínez-Moro, and Y. Pitones, “Free Resolutions and Generalized Hamming Weights of Binary Linear Codes,” *Mathematics* **10** (2022), 2079, DOI: 10.3390/math10122079.
