# Sharp minimum-weight multiplicities for rank-three quaternary paired-locality codes

## Finding

Let \(7\le u\le21\). Among the quaternary length-\(2u\) locality-one codes whose \(u\) disjoint repair pairs are constrained by a full-rank three-row global parity check with pairwise nonproportional nonzero columns, the smallest number \(A_6\) of nonzero codewords of Hamming weight six, and the number \(N_u\) of projective column subsets attaining it, are exactly:

| \(u\) | Minimum \(A_6\) | \(N_u\) |
|---:|---:|---:|
| 7 | 9 | 2520 |
| 8 | 18 | 10080 |
| 9 | 27 | 1120 |
| 10 | 45 | 10080 |
| 11 | 63 | 2520 |
| 12 | 84 | 210 |
| 13 | 120 | 1680 |
| 14 | 156 | 2520 |
| 15 | 195 | 336 |
| 16 | 240 | 21 |
| 17 | 312 | 105 |
| 18 | 384 | 210 |
| 19 | 459 | 210 |
| 20 | 540 | 21 |
| 21 | 630 | 1 |

The count \(N_u\) means **distinct unordered subsets** of the 21 projective points in a fixed labelled \(\operatorname{PG}(2,4)\); it is not a count of monomially inequivalent codes. In particular, at \(u=10\) and \(u=11\), integral projective-line occupancy constraints would allow respectively \(A_6=42\) and \(A_6=60\), but projective geometry excludes both values. The sharp minima are 45 and 63.

## Assumptions and scope

Use \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\). Choose \(u\) vectors \(g_i\in\mathbb F_4^3\) representing **different one-dimensional subspaces**; equivalently choose a subset \(S\) of cardinality \(u\) in \(\operatorname{PG}(2,4)\). Define \(C(S)\subseteq\mathbb F_4^{2u}\) by parity checks
\[
 x_{2i-1}+x_{2i}=0\quad(1\le i\le u),\qquad
 \sum_{i=1}^{u}g_i x_{2i}=0.
\]
Every such code has parameters \([2u,u-3,6]_4\) and disjoint repair pairs. Indeed, the global matrix has rank three because no projective line has more than five points, and a projective six-cap is the largest possible in order four; thus at least one dependent triple exists for \(u\ge7\). No two selected global columns are proportional. The scope excludes arbitrary locality-one codes with a different global-check structure, repeated projective columns, and \(u\le6\).

## Proof

**Reduction to collinear triples.** The pair equations force \(x_{2i-1}=x_{2i}=a_i\), so \(C(S)\) is the two-fold repetition of the kernel of the \(3\times u\) column matrix \((g_i)\). The Hamming weight doubles. A kernel word of weight three has support on precisely three collinear projective points, and conversely each distinct collinear triple has exactly \(4-1=3\) nonzero scalar multiples of a relation, with all three coefficients nonzero. Therefore
\[
 A_6(C(S))=3T(S),\qquad
 T(S)=\sum_{L\in\operatorname{PG}(2,4)\text{ lines}}\binom{|L\cap S|}{3}.
\]
Here each of the 21 lines has exactly five points and every two distinct points lie on precisely one line. Three elementary incidence identities for \(n_j=|\{L:|L\cap S|=j\}|\), \(0\le j\le5\), give
\[
 \sum_{j=0}^5 n_j=21,\qquad
 \sum_{j=0}^5 j n_j=5u,\qquad
 \sum_{j=0}^5\binom j2 n_j=\binom u2,
\]
while \(T(S)=n_3+4n_4+10n_5\). Solving this tiny nonnegative integer relaxation yields the table's stated minima for every \(u\) except \(u=10,11\), at which it yields respectively 14 and 20 collinear triples. In each exceptional case the unique integer-minimum occupancy vector \((n_0,\ldots,n_5)\) is respectively \((2,2,3,14,0,0)\) and \((2,1,1,16,1,0)\).

**Obstructions at the two exceptional sizes.** In either occupancy vector, two lines avoid \(S\). They meet at an unselected point \(p\). The other three lines through \(p\) partition \(S\), with each carrying at most four selected points. Ten selected points therefore force at least one four-secant, contradicting \(n_4=0\) in the first vector. Eleven selected points force at least two four-secants, contradicting \(n_4=1\) in the second. Hence the sharp lower bounds are 15 and 21 triples, respectively. These bounds, and all the remaining incidence-relaxation minima, are attained by explicitly enumerable subsets.

