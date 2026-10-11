# Exact face-angle obstruction radius for regular simplices

## Finding

Let \(\Delta_n\subset\mathbb R^n\), \(n\ge2\), be a regular simplex. For each exposed face \(F\), let \(L_F\) denote the linear subspace parallel to \(\operatorname{aff}F\). Kenderov--Mushkarov--Nikolov define, over pairs with
\[
L_F\cap L_G=\{0\},
\]
the angular constant
\[
c(\Delta_n)
=
\max
\max_{\substack{u\in L_F,\ v\in L_G\\ \|u\|=\|v\|=1}}
\langle u,v\rangle.
\]

Put
\[
r=\left\lfloor\frac n2\right\rfloor,
\qquad
s=\left\lceil\frac n2\right\rceil.
\]
Then
\[
\boxed{
c(\Delta_n)
=
\sqrt{\frac{rs}{(r+1)(s+1)}}.
}
\]

Equality occurs exactly, up to exchanging the two faces, when the faces are positive-dimensional, share exactly one vertex, together use all \(n+1\) vertices of the simplex, and have dimensions \(r\) and \(s\).

The bounded exceptional region in Proposition 4.3 of the source can therefore be made explicit:
\[
\boxed{
U_n
=
\left\{
X\in\mathbb R^n:
\operatorname{dist}(X,\Delta_n)
\le
M_n\operatorname{diam}(\Delta_n)
\right\},
}
\]
where
\[
\boxed{
M_n
=
\frac12
\left(
1+
\sqrt{\frac{(r+1)(s+1)}{n+1}}
\right).
}
\]
Hence, whenever \(O\notin U_n\), every local maximizer \([A^*B^*]\) of the source's exterior function \(G\) obeys
\[
d_{\Delta_n}(A^*)+d_{\Delta_n}(B^*)\le n-1.
\]

For example,
\[
c(\Delta_2)=\frac12,
\qquad
M_2=\frac12\left(1+\frac2{\sqrt3}\right),
\]
and
\[
c(\Delta_3)=\frac1{\sqrt3},
\qquad
M_3=\frac12\left(1+\sqrt{\frac32}\right).
\]

## Assumptions and scope

The simplex is Euclidean and regular. Scaling and rigid motions do not affect the angular constant.

Only positive-dimensional faces contribute to the inner unit-vector maximization. Vertex faces have zero direction space and therefore cannot supply unit vectors.

The quantity \(d_{\Delta_n}(A)\) is the dimension attached in the source to the minimal affine boundary piece through \(A\); for a polytope this is the dimension of the corresponding exposed face used in Proposition 4.3.

The conclusion is a specialization of the source's far-observer local-maximizer theorem. It makes the source's abstract finite angular maximum explicit for regular simplices; it does not claim that the resulting sufficient radius \(M_n\) is the smallest possible radius for every regular simplex.

## Proof

Use the standard centered model of a regular simplex with vertices
\[
v_0,\ldots,v_n
\]
satisfying
\[
\langle v_i,v_i\rangle=1,
\qquad
\langle v_i,v_j\rangle=-\frac1n
\quad(i\ne j).
\]
For a nonempty vertex set \(I\), the direction space of the corresponding face is
\[
L_I
=
\operatorname{span}\{v_i-v_j:i,j\in I\},
\]
and
\[
\dim L_I=|I|-1.
\]

Consider two positive-dimensional faces indexed by \(I\) and \(J\).

If \(|I\cap J|\ge2\), choose distinct \(p,q\in I\cap J\). Then
\[
v_p-v_q\in L_I\cap L_J,
\]
so the intersection is nontrivial.

Conversely, if \(|I\cap J|\le1\), then
\[
L_I\cap L_J=\{0\}.
\]
Indeed, after choosing one anchor in each face, the corresponding difference vectors are linearly independent because the vertices of a simplex are affinely independent. Thus the pairs appearing in the source's angular maximum are exactly the pairs of positive-dimensional faces sharing at most one vertex.

If \(I\cap J=\varnothing\), every generator from the first direction space is orthogonal to every generator from the second:
\[
\langle v_i-v_{i'},v_j-v_{j'}\rangle=0
\]
for \(i,i'\in I\) and \(j,j'\in J\). Hence the maximal cosine is \(0\).

Now suppose
\[
I\cap J=\{p\}.
\]
Write
\[
r=|I|-1,
\qquad
s=|J|-1.
\]
Choose bases
\[
e_i=v_i-v_p
\quad(i\in I\setminus\{p\}),
\qquad
f_j=v_j-v_p
\quad(j\in J\setminus\{p\}).
\]
After dividing all inner products by the common positive factor \((n+1)/n\), their Gram matrices are
\[
G_r=I_r+J_r,
\qquad
G_s=I_s+J_s,
\]
while the cross-Gram matrix is the all-ones matrix
\[
J_{r\times s}.
\]

