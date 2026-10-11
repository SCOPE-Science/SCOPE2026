# A sharp angular phase boundary for the Frobenius symmetric-modulus defect of orthogonal-column rank-one pairs

## Finding
For a real or complex square matrix, write \(\mathfrak{s}(Z)=(|Z|+|Z^*|)/2\), where \(|Z|=(Z^*Z)^{1/2}\). Define the signed squared Frobenius triangle defect
\[\Delta(A,B)=\|\mathfrak{s}(A+B)\|_{S_2}^2-\|\mathfrak{s}(A)+\mathfrak{s}(B)\|_{S_2}^2.\]
The theorem gives the complete sign profile on a natural two-parameter family of *rank-one pairs with orthogonal input supports*, one of which is a positive corner projection.

For \(a>0\), \(0\le x\le1\), \(y=\sqrt{1-x^2}\), and \(t\ge0\), set
\[A=a\begin{pmatrix}x&0\\y&0\end{pmatrix},\qquad B=at\begin{pmatrix}0&0\\0&1\end{pmatrix}.\]
Then \(|A|=aE_{11}\), \(|B|=atE_{22}\), so in particular \(|A||B|=0\). The **exact signed defect** is
\[\boxed{\frac{\Delta(A,B)}{a^2}=\frac{t(1-x^2)(2x-1-2xt-t^2)}{1+2xt+t^2}.}\]
For \(0\le x<1\) and \(t>0\), define the positive threshold only when \(x>1/2\):
\[T(x)=\sqrt{x^2+2x-1}-x.\]
When \(1/2<x<1\), the defect is strictly positive for \(0<t<T(x)\), zero at \(t=T(x)\), and strictly negative for \(t>T(x)\). When \(0\le x\le1/2\), it is strictly negative for every \(t>0\). At \(x=1\) or \(t=0\) it is zero. Therefore **\(x=1/2\) is the sharp angular cutoff**: some positive coupling violates the usual Frobenius triangle bound exactly when \(1/2<x<1\). The function \(T(x)\) is strictly increasing on \((1/2,1)\) and tends to \(\sqrt2-1\) at the right endpoint; the defect itself vanishes at \(x=1\).

## Assumptions and scope
All statements apply to the displayed real \(2\times2\) matrices, embedded in complex matrices if desired, with the parameters quantified above. The angle \(\arccos x\) measures the overlap of the outgoing unit direction of \(A\) with its incoming right support. The comparison is between the Schatten \(2\)-norm of the symmetric modulus of the sum and the Schatten \(2\)-norm of the sum of the symmetric moduli. The theorem **does not** determine the unrestricted optimal matrix constant for arbitrary pairs and does not classify all pairs with orthogonal input supports.

## Proof
For every nonzero \(2\times2\) matrix \(Z\), put \(R=Z^*Z\), \(h=\operatorname{tr}R\), and \(d=|\det Z|\). Cayley–Hamilton gives \(R^2-hR+d^2I=0\), hence
\[(R+dI)^2=(h+2d)R,\qquad |Z|=\frac{R+dI}{\sqrt{h+2d}}.\]
The second identity is the unique positive square root, because \(h+2d>0\). Applying the same argument to \(ZZ^*\) yields
\[\mathfrak{s}(Z)=\frac{Z^*Z+ZZ^*+2dI}{2\sqrt{\operatorname{tr}(Z^*Z)+2d}}.\]

By homogeneity set \(a=1\). Let \(d_0=1+2xt+t^2>0\). Since \(\det(A+B)=xt\), the preceding formula gives
\[\mathfrak{s}(A+B)=\frac1{2\sqrt{d_0}}\begin{pmatrix}1+x^2+2xt&y(x+t)\\y(x+t)&1-x^2+2t^2+2xt\end{pmatrix}.\]
For the separate rank-one terms, use \(|A|=E_{11}\), \(|A^*|=uu^{\mathsf T}\) for \(u=(x,y)^{\mathsf T}\), and \(\mathfrak{s}(B)=tE_{22}\), obtaining
\[\mathfrak{s}(A)+\mathfrak{s}(B)=\frac12\begin{pmatrix}1+x^2&xy\\xy&1-x^2+2t\end{pmatrix}.\]
For each real symmetric \(2\times2\) matrix \(H\), \(\|H\|_{S_2}^2=\operatorname{tr}(H^2)\). Expanding the two displayed matrices, replacing \(y^2\) with \(1-x^2\), and factoring yields exactly
\[\Delta(A,B)=\frac{t(1-x^2)(2x-1-2xt-t^2)}{1+2xt+t^2}.\]
Undoing \(a=1\) multiplies both squared norms by \(a^2\).

