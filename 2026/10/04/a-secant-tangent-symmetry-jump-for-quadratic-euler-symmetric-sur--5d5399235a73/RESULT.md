# A secant–tangent symmetry jump for quadratic Euler-symmetric surfaces
## Finding
Let \(W=\mathbf C^2\) and let
\[
U\subset\operatorname{Sym}^2W^*
\]
have dimension \(2\). Put
\[
S=\mathbf C\oplus W^*\oplus U.
\]
The line
\[
\mathbf P(U)\subset\mathbf P(\operatorname{Sym}^2W^*)\cong\mathbf P^2
\]
meets the discriminant conic of rank-one binary quadrics in a length-\(2\) scheme. There are exactly two \(\operatorname{GL}(W)\)-orbits.

In the secant orbit one may take
\[
U_{\mathrm{sec}}=\langle X^2,Y^2\rangle.
\]
The Euler-symmetric surface is
\[
Z_{\mathrm{sec}}
=
V(ta-x^2,\;tb-y^2)
\subset\mathbf P^4_{[t:x:y:a:b]}.
\]
It is a degree-\(4\) nonnormal complete intersection, and
\[
\dim\mathfrak{aut}(\widehat Z_{\mathrm{sec}})=5.
\]
For the Euler weights
\[
(0,1,1,2,2)
\]
on \((t,x,y,a,b)\), its infinitesimal linear automorphism algebra has weight dimensions
\[
3\ \text{in weight }0,\qquad 2\ \text{in weight }1.
\]

In the tangent orbit one may take
\[
U_{\mathrm{tan}}=\langle X^2,XY\rangle.
\]
The Euler-symmetric surface is
\[
Z_{\mathrm{tan}}
=
V(ta-x^2,\;tb-xy,\;xb-ay)
\subset\mathbf P^4.
\]
This is the smooth rational normal cubic scroll \(S(1,2)\), and
\[
\dim\mathfrak{aut}(\widehat Z_{\mathrm{tan}})=7.
\]
Its Euler-weight dimensions are
\[
1,\ 4,\ 2
\]
in weights
\[
-1,\ 0,\ 1,
\]
respectively.

Consequently, Hwang–Li's 2026 automorphism theorem gives the sharp numerical specialization
\[
\dim\mathfrak{aut}(\widehat Z)\le5
\]
for every linearly nondegenerate surface in \(\mathbf P^4\) whose general symbol is of secant type, and
\[
\dim\mathfrak{aut}(\widehat Z)\le7
\]
for tangent type. Equality holds exactly for the corresponding Euler-symmetric model.

Thus the discriminant tangency is accompanied by a two-dimensional symmetry jump and, more specifically, by the appearance of a weight-\(-1\) hidden infinitesimal symmetry together with one additional weight-\(0\) symmetry.

## Assumptions and scope
All varieties are over \(\mathbf C\). The automorphism algebra is the Lie algebra of linear automorphisms of the affine cone, exactly the invariant used in Hwang–Li's theorem; scalar homotheties are therefore included.

The statement concerns rank-\(2\) symbols on a two-dimensional tangent space for which
\[
\dim U=2.
\]
It does not classify higher-dimensional tangent spaces, other dimensions of \(U\), or symbol systems of rank at least \(3\).

For the upper-bound conclusion, \(Z\subset\mathbf P^4\) is assumed linearly nondegenerate and its system of fundamental forms at a general point is assumed isomorphic to the indicated symbol system. These are the hypotheses needed to invoke Hwang–Li's theorem.

## Proof
Write a binary quadric as
\[
A X^2+BXY+C Y^2.
\]
Its rank drops to one exactly on the smooth conic
\[
\Delta:\ B^2-4AC=0
\]
in
\[
\mathbf P(\operatorname{Sym}^2W^*).
\]
A projective line cannot be contained in \(\Delta\), so
\[
\mathbf P(U)\cap\Delta
\]
has length \(2\). The group \(\operatorname{PGL}(W)\) acts on \(\Delta\cong\mathbf P^1\) as the full projective linear group. Hence it is transitive on unordered pairs of distinct points and on tangent points. This gives exactly two orbits of \(U\).

For the secant representative
\[
U_{\mathrm{sec}}=\langle X^2,Y^2\rangle,
\]
the restricted discriminant is
\[
-4uv,
\]
so the intersection with \(\Delta\) consists of two reduced points. Hwang–Li's Euler-symmetric construction in rank \(2\) is the closure of
\[
(s,p,q)\longmapsto
(s^2,\;sp,\;sq,\;p^2,\;q^2).
\]
Its image satisfies
\[
ta=x^2,\qquad tb=y^2.
\]
These two independent quadrics form a regular sequence, and the open chart \(t\ne0\) is irreducible with coordinates \(t,x,y\); the complement has smaller dimension. Thus the closure is the stated irreducible complete intersection and has degree
\[
2\cdot2=4.
\]
Along the boundary line
\[
t=x=y=0
\]
the Jacobian of the two quadrics has rank \(1\), so the surface is singular in codimension one. A complete intersection is Cohen–Macaulay, hence satisfies Serre's condition \(S_2\); failure of regularity in codimension one shows that this surface is not normal.

