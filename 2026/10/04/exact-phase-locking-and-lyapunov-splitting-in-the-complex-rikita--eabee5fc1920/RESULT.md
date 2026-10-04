# Exact phase locking and Lyapunov splitting in the complex Rikitake dynamo
## Finding
Consider the complex Rikitake system
\[
\dot x=-\beta x+yz,\qquad
\dot y=-\beta y-\alpha x+xz,\qquad
\dot z=1-\operatorname{Re}(\overline{x}y),
\]
where \(x,y\in\mathbb C\), \(z\in\mathbb R\), and \(\alpha,\beta>0\). Define the relative-phase defect
\[
J=\operatorname{Im}(\overline{x}y).
\]
Then
\[
\dot J=-2\beta J,
\qquad
J(t)=J(t_0)e^{-2\beta(t-t_0)}.
\]
Consequently every bounded complete trajectory satisfies \(J\equiv0\). Such a trajectory never reaches \(x=y=0\), and therefore it lies, for one fixed \(\theta\) modulo \(\pi\), in the invariant real slice
\[
\mathcal M_\theta=\{(e^{i\theta}X,e^{i\theta}Y,Z):X,Y,Z\in\mathbb R\}.
\]
After the fixed rotation \((x,y)\mapsto(e^{-i\theta}x,e^{-i\theta}y)\), the trajectory obeys exactly the classical real Rikitake equations
\[
\dot X=-\beta X+YZ,\qquad
\dot Y=-\beta Y-\alpha X+XZ,\qquad
\dot Z=1-XY.
\]
It follows in particular that every compactly supported ergodic invariant probability measure is supported on one fixed-phase real slice.

Along any such slice the five-dimensional variational system splits into a three-dimensional tangent block and the normal block
\[
\dot u=-\beta u+Zv,\qquad
\dot v=(Z-\alpha)u-\beta v.
\]
The vector \((u,v)=(X,Y)\) is an exact nonvanishing bounded solution of this normal block on a compact recurrent support, so one normal Lyapunov exponent is \(0\). The normal trace is the constant \(-2\beta\), hence Liouville's formula gives the other normal exponent as \(-2\beta\). Therefore the full five-dimensional Lyapunov spectrum of every compactly supported ergodic invariant measure is the multiset union of the corresponding three-dimensional real-Rikitake spectrum and
\[
\{0,-2\beta\}.
\]
At the parameters \(\alpha=5\), \(\beta=2\) used for the paper's chaotic example, these two phase-normal exponents are exactly \(0\) and \(-4\). For its displayed initial condition \((x,y,z)=(5-3i,1-4i,5.5)\),
\[
J(0)=\operatorname{Im}((5+3i)(1-4i))=-17,
\qquad
J(t)=-17e^{-4t}.
\]
Thus the complex relative phase is an exponentially decaying transient; compact recurrent dynamics have no genuinely time-varying relative phase.

## Assumptions and scope
The phase-locking conclusion uses \(\beta>0\) and bounded completeness, not merely boundedness for forward time. Compact invariant sets consist of complete bounded trajectories, so the conclusion applies to all compact recurrent dynamics. A compact invariant set may be a union of several phase-rotated copies; the stronger single-slice statement is asserted for each complete trajectory and, by ergodicity of the phase label modulo \(\pi\), for each ergodic invariant measure. The Lyapunov splitting is asserted for compactly supported ergodic invariant measures, where the derivative cocycle is bounded and the normal solution \((X,Y)\) is bounded away from zero because \(X=Y=0\) cannot occur on a bounded complete trajectory.

## Proof
Differentiate \(\overline{x}y\):
\[
\frac{d}{dt}(\overline{x}y)=(-\beta\overline{x}+\overline{y}z)y+\overline{x}(-\beta y-\alpha x+xz).
\]
Therefore
\[
\frac{d}{dt}(\overline{x}y)=-2\beta\overline{x}y+z|y|^2+(z-\alpha)|x|^2.
\]
The last two terms are real, which proves \(\dot J=-2\beta J\). If a complete trajectory is bounded and \(J(t_0)\ne0\), then \(|J(t)|=|J(t_0)|e^{2\beta(t_0-t)}\to\infty\) as \(t\to-\infty\), contradicting boundedness. Hence \(J\equiv0\).

