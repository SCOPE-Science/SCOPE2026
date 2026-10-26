# Exact quaternionic numerical-range shells and a quintic convexification-volume law

## Finding
Let \(i,j,k\) be the standard quaternion units and let \(a\ge b>0\), \(c>0\). For the quaternionic matrix
\[
A_{a,b,c}=\begin{pmatrix}ai&cj\\-cj&bi\end{pmatrix},
\]
write every quaternion as \(z=x+v\), with \(x\in\mathbb R\) and purely imaginary \(v\in\operatorname{span}_{\mathbb R}\{i,j,k\}\). Set \(d=a-b\), \(s=a+b\) and \(r=d/s\). Its full quaternionic numerical range is the nonlinearly radial elliptic shell
\[
W_{\mathbb H}(A_{a,b,c})
=\left\{x+v:\frac{x^2}{c^2}+\frac{(2|v|-d)^2}{s^2}\le1\right\}.
\]
In particular \(|x|\le c\) is automatic. The convex hull is the solid of revolution
\[
\operatorname{conv}W_{\mathbb H}(A_{a,b,c})
=\left\{x+v:|x|\le c,\quad
 |v|\le\frac{d+s\sqrt{1-x^2/c^2}}2\right\}.
\]
The difference has exact four-dimensional Lebesgue volume
\[
\boxed{\;
\operatorname{vol}_4\!\left(\operatorname{conv}W_{\mathbb H}(A_{a,b,c})\setminus W_{\mathbb H}(A_{a,b,c})\right)
=\frac{\pi c s^3}{3}\,I(r),\qquad
I(r)=\int_0^{\arcsin r}(r-\sin\theta)^3\sin\theta\,d\theta.\;}
\]
An elementary closed form, valid for \(0\le r<1\), is
\[
I(r)=\frac{8r^3+16r-(2r^3+13r)\sqrt{1-r^2}-(12r^2+3)\arcsin r}{8}.
\]
The volume deficit vanishes exactly when \(a=b\). As the skew-diagonal anisotropy \(d\) tends to zero with \(s,c\) fixed, it has the **sharp quintic onset**
\[
\boxed{\;\operatorname{vol}_4(\operatorname{conv}W\setminus W)
=\frac{\pi c}{60}\frac{d^5}{s^2}
+O\!\left(\frac{c d^7}{s^4}\right).\;}
\]
Moreover \(I(r)=r^5\int_0^1 t(1-t)^3(1-r^2t^2)^{-1/2}\,dt\), which proves strict positivity for \(r>0\), shows the normalized volume deficit is strictly increasing in \(r\), and establishes that the fifth-order exponent cannot be improved.

## Assumptions and scope
All numerical ranges are quaternionic: \(W_{\mathbb H}(A)=\{u^*Au:u\in\mathbb H^2,\ u^*u=1\}\). Imaginary directions are measured with the Euclidean norm on \(\mathbb R^3\), and the volume is ordinary Lebesgue measure on \(\mathbb H\cong\mathbb R^4\). The hypotheses are \(a\ge b>0\) and \(c>0\); the case \(b>a\) follows by relabeling the two coordinates. The first-public motivating source is the October 13, 2026 proof of the convexity of the upper bild, whose general five-coordinate representation is used explicitly below. The present volume assertion is a quantitative invariant of this canonical anticommuting two-level family, not a classification of all quaternionic matrices.

## Proof
Fix a quaternionic unit vector. Right multiplication by a unit quaternion preserves the real component and the norm of the imaginary component of its numerical value. Hence, as in the published five-coordinate representation, choose its first coordinate real, write it as \((u,q)\), and introduce \(t=u^2-|q|^2\) and \(p_\ell=2u q_\ell\) for the real coefficients \(q_0,q_1,q_2,q_3\) of \(q\). These parameters range over the unit four-sphere, and the published ball-filling lemma allows replacement by the unit five-ball without changing the upper bild. In this special family the real component \(x\) and imaginary radius \(y\) are
\[
x=-cp_2,\qquad
 y=\sqrt{\frac{(d+st)^2}{4}+ab(p_0^2+p_1^2)}.
\]
For fixed \(x\in[-c,c]\), put \(R=\sqrt{1-x^2/c^2}\). All feasible parameters satisfy \(t^2+p_0^2+p_1^2\le R^2\), and conversely every such triple extends to the ball by putting \(p_3=0\). This feasible set is connected, so the radii obtained form an interval.

