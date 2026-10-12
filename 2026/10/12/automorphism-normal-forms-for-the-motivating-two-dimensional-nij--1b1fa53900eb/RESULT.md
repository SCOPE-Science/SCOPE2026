# Automorphism normal forms for the motivating two-dimensional Nijenhuis Leibniz example

## Finding

Let \(K\) be any field and let \(L\) have basis \(\{e_1,e_2\}\) with
\[
[e_2,e_1]=[e_2,e_2]=e_1,
\]
and all other basis brackets zero.

A linear map \(N:L\to L\), written as
\[
N=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix},
\]
with columns giving \(N(e_1)\) and \(N(e_2)\), is a Nijenhuis operator exactly when
\[
\boxed{c=0,\qquad (a-d)(a-b-d)=0.}
\]
Thus the Nijenhuis-operator variety is the union of two affine planes,
\[
\mathcal P=\left\{\begin{pmatrix}a&b\\0&a\end{pmatrix}:a,b\in K\right\}
\]
and
\[
\mathcal Q=\left\{\begin{pmatrix}a&a-d\\0&d\end{pmatrix}:a,d\in K\right\},
\]
meeting along the scalar line \(K I_2\).

The automorphism group is
\[
\boxed{
\operatorname{Aut}(L)=
\left\{
\Phi_t=
\begin{pmatrix}
t&t-1\\
0&1
\end{pmatrix}:t\in K^\times
\right\}.
}
\]
For an upper-triangular matrix \(N=\begin{pmatrix}a&b\\0&d\end{pmatrix}\), conjugation is
\[
\Phi_tN\Phi_t^{-1}
=
\begin{pmatrix}
a&t b+(t-1)(d-a)\\
0&d
\end{pmatrix}.
\]
Equivalently, the coordinate
\[
u=b+d-a
\]
transforms by
\[
u\longmapsto t u,
\]
while \(a\) and \(d\) are fixed.

Consequently every Nijenhuis pair \((L,N)\), up to Leibniz-algebra automorphism, has a unique representative of one of the following forms:
\[
\boxed{
Q_{a,d}=
\begin{pmatrix}
a&a-d\\
0&d
\end{pmatrix},
\qquad a,d\in K,
}
\]
or
\[
\boxed{
J_a=
\begin{pmatrix}
a&1\\
0&a
\end{pmatrix},
\qquad a\in K.
}
\]
The scalar maps are exactly \(Q_{a,a}=aI_2\), so these two families do not overlap.

Over \(\mathbf F_q\), the total number of Nijenhuis operators is
\[
\boxed{2q^2-q,}
\]
and the number of automorphism-conjugacy classes is
\[
\boxed{q^2+q.}
\]
More precisely, every \(Q_{a,d}\) is fixed by the whole automorphism group, while each \(J_a\) orbit has size \(q-1\). When \(q=2\), the automorphism group is trivial and therefore all \(q^2+q=6\) classes are singletons.

## Assumptions and scope

The source works over characteristic zero, but the displayed algebra, Nijenhuis equation, automorphism computation, and orbit classification above are valid over every field. The only use of the field hypothesis is that \(c^2=0\) implies \(c=0\), which holds in every field.

The result concerns the specific two-dimensional Leibniz algebra used as the paper's motivating Nijenhuis example. It does not classify Nijenhuis operators on every two-dimensional Leibniz algebra, nor triangular Nijenhuis Leibniz bialgebra structures.

Isomorphism means conjugacy by an automorphism of the fixed Leibniz algebra.

## Proof

For
\[
x=x_1e_1+x_2e_2,
\qquad
y=y_1e_1+y_2e_2,
\]
the bracket is
\[
[x,y]=x_2(y_1+y_2)e_1.
\]

The Nijenhuis condition is
\[
[Nx,Ny]
=N\bigl([Nx,y]+[x,Ny]-N[x,y]\bigr).
\]
Substitution on the four ordered basis pairs gives the polynomial conditions
\[
c^2=0,
\]
\[
c(a-b-d)=0,
\]
and
\[
a^2-ab-2ad+bc+bd+d^2=0.
\]
Because \(K\) is a field, \(c=0\). The remaining quadratic then factors as
\[
a^2-ab-2ad+bd+d^2
=(a-d)(a-b-d).
\]
This proves the two-plane description. It also independently recovers the source's characteristic-zero criterion \(c=0\) with either \(a=d\) or \(a-d=b\).