For coefficient vectors \(a\in\mathbb R^r\) and \(b\in\mathbb R^s\), the normalized inner product factors as
\[
\frac{(\mathbf 1^\mathsf T a)(\mathbf 1^\mathsf T b)}
{\sqrt{a^\mathsf T(I_r+J_r)a}\,
 \sqrt{b^\mathsf T(I_s+J_s)b}}.
\]
The two optimizations separate. Since
\[
(I_r+J_r)^{-1}
=
I_r-\frac1{r+1}J_r,
\]
Cauchy--Schwarz in the \(I_r+J_r\) metric gives
\[
\max_{a\ne0}
\frac{|\mathbf 1^\mathsf T a|}
{\sqrt{a^\mathsf T(I_r+J_r)a}}
=
\sqrt{
\mathbf 1^\mathsf T(I_r+J_r)^{-1}\mathbf 1
}
=
\sqrt{\frac r{r+1}}.
\]
The analogous value for the second face is
\[
\sqrt{\frac s{s+1}}.
\]
Therefore
\[
c_{r,s}
=
\sqrt{\frac{rs}{(r+1)(s+1)}}.
\]

A shared-vertex pair with trivial intersection satisfies
\[
r+s\le n.
\]
The function
\[
\frac r{r+1}\frac s{s+1}
\]
is strictly increasing in each positive integer variable. Hence any maximizer has
\[
r+s=n.
\]
For fixed sum \(n\), the product
\[
(r+1)(s+1)
\]
is largest, and equivalently the displayed cosine is largest, when \(r\) and \(s\) differ by at most one. Thus
\[
r=\left\lfloor\frac n2\right\rfloor,
\qquad
s=\left\lceil\frac n2\right\rceil.
\]
Strictness also gives the stated equality classification.

Finally,
\[
1-c(\Delta_n)^2
=
1-\frac{rs}{(r+1)(s+1)}
=
\frac{n+1}{(r+1)(s+1)},
\]
because \(r+s=n\). The source chooses
\[
M
=
\frac12\left(1+\frac1{\sqrt{1-c^2}}\right).
\]
Substitution yields
\[
M_n
=
\frac12
\left(
1+
\sqrt{\frac{(r+1)(s+1)}{n+1}}
\right),
\]
and Proposition 4.3 gives the asserted far-observer conclusion.

## Verification

The bundled checker uses exact rational arithmetic and exact integer-rank calculations. For every dimension
\[
2\le n\le6
\]
it exhaustively enumerates every pair of positive-dimensional faces and verifies
\[
L_I\cap L_J=\{0\}
\quad\Longleftrightarrow\quad
|I\cap J|\le1,
\]
It then checks every admissible dimension pair \((r,s)\) by exact rational arithmetic for \(2\le n\le100\), and confirms that the maximum equals
\[
\frac{rs}{(r+1)(s+1)}
\]
with
\[
r=\left\lfloor\frac n2\right\rfloor,
\qquad
s=\left\lceil\frac n2\right\rceil.
\]
It also verifies the equality classification and the algebraic simplification of \(M_n\).

These finite checks are supplementary. The all-dimensional result is proved by affine independence, the explicit face-direction Gram matrices, and the monotonicity argument above.

## Relationship to prior work

Kenderov--Mushkarov--Nikolov prove that for any convex polytope there is a bounded exceptional region outside which every local maximizer of their exterior section-length function satisfies
\[
d_{\mathcal C}(A^*)+d_{\mathcal C}(B^*)\le n-1.
\]
Their proof defines an angular constant \(c\) as a finite maximum over pairs of direction spaces of exposed faces with trivial intersection, then sets
\[
M=\frac12\left(1+\frac1{\sqrt{1-c^2}}\right).
\]
The paper does not evaluate this constant for regular simplices or classify the extremizing face pairs.

Standard regular-simplex angle formulas include the familiar facet dihedral angle, but the quantity here is different: it is the largest principal cosine over all pairs of positive-dimensional face-direction spaces whose intersection is trivial. Targeted searches for arbitrary face-subspace angles, Friedrichs angles of simplex faces, and the source's Proposition 4.3 found no formula covering the stated maximum or its equality classification.

## Limitations

The value \(M_n\) is the explicit radius obtained by inserting the exact regular-simplex angular constant into the source's proof. The result does not prove that no smaller universal far-observer radius can work for regular simplices.

The originality comparison did not locate an equivalent formula in the classical literature on simplex face angles. Such a formula could exist under older principal-angle or Friedrichs-angle terminology; this remains the main bibliographic residual risk.

## References

1. P. Kenderov, O. Mushkarov, N. Nikolov, *A Generalization of a Classical Geometric Extremum Problem*, arXiv:2506.07252v1, 8 June 2025.
2. P. Kenderov, O. Mushkarov, N. Nikolov, *A Generalization of a Classical Geometric Extremum Problem*, Journal of Convex Analysis 34 (2027), 33--48.
