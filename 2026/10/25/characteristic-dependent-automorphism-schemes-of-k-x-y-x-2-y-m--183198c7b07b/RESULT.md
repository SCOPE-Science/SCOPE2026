# Characteristic-dependent automorphism schemes of \(k[x,y]/(x^2,y^m)\)

## Finding

Let \(k\) be a field of positive characteristic \(p\), let \(m\ge 2\), put \(A_m=k[x,y]/(x^2,y^m)\), and write \(G_m=\underline{\operatorname{Aut}}_k(A_m)\) for the affine group scheme of algebra automorphisms. Then

\[
\dim G_m=\begin{cases}
3m-2,&p>2\text{ and }p\nmid m,\\
3m-1,&p>2\text{ and }p\mid m,\\
3m+\lfloor m/2\rfloor-2,&p=2\text{ and }m\text{ odd},\\
7m/2-1,&p=2\text{ and }m\text{ even}.
\end{cases}
\]

The tangent space at the identity is the derivation space, with dimension

\[
\dim T_eG_m=\dim_k\operatorname{Der}_k(A_m)=\begin{cases}
3m-2,&p>2\text{ and }p\nmid m,\\
3m,&p>2\text{ and }p\mid m,\\
4m-2,&p=2\text{ and }m\text{ odd},\\
4m,&p=2\text{ and }m\text{ even}.
\end{cases}
\]

Consequently, \(G_m\) is smooth over \(k\) exactly when \(p>2\) and \(p\nmid m\). In the nonsmooth cases, the tangent excess \(\dim T_eG_m-\dim G_m\) is respectively \(1\) for odd \(p\mid m\), \(\lceil m/2\rceil\) for \(p=2\) and odd \(m\), and \(m/2+1\) for \(p=2\) and even \(m\).

## Assumptions and scope

The algebra is the finite-dimensional commutative local algebra \(A_m\) with basis \(1,y,\ldots,y^{m-1},x,xy,\ldots,xy^{m-1}\). The assertion concerns the scheme representing automorphisms after arbitrary base change, not only the abstract group of \(k\)-rational automorphisms. Dimensions and smoothness may be checked after extension to an algebraic closure. The case \(m=2\) is included; in odd characteristic its automorphism variety has two components, each of dimension four.

## Proof

Work over an algebraic closure of \(k\). Every geometric automorphism preserves the unique maximal ideal \(\mathfrak m=(x,y)\). Its images therefore have the form

\[
X=a(y)x+f(y),\qquad Y=b(y)x+g(y),
\]

where \(a,b\in k[y]/(y^m)\) and \(f,g\in yk[y]/(y^m)\). Write \(a_0,b_0\) for the constant coefficients of \(a,b\), and \(f_1,g_1\) for the coefficients of \(y\) in \(f,g\). The induced map on \(\mathfrak m/\mathfrak m^2\) is invertible precisely when

\[
 a_0g_1-f_1b_0\ne0.
\]

The defining relations reduce to

\[
X^2=f^2+2xaf=0,\qquad Y^m=g^m+mxb g^{m-1}=0.
\]

Since \(g\in(y)\), one has \(g^m=0\), and since \(g_1\ne0\) whenever the linear part is triangular with nonzero diagonal, \(g^{m-1}=g_1^{m-1}y^{m-1}\).

**Odd characteristic, \(m\ge3\).** The coefficient of \(y^2\) in \(f^2\) is \(f_1^2\), so \(f_1=0\). Invertibility then forces \(a_0,g_1\ne0\); hence \(a(y)\) is a unit. The equation \(2xaf=0\) now gives \(f=0\). The remaining relation is \(m b_0g_1^{m-1}xy^{m-1}=0\). Thus \(b_0=0\) if \(p\nmid m\), while \(b_0\) is free if \(p\mid m\). The free coefficients are: \(m\) coefficients of the unit \(a(y)\), \(m-1\) coefficients of \(g(y)\) with \(g_1\ne0\), and respectively \(m-1\) or \(m\) coefficients of \(b(y)\). These give dimensions \(3m-2\) and \(3m-1\). For \(m=2\), the equations are \(a_0f_1=0\) and \(b_0g_1=0\); invertibility gives a diagonal or antidiagonal linear part. Each of the two open coefficient charts has dimension four, agreeing with \(3m-2\).

**Characteristic two.** Here \(X^2=f^2\). Since squaring is additive, \(f^2=0\) exactly when \(f\in y^{\lceil m/2\rceil}k[y]/(y^m)\), giving \(\lfloor m/2\rfloor\) free coefficients. For \(m\ge3\), this forces \(f_1=0\), so invertibility gives \(a_0,g_1\ne0\). In \(Y^m\), the coefficient of the cross term \(xb g^{m-1}\) is zero when \(m\) is even; when \(m\) is odd, its vanishing is equivalent to \(b_0=0\). Counting coefficients gives \(3m+\lfloor m/2\rfloor-2\) for odd \(m\), and \(7m/2-1\) for even \(m\). At \(m=2\), the same latter count follows directly: all six coefficients of \(a(y),b(y),f(y),g(y)\) are free subject to the open determinant condition.

To compute the tangent space, a first-order automorphism over \(k[\epsilon]/(\epsilon^2)\) has \(x\mapsto x+\epsilon u\) and \(y\mapsto y+\epsilon v\). Linearizing the relations gives exactly

\[
2xu=0,\qquad my^{m-1}v=0.
\]

If \(p\ne2\), the first equation says \(u\in xA_m\), of dimension \(m\). If additionally \(p\nmid m\), the second says \(v\in yA_m\), of dimension \(2m-2\); if \(p\mid m\), it leaves \(v\) arbitrary in the \(2m\)-dimensional algebra. If \(p=2\), the first equation imposes no condition on \(u\), while the second leaves \(v\in yA_m\) for odd \(m\) and leaves \(v\) arbitrary for even \(m\). This proves the stated tangent dimensions. Comparing tangent dimension with scheme dimension yields the excesses above. A group scheme is smooth everywhere if it is smooth at the identity, by translation; a strict tangent excess therefore proves nonsmoothness, while equality gives smoothness at the identity and hence everywhere.

## Verification

The dimension calculation uses explicit coefficient charts for geometric automorphisms; the tangent calculation uses the dual-number definition of derivations. The small boundary case \(m=2\) was handled separately in odd characteristic and checked against both characteristic-two formulas. No finite enumeration is used as a substitute for the proof.

## Relationship to prior work

The closest inspected literature on automorphisms of zero-dimensional monomial algebras explicitly assumes characteristic zero and studies the ordinary linear algebraic automorphism group. A second paper recovering finite monomial algebras from their automorphism groups also states a characteristic-zero hypothesis. Neither result supplies the positive-characteristic group-scheme structure or the tangent-excess formulas proved here. The present calculation is restricted to the natural tensor-product family \(A_m\); it does not claim a criterion for arbitrary monomial algebras.

## Limitations

The result determines the dimension, tangent dimension, and smoothness of \(G_m\), but not a full presentation of its coordinate ring or its group law in every characteristic. No independent verification has been performed, and the literature comparison is not an exhaustive proof of global novelty.

## References

1. R. Díaz, A. Liendo, G. Manzano-Flores, and A. Regeta, *The Automorphism groups of zero-dimensional monomial algebras*, arXiv:2408.02197 (first public version dated 2024-08-05; characteristic-zero scope).
2. R. Díaz and G. Lucchini Arteche, *Finite-dimensional monomial algebras are determined by their automorphism group*, arXiv:2409.15081 (first public version dated 2024-09-23; characteristic-zero scope).
