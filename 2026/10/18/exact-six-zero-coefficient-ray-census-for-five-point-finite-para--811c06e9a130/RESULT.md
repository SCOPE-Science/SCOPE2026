# Exact six-zero coefficient-ray census for five-point finite-parabola Fourier sums over the eleven-element field

## Finding
Let \(\zeta=\exp(2\pi i/11)\). For each five-element subset \(S\subset\mathbb F_{11}\), choose nonzero complex coefficients \(c_x\) for every \(x\in S\), and set
\[
F_{S,c}(a,b)=\sum_{x\in S}c_x\zeta^{ax^2+bx},\qquad (a,b)\in\mathbb F_{11}^2.
\]
Two coefficient choices on the same support are identified exactly when they differ by a common scalar in \(\mathbb C^\times\). Among the \(462=\binom{11}{5}\) distinct supports, there are exactly **\(532400\) pairs consisting of a support and a projective coefficient ray whose Fourier sum has precisely six zeros**.

All six affine support orbits under \(x\mapsto ux+v\), with \(u\in\mathbb F_{11}^\times\), \(v\in\mathbb F_{11}\), and their exact counts are:

| Support representative | Supports in orbit | Six-zero rays per support | Largest zero count |
| --- | ---: | ---: | ---: |
| \(\{0,1,2,3,4\}\) | 55 | 1210 | 6 |
| \(\{0,1,2,3,5\}\) | 110 | 605 | 6 |
| \(\{0,1,2,3,6\}\) | 110 | 3025 | 6 |
| \(\{0,1,2,3,7\}\) | 55 | 0 | 5 |
| \(\{0,1,2,4,5\}\) | 110 | 605 | 6 |
| \(\{0,1,2,4,7\}\) | 22 | 0 | 5 |

Thus precisely four affine support orbits admit the known sharp six-zero configuration, and the other two do not. The count is \(55\cdot1210+110\cdot605+110\cdot3025+110\cdot605=532400\). This is an **equality-structure census**, not a new six-zero upper bound.

## Assumptions and scope
The field is exactly \(\mathbb F_{11}\), support size is exactly five, all support coefficients are nonzero, and zeros are counted as distinct points of \(\mathbb F_{11}^2\). All scalars are complex. No coefficients are restricted to a phase alphabet. A projective ray means common scaling equivalence only, not frequency modulation or affine support equivalence. The affine orbit table is a separate classification of possible supports.

## Proof
**(1) Normalizing a Fourier zero.** Multiplying \(c_x\) by \(\zeta^{Ax^2+Bx}\) translates the zero set by \((-A,-B)\). This action of \(\mathbb F_{11}^2\) on coefficient rays is free: a quadratic polynomial that is constant on five distinct field points has vanishing quadratic and linear coefficients. Hence each ray has 121 distinct frequency-translated versions.

**(2) Why three additional zero rows suffice.** Use the row \((a,b)=(0,0)\) to eliminate the fifth coefficient. For a further frequency \(r=(a,b)\), write the resulting relation as
\[
\sum_{j=1}^{4}c_{x_j}\bigl(\zeta^{ax_j^2+bx_j}-\zeta^{ax_5^2+bx_5}\bigr)=0.
\]
For three further distinct frequencies, the \(3\times4\) complex matrix of these relations has rank at most three. If it has rank three, its signed maximal minors span its unique projective nullspace; reconstruct the fifth coefficient as minus the other four. Thus every coefficient ray with a zero at the origin and four independent zero evaluations occurs among the exhaustive enumeration of three-frequency subsets from the remaining 120 frequencies.

To exclude the overlooked rank-at-most-three case for a *six*-zero ray, the included integer-arithmetic checker exhaustively tests every one of the \(6\binom{120}{3}\) matrices for the six affine-support representatives. It finds that **each rank-deficient triple of nonorigin frequencies is collinear with the origin**. Were six zero-evaluation rows to have rank at most three, any three nonorigin zeros would yield rank-deficient triples and hence every zero would lie on one line through the origin. On such a line, the Fourier sum is the one-dimensional Fourier transform of fiber sums for \(h(x)=Ax^2+Bx\). Rank deficiency of the four row evaluations forces the image of \(h\) on the five support points to have **at most three** distinct values: if there were at least four, a square Fourier evaluation minor on four distinct image values and four distinct line parameters would be nonsingular by the classical prime Fourier minor theorem. The image also has **at least three** values because a nonconstant quadratic has fibers of size at most two. Thus the image has exactly three values with occupancies \(2,2,1\). Four distinct vanishing Fourier samples of a function supported on these three image values force all three fiber sums to vanish by the same prime Fourier minor theorem. The singleton forces one coefficient to vanish, contradicting exact support. Therefore every six-zero full-support ray has zero-evaluation rank four and is found by rank-three triples of eliminated relations.

