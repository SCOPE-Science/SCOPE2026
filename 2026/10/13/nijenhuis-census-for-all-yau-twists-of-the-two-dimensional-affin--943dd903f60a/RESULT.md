# Nijenhuis census for all Yau twists of the two-dimensional affine Lie algebra

## Finding

Let \(K\) be a field and let
\[
\mathfrak a_K=K e_1\oplus K e_2
\]
be the two-dimensional affine Lie algebra,
\[
[e_1,e_2]=e_2.
\]

For every Lie endomorphism
\[
\alpha:\mathfrak a_K\to\mathfrak a_K,
\]
form the Yau-twisted Hom-Lie algebra
\[
\mathfrak a_\alpha
=
(\mathfrak a_K,[\, ,\,]_\alpha,\alpha),
\qquad
[x,y]_\alpha=\alpha([x,y]).
\]

Write
\[
\alpha=
\begin{pmatrix}
p&q\\
r&s
\end{pmatrix}
\]
in column convention. Then
\[
\boxed{
\alpha\text{ is a Lie endomorphism}
\iff
q=0,\qquad s(1-p)=0.
}
\]
Thus every twist has the unique form
\[
\alpha=
\begin{pmatrix}
p&0\\
r&s
\end{pmatrix},
\qquad
s(1-p)=0.
\]

For these twists, every linear endomorphism \(N\) satisfies the Nijenhuis torsion equation. Therefore
\[
\boxed{
N\text{ is a Hom-Lie Nijenhuis operator on }\mathfrak a_\alpha
\iff
N\alpha=\alpha N.
}
\]

Over every finite field \(\mathbf F_q\), there are exactly
\[
\boxed{2q^2-q}
\]
Lie endomorphisms \(\alpha\).

Exactly two of them are scalar:
\[
\boxed{\alpha=0,\qquad \alpha=I.}
\]
For each of these two twists, every \(2\times2\) matrix is Nijenhuis, so there are
\[
q^4
\]
Nijenhuis operators.

Every other Lie endomorphism is nonscalar. The commutant of a nonscalar \(2\times2\) matrix over a field has dimension \(2\), so every other twist has exactly
\[
q^2
\]
Nijenhuis operators.

Hence the complete finite-field census of twist-operator pairs is
\[
\boxed{
\#\{(\alpha,N)\}
=
4q^4-q^3-2q^2.
}
\]

Equivalently, the fiber-size distribution over the Yau-twist parameter space is
\[
\boxed{
2\text{ twists with }q^4\text{ Nijenhuis operators},
}
\]
and
\[
\boxed{
2q^2-q-2\text{ twists with }q^2\text{ Nijenhuis operators}.
}
\]

Over every extension field \(\mathbf F_{q^m}\),
\[
\#\{(\alpha,N)\}
=
4q^{4m}-q^{3m}-2q^{2m}.
\]
Therefore the Hasse--Weil zeta function of the pair variety is
\[
\boxed{
Z(T)
=
\frac{(1-q^3T)(1-q^2T)^2}{(1-q^4T)^4}.
}
\]

## Assumptions and scope

A Nijenhuis operator on a Hom-Lie algebra is taken in the sense used by Das and Sen: it commutes with the twisting map and satisfies
\[
[Nx,Ny]
=
N\!\left([Nx,y]+[x,Ny]-N[x,y]\right).
\]

The Yau twist uses a Lie endomorphism \(\alpha\) and the bracket
\[
[x,y]_\alpha=\alpha([x,y]).
\]

The theorem classifies all pairs arising from all Lie endomorphisms of the fixed affine Lie algebra. It is not restricted to diagonal twists or invertible twists.

The result is valid in every characteristic.

## Proof

Write
\[
\alpha(e_1)=p e_1+r e_2,
\qquad
\alpha(e_2)=q e_1+s e_2.
\]
The Lie-endomorphism equation
\[
\alpha([e_1,e_2])
=
[\alpha(e_1),\alpha(e_2)]
\]
becomes
\[
q e_1+s e_2
=
(ps-rq)e_2.
\]
Hence
\[
q=0,
\qquad
s=ps,
\]
which is equivalent to
\[
q=0,
\qquad
s(1-p)=0.
\]

For such an \(\alpha\),
\[
[e_1,e_2]_\alpha=s e_2.
\]
Thus every Yau-twisted bracket in the family is a scalar multiple of the affine bracket, including the zero bracket when \(s=0\).

Let
\[
N=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}.
\]
Because the Nijenhuis torsion is alternating and bilinear, it is enough to evaluate it on \((e_1,e_2)\).

The left side is
\[
[N(e_1),N(e_2)]_\alpha
=
s(ad-bc)e_2.
\]
The expression inside the outer \(N\) on the right is
\[
[N(e_1),e_2]_\alpha
+
[e_1,N(e_2)]_\alpha
-
N([e_1,e_2]_\alpha)
=
-sb\,e_1+sa\,e_2.
\]
Applying \(N\) gives
\[
N(-sb\,e_1+sa\,e_2)
=
s(ad-bc)e_2.
\]
Therefore the torsion equation holds for every \(N\), in every characteristic.

