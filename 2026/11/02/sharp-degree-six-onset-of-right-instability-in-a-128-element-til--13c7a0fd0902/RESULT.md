# Sharp degree-six onset of right instability in a 128-element tiled matrix ring

## Finding

Let \(S\) be the characteristic-four ring of order \(128\)
\[
S=\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}:a,b,c,d\in\mathbb Z/4\mathbb Z,\ b\in\{0,2\}\right\}.
\]
For a polynomial \(F(X)=\sum_{i=0}^{n}C_iX^i\in S[X]\) with a central indeterminate, use **right evaluation** \(F(r)=\sum_i C_ir^i\), and let \(\mathcal N(S)\) denote the polynomials vanishing at every \(r\in S\).

**Theorem.** (1) Every \(F\in\mathcal N(S)\) with \(\deg F\le5\) has all four entries of every coefficient matrix \(C_i\) even modulo four. (2) Every null polynomial with this entrywise-even coefficient property, in any degree, remains null after right multiplication by every element of \(S[X]\). (3) There is a degree-six null polynomial whose right multiple by the idempotent \(E_{11}\) is not null. Therefore
\[
\min\{\deg F:F\in\mathcal N(S),\;Fh\notin\mathcal N(S)\text{ for some }h\in S[X]\}=6.
\]
The conclusion concerns the degree of an instability witness for this particular ring; it is not a universal bound for all finite rings.

## Assumptions and scope

All computations are in \(\mathbb Z/4\mathbb Z\) unless specified. The matrices \(E_{ij}\) are the usual matrix units. The indeterminate commutes with all coefficients, although substitution is not multiplicative for noncommuting coefficients. "Entrywise even" means that each matrix entry is in \(\{0,2\}\); it does **not** assert that a coefficient belongs to the ideal \(2S\), since its upper-right entry may equal two. The zero polynomial is included in the degree bound by convention.

## Proof

**1. An exact low-degree linear certificate.** Write a polynomial of degree at most five using coefficient matrices
\[
C_i=\begin{pmatrix}a_i&b_i\\c_i&d_i\end{pmatrix}\quad(0\le i\le5).
\]
Arrange the \(24\) entries as
\[
\mathbf t=(a_0,b_0,c_0,d_0,a_1,b_1,c_1,d_1,\ldots,a_5,b_5,c_5,d_5)^T.
\]
For each \(r\in S\) and matrix-entry position \(v\in\{11,12,21,22\}\), let \(L_{r,v}\) be the integer row obtained by taking least nonnegative residues of all coefficients in the linear form \((\sum_{i=0}^{5}C_ir^i)_v\). In other words, its column \((i,j)\) is the specified entry of \(E_jr^i\), reduced to \(\{0,1,2,3\}\), with \(j\) ranging in the order \(11,12,21,22\). An arbitrary coefficient at position \(12\) is temporarily permitted in constructing these linear forms; the necessary ring restrictions are then imposed explicitly.

Form an integer \(24\)-by-\(24\) matrix \(M\) with the following rows in the stated order:

- All four \(L_{r,v}\) for each of \(r=(0,0,0,0),(1,0,0,1),(0,2,1,0),(1,2,1,1)\), where a tuple lists entries in order \(11,12,21,22\).
- The two rows \(L_{r,11},L_{r,21}\) for \(r=(0,0,1,0)\) and \(r=(1,0,1,1)\).
- The rows \(L_{r,21}\) for \(r=(0,0,1,2)\) and \(r=(1,0,1,3)\).
- Two coordinate rows containing two in precisely the coordinates \(b_2\) and \(b_3\), respectively, and zero elsewhere.

These are \(16+4+2+2=24\) rows. Exact integer Bareiss elimination gives
\[
\det M=4096=2^{12},\qquad\operatorname{rank}_{\mathbb F_2}(M\bmod2)=12.
\]
The independent executable `check.py` constructs all rows directly from matrix multiplication and verifies both equalities. Every degree-at-most-five null polynomial satisfies \(M\mathbf t\equiv0\pmod4\): the first \(22\) rows are evaluations and the final two encode necessary conditions \(b_2,b_3\in\{0,2\}\).

For completeness, take a Smith normal form of the integer matrix \(M\). Its determinant and mod-two rank show that precisely twelve invariant factors are odd and the other twelve have two-adic valuation exactly one. The integral changes of basis are invertible modulo four. If \(M\mathbf t\equiv0\pmod4\), the transformed coordinates corresponding to odd invariant factors vanish modulo four, and the remaining coordinates are even. Therefore every coordinate of \(\mathbf t\) is even, proving part (1) without enumerating null polynomials or assuming any degree above five.

**2. Stability of entrywise-even null polynomials.** If all coefficients of \(F\) are entrywise even, write \(F=2G\) with coefficients of \(G\) arbitrary in \(M_2(\mathbb Z/4\mathbb Z)\); no assertion that \(G\in S[X]\) is needed. Reduce \(G\) and the input matrices modulo two. The image of \(S\) is the lower-triangular ring
\[
B=\left\{\begin{pmatrix}a&0\\c&d\end{pmatrix}:a,c,d\in\mathbb F_2\right\}.
\]
The condition \(F(r)=0\) for all \(r\in S\) is equivalent to \(\bar G(t)=0\) for all \(t\in B\), since \(2G(r)=0\) modulo four exactly when \(\bar G(\bar r)=0\) modulo two.