**(3) Exact cyclotomic arithmetic.** For a primitive eleventh root \(\zeta\), an integral polynomial of degree at most ten vanishes at \(\zeta\) precisely when all eleven coefficients are equal. Every maximal minor constructed from three rows of differences of roots of unity has augmentation (sum of cyclic polynomial coefficients) zero; the same holds for each reconstructed Fourier evaluation. Thus, within this calculation, vanishing at \(\zeta\) is equivalent to **all eleven integer cyclic coefficients being zero**. The checker represents these elements of \(\mathbb Z[\zeta]\) as signed integer arrays of length eleven. Its six permutation terms in each \(3\times3\) determinant and its eight binomial choices per term are evaluated exactly. It rejects coefficient vectors with any zero coordinate, determines all 121 Fourier evaluations exactly, and deduplicates by the full six-zero location set. Every zero-row set of rank four has a unique projective coefficient direction; no two different rays can therefore be conflated by this deduplication.

**(4) Complete count.** The checker exhaustively partitions \(\binom{11}{5}=462\) supports into the six displayed affine orbits, then checks all \(\binom{120}{3}=280840\) triples for each representative. The numbers of distinct projective rays with an origin zero and precisely six zeros are, in table order, \(60,30,150,0,30,0\). Each of their translation orbits has 121 elements, of which exactly six have a zero at the origin. Therefore the numbers of all six-zero rays on one fixed support are respectively \(121\cdot(60,30,150,0,30,0)/6=(1210,605,3025,0,605,0)\), and the total is \(532400\). The maximal observed count on the two other orbits is exactly five (with a full-support witness checked by the same exhaustive enumeration); the published global bound excludes more than six everywhere.

## Verification
Compile the embedded `verify_p11.cpp` with `g++ -std=c++17 -O3 verify_p11.cpp -o verify_p11` and run `./verify_p11`. Its output reports the six representative supports, exact counts of rank-drop triples, counts of full-support minor seeds and distinct six-zero sets, confirms absence of noncollinear rank-drop triples, checks the support-orbit partition and prints `TOTAL_PROJECTIVE_RAYS=532400`. The full enumeration was run successfully using the distributed source prior to packaging. Integer-only cyclotomic calculations avoid tolerance thresholds or finite-field lifting assumptions. A separate direct cyclotomic witness check found six zero frequencies for the first support orbit. This is a computer-assisted exhaustive finite classification; the enumeration source is the reproducible computational certificate, rather than an unexecuted assertion.

## Relationship to prior work
D. Li, *Parity-Sensitive Fourier Uncertainty and Zero-Set Rigidity on the Finite Parabola* (arXiv:2609.16030, public September 11, 2026), already proves the general five-support upper bound of six Fourier zeros and establishes sharpness. Those claims are not novel here. The present classification instead counts all projective coefficient rays attaining six in the first prime-eleven five-support case and proves that only four of its six affine support orbits attain the bound. A published finite-parabola census over \(\mathbb F_7\) gives at most five zeros, with a distinct projective-ray count; a separate prime-eleven seven-support witness concerns a different support size. None of the inspected scientific statements implies the support-by-support prime-eleven equality census.

## Limitations
The theorem is restricted to the field with eleven elements. It does not classify coefficients with fewer than five nonzero entries or other field orders. Its completeness depends on the explicitly supplied, executed, exact-arithmetic enumeration, including the rank-deficient-triple geometry check; independent validation has not been performed. Historical priority relative to inaccessible full texts in related sparse uncertainty literature remains a residual risk. No generalization to all primes is claimed.

## References
1. D. Li, *Parity-Sensitive Fourier Uncertainty and Zero-Set Rigidity on the Finite Parabola*, arXiv:2609.16030, first posted 2026-09-11. https://arxiv.org/abs/2609.16030.
2. *Exact five-point finite-parabola uncertainty over the field of seven elements*, publicly indexed published-finding corpus record (2026-10-11), identifier `2026/10/11/SCOPE-exact-five-point-finite-parabola-uncertainty-over-the-field-of-s--c8e97af8983f`.
3. *An exact nine-zero seven-point Fourier witness on the parabola over the eleven-element field*, publicly indexed published-finding corpus record (2026-10-11), identifier `2026/10/11/SCOPE-an-exact-nine-zero-seven-point-fourier-witness-on-the-parabola-o--2b8dd5838a06`.
