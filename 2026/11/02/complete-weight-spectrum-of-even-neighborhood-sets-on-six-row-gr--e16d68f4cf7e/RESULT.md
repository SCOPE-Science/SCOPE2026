# Complete weight spectrum of even-neighborhood sets on six-row grids

## Finding
For the rectangular grid \(G_n=P_6\square P_n\), let \(\mathcal K_n\) be the family of vertex subsets \(S\) such that every closed neighborhood meets \(S\) in an even number of vertices. Include the empty set. For every integer \(n\ge1\), define the weight polynomial
\[
W_n(z)=\sum_{S\in\mathcal K_n}z^{|S|}.
\]
Then
\[
\boxed{W_n(z)=\begin{cases}
1,&9\nmid(n+1),\\[2pt]
1+4z^{18q}+12z^{20q}+12z^{22q}+3z^{24q}
+12z^{26q}+15z^{28q}+4z^{30q}+z^{36q},
&n+1=9q,\ q\in\mathbb Z_{\ge1}.
\end{cases}}
\]
Thus a nonempty even-neighborhood set exists precisely when \(n\equiv8\pmod9\). At such lengths there are exactly \(63\) nonempty sets, exactly four of minimum size \(18q\), and exactly one of maximum size \(36q\). As a binary linear code, the closed-neighborhood kernel has parameters \([6(9q-1),6,18q]\) when \(n=9q-1\); otherwise its dimension is zero.

## Assumptions and scope
The graphs are finite, simple, Cartesian products of paths with open ends in both directions. The closed neighborhood \(N[v]\) contains \(v\) itself and every horizontally or vertically adjacent vertex. All parity and matrix computations use \(\mathbb F_2\). Sets are counted with the grid's coordinates labelled, not modulo rotations or reflections. This is the usual zero-effect or *quiet-pattern* kernel of the standard Lights Out move matrix, not a count of arbitrary solutions of an inhomogeneous Lights Out board.

## Proof
**Column recurrence.** Number the columns from \(1\) to \(n\), with six entries in each. Represent the chosen cells in column \(j\) by \(c_j\in\mathbb F_2^6\). Let \(B=I_6+A(P_6)\), the tridiagonal matrix with ones on the diagonal and two adjacent diagonals. Set virtual boundary columns \(c_0=c_{n+1}=0\). The parity equation at column \(j\) is exactly
\[
c_{j-1}+Bc_j+c_{j+1}=0.
\]
Consequently a quiet pattern is uniquely determined by its first column \(w=c_1\). Let \(f_0(x)=0\), \(f_1(x)=1\), and \(f_{r+1}(x)=xf_r(x)+f_{r-1}(x)\). Then \(c_j=f_j(B)w\), and the remaining right boundary condition is \(f_{n+1}(B)w=0\).

**Nine-column vanishing.** Over \(\mathbb F_2\), the characteristic polynomial of \(B\) is
\[
\chi_B(x)=x^6+x^2+1=(x^3+x+1)^2.
\]
This follows either by expanding the tridiagonal determinant or by substituting \(x+1\) into the characteristic polynomial of \(A(P_6)\). Direct recurrence gives
\[
f_1=1,\ f_2=x,\ f_3=x^2+1,\ f_4=x^3,\ f_5=x^4+x^2+1,\
f_6=x^5+x,\ f_7=x^6+x^4+1,\ f_8=x^7,\
f_9=x^8+x^6+x^4+1=(x^2+1)\chi_B(x).
\]
Cayley–Hamilton therefore yields \(f_9(B)=0\). The polynomial \(g(x)=x^3+x+1\) is irreducible over \(\mathbb F_2\). The remainders of \(f_r\) modulo \(g\), for \(1\le r\le8\), are respectively
\[
1,\ x,\ x^2+1,\ x+1,\ x+1,\ x^2+1,\ x,\ 1.
\]
Each is nonzero, so \(\gcd(f_r,\chi_B)=1\) and every \(f_r(B)\) is invertible. In particular \(f_8(B)=B^7\) is invertible.

Define the block recurrence matrix \(T=\left(\begin{smallmatrix}B&I_6\\I_6&0\end{smallmatrix}\right)\). Induction on its powers gives
\[
T^r=\begin{pmatrix}f_{r+1}(B)&f_r(B)\\f_r(B)&f_{r-1}(B)\end{pmatrix}
\quad(r\ge1).
\]
Since \(f_9(B)=0\), this implies \(T^9=\operatorname{diag}(B^7,B^7)\), whence
\[
f_{9q+r}(B)=B^{7q}f_r(B)\qquad(q\ge0,\ 0\le r<9).
\]
Thus \(\ker f_{n+1}(B)\) is all of \(\mathbb F_2^6\) if \(9\mid(n+1)\) and is zero otherwise. This proves the count of allowable first columns, including the boundary cases \(1\le n<8\).

**Weights at lengths \(n=9q-1\).** For any first column \(w\), the first eight columns satisfy \(c_9=0\). The recurrence then forces \(c_{9+r}=c_{9-r}\) for \(0\le r\le8\), with \(c_{18}=0\), and this reflected sequence continues across each later zero column. Hence a valid \((9q-1)\)-column pattern consists of exactly \(q\) copies of the multiset of the first eight nonzero-or-zero columns, possibly reversed, separated by \(q-1\) all-zero columns. Its Hamming weight is therefore \(q\) times the eight-column weight determined by \(w\).