**Complete realization and counts.** The included standard-library program `verify.py` constructs all 21 normalized projective points and lines using \(t^2=t+1\); it examines **each of the \(2^{21}\) subsets**, not a statistical sample, using an exact integer dynamic program. The recurrence for a nonempty subset \(M\) removes its least-indexed point \(p\) to obtain \(R\), and computes
\[
 T(M)=T(R)+\sum_{L\ni p}\binom{|R\cap L|}{2}.
\]
Every new collinear triple contains \(p\) and a unique pair from one of its five incident lines, proving the recurrence. Recording the minimum and how many subsets attain it at every cardinality gives precisely the displayed \(N_u\) values and attains every lower bound. The program independently checks each representative by the direct 21-line sum, verifies the incidence identities, and enumerates all kernel words for \(u\in\{7,8,10,11\}\) to compare their weight-three counts with \(3T(S)\). The mathematical reduction and exact exhaustive recurrence together give a complete finite proof of the table, not an extrapolation from bounded numerical experiments.

## Verification

Run `python3 verify.py` with Python 3.9 or later. It requires only the Python standard library and no external files. The last line must be `VERIFY_OK`, preceded by the complete optimum, multiplicity and representative-index table. Projective point indices are the zero-based positions of the lexicographically sorted normalized nonzero triples over \(\mathbb F_4\), under the encoding \(0,1,t,1+t\) as integers \(0,1,2,3\). The checker first verifies the exact incidence parameters, then all cardinality profiles, then independent direct and kernel-code checks.

## Relationship to prior work

The parity-check construction and its parameters belong to J. Li, Q. Fu, and R. Yang, *Construction of Cadambe-Mazumdar Optimal and Almost Optimal Quaternary Locally Repairable Codes with Distance 6*, first publicly available 2026-09-08, DOI:10.1587/transfun.2026EAP1076, especially Theorem 1 and Equation (12). Their result does not report this optimal weight-six multiplicity table. The rank-three projective interpretation is classical: the 21-point plane, its lines and the 168 hyperovals are standard facts, recorded by H. Cuypers and in P. J. Cameron's finite-plane exposition. In particular, the \(u=7\) optimum and its count can also be understood from adding one external point to a hyperoval; the claimed new scope is the **complete extremal distribution across all fifteen sizes**, including the \(u=10,11\) geometric obstructions. A separate published eight-point/eight-line incidence optimization in the same plane studies a different extremal functional and does not give the present weight-six table.

## Limitations

The enumeration optimizes only the number of minimum-weight codewords within the specified rank-three paired-repair construction. It does not optimize an arbitrary quaternary LRC, other Hamming weights, decoding algorithms, or general field orders. Projectively different minimizing point subsets may produce equivalent codes, and no equivalence-class count is asserted. The exhaustive program is a finite certificate with an explicitly proved complete search space and recurrence, not a claim of independent formal certification. An older finite-geometry configuration catalogue could conceivably state equivalent subset counts; the searched sources did not establish such coverage.

## References

1. J. Li, Q. Fu, and R. Yang, *Construction of Cadambe-Mazumdar Optimal and Almost Optimal Quaternary Locally Repairable Codes with Distance 6*, IEICE Transactions on Fundamentals, advance publication 2026-09-08, DOI:10.1587/transfun.2026EAP1076. https://www.jstage.jst.go.jp/article/transfun/advpub/0/advpub_2026EAP1076/_pdf/-char/en
2. H. Cuypers, *The projective plane of order 4*, 1996. https://hansc.win.tue.nl/mathieu/node2.html
3. P. J. Cameron, *Projective and affine planes*, Encyclopedia of Design Theory, 2002, §§1 and 5. https://webspace.maths.qmul.ac.uk/p.j.cameron/design/encyc/topics/pap.pdf
4. *Sharp 8-by-8 point-line incidence ceiling in PG(2,4): 24 incidences with extremal types*, public result, 2026-09-07. https://github.com/published-finding corpus/2026/tree/main/2026/9/7/SCOPE025
