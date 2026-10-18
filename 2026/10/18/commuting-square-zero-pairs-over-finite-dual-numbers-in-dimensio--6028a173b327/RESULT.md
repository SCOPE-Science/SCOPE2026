# Commuting square-zero pairs over finite dual numbers in dimension three: an exact odd-characteristic count

## Finding

Let \(q\) be any odd prime power, let \(k=\mathbb F_q\), and let \(R=k[\varepsilon]/(\varepsilon^2)\). Define
\[
C(q)=\#\{(X,Y)\in M_3(R)^2:X^2=Y^2=0,\ XY=YX\}.
\]
Put \(S(q)=(q^2-1)(q^2+q+1)\). Then
\[
\boxed{C(q)=q^{18}+(5q-3)S(q)q^9.}
\]
More precisely, under reduction of both matrices modulo \(\varepsilon\), the solution fibers are affine spaces with four exact strata. The reduction \((0,0)\) has one base point and fiber dimension \(18\). The stratum with exactly one nonzero reduction has \(2S(q)\) base points and fiber dimension \(10\). The stratum with two nonzero proportional reductions has \(S(q)(q-1)\) base points and fiber dimension \(9\). The stratum with two linearly independent nonzero reductions has \(2q(q-1)S(q)\) base points and fiber dimension \(8\). Consequently their respective contributions are \(q^{18}\), \(2S(q)q^{10}\), \(S(q)(q-1)q^9\), and \(2q(q-1)S(q)q^8\).

The same four-stratum description holds for geometric fibers over any field of characteristic different from two, with affine-fiber dimensions as specified; only the finite-field point enumeration uses \(q\). This is an enumeration of labeled ordered pairs, not simultaneous similarity orbits.

## Assumptions and scope

The coefficient field has characteristic different from two. Matrices are \(3\times3\) and are considered as ordered pairs. A square-zero matrix satisfies \(X^2=0\) exactly; commuting means \(XY=YX\). The dual-number parameter \(\varepsilon\) is central with \(\varepsilon^2=0\). Every matrix admits a unique decomposition \(X=A+\varepsilon P\) with \(A,P\in M_3(k)\). The word *fiber* refers to the set of solutions for \((P,Q)\) over a fixed field-valued reduction \((A,B)\); these fibers are kernels of explicit homogeneous linear maps.

The geometric claim about affine fibers does not imply that the full representation scheme is reduced. No classification of simultaneous similarity classes is asserted. In characteristic two the commutator and anticommutator conditions coincide for the two generators, and that different case is outside the finding.

## Proof

**Step 1: square-zero reductions.** If \(A\in M_3(k)\) has \(A^2=0\) and \(A\ne0\), then \(\operatorname{im}A\subseteq\ker A\), whence \(\operatorname{rank}A=1\). Such a matrix is a nonzero rank-one map \(u\alpha\), where \(u\in k^3\setminus\{0\}\), \(\alpha\in(k^3)^*\setminus\{0\}\), and \(\alpha(u)=0\). Choose its image line in \(q^2+q+1\) ways, a kernel plane containing that line in \(q+1\) ways, and a nonzero map between the one-dimensional quotient and the image line in \(q-1\) ways. The number is therefore
\[
(q^2+q+1)(q+1)(q-1)=S(q).
\]
Every such \(A\) is conjugate to the elementary matrix \(E_{12}\).

**Step 2: commuting reduction pairs.** If nonzero square-zero matrices \(A=u\alpha\) and \(B=v\beta\) commute and their common product \(AB=BA\) is nonzero, equality of the rank-one maps forces \(u,v\) proportional and \(\alpha,\beta\) proportional. Thus \(B\) is a scalar multiple of \(A\), contradicting \(AB\ne0\), since \(A^2=0\). Therefore every commuting square-zero pair \((A,B)\) in dimension three has \(AB=BA=0\).

Fix \(A=E_{12}\). A commuting matrix has the form
\[
B=\begin{pmatrix}a&b&c\\0&a&0\\0&d&e\end{pmatrix}.
\]
The condition \(B^2=0\) forces \(a=e=0\) and \(cd=0\). Thus either \(B=bE_{12}\), or precisely one of \(c,d\) is nonzero, while \(b\) is arbitrary. There are \(q-1\) nonzero proportional choices and \(2q(q-1)\) independent choices for every \(A\ne0\). Summing over the \(S(q)\) choices of \(A\), and allowing either member of the pair to be zero, gives the four base-stratum counts stated above. Every independent pair is simultaneously conjugate, after a common nonzero scalar adjustment and possibly transposition, to \((E_{12},E_{13})\); transposition preserves all three lifting equations after reversing matrix products.

**Step 3: linear lifts.** Write \(X=A+\varepsilon P\), \(Y=B+\varepsilon Q\). Because \(\varepsilon^2=0\), the equations are equivalent to the reduction constraints and
\[
AP+PA=0,\qquad BQ+QB=0,\qquad [A,Q]+[P,B]=0.
\]
These are \(27\) homogeneous scalar linear equations in the \(18\) entries of \((P,Q)\). Thus, whenever consistent reduction equations hold, each lift fiber is an affine \(k\)-space whose dimension is the common nullity. At \((0,0)\) every entry is free, giving dimension \(18\).

For \((A,0)\), the first equation says that \(P\) anticommutes with \(A\), while the third says that \(Q\) commutes with \(A\). Taking \(A=E_{12}\), each of these two spaces has dimension \(5\). Hence the fiber dimension is \(10\); the case \((0,B)\) is symmetric.

