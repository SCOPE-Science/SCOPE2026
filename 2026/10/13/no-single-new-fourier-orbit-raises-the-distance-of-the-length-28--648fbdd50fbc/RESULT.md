# No single new Fourier orbit raises the distance of the length-289 16-ary abelian code

## Finding
For the length-\(289\) abelian code over \(\mathbb F_{16}\) whose defining Fourier-zero set is
\[
D_0=\{(0,0),(1,0),(-1,0),(0,1),(0,-1)\}\subset (\mathbb Z/17\mathbb Z)^2,
\]
adding **any one new** \(16\)-cyclotomic orbit \(\{(u,v),(-u,-v)\}\) leaves the minimum Hamming distance exactly \(4\). Thus every proper single-orbit subcode obtained in this way has parameters \([289,282,4]_{16}\); no such subcode attains distance \(5\).

## Assumptions and scope
Let \(K=\mathbb F_2[t]/(t^8+t^4+t^3+t^2+1)\), with \(\alpha=t\), and put \(F=\mathbb F_{16}\subset K\) and \(\epsilon=\alpha^{15}\), a primitive seventeenth root of unity. The length-\(289\) coordinate positions are \((i,j)\in (\mathbb Z/17\mathbb Z)^2\). A word \(c=(c_{ij})\in F^{289}\) lies in the code with defining set \(D\) exactly when
\[
\sum_{i,j=0}^{16}c_{ij}\epsilon^{ri+sj}=0\quad\text{for each }(r,s)\in D.
\]
The field \(K\) and the chosen primitive root supply a reproducible normalization only; the conclusion is independent of the choice of primitive root and of coordinate labeling. Since \(16\equiv-1\pmod{17}\), every nonzero exponent pair forms a two-element cyclotomic orbit, except that \((0,0)\) has a singleton orbit. The added orbit must be disjoint from \(D_0\). The claim concerns this *one-orbit, fixed-base-code* family, not arbitrary \(16\)-ary linear codes of these parameters or simultaneous multiple-orbit extensions.

## Proof
**Base distance and dimensions.** The characters indexed by the \(289\) exponent pairs form an invertible Fourier basis over \(K\); conjugate pairs represent two independent \(F\)-linear zero restrictions. Therefore \(D_0\) gives \(289-5=284\) dimensions, and each new disjoint two-element orbit gives \(289-7=282\). The five Fourier conditions are exactly the conditions on the three rows \(1,a,b\), plus their \(16\)-power conjugates, where \(a=\epsilon^i,b=\epsilon^j\) range over the norm-one group \(U=\{z\in K^\times:z^{17}=1\}\). Any purported nonzero word supported at most three positions gives \(\sum x_i=\sum x_i a_i=\sum x_i a_i^{-1}=\sum x_i b_i=\sum x_i b_i^{-1}=0\). If the three \(a_i\) are distinct, the \(3\)-by-\(3\) matrix with rows \(1,a,a^{-1}\) is invertible by the Vandermonde determinant. If exactly two distinct \(a_i\) occur, the unique-position coefficient vanishes by the first two equations, and the remaining two are killed by \(1,b\), since their \(b\) values differ. If all \(a_i\) are equal, the \(b_i\) are distinct and the symmetric Vandermonde argument works. Lower support sizes are included by zero padding. Consequently the base has distance at least \(4\). Any rectangle of four distinct positions \((i_1,j_1),(i_1,j_2),(i_2,j_1),(i_2,j_2)\), with all coefficients \(1\), gives a base word of weight \(4\). Thus every subcode under consideration has distance at least \(4\).

**Necessary exponent restrictions.** The rectangle Fourier equation for \((u,v)\) factors as \((\epsilon^{u i_1}+\epsilon^{u i_2})(\epsilon^{v j_1}+\epsilon^{v j_2})\); in particular, \(u=0\) or \(v=0\) cannot remove all rectangles. Hence a putative distance-\(5\) extension has \(1\le u,v\le16\). For any four distinct elements \(z_1,\ldots,z_4\in U\), define
\[
A_i=\prod_{j\ne i}(z_i-z_j),\qquad \eta_i=\frac{z_i}{A_i},\qquad E=\prod_{i=1}^{4}z_i.
\]
Lagrange interpolation for degree at most \(2\) gives \(\sum_i z_i^k/A_i=0\) for \(k=0,1,2\); in particular \(\sum\eta_i=\sum\eta_i z_i=\sum\eta_i z_i^{-1}=0\). Since \(z_i^{16}=z_i^{-1}\) and \(A_i^{16}=A_i/(z_i^2E)\), we have \(\eta_i^{16}=E\eta_i\). Choose \(c\in K^\times\) satisfying \(c^{15}=E^{-1}\), possible since the image of the fifteenth-power map is \(U\). Then all \(x_i=c\eta_i\) belong to \(F^\times\).

