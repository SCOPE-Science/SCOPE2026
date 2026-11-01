# Shape-independent angular response and a sharp contraction threshold for triangular \(\lambda\)-Steiner symmetrization

## Finding
Let \(T\subset\mathbb R^2\) be any nondegenerate Euclidean triangle of area \(A\), and let
\(I(T)=\int_T\|x-c_T\|^2\,dx\), where \(c_T\) is its area centroid.  Let
\(U\) be uniformly distributed over oriented unit vectors, and let
\(S_U^\lambda T\) be the \(\lambda\)-Steiner symmetral for
\(0\le\lambda\le\tfrac12\), defined precisely below. Then
\[
\mathbb E_U I(S_U^\lambda T)
 =\frac12 I(T)+\frac{A^2}{4\pi}
 +\frac{A^2}{3\pi}\left(\lambda-\frac12\right)^2.
\]
In particular, for any two parameters \(\lambda,\mu\in[0,\tfrac12]\),
\[
\mathbb E_U\!\left[I(S_U^\lambda T)-I(S_U^\mu T)\right]
 =\frac{A^2}{3\pi}\left[
 \left(\lambda-\frac12\right)^2-\left(\mu-\frac12\right)^2\right],
\]
which is independent of the shape of \(T\) at fixed area.

Define the constant
\[
\lambda_* =\frac12-\sqrt{\frac{\pi\sqrt3}{6}-\frac34}
 =0.103894354853268\ldots.
\]
The inequality \(\mathbb E_U I(S_U^\lambda T)\le I(T)\) holds for **every**
nondegenerate triangle \(T\) if and only if \(\lambda\in[\lambda_*,\tfrac12]\).
At \(\lambda=\lambda_*\), equality occurs exactly for equilateral triangles;
for \(\lambda>\lambda_*\), the inequality is strict for all triangles.  For
\(0\le\lambda<\lambda_*\), every equilateral triangle has strictly larger
expected inertia after one step, while sufficiently slender triangles have
strictly smaller expected inertia.

## Assumptions and scope
The plane is Euclidean and the inertia is the **unnormalized, centroidal**
second area moment, not a moment about a fixed origin.  Choose an orthonormal
pair \((u,v)\), with \(u\) the chord direction and \(v\perp u\).  For each
\(t\), let \(\ell(t)\) be the length of the chord of \(T\) parallel to
\(u\) at \(v\cdot x=t\) (zero if there is no chord). The symmetral is defined by
\[
S_u^\lambda T=\{tv+su:\ t\in\mathbb R,\ -\lambda\ell(t)\le s\le(1-\lambda)\ell(t)\}.
\]
This is the planar chord formulation used in Kipp--Sagmeister (2026).  At
\(\lambda=0\) it is Blaschke shaking; at \(\lambda=\tfrac12\) it is
ordinary Steiner symmetrization.  The law of \(U\) is normalized arc measure
\(d\theta/(2\pi)\) on \(S^1\).  Translations of \(T\) do not affect either
side. No assertions about multiple symmetrization steps or general convex
bodies are made.

## Proof
**1. A directionwise chord identity.** Put
\(h=\tfrac12-\lambda\), \(M_2=\int_\mathbb R\ell(t)^2dt\), and
\(M_3=\int_\mathbb R\ell(t)^3dt\).  The symmetral has the same projected
marginal distribution in the \(v\) direction as \(T\).  Its centroidal
\(v\)-second moment is consequently
\(A\operatorname{Var}(v\cdot X)\), where \(X\) is uniform in \(T\).
For a fixed chord of length \(L\), integration from
\(-\lambda L\) to \((1-\lambda)L\) gives its first and second
\(u\)-moments as \(hL^2\) and
\((\tfrac1{12}+h^2)L^3\), respectively.  Its area-normalized centroidal
\(u\)-moment is therefore
\((\tfrac1{12}+h^2)M_3-h^2M_2^2/A\).  Adding the
orthogonal components gives the exact identity
\[
I(S_u^\lambda T)=A\operatorname{Var}(v\cdot X)
 +\frac{M_3}{12}+h^2\left(M_3-\frac{M_2^2}{A}\right).
\]

**2. Triangular fibers and inverse width.** Write \(w(v)\) for the length
of the orthogonal projection of \(T\) on the \(v\) axis. Except at finitely
many directions, \(\ell(t)\) is a two-sided linear tent whose height is
\(H=2A/w(v)\).  Direct integration gives
\[
M_2=\frac{wH^2}{3}=\frac{4A^2}{3w(v)},\qquad
M_3=\frac{wH^3}{4}=\frac{2A^3}{w(v)^2}.
\]
The same formulas hold at the exceptional directions by continuity. Hence
\[
I(S_u^\lambda T)=A\operatorname{Var}(v\cdot X)
 +\left(\frac16+\frac{2h^2}{9}\right)\frac{A^3}{w(v)^2}.
\]

