# Geometric threshold accumulation and logarithmic gap-count divergence in the golden-mean Bethe–Sommerfeld lattice
## Finding
For the golden-mean rectangular periodic quantum graph with \(\delta\)-coupling, let the two edge lengths satisfy \(a/b=\phi=(1+\sqrt5)/2\) and let \(\alpha<0\). Introduce the dimensionless attractive coupling
\[
g=a|\alpha|,
\qquad
g_c=\frac{\pi^2}{\sqrt5}.
\]
Exner and Turek's exact finite-gap theorem uses the increasing thresholds
\[
A_N=\frac{2\pi}{\sqrt5}\left(\phi^{2N}-\phi^{-2N}\right)
\tan\!\left(\frac{\pi}{2}\phi^{-2N}\right),
\qquad N\ge1,
\]
and states that the positive spectrum has exactly \(N\) open gaps precisely when
\[
A_N<g\le A_{N+1}.
\]
These thresholds approach the infinite-gap boundary with the sharp law
\[
\boxed{
g_c-A_N=C_\phi\,\phi^{-4N}+O(\phi^{-8N})
},
\qquad
C_\phi=\frac{\pi^2}{\sqrt5}\left(1-\frac{\pi^2}{12}\right)>0.
\]
In particular,
\[
\boxed{
\lim_{N\to\infty}\frac{g_c-A_{N+1}}{g_c-A_N}=\phi^{-4}
}.
\]
If \(N(g)\) denotes the exact finite number of positive gaps in this window, then
\[
\boxed{
N(g)=\frac{\log(C_\phi/(g_c-g))}{4\log\phi}+O(1)
}
\qquad(g\uparrow g_c),
\]
and therefore
\[
\boxed{
\lim_{g\uparrow g_c}\frac{N(g)}{\log(1/(g_c-g))}
=\frac{1}{4\log\phi}
}.
\]
Thus the exact finite-gap intervals form a geometric staircase approaching the infinite-gap transition, with ratio \(\phi^{-4}\), while the gap count diverges only logarithmically.

## Assumptions and scope
The graph, coupling convention, positive-spectrum gap count, and threshold sequence are those of Exner and Turek for the rectangular lattice with golden-mean aspect ratio. The result concerns the attractive branch \(\alpha<0\) and the limit from the finite-gap side \(g\uparrow g_c\). It uses the source's exact theorem identifying the number of open positive spectral gaps from the intervals \(A_N<g\le A_{N+1}\).

The statement does not address individual gap widths, the repulsive branch, other irrational edge ratios, magnetic perturbations, or finite-volume spectra. The \(O(1)\) term in the asymptotic for \(N(g)\) reflects the integer staircase and is not claimed to converge.

## Proof
Set
\[
x=\phi^{-2N}.
\]
Then \(x\to0\) as \(N\to\infty\), and the exact source threshold becomes
\[
A_N=\frac{2\pi}{\sqrt5}(x^{-1}-x)
\tan\!\left(\frac{\pi x}{2}\right).
\]
The Taylor expansion of the tangent at the origin is
\[
\tan\!\left(\frac{\pi x}{2}\right)
=\frac{\pi x}{2}+\frac{\pi^3x^3}{24}+
\frac{\pi^5x^5}{240}+O(x^7).
\]
Multiplication gives
\[
A_N=\frac{\pi^2}{\sqrt5}
-\frac{\pi^2}{\sqrt5}\left(1-\frac{\pi^2}{12}\right)x^2
-\frac{\pi^2}{\sqrt5}\frac{\pi^2(10-\pi^2)}{120}x^4
+O(x^6).
\]
Because \(x^2=\phi^{-4N}\), this proves
\[
g_c-A_N=C_\phi\phi^{-4N}+O(\phi^{-8N}).
\]
The coefficient is positive since \(\pi^2<12\). Dividing the formulas for consecutive indices immediately yields
\[
\frac{g_c-A_{N+1}}{g_c-A_N}
=\phi^{-4}\left(1+O(\phi^{-4N})\right),
\]
which proves the geometric-ratio limit.

For the counting law, write \(\delta=g_c-g\) and \(\Delta_j=g_c-A_j\). The exact source theorem gives, whenever \(N(g)=N\),
\[
\Delta_{N+1}\le\delta<\Delta_N.
\]
Since
\[
\Delta_j=C_\phi\phi^{-4j}\left(1+O(\phi^{-4j})\right),
\]
taking logarithms in the two bounding inequalities yields
\[
N=\frac{\log(C_\phi/\delta)}{4\log\phi}+O(1).
\]
As \(\delta\downarrow0\), division by \(\log(1/\delta)\) proves the final limit.

## Verification
The standalone script `artifacts/verify_threshold_accumulation.py` evaluates the exact threshold formula with standard-library floating-point arithmetic. It checks monotonicity for the tested indices, convergence of \((g_c-A_N)/(C_\phi\phi^{-4N})\) to one, convergence of consecutive threshold deficits to \(\phi^{-4}\), and the exact interval inequalities for representative midpoint couplings. These finite calculations are corroborative only; the proof is the analytic expansion above.

## Relationship to prior work
The short 2017 paper by Exner and Turek and their longer companion paper give the golden-mean rectangular lattice, the critical value \(g_c=\pi^2/\sqrt5\), the exact threshold sequence \(A_N\), and the theorem assigning exactly \(N\) positive gaps to each interval \(A_N<g\le A_{N+1}\). They also show that \(A_N\) is increasing and remains below \(g_c\). The published theorem does not state the rate at which \(A_N\) approaches \(g_c\), the geometric ratio \(\phi^{-4}\), or the logarithmic divergence law for the gap count.

Targeted searches for threshold accumulation, Fibonacci/golden-mean aliases, critical gap-count scaling, and logarithmic divergence found no source stating or implying these asymptotics. A later presentation by Exner reproduces the exact \(N\)-gap bounds and the narrow finite-gap window, but likewise does not supply the displayed scaling law.

## Limitations
The asymptotic is specific to the golden-mean aspect ratio because the source's exact thresholds reduce to the explicit sequence \(A_N\). It does not claim a corresponding coefficient for general badly approximable edge ratios. The result counts open positive spectral gaps but gives no asymptotic for their individual widths or locations. The integer nature of \(N(g)\) prevents a generally convergent additive constant in the displayed counting law.

## References
1. P. Exner and O. Turek, “Quantum graphs with the Bethe–Sommerfeld property,” arXiv:1705.04363v1 (2017), Nanosystems: Physics, Chemistry, Mathematics 8 (2017), 305–309, DOI:10.17586/2220-8054-2017-8-3-305-309.
2. P. Exner and O. Turek, “Periodic quantum graphs from the Bethe–Sommerfeld perspective,” arXiv:1705.07306v1 (2017), Journal of Physics A: Mathematical and Theoretical 50 (2017), 455201, DOI:10.1088/1751-8121/aa8d8d.
