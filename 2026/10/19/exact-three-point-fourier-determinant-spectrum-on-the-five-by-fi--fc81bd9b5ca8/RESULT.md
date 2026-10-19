# Exact three-point Fourier determinant spectrum on the five-by-five affine plane

## Finding
Put \(G=\mathbb F_5^2\), \(\zeta=\exp(2\pi i/5)\), and, for distinct three-element sets \(A,B\subset G\), define the *unnormalized squared Fourier volume*
\[
Q(A,B)=\left|\det\bigl(\zeta^{a\cdot b}\bigr)_{a\in A,\,b\in B}\right|^2.
\]
For each fixed \(A\), the complete list of \(Q(A,B)\) values and their multiplicities among the \(\binom{25}{3}=2300\) choices of \(B\) depends only on whether \(A\) is collinear or noncollinear. Write \(s=\sqrt5\).

| Squared determinant \(Q(A,B)\) | Collinear \(A\) | Noncollinear \(A\) |
| --- | ---: | ---: |
| \(0\) | 1050 | 150 |
| \(5\) | 0 | 900 |
| \((15-5s)/2\) | 0 | 500 |
| \((15+5s)/2\) | 0 | 500 |
| \((25-5s)/2\) | 625 | 75 |
| \((25+5s)/2\) | 625 | 75 |
| \((35-5s)/2\) | 0 | 50 |
| \((35+5s)/2\) | 0 | 50 |

Consequently the exact maximum of \(Q(A,B)\) over \(B\), namely the square of the determinant tightness \(D(A)\), equals \((25+5\sqrt5)/2\) for collinear \(A\) and \((35+5\sqrt5)/2\) for noncollinear \(A\): the optimal squared volume increases by **exactly \(5\)** when the row aperture is noncollinear. The numbers of optimizing partners per row support are respectively \(625\) and \(50\).

In the standard noncollinear coordinates \(A=\{(0,0),(1,0),(0,1)\}\), every optimizing \(B\) is a translate of exactly one of
\[
\{(0,0),(1,3),(3,1)\},\qquad
\{(0,0),(1,3),(3,2)\},
\]
and these two translation orbits are disjoint and have \(25\) members each. For a standard collinear aperture \(A=\{(0,0),(1,0),(2,0)\}\), the optimizers are precisely the \(B\) whose first-coordinate projection is \(\{t,t+1,t+3\}\) for some \(t\in\mathbb F_5\), with arbitrary second coordinates for the three frequency points.

Since exactly \(300\) three-point row sets are collinear and \(2000\) are noncollinear, the number of ordered pairs \((A,B)\) in which \(B\) maximizes \(Q(A,B)\) is \(300\cdot625+2000\cdot50=287500\). There are \(615000\) singular and \(4675000\) nonsingular ordered three-by-three Fourier minors in total.

## Assumptions and scope
All coordinates and dot products are taken modulo \(5\). Sets of row and column indices contain exactly three **distinct** points; ordering changes the determinant only by sign. The Fourier matrix is **unnormalized**: its entries have modulus one. The squared volume is zero for singular submatrices. A row set is collinear if it lies in an affine line in \(\mathbb F_5^2\). The result is an exact finite classification at characteristic five; it makes no assertion for other primes or for larger minors.

## Proof
**Affine reduction.** Translating either indexing set multiplies matrix rows or columns by complex unit scalars, preserving \(Q\). For any invertible \(2\)-by-\(2\) matrix \(L\) over \(\mathbb F_5\), the simultaneous transformation \(A\mapsto LA\), \(B\mapsto L^{-T}B\) preserves every matrix entry. Affine transformations are transitive on noncollinear triples, represented by \(A_{\mathrm{tri}}=\{0,e_1,e_2\}\), and on collinear triples, represented by \(A_{\mathrm{line}}=\{0,e_1,2e_1\}\). For the latter, this follows because every three-subset of a five-point affine line is the complement of a two-set, and the one-dimensional affine group is transitive on two-sets.

**Collinear triples.** Write a column index as \(b=(x,y)\). The selected matrix is the Vandermonde matrix with nodes \(\zeta^x\), so its determinant is \(\prod_{i<j}(\zeta^{x_j}-\zeta^{x_i})\), up to sign. If any first coordinates coincide the determinant is zero. Otherwise the ten unordered triples of distinct residues \(x\in\mathbb F_5\) split into two five-member classes, represented by \(\{0,1,2\}\) and \(\{0,1,3\}\). The identity \(|1-\zeta^k|^2=2-2\cos(2\pi k/5)\) gives the two corresponding squared Vandermonde volumes \((25-5\sqrt5)/2\) and \((25+5\sqrt5)/2\). Every choice of three distinct first coordinates has \(5^3=125\) separate lifts to \(G\), establishing the \(625,625,1050\) counts and the explicit equality cases.