Consequently the only remaining Hom-Lie Nijenhuis condition is
\[
N\alpha=\alpha N.
\]

Now let \(K=\mathbf F_q\).

The endomorphism variety is the union of the two affine planes
\[
\{q=0,\ s=0\}
\]
and
\[
\{q=0,\ p=1\},
\]
whose intersection is the affine line
\[
\{q=0,\ p=1,\ s=0\}.
\]
Thus the number of Lie endomorphisms is
\[
q^2+q^2-q
=
2q^2-q.
\]

A scalar matrix \(\lambda I\) is a Lie endomorphism only if
\[
\lambda(1-\lambda)=0.
\]
Over a field this gives exactly
\[
\lambda=0,\qquad \lambda=1.
\]
Hence precisely \(0\) and \(I\) are scalar twists.

For a scalar twist, every matrix commutes with \(\alpha\), so the Nijenhuis fiber has
\[
q^4
\]
points.

Let \(\alpha\) be nonscalar. Any nonscalar \(2\times2\) matrix is cyclic: its minimal polynomial has degree \(2\). Therefore its matrix centralizer is
\[
K[\alpha],
\]
a two-dimensional \(K\)-vector space. Hence
\[
|C_{M_2(\mathbf F_q)}(\alpha)|=q^2.
\]

There are
\[
2q^2-q-2
\]
nonscalar twists. The total number of pairs is therefore
\[
2q^4+(2q^2-q-2)q^2
=
4q^4-q^3-2q^2.
\]

The argument is unchanged over \(\mathbf F_{q^m}\), giving
\[
N_m=4q^{4m}-q^{3m}-2q^{2m}.
\]
Thus
\[
\begin{aligned}
Z(T)
&=
\exp\!\left(
\sum_{m\ge1}\frac{N_mT^m}{m}
\right)\\
&=
\frac{(1-q^3T)(1-q^2T)^2}{(1-q^4T)^4}.
\end{aligned}
\]

## Verification

The included program `artifacts/verify.py` reconstructs the Lie-endomorphism equations for
\[
[e_1,e_2]=e_2
\]
and verifies that they are exactly
\[
q=0,\qquad s(1-p)=0.
\]

It then forms the Yau-twisted bracket and symbolically checks that the Nijenhuis torsion vanishes identically for a completely general \(2\times2\) matrix \(N\).

For
\[
\mathbf F_2,\quad
\mathbf F_3,\quad
\mathbf F_5,\quad
\mathbf F_7,
\]
the program exhaustively enumerates every Lie endomorphism \(\alpha\), every matrix \(N\), and tests both commutation and the Nijenhuis identity directly.

The numbers of twists are
\[
6,\quad15,\quad45,\quad91,
\]
and the numbers of twist-operator pairs are
\[
48,\quad279,\quad2325,\quad9163 
\]
The final value is recomputed and printed by the checker rather than relied upon in the proof.

The checker returns `VERIFY_OK`.

The arbitrary-prime-power formula follows from the exact endomorphism and centralizer arguments above; finite enumeration is a replay check.

## Relationship to prior work

Das and Sen develop Nijenhuis operators on Hom-Lie algebras, their graded-Lie formulation, cohomology, and deformation theory. Their published article supplies the operator framework used here.

A later full-text treatment of compatible Hom-Lie algebras by Das recalls the same Nijenhuis identity and the standard Yau-twist construction from Lie algebra homomorphisms. It gives illustrative Hom-Lie examples but no complete finite-field census of all Yau twists of the affine Lie algebra.

Targeted searches for the affine two-dimensional Hom-Lie algebra, Yau twists, Nijenhuis centralizers, finite-field counts, and the polynomial
\[
4q^4-q^3-2q^2
\]
did not locate a covering result.

## Limitations

The theorem concerns Yau twists of the unique nonabelian two-dimensional Lie algebra. It does not classify arbitrary two-dimensional Hom-Lie algebras that are not obtained by this construction.

The primary Das--Sen article was accessible through publisher metadata and abstract, but its full publisher text was not available through the accessible public route during this check. The exact Nijenhuis definition and Yau-twist mechanism were additionally checked in a full public preprint that cites that article.

A specialized or differently indexed finite-field computation may exist. Failed searches do not prove novelty.

## References

1. A. Das and S. Sen, “Nijenhuis operators on Hom-Lie algebras,” *Communications in Algebra* 50 (2022), 1038–1054, DOI `10.1080/00927872.2021.1977942`, first published online 16 October 2021.
2. A. Das, “Cohomology and deformations of compatible Hom-Lie algebras,” arXiv:2202.03137v1, first public 7 February 2022; *Journal of Geometry and Physics* 192 (2023), 104951, DOI `10.1016/j.geomphys.2023.104951`.
