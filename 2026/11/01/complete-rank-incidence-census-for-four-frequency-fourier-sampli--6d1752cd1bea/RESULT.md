# Complete rank-incidence census for four-frequency Fourier sampling on the cyclic group of order fifteen

## Finding
Let \(\zeta=\exp(2\pi i/15)\), let \(F=(\zeta^{rc})_{r,c\in\mathbb Z_{15}}\), and let \(\mathcal Q\) be the set of all four-element subsets of \(\mathbb Z_{15}\). For every ordered pair \((R,C)\in\mathcal Q^2\), consider the complex matrix \(F[R,C]\) with rows and columns listed in increasing order. Its rank distribution is **exactly**:

| Complex rank | Number of ordered pairs \((R,C)\) |
|---:|---:|
| \(1\) | \(0\) |
| \(2\) | \(4,500\) |
| \(3\) | \(161,100\) |
| \(4\) | \(1,697,625\) |

The total is \(\binom{15}{4}^2=1,863,225\). There are exactly **18 affine orbits** of four-element index subsets. The following complete row-orbit profile gives the orbit representative, its cardinality, and the numbers of four-element column sets giving each rank:

| Orbit | Representative \(R\) | Size | Rank \(2\) | Rank \(3\) | Rank \(4\) |
|---:|---|---:|---:|---:|---:|
| 0 | \({0,1,2,3}\) | 60 | 0 | 0 | 1365 |
| 1 | \({0,1,2,4}\) | 120 | 0 | 0 | 1365 |
| 2 | \({0,1,2,5}\) | 120 | 0 | 15 | 1350 |
| 3 | \({0,1,2,6}\) | 120 | 0 | 15 | 1350 |
| 4 | \({0,1,2,7}\) | 120 | 0 | 15 | 1350 |
| 5 | \({0,1,3,4}\) | 60 | 0 | 60 | 1305 |
| 6 | \({0,1,3,6}\) | 120 | 0 | 165 | 1200 |
| 7 | \({0,1,3,7}\) | 30 | 0 | 150 | 1215 |
| 8 | \({0,1,3,9}\) | 120 | 0 | 150 | 1215 |
| 9 | \({0,1,3,10}\) | 120 | 0 | 75 | 1290 |
| 10 | \({0,1,3,11}\) | 60 | 0 | 45 | 1320 |
| 11 | \({0,1,3,13}\) | 60 | 0 | 75 | 1290 |
| 12 | \({0,1,4,5}\) | 30 | 0 | 75 | 1290 |
| 13 | \({0,1,4,10}\) | 60 | 0 | 195 | 1170 |
| 14 | \({0,1,5,6}\) | 60 | 15 | 300 | 1050 |
| 15 | \({0,1,5,10}\) | 60 | 15 | 600 | 750 |
| 16 | \({0,1,6,10}\) | 30 | 15 | 450 | 900 |
| 17 | \({0,3,6,9}\) | 15 | 150 | 810 | 405 |

This is also a complete **affine-orbit rank-incidence classification**: for each representative row orbit and each column orbit, the exact number of rank-\(2\) and rank-\(3\) column subsets is the following sparse table. An entry `j:a/b` means column orbit index `j` contributes `a` rank-\(2\) and `b` rank-\(3\) subsets; all omitted entries have both counts zero, and the rank-\(4\) count is the column-orbit size minus these two counts.

- Orbit 0: no singular column orbits.
- Orbit 1: no singular column orbits.
- Orbit 2: 17:0/15.
- Orbit 3: 17:0/15.
- Orbit 4: 17:0/15.
- Orbit 5: 15:0/60.
- Orbit 6: 14:0/60`; `15:0/60`; `16:0/30`; `17:0/15.
- Orbit 7: 12:0/30`; `13:0/60`; `15:0/60.
- Orbit 8: 14:0/60`; `15:0/60`; `16:0/30.
- Orbit 9: 15:0/60`; `17:0/15.
- Orbit 10: 16:0/30`; `17:0/15.
- Orbit 11: 15:0/60`; `17:0/15.
- Orbit 12: 7:0/30`; `16:0/30`; `17:0/15.
- Orbit 13: 7:0/30`; `14:0/60`; `15:0/60`; `16:0/30`; `17:0/15.
- Orbit 14: 6:0/120`; `8:0/120`; `13:0/60`; `17:15/0.
- Orbit 15: 5:0/60`; `6:0/120`; `7:0/30`; `8:0/120`; `9:0/120`; `11:0/60`; `13:0/60`; `16:0/30`; `17:15/0.
- Orbit 16: 6:0/120`; `8:0/120`; `10:0/60`; `12:0/30`; `13:0/60`; `15:0/60`; `17:15/0.
- Orbit 17: 2:0/120`; `3:0/120`; `4:0/120`; `6:0/120`; `9:0/120`; `10:0/60`; `11:0/60`; `12:0/30`; `13:0/60`; `14:60/0`; `15:60/0`; `16:30/0.

## Assumptions and scope
All ranks are over \(\mathbb C\), and all four-point row and column subsets are unordered selections of distinct residues, represented by increasing lists when forming a matrix. Both subset coordinates range independently over all \(\binom{15}{4}=1365\) possibilities. The Fourier matrix is **unnormalized**; scaling by a common nonzero constant does not alter any rank. The affine group consists of \(r\mapsto ar+b\), with \(a\) a unit modulo \(15\) and \(b\in\mathbb Z_{15}\), acting separately on row and column subsets. Rank-\(2\) means two linearly independent measured directions survive; it is not merely singularity of the determinant.