For \(t>0\) and \(x<1\), the denominator and the first two factors are positive. The remaining factor \(f_x(t)=2x-1-2xt-t^2\) strictly decreases in \(t\ge0\). If \(x\le1/2\), it is strictly negative for all \(t>0\). If \(x>1/2\), its unique positive zero is \(T(x)\), and its signs on either side are as claimed. If \(x=1\), the factor \(1-x^2\) annihilates the defect. The derivative \(T'(x)=(x+1)/\sqrt{x^2+2x-1}-1>0\) on \((1/2,1)\), giving the claimed endpoint behavior.

## Verification
A complete coefficient-level exact polynomial replay is supplied as `verify.py`, using only the Python standard library. It verifies the identity
\[\operatorname{tr}(N^2)-d_0\operatorname{tr}(M^2)=4t(1-x^2)(2x-1-2xt-t^2),\]
where \(2\sqrt{d_0}\,\mathfrak{s}(A+B)=N\) and \(2(\mathfrak{s}(A)+\mathfrak{s}(B))=M\) after \(a=1\). This is an exact polynomial identity in \(x,t\), not numerical sampling. It also tests an exact rational witness, taking \(a=5\), \(x=4/5\), \(y=3/5\), \(t=1/5\), for which
\[\|\mathfrak{s}(A+B)\|_{S_2}^2=\frac{803}{34},\quad\|\mathfrak{s}(A)+\mathfrak{s}(B)\|_{S_2}^2=\frac{233}{10},\quad\Delta=\frac{27}{85}>0.\]
The analytic proof, not the finite witness, establishes the complete parameter classification.

## Relationship to prior work
Bourin and Lee (2026, arXiv:2602.19607v1) introduce general triangle bounds for the arithmetic symmetric modulus and explicitly raise the corresponding Schatten-norm problem. Zhang (2026, arXiv:2603.01046v1, Section 8) **already proves general Frobenius subadditivity fails** and gives a numerical example with two invertible \(2\times2\) summands (Example 8.2). Consequently **that bare counterexample and the global dimension threshold are not claimed as new here**. The present result instead resolves the complete angular/coupling sign diagram inside a natural, substantially restricted rank-one pair with \(|A||B|=0\); the exact threshold \(x=1/2\), re-entrant equality, and formula do not follow from Zhang's full-rank example. Zhang's earlier quadratic symmetric-modulus triangle theorem (arXiv:2602.01463v3) concerns a different nonlinear modulus and cannot decide this arithmetic defect.

## Limitations
The exact phase law applies to the displayed canonical family only. It does not assert the globally optimal Schatten \(2\) constant, nor a classification for arbitrary rank-one pairs with orthogonal input supports, complex relative phases, other Schatten exponents, or infinite-dimensional operators. Literature checks cannot rule out unpublished or unindexed equivalent formulations. No external independent validation is represented.

## References
Bourin, J.-C., and Lee, E.-Y., *Triangle inequalities for the operator symmetric modulus*, arXiv:2602.19607v1 (first public: 2026-02-23), Sections 2 and 6; https://arxiv.org/html/2602.19607v1.

Zhang, T., *Operator symmetric moduli and sharp triangle inequalities*, arXiv:2603.01046v1 (2026), Section 8, Theorem 8.1 and Example 8.2; https://arxiv.org/html/2603.01046v1.

Zhang, T., *An operator triangle inequality for the quadratic symmetric modulus*, arXiv:2602.01463v3 (2026), Section 2; https://arxiv.org/html/2602.01463v3.