To average the last term, set \(D=T-T\). Its support function is
\(h_D(v)=w(v)\), so the radial function of its polar \(D^\circ\) is
\(\rho_{D^\circ}(v)=1/w(v)\). The polar area identity yields
\[
\frac1{2\pi}\int_0^{2\pi}\frac{d\theta}{w(v_\theta)^2}
 =\frac{|D^\circ|}{\pi}.
\]
For the reference triangle
\(T_0=\operatorname{conv}\{(0,0),(1,0),(0,1)\}\), the polar difference
body is the hexagon
\[
(T_0-T_0)^\circ=\{(z_1,z_2): |z_1|\le1,\ |z_2|\le1,
\ |z_1-z_2|\le1\},
\]
whose area is \(3\) (the square of area \(4\) with two right triangles of
area \(1/2\) removed).  Every \(T\) is a translation and a nonsingular
linear image \(BT_0\); \(|\det B|=2A\), and polar area scales by
\(|\det B|^{-1}\). Thus
\[
|(T-T)^\circ|=\frac3{2A},\qquad
\mathbb E_v\frac1{w(v)^2}=\frac3{2\pi A}.
\]
The other directional term averages to \(I(T)/2\), because
\(\mathbb E_v(v\cdot z)^2=\|z\|^2/2\) for every fixed \(z\). Substitution
proves the asserted exact expectation.

**3. Optimal universal contraction parameter and equality.** For side
lengths \(a,b,c\), the centroidal inertia of a uniform triangle is
\[
I(T)=\frac{A(a^2+b^2+c^2)}{36}.
\]
Heron's identity gives
\[
(a^2+b^2+c^2)^2-48A^2
=2\bigl[(a^2-b^2)^2+(b^2-c^2)^2+(c^2-a^2)^2\bigr]\ge0.
\]
Therefore \(I(T)\ge\sqrt3 A^2/9\), with equality exactly for
\(a=b=c\). The exact expectation gives
\[
\mathbb E_U I(S_U^\lambda T)-I(T)
=-\frac{I(T)}2+\frac{A^2}{4\pi}+\frac{h^2A^2}{3\pi}.
\]
For each fixed area and parameter this is maximized precisely by equilateral
triangles.  Its equilateral value is nonpositive if and only if
\[
h^2\le\frac{\pi\sqrt3}{6}-\frac34.
\]
Since \(h\in[0,\tfrac12]\), this is exactly
\(\lambda\in[\lambda_*,\tfrac12]\).  The equality and counterexample
statements follow, and arbitrarily slender fixed-area triangles have
\(I(T)/A^2\to\infty\), establishing the final comparison.

## Verification
The accompanying `verify.py` recomputes individual transformed moments by
**independent chord-endpoint quadrature**, rather than substituting the
triangular tent formula. It tests four noncongruent triangles, four parameter
values and two independent angular offsets; it additionally checks the
threshold signs, the exact rational polar-hexagon area and rational Heron
identities. The completed verifier reported
`TRIANGLE_RECENTERING_CHECK_OK: 35 exact/algebraic or independent quadrature comparisons; 115200 direction-level evaluations; threshold=0.103894354853268`.
The all-directions and all-triangles assertions follow from the proof, not
from these finite tests. Run `python3 verify.py` using the provided Python
standard library.

## Relationship to prior work
Kipp and Sagmeister (arXiv:2610.05113v1, first posted 2026-10-04) define
\(\lambda\)-Steiner symmetrization and establish qualitative convergence
criteria for its random iteration. They mention moments of inertia as familiar
Steiner Lyapunov functionals, but their displayed results do not give the
one-step triangular Haar-direction expectation or the sharp parameter
threshold here. The identity
\(|T|\,|(T-T)^\circ|=3/2\) is a classical triangle equality in the
Eggleston polar-difference-body inequality and is explicitly acknowledged as
an ingredient rather than claimed as new. Bianchi, Gardner and Gronchi's
symmetrization framework also predates this result; its geometric operations
are not claimed as new. The contribution asserted here is the combined exact
shape-independent angular response and the universal sharp mean-contraction
boundary for triangles, not the preexisting fiber, polarity or inertia
formulas separately.

## Limitations
The statement concerns a single Haar-uniform direction and a planar
nondegenerate triangle. No expected drift theorem for a repeated random
process, uniform per-direction monotonicity at intermediate parameters, or
corresponding universal threshold for arbitrary bodies is established.
The exact expectation is analytically proved, but independent mathematical
validation has not been performed. Historical priority of the combined
statement requires further specialist literature review; equivalent older
formulations could exist.

## References
- C. Kipp and Á. Sagmeister, *Random convergence of generalized Steiner processes*, arXiv:2610.05113v1, 2026-10-04, https://arxiv.org/html/2610.05113v1.
- A. Aliev, *Mahler-type volume inequality for convex bodies with tetrahedral symmetry*, arXiv:2511.14991v1, 2025-11-19, https://arxiv.org/html/2511.14991v1; contains the established planar polar-difference inequality and triangle equality.
- G. Bianchi, R. J. Gardner and P. Gronchi, *Symmetrization in Geometry*, arXiv:1603.00643v2, 2016; Adv. Math. 306 (2017), 51–88, https://arxiv.org/abs/1603.00643.