Write the four entries of the coefficient polynomial \(\bar G\) as scalar polynomials \(u,v,w,z\in\mathbb F_2[X]\), and put
\[
H_i(a,d)=\sum_{j=0}^{i-1}a^{i-1-j}d^j,\quad H_0(a,d)=0.
\]
For \(t=\bigl(\begin{smallmatrix}a&0\\c&d\end{smallmatrix}\bigr)\), the lower-left entry of \(t^i\) is \(cH_i(a,d)\). Varying \(a,c,d\) over \(\mathbb F_2\), the condition \(\bar G(t)=0\) is equivalent to
\[
\begin{gathered}
u(a)=w(a)=0,\quad v(d)=z(d)=0\qquad(a,d\in\mathbb F_2),\\
\sum_i v_i H_i(a,d)=\sum_i z_i H_i(a,d)=0\qquad(a,d\in\mathbb F_2),
\end{gathered}
\]
where \(v_i,z_i\) denote scalar coefficients. (The first line also gives \(v(a)=z(a)=0\) because the same two-element field is used for both variables.)

Right multiplying every coefficient matrix by \(h=\bigl(\begin{smallmatrix}\alpha&0\\\gamma&\delta\end{smallmatrix}\bigr)\in B\) replaces
\[
(u,v,w,z)\longmapsto(\alpha u+\gamma v,\delta v,\alpha w+\gamma z,\delta z).
\]
All four point-vanishing and both divided-difference conditions remain valid. Thus \(\bar G h\) is null on \(B\), so \(Fh\) is null on \(S\) for each constant \(h\in S\). Multiplication by a power of the central indeterminate also preserves nullity, because \((FX^j)(r)=F(r)r^j\). Linearity gives right stability under every polynomial in \(S[X]\), proving part (2).

**3. The sharp witness.** Define
\[
F(X)=E_{21}(X^2-X^4)+E_{22}(X^3-X^4-X^5+X^6).
\]
All its coefficients lie in \(S\), and its leading coefficient \(E_{22}\) is nonzero, so its degree is six. The finite ring has exactly \(4\cdot2\cdot4\cdot4=128\) elements. For each of them, exact modular multiplication of the displayed polynomial gives zero. The complete \(128\)-input check, not a random sample, is independently reproducible by `python3 check.py`; the program implements matrix multiplication and the polynomial evaluation directly and verifies each input separately.

Now take \(e=E_{11}\) and \(r=\bigl(\begin{smallmatrix}0&2\\1&0\end{smallmatrix}\bigr)\in S\). One has \(r^2=2I\) and \(r^4=0\), while \(E_{21}e=E_{21}\) and \(E_{22}e=0\). Consequently
\[
(Fe)(r)=E_{21}(r^2-r^4)=2E_{21}\ne0.
\]
Together with parts (1) and (2), this proves that six is the first possible degree of a right-instability witness. \(\square\)

## Verification

The supplied standalone, standard-library-only `check.py` constructs the necessary \(24\)-row integer certificate, computes its determinant by exact Bareiss elimination and its mod-two rank by exact elimination, verifies closure and cardinality of the ring, and exhaustively evaluates the degree-six witness at all \(128\) ring elements. It also verifies the nonzero right-multiple value. Running `python3 check.py` produces the accompanying `check_output.txt` ending `VERIFY_OK`. Exact arithmetic is used throughout; these finite checks verify the stated finite certificate and finite input enumeration, while the Smith-form and triangular-reduction arguments supply the universal low-degree reasoning.

## Relationship to prior work

Wu [1, Proposition 5.2] introduces this same characteristic-four ring of order \(128\) and proves non-two-sidedness of its null polynomial set, including a degree-six witness. Thus the **existence of a sextic witness and the ring construction are prior results**, not claimed here. The new contribution is the sharp **lower** degree cutoff and its stronger coefficient-parity obstruction, together with right stability of all entrywise-even null polynomials. Wu's examined full text does not state such a minimum-degree classification. Havlovec [2] gives a distinct characteristic-two, order-\(128\) counterexample, and Werner [3] proves broader nilpotent-radical sufficient conditions; neither source supplies the present degree-five certificate for the specific characteristic-four ring. Literature and mathematical-record searches did not uncover explicit equivalent coverage, but absence from searches does not certify absolute historical priority.

## Limitations

The result concerns right evaluation and right multiplication on this particular characteristic-four tiled matrix ring; it does not establish a lower bound for all counterexample rings. The explicit upper-bound witness overlaps in conclusion with Wu's prior example. The low-degree obstruction is certified by a finite integer determinant, not by a conceptual classification of all null polynomials. The finite exhaustive witness check is specific to the \(128\) elements of \(S\).

## References

[1] H. Wu, *Peirce Stability of Null Polynomials and a Sharp Radical Bound for Finite Rings*, arXiv:2609.01150 (first public September 1, 2026), especially Section 5, Proposition 5.2. https://arxiv.org/abs/2609.01150

[2] V. Havlovec, *Null polynomials over a finite ring need not form a two-sided ideal*, arXiv:2608.13251 (August 13, 2026), Theorem 2.1. https://arxiv.org/abs/2608.13251

[3] N. J. Werner, *Some results on null ideals of finite rings*, arXiv:2608.25853 (August 26, 2026), Theorem 1.2. https://arxiv.org/abs/2608.25853

[4] N. J. Werner, *Polynomials that kill each element of a finite ring*, J. Algebra Appl. 13 (2014), article 1350111, for the earlier null-ideal framework.
