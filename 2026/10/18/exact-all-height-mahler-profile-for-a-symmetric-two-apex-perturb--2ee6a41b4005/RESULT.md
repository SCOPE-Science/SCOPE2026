# Exact all-height Mahler profile for a symmetric two-apex perturbation of the four-cube

## Finding

Let \(C=[-1,1]^4\) and, for each real \(t>0\), define the centrally symmetric polytope
\[
P_t=\operatorname{conv}\big(C\cup\{\pm(1,1,1+t,1),\ \pm(1,1,1,1+t)\}\big).
\]
Its polar is \(P_t^\circ=\{y:\langle x,y\rangle\le1\text{ for all }x\in P_t\}\). Denote four-dimensional Lebesgue volume by \(|\cdot|\). The two volumes are exactly
\[
|P_t|=\begin{cases}
16+8t+\frac23t^2,&0<t\le2,\\
\frac43(t^2+6t+10),&t\ge2,
\end{cases}
\]
and
\[
|P_t^\circ|=\begin{cases}
\displaystyle\frac{-t^5-4t^4+44t^3+272t^2+464t+256}{3(t+2)^3(t+4)^2},&0<t\le2,\\[6pt]
\displaystyle\frac{8(3t^6+26t^5+80t^4+72t^3-88t^2-64t+128)}{3t^3(t+2)^3(t+4)^2},&t\ge2.
\end{cases}
\]
The two formulas in each pair agree at \(t=2\). In particular the Mahler volume \(\Phi(t)=|P_t|\,|P_t^\circ|\) satisfies the **strict four-dimensional cube bound**
\[
\Phi(t)>\frac{4^4}{4!}=\frac{32}{3}\qquad(t>0).
\]
Moreover \(\lim_{t\downarrow0}\Phi(t)=\lim_{t\to\infty}\Phi(t)=32/3\), while \(\Phi(2)=1027/81\). The profile has a genuine angular-combinatorial transition at \(t=2\): its one-sided derivatives are \(\Phi'_-(2)=-433/972\) and \(\Phi'_+(2)=515/972\), so it has a strict cusp local minimum there.

## Assumptions and scope

All constructions use ordinary Euclidean coordinates and volume in \(\mathbb R^4\); the polar is taken with respect to the origin. The height parameter ranges over every \(t>0\), not only small perturbations. There are exactly two marked positive facet apices and their negatives, with no extra points. The result is a complete exact computation and strict bound **only for this specified one-parameter family**, not an assertion about arbitrary centrally symmetric four-dimensional convex bodies.

## Proof

**Step 1: a two-dimensional difference-body transition.** Put \(S=[-1,1]^2\) and
\[
H_t=\operatorname{conv}\{(-1,-1),(1,-1),(1+t,1),(1,1+t),(-1,1)\}.
\]
Its area is \(A_t=4+2t+t^2/2\), and its coordinate widths are both \(2+t\). Writing \(D_t=|H_t-H_t|\), direct polygonal convex-hull and shoelace calculation gives
\[
D_t=\begin{cases}16+12t+t^2,&0<t\le2,\\8+12t+3t^2,&t\ge2.\end{cases}
\]
For reproducibility, here are all ten counterclockwise vertices of \(H_t-H_t\) in the first chamber, with consecutive ordered pairs separated by semicolons:
\[
(-t-2,-2);\ (-2,-t-2);\ (0,-t-2);\ (2,-2);\ (t+2,0);\
(t+2,2);\ (2,t+2);\ (0,t+2);\ (-2,2);\ (-t-2,0).
\]
In the second chamber replace \((2,-2)\) by \((t,-t)\), and \((-2,2)\) by \((-t,t)\), retaining the order. Every listed vertex is a difference of two vertices of \(H_t\); conversely, the oriented determinant of every proposed boundary edge with each of the 25 vertex differences is nonnegative throughout its chamber. Thus the lists are exhaustive, not just numerical hull guesses. The two changes of active difference vertices occur at \(t=2\), giving the displayed shoelace areas.

**Step 2: exact primal volume by fibers.** Make the linear change \(p=(x_1+x_2)/2\), \(q=(x_1-x_2)/2\), whose absolute Jacobian is \(2\). Let
\[
Q_t=\operatorname{conv}\big((\{1\}\times H_t)\cup(\{-1\}\times(-H_t))\big)\subset\mathbb R^3,
\qquad F=\{0\}\times S.
\]
The \(q\)-fiber of \(P_t\), for \(|q|\le1\), is precisely \((1-|q|)Q_t+|q|F\). This is because the original cube is the convex hull of its \(q=0\) slice and its \(q=\pm1\) square slices, while all four added apices lie at \(q=0\); mixtures of opposite \(q\)-end slices add nothing since \(F\subset Q_t\).

