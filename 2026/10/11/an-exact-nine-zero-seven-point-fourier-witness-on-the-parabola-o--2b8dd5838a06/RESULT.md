# An exact nine-zero seven-point Fourier witness on the parabola over the eleven-element field

## Finding
For the seven-point support \(R=\{0,1,2,3,4,5,7\}\subset\mathbb F_{11}\), an explicit full-support coefficient vector in \(\mathbb Z[\zeta]\), where \(\zeta=e^{2\pi i/11}\), makes
\[F(a,b)=\sum_{x\in R}c_x\zeta^{ax^2+bx}\]
vanish at **exactly nine** frequency pairs in \(\mathbb F_{11}^2\):
\[(0,4),(1,0),(1,1),(1,9),(6,6),(6,7),(6,9),(7,3),(9,9).\]
In particular, the maximum number of zeros at exact support size seven in this field is at least nine. **No global upper bound of nine or sharp classification is established here.**

## Assumptions and scope
All arithmetic in the exponents is modulo 11. Put \(\Phi_{11}(t)=1+t+\cdots+t^{10}\). For each support point \(x\), define \(c_x=\sum_{j=0}^9 d_{x,j}\zeta^j\), with integer coefficients in the following table. The entries are listed for \(j=0,1,\ldots,9\), in that order.

| \(x\) | \((d_{x,0},\ldots,d_{x,9})\) |
| --- | --- |
| 0 | 14, 6, 9, 12, 4, 7, 10, 2, 16, 8 |
| 1 | 4, -3, 1, 5, -2, 2, 6, -1, 3, -4 |
| 2 | -4, 3, -1, -5, 2, -2, 5, 1, -3, 4 |
| 3 | 9, 18, 5, 3, 12, 10, 8, 6, 15, 13 |
| 4 | 6, 1, 7, 2, -3, 3, 9, 4, -1, 5 |
| 5 | -12, -2, -3, -4, -5, -6, 4, -8, -9, 1 |
| 7 | -6, -12, -7, -2, -8, -3, -9, -4, -10, -5 |

## Proof
The eleventh cyclotomic polynomial \(\Phi_{11}\) is irreducible over \(\mathbb Q\) and has degree 10. Hence the ten classes \(1,\zeta,\ldots,\zeta^9\) form a rational basis of \(\mathbb Q(\zeta)\), and each of the seven distinct, visibly nonzero integer coefficient rows specifies a nonzero \(c_x\). Thus the actual spectral support consists of all seven listed points.

For each pair \((a,b)\in\mathbb F_{11}^2\), form the integer polynomial
\[P_{a,b}(t)=\sum_{x\in R}\Big(\sum_{j=0}^9d_{x,j}t^j\Big)t^{(ax^2+bx)\bmod 11}.\]
Then \(F(a,b)=0\) if and only if the remainder of \(P_{a,b}(t)\) upon division by \(\Phi_{11}(t)\) is zero. This criterion is exact; it involves no floating-point evaluation. Applying integer polynomial reduction to all \(11^2=121\) pairs gives precisely the nine pairs displayed in the finding. The following verification routine states this finite exhaustive computation completely and independently of external databases.

## Verification
Run `python3 verify_parabola_seven_nine.py` using the Python 3 standard library. It carries out integer arithmetic in the faithful quotient \(\mathbb Z[t]/(\Phi_{11}(t))\), verifies full support and the complete 121-pair zero set, and prints an exact PASS result. A separate symbolic remainder computation with SymPy independently reproduced the same nine pairs. The executable proof obligation is finite (121 evaluations), not an extrapolation from samples.

## Relationship to prior work
The first public version of Li's 2026 paper proves a seven-point upper bound of ten for primes at least eleven (Theorem 4.13), but states explicitly in Remark 4.15 that the exact maximum at \(p=11\) is not determined. It provides a five-point example with six zeros (Proposition 4.11), which does not imply existence at exact seven-point support. The October 3 second version focuses on complete mutually unbiased bases and retains a weaker general bound, without this seven-point refinement. The present statement is a constructive nine-zero **lower-bound witness**, not a reproof of either source bound or a determination of the optimum.

## Limitations
The global maximum for seven-point spectral support at eleven is not proved here. The first-version published ten-zero upper estimate would, if valid, confine it to nine or ten when combined with this construction; that estimate is not independently recertified in this result and was not retained in the later version. No uniqueness, orbit count, broader-prime extension, or arbitrary-support census is claimed. As with any novelty claim, an unindexed equivalent witness remains possible.

## References
1. Dongwei Li, Parity-Sensitive Fourier Uncertainty and Zero-Set Rigidity on the Finite Parabola, arXiv:2609.16030v1, 2026-09-11, Section 4.1, Theorem 4.13 and Remark 4.15. https://arxiv.org/html/2609.16030v1
2. Dongwei Li, Sharp Total-Support Uncertainty for the Standard Complete Set of Mutually Unbiased Bases, arXiv:2609.16030v2, 2026-10-03, Theorem 1.2 and Section 3. https://arxiv.org/html/2609.16030v2
