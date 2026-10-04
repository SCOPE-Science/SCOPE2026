# Exact covering-radius profile of the sharp planar parallelogram pair
## Finding
Let
\[
P_1=\{\alpha(1,1)+\beta(-\tfrac12,\tfrac12):0\le\alpha,\beta\le1\},
\]
\[
P_2=\{\alpha(-1,1)+\beta(\tfrac12,\tfrac12):0\le\alpha,\beta\le1\},
\]
which are the two covering parallelograms used by Codenotti, Freyer, and Krivokuća to show sharpness of their planar Brunn--Minkowski inequality for the covering radius. For
\[
Q_\lambda=(1-\lambda)P_1+\lambda P_2,\qquad 0\le\lambda\le1,
\]
the covering radius with respect to \(\mathbb Z^2\) is
\[
\mu(Q_\lambda)=
\begin{cases}
\dfrac{2}{2-\lambda},&0\le\lambda\le\tfrac12,\\[4pt]
\dfrac{2}{1+\lambda},&\tfrac12\le\lambda\le1.
\end{cases}
\]
Equivalently,
\[
\mu(Q_\lambda)^{-1}=1-\frac12\min\{\lambda,1-\lambda\}.
\]
Thus the inverse covering radius decreases linearly from \(1\) to \(3/4\) and then increases linearly back to \(1\). In particular, \(\lambda=1/2\) is the unique parameter in this family at which the sharp constant \(3/4\) is attained.

## Assumptions and scope
The covering radius is
\[
\mu(K)=\inf\{r\ge0:rK+\mathbb Z^2=\mathbb R^2\}.
\]
Translation of \(K\) does not change \(\mu(K)\), and an invertible linear map may be applied simultaneously to the body and the lattice. The statement is only about the explicit one-parameter family above. It does not classify equality cases for all pairs of planar convex bodies.

## Proof
Put
\[
u=(1,1),\qquad v=(-\tfrac12,\tfrac12).
\]
After translating to their centers, \(P_1\) is the rectangle in \((u,v)\)-coordinates with coefficient half-widths \(1/2,1/2\). Since
\[
(-1,1)=2v,\qquad (\tfrac12,\tfrac12)=\tfrac12u,
\]
the centered \(P_2\) has coefficient half-widths \(1/4,1\). Therefore the centered \(Q_\lambda\) becomes
\[
R_\lambda=[-a_\lambda,a_\lambda]\times[-b_\lambda,b_\lambda],
\qquad
a_\lambda=\frac{2-\lambda}{4},\quad b_\lambda=\frac{1+\lambda}{2}.
\]

Let \(B\) be the matrix with columns \(u,v\). Then
\[
B^{-1}=\begin{pmatrix}\tfrac12&\tfrac12\\-1&1\end{pmatrix},
\]
so the transformed lattice is
\[
L=B^{-1}\mathbb Z^2
 =\{(m/2,n):m,n\in\mathbb Z,\ m\equiv n\pmod2\}.
\]
Thus the horizontal row of height \(n\) has centers at \(\mathbb Z\) when \(n\) is even and at \(\mathbb Z+1/2\) when \(n\) is odd.

We now compute the covering radius of a general axis-parallel rectangle
\[
R=[-a,a]\times[-b,b]
\]
with respect to \(L\). Write \(A=ra\) and \(C=rb\) for the horizontal and vertical half-widths of \(rR\). There are exactly two ways to cover.

If \(C\ge1/2\) and \(A\ge1/2\), every horizontal line meets at least one lattice row, and a single active row covers the horizontal coordinate because its centers have spacing \(1\). Conversely, when \(1/2\le C<1\), the line of height \(0\) sees only the even row; hence \(A\ge1/2\) is necessary. If \(C<1/2\), the line of height \(1/2\) meets no row at all.