It remains to count exactly the \(64\) choices \(w\in\mathbb F_2^6\) for the eight-column block. Writing \(w\) as a six-bit integer in two-digit hexadecimal notation (row 1 is the least significant bit), the recurrence is explicitly
\[
(a,b)\longmapsto\bigl(b,\ b\oplus((b\ll1)\mathbin{\&}63)\oplus(b\gg1)\oplus a\bigr),
\]
where \(\oplus\) means bitwise addition modulo two. The following exhaustive, disjoint table gives the complete list of first columns at each eight-column Hamming weight; it provides a finite certificate without sampling.

| Eight-column weight | Number | First column \(w\) (hexadecimal) |
|:--:|--:|---|
| 0 | 1 | `00` |
| 18 | 4 | `01 0D 20 2C` |
| 20 | 12 | `03 04 07 08 11 15 22 2A 30 37 38 3B` |
| 22 | 12 | `02 05 0A 0E 10 14 1B 1C 28 2B 35 36` |
| 24 | 3 | `0C 21 2D` |
| 26 | 12 | `06 09 17 18 23 24 27 2F 31 39 3A 3D` |
| 28 | 15 | `0B 0F 12 16 19 1A 1D 25 26 29 2E 33 34 3C 3F` |
| 30 | 4 | `13 1F 32 3E` |
| 36 | 1 | `1E` |

The table partitions all \(64\) possible first columns, and each row follows from the displayed four-neighbor recurrence using eight steps. Multiplying every nonzero weight by \(q\) gives the asserted polynomial for every admissible length. The dimension, distance, and multiplicity statements follow immediately. \(\square\)

## Verification
The accompanying standalone `verify.py` checks the claimed eight-column table from all \(64\) initial columns; reconstructs the closed-neighborhood parity matrix directly and computes its kernel by independent binary Gaussian elimination for every length \(1\le n\le54\); and independently generates all possible initial columns by recurrence, checking their full parity constraints and spectra for every \(1\le n\le144\). It returns `VERIFY_OK`. These finite tests corroborate the proof; the infinite statement rests on the recurrence and the exact 64-case table, not extrapolation.

## Relationship to prior work
Goldwasser and Klostermeyer's *Nullspace-Primes and Fibonacci Polynomials* (2002) provides the Fibonacci recurrence and nullspace-dimension framework, explicitly noting the existence of a \(6\times8\) nullspace matrix. Klostermeyer's *Prime Nullspace Matrices and Even Dominating Sets* (first public October 22, 2026) studies existence, primality, and zero rows and columns. Neither inspected source gives the cardinality-resolved eight-level spectrum for the six-row family. Scherphuis's *Lights Out Mathematics* tabulates quiet-pattern dimensions for rectangular grids, not their Hamming distribution. Francis's *Algebra in the Game Lights Out* (May 19, 2026), Lemma 30 and Proposition 31, obtains a different 4-by-4 kernel spectrum and folds it into square boards; the result above concerns the width-six primitive and uses a distinct 64-case base census. Goldwasser and Klostermeyer's 2009 work on maximum orbit weights measures minimum configurations *within game orbits*, not the Hamming distribution of zero-effect click patterns.

The new coefficients are mathematically relevant beyond existence: \(18q\) is the minimum size of a nonempty silent button-press set, and the full spectrum gives exact probabilities for randomly chosen press sets with independent biased bits by substituting into \(\sum_w A_w p^w(1-p)^{6n-w}\). Dimension alone cannot supply these minimum or probability data.

## Limitations
The formula is specific to rectangular grids with exactly six rows and standard closed-neighborhood parity, with no wraparound. It does not determine the spectra of arbitrary rectangular grids, nonzero right-hand-side parity systems, or distributions modulo grid symmetries. The literature comparison is based on the identified primary results and available full-text sections; the possibility of an earlier equivalent weight table under different terminology is not completely excluded. This work has not received an independent mathematical audit.

## References
1. W. F. Klostermeyer, *Prime Nullspace Matrices and Even Dominating Sets*, arXiv:2610.31475v1, October 22, 2026. https://arxiv.org/html/2610.31475v1
2. W. F. Klostermeyer and J. L. Goldwasser, *Nullspace-Primes and Fibonacci Polynomials*, Fibonacci Quarterly **40** (2002), 323–327. https://www.fq.math.ca/Scanned/40-4/klostermeyer.pdf
3. J. L. Goldwasser, W. F. Klostermeyer, and H. Ware, *Fibonacci Polynomials and Parity Domination in Grid Graphs*, Graphs and Combinatorics **18** (2002), 271–283.
4. P. Francis, *Algebra in the Game Lights Out*, May 19, 2026. https://peterefrancis.com/lights-out-algebra/paper.pdf
5. J. Scherphuis, *Lights Out Mathematics*. https://www.jaapsch.net/puzzles/lomath.htm
6. J. L. Goldwasser and W. F. Klostermeyer, *Maximum Orbit Weights in the \(\sigma\)-Game and Lit-Only \(\sigma\)-Game on Grids and Graphs*, Graphs and Combinatorics **25** (2009), 309–326.
