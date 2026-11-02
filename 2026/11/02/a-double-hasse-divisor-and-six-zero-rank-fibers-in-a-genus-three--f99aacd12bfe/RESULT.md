# A double Hasse divisor and six zero-rank fibers in a genus-three order-four family

## Finding
Let \(k=\overline{\mathbb F}_5\), and let \(C_{a,b}\) be the smooth projective completion of
\[y^2=x^7+a x^5+b x^3+x,\qquad (a,b)\in k^2.\]
On the smooth locus defined below, the Jacobian's \(a\)-number and \(5\)-rank are
\[\boxed{(a(C_{a,b}),f_5(C_{a,b}))=\begin{cases}
(0,3),&ab+1\ne0,\\
(2,1),&ab+1=0\text{ and }b^6\ne1,\\
(2,0),&ab+1=0\text{ and }b^6=1.
\end{cases}}\]
The Hasse determinant has a square factor: its vanishing scheme is twice the smooth reduced nonordinary curve \(ab+1=0\). Its deepest locus consists of exactly six distinct smooth *coefficient-marked* parameters \((a,b)=(-b^{-1},b)\) with \(b^6=1\). Over \(\mathbb F_5\), two are rational and the remaining four form two Frobenius orbits of length two. These six geometric curves are mutually isomorphic, so the marked-point count is not an isomorphism-class count. Every member has genus three and an order-four automorphism. There are no \(a\)-number-one or \(5\)-rank-two fibers.

## Assumptions and scope
The base field is the algebraic closure of the field of characteristic five, and all parameters are coefficient-marked. Write
\[g(T)=T^3+aT^2+bT+1,\qquad \Delta(a,b)=a^3+a^2b^2+3ab+b^3+3.\]
Since the defining polynomial is \(xg(x^2)\) and \(g(0)=1\), it is squarefree precisely when \(\Delta\ne0\); throughout, assume this condition. A squarefree hyperelliptic polynomial of degree seven defines a smooth curve of genus three. The automorphism \((x,y)\mapsto(-x,\iota y)\), where \(\iota^2=-1\in k\), has order four and its square is the hyperelliptic involution. The \(a\)-number is \(\dim_k\operatorname{Hom}(\alpha_5,J)\); the \(5\)-rank is the stable rank of Frobenius on \(H^1(C,\mathcal O_C)\), equivalently the degree of the characteristic polynomial of Frobenius modulo five after omitting the zero roots.

## Proof
For \(i=1,2,3\), use the standard basis \(x^{i-1}dx/y\) of regular differentials. Let \(c_j\) be the coefficient of \(x^j\) in \(f(x)^{(5-1)/2}=f(x)^2\), where \(f=x^7+a x^5+b x^3+x\). The Hasse--Witt coefficient matrix, with entries \(H_{ij}=c_{5i-j}\), is
\[H=\begin{pmatrix}2b&0&1\\0&2(ab+1)&0\\1&0&2a\end{pmatrix},\qquad \det H=-2(ab+1)^2.\]
For \(ab+1\ne0\), the matrix is invertible: the \(a\)-number is zero and the \(5\)-rank is three. On \(ab=-1\), the middle entry vanishes and the remaining block
\[B=\begin{pmatrix}2b&1\\1&2a\end{pmatrix}
=\binom{2b}{1}\begin{pmatrix}1&2a\end{pmatrix}\]
has rank one, since its determinant is \(4ab-1=-5=0\) in characteristic five. Thus \(\operatorname{rank}(H)=1\) and the \(a\)-number equals two everywhere on the nonordinary divisor. This establishes the claimed multiplicity two of the Hasse scheme: \(-2\) is invertible and the equation \(ab+1\) cuts out a smooth divisor, as its gradient \((b,a)\) does not vanish there.

For the stable rank, the Frobenius-semilinear second iterate is represented by \(H H^{(5)}\), with fifth powers taken entrywise. Write \(u=(2b,1)^T\) and \(v=(1,2a)^T\); then \(B=uv^T\) and
\[BB^{(5)}=u\,(v^Tu^{(5)})\,(v^{(5)})^T,
\qquad v^Tu^{(5)}=2(b^5+a).\]
As \(ab=-1\) implies \(a=-b^{-1}\) and \(b\ne0\), the scalar vanishes exactly when \(b^6=1\). Then the second iterate vanishes, and the stable \(5\)-rank is zero. Otherwise the rank-one image persists under every further Frobenius iterate: each additional scalar is a fifth-power twist of this same nonzero scalar. Hence the stable \(5\)-rank is one. This establishes the complete rank formula over \(k\), not just over a finite subfield.

