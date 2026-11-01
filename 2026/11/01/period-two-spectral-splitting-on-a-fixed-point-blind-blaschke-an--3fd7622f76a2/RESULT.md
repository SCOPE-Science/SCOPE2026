# Period-two spectral splitting on a fixed-point-blind Blaschke–Anosov curve

## Finding

Consider the analytic, area-preserving torus map introduced by Bandtlow, Just and Slipantschuk [1]. Its deformation has a natural, nontrivial parameter curve on which the entire derivative at the unique fixed point is exactly the derivative of the undeformed cat map. Nevertheless, **both primitive two-cycles detect the deformation**, with different explicitly determined quadratic coefficients.

**Theorem.** Let \(0<\mu<1\), let \(\alpha(\mu)=\arccos(-\mu)\), and define \(T_\mu:\mathbb T^2\to\mathbb T^2\) by
\[
T_\mu(x,y)=\bigl(2x+y+f_\mu(x),\ x+y+f_\mu(x)\bigr)\pmod1,
\]
where
\[
f_\mu(x)=\frac1\pi\arctan\!\left(\frac{\mu\sin(2\pi x-\alpha(\mu))}{1-\mu\cos(2\pi x-\alpha(\mu))}\right).
\]
There is a constant \(\varepsilon>0\) such that, for every \(0<\mu<\varepsilon\), the following statements hold.

1. The unique fixed point is \(q_\mu=(\arcsin(\mu)/\pi,0)\) modulo \(1\), and its **full** derivative is exactly
\[
DT_\mu(q_\mu)=A:=\begin{pmatrix}2&1\\1&1\end{pmatrix}.
\]
2. Let \(\mathcal C_1(\mu)\) and \(\mathcal C_2(\mu)\) be the distinct primitive two-cycles obtained by analytic continuation from the cat-map cycles
\[
\mathcal C_1(0)=\{(4/5,3/5),(1/5,2/5)\},\quad
\mathcal C_2(0)=\{(3/5,1/5),(2/5,4/5)\}.
\]
For any representative \(p_i(\mu)\in\mathcal C_i(\mu)\),
\[
\operatorname{tr}D(T_\mu^2)(p_1(\mu))
=7+\frac{25-7\sqrt5}{2}\mu^2+O(\mu^3),
\]
\[
\operatorname{tr}D(T_\mu^2)(p_2(\mu))
=7+\frac{25+7\sqrt5}{2}\mu^2+O(\mu^3).
\]
The coefficients are strictly positive and unequal. In particular, \(T_\mu\) is **not** \(C^1\)-conjugate to the cat automorphism \(A\) for all sufficiently small positive \(\mu\), despite equality of the full derivative at the unique fixed point.

This is a quantitative distinction in **periodic derivative data**. It does not assert a new existence theorem for Anosov dynamics or a complete classification of all positive parameters.

## Assumptions and scope

Here \(\mathbb T^2=(\mathbb R/\mathbb Z)^2\). The branches of the displayed arctangent are unambiguous because \(1-\mu\cos(2\pi x-\alpha)>0\) for \(0<\mu<1\). All derivatives are derivatives of the smooth torus lift; changing integer representatives does not affect them. The notation \(O(\mu^3)\) is for each specified cycle as \(\mu\downarrow0\), with a constant independent of sufficiently small \(\mu\). The theorem asserts existence of some common positive \(\varepsilon\), not a numerical optimized radius. The fixed point and hyperbolicity of the two-parameter family are known from [1]; the periodic-data calculation is given below independently.

The restriction \(\cos\alpha=-\mu\) is not an arbitrary slice: the known exact fixed-point trace formula [1, equation (5)] equals the cat-map trace \(3\) precisely on this curve when \(\mu>0\). The more precise full-derivative cancellation is verified here.

## Proof

