# A rigid evolution algebra with infinitely many natural bases

## Finding

Over \(\mathbb Q\), let \(A\) have basis \(e_1,e_2,e_3\), with
\[
v=e_1+e_2+e_3,\qquad w=e_1,
\]
and multiplication
\[
e_1^2=v,\qquad e_2^2=-v,\qquad e_3^2=w,\qquad e_i e_j=0\quad(i\ne j).
\]
Then \(A\) is non-degenerate and non-perfect, \(\operatorname{Aut}_{\mathbb Q}(A)=\{I\}\), and \(A\) has infinitely many natural bases even after identifying bases that differ by permutation and nonzero rescaling of basis vectors. Thus even the trivial automorphism group does not force finite natural-basis moduli: infinitely many equivalence classes occur although no nonidentity algebra automorphism exists.

## Assumptions and scope

An evolution algebra is a vector space with a bilinear multiplication admitting a basis whose distinct basis vectors have zero product; such a basis is called a natural basis. Non-degenerate means that the annihilator is zero, equivalently every vector in every natural basis has nonzero square. Perfect means \(A^2=A\). All vector spaces, maps, and automorphisms here are over \(\mathbb Q\). The result is an explicit existence example, not a classification of all such algebras or a claim about minimal dimension.

## Proof

**1. The algebra is non-degenerate and non-perfect.** For \(x=(x_1,x_2,x_3)\) and \(y=(y_1,y_2,y_3)\), bilinearity and the table give
\[
xy=(x_1y_1-x_2y_2)v+x_3y_3w.
\]
The vectors \(v,w\) are linearly independent, so \(A^2=\operatorname{span}\{v,w\}\) has dimension \(2<3\); hence \(A\) is not perfect. If \(xA=0\), then \(xe_1=x_1v=0\), \(xe_2=-x_2v=0\), and \(xe_3=x_3w=0\). Since \(v,w\ne0\), all three coordinates vanish. Thus \(\operatorname{Ann}(A)=0\), so \(A\) is non-degenerate.

**2. Infinitely many natural bases.** For every integer \(t\ge2\), set
\[
f_1(t)=e_1+t e_2,\qquad f_2(t)=e_1+t^{-1}e_2,\qquad f_3(t)=e_3.
\]
The determinant of the first two coordinate columns is \(t^{-1}-t\ne0\), so these vectors form a basis. Their mixed products vanish:
\[
f_1(t)f_2(t)=e_1^2+e_2^2=0,\qquad
f_1(t)e_3=f_2(t)e_3=0.
\]
Thus each is a natural basis. The lines spanned by \(f_1(t)\) and \(f_2(t)\) in \(U=\operatorname{span}\{e_1,e_2\}\) are respectively \([1:t]\) and \([1:t^{-1}]\). Scaling does not change these lines, and permutation only interchanges the two lines; the third line \(\mathbb Q e_3\) lies outside \(U\) and cannot be exchanged with them. Consequently two such bases are equivalent only if their parameters satisfy \(s=t\) or \(s=t^{-1}\). For integers \(s,t\ge2\), the second possibility is impossible unless \(s=t=1\), which is excluded. Hence all parameters \(t=2,3,4,\ldots\) give pairwise inequivalent natural bases.

**3. The automorphism group is trivial.** Define symmetric bilinear forms
\[
q_1(x,y)=x_1y_1-x_2y_2,\qquad q_2(x,y)=x_3y_3,
\]
so that \(xy=q_1(x,y)v+q_2(x,y)w\). Let \(T\in\operatorname{Aut}_{\mathbb Q}(A)\). Since \(A^2\) is characteristic, write
\[
T(v)=\alpha v+\beta w,\qquad T(w)=\gamma v+\delta w
\]
with \(\alpha\delta-\beta\gamma\ne0\). Comparing coefficients of \(v,w\) in \(T(xy)=T(x)T(y)\) gives
\[
q_1(Tx,Ty)=\alpha q_1(x,y)+\gamma q_2(x,y),\qquad
q_2(Tx,Ty)=\beta q_1(x,y)+\delta q_2(x,y).
\]
The ranks of \(q_1,q_2\) are \(2,1\), respectively. Every linear combination \(a q_1+b q_2\) with \(ab\ne0\) has rank \(3\), since its matrix is \(\operatorname{diag}(a,-a,b)\). Pullback by an invertible \(T\) preserves rank. The first displayed form therefore forces \(\gamma=0\) and \(\alpha\ne0\); the second forces \(\beta=0\) and \(\delta\ne0\). Thus \(T(v)=\alpha v\), \(T(w)=\delta w\), and \(q_i(Tx,Ty)\) equals \(\alpha q_1(x,y)\) for \(i=1\) and \(\delta q_2(x,y)\) for \(i=2\).

The radicals of \(q_1,q_2\) are \(\mathbb Q e_3\) and \(U\), respectively, so \(T\) preserves both subspaces. Since \(w=e_1\), we have \(T(e_1)=\delta e_1\). Write \(T(e_2)=a e_1+b e_2\) and \(T(e_3)=c e_3\). The equation \(T(v)=\alpha v\) gives \(a=\alpha-\delta\), \(b=c=\alpha\). Now
\[
0=\alpha q_1(e_1,e_2)=q_1(T e_1,T e_2)=\delta(\alpha-\delta),
\]
so \(\alpha=\delta\). Finally,
\[
\alpha=q_1(T e_1,T e_1)=\delta^2=\alpha^2.
\]
As \(\alpha\ne0\), it follows that \(\alpha=\delta=1\), whence \(a=0\), \(b=c=1\), and \(T=I\). This proves \(\operatorname{Aut}_{\mathbb Q}(A)=\{I\}\).

## Verification

The multiplication table gives the product formula directly. The two-dimensionality of \(A^2\) and the zero-annihilator calculation establish the stated structural assumptions. The family \(f_1(t),f_2(t),f_3(t)\) is checked by its determinant and all three mixed products. The automorphism proof uses only rank preservation of two explicitly written bilinear forms and coefficient comparison; it does not rely on finite experiments or an external certificate.

## Relationship to prior work

Kaygorodov, Martín González, and Viruel ask whether infinitely many natural-basis classes can coexist with a finite automorphism group (arXiv:2610.22248v1, Question 14). A related two-dimensional rank-one case establishes the broad finite-group phenomenon with a nontrivial group of order \(2\); that does not imply the stronger trivial-group case proved here, where \(\dim A=3\) and \(\dim A^2=2\). The survey's own preceding example has an infinite orthogonal symmetry group. Boudi, Cabrera Casado, and Siles Molina characterize natural vectors and describe how orthogonal natural families extend to natural bases (arXiv:2006.14460v1, especially Section 2), but do not give this trivial-automorphism construction.

## Limitations

This is one explicit three-dimensional example over \(\mathbb Q\); it does not classify the natural bases of arbitrary non-perfect evolution algebras, establish a minimum dimension, or determine the result over every field. The literature search was targeted rather than exhaustive, so unindexed equivalent examples remain a residual originality risk. No independent audit has been performed.

## References

1. I. Kaygorodov, C. Martín González, and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1, submitted 2026-10-15, Question 14 and the discussion of natural bases.
2. N. Boudi, Y. Cabrera Casado, and M. Siles Molina, *Natural families in evolution algebras*, arXiv:2006.14460v1 (2020); published in *Publicacions Matemàtiques* 66 (2022), 159–181.
