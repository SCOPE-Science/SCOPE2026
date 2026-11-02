# A smooth rank-zero curve inside a three-parameter genus-five Hasse stratum

## Finding

Let \(k\) be algebraically closed of characteristic \(3\). For \((a,b,c)\in k^3\), let \(C_{a,b,c}\) be the smooth projective model of
\[
y^2=x^{11}+ax^7+bx^5+cx^3+x=x\,h(x^2),\qquad
h(t)=t^5+at^3+bt^2+ct+1.
\]
Write \(\Delta=\operatorname{Res}_t(h,h')\), and work on the open parameter space \(U=\{\Delta\ne0\}\subset\mathbf A_k^3\). Define
\[
u=b^3+ac^3,\qquad T=a^3b^3+c^3(a^4-b)-1,\qquad E=u+a^{27}.
\]
Every curve over \(U\) has genus \(5\) and Jacobian \(a\)-number \(1\). Its geometric Jacobian \(3\)-rank is exactly
\[
f_3(C_{a,b,c})=\begin{cases}
4,&T\ne0,\\
2,&T=0,\ E\ne0,\\
0,&T=E=0.
\end{cases}
\]
The rank-drop divisor \(V(T)\cap U\) is smooth and irreducible. Its rank-zero sublocus \(V(T,E)\cap U\) is a nonempty smooth complete-intersection curve, cut transversely inside \(U\). Each of the three strata is nonempty. In particular, the single Cartier-rank value \(4\) coexists with three different stable Frobenius ranks in this natural order-four-automorphism family.

## Assumptions and scope

The statement concerns coefficient-marked curves over the algebraic closure, not isomorphism classes. The leading coefficient of \(x^{11}\) and the coefficient of \(x\) are normalized to \(1\). Smoothness is exactly \(\Delta\ne0\): \(x h(x^2)\) is separable if and only if the quintic \(h\) is separable, since \(h(0)=1\) and the characteristic is odd. The automorphism \((x,y)\mapsto(-x,\iota y)\), where \(\iota^2=-1\), has order four. The terminology \(a\)-number means \(\dim\ker\mathcal C\) on regular differentials; \(3\)-rank means the stable Frobenius rank on \(H^1(C,\mathcal O_C)\).

## Proof

**Cartier matrix.** In the standard basis \(x^{i-1}dx/y\) for \(1\le i\le5\), the Cartier–Manin coefficient matrix is given by coefficients \(H_{ij}=[x^{3i-j}]\,f(x)\), because \((3-1)/2=1\). Thus
\[
H=\begin{pmatrix}
0&1&0&0&0\\
b&0&c&0&1\\
0&a&0&b&0\\
1&0&0&0&a\\
0&0&0&1&0
\end{pmatrix}.
\]
Reorder the indices as odd \((1,3,5)\) and even \((2,4)\). In these blocks,
\[
H=\begin{pmatrix}0&B\\ C&0\end{pmatrix},\quad
B=\begin{pmatrix}1&0\\a&b\\0&1\end{pmatrix},\quad
C=\begin{pmatrix}b&c&1\\1&0&a\end{pmatrix}.
\]
The matrix \(B\) has rank \(2\). If \(C\) had rank below \(2\), then \(c=0\) and \(ab=1\). In that case \(h'(t)=2t(t^3+b)\), and every nonzero root of \(t^3=-b\) is also a root of \(h(t)\), because \(h(t)=t^2(t^3+b)+at^3+1=1-ab=0\); the curve is singular. Therefore \(C\) has rank \(2\) throughout \(U\), giving \(\operatorname{rank}H=4\) and \(a(C)=5-4=1\).

**Frobenius-stable rank.** Write \(M^{(q)}\) for entrywise \(q\)-th power. The three-semilinear Frobenius matrix on cohomology is the transpose of the coefficient matrix above. Therefore the two-step Frobenius map on the even two-dimensional block has matrix
\[
D=B^{\mathsf T}(C^{\mathsf T})^{(3)}=\begin{pmatrix}b^3+ac^3&1\\1+bc^3&a^3\end{pmatrix},
\qquad\det D=T.
\]
On the odd block its matrix is \(C^{\mathsf T}(B^{\mathsf T})^{(3)}\). Since \(C^{\mathsf T}\) is injective and \(B^{\mathsf T}\) is surjective, the image of the latter odd-block map is exactly \(\operatorname{im}C^{\mathsf T}\); there its next iteration is conjugate through \(C^{\mathsf T}\) to \(D^{(3)}\). Therefore the stable rank of the full three-semilinear Frobenius operator is twice the stable rank of the nine-semilinear operator \(v\mapsto Dv^{(9)}\) on \(k^2\).

If \(T\ne0\), then \(D\) is invertible and the stable rank is \(2\), hence \(f_3=4\). On \(T=0\), its upper-right entry remains \(1\), so \(\operatorname{rank}D=1\), and the determinant relation yields
\[
D=\begin{pmatrix}1\\a^3\end{pmatrix}\begin{pmatrix}u&1\end{pmatrix}.
\]
The second iterate of its nine-semilinear map has scalar factor
\[
\begin{pmatrix}u&1\end{pmatrix}\begin{pmatrix}1\\a^{27}\end{pmatrix}=u+a^{27}=E.
\]
When \(E\ne0\), the stable rank of this map is \(1\), so \(f_3=2\). When \(E=0\), its square is zero, so \(f_3=0\). These calculations hold over every algebraically closed field of characteristic \(3\), without finite-field extrapolation.

**Geometry of the strata.** The polynomial \(T=(a^4-b)c^3+(ab-1)^3\) is irreducible: the rational function \(-(ab-1)^3/(a^4-b)\) is not a cube in \(k(a,b)\), because its pole along the prime divisor \(a^4-b=0\) has order one. Hence \(c^3+(ab-1)^3/(a^4-b)\) is irreducible over \(k(a,b)\), and Gauss's lemma applies since the two coefficients are coprime. In characteristic \(3\),
\[
\frac{\partial T}{\partial b}=-c^3,\quad
\frac{\partial E}{\partial a}=c^3,\quad
\frac{\partial E}{\partial b}=\frac{\partial E}{\partial c}=0.
\]
On the smooth parameter domain, \(T=0\) forces \(c\ne0\), since \(c=0\) and \(T=0\) imply \(ab=1\) and an inseparable quintic as above. Thus \(V(T)\cap U\) is smooth, and the independent gradients of \(T\) and \(E\) make \(V(T,E)\cap U\) a smooth codimension-two complete intersection wherever it is nonempty.

For nonemptiness within \(U\), the smooth triples \((a,b,c)=(0,0,0),(0,1,2),(1,1,1)\) have respectively \((T\ne0),(T=0,E\ne0),(T=E=0)\). Smoothness of all three is certified by \(\operatorname{Res}_t(h,h')\ne0\) in \(\mathbb F_3\). This completes the classification.

## Verification

Run, with Python 3 and SymPy installed, `python3 verify_symbolic.py`. It independently constructs the coefficient matrix, checks the block factorization and determinant, verifies the quintic resultant polynomial, and checks the derivative and sample identities in characteristic three. Run `python3 verify_fields.py` using only the Python 3 standard library. It independently implements \(\mathbb F_9=\mathbb F_3[\theta]/(\theta^2+1)\), checks squarefreeness directly by polynomial Euclid, constructs all matrices, and checks their fivefold Frobenius-twisted products on every smooth coefficient triple over \(\mathbb F_3\) and \(\mathbb F_9\). The exact counts are \(15,4,1\) for ranks \(4,2,0\) over \(\mathbb F_3\), and \(589,60,7\) over \(\mathbb F_9\); the respective singular counts are \(7\) and \(73\). These finite checks corroborate, but do not supply, the geometric proof.

## Relationship to prior work

Novoselov's work on hyperelliptic Cartier–Manin matrices and rational point counting treats the distinct binomial/trinomial model \(y^2=x^{2g+1}+ux^{g+1}+vx\); its genus-five specialization has degrees \(11,6,1\), not the odd-coefficient family with degrees \(11,7,5,3,1\) here. Frei studies bounds on large hyperelliptic \(a\)-numbers, and Nourozi–Rahmati–Tafazolian treat \(y^2=x^m+1\) and \(y^2=x^m+x\), which include a special binomial member of this family but not its three-dimensional Frobenius-rank degeneration. Existing general Hasse–Witt methods are explicitly credited, not claimed as new. The contribution assessed here is the *exact three-stratum geometric classification*, smoothness of the two rank-drop loci, and the coexistence of rank zero with constant \(a=1\). Relevant existing specialized classifications could remain unindexed.

## Limitations

The parameter space records equations, not distinct geometric isomorphism classes. No Newton-polygon, Ekedahl–Oort, conductor, or full automorphism-group classification is asserted. The rank-zero stratum is shown smooth and nonempty, not irreducible. The results require characteristic three and the specified normalized odd polynomial family. The mathematical proof and finite-field checks have not been externally audited.

## References

1. S. Novoselov, *Counting points on hyperelliptic curves of type \(y^2=x^{2g+1}+ax^{g+1}+bx\)*, arXiv:1902.05992 (first posted 2019-02-15), particularly Sections 1–2, https://arxiv.org/abs/1902.05992.
2. S. Novoselov, *Hyperelliptic curves, Cartier–Manin matrices and Legendre polynomials*, Prikladnaya Diskretnaya Matematika 37 (2017), 20–31, https://geodesic.mathdoc.fr/item/PDM_2017_3_a1/.
3. S. Frei, *The a-number of hyperelliptic curves*, arXiv:1703.03516 (2017), https://arxiv.org/abs/1703.03516.
4. V. Nourozi, F. Rahmati, S. Tafazolian, *The a-number of Certain Hyperelliptic Curves*, arXiv:1902.03672 (2019), https://arxiv.org/abs/1902.03672.