For \(r\in[-1,1]\), the \(p=r\) slice of \(Q_t\) is \(\lambda H_t+(1-\lambda)(-H_t)\), where \(\lambda=(1+r)/2\). For any planar convex \(G\), the area identity
\[
|(1-q)G+qS|=(1-q)^2|G|+2q(1-q)\big(w_x(G)+w_y(G)\big)+4q^2
\]
holds, where \(w_x,w_y\) denote coordinate widths. Its application inside the two nested fibers, followed by the elementary \(q\)-integration, yields
\[
|P_t|=\int_{-1}^1|Q_t(r)|\,dr+\frac23\int_{-1}^1\big(w_x(Q_t(r))+w_y(Q_t(r))\big)\,dr+\frac83.
\]
The first integral equals \((2A_t+D_t)/3\), by polarization of planar area, and the width sum in the second integral is constantly \(4+2t\). Consequently,
\[
|P_t|=\frac23 A_t+\frac13D_t+8+\frac83t,
\]
which proves the two primal-volume formulas.

**Step 3: an exact polar integral.** By polar duality,
\[
P_t^\circ=\big\{y:\ |y_1|+|y_2|+|y_3|+|y_4|\le1,\ 
|y_1+y_2+(1+t)y_3+y_4|\le1,\
|y_1+y_2+y_3+(1+t)y_4|\le1\big\}.
\]
Set \(s=y_1+y_2\), \(u=y_3+y_4\), and \(v=y_3-y_4\). For fixed \(u,v\), the first constraint gives \(|s|\le q_*:=1-\max(|u|,|v|)\). The measure of \((y_1,y_2)\) at prescribed \(s\) is \(q_*\,ds\), because \(|y_1|+|y_2|=\max(|s|,|y_1-y_2|)\). The two remaining constraints cut out an interval in \(s\) with center \(-(1+t/2)u\) and half-width \(h=1-(t/2)|v|\). Reflection symmetry, and the Jacobian \(dy_3\,dy_4=du\,dv/2\), give
\[
|P_t^\circ|=2\int_0^1\int_0^{\min(1,2/t)}(1-\max(u,v))L(u,v)\,dv\,du,
\]
where \(L\) is the length of intersection between \([-q_*,q_*]\) and \([-m-h,-m+h]\), with \(m=(1+t/2)u\). On the integration domain \(u,v\ge0\),
\[
L=(q_*+h-m)_+-(q_*-h-m)_+-(h-q_*-m)_+,
\quad z_+=\max(z,0).
\]
For \(u\ge v\), this simplifies to \(L=(2-(2+t/2)u-tv/2)_+\). For \(v\ge u\), writing \(a=(t+2)/2\), it becomes
\[
L=(2-a(u+v))_+-\big((t-2)v/2-au\big)_+-\big((2-t)v/2-au\big)_+.
\]
All positivity regions are triangles or trapezoids. For transparency, write \(b=2/(t+2)\). The contribution before the overall factor \(2\) is \(J_1+J_0+J_\pm-E_\pm\), with
\[
J_1=\int_0^b\int_v^{(4-tv)/(t+4)}(1-u)\big(2-(t+4)u/2-tv/2\big)\,du\,dv
=\frac{4(2t^2+9t+8)}{3(t+2)^2(t+4)^2},
\]
\[
J_0=\int_0^b\int_0^v(1-v)(2-a(u+v))\,du\,dv
=\frac{6t+5}{3(t+2)^3}.
\]
For \(0<t\le2\), the remaining two integrals are
\[
J_-=\int_b^1\int_0^{4/(t+2)-v}(1-v)(2-a(u+v))\,du\,dv
=\frac{t^2(t^2-8t+24)}{48(t+2)^3},
\]
\[
E_-=\int_0^1\int_0^{(2-t)v/(t+2)}(1-v)\big((2-t)v/2-au\big)\,du\,dv
=\frac{(t-2)^2}{48(t+2)}.
\]
For \(t\ge2\), instead,
\[
J_+=\int_b^{2/t}\int_0^{4/(t+2)-v}(1-v)(2-a(u+v))\,du\,dv
=\frac{4(3t^4-6t^3-2t^2+16t-12)}{3t^4(t+2)^3},
\]
\[
E_+=\int_0^{2/t}\int_0^{(t-2)v/(t+2)}(1-v)\big((t-2)v/2-au\big)\,du\,dv
=\frac{(t-2)^2(2t-3)}{3t^4(t+2)}.
\]
Thus \(|P_t^\circ|=2(J_1+J_0+J_--E_-)\) in the first chamber and \(2(J_1+J_0+J_+-E_+)\) in the second, giving exactly the two stated rational expressions. In fact their algebraic difference, when continued outside their respective chambers, is \((t-2)^4/[3t^3(t+2)]\).

