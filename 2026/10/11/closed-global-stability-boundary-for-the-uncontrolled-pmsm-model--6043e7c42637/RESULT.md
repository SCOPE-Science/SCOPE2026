# Closed global-stability boundary for the uncontrolled PMSM model
## Finding
Consider the uncontrolled normalized permanent-magnet synchronous-motor model
\[
\dot x=-x+yz,\qquad \dot y=-y-xz+\gamma z,\qquad \dot z=\sigma(y-z),
\]
with \(\sigma>0\). The origin is globally asymptotically stable exactly for \(\gamma\le1\). In the same closed parameter region, the only compactly supported invariant probability measure is the Dirac mass at the origin.

## Assumptions and scope
The result concerns the autonomous, zero-input, zero-load normalized PMSM equations above, with real state \( (x,y,z)\in\mathbb R^3\), parameter \(\sigma>0\), and real \(\gamma\). It does not concern the controlled or perturbed system, nor does it assert anything about attraction rates at the critical value beyond convergence.

## Proof
For \(\gamma\le1\), define
\[
V(x,y,z)=\frac12\left(x^2+y^2+\frac{2-\gamma}{\sigma}z^2\right).
\]
Because \(\sigma>0\) and \(2-\gamma>0\), this is positive definite and radially unbounded. Direct substitution gives the exact cancellation
\[
\dot V=x(-x+yz)+y(-y-xz+\gamma z)+(2-\gamma)z(y-z)
=-x^2-(y-z)^2-(1-\gamma)z^2.
\]
If \(\gamma<1\), the right side is negative definite, so the origin is globally asymptotically stable.

At \(\gamma=1\), \(\dot V=-x^2-(y-z)^2\). Its zero set is \(x=0\) and \(y=z\). A trajectory that remains in this set must also satisfy \(\dot x=yz=y^2=0\), hence \(y=z=0\). LaSalle's invariance principle therefore gives global asymptotic stability at the nonhyperbolic endpoint as well.

If \(\gamma>1\), the system has the two nonzero equilibria
\[
E_\pm=\left(\gamma-1,\;\pm\sqrt{\gamma-1},\;\pm\sqrt{\gamma-1}\right),
\]
so the origin cannot be globally attractive. This proves the stated if-and-only-if boundary.

For a compactly supported invariant probability measure \(\mu\), invariance gives \(\int \dot V\,d\mu=0\). For \(\gamma<1\), the nonnegative defect \(x^2+(y-z)^2+(1-\gamma)z^2\) therefore vanishes \(\mu\)-almost surely, forcing support at the origin. At \(\gamma=1\), the support lies in \(x=0, y=z\); invariance then restricts it to the largest invariant subset of that set, which is again only the origin.

## Verification
The bundled verifier expands the Lyapunov derivative algebraically without external packages and checks that it equals \(-x^2-(y-z)^2-(1-\gamma)z^2\) coefficient by coefficient. It also checks the algebraic equilibrium substitution used for \(E_\pm\). The endpoint argument is an analytic LaSalle argument, not a finite numerical experiment.

## Relationship to prior work
Yao et al. (2023) use this normalized PMSM model with \(\gamma=20\) and \(\sigma=5.46\) as the uncontrolled chaotic plant before designing fixed-time adaptive controllers; they list primary MSC 34C28. He (2017) classifies equilibria and local bifurcations of the same normalized model and numerically reports convergence to the origin for \(0<\gamma<1\), but does not supply the closed global theorem or the critical \(\gamma=1\) invariance argument above. A later 2026 analysis likewise identifies the local stability loss and pitchfork threshold at \(\gamma=1\), while its displayed analysis is local/numerical rather than a global Lyapunov proof at the boundary. The present statement therefore closes the global threshold with an explicit storage identity and adds invariant-measure rigidity.

## Limitations
The proof requires \(\sigma>0\). It is specific to the zero-input, zero-load autonomous normalization; external inputs, load torque, parameter uncertainty, or feedback controls change the derivative identity. The literature search cannot exclude an inaccessible or differently parameterized older proof of the same global identity, although the closest inspected PMSM analyses establish local or numerical stability rather than this closed global statement.

## References
1. Q. Yao, H. Jahanshahi, S. Bekiros, J. Liu, and A. A. Al-Barakati, “Fixed-Time Adaptive Chaotic Control for Permanent Magnet Synchronous Motor Subject to Unknown Parameters and Perturbations,” Mathematics 11 (2023), 3182. DOI: 10.3390/math11143182.
2. S. He, “Dynamics and Stability of Permanent-Magnet Synchronous Motor,” Mathematical Problems in Engineering (2017), Article 4923987. DOI: 10.1155/2017/4923987.
3. A. S. Hunaish, F. N. Ayoob, F. R. Tahir, and V.-T. Pham, “Stability Analysis and Chaos Control of Permanent-Magnet Synchronous Motor,” Dynamics 6 (2026), 8. DOI: 10.3390/dynamics6010008.
