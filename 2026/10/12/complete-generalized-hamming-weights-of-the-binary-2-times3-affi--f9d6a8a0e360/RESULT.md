# Complete generalized Hamming weights of the binary \(2\times3\) affine Grassmann code

## Finding
Let \(C=C^{\mathbb A}(2,5)\) be the binary affine Grassmann code obtained by evaluating the constant, the six coordinate functions and the three \(2\times2\) minors of a generic binary \(2\times3\) matrix at all 64 such matrices. Its generalized Hamming weights are exactly
\[
(d_1,d_2,d_3,d_4,d_5,d_6,d_7,d_8,d_9,d_{10})=(24,36,42,48,54,56,60,62,63,64).
\]
In particular, the previously undetermined middle values are \(d_4=48\) and \(d_5=54\). Exactly 28 four-dimensional subcodes attain support 48, and 1,120 five-dimensional subcodes attain support 54. These counts concern subspaces, not ordered bases.

## Assumptions and scope
All matrices and code operations are over \(\mathbb F_2\). Write \(X=(x_{ij})\), with \(i\in\{0,1\}\) and \(j\in\{0,1,2\}\). Define ten functions in this order: the constant 1; the six entries \(x_{00},x_{01},x_{02},x_{10},x_{11},x_{12}\); and the three minors
\[
M_{ij}=x_{0i}x_{1j}+x_{0j}x_{1i},\qquad 0\le i<j\le2.
\]
The code is the span of their evaluation vectors, with coordinates indexed by all \(X\in\mathbb F_2^{2\times3}\), ordered by the six entry bits (first row, then second). For an \(r\)-dimensional subcode \(U\le C\), its support is the set of positions where some word of \(U\) is nonzero; \(d_r(C)\) is the minimum support cardinality over all such \(U\). Only this one finite binary code is classified.

## Proof
**Injectivity and normalization.** The attached verifier constructs evaluation vectors \(E(a)\in\mathbb F_2^{64}\) for all 1,024 binary coefficient masks \(a\in\{0,\ldots,1023\}\), checking that all are distinct. Hence evaluation from the coefficient space \(\mathbb F_2^{10}\) onto \(C\) is an isomorphism and \(\dim C=10\). The ten functions are precisely the minors of sizes zero, one and two in the standard definition, so the tested code is the stated affine Grassmann code.

**Exhaustive finite lower bounds.** Every \(r\)-dimensional coefficient subspace has exactly one reduced-row-echelon \(r\times10\) basis. For every increasing pivot tuple \(p_1<\cdots<p_r\), its row \(i\) has a 1 in pivot \(p_i\); every other pivot position is 0; every nonpivot entry strictly left of \(p_i\) is 0; and every nonpivot entry strictly right of \(p_i\) may be chosen freely in \(\mathbb F_2\). The verifier iterates all pivot tuples and all free bits. No subspace is missed or counted twice. For each basis the support of the generated subcode is exactly the bitwise union of its \(r\) row-evaluation supports. Thus taking the minimum of its 64-bit population count proves the global minimum, not merely a constructed upper bound. Each stage checks the total number of enumerated subspaces against the Gaussian binomial coefficient \(\genfrac{[}{]}{0pt}{}{10}{r}_2\), and checks the minimum and its multiplicity. The resulting complete vectors are
\[
(d_r)_{r=1}^{10}=(24,36,42,48,54,56,60,62,63,64),
\]
\[
(N_r)_{r=1}^{10}=(112,448,64,28,1120,24,1456,2016,64,1),
\]
where \(N_r=|\{U\le C:\dim U=r,\ |\operatorname{Supp}(U)|=d_r\}|\).

**Upper-bound witnesses.** Coefficient vectors, encoded by their ten basis bits as nonnegative integers, for the four-dimensional optimum are \((65,258,516,8)\), and for the five-dimensional optimum are \((65,258,516,8,144)\). Their evaluation-support unions have cardinalities 48 and 54 respectively. The verifier recomputes those unions directly. In conjunction with exhaustive lower bounds this establishes equality. All remaining ranks are enumerated by the same method and agree with the published initial and terminal formulas.

## Verification
Run `g++ -O3 -std=c++17 artifacts/verify.cpp -o verify` and then `./verify` from the directory containing this document. Standard C++17 and its library suffice; no external datasets, packages, optimization solvers, or network access are needed. The verifier builds the generator evaluations afresh, verifies all 1,024 coefficient masks give distinct codewords, visits every binary RREF space in dimensions 1 through 10, and asserts the claimed minima, numbers of attaining subcodes, and all Gaussian-binomial totals. The successful run ends with `VERIFY_OK`. In particular, rank four checks 53,743,987 spaces and rank five checks 109,221,651 spaces. The exhaustive certificate proves this finite instance only; no partial-enumeration extrapolation is used.

## Relationship to prior work
Datta and Ghorpade, *Higher Weights of Affine Grassmann Codes and Their Duals* (2015), Theorems 2.5 and 3.3, determine the first three and last five entries for the specific parameters \(q=2,\ell=2,\ell'=3\). Their general formulas therefore establish ranks \(1,2,3,6,7,8,9,10\), but not ranks 4 or 5. The present exact computation fills precisely that two-rank interval and gives the numbers of minimizing subcodes. Rohit Yadav, *Revisiting the Weight Spectrum of the Affine Grassmann Code* (2026), investigates weights of individual codewords, rather than the supports of higher-dimensional subcodes as described in its abstract. Ordinary codeword weight distributions do not determine these missing generalized weights without further arguments. The original construction and minimum-distance results are due to Beelen, Ghorpade and Høholdt.

## Limitations
This is an exact finite classification for \(C^{\mathbb A}(2,5)\) over \(\mathbb F_2\), not a general formula for other alphabets or matrix sizes. Completeness depends on the explicit RREF census and its reproducible implementation. The September 2026 preprint's full text was not available for inspection; while its abstract concerns individual codeword weights, an unindexed equivalent higher-weight calculation cannot be ruled out. Scientific review performed here is not an independent audit.

## References
1. M. Datta and S. R. Ghorpade, *Higher Weights of Affine Grassmann Codes and Their Duals*, Contemporary Mathematics 637 (2015), 79–91, arXiv:1503.02196v1, DOI: 10.1090/conm/637/12750.
2. R. Yadav, *Revisiting the Weight Spectrum of the Affine Grassmann Code \(C^{\mathbb A}(2,m)\)*, arXiv:2609.10274v1 (first public version 2026-09-09).
3. P. Beelen, S. R. Ghorpade, and T. Høholdt, *Affine Grassmann codes*, IEEE Transactions on Information Theory 56 (2010), 3166–3176, DOI: 10.1109/TIT.2010.2048470.
