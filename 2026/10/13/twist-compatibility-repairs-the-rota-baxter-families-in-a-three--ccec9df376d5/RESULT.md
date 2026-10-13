# Twist compatibility repairs the Rota–Baxter families in a three-dimensional BiHom-Lie example

## Finding

Let \(K\) be a field of characteristic different from \(2\), and let
\[
A=A_{\bar 0}\oplus A_{\bar 1},
\qquad
A_{\bar 0}=\langle e_1,e_2\rangle,
\qquad
A_{\bar 1}=\langle e_3\rangle,
\]
with
\[
[e_1,e_2]=e_1,
\qquad
[e_1,e_3]=[e_2,e_3]=[e_3,e_3]=0.
\]
Let \(\gamma,\lambda\in K^\times\), and define
\[
\alpha(e_1)=\gamma e_1,\qquad
\alpha(e_2)=e_2,\qquad
\alpha(e_3)=\lambda e_3,
\]
\[
\beta(e_1)=\gamma e_1,\qquad
\beta(e_2)=e_2,\qquad
\beta(e_3)=-\lambda e_3.
\]

This is the BiHom-Lie superalgebra of Example 1.1 in Ncib.

Definition 1.3(3) first defines an \(\mathcal O\)-operator by requiring
\[
\alpha R=R\alpha,\qquad
\beta R=R\beta,
\]
together with its operator identity, and then calls the adjoint special case a Rota–Baxter operator. Reading the Rota–Baxter notion as that stated special case, the complete weight-zero classification is as follows.

Every even linear map has the form
\[
R(e_1)=a e_1+b e_2,\qquad
R(e_2)=c e_1+d e_2,\qquad
R(e_3)=f e_3.
\]
It is a weight-zero Rota–Baxter operator exactly when
\[
\boxed{
a^2+bc=0,\qquad
b(a+d)=0,\qquad
(\gamma-1)b=0,\qquad
(\gamma-1)c=0.
}
\]

If
\[
\gamma=1,
\]
the source's two product-identity families are complete:
\[
\boxed{
R(e_1)=0,\qquad
R(e_2)=c e_1+d e_2,\qquad
R(e_3)=f e_3,
}
\]
or, for \(b\ne0\),
\[
\boxed{
R(e_1)=a e_1+b e_2,\qquad
R(e_2)=-\frac{a^2}{b}e_1-ae_2,\qquad
R(e_3)=f e_3.
}
\]

If
\[
\gamma\ne1,
\]
twist compatibility removes every off-diagonal even coefficient, and the full family collapses to
\[
\boxed{
R(e_1)=0,\qquad
R(e_2)=d e_2,\qquad
R(e_3)=f e_3.
}
\]

Consequently, the first family printed in Example 1.1,
\[
R_1(e_1)=0,\qquad
R_1(e_2)=a_1e_1+a_2e_2,\qquad
R_1(e_3)=c_1e_3,
\]
satisfies the complete definition only if
\[
\boxed{(\gamma-1)a_1=0.}
\]
The second printed family has a coefficient \(b_2\) in a denominator, hence \(b_2\ne0\); twist compatibility then forces
\[
\boxed{\gamma=1.}
\]
Thus for every \(\gamma\ne1\), the entire printed second family fails the twist-commutation requirement.

As a finite-field consequence, let \(q\) be odd and fix \(\lambda\in\mathbf F_q^\times\). Then
\[
\boxed{
\#\operatorname{RB}_0(A_{\gamma,\lambda})=
\begin{cases}
2q^3-q^2,&\gamma=1,\\[1mm]
q^2,&\gamma\ne1.
\end{cases}}
\]
Summing over all nonzero parameters gives
\[
\boxed{
\#\{(\gamma,\lambda,R)\}
=
3q^2(q-1)^2.
}
\]

## Assumptions and scope

Ncib works over a characteristic-zero field. The correction to the published example already holds in that setting.

The finite-field corollary is stated only in odd characteristic. The same multiplication, grading, and twist formulas satisfy the required identities there, and the classification proof below is purely algebraic.

The phrase “Rota–Baxter operator” is interpreted exactly through Definition 1.3(3): a Rota–Baxter operator is introduced as the adjoint special case of an \(\mathcal O\)-operator, whose preceding equation (1.9) requires commutation with both twisting maps.

The parameter \(\lambda\) is nonzero because the example assumes regular twisting maps. It does not enter the final operator equations because the odd line is central and every even operator acts on that line by a scalar.

## Proof

Because \(R\) is even, write
\[
R(e_1)=a e_1+b e_2,\qquad
R(e_2)=c e_1+d e_2,\qquad
R(e_3)=f e_3.
\]

On the even subspace the twisting maps both restrict to
\[
\operatorname{diag}(\gamma,1).
\]
Hence
\[
R\alpha-\alpha R
=
\begin{pmatrix}
0&(1-\gamma)c&0\\
(\gamma-1)b&0&0\\
0&0&0
\end{pmatrix}.
\]
The equation for \(\beta\) gives the same even constraints. Thus twist compatibility is exactly
\[
(\gamma-1)b=0,\qquad
(\gamma-1)c=0.
\]

The odd line is central, so every Rota–Baxter defect involving \(e_3\) vanishes.

