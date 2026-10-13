# Grassmann distance degree six for the ruling curve of \(S(2,2)\)
## Finding
Let
\[
\mathcal S\subset\operatorname{pGr}(2,6)
\]
be the curve of ruling lines of the rational normal scroll
\[
S(2,2)\subset\mathbf P^5.
\]
Then
\[
\operatorname{GDdeg}(\mathcal S)=6.
\]

The same curve has Euclidean distance degree
\[
\operatorname{EDdeg}(\mathcal S)=6
\]
by the rational-normal-scroll formula of Friedman–Hoşten–Rosana. Hence restricting the data from a generic symmetric matrix to a generic rank-two projection matrix causes no degree drop in this smallest balanced scroll case.

## Assumptions and scope
The projection Grassmannian is
\[
\operatorname{pGr}(2,6)
=
\{Q\in\operatorname{Sym}_6(\mathbf C):Q^2=Q,\ \operatorname{trace}(Q)=2\}.
\]
The Grassmann distance degree is the generic number of complex critical points of the chordal-distance objective after removing the algebraic cut locus.

A ruling line of \(S(2,2)\) is represented by the row span of
\[
B(t)=
\begin{pmatrix}
1&t&t^2&0&0&0\\
0&0&0&1&t&t^2
\end{pmatrix}.
\]
Put
\[
v(t)=(1,t,t^2),\qquad s(t)=1+t^2+t^4.
\]
Away from the isotropic poles \(s(t)=0\), its orthogonal projection matrix is block diagonal, with both diagonal blocks equal to
\[
\frac{v(t)^{\mathsf T}v(t)}{s(t)}.
\]

## Proof
For any symmetric data matrix \(Q\), write \(Q_{11}\) and \(Q_{22}\) for its two diagonal \(3\times3\) blocks. On the ruling curve,
\[
\operatorname{trace}(P(t)Q)
=
\frac{G_Q(t)}{s(t)},
\]
where
\[
G_Q(t)
=
v(t)Q_{11}v(t)^{\mathsf T}
+
v(t)Q_{22}v(t)^{\mathsf T}.
\]
The polynomial \(G_Q\) has degree at most \(4\). Therefore the finite critical points are zeros of
\[
H_Q(t)=G_Q'(t)s(t)-G_Q(t)s'(t).
\]
The nominal degree \(7\) cancels identically, so
\[
\deg H_Q\le6.
\]
Thus the Grassmann distance degree is at most \(6\), provided poles, infinity, and the cut locus are removed as in the definition.

To prove that the generic count actually reaches \(6\), take the rational \(2\times6\) matrix
\[
A=
\begin{pmatrix}
0&-1&-2&0&-2&3\\
0&-3&-1&-1&-2&-1
\end{pmatrix}
\]
and let
\[
Q=A^{\mathsf T}(AA^{\mathsf T})^{-1}A.
\]
Exact arithmetic gives
\[
Q^2=Q,\qquad Q^{\mathsf T}=Q,\qquad
\operatorname{rank}(Q)=2,\qquad
\operatorname{trace}(Q)=2,
\]
so \(Q\in\operatorname{pGr}(2,6)\).

For this data point,
\[
G_Q(t)
=
\frac{128t^4+8t^3+151t^2+24t+9}{126},
\]
and
\[
H_Q(t)
=
-\frac{h(t)}{63},
\]
where
\[
h(t)
=
4t^6+23t^5+32t^4-238t^3-142t-12.
\]
Its discriminant is
\[
6779465482547678036224,
\]
which is nonzero. Hence \(h\) has six distinct complex roots.

None of those roots is an isotropic pole, because
\[
\operatorname{Res}_t(h,s)=2875220721\ne0.
\]
The point at infinity is not critical either. With \(u=1/t\), the derivative of the objective at \(u=0\) is
\[
\frac{4}{63}\ne0.
\]

It remains to remove the algebraic cut locus. For a ruling plane with row matrix \(B(t)\), the restriction of \(Q\) to its image drops rank exactly when
\[
\det\!\bigl(B(t)QB(t)^{\mathsf T}\bigr)=0.
\]
For the displayed \(Q\),
\[
\det\!\bigl(B(t)QB(t)^{\mathsf T}\bigr)
=
\frac{t^2(5t^3+12t^2-2t+1)^2}{252}.
\]
The resultant
\[
\operatorname{Res}_t
\left(
h,\,
t(5t^3+12t^2-2t+1)
\right)
=
-1358879507628
\]
is nonzero. Therefore all six critical points lie outside the cut locus.

The conditions that the leading coefficient of \(H_Q\), its discriminant, the pole resultant, and the cut-locus resultant are nonzero are Zariski-open conditions on an affine chart of the data Grassmannian. The explicit \(Q\) proves that this open set is nonempty. Consequently generic \(Q\in\operatorname{pGr}(2,6)\) has six valid critical points. Together with the universal degree-\(6\) upper bound,
\[
\operatorname{GDdeg}(\mathcal S)=6.
\]

Finally, the 2026 scroll formula gives
\[
\operatorname{EDdeg}(\mathcal S)=2\delta-2.
\]
For \(S(2,2)\), both denominator polynomials are \(s(t)\), so their least common multiple has degree
\[
\delta=4.
\]
Thus
\[
\operatorname{EDdeg}(\mathcal S)=6
\]
as well.

## Verification
The accompanying `verify.py` reconstructs the rational projection matrix \(Q\), verifies its projection identities, derives the objective and degree-\(6\) critical polynomial, and checks its exact discriminant.

It independently verifies the nonzero resultants with the pole polynomial and the cut-locus polynomial, and evaluates the derivative at the point at infinity. The replay also checks that the scroll formula gives Euclidean distance degree \(6\).

The saved output ends in `VERIFY_OK`.

## Relationship to prior work
Friedman–Hoşten–Rosana treat rational normal scrolls as their warm-up example and prove a formula for the Euclidean distance degree of the ruling curve. Specializing their theorem to \(S(2,2)\) gives Euclidean distance degree \(6\). In the same paper, the Grassmann distance degree is defined by restricting the data point to the projection Grassmannian and deleting the algebraic cut locus; the paper emphasizes that Euclidean and Grassmann distance degrees can differ.

The earlier Friedman–Rosana–Sturmfels paper introduced the Grassmann distance degree for varieties of lines and developed the cut-locus formalism. The checked text contains no rational-normal-scroll computation.

Targeted searches for the ruling curve of \(S(2,2)\), rational normal scrolls, and Grassmann distance degree found no statement of the value \(6\). The nearest published work supplies the general invariant and the Euclidean-distance scroll calculation, but neither implies equality after the data restriction.

## Limitations
This determines one natural balanced scroll case, not the Grassmann distance degree of every rational normal scroll \(S(n_1,\ldots,n_d)\).

The proof counts complex critical points for generic data. It does not assert that all six are real for generic real data, nor does it classify the real minimizers.

The witness \(Q\) is used only to prove nonemptiness of the Zariski-open genericity conditions. The result is not a special-data count.

## References
1. H. Friedman, S. Hoşten, A. Rosana, *Euclidean Distance Optimization Within the Grassmannian*, arXiv:2610.02018v1, 2026.
2. H. Friedman, A. Rosana, B. Sturmfels, *Distance Optimization in the Grassmannian of Lines*, arXiv:2601.22843v1, 2026.