If \(x=y=0\) at some time, uniqueness forces \(x=y=0\) thereafter and backward as well, while \(\dot z=1\); such a complete trajectory is unbounded. Thus \((x,y)\ne(0,0)\) at every time on a bounded complete trajectory. The identity \(J=0\) says that the two complex numbers \(x\) and \(y\) are real-collinear. At one time choose \(\theta\) so that both \(e^{-i\theta}x\) and \(e^{-i\theta}y\) are real. The vector field has real coefficients and preserves \(\mathcal M_\theta\), so uniqueness keeps the whole orbit in that same slice. Substitution gives the real Rikitake system above.

For the variational statement, decompose infinitesimal perturbations into the real tangent directions and the common-phase imaginary directions. In the latter, the normal block is exactly the displayed two-dimensional linear system. Differentiating the family \((e^{i\theta}X,e^{i\theta}Y,Z)\) with respect to \(\theta\) at \(\theta=0\) shows that \((u,v)=(X,Y)\) is a normal solution. On a compact recurrent support its norm is bounded above and, because it never vanishes, bounded below, so its Lyapunov exponent is exactly zero. The determinant of a fundamental matrix of the normal block is \(e^{-2\beta t}\) up to its initial determinant. Hence the sum of its two Lyapunov exponents is \(-2\beta\), giving the second exponent \(-2\beta\). Block diagonalization then gives the full spectral union.

## Verification
The key identity was checked by expanding the five real equations with \(x=x_1+ix_2\), \(y=x_3+ix_4\): for \(J=x_1x_4-x_2x_3\), direct differentiation reduces exactly to \(-2\beta J\). The source's equilibrium characteristic polynomial contains factors \(\lambda\) and \(\lambda+2\beta\), consistent with the two exact phase-normal rates derived globally here. At \(\beta=2\), the normal rates are therefore exactly \(0\) and \(-4\), independently of numerical Lyapunov estimation.

## Relationship to prior work
Pang, Wu, Xiao, Jiang and collaborators introduced and studied this complex Rikitake model, including its five-real-dimensional form, equilibrium circle, constant divergence \(-4\beta\), numerical Lyapunov exponents, chaos control, and synchronization. Their local equilibrium characteristic polynomial already contains the factors \(\lambda\) and \(\lambda+2\beta\), but the inspected full text does not state the global relative-phase identity, the collapse of bounded complete trajectories to fixed-phase real slices, or the exact normal Lyapunov splitting.

A published result for the classical real Rikitake system gives a different stationary mean-height rigidity law. That result applies after the phase reduction but does not imply the reduction itself or the two exact normal exponents. Searches for phase locking, relative-phase decay, invariant-slice reduction, and exact complex-Rikitake Lyapunov splitting did not locate a statement dominating the finding above.

## Limitations
The result does not say that a generic forward solution with \(J(0)\ne0\) lies exactly in a real slice at finite time; it says that its relative-phase defect decays exponentially and that every bounded complete/recurrent orbit already has zero defect. It does not classify the dynamics inside the real Rikitake slice. The literature comparison is limited by indexing and terminology: a differently phrased or non-indexed prior reduction could exist.

## References
1. W. Pang, Z. Wu, Y. Xiao, C. Jiang, et al., "Chaos Control and Synchronization of a Complex Rikitake Dynamo Model," Entropy 22 (2020), 671. DOI: 10.3390/e22060671. PMCID: PMC7517210.
2. "Chaos in the Rikitake two-disc dynamo system," Earth and Planetary Science Letters (1980). DOI: 10.1016/0012-821X(80)90224-1.
