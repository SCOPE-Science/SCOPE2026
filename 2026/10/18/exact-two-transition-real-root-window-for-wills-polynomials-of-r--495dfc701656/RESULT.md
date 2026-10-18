# Exact two-transition real-root window for Wills polynomials of right circular cones

## Finding
For a solid right circular cone \(K_{r,h}\subset\mathbb R^3\) of base radius \(r>0\) and height \(h>0\), set \(t=h/r\). Its intrinsic-volume (Wills) polynomial has the same root types as
\[
G_t(z)=1+m(t)z+\frac{\pi}{2}s(t)z^2+\frac{\pi t}{3}z^3,
\quad m(t)=t+\pi-\arctan t,\quad s(t)=1+\sqrt{1+t^2}.
\]
Put
\[
Q(t)=m(t)^2-\frac{3\pi}{2}s(t),\qquad
H(t)=2m(t)^3-\frac{9\pi}{2}m(t)s(t)+9\pi t.
\]
On the set \(Q(t)>0\), define \(F_\pm(t)=H(t)\pm2Q(t)^{3/2}\). There are exactly two positive parameters \(\alpha<\beta\), uniquely characterized by
\[
F_+(\alpha)=0,\qquad F_-(\beta)=0,\qquad
\alpha=1.7602188991659217\ldots,\quad
\beta=1.8972451274494761\ldots.
\]
The root-type diagram (with multiplicities) is exhaustive:
\[
\begin{array}{c|c}
0<t<\alpha&\text{one negative real root and two nonreal conjugate roots}\\
t=\alpha&\text{one simple and one double negative real root}\\
\alpha<t<\beta&\text{three distinct negative real roots}\\
t=\beta&\text{one simple and one double negative real root}\\
t>\beta&\text{one negative real root and two nonreal conjugate roots}.
\end{array}
\]
Both transitions are simple sign transitions of the cubic discriminant. In contrast with the corresponding cone *Steiner* polynomial, whose real-root interval is much wider, the Wills real-root window is narrow.

## Assumptions and scope
For a convex body \(K\subset\mathbb R^3\), write \(V_j(K)\), \(0\le j\le3\), for the Euclidean intrinsic volumes normalized by
\[
\operatorname{vol}_3(K+\lambda B_3)
=\sum_{j=0}^3\kappa_{3-j}V_j(K)\lambda^{3-j},
\qquad (\kappa_0,\kappa_1,\kappa_2,\kappa_3)=(1,2,\pi,4\pi/3).
\]
The Wills polynomial is \(g_K(z)=\sum_{j=0}^3V_j(K)z^j\). This convention makes \(V_0(K)=1\) for a full-dimensional convex body. \(K_{r,h}\) is the convex hull of a circular disk of radius \(r\) in one plane and a point on its perpendicular axis at distance \(h\) from that plane. No truncation, obliqueness, or degeneracy is included. All roots are counted over \(\mathbb C\).

## Proof
**Intrinsic volumes.** Scaling reduces the analysis to \(r=1\). The base area and lateral area give
\[
V_3(K_{1,t})=\pi t/3,\qquad
V_2(K_{1,t})=\pi(1+\sqrt{1+t^2})/2.
\]
For \(u\in S^2\) with last coordinate \(v\in[-1,1]\), the support function is
\[
h_{K_{1,t}}(u)=\max\{\sqrt{1-v^2},tv\}.
\]
The two terms exchange at \(v=1/\sqrt{1+t^2}\). The mean-support formula
\(V_1(K)=\pi^{-1}\int_{S^2}h_K(u)\,d\omega(u)\), hence
\(V_1(K_{1,t})=2\int_{-1}^1h_{K_{1,t}}(v)\,dv\), yields
\[
V_1(K_{1,t})=\pi+t-\arctan t=m(t).
\]
In general, \(V_j(K_{r,h})=r^jV_j(K_{1,t})\), so \(g_{K_{r,h}}(z)=G_t(rz)\). Positive scaling does not alter root type.

**Discriminant.** The reciprocal polynomial is the monic cubic
\[
z^3g_{K_{1,t}}(1/z)=z^3+mz^2+\frac{\pi s}{2}z+\frac{\pi t}{3}.
\]
Its discriminant, equal in sign to that of \(G_t\), is
\[
\Delta(t)=\frac{4Q(t)^3-H(t)^2}{27}.
\]
Thus \(\Delta>0\) means three distinct real roots, \(\Delta<0\) means one real and two nonreal roots, and \(\Delta=0\) is a repeated-root boundary. A real root must be negative because the reciprocal cubic has strictly positive coefficients and hence no nonnegative real root.

**A positivity identity.** Set \(x=t/\sqrt{1+t^2}\). Direct differentiation gives \(m'=x^2\) and \(s'=x\). On \(Q>0\), differentiation and completion of squares yield
\[
\boxed{\quad F_\pm'(t)
=3\left(x(t)(m(t)\pm\sqrt{Q(t)})-\frac{3\pi}{4}\right)^2
+\frac{9\pi}{16}(16-3\pi)>0.\quad}
\]
This proves strict monotonicity of *both* transition functionals on *every* component of \(\{t>0:Q(t)>0\}\).