**1. Exact fixed-point invisibility.** Set \(h=\arcsin\mu\), so \(\alpha=\pi/2+h\). The fixed point formula of [1, equation (4)] reduces to \(q_\mu=(h/\pi,0)\). Direct differentiation gives
\[
f_\mu'(x)=\frac{2\mu\bigl(\cos(2\pi x-\alpha)-\mu\bigr)}{1-2\mu\cos(2\pi x-\alpha)+\mu^2}.
\]
At \(x=h/\pi\), the cosine equals \(\cos(h-\pi/2)=\mu\), so \(f_\mu'(h/\pi)=0\). Since
\[
DT_\mu(x,y)=\begin{pmatrix}2+f_\mu'(x)&1\\1+f_\mu'(x)&1\end{pmatrix},
\]
the full fixed-point derivative is \(A\), not merely a matrix with the same trace and determinant.

**2. Analytic continuation of the two cycles.** Write \(a\) and \(b\) for successive first coordinates along a primitive two-cycle. Because the second coordinate at one time is the difference between successive first coordinates modulo one, the two-cycle equations can be lifted as
\[
2b-3a=f_\mu(a)+k,\qquad 2a-3b=f_\mu(b)+\ell,
\]
for locally fixed integers \((k,\ell)\). At \(\mu=0\), the two solutions of interest are respectively
\[
(a,b;k,\ell)=(4/5,1/5;-2,1),\qquad
(a,b;k,\ell)=(3/5,2/5;-1,0).
\]
The Jacobian of the equations with respect to \((a,b)\) at zero deformation is
\[
J=\begin{pmatrix}-3&2\\2&-3\end{pmatrix},\qquad\det J=5.
\]
The real-analytic implicit-function theorem therefore produces a unique analytic solution pair near each seed. Their two points remain distinct, and the two cycles stay disjoint, for sufficiently small positive \(\mu\).

**3. First position correction.** With \(X=2\pi x\) and \(\alpha=\pi/2+\mu+O(\mu^3)\), the defining arctangent has the uniform expansion
\[
f_\mu(x)=-\frac{\mu}{\pi}\cos X-\frac{\mu^2}{\pi}\left(\sin X+\frac12\sin(2X)\right)+O(\mu^3).
\]
The error and its first derivative are uniform on the circle. In either seed cycle the initial cosine values at \(a_0\) and \(b_0\) agree; put \(c=\cos(2\pi a_0)=\cos(2\pi b_0)\). Differentiating the two lifted equations at \(\mu=0\) yields the common displacement
\[
a(\mu)=a_0+\frac{c}{\pi}\mu+O(\mu^2),\qquad
b(\mu)=b_0+\frac{c}{\pi}\mu+O(\mu^2).
\]

**4. The exact trace identity.** Put \(d_a=f_\mu'(a(\mu))\) and \(d_b=f_\mu'(b(\mu))\). Every branch derivative equals \(A+dE\), with
\[
E=\begin{pmatrix}1&0\\1&0\end{pmatrix}.
\]
The identities \(\operatorname{tr}A^2=7\), \(\operatorname{tr}(AE)=3\), and \(\operatorname{tr}E^2=1\) give the *exact* equation
\[
\operatorname{tr}D(T_\mu^2)=7+3(d_a+d_b)+d_ad_b.
\]
Let \(r=\cos(4\pi a_0)=\cos(4\pi b_0)\). Differentiating the expansion in step 3 and substituting the first-order position displacements gives
\[
d_a+d_b=(8c^2-4c-4r)\mu^2+O(\mu^3),
\]
\[
d_ad_b=-4(1-c^2)\mu^2+O(\mu^3).
\]
The linear terms cancel because the two seed sines are opposite. Thus the coefficient of \(\mu^2\) in the two-step trace is
\[
28c^2-12c-12r-4.
\]
For the first seed \((a_0,b_0)=(4/5,1/5)\),
\[
c=\frac{\sqrt5-1}{4},\qquad r=-\frac{\sqrt5+1}{4},
\]
which gives \((25-7\sqrt5)/2\). For the second seed \((3/5,2/5)\),
\[
c=-\frac{\sqrt5+1}{4},\qquad r=\frac{\sqrt5-1}{4},
\]
which gives \((25+7\sqrt5)/2\). Both are positive, and their difference is \(7\sqrt5\).

**5. Conjugacy obstruction.** On the undeformed cat map every period-two orbit has derivative \(A^2\) and hence two-step trace \(7\). A \(C^1\) diffeomorphic conjugacy must take period-two orbits to period-two orbits and, by differentiating the conjugacy equation twice, must conjugate their two-step derivatives by an invertible matrix. It must therefore preserve the trace. The strictly positive quadratic deviations contradict that requirement for all sufficiently small \(\mu>0\). This proves the claim.

## Verification

The standalone script `verify_periodic_data.py` checks the exact fixed-point cancellation numerically at seven parameter values and solves the lifted two-cycle equations by Newton iteration at five small deformation values for both orbits. It verifies the predicted positive quadratic trace coefficients against direct derivatives, checks the first-order position displacement, and confirms distinct traces at \(\mu=0.01\). On that last sample, the traces are approximately \(7.000467346768\) and \(7.002032773233\).

The numerical checks are **supporting** evidence only. The universal small-parameter assertions follow from the analytic implicit-function theorem, the explicitly derived Taylor expansion, and the exact trace identity. No numerical extrapolation is used to prove the existence of \(\varepsilon\).

## Relationship to prior work

Bandtlow, Just and Slipantschuk [1] introduce the analytic two-parameter torus map, its unique fixed point, its trace formula, invariant area, and hyperbolicity. They study smoothness of the hyperbolic splitting numerically. The present theorem does not claim those properties as new. The exact fixed-point formula shows that a one-dimensional curve of nonlinear maps has *identical full fixed-point derivative* to the cat map. This makes period-two data the first natural test unavailable to the fixed-point comparison. The explicit two-cycle quadratic coefficients and their unequal splitting are the asserted new information.

Slipantschuk, Bandtlow and Just [2] establish far-reaching resonances and operator-spectral results for rational Anosov maps. Its complex fixed-point multiplier formulas and generic conjugacy constructions do not state the real two-cycle quadratic splitting in the specific curve considered here. Shchetka [3] proves non-\(C^1\)-conjugacy for two distinct Blaschke deformation families of a different hyperbolic toral automorphism and studies their mixing rates; that theorem does not imply this map's coefficients. The elementary conjugacy invariance of periodic derivatives is classical, and is not a novelty claim.

## Limitations

The two trace expansions and conjugacy obstruction are proved only for all sufficiently small positive \(\mu\) on the specified exceptional curve. The positive cutoff is not optimized or explicitly quantified. The proof does not show that the same trace inequalities persist for arbitrary \(0<\mu<1\), even though exploratory numerical values may suggest this. It does not independently establish higher-regularity obstruction for the invariant splitting, mixing rates, periodic-orbit counting outside the displayed cycles, or a complete rigidity classification.

The originality assessment is necessarily relative to the inspected publications, recoverable research comparisons, and searches; equivalent previously unpublished or unindexed calculations remain possible. The mathematical verification here is not an independent audit.

## References

[1] O. F. Bandtlow, W. Just, and J. Slipantschuk, *A numerical study of rigidity of hyperbolic splittings in simple two-dimensional maps*, arXiv:2402.14770v1 (first posted 2024-02-22); equations (2)–(5) and discussion of fixed-point rigidity. https://arxiv.org/abs/2402.14770

[2] J. Slipantschuk, O. F. Bandtlow, and W. Just, *Resonances for rational Anosov maps on the torus*, arXiv:2211.05925v1 (2022); Sections 1, 4, and 5. https://arxiv.org/abs/2211.05925

[3] E. Shchetka, *Mixing Rates for Analytic Observables: Toral Endomorphisms and Anosov Blaschke Deformations*, arXiv:2610.19019v1 (2026); Section 4, especially Theorem 4.1 and its proof of nonconjugacy. https://arxiv.org/abs/2610.19019