**Step 4: strict Mahler gap and the transition.** Elementary multiplication and factorization yield
\[
\Phi(t)-\frac{32}{3}=
\begin{cases}
\displaystyle\frac{2t\,N_-(t)}{9(t+2)^3(t+4)^2},&0<t\le2,\\[6pt]
\displaystyle\frac{64\,N_+(t)}{9t^3(t+2)^3(t+4)^2},&t\ge2,
\end{cases}
\]
with
\[
N_-(t)=1920+2752t+1136t^2+32t^3-76t^4-16t^5-t^6
\]
and
\[
N_+(t)=t^7+19t^6+106t^5+188t^4-128t^3-568t^2+64t+640.
\]
For \(0<t\le2\), the three negative terms in \(N_-\) have total absolute value at most \(448t^2\), hence \(N_-(t)\ge1920+2752t+688t^2+32t^3>0\). For \(t\ge2\), write \(z=t-2\ge0\); then
\[
N_+(t)=z^7+33z^6+418z^5+2668z^4+9216z^3+16888z^2+14848z+5216>0.
\]
This proves strictness for every positive height. The stated limits, exact value, and unequal one-sided derivatives at \(t=2\) follow by substitution and differentiation of the rational profiles.

## Verification

Run the complete symbolic checker with Python 3 and SymPy: `python verify_profile.py`. It reconstructs the 25 differences of the five vertices of \(H_t\); verifies that both ten-vertex candidate difference polygons contain all differences by chamberwise nonnegative polynomial certificates; checks their exact shoelace areas; symbolically performs all six elementary integrals for the polar volume; factors both strict-gap numerators; and checks the transition values and derivatives. A successful independent run prints `TWO_APEX_4D_EXACT_PROFILE_OK`. No finite sampling is used as a substitute for the chamberwise analytic arguments.

## Relationship to prior work

Shen and Dubovski [1, Theorems 1–3 and Corollary 4] analyze cube-facet-apex families, establish an exact constrained minimum under a polar-denominator product condition, and prove the strict four-dimensional Mahler inequality for this same symmetric two-apex family only through \(0<t\le12/7\), using a lower bound. The present statement supplies the **exact primal and polar volumes and complete strict bound for every \(t>0\)**, including the regime beyond that certificate and a combinatorial nondifferentiability at \(t=2\). The two-apex family is not product-compatible for positive heights (as [1] notes), so its all-height exact profile is not a corollary of the source's constrained extremum. Classical local-minimality results near cubes and Hanner polytopes [2] do not give these global rational formulas. General symmetry-based reverse Santaló bounds [3] concern lower bounds, not the present exact one-parameter profile.

## Limitations

The result says nothing about the full four-dimensional symmetric Mahler conjecture; the strict bound is for the explicitly defined family only. The parameter \(t\) is not a Banach–Mazur distance, and the cusp concerns the chosen parametrization. The analytic method uses a special block symmetry and does not directly cover arbitrary tangential apex coordinates. The complete historical literature may contain equivalent unindexed polytope-volume calculations; independent review has not been performed.

## References

[1] H. Shen and P. B. Dubovski, *A sharp minimum for cube-apex bodies in every dimension*, arXiv:2610.11014v1, first submitted 7 October 2026, especially Section 3 and Corollary 4. https://arxiv.org/abs/2610.11014

[2] J. Kim, *Minimal volume product near Hanner polytopes*, Journal of Functional Analysis 266 (2014), 2360–2402, arXiv:1212.2544. https://arxiv.org/abs/1212.2544

[3] F. Barthe and M. Fradelizi, *The volume product of convex bodies with many hyperplane symmetries*, American Journal of Mathematics 135 (2013), 311–347. https://doi.org/10.1353/ajm.2013.0018
