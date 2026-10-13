# Corrected Rota–Baxter locus for the three-dimensional Zinbiel algebra \\(A_2\\)
## Finding
Let \\(K\\) be a field and let \\(A_2(K)\\) have basis \\(\\{e_1,e_2,e_3\\}\\) with sole nonzero product
\\[
e_1e_1=e_3.
\\]
A weight-zero Rota–Baxter operator satisfies
\\[
R(x)R(y)=R\\bigl(R(x)y+xR(y)\\bigr)
\\]
for all \\(x,y\\in A_2(K)\\).

Write, in the column convention used in Gao–Ni–Yu,
\\[
R=
\\begin{pmatrix}
a&u&v\\\\
b&c&d\\\\
e&f&g
\\end{pmatrix}.
\\]
Then the complete Rota–Baxter locus over every field is
\\[
\\boxed{u=v=0,\\qquad 2ad=0,\\qquad a(a-2g)=0.}
\\]

Thus, when \\(\\operatorname{char}K\\ne2\\), there are exactly two strata:
\\[
\\boxed{a=0}
\\]
with \\(b,c,d,e,f,g\\) arbitrary, and
\\[
\\boxed{a\\ne0,\\qquad d=0,\\qquad g=a/2}
\\]
with \\(b,c,e,f\\) arbitrary.

This corrects Table 1 of Gao–Ni–Yu for the algebra \\(A_2\\). Their nonzero-\\(r_{11}\\) family prints \\(r_{23}\\) as a free parameter, but the Rota–Baxter equation forces
\\[
\\boxed{r_{23}=0.}
\\]
A concrete printed-family counterexample is
\\[
R=
\\begin{pmatrix}
1&0&0\\\\
0&0&1\\\\
0&0&1/2
\\end{pmatrix}.
\\]
It has
\\[
R(e_1)=e_1,
\\qquad
R(e_3)=e_2+\\tfrac12e_3.
\\]
For \\(x=y=e_1\\), the left side of the Rota–Baxter identity is \\(e_3\\), whereas the right side is
\\[
R(2e_3)=2e_2+e_3,
\\]
so the identity fails.

In characteristic \\(2\\), the equation \\(a(a-2g)=a^2=0\\) forces \\(a=0\\), so only the first stratum survives.

Over \\(\\mathbf F_q\\), this gives
\\[
\\boxed{
|\\operatorname{RB}(A_2(\\mathbf F_q))|=
\\begin{cases}
q^6,&q\\text{ even},\\\\
q^6+(q-1)q^4=q^4(q^2+q-1),&q\\text{ odd}.
\\end{cases}}
\\]

The rank distribution sharpens the count. For even \\(q\\), the multiplicities for ranks \\(0,1,2,3\\) are
\\[
\\boxed{
1,\\quad (q+1)(q^3-1),\\quad (q^3-1)(q^3-q),\\quad0.
}
\\]
For odd \\(q\\), they are
\\[
\\boxed{
1,\\quad (q+1)(q^3-1),\\quad (q^3-1)(q^3-q)+q^3(q-1),\\quad q^3(q-1)^2.
}
\\]
In particular, invertible Rota–Baxter operators exist exactly in odd characteristic in this finite-field family, and their number is \\(q^3(q-1)^2\\).

## Assumptions and scope
The multiplication is exactly the \\(A_2\\) algebra in Gao–Ni–Yu's three-dimensional Zinbiel list. The matrix convention is their stated convention: the \\(j\\)-th column gives \\(R(e_j)\\).

The published paper works over \\(\\mathbb C\\). The corrected polynomial equations above are derived directly from the defining identity and therefore make sense over any field. The finite-field statements are consequences of those equations, not a specialization of the erroneous table entry.

The claim concerns weight zero only and only this one three-dimensional Zinbiel algebra.

## Proof
For vectors \\(x=(x_1,x_2,x_3)^T\\) and \\(y=(y_1,y_2,y_3)^T\\), multiplication is
\\[
xy=x_1y_1e_3.
\\]
Let the first coordinates of \\(R(e_1),R(e_2),R(e_3)\\) be \\(a,u,v\\).

Applying the Rota–Baxter identity to \\((e_2,e_2)\\) gives
\\[
u^2e_3=0,
\\]
so \\(u=0\\). Applying it to \\((e_3,e_3)\\) gives \\(v^2e_3=0\\), hence \\(v=0\\).