For the tangent representative
\[
U_{\mathrm{tan}}=\langle X^2,XY\rangle,
\]
the restricted discriminant is
\[
v^2,
\]
so the line is tangent to \(\Delta\). The construction gives the closure of
\[
(s,p,q)\longmapsto
(s^2,\;sp,\;sq,\;p^2,\;pq).
\]
Its ideal is
\[
(ta-x^2,\;tb-xy,\;xb-ay),
\]
the \(2\times2\) minors of
\[
\begin{pmatrix}
t&x&y\\
x&a&b
\end{pmatrix}.
\]
This is the standard determinantal ideal of the rational normal cubic scroll \(S(1,2)\), hence the surface is smooth and has degree \(3\).

It remains to compute the two infinitesimal automorphism algebras. Let
\[
A\in\mathfrak{gl}_5
\]
act on the homogeneous coordinates. For each quadratic generator \(f_i\), impose the exact linear condition
\[
A\cdot f_i\in I_2,
\]
where \(I_2\) is the quadratic part of the homogeneous ideal. Since the displayed quadrics are a basis of \(I_2\) in each case, this is a finite rational linear system.

For the secant ideal, the solution space has dimension
\[
5.
\]
Decomposing \(A\) under conjugation by the Euler one-parameter subgroup with coordinate weights
\[
(0,1,1,2,2)
\]
gives dimensions
\[
3\ \text{in weight }0,\qquad
2\ \text{in weight }1.
\]

For the tangent ideal, the same exact calculation has dimension
\[
7
\]
and decomposes as
\[
1\ \text{in weight }-1,\qquad
4\ \text{in weight }0,\qquad
2\ \text{in weight }1.
\]
This proves the claimed two-dimensional jump and identifies a genuinely grading-shifting symmetry in the tangent stratum.

Finally, Hwang–Li prove that for a linearly nondegenerate projective variety the cone automorphism dimension is bounded above by that of the Euler-symmetric variety associated with its general symbol system, with equality exactly for the Euler-symmetric model. Substituting the two exact dimensions above gives the bounds \(5\) and \(7\) and their equality cases.

## Verification
The accompanying `verify.py` uses exact rational symbolic arithmetic.

It first restricts the binary-quadratic discriminant to the two normal forms and verifies
\[
-4uv
\]
in the secant case and
\[
v^2
\]
in the tangent case. It checks both parametrizations against the displayed homogeneous ideals and verifies that the tangent ideal is the full set of \(2\times2\) minors of its \(2\times3\) matrix.

For each ideal, an exact Gröbner-basis monomial count computes the Hilbert function through degree \(8\). The stable second differences are identically \(4\) for the secant surface and \(3\) for the tangent surface, matching the geometric degree proofs.

For the automorphism calculation, the verifier introduces a generic \(5\times5\) matrix \(A\) and requires the induced derivation of each quadratic generator to remain in the quadratic ideal. Exact linear algebra gives cone-automorphism dimensions \(5\) and \(7\). Intersecting the nullspace with each Euler-weight block gives the graded dimensions
\[
(3,2)
\]
for weights \((0,1)\) in the secant case and
\[
(1,4,2)
\]
for weights \((-1,0,1)\) in the tangent case.

The saved replay ends in `VERIFY_OK`.

## Relationship to prior work
Hwang–Li prove the general 2026 inequality comparing the automorphism algebra of a projective variety with that of the Euler-symmetric variety determined by its general symbol, and characterize equality. They explicitly note that every subspace
\[
S^2\subset\operatorname{Sym}^2W^*
\]
defines such a rank-\(2\) symbol system, but do not give the present two-dimensional binary-pencil stratification or its automorphism dimensions.

Fu–Hwang's earlier theory identifies rank-\(2\) symbol systems with quadratically symmetric varieties and constructs the associated models. Their nonsingular classification covers the smooth tangent model abstractly, while the present secant model is singular. The checked earlier sources do not state the paired secant/tangent equations, the \(5\)-versus-\(7\) cone-automorphism dimensions, or the Euler-weight jump.

Targeted searches were made for the exact equations, the binary-pencil discriminant formulation, cubic-scroll aliases, automorphism dimensions, and hidden negative-weight symmetry. No checked source stated the combined dichotomy.

## Limitations
The two orbit representatives are special to
\[
\dim W=\dim U=2.
\]
For larger spaces, pencils and higher-dimensional linear systems of quadrics have substantially richer orbit structure.

The computation concerns infinitesimal linear automorphisms of the affine cone, not the full abstract automorphism group of the underlying surface. The corresponding projective linear automorphism dimensions are one less because scalar homotheties act trivially on projective space.

The result does not classify all surfaces in \(\mathbf P^4\) realizing either symbol type. It supplies the sharp automorphism bound and the unique equality model furnished by Hwang–Li's theorem.

## References
1. J.-M. Hwang and Q. Li, *Fundamental forms and infinitesimal symmetries of projective varieties*, arXiv:2608.08442v1, 2026.
2. B. Fu and J.-M. Hwang, *Euler-symmetric projective varieties*, Algebraic Geometry 7 (2020), 377–389.
3. B. Fu and J.-M. Hwang, *Special birational transformations of type \((2,1)\)*, for the quadratic model \(Z(\sigma)\) and its second fundamental form.
4. I. Arzhantsev and Y. Zaitseva, *Equivariant completions of affine spaces*, Russian Mathematical Surveys 77 (2022), 571–650.