Suppose \(A=E_{12}\) and \(B=tA\) for \(t\ne0\). Put \(H=Q-tP\). Then \(P,H\) both anticommute with \(A\), and \(H\) must also commute with \(A\). The anticommutant of \(E_{12}\) consists of the matrices
\[
H=\begin{pmatrix}h&h_{12}&h_{13}\\0&-h&0\\0&h_{32}&h_{33}\end{pmatrix},
\]
with \(5\) free coordinates. Within this space the equation \([A,H]=0\) is exactly \(2h=0\), since the remaining components already vanish. Because the characteristic is odd, this sets \(h=0\) and leaves a four-dimensional intersection. The independent choice of \(P\) has dimension \(5\). The proportional-pair fiber therefore has dimension \(9\).

Finally take the independent representative \((A,B)=(E_{12},E_{13})\). Choose arbitrary \(a_1,a_2,a_8,b_1,b_2,b_4,b_5,b_8\in k\), and set
\[
P=\begin{pmatrix}
 a_8-b_5&a_1&a_2\\0&-a_8+b_5&0\\0&b_4+b_8&a_8
\end{pmatrix},\qquad
Q=\begin{pmatrix}
 -b_8&b_1&b_2\\0&b_4&b_5\\0&0&b_8
\end{pmatrix}.
\]
Direct multiplication verifies all three lift equations. Conversely, solving the entries of those equations successively forces every solution to take exactly this form, with the displayed eight coordinates free. Thus the fiber dimension is \(8\). The other independent-reduction branch is obtained by conjugation combined with transposition and has the same dimension.

**Step 4: exact summation.** Each affine \(k\)-space of dimension \(d\) has \(q^d\) points. Therefore
\[
\begin{aligned}
 C(q)&=q^{18}+2S(q)q^{10}+S(q)(q-1)q^9
                  +2S(q)q(q-1)q^8\\
 &=q^{18}+S(q)q^9(2q+q-1+2q-2)\\
 &=q^{18}+(5q-3)S(q)q^9.
\end{aligned}
\]
This proves both the exact stratification and the closed formula for every odd prime power.

## Verification

The accompanying `verify.py` uses only the Python standard library. It enumerates all square-zero reductions \((A,B)\) and all commuting ordered pairs for the prime fields \(\mathbb F_2\) and \(\mathbb F_3\), constructs the actual \(27\)-by-\(18\) linear lift map at every such pair, and computes the rank by exact modular Gaussian elimination. The odd-field complete enumeration for \(q=3\) finds \(105\) square-zero reductions and base-stratum sizes \((1,208,208,1248)\) with lift dimensions \((18,10,9,8)\); the resulting count is \(411984873\), precisely the closed formula. The characteristic-two check is a boundary check only, not part of the stated theorem. The script additionally checks the four representative nullities over the prime fields \(2,3,5,7\). Output terminates with `VERIFY_OK`.

These are finite checks and are not offered as a proof for all odd prime powers. The arbitrary-field deductions are the rank-one classification, explicit commuting normal forms and the symbolic linear solution above.

## Relationship to prior work

Avni–Onn–Prasad–Vaserstein (2007) classify similarity classes of individual \(3\)-by-\(3\) matrices over local principal ideal rings; their classification provides context but does not directly count commuting square-zero ordered pairs in a fixed dual-number ring. Prasad–Singla–Spallone (2012) classify matrix similarity over local rings of length two; it likewise addresses individual matrices. Britnell–Wildon (2010/2011) analyze the coexistence of commuting similarity classes over finite fields; Sharma (2014) studies simultaneous similarity classes of commuting pairs over a field. Neither is the present labeled lift-fiber count over dual numbers.

Previously recorded work on the three-dimensional exterior-algebra representation scheme studies \(X^2=Y^2=XY+YX=0\). Its characteristic-two instance agrees with commuting square-zero pairs, so that characteristic is expressly excluded here. Over odd-characteristic fields the exterior-algebra relation is anticommutation rather than commutation: in particular its proportional-stratum first-order fiber has dimension \(10\), whereas the commutative-algebra fiber above has dimension \(9\). Thus the odd-characteristic count is not the same result under a change of signs. A previously recorded count of one square-zero \(2\)-by-\(2\) matrix over a different, four-dimensional local algebra likewise does not imply the present pair count.

## Limitations

The formula covers ordered, labeled pairs of square-zero \(3\)-by-\(3\) matrices over dual numbers only for odd prime powers. It does not count similarity orbits, assert reducedness of the representation scheme, classify higher dimensions, or treat thicker nilpotent coefficient rings. The characteristic-two computation is deliberately excluded from the claimed novelty because the corresponding anticommuting exterior-algebra problem already covers that boundary. Exhaustive historical coverage of mathematical literature is not claimed; earlier equivalent or stronger descriptions in unlocated work remain possible. Independent review has not been performed.

## References

1. N. Avni, U. Onn, A. Prasad, and L. Vaserstein, *Similarity classes of \(3\times3\) matrices over a local principal ideal ring*, arXiv:0708.1608 (first public preprint 2007-08-12). Sections 1–3.
2. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811 (2010), Journal of the London Mathematical Society (2011). Sections 1–4.
3. A. Prasad, P. Singla, and S. Spallone, *Similarity of matrices over local rings of length two*, arXiv:1212.6157 (2012). Introduction and early classification sections.
4. A. Sharma, *Simultaneous similarity classes of commuting matrices over a finite field*, arXiv:1409.2698 (2014). Introduction and dimension-three discussion.