Now the only possible nonzero first coordinate among the three images is \\(a\\). For \\((e_1,e_1)\\),
\\[
R(e_1)R(e_1)=a^2e_3,
\\]
while
\\[
R\\bigl(R(e_1)e_1+e_1R(e_1)\\bigr)
=R(2ae_3)
=2a(de_2+ge_3),
\\]
because the first coordinate of \\(R(e_3)\\) is already zero. Equality is therefore equivalent to
\\[
2ad=0,
\\qquad
a^2=2ag.
\\]
Every other ordered basis pair gives zero on both sides once \\(u=v=0\\). This proves the complete polynomial system.

If the characteristic is not \\(2\\), either \\(a=0\\), or \\(a\\ne0\\) and then
\\[
d=0,
\\qquad
g=a/2.
\\]
If the characteristic is \\(2\\), then \\(a^2=0\\), so \\(a=0\\).

For the finite-field count, the \\(a=0\\) stratum has six free parameters and contributes \\(q^6\\). In odd characteristic, the nonzero \\(a\\) stratum has \\(q-1\\) choices for \\(a\\) and four further free parameters, hence contributes \\((q-1)q^4\\).

For ranks on the \\(a=0\\) stratum, the first row is zero and the lower \\(2\\times3\\) block is arbitrary. The standard rank count for a \\(2\\times3\\) matrix over \\(\\mathbf F_q\\) is
\\[
1
\\]
of rank \\(0\\),
\\[
(q+1)(q^3-1)
\\]
of rank \\(1\\), and
\\[
(q^3-1)(q^3-q)
\\]
of rank \\(2\\).

On the odd-characteristic nonzero stratum, row operations reduce the matrix to
\\[
\\begin{pmatrix}
a&0&0\\\\
0&c&0\\\\
0&f&a/2
\\end{pmatrix}.
\\]
Thus the operator has rank \\(2\\) exactly when \\(c=0\\), giving \\(q^3(q-1)\\) operators, and rank \\(3\\) exactly when \\(c\\ne0\\), giving \\(q^3(q-1)^2\\). Adding the strata yields the stated distribution.

## Verification
The included program `artifacts/verify.py` reconstructs the Rota–Baxter defect from the multiplication table and symbolically checks that the complete ideal is generated, over a field, by
\\[
u,
\\qquad
v,
\\qquad
2ad,
\\qquad
a(a-2g).
\\]

It checks the explicit counterexample to the printed nonzero-\\(r_{11}\\) family over \\(\\mathbb Q\\).

It then exhaustively enumerates every linear endomorphism over \\(\\mathbf F_2\\) and \\(\\mathbf F_3\\). The direct counts are
\\[
64
\\]
and
\\[
891,
\\]
respectively, agreeing with the closed formulas. The rank histograms also agree exactly with the displayed formulas.

The program returns `VERIFY_OK`.

Finite enumeration is a replay check; the arbitrary-field classification is proved symbolically above.

## Relationship to prior work
Gao, Ni, and Yu define weight-zero Rota–Baxter operators on Zinbiel algebras, state the column matrix convention, and claim a complete list for all two- and three-dimensional complex Zinbiel algebras. Their Table 1 includes \\(A_2:e_1e_1=e_3\\).

For the branch with \\(r_{11}\\ne0\\), the printed matrix leaves \\(r_{23}\\) free while fixing \\(r_{33}=r_{11}/2\\). Direct substitution into the defining identity shows that this is too large: the same \\((e_1,e_1)\\) equation also forces \\(r_{23}=0\\).

Focused searches for the article title together with correction, erratum, \\(A_2\\), \\(r_{23}\\), and Rota–Baxter terminology did not locate a published correction or an equivalent corrected table. The exact finite-field count and rank distribution were likewise not located.

The two-dimensional algebra \\(T_2:e_1e_1=e_2\\) from the same paper is a different object and is not part of this claim.

## Limitations
The correction concerns only the \\(A_2\\) row of the three-dimensional table. No statement is made here about the accuracy of the other rows.

The source paper is complex-field work; the positive-characteristic extension here follows from a fresh derivation of the defining equations.

Search noncoverage does not prove that no independent correction exists in unindexed literature.

## References
1. J. Gao, J. Ni, and J. Yu, “Some Results on Zinbiel Algebras and Rota–Baxter Operators,” *Axioms* 13 (2024), 314, DOI `10.3390/axioms13050314`.