## Proof
The cyclotomic polynomial for the primitive fifteenth root is
\[\Phi_{15}(X)=X^8-X^7+X^5-X^4+X^3-X+1.\]
For any \(k\in\{2,3,4\}\) and any distinct \(k\)-element row and column sets \(A=(a_1,\ldots,a_k)\), \(B=(b_1,\ldots,b_k)\), expand the Fourier minor determinant as the integer polynomial
\[P_{A,B}(X)=\sum_{\sigma\in S_k}\operatorname{sgn}(\sigma)X^{(\sum_{i=1}^k a_i b_{\sigma(i)})\bmod15}.\]
Then \(\det F[A,B]=P_{A,B}(\zeta)\), and, since \(\Phi_{15}\) is the minimal polynomial of \(\zeta\) over \(\mathbb Q\),
\[\det F[A,B]=0\quad\Longleftrightarrow\quad P_{A,B}(X)\equiv0\pmod{\Phi_{15}(X)}.\]
This is a computation in the free integer basis \(1,X,\ldots,X^7\), so zero testing involves no rounding or approximate equality. The attached complete executable certificate precomputes the eight integer coefficients of \(X^t\bmod\Phi_{15}\) for \(0\le t<15\); it then tests all \(k\)-minors by signed-permutation expansion. The rank is \(4\) if the four-minor is nonzero, otherwise \(3\) if some three-minor is nonzero, otherwise \(2\) if some two-minor is nonzero, and \(1\) otherwise (all Fourier entries are nonzero). These conditions are equivalent to the ordinary rank definition by the minor criterion.

There are \(8\) units modulo \(15\), hence \(120\) affine transformations. They partition the \(1365\) index sets into precisely the 18 disjoint orbits tabulated above: the certificate constructs each orbit from every not-yet-covered subset and checks coverage and disjointness. If \(R'=aR+b\), then
\[F[R',C]=F[R,aC]\,\operatorname{diag}(\zeta^{bc})_{c\in C},\]
up to row ordering, so the complex rank is unchanged; multiplication of columns by the unit \(a\) permutes each affine column orbit. Consequently it is sufficient to test every one of the \(1365\) column sets against each of the 18 displayed row representatives, not every pair separately. The executable certifies each of those \(24,570\) representative cases exactly, counts the rank distribution separately for each column orbit, and checks that the transpose-symmetry weighted incidence identities hold. Multiplying each representative count by the size of its row orbit proves the four stated global totals and the entire 18-by-18 incidence table.

## Verification
Run `python3 verify_fourier15.py` from the directory containing the attached verifier. Only the Python standard library is used. Successful execution prints all 18 row profiles, the 18-by-18 sparse rank-\(2\)/rank-\(3\) incidence table, `RANK_TOTALS {2: 4500, 3: 161100, 4: 1697625}`, and `EXACT_CERTIFICATE_OK`. The certificate tests 18 orbit representative rows against all 1365 four-element column subsets, computes any necessary lower-order minors, and checks weighted transposition symmetry and the entire count. It has no external tables, numerical rank tolerances, or unaudited file inputs. The monic cyclotomic identity was independently checked by symbolic polynomial computation.

## Relationship to prior work
The familiar Vandermonde four-row family and the already-known full-spark criterion for the near-consecutive row pattern \(\{0,1,2,4\}\) imply two full-spark orbits in the table; these are **not** claimed as new. Alexeev, Cahill and Mixon's Fourier full-spark analysis gives foundational affine symmetries and prime-power criteria, not the rank-\(2\)/rank-\(3\) incidence of all order-fifteen four-minors. Delvaux and Van Barel's work concerns low-rank Fourier blocks and Kronecker tilings; its inspected abstracts describe constructions and uncertainty inequalities, not an exhaustive 18-orbit four-minor rank census. The original full text of that historical work could not be inspected, so a stronger historical implication remains possible. Other published classifications examine different Fourier orders, principal minors, or three-by-three minors; none inspected supplies this exact table.

## Limitations
The result is finite and **only** for the 15-point complex Fourier matrix and four distinct rows/four distinct columns. It does not determine singular values, condition numbers, larger minors, arbitrary group orders, or the number of realizations modulo simultaneous row-column symmetries. The proof is an exhaustive exact integer certificate combined with the stated cyclotomic and affine reductions, not a short closed-form derivation for the counts. Historical coverage uncertainty persists where plausible older full text was inaccessible, and independent mathematical validation has not been performed.

## References
1. B. Alexeev, J. Cahill, and D. G. Mixon, *Full Spark Frames*, first posted 17 October 2011, arXiv:1110.3548, especially Section 2 and Theorem 4. https://arxiv.org/abs/1110.3548
2. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices*, Linear Algebra and its Applications 426 (2007), 349–367, DOI:10.1016/j.laa.2007.05.009; technical report TW477 (November 2006). Full text not inspected.
3. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Fourier matrices*, Linear Algebra and its Applications 429 (2008), 1587–1605, DOI:10.1016/j.laa.2008.04.043. Abstract inspected.
