# Uniform twisted-commutator rank spectrum in the \(5\times5\) nilradical

## Finding
Let \(\mathfrak n_5(\mathbb F_q)\) be the ten-dimensional algebra of strictly upper-triangular \(5\times5\) matrices. For every prime power \(q\), every \(\lambda\in\mathbb F_q^{\times}\), and every \(X\in\mathfrak n_5(\mathbb F_q)\), define the linear map \(L_{X,\lambda}(Y)=XY-\lambda YX\) on \(\mathfrak n_5(\mathbb F_q)\). The number \(R_r(q)\) of matrices \(X\) for which this map has rank \(r\) is **independent of \(\lambda\)** and equals

\[
\begin{aligned}
R_0&=q,\\
R_1&=q(q-1)(q+1),\\
R_2&=3q^3(q-1),\\
R_3&=q^3(q-1)(3q^2+3q-2),\\
R_4&=q^4(q-1)^2(q+2)(2q+1),\\
R_5&=q^5(q-1)^2(2q^2+2q-1),\\
R_6&=q^6(q-1)^3(q+1).
\end{aligned}
\]

There are no other ranks. In particular, the full fixed-flag quantum-plane point count is

\[
\big|\{(X,Y)\in\mathfrak n_5(\mathbb F_q)^2:XY=\lambda YX\}\big|
=\sum_{r=0}^6 R_r(q)q^{10-r}
=q^{10}(5q^4-5q^2+1).
\]

## Assumptions and scope
The field may have any characteristic, including two; no assumption on the multiplicative order of the nonzero parameter \(\lambda\) is needed. The matrices \(X\) and \(Y\) preserve the **specified standard complete flag** and induce zero on its graded one-dimensional factors, so both lie in the particular nilradical \(\mathfrak n_5\). This is not a formula for all nilpotent matrices up to change of basis, for all pairs of upper-triangular matrices with arbitrary diagonal, or for arbitrary matrix dimension.

Write the coordinates of \(X\) in increasing superdiagonal order as
\(A=X_{12},B=X_{23},C=X_{34},D=X_{45},E=X_{13},F=X_{24},G=X_{35},H=X_{14},I=X_{25},J=X_{15}\).
Use the coordinates of \(Y\), in order, \((y_{12},y_{23},y_{34},y_{45},y_{13},y_{24},y_{35},y_{14},y_{25},y_{15})\).

## Proof
The only possibly nonzero outputs of \(XY-\lambda YX\) are its six entries on the second and higher superdiagonals. Their coefficient matrix, after omitting the zero column of \(y_{15}\), is

\[
M=\begin{pmatrix}
-\lambda B&A&0&0&0&0&0&0&0\\
0&-\lambda C&B&0&0&0&0&0&0\\
0&0&-\lambda D&C&0&0&0&0&0\\
-\lambda F&0&E&0&-\lambda C&A&0&0&0\\
0&-\lambda G&0&F&0&-\lambda D&B&0&0\\
-\lambda I&0&0&H&-\lambda G&0&E&-\lambda D&A
\end{pmatrix}.
\]

Conjugation by an invertible diagonal matrix preserves \(\operatorname{rank}M\). Its four successive diagonal ratios may be prescribed independently, so every nonzero entry among \((A,B,C,D)\) can be normalized to one. For a fixed support mask \(s\in\{0,\ldots,15\}\), its binary digits indicate which of \((A,B,C,D)\) are nonzero. Each normalized support represents exactly \((q-1)^{\operatorname{popcount}(s)}\) choices of first-superdiagonal entries. The five coordinates \((E,F,G,H,I)\) remain unrestricted, and \(J\) is a free central coordinate.

Let \(n_r(s)\) denote the number of five-tuples \((E,F,G,H,I)\) producing rank \(r\) with the four first-superdiagonal entries normalized according to mask \(s\). Direct row reduction of the displayed matrix gives the complete **support-stratified certificate**:

| Masks \(s\) | Nonzero \(n_r(s)\) |
|---|---|
| \(0\) | \(n_0=1,\ n_1=q^2-1,\ n_2=3q^2(q-1),\ n_3=q^2(q-1)^2(q+2)\) |
| \(1,8\) | \(n_3=q^4,\ n_4=q^4(q-1)\) |
| \(2,4\) | \(n_3=q^3,\ n_4=q^3(q^2-1)\) |
| \(5,10\) | \(n_4=q^5\) |
| \(9\) | \(n_4=q^4,\ n_5=q^4(q-1)\) |
| \(3,6,11,12,13\) | \(n_5=q^5\) |
| \(7,14,15\) | \(n_6=q^5\) |