If \(C\ge1\), every horizontal line meets two consecutive lattice rows of opposite parity. Their centers interlace to \(\tfrac12\mathbb Z\), so \(A\ge1/4\) is sufficient. It is also necessary in this regime: at height \(0\), the active row phases together have horizontal center spacing \(1/2\), and a point midway between consecutive centers is uncovered when \(A<1/4\).

Hence
\[
\mu(R,L)=
\min\left\{
\max\left(\frac1{2a},\frac1{2b}\right),
\max\left(\frac1{4a},\frac1b\right)
\right\}.
\]
For \(a=a_\lambda\) and \(b=b_\lambda\), the two candidates simplify on \(0\le\lambda\le1\) to
\[
\max\left(\frac{2}{2-\lambda},\frac1{1+\lambda}\right)
=\frac{2}{2-\lambda},
\]
and
\[
\max\left(\frac1{2-\lambda},\frac{2}{1+\lambda}\right)
=\frac{2}{1+\lambda}.
\]
The first is smaller exactly when \(\lambda\le1/2\). This proves the formula.

## Verification
The proof is analytic for every real \(\lambda\in[0,1]\); no finite sampling is used to establish the continuum statement. The companion script `verify_profile.py` checks the coordinate change, the two rational covering mechanisms, the switch at \(\lambda=1/2\), and exact representative values using rational arithmetic. Its stored output is `VERIFY_OK`.

At \(\lambda=0\) and \(\lambda=1\), the formula gives \(\mu=1\), as required because both endpoint parallelograms cover. At \(\lambda=1/2\), it gives \(\mu=4/3\), hence \(\mu(Q_{1/2})^{-1}=3/4\). Since \(P_1+P_2=2Q_{1/2}\), homogeneity gives \(\mu(P_1+P_2)^{-1}=3/2\), exactly the equality value in the source theorem.

## Relationship to prior work
Codenotti, Freyer, and Krivokuća introduce these two parallelograms as a counterexample to preservation of covering under Minkowski interpolation, prove the sharp planar inequality
\[
\mu(K_1+K_2)^{-1}\ge\frac34\bigl(\mu(K_1)^{-1}+\mu(K_2)^{-1}\bigr),
\]
and state that equality for \(P_1,P_2\) follows from elementary geometry. Their paper does not state the full \(\lambda\)-profile above. Applied to the scaled pair \((1-\lambda)P_1\) and \(\lambda P_2\), their theorem yields only the uniform lower bound \(\mu(Q_\lambda)^{-1}\ge3/4\), whereas the formula here gives the exact value and shows uniqueness of the balanced equality parameter within this family.

Malikiosis, Santos, and Schymura give exact covering radii for several classes of lattice two-dimensional zonotopes. Those results concern lattice zonotopes with integer generators and do not state the continuous non-lattice interpolation profile above. Lian and Xue independently study minimal covering bodies and a Minkowski-type covering criterion; their inspected paper cites the Codenotti--Freyer--Krivokuća preprint but contains no Brunn--Minkowski interpolation formula for this pair.

## Limitations
No global equality classification for the planar Brunn--Minkowski inequality is claimed. The reduction to a staggered lattice is special to this parallel-edge pair. The novelty assessment is based on full-text inspection of the lead preprint and the closest covering-body and lattice-zonotope sources, together with targeted searches for equivalent formulas; an unindexed source could contain the same elementary profile.

## References
1. G. Codenotti, A. Freyer, K. Krivokuća, *Minimal covering bodies and Brunn--Minkowski type inequalities for the covering radius*, arXiv:2606.14442v1, first public 2026-06-12.
2. R. D. Malikiosis, F. Santos, M. Schymura, *Linearly exponential checking is enough for the lonely runner conjecture and some of its variants*, Forum of Mathematics, Sigma, DOI: 10.1017/fms.2025.10107.
3. Y. Lian, F. Xue, *Minimal Covering Bodies and a Minkowski-Type Criterion for Lattice Coverings*, arXiv:2606.14584v3.