The bracket on the even subspace is
\[
[xe_1+ye_2,\;ue_1+ve_2]=(xv-yu)e_1.
\]
For the pair \((e_1,e_2)\), the weight-zero Rota–Baxter defect is
\[
[R(e_1),R(e_2)]
-
R\!\left([R(e_1),e_2]+[e_1,R(e_2)]\right).
\]
Its two even coordinates are
\[
-(a^2+bc),\qquad
-b(a+d).
\]
The reversed ordered pair gives the negatives, and the equal-input pairs give zero. Therefore the product identity is equivalent to
\[
a^2+bc=0,\qquad
b(a+d)=0.
\]

Suppose first that
\[
\gamma=1.
\]
There are no additional twist restrictions. If \(b=0\), then
\[
a^2=0,
\]
so \(a=0\), while \(c,d,f\) are arbitrary. This is the first family.

If \(b\ne0\), then
\[
d=-a,\qquad
c=-\frac{a^2}{b},
\]
while \(f\) is arbitrary. This is the second family.

Now suppose
\[
\gamma\ne1.
\]
Twist compatibility gives
\[
b=c=0.
\]
The product equation then yields
\[
a^2=0,
\]
hence \(a=0\). Only
\[
d,\ f
\]
remain free.

For the finite-field count with \(\gamma=1\), the \(b=0\) branch has
\[
q^3
\]
operators. The \(b\ne0\) branch has
\[
q(q-1)q=q^2(q-1)
\]
operators, corresponding to free \(a\), nonzero \(b\), and free \(f\). Thus
\[
q^3+q^2(q-1)=2q^3-q^2.
\]

For each \(\gamma\ne1\), only \(d,f\) are free, giving
\[
q^2
\]
operators.

There are \(q-1\) choices of nonzero \(\lambda\). Therefore, over all nonzero \((\gamma,\lambda)\),
\[
(q-1)(2q^3-q^2)+(q-2)(q-1)q^2
=
3q^2(q-1)^2.
\]

## Verification

The included program `artifacts/verify.py` reconstructs the twist commutators and the Rota–Baxter defect from the displayed basis formulas.

Symbolically it obtains exactly
\[
(\gamma-1)b,\qquad
(\gamma-1)c,\qquad
a^2+bc,\qquad
b(a+d).
\]

It separately substitutes both families printed in Example 1.1. The first has twist defect proportional to
\[
(\gamma-1)a_1,
\]
while the second, because its denominator coefficient is nonzero, has a nonzero off-diagonal twist defect whenever
\[
\gamma\ne1.
\]

The checker then exhaustively enumerates every even endomorphism for all nonzero \(\gamma,\lambda\) over
\[
\mathbf F_3,\qquad
\mathbf F_5,\qquad
\mathbf F_7.
\]
For fixed \(\lambda\), it obtains
\[
2q^3-q^2
\]
operators at \(\gamma=1\) and
\[
q^2
\]
at every \(\gamma\ne1\). The total parameter-operator counts are
\[
108,\qquad1200,\qquad5292,
\]
agreeing with
\[
3q^2(q-1)^2.
\]

The script returns `VERIFY_OK`.

Finite enumeration is a replay check. The arbitrary-field classification follows from the exact symbolic equations above.

## Relationship to prior work

Ncib's paper introduces \(\mathcal O\)-operators and Rota–Baxter operators for BiHom-Lie superalgebras. Equation (1.9) requires an \(\mathcal O\)-operator to commute with both twists, and the paper then defines a Rota–Baxter operator as the adjoint special case.

Example 1.1 uses exactly the algebra above and prints two families as “the Rota-Baxter operators of weight zero.” Those families solve the Rota–Baxter product identity, but the printed parameter ranges do not enforce equation (1.9). The correction here is the complete simultaneous solution of both requirements.

Focused searches for the article identifier, Example 1.1, the displayed families, twist commutation, corrections, and errata did not locate a published repair. Semantic searches for the same BiHom-Lie example likewise returned no covering result.

The earlier literature on Rota–Baxter operators on ordinary pre-Lie superalgebras does not contain the two-twist compatibility condition and therefore does not imply this repair.

## Limitations

The result concerns the specific three-dimensional BiHom-Lie superalgebra in Example 1.1.

The correction depends on interpreting “Rota–Baxter operator” as the adjoint special case of the \(\mathcal O\)-operator defined immediately before it, including equation (1.9). This is the literal structural dependency in Definition 1.3(3); a convention that intentionally discarded (1.9) would instead define a weaker product-identity notion.

The finite-field statement is restricted to odd characteristic and nonzero twisting parameters.

An unindexed correction or author note may exist. Failed searches do not prove absolute novelty.

## References

1. O. Ncib, “BiHom pre-Lie Superalgebras and Related Structures,” arXiv:1910.13863v1, first public 28 October 2019; *Hacettepe Journal of Mathematics and Statistics* 51 (2022), 1385–1402, DOI `10.15672/hujms.1035821`.
2. E. Abdaoui, S. Mabrouk, and A. Makhlouf, “Rota-Baxter operators on Pre-Lie Superalgebras,” *Bulletin of the Malaysian Mathematical Sciences Society* 42 (2019), 1567–1606.
