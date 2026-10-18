# The uniquely most directionally uniform right circular cone

## Finding

A solid right circular cone admits a natural, similarity-invariant measure of departure from constant width: the squared coefficient of variation of its widths over Haar-uniform unoriented directions. **Exactly one similarity class of nondegenerate right circular cones minimizes this departure.** Its height-to-base-radius ratio is strictly less than \(\sqrt 3\), although the cone with ratio \(\sqrt 3\) uniquely minimizes the *worst-direction width ratio*. Thus mean-square and worst-direction notions of nearly constant width select different cones.

Precisely, for \(r,h>0\) let
\[
 K_{r,h}=\operatorname{conv}\!\bigl(\{(x,y,0):x^2+y^2\le r^2\}\cup\{(0,0,h)\}\bigr),
 \qquad t=h/r.
\]
For a uniformly random unoriented line \(U\) in \(\mathbb R^3\), let \(W\) be the Euclidean length of the orthogonal projection of \(K_{r,h}\) on \(U\). Define
\[
 \mathcal V(t)=\frac{\operatorname{Var}(W)}{(\mathbb EW)^2},\quad
 a(t)=\pi+t-\arctan t,\quad
 b(t)=t^2+2+\frac{2(t^2+3)}{\sqrt{1+t^2}}.
\]
Then for every \(t>0\),
\[
 \boxed{\quad\mathbb EW=\frac r2 a(t),\qquad
 \mathbb EW^2=\frac{r^2}{3}b(t),\qquad
 \mathcal V(t)=\frac{4b(t)}{3a(t)^2}-1.\quad}
\]
Put
\[
 A(t)=(1+t^2)^{3/2}+t^2-1,
 \qquad B(t)=t(t^2+2)\sqrt{1+t^2}+2t(t^2+3),
\]
\[
 T(t)=\arctan t+\frac{B(t)}{A(t)}-t
 =\arctan t+\frac{t\bigl(\sqrt{1+t^2}+t^2+7\bigr)}{A(t)}.
\]
There is a **unique** \(t_*\in(0,3)\) solving \(T(t_*)=\pi\). The function \(\mathcal V\) is strictly decreasing on \((0,t_*)\) and strictly increasing on \((t_*,\infty)\). In particular,
\[
 \boxed{\quad t_*=1.7090130666055156\ldots<\sqrt 3,\qquad
 \inf_{t>0}\mathcal V(t)=\mathcal V(t_*)
 =0.00168696607831620\ldots.\quad}
\]
The corresponding optimal coefficient of variation is \(\sqrt{\mathcal V(t_*)}=0.0410726926109819\ldots\), or about \(4.11\%\). These decimals illustrate the exact equation rather than define the theorem. The optimal worst-direction ratio \(\operatorname{ess\,sup}W/\operatorname{ess\,inf}W\) instead occurs at \(t=\sqrt3\), with value \(2/\sqrt3\).

## Assumptions and scope

The body is the **solid convex cone** over a filled base disk with an apex above its center; it is not a hollow surface, an infinite cone, a double cone, or an arbitrary rotationally symmetric convex body. The radius and height are strictly positive, and the Euclidean metric and normalized rotation-invariant measure on unoriented lines are fixed. All formulas concern every real \(t>0\); no small-eccentricity assumption is imposed. \(\mathcal V\) is invariant under uniform scaling \((r,h)\mapsto(cr,ch)\). The optimization is solely **within** this natural one-parameter family, not among all convex bodies. In particular, balls have zero width variance but are not members of this cone family.

## Proof

**1. Direction reduction and width formula.** Let \(z=|u_3|\) for a uniformly random unit vector \(u\in S^2\); then \(z\) is uniform on \([0,1]\). Write \(s=(1+t^2)^{-1/2}\). The base disk has transverse support \(r\sqrt{1-z^2}\), while the apex contributes \(rz t\) in the forward direction. The backward support comes from the base. Consequently,
\[
 \frac{W(z)}r=\sqrt{1-z^2}+\max\{\sqrt{1-z^2},tz\}
 =\begin{cases}
 2\sqrt{1-z^2},&0\le z\le s,\\
 \sqrt{1-z^2}+tz,&s\le z\le1.
 \end{cases} \tag{1}
\]
The switch occurs at \(z=s\) because \(\sqrt{1-s^2}=ts\). Formula (1) exhausts every direction by axial symmetry.