**Noncollinear triples.** Normalize \(A=A_{\mathrm{tri}}\). Translate and order the three frequency points so they become \(0,(a,b),(c,d)\), with the latter two distinct and nonzero. Elementary determinant expansion gives
\[
\Delta=(\zeta^a-1)(\zeta^d-1)-(\zeta^c-1)(\zeta^b-1)
=\zeta^{a+d}-\zeta^a-\zeta^d-\zeta^{b+c}+\zeta^b+\zeta^c.
\]
Let \(c_j\in\mathbb Z\) be the coefficient of \(\zeta^j\) in this six-term expression (all exponents reduced modulo five) and set
\[
R_k=\sum_{j=0}^4 c_jc_{j-k\bmod5},\qquad k=0,1,2.
\]
The cyclotomic identities \(\zeta+\zeta^{-1}=(\sqrt5-1)/2\) and \(\zeta^2+\zeta^{-2}=(-1-\sqrt5)/2\) imply the **exact integer-pair formula**
\[
Q=\frac{2R_0-R_1-R_2+(R_1-R_2)\sqrt5}{2}.
\]
Enumerate the \(\binom{24}{2}=276\) unordered pairs of nonzero distinct vectors \((a,b),(c,d)\); the displayed six-term formula and three five-term integer sums require no numerical approximation. The resulting *rooted* counts, in the same row order as the theorem table, are
\[
(18,108,60,60,9,9,6,6).
\]
These are a finite exact certificate: `checker.py` contains the complete two-level nested finite loops and checks every case again by an independent six-permutation determinant expansion. For each frequency set \(B\), exactly three of the \(25\) translates of the rooted configurations represent \(B\) (one translation for each of its members). Hence the counts among all \(2300\) unrooted frequency triples equal \(25/3\) times the rooted counts. This proves the eight-level table with exact arithmetic.

The rooted maximizers consist of the following six unordered pairs (listed in coordinates over \(\mathbb F_5\)):
\[
\begin{gathered}
\{(1,3),(3,1)\},\ \{(1,3),(3,2)\},\ \{(2,3),(3,1)\},\\
\{(2,3),(4,2)\},\ \{(2,4),(3,2)\},\ \{(2,4),(4,2)\}.
\end{gathered}
\]
Translating each of the three points of an optimizing triple to the origin partitions the six rooted patterns into two classes of three, giving precisely the two \(25\)-element translation orbits stated above. No three-point set is fixed by any nonzero translation in this group of exponent five, since an entire nontrivial orbit would contain five points.

**Global counts.** There are \(5(5+1)=30\) affine lines, each with \(\binom53=10\) triple subsets: \(300\) collinear row sets and \(2300-300=2000\) noncollinear row sets. Multiplying the two row-type partner counts establishes both the global optimizer total and singular/nonsingular totals.

## Verification
Run `python3 checker.py`. The standalone standard-library script recomputes the two full \(2300\)-column spectra by exact cyclotomic integer arithmetic, independently expands each determinant using all six matrix permutations, verifies the \(276\)-pair rooted formula and its multiplicity scaling, checks both families of equality cases, and verifies the global totals. It prints `CHECK_PASS`. The proof is a finite exhaustive classification, not an extrapolation from a sample; the checker uses no floating-point comparisons or external data.

## Relationship to prior work
Ferguson, Mayeli and Sothanaphan [1] define the determinant tightness \(D(A)=\max_B|\det F_{A,B}|\) for finite-group exponential bases (Definitions 3.9--3.10) and derive general conditioning inequalities. Their framework motivates computing exact determinant spectra but does not provide this eight-level affine-plane classification. Caragea and Lee [2] analyze vanishing of **principal** minors for **cyclic** Fourier matrices, not the magnitude distribution of all three-row/three-column minors of the noncyclic character table here. The existing rank classification of three-by-three affine-plane Fourier minors [3] settles only whether each determinant is zero, and cannot determine the seven positive squared-volume levels or the optimizer orbits. A corresponding cyclic prime-square rank census [4] concerns the nonisomorphic cyclic group and again does not give these magnitudes.

## Limitations
This result is exact for the finite field of five elements only and does not yield a formula in general prime order. Determinant volume is a quantitative basis-quality invariant, but it is **not** the condition number; no optimal Riesz ratio is inferred. Possible equivalent calculations in older complex-Hadamard, generalized-Vandermonde, or signal-design tables remain a bibliographic risk; an unsuccessful search alone would not establish originality. No independent mathematical validation has been performed.

## References
1. S. Ferguson, A. Mayeli and N. Sothanaphan, *Riesz bases of exponentials and multi-tiling in finite abelian groups*, arXiv:1904.04487 (first public version 2019-04-09), Sections 1, 3.2, 4.19.
2. A. Caragea and D. G. Lee, *On the principal minors of Fourier matrices*, arXiv:2409.09793 (first public version 2024-09-15), Introduction and Theorems 1.1--1.2.
3. *Complete rank geometry of three-by-three Fourier minors in prime affine planes*, published mathematical research record, claim identifier `ba0b52ec-4cec-4558-ae98-7f2dff2d78cf` (rank comparison only).
4. *All singular three-by-three minors of prime-square Fourier matrices*, published research record at https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-all-singular-three-by-three-minors-of-prime-square-fourier-matri--feb52ea6712b (cyclic group comparison only).
