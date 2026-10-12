# Universal BFGS counterexample objective with parameter-dependent starts, and a common-start obstruction
## Finding

Let \(\mathcal C\) be the conjugate-descent class in Diao's counterexample: it contains full-memory BFGS, L-BFGS with arbitrary memory, the Broyden positive family, and Hestenes--Stiefel conjugate gradient when the line search returns the first local minimizer on each search ray.

There exists one function
\[
F\in C^\infty(\mathbb R^2)
\]
that is bounded below and has globally Lipschitz gradient, independent of the line-search constants, with the following property:

\[
\forall\,0<c_1<c_2<1\quad
\exists\,x_0(c_1,c_2)
\]
such that every method in \(\mathcal C\), started at that point with the standard steepest first ray and using the first-local-minimizer line search, follows an infinite trajectory on which the gradient norm stays bounded away from zero and every accepted step satisfies strong Wolfe, weak Wolfe, Armijo, and Goldstein with constants \((c_1,c_2)\).

The initialization is allowed to depend on \((c_1,c_2)\), but the objective \(F\) does not.

There is also a sharp obstruction to strengthening this statement to one common initialization. If \(F\), the initial point, the initial ray, and the first-local-minimizer rule are fixed, then the first step is fixed. Its normalized decrease ratio
\[
R=
\frac{F(x_1)-F(x_0)}
     {\langle\nabla F(x_0),x_1-x_0\rangle}
\]
is therefore fixed, whereas Goldstein with constants \((c_1,c_2)\) requires
\[
c_1\le R\le c_2.
\]
No real number belongs to every interval with
\[
0<c_1<c_2<1.
\]
Hence simultaneous Goldstein validity for all parameter pairs is impossible from one common first-local-minimizer initialization.

This resolves the quantifier split:
\[
\exists F\;\forall(c_1,c_2)\;\exists x_0
\]
is achievable, while the stronger common-start interpretation
\[
\exists F\;\exists x_0\;\forall(c_1,c_2)
\]
is impossible when the same first-local-minimizer first step must satisfy Goldstein for every pair.

## Assumptions and scope

The construction uses the exact tubular counterexamples of Diao. For a tube width
\[
0<\delta\le\frac1{20},
\]
that construction gives a smooth function \(f\), constant outside its tubular neighborhood, with
\[
f(x)\ge f_\infty-2\delta
\]
and
\[
\|\nabla^2 f(x)\|\le \frac K{\delta^2}
\]
for a universal constant \(K\). Along its designed orbit, every step is a first local minimizer and the endpoint gradient is orthogonal to the step.

The source's axial-curvature interpolation produces a normalized decrease ratio \(r(\lambda)\) that is affine in the split parameter and satisfies
\[
r(1)<6\delta,
\qquad
r(0)>1-6\delta.
\]
Therefore any prescribed
\[
q\in(0,1)
\]
can be realized by choosing
\[
\delta(q)
=
\min\left\{
\frac1{20},
\frac q{12},
\frac{1-q}{12}
\right\}.
\]
Indeed,
\[
6\delta(q)<q<1-6\delta(q).
\]

The positive universal statement allows the initial point to depend on the line-search constants. The negative statement concerns a fixed objective, fixed initial point and ray, and the same first-local-minimizer rule.

## Proof

Enumerate the rationals in the open unit interval:
\[
\mathbb Q\cap(0,1)=\{q_1,q_2,\ldots\}.
\]
For each \(q_n\), set
\[
\delta_n
=
\min\left\{
\frac1{20},
\frac{q_n}{12},
\frac{1-q_n}{12}
\right\}.
\]
Then
\[
r(1)<6\delta_n<q_n<1-6\delta_n<r(0),
\]
so the source interpolation admits split parameters on every segment that make the normalized decrease ratio exactly \(q_n\).

Let \(f_n\) denote the resulting source counterexample and let \(a_n\) be its exterior constant. Define
\[
\phi_n=f_n-a_n.
\]
Then \(\phi_n\) is globally smooth, equals zero outside its source tube, and satisfies
\[
\phi_n\ge-2\delta_n,
\qquad
\|\nabla^2\phi_n\|\le \frac K{\delta_n^2}.
\]

Now put
\[
b_n=\delta_n^{-1}
\]
and spatially rescale:
\[
\psi_n(x)
=
\phi_n\left(\frac{x}{b_n}\right).
\]
The rescaled Hessian obeys
\[
\|\nabla^2\psi_n(x)\|
=
b_n^{-2}
\left\|
\nabla^2\phi_n\left(\frac{x}{b_n}\right)
\right\|
\le K.
\]
The rescaled orbit gradient norm is
\[
b_n^{-1}=\delta_n>0.
\]
Hence each rescaled copy remains nonstationary forever, while all copies now have one uniform Hessian bound.

Spatial scaling preserves every normalized line-search ratio. If a source step is \(s\), the rescaled step is \(b_ns\), while the gradient is divided by \(b_n\), so
\[
\left\langle
b_n^{-1}\nabla\phi_n,
b_ns
\right\rangle
=
\langle\nabla\phi_n,s\rangle.
\]
Function differences are unchanged. Exact endpoint orthogonality and the conjugate-descent ray conditions are preserved for the same reason.