Here is a row-reduction derivation that applies over every field. For mask zero, the first three rows vanish. The fourth and fifth rows are independent when \(F\ne0\), while with \(F=0\) they are supported respectively when \(E\ne0\) and \(G\ne0\). If \((E,G)\ne(0,0)\), the sixth row has a new coordinate in \(y_{13}\) or \(y_{35}\), so it increases rank by one. If \(E=G=0\) and \(F\ne0\), the fourth and fifth rows already span the sixth; if \(E=F=G=0\), only the sixth row survives, precisely when \((H,I)\ne(0,0)\). These alternatives yield the mask-zero line.

For masks \(1\) and \(8\), three rows have independent pivots and the remaining row increases rank exactly when \(F\ne0\). For mask \(2\), the three basic pivots occur in rows \(13,24,25\); the row \(15\) is dependent exactly when \(G=0\) and \(BH=FE\). With normalized \(B=1\), this leaves three free parameters. For mask \(4\), the symmetric dependency condition is \(E=0\) and \(CI=FG\); with normalized \(C=1\) this likewise leaves three free parameters. For mask \(9\), four pivots are always present, and the fifth occurs exactly when \(F\ne0\).

For masks \(5,10\), the nonzero rows have four independent pivots, while the remaining rows lie in their span. For masks \(3,6,11,12,13\), five independent pivots occur in the five nonvanishing or nonredundant rows; the last row lies in their span if applicable. Finally, for masks \(7,14,15\), the three second-superdiagonal output rows have three independent pivots; the next two rows have independent projections to the \((y_{13},y_{24},y_{35})\)-coordinates; the last row has a nonzero projection to \((y_{14},y_{25})\). Thus all six rows are independent. All these pivots use only nonzero factors among the normalized first-superdiagonal entries and \(\lambda\), so no special characteristic or value of \(\lambda\) arises. The seven lines exhaust all sixteen masks and every line sums to \(q^5\).

Summing the table gives
\[
R_r(q)=q\sum_{s=0}^{15}(q-1)^{\operatorname{popcount}(s)}n_r(s),
\]
where the leading factor \(q\) counts \(J\). Expanding yields the seven displayed rank polynomials, whose sum is \(q^{10}\). Since \(\ker L_{X,\lambda}\) has size \(q^{10-r}\), summing its fibers proves the pair count.

## Verification
The included standalone `verify.py` constructs the six-by-nine matrix directly, computes its rank using exact finite-field arithmetic, enumerates all five free coordinates for every normalized support, and compares **each support's entire rank histogram** with the table and the resulting global and pair-count formulas. Complete tests were executed for \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\) and for every nonzero \(\lambda\) in each field, including the nonprime field \(\mathbb F_4\). The checker returned `TWISTED_FLAG_RANKS_OK`. The proof is the symbolic field-independent row reduction above; finite tests are cross-checks, not a substitute for it.

## Relationship to prior work
Goodwin and Röhrle (2012, §3.4) identified five irreducible components of the **untwisted** commuting variety of this type-\(A_4\) nilradical over an algebraically closed field of characteristic zero. Their result motivates the leading coefficient five, but the component decomposition alone neither implies the seven exact finite-field rank multiplicities nor the full point-count polynomial, and it does not address \(XY=\lambda YX\) for arbitrary \(\lambda\ne0\).

Britnell and Wildon (2010) study commuting similarity classes of unrestricted matrices. Chen and Lu (2019) describe geometric components of unrestricted quantum-plane representation varieties; Huang (2021) counts unrestricted twisted-commuting matrices and the larger locus where only the first matrix is nilpotent. None of those exact theorems prescribes one complete flag simultaneously for both nilpotent matrices. Their unrestricted counts cannot be specialized to the displayed fixed-flag count without additional incidence information.

## Limitations
No assertion is made about irreducibility or scheme-theoretic multiplicities of the twisted varieties. The theorem counts points and ranks for the specified nilradical only; it does not prove a corresponding independence theorem in higher matrix dimensions. The literature comparison is bounded, and the 2005 Kobal canonical-form paper was not inspected in full. The originality assessment is therefore subject to that named residual risk; no claim of absolute priority or external certification is made.

## References
1. S. M. Goodwin and G. Röhrle, *On commuting varieties of nilradicals of Borel subalgebras of reductive Lie algebras*, arXiv:1209.1289 (first public posting 2012-09-06), especially §3.4.
2. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811 (2010-01-06).
3. X. Chen and M. Lu, *Varieties of modules over the quantum plane*, arXiv:1910.02198 (2019-10-05).
4. Y. Huang, *Counting on the variety of modules over the quantum plane*, arXiv:2110.15570 (2021-10-29).
5. D. Kobal, *Belitskiĭ's canonical form for 5 × 5 upper triangular matrices under upper triangular similarity*, Linear Algebra Appl. 403 (2005), 178–182, doi:10.1016/j.laa.2005.01.028 (bibliographic comparison only).