Now let
\[
\Phi=
\begin{pmatrix}
p&q\\
r&s
\end{pmatrix}
\]
be a Leibniz algebra automorphism. Since
\[
[L,L]=K e_1,
\]
the derived line is characteristic, so \(r=0\). Preservation of
\[
[e_2,e_1]=e_1
\]
gives
\[
s=1,
\]
and preservation of
\[
[e_2,e_2]=e_1
\]
gives
\[
p=q+1.
\]
Invertibility requires \(p\ne0\). Putting \(t=p\) yields the displayed group \(\Phi_t\).

Direct matrix multiplication gives
\[
b' = t b+(t-1)(d-a).
\]
Hence
\[
b'+d-a=t(b+d-a).
\]

On the plane \(\mathcal Q\), one has \(b+d-a=0\), so every point is fixed by every automorphism. On \(\mathcal P\), one has \(a=d\), so \(b\mapsto tb\). Thus \(b=0\) is the scalar point already in \(\mathcal Q\), while all \(b\ne0\) are conjugate to \(b=1\). This proves the normal forms and their uniqueness.

For \(K=\mathbf F_q\), each plane has \(q^2\) points and their intersection has \(q\) scalar points. Therefore
\[
|\operatorname{Nij}(L)|=q^2+q^2-q=2q^2-q.
\]
The fixed plane contributes \(q^2\) conjugacy classes, and the nonzero-\(b\) part of \(\mathcal P\) contributes one class for each \(a\in\mathbf F_q\), hence \(q\) more. Therefore
\[
|\operatorname{Nij}(L)/\operatorname{Aut}(L)|=q^2+q.
\]

## Verification

The included checker `artifacts/verify.py` reconstructs the Nijenhuis torsion equations symbolically from the bracket table, factors the surviving quadratic, derives the automorphism equations symbolically, and verifies the conjugation formula.

It then exhaustively enumerates all linear endomorphisms over
\[
\mathbf F_2,\quad\mathbf F_3,\quad\mathbf F_5,\quad\mathbf F_7,
\]
tests the Nijenhuis identity directly, constructs the full automorphism group, and computes all conjugacy orbits.

For every tested \(q\), it obtains
\[
2q^2-q
\]
operators and
\[
q^2+q
\]
orbits, with the stated normal forms.

The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the arbitrary-field theorem.

## Relationship to prior work

Mondal and Saha introduce and develop Nijenhuis operators on Leibniz algebras. Their Example 2.10 uses exactly the algebra above and solves the raw Nijenhuis equations over \(\mathbb R\), obtaining \(c=0\) and either \(a=d\) or \(a-d=b\). The paper does not quotient that family by automorphisms, does not give normal forms for Nijenhuis pairs, and does not count finite-field points or orbits.

Li, Ma, and Wang study Nijenhuis operators through triangular Leibniz bialgebra structures and classify triangular Leibniz bialgebras in low dimensions. That additional bialgebra structure is not the automorphism quotient of all Nijenhuis operators on the fixed example above.

A 2026 paper on Nijenhuis Leibniz bialgebras states in its abstract that it classifies two-dimensional triangular Nijenhuis Leibniz bialgebras. The accessible abstract concerns bialgebra structures with additional compatibility data, not the full conjugacy quotient of the source's Example 2.10. Because its full classification table was not available in the inspected public material, it remains a bibliographic risk rather than evidence of coverage.

Targeted semantic and web searches for the exact bracket, the source's matrix criterion, automorphism conjugacy, normal forms, and finite-field counts did not locate the quotient theorem above.

## Limitations

The result is a complete automorphism quotient only for this one two-dimensional Leibniz algebra.

It does not classify compatible cobrackets, triangular structures, or Nijenhuis Leibniz bialgebras.

The 2026 triangular Nijenhuis Leibniz bialgebra paper was inspectable only at abstract level; a specialized table in its inaccessible full text could overlap with some operator representatives after forgetting the bialgebra data.

Failed searches do not prove novelty.

## References

1. B. Mondal and R. Saha, “Nijenhuis operators on Leibniz algebras,” arXiv:2306.06428v1, first public 10 June 2023. MSC 2020: 17A30, 17A32, 17A36, 16S80.
2. H. Li, T. Ma, and S. Wang, “When Leibniz algebras are Nijenhuis?”, arXiv:2310.14267v1, 22 October 2023.
3. T. Ma, Y. Sun, and H. Zheng, “Nijenhuis Leibniz bialgebras,” *Communications in Algebra*, published online 7 January 2026, DOI 10.1080/00927872.2025.2602882.
