# Reynolds operators on the canonical two-dimensional Hom–Lie triple example

## Finding

Let \(K\) be a field with \(\operatorname{char}K\ne2\). Let \(L_K\) have basis
\[
\{e_1,e_2\},
\]
twist
\[
\alpha(e_1)=e_1,\qquad \alpha(e_2)=-e_2,
\]
and sole nonzero basic triple products
\[
[e_1,e_2,e_2]=e_1,\qquad [e_2,e_1,e_2]=-e_1.
\]

A Reynolds operator is a linear map \(T:L_K\to L_K\) satisfying
\[
T\alpha=\alpha T
\]
and
\[
[Tx,Ty,Tz]
=
T\!\left([Tx,Ty,z]+[x,Ty,Tz]+[Tx,y,Tz]-[Tx,Ty,Tz]\right).
\]

Writing
\[
T=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\]
twist commutation gives
\[
\alpha T-T\alpha
=
\begin{pmatrix}0&2b\\-2c&0\end{pmatrix},
\]
hence \(b=c=0\). The complete remaining Reynolds equation is
\[
\boxed{a^2d(d-2)=0.}
\]

Therefore
\[
\boxed{
\operatorname{Rey}(L_K)=
\{\operatorname{diag}(0,d):d\in K\}
\cup
\{\operatorname{diag}(a,0):a\in K\}
\cup
\{\operatorname{diag}(a,2):a\in K\}.
}
\]

For every odd prime power \(q\),
\[
\boxed{|\operatorname{Rey}(L_{\mathbf F_q})|=3q-2.}
\]
The rank distribution is
\[
\boxed{(1,\ 2q-2,\ q-1)}
\]
in ranks \(0,1,2\). Thus the invertible Reynolds operators are exactly
\[
\operatorname{diag}(a,2),\qquad a\ne0.
\]

The full Hom–Lie triple automorphism group is
\[
\boxed{
\operatorname{Aut}(L_K)=
\{\operatorname{diag}(s,\varepsilon):s\in K^\times,\ \varepsilon^2=1\}.
}
\]
Hence over every odd finite field all Reynolds operators are fixed under automorphism conjugacy, so there are exactly \(3q-2\) conjugacy classes.

Over every extension field,
\[
N_m=3q^m-2,
\]
and the zeta function of the reduced solution set is
\[
\boxed{
Z(T)=\frac{(1-T)^2}{(1-qT)^3}.
}
\]

## Assumptions and scope

Xiao, Teng, and Long give this two-dimensional Hom–Lie triple system as their first concrete example and later specialize generalized Reynolds operators to Reynolds operators for the adjoint representation. Their paper assumes characteristic \(0\).

The theorem above extends this particular calculation to every field of characteristic different from \(2\). Characteristic \(2\) is excluded because the twist eigenvalues \(1\) and \(-1\) coincide.

The zeta function concerns the reduced set of field-valued solutions. No scheme-theoretic statement about the nonreduced equation \(a^2d(d-2)=0\) is claimed.

## Proof

For
\[
x=x_1e_1+x_2e_2,\quad
y=y_1e_1+y_2e_2,\quad
z=z_1e_1+z_2e_2,
\]
the bracket is
\[
[x,y,z]=(x_1y_2-x_2y_1)z_2e_1.
\]

The displayed twist is multiplicative. The Hom–Lie triple identities are multilinear and are verified on all basis tuples by the packaged symbolic checker.

Let
\[
T=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
\]
The commutation equation is
\[
\alpha T-T\alpha
=
\begin{pmatrix}0&2b\\-2c&0\end{pmatrix}.
\]
Since \(2\) is invertible, \(b=c=0\).

Thus
\[
T(e_1)=ae_1,\qquad T(e_2)=de_2.
\]
Substitution in the Reynolds identity on \((e_1,e_2,e_2)\) gives
\[
a^2d(d-2)e_1=0.
\]
Every other basis triple yields zero or the negative of this equation. Hence the equation is complete.

Over a field, \(a^2d(d-2)=0\) is equivalent to
\[
a=0,\qquad d=0,\qquad\text{or}\qquad d=2,
\]
which gives the three affine lines.

Over \(\mathbf F_q\), each line has \(q\) points. Their only intersections are
\[
\{0\}
\quad\text{and}\quad
\{\operatorname{diag}(0,2)\},
\]
so the total is \(3q-2\). Only the \(q-1\) points \(\operatorname{diag}(a,2)\) with \(a\ne0\) have rank \(2\); all other nonzero points have rank \(1\).

For automorphisms, commuting with \(\alpha\) forces
\[
P=\operatorname{diag}(s,t).
\]
Bracket preservation gives
\[
[se_1,te_2,te_2]=st^2e_1=P(e_1)=se_1,
\]
so \(t^2=1\). Every such automorphism is diagonal and therefore centralizes every Reynolds operator.

Finally,
\[
N_m=3q^m-2,
\]
so
\[
\exp\!\left(\sum_{m\ge1}\frac{N_mT^m}{m}\right)
=
\frac{(1-T)^2}{(1-qT)^3}.
\]

## Verification

The included `artifacts/verify.py` reconstructs the triple product, twist, Hom–Lie triple identities, twist-commutation equation, Reynolds defect, automorphisms, finite-field ranks, and conjugacy action.

It exhaustively checks every \(2\times2\) matrix over
\[
\mathbf F_3,\quad \mathbf F_5,\quad \mathbf F_7,\quad \mathbf F_{11}.
\]
The operator totals are
\[
7,\quad13,\quad19,\quad31,
\]
with rank profiles
\[
(1,4,2),\quad(1,8,4),\quad(1,12,6),\quad(1,20,10).
\]
Every automorphism-conjugacy orbit is singleton.

The checker returns `VERIFY_OK`.

Finite enumeration is replay evidence. The arbitrary-field theorem follows from the symbolic proof above.

## Relationship to prior work

Xiao, Teng, and Long provide both ingredients of this result: the concrete two-dimensional Hom–Lie triple system and the Reynolds identity. Their inspected full text develops the general graph, cohomology, deformation, and Hom-NS-Lie triple theory, but does not classify all Reynolds endomorphisms of the concrete example.

Teng and Jin study weighted \(\mathcal O\)-operators on Hom–Lie triple systems. Their defining identity contains a weighted source triple product and is different from the Reynolds identity used here.

Focused searches for the exact two-dimensional object, Reynolds operators, diagonal classifications, finite-field counts, and the polynomial \(3q-2\) did not locate a covering result.

## Limitations

Characteristic \(2\) is excluded.

The theorem treats only the two-dimensional example displayed by the primary source.

A differently indexed thesis or short note may contain the same elementary classification. Failed searches do not prove absolute novelty.

## References

1. Y. Xiao, W. Teng, and F. Long, “Generalized Reynolds Operators on Hom-Lie Triple Systems,” Preprints 2024, DOI `10.20944/preprints202401.0052.v1`, first public 2 January 2024; peer-reviewed in *Symmetry* 16 (2024), 262, DOI `10.3390/sym16030262`.
2. W. Teng and J. Jin, “Weighted \(\mathcal O\)-operators on Hom-Lie triple systems,” arXiv:2310.13728v1, first public 21 October 2023.