**2. Exact first two moments.** Integrating (1) over the uniform variable \(z\) gives
\[
 \frac{\mathbb EW}{r}
 =\int_0^1\sqrt{1-z^2}\,dz
  +\int_0^s\sqrt{1-z^2}\,dz
  +t\int_s^1z\,dz
 =\frac{\pi+t-\arctan t}{2}.\tag{2}
\]
Here \(\arcsin s=\pi/2-\arctan t\). Expanding the square of (1) similarly yields
\[
 \begin{split}
 \frac{\mathbb EW^2}{r^2}
 &=\int_0^1(1-z^2)\,dz
   +3\int_0^s(1-z^2)\,dz\\
 &\quad+2t\int_s^1z\sqrt{1-z^2}\,dz
   +t^2\int_s^1z^2\,dz\\
 &=\frac13\left(t^2+2+\frac{2(t^2+3)}{\sqrt{1+t^2}}\right).
 \end{split}\tag{3}
\]
Equations (2)–(3) prove the exact expression for \(\mathcal V(t)\). Since the first branch of (1) decreases strictly on a nonempty interval for every \(t>0\), no such cone has constant width, and \(\mathcal V(t)>0\).

**3. One exact stationary equation.** Differentiate the elementary moment factors:
\[
 a'(t)=\frac{t^2}{1+t^2},\qquad
 b'(t)=2t\left(1+\frac{t^2-1}{(1+t^2)^{3/2}}\right).
\]
A direct expansion gives
\[
 \mathcal V'(t)=\frac{8tA(t)}{3a(t)^3(1+t^2)^{3/2}}
 \bigl(\pi-T(t)\bigr).\tag{4}
\]
All factors outside the parentheses are strictly positive when \(t>0\). Thus the sign of the derivative is exactly that of \(\pi-T(t)\); uniqueness of an optimum reduces to a one-variable inequality for \(T\).

**4. Rigorous global uniqueness.** Set \(y=t^2\), and introduce
\[
 P(y)=y^3-6y^2-15y-4,\qquad
 Q(y)=9y^3+16y^2+3y-4.
\]
Exact differentiation, with no approximation, gives
\[
 T'(t)=\frac{\sqrt{1+y}\,P(y)-Q(y)}
 {(1+y)^{3/2}\bigl((1+y)^{3/2}+y-1\bigr)^2}.\tag{5}
\]
The denominator is positive for \(t>0\). For \(0<y\le9\), we prove the numerator is negative by splitting into two exhaustive cases. If \(P(y)\le0\), then \(\sqrt{1+y}\ge1\) implies
\[
 \sqrt{1+y}\,P(y)-Q(y)\le P(y)-Q(y)
 =-8y^3-22y^2-18y<0.
\]
If \(P(y)>0\), then \(\sqrt{1+y}\le\sqrt{10}<4\), whence
\[
 \sqrt{1+y}\,P(y)-Q(y)<4P(y)-Q(y)
 =-5y^3-40y^2-63y-12<0.
\]
Thus **\(T\) is strictly decreasing throughout \((0,3]\)**.

For \(t\ge3\), it is unnecessary to control the derivative. Using \(\sqrt{1+t^2}\le t+1/(2t)\) and Bernoulli's inequality \((1+t^2)^{3/2}\ge t^3+3t/2\), we obtain
\[
 T(t)-\arctan t
 \le\frac{t^3+t^2+7t+1/2}{t^3+t^2+3t/2-1}
 <\frac32.\tag{6}
\]
Indeed, the final strict inequality is equivalent to
\(t^3+t^2-\frac{19}{2}t-4>0\), which holds at \(t=3\) and increases strictly for \(t\ge3\). Consequently,
\[
 T(t)<\frac\pi2+\frac32<\pi\qquad(t\ge3).
\]
As \(t\downarrow0\), the second representation of \(T\) shows \(T(t)\sim 16/(5t)\to\infty\). By continuity and strict decrease up to \(3\), there is exactly one root of \(T(t)=\pi\) in \((0,3)\). There are no roots thereafter, by (6). Equation (4) now proves the strict decrease–increase profile and the globally unique minimizing similarity class. The bisection values in the statement are obtained from this exact scalar equation and verified independently by `verify.py`.

