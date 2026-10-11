# Global stability on the full \(\alpha\le k\) half-space of the Hide–Skeldon–Acheson dynamo
## Finding

For the Hide–Skeldon–Acheson dynamo
\[
\dot x=x(y-1)-\beta z,\qquad
\dot y=\alpha(1-x^2)-ky,\qquad
\dot z=x-bz,
\]
with \(\alpha,\beta,b,k>0\), the equilibrium
\[
E=\left(0,\frac{\alpha}{k},0\right)
\]
is globally asymptotically stable throughout the closed parameter half-space \(0<\alpha\le k\).

A cross-term-free quadratic Lyapunov function is
\[
V(x,y,z)=\alpha x^2+\left(y-\frac{\alpha}{k}\right)^2+\alpha\beta z^2.
\]
Along every solution,
\[
\dot V
=-\frac{2\alpha(k-\alpha)}{k}x^2
-2k\left(y-\frac{\alpha}{k}\right)^2
-2\alpha\beta b z^2.
\]

Thus, for \(0<\alpha<k\), \(\dot V<0\) away from \(E\). At \(\alpha=k\), the zero-derivative set is
\[
\{\dot V=0\}=\{y=1,\ z=0\}.
\]
A complete trajectory can remain in this set only when \(x=0\), because \(\dot z=x-bz=x\) on \(z=0\). Hence its largest invariant subset is exactly \(E\), and LaSalle's invariance principle gives global asymptotic stability at the boundary as well.

## Assumptions and scope

The claim concerns the real three-dimensional HSA system written above with strictly positive parameters \(\alpha,\beta,b,k\). No smallness assumption, perturbative hypothesis, or restriction on the initial condition is used. For \(0<\alpha\le k\), the source equilibrium is unique because
\[
\alpha b-bk-\beta k=b(\alpha-k)-\beta k<0.
\]

The result does not assert global stability for \(\alpha>k\). It also does not classify bifurcations, periodic orbits, or hidden attractors outside the stated half-space.

## Proof

Differentiate \(V\) using the vector field:
\[
\begin{aligned}
\dot V
&=2\alpha x\bigl(x(y-1)-\beta z\bigr)
+2\left(y-\frac{\alpha}{k}\right)
\bigl(\alpha(1-x^2)-ky\bigr)
+2\alpha\beta z(x-bz).
\end{aligned}
\]
The mixed \(xz\) terms cancel exactly. The cubic \(x^2y\) terms also cancel:
\[
2\alpha x^2y-2\alpha x^2y=0.
\]
Collecting the remaining terms gives
\[
\dot V
=-\frac{2\alpha(k-\alpha)}{k}x^2
-2k\left(y-\frac{\alpha}{k}\right)^2
-2\alpha\beta b z^2.
\]

Because \(\alpha,eta,k>0\), the function \(V\) is positive definite about \(E\) and radially unbounded. Therefore every forward orbit is confined to a compact sublevel set of \(V\), so no separate boundedness theorem is needed for continuation.

If \(0<\alpha<k\), all three coefficients on the right-hand side are strictly negative, so \(\dot V=0\) only at \(E\). Standard Lyapunov theory gives global asymptotic stability.

If \(\alpha=k\), then
\[
\dot V=-2k(y-1)^2-2k\beta b z^2.
\]
The zero set is \(S=\{y=1,z=0\}\). If a trajectory remains in \(S\), then \(z\equiv0\) and therefore \(0=\dot z=x\), so \(x\equiv0\). With \(x=0\), \(y=1\), and \(z=0\), all three derivatives vanish. Hence the largest invariant subset of \(S\) is \(E=(0,1,0)\). LaSalle's invariance principle proves convergence of every orbit to \(E\).

## Verification

The differentiation was independently expanded symbolically from the stated vector field and the stated \(V\); the difference between the expanded derivative and
\[
-\frac{2\alpha(k-\alpha)}{k}x^2
-2k\left(y-\frac{\alpha}{k}\right)^2
-2\alpha\beta b z^2
\]
simplifies identically to zero.

Two boundary checks demonstrate that the result is genuinely stronger than the published sufficient condition. First, \(\alpha=k\) is included here but excluded by the source hypothesis \(k>\alpha\). Second, at \((\alpha,k,b,\beta)=(1,2,1,3)\), the source's additional expression equals
\[
k(\alpha\beta-1)^2+4\alpha b(\alpha-k)=4>0,
\]
so its global-stability theorem does not apply, while the present Lyapunov identity still proves global asymptotic stability.

## Relationship to prior work

Li's 2022 paper studies exactly this HSA system and proves global uniform asymptotic stability under the two simultaneous conditions \(k>\alpha\) and
\[
k(\alpha\beta-1)^2+4\alpha b(\alpha-k)<0.
\]
Its Lyapunov function leaves an \(xz\) cross term and therefore requires a quadratic-form inequality. Weighting the \(z^2\) term by \(\alpha\beta\) cancels that cross term exactly and removes the extra condition, while also admitting the boundary \(\alpha=k\).

Mahdi and Valls study integrability of the same HSA equations, and later work by Diz-Pita, Llibre, Otero-Espinar, and Valls classifies invariant algebraic surfaces, low-degree first integrals, and Darboux invariants. Those results address different questions and do not supply this global Lyapunov half-space. Moroz's bifurcation analysis studies coexistence of attractors and unstable periodic orbits rather than a global stability criterion of this form.

## Limitations

The proof is specific to positive \(\alpha,\beta,b,k\) and to the stated HSA normalization. It does not establish necessity of \(\alpha\le k\): the local stability region is larger for some parameters, so global stability may persist beyond this half-space. The original 1996 model paper was located bibliographically but its full text was not available for whole-document comparison; later HSA papers that explicitly discuss stability were checked, so this remains a residual literature risk rather than evidence of coverage.

## References

1. X. Li, “New insights to the Hide-Skeldon-Acheson dynamo,” *Discrete and Continuous Dynamical Systems - B* 27 (2022), 6257–6267. DOI: 10.3934/dcdsb.2021315. Early access: 2022-01-18.
2. A. Mahdi and C. Valls, “Integrability of the Hide–Skeldon–Acheson dynamo,” *Bulletin des Sciences Mathématiques* 138 (2014), 470–482. DOI: 10.1016/j.bulsci.2013.04.001.
3. I. M. Moroz, “The Hide, Skeldon, Acheson dynamo revisited,” *Proceedings of the Royal Society A* 463 (2007), 113–130. DOI: 10.1098/rspa.2006.1758.
4. É. Diz-Pita, J. Llibre, M. V. Otero-Espinar, and C. Valls, “On the integrability and dynamics of the Hide, Skeldon and Acheson differential system,” *Electronic Journal of Qualitative Theory of Differential Equations* 2025 (2025), Article 76. DOI: 10.14232/ejqtde.2025.1.76.
5. R. Hide, A. C. Skeldon, and D. J. Acheson, “A study of two novel self-exciting single-disk homopolar dynamos: Theory,” *Proceedings of the Royal Society A* 452 (1996), 1369–1395. DOI: 10.1098/rspa.1996.0070.