**Exclusion of hidden transition components.** We next prove the strict inequality
\[
\boxed{\ m(t)^3>9\pi t\quad\text{for every }t>0.\ }
\]
Because \(\arctan\) is concave for positive arguments and \(\arctan(3/2)<\pi/3\), its tangent at \(3/2\) gives
\[
m(t)>\frac9{13}t+\frac{2\pi}{3}+\frac6{13}=:at+b.
\]
For \(a,b>0\), elementary one-variable minimization gives \((at+b)^3/t\ge(27/4)ab^2\), with equality at \(t=b/(2a)\). Here
\[
\frac34ab^2-\pi
=\frac{507\pi^2-1495\pi+243}{2197}>0.
\]
Indeed the displayed quadratic is positive at \(\pi=3\) (its numerator is \(321\)) and has strictly positive derivative throughout \([3,\infty)\). The boxed inequality follows.

Whenever \(Q(t)=0\), the equality \(m^2=3\pi s/2\) therefore implies
\[
H(t)=9\pi t-m(t)^3<0.
\]
At \(t=0\), \(Q(0)=\pi(\pi-3)>0\) and
\[
F_+(0)=\pi^2(2\pi-9)+2[\pi(\pi-3)]^{3/2}<0.
\]
For the last sign, the classical bounds \(3<\pi<22/7\) give \(\pi(\pi-3)<22/49<1\) and \(\pi^2(2\pi-9)<-171/7\). Also \(F_-(0)<F_+(0)\).

Since \(Q(t)=t^2+O(t)\) as \(t\to\infty\), the open set \(Q>0\) has a unique unbounded component, possibly beginning at zero. On each bounded component, the common endpoint value \(F_+(b)=F_-(b)=H(b)<0\) at its right boundary \(Q(b)=0\), together with strict monotonicity, makes both functions negative throughout that component. On the unbounded component, their left values are likewise negative (either the values at zero, or the limit \(H<0\) at a finite endpoint). The strict positive lower bound on their derivatives forces both functions to tend to \(+\infty\). Each therefore has exactly one zero in this final component. Since \(F_+>F_-\) for \(Q>0\), the zero \(\alpha\) of \(F_+\) precedes the zero \(\beta\) of \(F_-\).

For \(Q\le0\), \(4Q^3-H^2<0\), including \(Q=0\) by the preceding strict bound. On \(Q>0\), the factorization \(27\Delta=-F_+F_-\) and the established signs now give exactly the five phases in the finding, and no other transitions. At each boundary \(Q>0\) and the other \(F\)-factor is nonzero, so the repeated root is exactly double, not triple. All real roots are negative as noted above.

## Verification
The accompanying self-contained `verify.py` checks the intrinsic-volume coefficients, the differentiated square identity (using symbolic algebra), the exact rational inequality that excludes concealed crossings, and numerical discriminant signs on both sides of each transition. It also recomputes the two reported root values at high precision. The numerical calculations check, but are not substituted for, the global analytic argument; in particular, finite samples alone would not exclude additional transitions.

## Relationship to prior work
Hernández Cifre and Yepes Nicolás (2013) define the Wills polynomial using these intrinsic-volume coefficients, establish universal root-location results in dimensions two and three, and compare Wills and Steiner polynomials. Their general root cone and coefficient results do **not** imply a cone-specific all-aspect-ratio discriminant classification.

Saorín (2009) provides explicit volume, surface area and mean-curvature formulas for right circular cones in the context of the *Steiner* polynomial. A separate published cone Steiner-root phase classification gives transition ratios approximately \(1.15239\) and \(3.37108\), not the two Wills values above. The two polynomials rescale coefficients by different unit-ball volumes, so their discriminants are distinct: the Steiner result neither states nor directly implies the present Wills classification. Henk, Hernández Cifre and Saorín (2011) classify root cones for *relative Steiner* polynomials. Hernández Cifre and Yepes Nicolás (2015) treat general measure-weighted Wills polynomials and root cones, but neither treatment yields this fixed-body all-parameter Wills discriminant. Searches for Wills/Steiner aliases, both aspect-ratio transitions, right circular cones, and the cubic discriminant found no stronger Wills-specific phase statement in the inspected sources.

## Limitations
The theorem concerns the Wills polynomial in exactly three Euclidean dimensions and one cone family. It does not give elementary closed forms for the two transcendental thresholds, nor classify oblique or truncated cones. The root-type result does not prescribe individual complex-root locations. Historical literature access was substantial but not exhaustive, so unindexed equivalent prior formulations remain possible. There is no independent audit.

## References
1. M. A. Hernández Cifre and J. Yepes Nicolás, *On the roots of the Wills functional*, Journal of Mathematical Analysis and Applications **401** (2013), 733–742. DOI: 10.1016/j.jmaa.2012.12.065 (complete open author preprint inspected; first posted in September 2012, exact day not established).
2. E. Saorín, *On Hadwiger's problem on inner parallel bodies*, Banach Center Publications **84** (2009), 121–129. DOI: 10.4064/bc84-0-8 (full open-access paper inspected, including cone example).
3. M. Henk, M. A. Hernández Cifre and E. Saorín, *Steiner polynomials via ultra-logconcave sequences*, arXiv:1112.4741v1 (public 20 December 2011).
4. M. A. Hernández Cifre and J. Yepes Nicolás, *On the roots of generalized Wills μ-polynomials*, Revista Matemática Iberoamericana **31** (2015), 477–496. DOI: 10.4171/RMI/842 (author preprint inspected).
5. *Complete two-transition Steiner-root phase diagram for right circular cones*, publicly accessible research record (2026); https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-two-transition-steiner-root-phase-diagram-for-right-cir--645636c244de (full result materially compared, as a different coefficient normalization).