The discriminant of \(g\) is \(\Delta\), and on \(a=-b^{-1}\) it simplifies to
\[\Delta(-b^{-1},b)=\frac{(b^3-2)^2}{b^3}.\]
Thus the hyperbola loses precisely the three geometric points with \(b^3=2\); none is in \(b^6=1\), as \(b^3=\pm1\) there. Since \((b^6-1)'=b^5\ne0\) at its roots, the six exceptional marked parameters are distinct. Frobenius sends \(b\mapsto b^5=b^{-1}\) on these roots. Two satisfy \(b\in\mathbb F_5\) and the other four form two two-cycles, giving degrees \(1,1,2,2\). Finally, scaling \(x\mapsto t x\), \(y\mapsto t^{1/2}y\) for \(t^6=1\) transforms \((a,b)\) into \((at^4,bt^2)\), and inversion \(x\mapsto x^{-1}\), \(y\mapsto y/x^4\) exchanges \((a,b)\) with \((b,a)\). On the six-point exceptional set, scaling acts transitively on each three-point subset with fixed \(b^3\), and inversion exchanges the two subsets; hence all six curves are isomorphic over \(k\).

## Verification
Run \(\texttt{python verify\_symbolic.py}\) (requires SymPy) to reconstruct every Hasse coefficient, the determinant, cubic discriminant, restricted discriminant, the Frobenius scalar, and the coprimality and squarefreeness of the exceptional locus. It prints \(\texttt{EXACT\_HASSE\_DISCRIMINANT\_AND\_EXCEPTION\_OK}\).

Separately run \(\texttt{python verify\_fields.py}\) (Python standard library only). It constructs \(\mathbb F_5\), \(\mathbb F_{25}\), and \(\mathbb F_{125}\) directly, derives the Cartier matrix by coefficient convolution instead of importing the matrix, and computes all smooth parameter strata over the first two fields from ordinary rank and Frobenius-twisted stable rank. Smooth-field counts are \(18,1,2\) (ordinary, rank-one, rank-zero) over \(\mathbb F_5\), and \(580,15,6\) over \(\mathbb F_{25}\). Independently, direct point counting for \((a,b)=(4,1)\) gives \(\#C(\mathbb F_5)=6\), \(\#C(\mathbb F_{25})=26\), \(\#C(\mathbb F_{125})=96\), so the first three numerator coefficients are \(0,0,-10\), all divisible by five. These finite checks corroborate the symbolic proof but are not substitutes for its algebraic-closure quantifiers.

## Relationship to prior work
S. Novoselov's 2019 preprint studies genus-three hyperelliptic curves of the different two-parameter form \(y^2=x^7+A x^4+B x\), emphasizing Frobenius polynomial and point counting; its explicit models do not specialize to the generic \(x^7+a x^5+b x^3+x\) family through a coefficient-preserving parameter substitution. Ohashi--Kudo--Harashita (2021) determine \(a\)-numbers in a family of *nonhyperelliptic* genus-three curves with cyclic automorphism group of order six; the present hyperelliptic order-four family is geometrically different. The general hyperelliptic Cartier--Manin coefficient rule used here is established mathematics and is not claimed as new. The present contribution is the complete geometric scheme-theoretic Hasse divisor and its distinct stable-rank-zero stratum, including the marked Frobenius-orbit structure. An earlier equivalent unindexed calculation remains possible.

## Limitations
All claims hold for smooth coefficient-marked members in characteristic five, not for the excluded discriminant locus or other characteristics. Six exceptional marked parameters represent one geometric isomorphism class. This result does not determine the full Newton polygon, Ekedahl--Oort type, or geometric moduli image, and a self-review is not independent external verification. The originality comparison is limited to the available inspected literature and searchable records.

## References
1. S. Novoselov, *Counting points on hyperelliptic curves of type \(y^2=x^{2g+1}+ax^{g+1}+bx\)* (first public arXiv version, 15 February 2019), arXiv:1902.05992, https://arxiv.org/abs/1902.05992.
2. R. Ohashi, M. Kudo, and S. Harashita, *The a-numbers of non-hyperelliptic curves of genus 3 with cyclic automorphism group of order 6* (first public arXiv version, 18 November 2021), arXiv:2111.09777, https://arxiv.org/abs/2111.09777.
