# Sharp prime-two exclusion and a saturated repelling cycle in a two-cell spiking map

## Finding

Consider the two-cell Euler map of Buscarino, Famoso and Fortuna [1], with the parameter choices used in their numerical bifurcation study:
\[
 F_{T,\alpha}(z)=(1-T)z+T\bigl(M\theta_\alpha(z)+b\bigr),\qquad
 M=\begin{pmatrix}17/10&-1\\1&17/10\end{pmatrix},\quad
 b=\begin{pmatrix}-3/10\\3/10\end{pmatrix},\quad
 \theta_\alpha(z)=\begin{pmatrix}\tanh(\alpha z_1)\\\tanh(\alpha z_2)\end{pmatrix}.
\]
Here \(z\in\mathbb R^2\), \(T>0\) and \(\alpha>0\). A *primitive two-cycle* is a pair of distinct points \(p\neq q\) such that \(F_{T,\alpha}(p)=q\) and \(F_{T,\alpha}(q)=p\).

**Theorem (sharp step-size obstruction and saturated witness).**

1. For every \(\alpha>0\) and every \(0<T\le2\), the map has **no primitive two-cycle anywhere in \(\mathbb R^2\)**.
2. For every \(T>2\) and \(\alpha\ge10\), the map has a primitive two-cycle \(p\leftrightarrow q\) with \(p\) strictly in the first quadrant and \(q\) strictly in the third quadrant. It is the unique such cycle whose ordered midpoint and rescaled half-difference lie in the explicit box specified below. Both points are repelling, with all eigenvalues of the two-step derivative having modulus strictly greater than one.

To locate the cycle, put
\[
 c=\frac{T-2}{T},\qquad
 v=M\begin{pmatrix}1\\1\end{pmatrix}
   =\begin{pmatrix}7/10\\27/10\end{pmatrix},\qquad
 E=\exp\left(-\frac{3\alpha}{5c}\right).
\]
There is a unique pair \((m,w)\) in
\[
 \mathcal B=\left\{(m,w):\|m-b\|_\infty\le\frac1{20},\quad
 \|w-v\|_\infty\le\frac1{20}\right\}
\]
for which \(p=m+w/c\) and \(q=m-w/c\) form a two-cycle. In particular,
\[
 \left\|p-\left(b+\frac vc\right)\right\|_\infty,
 \quad\left\|q-\left(b-\frac vc\right)\right\|_\infty
 \le \frac{27}{5}\left(1+\frac1c\right) E.
\]
Writing \(\rho_T=1+(T-2)(1-108e^{-6})>1\), the two-step derivative satisfies
\[
 \|D(F_{T,\alpha}^{2})(p)u\|_\infty\ge\rho_T^2\|u\|_\infty
 \quad\text{for every }u\in\mathbb C^2.
\]
Consequently \(T=2\) is the *sharp frontier for possible primitive-two recurrence across this parameter family*: such recurrence is impossible at or below the frontier, but exists for every larger step size at sufficiently steep sigmoid gain. This does not claim existence for every gain when \(T>2\), nor global uniqueness of all two-cycles.

## Assumptions and scope

All dynamics are deterministic, noise-free, and defined on the entire real plane, with the exact real hyperbolic tangent. The matrix, biases and sigmoid are the stated numerical slice of equations (4)–(5) in [1]. The free parameters are the positive Euler step \(T\) and sigmoid slope \(\alpha\). No compact absorbing domain is assumed. The box uniqueness assertion refers only to the ordered pair whose first point lies in the first quadrant and whose coordinates \((m,w)\) lie in \(\mathcal B\).

## Proof

**1. Global exclusion below and at the boundary.** Suppose a primitive two-cycle \(p\leftrightarrow q\) exists. Define \(\delta=p-q\neq0\) and \(\eta=\theta_\alpha(p)-\theta_\alpha(q)\neq0\). Subtracting the two return equations, with their orientations carefully retained, yields
\[
 (T-2)\delta=T M\eta.
\]
The scalar function \(s\mapsto\tanh(\alpha s)\) is strictly increasing, so \(\delta\cdot\eta>0\). On the other hand, the skew-symmetric part of \(M\) cancels in the quadratic form:
\[
 \eta\cdot M\eta=\frac{17}{10}\|\eta\|_2^2>0.
\]
Taking the inner product with \(\eta\) forces
\[
 (T-2)(\delta\cdot\eta)=\frac{17T}{10}\|\eta\|_2^2>0.
\]
Therefore \(T>2\), proving the first assertion for every \(\alpha>0\). This argument excludes *all* two-cycles rather than only attracting ones.

**2. Two-cycle equations in saturated coordinates.** Now suppose \(T>2\), and set \(c=(T-2)/T\in(0,1)\). For an ordered candidate pair define
\[
 m=\frac{p+q}{2},\qquad w=\frac c2(p-q),\qquad
 p=m+\frac wc,\quad q=m-\frac wc.
\]
Adding and subtracting the two return equations shows that the cycle equations are *equivalent* to
\[
 (m,w)=G(m,w):=
 \left(b+\frac M2[\theta_\alpha(p)+\theta_\alpha(q)],\quad
 \frac M2[\theta_\alpha(p)-\theta_\alpha(q)]\right).
\]
The saturated limit of this map near a positive/negative quadrant pair is \((b,v)\), with \(v=M(1,1)^\mathsf T\). Here and below \(\|\cdot\|_\infty\) is the maximum-coordinate norm on \(\mathbb R^2\) or \(\mathbb C^2\), and on ordered pairs it means the maximum of the two vector norms.