It remains to place the copies disjointly. Let
\[
s_*=
\left(
\frac{\sqrt3}{2},
\frac12
\right)
\]
be the source's limiting step direction, and let \(e_*\) be a perpendicular unit vector. The source headings differ from the limiting heading by
\[
\frac{\pi}{3\cdot2^{k+1}}
\]
in absolute value. Therefore the total transverse displacement of its center polyline is bounded by
\[
\sum_{k\ge0}
\frac{\pi}{3\cdot2^{k+1}}
=
\frac{\pi}{3}.
\]
Including the tubular width and the finite backward extension, the source tube is contained in a strip of finite half-width, for example
\[
\frac{\pi}{3}+2\delta_n.
\]
After scaling, copy \(n\) is therefore contained in a strip of half-width
\[
W_n
=
\frac{\pi}{3\delta_n}+2.
\]

Choose translations \(L_ne_*\) recursively so that
\[
L_{n+1}
>
L_n+W_n+W_{n+1}+1.
\]
The translated containing strips are pairwise disjoint and locally finite. Define
\[
\Psi_n(x)
=
\psi_n(x-L_ne_*),
\qquad
F(x)=\sum_{n=1}^{\infty}\Psi_n(x).
\]
The sum is locally finite, and at every point at most one summand is nonzero. Thus
\[
F\in C^\infty(\mathbb R^2),
\qquad
\|\nabla^2F\|\le K.
\]
Moreover,
\[
F(x)\ge-\sup_n2\delta_n\ge-\frac1{10},
\]
so \(F\) is bounded below.

Fix arbitrary
\[
0<c_1<c_2<1.
\]
Choose a rational \(q_n\) satisfying
\[
c_1<q_n<c_2.
\]
Initialize the method on the translated and rescaled orbit of copy \(n\). Every designed step has normalized decrease ratio \(q_n\), so it satisfies Armijo and Goldstein:
\[
c_1<q_n<c_2.
\]
Because the step ends at an exact local minimizer on the search ray, the endpoint directional derivative is zero, so both weak and strong Wolfe curvature conditions hold for every \(c_2\in(0,1)\). The first-local-minimizer property is unchanged before the designed step because that segment lies inside its own copy and the supports are disjoint. Every method in \(\mathcal C\) therefore follows the source orbit, with
\[
\|\nabla F(x_k)\|=\delta_n>0
\]
for every \(k\).

For the common-start obstruction, fix \(F\), \(x_0\), and the initial descent ray. The first-local-minimizer rule chooses one fixed first step \(s_0\), independent of \((c_1,c_2)\). Its ratio \(R\) is fixed. Goldstein for a pair \((c_1,c_2)\) is equivalent to
\[
c_1\le R\le c_2.
\]
For any real \(R\), one can choose an interval
\[
0<c_1<c_2<1
\]
that excludes \(R\). Hence no common first step can satisfy Goldstein for every parameter pair.

## Verification

The standalone script `artifacts/verify_universal_gluing.py` checks the exact calibration inequalities on a deterministic enumeration of rational target ratios, verifies the Hessian and gradient scaling identities, checks a finite prefix of the disjoint-strip recursion, and verifies representative Goldstein-interval exclusions.

Those finite checks are not the proof of the infinite construction. The proof uses density of \(\mathbb Q\), local finiteness of pairwise disjoint translated strips, the source's global smooth extension and uniform \(K/\delta^2\) Hessian bound, and the elementary Goldstein interval argument.

## Relationship to prior work

Diao constructs, for every prescribed pair \((c_1,c_2)\), a parameter-specific smooth lower-bounded objective with Lipschitz gradient and explicitly leaves open whether the dependence of the objective on the line-search parameters can be eliminated. The same paper already provides the three structural ingredients needed here: arbitrary placement of the normalized decrease ratio inside \((0,1)\), a function that is constant outside its tube, and the Hessian estimate \(K/\delta^2\).

The new step is to separate the line-search ratio from the parameter pair, retain only a countable dense set of target ratios, normalize every tube's Hessian bound by spatial scaling, and place the resulting copies in disjoint parallel strips. Density then covers the uncountable parameter triangle with one objective.

Related recent quasi-Newton counterexamples also use pairwise disjoint smooth supports to interpolate prescribed behavior, showing that disjoint-support assembly is a legitimate technique in this area. They do not provide the dense-ratio universalization above or the associated common-start Goldstein obstruction.

The result should not be read as asserting one common initialization for all line-search constants. On the contrary, the second half proves that such a strengthening is impossible if Goldstein is required for all pairs and the first-local-minimizer first ray is fixed.

## Limitations

The positive construction is existential and highly noncompact. Its parameter-dependent starting points lie in different translated copies, and the copies may be arbitrarily far apart.

The result preserves a uniform Lipschitz constant for the gradient, but it does not claim bounded level sets; the source counterexample mechanism necessarily uses an escaping trajectory.

The negative common-start statement uses simultaneous Goldstein validity. If Goldstein is dropped and only Armijo plus Wolfe conditions are imposed, the first-step interval obstruction no longer applies in this form.

No claim is made that the displayed disjoint-copy construction is minimal or numerically practical.

## References

1. R. Diao, *Counterexamples for BFGS-type methods under arbitrary strong Wolfe constants*, arXiv:2609.09686v1, 2026.
2. B. Liu, Z. Wang, Z. Wen, L. Zhang, Y. Yuan, *A counterexample to global convergence of classical DFP under the standard strong Wolfe conditions*, arXiv:2608.21708, 2026.