**5. Strict separation from the worst-direction optimum.** The pointwise width (1) yields the essential endpoint ratio
\[
 \frac{\operatorname{ess\,sup}W}{\operatorname{ess\,inf}W}
 =\begin{cases}
 2/t,&0<t\le\sqrt3,\\
 (t+1/t)/2,&t\ge\sqrt3.
 \end{cases}\tag{7}
\]
This is strictly decreasing before \(\sqrt3\) and strictly increasing afterward; hence its unique minimizer is \(\sqrt3\). Substitution in the exact equation gives
\[
 T(\sqrt3)=\frac\pi3+\frac{6\sqrt3}{5}<\pi,
\]
where the final inequality follows, for example, from \(\sqrt3<26/15\) and \(\pi>223/71\). Since \(T\) is strictly decreasing on \((0,3]\), its unique crossing of \(\pi\) occurs **before** \(\sqrt3\). This proves that the minimizing cones for the two natural directional-isotropy losses are genuinely different.

## Verification

Run the standalone standard-library script `python3 verify.py` in the directory containing this document. In the recorded execution, it completed `VERIFY_OK 1533` finite diagnostics: independent Simpson quadrature of the first two moments for 16 aspect ratios; numerical comparisons between the derivative of \(T\) and the exact rational-radical identity (5); rational polynomial-sign test points in the two proof cases; the bisection root and its comparison to \(\sqrt3\); and the analytic derivative identity (4) on 400 further aspect ratios. The numerical output reported \(t_*=1.7090130666055141\) and \(\mathcal V(t_*)=0.0016869660783161\) at standard double precision. Equation (5) and the global bounds (6) constitute the proof; quadrature, sampled inequalities and bisection are **diagnostics**, not exhaustive or infinite certificates.

## Relationship to prior work

The 10 August 2026 manuscript *Random Width and Brightness* by Omri Abas (arXiv:2609.26202v1) motivates directional-width statistics and gives a general polyhedral and zonotopal approach, including variance analysis, but not the circular-cone optimization here. Its full text was examined at the introduction, width-calculus section and harmonic variance theorem; its specific exact-model examples are polyhedral, not this rotational cone. The published geometric note *Unlabeled directional widths determine a right circular cone* determines the complete directional-width **density**, including the aspect-ratio transition at \(\sqrt3\), and therefore contains sufficient information to derive the basic moments by integration. Its inspected full text gives neither (4)–(6) nor the unique mean-square optimum and its separation from the worst-case optimum. The endpoint ratio (7) is an existing consequence of that earlier density study, **not** claimed as a new result. A separate published width-variance extremal result concerns graphical tree zonotopes, not cones or the coefficient-of-variation optimum. The present claimed addition is the exact optimization and global uniqueness theorem, not the generic idea of random width, the support formula, or a rediscovery of the complete width density.

## Limitations

The unique optimum is relative to the family of **solid right circular cones in \(\mathbb R^3\)** and the specific squared relative standard-deviation objective, rather than a universal best shape. Directional variance weights all orientations equally; other weighting schemes can select different shapes. The exact \(4.11\%\) figure describes ideal Haar directions, not measurement noise or finite-sample optimality. Moment formulas are elementary consequences of the support function and of previously available full-density information, so the originality claim is confined to rigorous global minimization and its distinctness from the sharp worst-direction shape. Historical overlap risk remains for older unindexed computations of cone width-dispersion optima. No independent mathematical audit has been performed.

## References

1. Omri Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202v1, first public date recorded 2026-08-10, https://arxiv.org/abs/2609.26202v1 . See introduction, Sections 6.7 and 6.12 for width moments and variance.
2. *Unlabeled directional widths determine a right circular cone*, published geometry research note, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-unlabeled-directional-widths-determine-a-right-circular-cone--30a3b32d19eb . See the full exact density, support endpoint formula, and inverse reconstruction result.
3. *Sharp width-variance extremizers among tree graphical zonotopes*, published geometry research note, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-width-variance-extremizers-among-tree-graphical-zonotopes--482983ab9269 . A related variance extremization problem for a different class of convex bodies.
4. R. Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, second expanded edition, Cambridge University Press, 2014. Standard support-function and mean-width background.