Use these four nonzero coefficients at grid positions with first and second root coordinates \((z_i,1)\), \((1,z_i)\), \((z_i,z_i)\), or \((z_i,z_i^{-1})\). Each pattern satisfies the base Fourier checks. Its new \((u,v)\) check vanishes respectively when
\[
H_w(Z):=\sum_{i=1}^{4}\frac{z_i^w}{A_i}=0
\quad\text{for }w=u+1,\ v+1,\ u+v+1,\ u-v+1\pmod{17}.
\]
Thus all four displayed exponents must lie in \(S=\{w\bmod17:H_w(Z)\ne0\text{ for every four-subset }Z\subset U\}\).

**Exhaustive exact finite reduction.** The supplied `verify.py` constructs \(K\) in the polynomial basis, checks the multiplicative order of \(\alpha\) is \(255\), and exhausts all \(\binom{17}{4}=2380\) four-subsets. For exponents \(w=0,1,\ldots,16\), the exact zero counts are
\[
(2380,2380,2380,0,0,68,34,0,34,0,0,34,0,34,68,0,0).
\]
Hence \(S=\{3,4,7,9,10,12,15,16\}\). Exhausting the \(256\) pairs with \(1\le u,v\le16\) and imposing the four necessary memberships leaves precisely
\[
\begin{split}
\{&(3,6),(3,11),(6,3),(6,8),(6,9),(6,14),(8,6),(8,11),\\
 &(9,6),(9,11),(11,3),(11,8),(11,9),(11,14),(14,6),(14,11)\}.
\end{split}
\]
Coordinate-wise inversion and exchange of the two coordinate axes preserve \(D_0\) and carry the new orbit accordingly. The sixteen pairs form exactly two orbits of size \(8\), represented by \((3,6)\) and \((6,8)\).

**Two explicit obstruction words.** Let \(\zeta=\alpha^{17}\in F\), and write a support point as its grid exponents \((i,j)\). For \((u,v)=(3,6)\), take the four support positions \((1,5),(16,12),(7,9),(10,8)\) with coefficients \((1+\zeta^2,1+\zeta^2,\zeta^3,\zeta^3)\). For \((u,v)=(6,8)\), take positions \((2,4),(7,13),(3,16),(6,1)\) with coefficients \((\zeta^3,\zeta^3,1+\zeta+\zeta^2+\zeta^3,1+\zeta+\zeta^2+\zeta^3)\). All eight displayed coefficients are nonzero elements of \(F\). Exact polynomial-basis arithmetic checks that the Fourier sums at \((0,0),(1,0),(0,1),(u,v)\) are all zero in both cases. Because coefficients lie in \(F\), their \(16\)-power conjugate equations for \((-1,0),(0,-1),(-u,-v)\) also vanish. Thus each representative extension contains a weight-\(4\) word; symmetry transports the obstructions to the sixteen surviving pairs. Every excluded pair already has a weight-\(4\) word from one of the four patterns above or from a rectangle. The asserted exact distance \(4\) follows for all new orbits.

## Verification
Run `python3 verify.py` using Python 3 and only its standard library. The program independently constructs the specified finite fields, enumerates all \(2380\) four-subsets, reproduces the complete length-\(17\) divided-difference count vector, exhausts the \(256\) candidate exponent pairs, partitions the necessary pairs into the two eight-element symmetry orbits, and directly evaluates all eight required Fourier sums for the two representative witnesses. Successful termination prints `VERIFY_OK`. These are finite exhaustive checks over explicitly enumerated domains, not an inference from random experiments. The lower distance bound and the reduction to these checks are established in the proof above.

## Relationship to prior work
Yu, Chen, Sun, and Zhu (arXiv:2608.18664), Theorem V.3, introduce the base code for general \(q\); Questions V.4–V.5 and Theorem V.13 describe the one-orbit extension problem and a necessary-and-sufficient testing framework. Their Corollary V.15 treats \(q=2,4,8\); Example 3 exhibits a *successful* single-orbit distance-\(5\) extension when \(q=8\). They do not give a \(q=16\) yes/no resolution. The present result rules out **all** one-orbit extensions for that next power of two using an exact divided-difference census and two explicit collinear/noncollinear obstruction words. Feng, Hollmann, and Xiang (arXiv:1804.00367) supply the broader abelian-code shift-bound framework rather than this concrete classification. No claim is made that a literature search proves absolute novelty.

## Limitations
The no-extension statement is restricted to the displayed base defining set over \(\mathbb F_{16}\), and to adding exactly one new cyclotomic orbit. It does not exclude a different base code or a code outside this abelian family with parameters \([289,282,5]_{16}\), nor address adding multiple orbits or any other \(q\). The finite enumeration is exhaustive only for the explicitly stated four-subsets and exponent pairs.

## References
1. C. Yu, H. Chen, Z. Sun, and S. Zhu, *Constructing Good Abelian Codes via Shift Bounds and Genetic Algorithms*, arXiv:2608.18664, first posted 2026-08-19; Theorem V.3, Questions V.4–V.5, Theorem V.13, Corollary V.15, Example 3. https://arxiv.org/abs/2608.18664
2. T. Feng, H. D. L. Hollmann, and Q. Xiang, *The shift bound for abelian codes and generalizations of the Donoho–Stark uncertainty principle*, arXiv:1804.00367, 2018. https://arxiv.org/abs/1804.00367