**3. Invariant box and strict contraction.** On \(\mathcal B\), elementary coordinate bounds give
\[
 p_1\ge\frac3{10c},\qquad p_2\ge\frac{53}{20c},\qquad
 q_1\le-\frac{13}{20c},\qquad q_2\le-\frac{23}{10c}.
\]
Thus every coordinate of \(p\) or \(q\) has magnitude at least \(3/(10c)\). Set \(E=e^{-3\alpha/(5c)}\). The elementary estimates
\[
 |\tanh t-\operatorname{sign}(t)|\le2e^{-2|t|},\qquad
 0<\operatorname{sech}^2 t\le4e^{-2|t|}
\]
imply componentwise saturation errors at most \(2E\) and sigmoid derivatives at most \(4\alpha E\). Since \(\|M\|_\infty=27/10\), both components of \(G\) deviate from \(b\) and \(v\), respectively, by at most \(27E/5\). For \(\alpha\ge10\) and \(c\le1\),
\[
 \frac{27}{5}E\le\frac{27}{5}e^{-6}<\frac1{20},
\]
so \(G\) maps the closed, complete box \(\mathcal B\) into its interior.

For two points of \(\mathcal B\), apply the mean-value inequality on their joining segment (which remains in \(\mathcal B\)). Because \(p\) and \(q\) depend on \((m,w)\) with Lipschitz constant at most \(1+1/c\),
\[
 \operatorname{Lip}(G|_{\mathcal B})
 \le\frac{54}{5}\alpha\left(1+\frac1c\right)E
 \le\frac{108}{5} t e^{-3t/5}
 \le216e^{-6}<1,\qquad t=\frac\alpha c\ge10.
\]
The last inequality uses that \(t e^{-3t/5}\) decreases on \([10,\infty)\). The Banach fixed-point theorem now supplies exactly one \((m,w)\in\mathcal B\). The displayed quadrant bounds ensure \(p\neq q\), so the reconstructed pair is a genuine primitive two-cycle. The stated position error follows directly by combining \(\|m-b\|_\infty,\|w-v\|_\infty\le27E/5\).

**4. Uniform hyperbolic repulsion.** The Jacobian at either member \(z=p,q\) is
\[
 DF_{T,\alpha}(z)=(1-T)I+T M
 \operatorname{diag}\bigl(\alpha\operatorname{sech}^2(\alpha z_1),
 \alpha\operatorname{sech}^2(\alpha z_2)\bigr).
\]
The perturbation of \((1-T)I\) has induced maximum norm at most \((54/5)T\alpha E\). With \(t=\alpha/c\ge10\),
\[
 \frac{54}{5}\frac\alpha c E\le108e^{-6}<1.
\]
The reverse triangle inequality therefore gives, for either \(z=p,q\) and every complex vector \(u\),
\[
 \|DF_{T,\alpha}(z)u\|_\infty\ge
 \left[T-1-\frac{54}{5}T\alpha E\right]\|u\|_\infty
 \ge\rho_T\|u\|_\infty,
\]
where \(\rho_T=1+(T-2)(1-108e^{-6})>1\). Composing these two bounds yields the stated two-step estimate. Substituting a complex eigenvector proves that every eigenvalue of \(D(F_{T,\alpha}^2)(p)\) has modulus at least \(\rho_T^2>1\). Hence the orbit is a hyperbolic repeller. This proves all assertions.

## Verification

The standalone Python standard-library program `VERIFY.py` constructs the unique box-fixed-point numerically at 95-digit decimal precision for \(T\in\{2.0001,2.01,2.1,2.5,3,10,100\}\) and \(\alpha\in\{10,12,20\}\), giving 21 parameter pairs. It checks all 42 one-step cycle equations to residual below \(10^{-72}\), the 42 position-error bounds, the real quadrant constraints, and the matrix-norm criterion for expansion. It separately tests the explicit constants \(216e^{-6}<1\), \(108e^{-6}<1\), and \((27/5)e^{-6}<1/20\).

For the illustrative parameters \((T,\alpha)=(3,10)\), the period-two orbit lies extremely close to \(p=(1.8,8.4)\) and \(q=(-2.4,-7.8)\). Run `python3 VERIFY.py` from the directory containing the standalone program. These finite high-precision checks corroborate the algebra; the global theorem rests entirely on the analytic proof above.

## Relationship to prior work

The map, parameter slice, equilibria and numerical bifurcation scenarios are from Buscarino, Famoso and Fortuna [1]. Their open-access full article (Sections 3–7 and appendices inspected) includes period-four behavior and numerical period-doubling routes but does not establish a global nonexistence theorem for primitive period two, or a saturated large-gain repelling orbit with a sharp step frontier. The repeller is structurally different from an attracting cycle observed by forward simulation. General monotonicity and contraction arguments are standard techniques; their combination here yields explicit parameter-dependent, orbit-specific boundaries for this published map. The comparison does not assert that all related literature is indexed, and priority remains subject to further scrutiny.

## Limitations

The existence and repulsion claim is proved only for \(\alpha\ge10\); it does not describe the full \((T,\alpha)\) phase diagram or any higher-period orbits. The assertion of uniqueness is restricted to the explicitly defined box, not to every primitive two-cycle in the plane. The numbers in the illustrative orbit are approximations, not exact decimal equalities. The model excludes additive noise, finite-precision hardware effects, and state-space restrictions not present in its mathematical definition. A separate independent mathematical audit has not been performed.

## References

[1] A. Buscarino, C. Famoso, and L. Fortuna, “Bifurcations in a new two-cell spiking map: a numerical and experimental study,” *Nonlinear Dynamics* **111** (2023), 20361–20375. First publicly dated September 27, 2023. DOI: 10.1007/s11071-023-08897-7. Full text: https://link.springer.com/article/10.1007/s11071-023-08897-7 .
