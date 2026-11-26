# Exact finite-field census of a characteristic-five cyclic trigonal slice

## Finding

Let \(q=5^m\), \(m\ge1\). Among the \(q^3\) triples \((a,b,c)\in\mathbb F_q^3\) defining
\[
y^3=x^5+a x^3+b x+c,
\]
exactly \(q^2\) have a geometrically singular affine equation. Of the others, the numbers of triples for which the smooth projective genus-four curve has geometric Jacobian invariants \((f_5,a_J)\) are
\[
\begin{array}{c|r}
(f_5,a_J)&\text{number of coefficient triples}\\\hline
(0,4)&q(q-1)\\
(0,2)&(q-1)^2\\
(2,2)&(q-1)^3.
\end{array}
\]
Here \(f_5\) is the geometric \(5\)-rank, and \(a_J\) is the dimension of the kernel of Cartier on regular differentials. The census counts equations in the displayed coordinates, not isomorphism classes, and applies over all extensions of \(\mathbb F_5\). This odd-plus-constant slice contains \(y^3=x^5-x\); the census measures the two geometric rank-zero types and the rank-two type among smooth presentations in this slice. The geometric partition is an input to the census and is not asserted as a distinct finding.

## Separability and the geometric partition

Write \(F=x^5+a x^3+b x+c\). If \(a=0\), \(F\) is squarefree exactly when \(b\ne0\). If \(a\ne0\), a multiple root \(t\) must satisfy
\[
t^2=3b/a,\qquad F(t)=c+4b(a^2+b)t/a^2.
\]
Over the algebraic closure these conditions have a common solution exactly when \(a^5c^2=3b^3(a^2+b)^2\), including when either side vanishes. Thus in all cases squarefreeness is equivalent to \(a^5c^2-3b^3(a^2+b)^2\ne0\). The affine equation is smooth exactly when \(F\) is squarefree, by the two partial derivatives. For a squarefree \(F\), the degree-three Kummer cover of \(\mathbb P^1\) is totally ramified at the five roots and infinity, so Riemann–Hurwitz gives genus four. If \(F\) is not squarefree, it has at most four distinct finite roots, so the normalization has at most five branch points and genus at most three. In both cases the pole order of \(F\) at infinity is five, so \(F\) is not a cube and the cover has degree three.

The broader monic-quintic result cited below implies on this slice that for squarefree \(F\), \((f_5,a_J)=(0,4)\) if \(a=0\), \((0,2)\) if \(a\ne0\) and \(b=-a^2\), and \((2,2)\) otherwise. For a direct check, take the regular differential basis \(\omega_0=dx/y\) and \(\omega_j=x^{j-1}dx/y^2\) for \(j=1,2,3\). At a finite branch point, \(dx\) vanishes to order two; at infinity the orders of \(x,y,dx\) are \(-3,-5,-4\), which proves regularity. Rewrite \(dx/y=(y^{-2})^5 F^3 dx\) and \(dx/y^2=(y^{-1})^5 F dx\). The coefficients of \(F^3\) of degrees \(4,9,14\) are \(abc,a(a^2+b),0\) modulo five. In the numerators \(F,xF,x^2F\) only \(xF\) contributes in degree four, with coefficient \(a\). Thus the \(5^{-1}\)-linear Cartier operator sends
\[
\omega_0\longmapsto (abc)^{1/5}\omega_1+[a(a^2+b)]^{1/5}\omega_2,
\qquad \omega_2\longmapsto a^{1/5}\omega_0,
\qquad \omega_1,\omega_3\longmapsto0.
\]
For \(a=0\) it is zero. For \(a\ne0\) the rank is two: if \(b=-a^2\), it is nilpotent, and otherwise its restriction to its two-dimensional image is bijective. Taking stable rank for \(f_5\) and nullity for \(a_J\) gives the partition.

## Exact census

For \(a=0\) there are \(q(q-1)\) smooth triples giving \((0,4)\) and \(q\) singular triples. For \(a\ne0\) and \(b=-a^2\), exactly the single choice \(c=0\) is singular. This gives \((q-1)^2\) smooth triples of type \((0,2)\).

To count all singular triples with a fixed \(a\ne0\), let \(\chi\) be the quadratic character of \(\mathbb F_q^\times\). For \(b\notin\{0,-a^2\}\), the two possible critical points are distinct and the coefficient of \(t\) in \(F(t)\) is nonzero. Each gives a distinct singular value of \(c\) in \(\mathbb F_q\) if and only if \(t\in\mathbb F_q\). There are \((q-1)/2\) nonzero \(b\) for which \(3b/a\) is a square, including \(-a^2\) exactly when \(\chi(2a)=1\). Each of the exceptional cases \(b=0,-a^2\) gives one singular \(c\), whether or not the critical points are rational. The total for this \(a\) is therefore
\[
2\Big(\frac{q-1}{2}-\frac{1+\chi(2a)}2\Big)+2=q-\chi(2a).
\]
Summing this over nonzero \(a\) cancels the character sum. Including \(a=0\) gives exactly \(q^2\) singular triples. The smooth remainder after the two rank-zero strata is \(q^3-q^2-q(q-1)-(q-1)^2=(q-1)^3\), all of type \((2,2)\).

## Verification and scope

The symbolic argument proves the result for each \(m\). The accompanying Python verifier checks squarefreeness and the census over \(\mathbb F_5\) and \(\mathbb F_{25}\) and tests the Cartier calculation on smooth examples in both fields. The corresponding count vectors, ordered as singular, \((0,4)\), \((0,2)\), \((2,2)\), are \((25,20,16,64)\) and \((625,600,576,13824)\). No isomorphism-class count or Newton-polygon classification is asserted.

## Related results

- *An irreducible 5-rank-zero divisor for genus-four cyclic trigonal curves*, [Resultary, Finding and Cartier/rank proof](https://github.com/Resultary/2026/blob/36a7204b5741b75430355c38bf9bf0ef7468c2a4/2026/11/2/SCOPE-an-irreducible-5-rank-zero-divisor-for-genus-four-cyclic-trigona--97685916466f/RESULT.md), gives the geometric classification for monic quintics. Its polynomial criterion restricts to \(a^6(a^2+b)\), and its superspecial coefficient equations restrict to \(a=0\). Its finite-field census for the full monic-quintic family does not supply the all-extension counts for this fixed slice.
- E. Özman, R. Pries and C. Weir, [arXiv:1907.05684](https://arxiv.org/abs/1907.05684), Theorem 1.2 and Proposition 5.8, give moduli-level results on \(p\)-ranks of cyclic cubic covers, including the relevant genus-four signature. M. Kudo, [arXiv:1804.09063](https://arxiv.org/abs/1804.09063), Theorem 3.1, gives superspecial genus-four examples in characteristic five. These are distinct from counting fixed-coordinate presentations.
- G. Sohn, *The a-number of superelliptic curves of genus four*, DOI `10.23091/japm.2025.059`, is relevant to the geometry; its full text was not inspected, so the extent of its overlap has not been established.
