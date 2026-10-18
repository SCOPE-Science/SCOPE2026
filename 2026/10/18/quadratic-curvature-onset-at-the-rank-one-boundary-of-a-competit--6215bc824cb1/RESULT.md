# Quadratic curvature onset at the rank-one boundary of a competitive rational map

## Finding

Consider the positive-plane rational family
\[
T_\varepsilon(x,y)=\left(\frac{b x}{A+y},\frac{d(A+y)+\varepsilon}{x}\right),
\qquad A,d>0,\quad b>A,\quad x>0,\ y\geq0,
\]
where \(\varepsilon\) is real and \(Ad+\varepsilon>0\). Put \(q=b-A>0\) and \(B=2b-A>0\). The saddle equilibrium is \(E_\varepsilon=((bd+\varepsilon)/q,q)\). At the singular parameter \(\varepsilon=0\), the **entire positive stable set** of \(E_0\) is the straight line
\[
\mathcal C_0:\quad x=s_0(y):=\frac{d(A+y)}q,\qquad y\geq0.
\]
Every point of this line maps to \(E_0\) in one iteration. On opposite sides, trajectories respectively escape toward \((0,+\infty)\) and \((+\infty,0)\), in the sense detailed below.

The local-to-global stable separatrix near this line has a **nonzero quadratic curvature onset**. More precisely, for any compact interval \(K\subset[0,\infty)\), and all sufficiently small \(|\varepsilon|\), its unique stable-set graph \(x=s_\varepsilon(y)\) in a fixed neighborhood of \(\mathcal C_0\) over \(K\) admits, uniformly in the \(C^2(K)\) norm,
\[
\boxed{\displaystyle
s_\varepsilon(y)=\frac{d(A+y)}q
+\varepsilon\frac{b+y}{qB}
+\varepsilon^2\frac{q(y-q)}{dB^3(A+y)}
+O_K(\varepsilon^3).}
\]
Consequently
\[
\boxed{\displaystyle
\partial_y^2s_\varepsilon(y)
=-\frac{2bq}{dB^3(A+y)^3}\,\varepsilon^2
+O_K(\varepsilon^3),}
\]
and the perturbed separatrix is strictly concave on every prescribed compact \(K\) whenever \(\varepsilon\ne0\) is sufficiently small. Notably, the first-order displacement is affine in \(y\): curvature does not appear until second order, and its leading sign is the same on both sides of the rank-one parameter.

## Assumptions and scope

All three base parameters \(A,b,d\) are fixed positive real numbers with \(b>A\). The parameter \(\varepsilon\) varies near zero so that the second numerator remains positive. The state space is \((0,\infty)\times[0,\infty)\). The stable-set graph statement is **local in parameter and uniform only on specified compact \(y\)-intervals**, not a uniform expansion along the entire noncompact separatrix. Here a point belongs to the stable set if its forward orbit tends to \(E_\varepsilon\). Curvature is \(\partial_y^2s_\varepsilon\) in the original \((x,y)\) coordinates, not Euclidean curvature or an invariant curvature under coordinate changes.

## Proof

### Exact rank-one geometry and the basin split

At \(\varepsilon=0\), direct substitution gives \(x_1y_1=bd\) for every permitted initial state. Thus for every \(n\ge1\),
\[
 y_n=\frac{bd}{x_n},\qquad
 x_{n+1}=g(x_n):=\frac{b x_n^2}{A x_n+bd}.
\]
The scalar map \(g\) is increasing on positive inputs, and
\[
 g(x)-x=\frac{x(qx-bd)}{Ax+bd}.
\]
It has the unique positive fixed point \(x_*=bd/q\). For \(0<x_1<x_*\), the sequence decreases to zero and \(y_n\to\infty\); for \(x_1>x_*\), it increases without bound and \(y_n\to0\). Equality holds exactly when \(x_0=d(A+y_0)/q\), yielding \(T_0(x_0,y_0)=E_0\). These exhaust all initial conditions, proving the entire stable-line assertion and basin separation. The invariant curve \(xy=bd\) is reached after one step. Differentiating the family also gives
\[
 \det DT_\varepsilon(x,y)=-\frac{b\varepsilon}{x(A+y)^2},
\]
so the boundary parameter is exactly where the map drops rank.

### Existence of a smooth perturbed stable graph

For every small \(\varepsilon\), the point \(E_\varepsilon=((bd+\varepsilon)/q,q)\) is an equilibrium. At \(\varepsilon=0\), its Jacobian has eigenvalues \(0\) and \(B/b>1\), and its stable eigendirection is tangent to \(x=s_0(y)\). Thus the equilibrium is hyperbolic for a real-analytic endomorphism. The parameter-dependent smooth stable-manifold theorem yields a smooth local stable curve near \(E_\varepsilon\), representable as \(x=\sigma_\varepsilon(y)\) for \(y\) near \(q\); \(\sigma_0(y)=s_0(y)\) there.