The minimum radius is obtained with \(p_0=p_1=0\), minimizing \(|d+st|/2\) over \(-R\le t\le R\). Thus
\[
L(x)=\frac12\max\{0,d-sR\}.
\]
For the maximum, maximize \(p_0^2+p_1^2\) at fixed \(t\); the squared radius becomes
\[
\frac{d^2}{4}+abR^2+\frac{sd}{2}t+\frac{d^2}{4}t^2.
\]
This is a convex quadratic in \(t\). Since \(d\ge0\), its maximum on \([-R,R]\) is attained at \(t=R\), yielding
\[
U(x)=\frac{d+sR}{2}.
\]
Therefore the upper bild is exactly \(\{x+iy:|x|\le c,\ L(x)\le y\le U(x)\}\), equivalent to the asserted half-elliptic disk. All purely imaginary directions with a fixed norm occur by quaternionic similarity, giving the full four-dimensional shell.

The function \(U\) is nonnegative and concave on \([-c,c]\). Consequently \(K=\{x+v:|x|\le c,\ |v|\le U(x)\}\) is convex and contains the numerical range. At each \(x\), the entire two-sphere of imaginary vectors with norm \(U(x)\) belongs to the numerical range; its convex hull is the complete three-ball of that radius. Thus \(K\subseteq\operatorname{conv}W\), proving the convex-hull formula.

Every missing cross-section is exactly the three-ball of radius \(L(x)\), up to its boundary. With \(r=d/s\) and \(x_0=c\sqrt{1-r^2}\), it follows that
\[
\begin{aligned}
\operatorname{vol}_4(K\setminus W)
&=\frac{4\pi}{3}\int_{-c}^c L(x)^3\,dx\\
&=\frac{\pi}{3}\int_{x_0}^{c}
\left(d-s\sqrt{1-x^2/c^2}\right)^3\,dx\\
&=\frac{\pi c s^3}{3}\int_0^{\arcsin r}(r-\sin\theta)^3\sin\theta\,d\theta.
\end{aligned}
\]
The displayed closed form follows by integrating four powers of sine, with the lower endpoint zero. Setting \(\sin\theta=rt\) gives the nonsingular integral representation
\[
I(r)=r^5\int_0^1\frac{t(1-t)^3}{\sqrt{1-r^2t^2}}\,dt.
\]
Its integral is positive for positive \(r\). Expanding the denominator uniformly for \(r\) near zero and using \(\int_0^1t(1-t)^3dt=1/20\) yields \(I(r)=r^5/20+O(r^7)\) and the claimed quintic law. The same representation proves strict increase of \(I\) on \((0,1)\).

## Verification
The accompanying `verify.py` uses standard-library quaternion multiplication, deterministic sampling of normalized vectors for several regimes, exact rational checks of the quadratic maximization identity, and independent numerical quadrature of the closed integral. It passed 50,396 finite assertions in the packaged execution. These checks are auxiliary; the all-parameter proof is the coordinate reduction, optimization, convex-hull argument and exact volume integral above.

## Relationship to prior work
Carvalho's October 13, 2026 manuscript gives the general five-coordinate characterization of the upper bild and proves its convexity. That result underpins the ball-filling step and strongly constrains possible quantitative refinements. The distinct conclusion here is the *four-dimensional convexification-volume profile* for the anticommuting quaternionic two-level pencil, and especially its exact sharp fifth-order loss of convexity. So's 1998 paper gives a general binary criterion for convexity but not a four-dimensional volume deficit. Carvalho–Diogo–Mendes (first public 2020) focus on complex-entry matrices; Chien–Nakazato (2019) give boundary-generating algebraic curves without an identified quintic volume formula for this family. The precise full shape is an intermediate consequence of Carvalho's parametrization and is **not claimed as a wholly independent characterization method**.

## Limitations
The claim concerns this specified three-parameter family and ordinary four-dimensional volume. It does not extend the upper-bild convexity theorem, calculate the Hausdorff nonconvexity gap, or determine volumes for all \(2\times2\) quaternionic matrices. A broader prior theorem could encode the same special-family result implicitly. The 1996 So–Thompson treatment and other possible historic examples were not fully accessible; priority for an equivalent volume-asymptotic calculation therefore remains uncertain. No independent scientific audit has been performed.

## References
- L. Carvalho, *On the Convexity of the Upper Bild*, arXiv:2610.18096, first public October 13, 2026, especially the five-coordinate representation, Proposition 8 and Corollary 10. https://arxiv.org/abs/2610.18096
- W. So, *An Explicit Criterion for the Convexity of Quaternionic Numerical Range*, Canadian Mathematical Bulletin 41 (1998), 105–108, especially Theorem 2.2. https://doi.org/10.4153/CMB-1998-016-4
- L. Carvalho, C. Diogo and S. Mendes, *Quaternionic Numerical Range of Complex Matrices*, arXiv:2008.02850, first public August 6, 2020. https://arxiv.org/abs/2008.02850
- M.-T. Chien and H. Nakazato, *Boundary Generating Curves of Quaternionic Numerical Ranges*, Linear Algebra and its Applications 574 (2019), 201–215. https://doi.org/10.1016/j.laa.2019.04.005