Fix compact \(K\subset[0,\infty)\). Every point \((s_0(y),y)\), with \(y\in K\), maps **exactly** to \(E_0\). Therefore, for all sufficiently small \(\varepsilon\), the equation
\[
 \frac{bx}{A+y}-\sigma_\varepsilon\!\left(\frac{d(A+y)+\varepsilon}{x}\right)=0
\]
is well-defined in a tubular neighborhood of \(\mathcal C_0\) over \(K\). At \(\varepsilon=0\), its derivative with respect to \(x\), evaluated on the line, equals
\[
 \frac{B}{A+y}>0.
\]
The smooth implicit-function theorem, uniformly over \(K\), gives a unique smooth graph \(x=s_\varepsilon(y)\) there, mapped in one step into the local stable manifold. Thus it consists of points converging to \(E_\varepsilon\). For \(\varepsilon\ne0\), the global separating stable manifold identified in Theorem 2.3 of Reference 2 contains this branch; local stable-set uniqueness around the equilibrium, combined with its strictly increasing graph property, identifies the branch near the original line. On overlaps the implicitly constructed branches agree by uniqueness. It follows that their parameter Taylor expansions, together with two \(y\)-derivatives, have uniformly bounded third-order remainders on compact intervals.

### Evaluation of the first nontrivial bending coefficient

The graph satisfies the exact invariance identity
\[
 \frac{b s_\varepsilon(y)}{A+y}
 =s_\varepsilon\!\left(\frac{d(A+y)+\varepsilon}{s_\varepsilon(y)}\right).
\]
Write \(s_\varepsilon=s_0+\varepsilon u+\varepsilon^2 v+O_K(\varepsilon^3)\). Because the graph passes through the equilibrium at \(y=q\), we have \(u(q)=1/q\) and \(v(q)=0\). Expanding the invariance identity at first order uniquely gives
\[
 u(y)=\frac{b+y}{qB}.
\]
Indeed, the inner argument is \(q+\varepsilon w_1+O(\varepsilon^2)\), with \(w_1=q(q-y)/(dB(A+y))\). The first-order equation is \(bu(y)/(A+y)=(d/q)w_1+u(q)\).

At second order, the inner argument equals \(q+\varepsilon w_1+\varepsilon^2 w_2+O_K(\varepsilon^3)\), with
\[
 w_2=\frac{q^2(qu(y)^2-u(y))}{d^2(A+y)^2}
 -\frac{q^2v(y)}{d(A+y)}.
\]
Equating quadratic coefficients gives
\[
 \frac{b v(y)}{A+y}=\frac d q w_2+u'(q)w_1+v(q),
 \qquad u'(q)=\frac1{qB},\quad v(q)=0.
\]
Solving this linear identity yields the unique coefficient
\[
 v(y)=\frac{q(y-q)}{dB^3(A+y)}.
\]
Twice differentiating gives \(v''(y)=-2bq/[dB^3(A+y)^3]\), strictly negative. The smooth \(C^2\)-remainder implies the stated strict concavity on each compact interval for every sufficiently small nonzero perturbation.

## Verification

A standalone exact-arithmetic checker `verify.py` independently confirms: the one-step product identity, equilibrium, determinant and eigenvalue formulas; the first- and second-order invariance residuals vanish symbolically; and the second derivative is strictly negative on the prescribed parameter domain. Finite numerical shooting at representative parameter values, including both signs of \(\varepsilon\), confirms cubic-order approximation errors. Those computations are independent checks of algebra and examples, not a substitute for the smooth stable-manifold/implicit-function argument proving uniform existence and all-parameter coverage.

## Relationship to prior work

Camouzis, Kulenović, Ladas, and Merino identified the rational pair corresponding to system (14,21) as a global-dynamics problem in 2009. Garić-Demirović, Kulenović, and Nurkanović settled its qualitative global basin decomposition for the nondegenerate parameter range in Theorems 2.1–2.3 of their 2009 article. Their Remark 2.4 **explicitly records the degenerate scalar reduction** when \(\alpha_2=A_1\gamma_2\). This reduction and the qualitative trichotomy are therefore prior art, not claimed discoveries here. The present claim is instead the exact stable line and, principally, the **first two parameter derivatives of the stable-set graph**, giving a new explicit quadratic, strictly concave unfolding of the separatrix on compact intervals. The cited general invariant-manifold theorems guarantee existence and monotonicity but do not supply this parameter expansion. Priority remains subject to earlier results not indexed by the searches described in the accompanying review.

## Limitations

The result applies only to the one-parameter perturbation of this specific family with fixed \(A,b,d\) and \(b>A\). It does not establish a global-in-\(y\) error estimate, a universal curvature property away from the degenerate surface, or convergence rates of general orbits for \(\varepsilon\ne0\). The underlying one-dimensional reduction and the already-known qualitative basin dichotomy are not original contributions.

## References

1. E. Camouzis, M. R. S. Kulenović, G. Ladas, and O. Merino, “Rational systems in the plane,” *Journal of Difference Equations and Applications* **15** (2009), 303–323. DOI: `10.1080/10236190802125264` (first published online 2009-02-16).
2. M. Garić-Demirović, M. R. S. Kulenović, and M. Nurkanović, “Global Behavior of Four Competitive Rational Systems of Difference Equations in the Plane,” *Discrete Dynamics in Nature and Society* **2009**, Article ID 153058. DOI: `10.1155/2009/153058`; especially Theorems 2.1–2.3 and Remark 2.4.
3. G. Lugo and F. J. Palladino, “On competitive discrete systems in the plane. I. Invariant Manifolds,” arXiv:`1203.0703` (2012), for general invariant-curve context.
