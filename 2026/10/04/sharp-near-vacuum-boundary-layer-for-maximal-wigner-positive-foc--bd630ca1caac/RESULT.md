# Sharp near-vacuum boundary layer for maximal Wigner-positive Fock coherence
## Finding
For each fixed integer \(n\ge 3\), define
\[
\rho_n(t,s)=(1-t)|0\rangle\langle0|+t|n\rangle\langle n|+s(|0\rangle\langle n|+|n\rangle\langle0|),
\]
with \(0<t<1\) and \(s\ge0\), and let \(s_n(t)\) be the largest coherence for which the Wigner function is nonnegative. Write \(A_n=(n!)^{1/n}\). If \(z_n(t)=2R_n(t)\) is any global minimizer in the exact radial formula
\[
s_n(t)=\inf_{z>0}\frac{\sqrt{n!}\,[1-t+t(-1)^nL_n(z)]}{2z^{n/2}},
\]
then, as \(t\to0^+\) with \(n\) fixed,
\[
z_n(t)=A_n t^{-1/n}+(n-2)+O(t^{1/n}),
\]
and
\[
s_n(t)=\sqrt t\left[1-\frac{n^2}{2A_n}t^{1/n}+\frac{n^2(n^2-2)}{8A_n^2}t^{2/n}+O(t^{3/n})\right].
\]
Consequently,
\[
s_n(t)^2=t\left[1-\frac{n^2}{A_n}t^{1/n}+\frac{n^2(n^2-1)}{2A_n^2}t^{2/n}+O(t^{3/n})\right].
\]
At maximal coherence the Wigner-positivity inequality is saturated at \(\cos(n\theta)=-1\) and \(R=R_n(t)=z_n(t)/2\), so the first boundary zero lies at squared radius
\[
R_n(t)=\frac{A_n}2t^{-1/n}+\frac{n-2}2+O(t^{1/n}).
\]

## Assumptions and scope
The Laguerre convention is
\[
L_n(z)=\sum_{k=0}^n(-1)^k\binom nk\frac{z^k}{k!}.
\]
All asymptotics are for fixed integer \(n\ge3\) and \(t\to0^+\). The result concerns only the maximal-coherence two-level family above; it does not assert a global extremum over all Wigner-positive states and it does not strengthen the entropy expansion of the source paper beyond what follows from the displayed coherence boundary.

## Proof
Set \(P_n(z)=(-1)^nL_n(z)\), \(\varepsilon=t^{1/n}\), and \(A=A_n=(n!)^{1/n}\). The exact coefficient formula for the Laguerre polynomial gives
\[
P_n(z)=\frac{z^n}{n!}-\frac{n^2z^{n-1}}{n!}+\frac{n^2(n-1)^2z^{n-2}}{2n!}+O(z^{n-3}).
\]
Introduce the scaled radius \(z=A u/\varepsilon\). Dividing the exact objective by \(\sqrt t\) gives an exact finite-polynomial expression whose expansion, uniformly with two \(u\)-derivatives on compact subsets of \((0,\infty)\), is
\[
F_\varepsilon(u)=g_0(u)+\varepsilon g_1(u)+\varepsilon^2g_2(u)+O(\varepsilon^3),
\]
where
\[
g_0(u)=\frac12\left(u^{-n/2}+u^{n/2}\right),\qquad
g_1(u)=-\frac{n^2}{2A}u^{n/2-1},
\]
\[
g_2(u)=\frac{n^2(n-1)^2}{4A^2}u^{n/2-2}.
\]
For \(n=3\), the term \(-t=-\varepsilon^3\) enters only the stated remainder; for \(n>3\) it is still higher order.

The source paper proves \(s_n(t)/\sqrt t\to1\). A global minimizer exists because the exact objective diverges as \(z\downarrow0\) and as \(z\to\infty\). The same exact rescaling shows that a minimizing sequence cannot have \(u\to0\) or \(u\to\infty\); hence every minimizing sequence is precompact in \((0,\infty)\). Any limit point minimizes \(g_0\). Since \(g_0(u)\ge1\), with equality only at \(u=1\), every minimizer satisfies \(u\to1\). In a fixed neighborhood of \(1\), \(g_0''(1)=n^2/4>0\), so the stationary point is unique there for sufficiently small \(\varepsilon\), and the implicit-function expansion applies.

Because
\[
g_1'(1)=-\frac{n^2(n-2)}{4A},\qquad g_0''(1)=\frac{n^2}4,
\]
the minimizing scaled radius obeys
\[
u_\varepsilon=1+\frac{n-2}A\varepsilon+O(\varepsilon^2).
\]
Therefore
\[
z_n(t)=\frac A\varepsilon u_\varepsilon=A t^{-1/n}+(n-2)+O(t^{1/n}).
\]
For the minimum value, the standard perturbed-minimum formula yields
\[
F_\varepsilon(u_\varepsilon)=g_0(1)+\varepsilon g_1(1)+\varepsilon^2\left[g_2(1)-\frac{g_1'(1)^2}{2g_0''(1)}\right]+O(\varepsilon^3).
\]
Substitution gives
\[
F_\varepsilon(u_\varepsilon)=1-\frac{n^2}{2A}\varepsilon+\frac{n^2(n^2-2)}{8A^2}\varepsilon^2+O(\varepsilon^3),
\]
which proves the expansion for \(s_n(t)\); squaring it gives the stated expansion for \(s_n(t)^2\).

Finally, the exact Wigner-positivity condition is minimized over angle at \(\cos(n\theta)=-1\). At a radial minimizer defining \(s_n(t)\), equality holds in that inequality, so the Wigner function vanishes there. This identifies the asymptotic boundary-zero location.

## Verification
The proof uses only the exact radial formula and exact Laguerre coefficients. The bundled script `artifacts/verify.py` independently reconstructs the first three leading Laguerre coefficients and numerically minimizes the exact radial objective for representative \(n\) and small \(t\). Its numerical checks are corroborative only and are not used to justify the asymptotic theorem.

## Relationship to prior work
Van Herstraeten, Cerf, and Chabaud define this exact maximal coherence and prove only the leading statement \(s_n(t)^2=t+o(t)\), using a two-sided bound; they do not give a first correction, a second correction, or the asymptotic minimizing radius. Their construction is the direct motivation for the present refinement. Abreu, Chabaud, Dias, and Prata study rigidity and geometry of Wigner zeros for finite Hermite expansions, but their results do not determine this maximal-coherence optimization or its near-vacuum radial boundary layer. Older results on positive-Wigner mixed states and Wigner majorization concern broader structural or entropy questions rather than the sharp two-level coherence boundary.

## Limitations
The expansion is pointwise in fixed \(n\); no uniformity as \(n\to\infty\) is claimed. The result does not determine the globally smallest Wigner entropy, nor does it classify all boundary points of the Wigner-positive set. The literature search did not reveal an equivalent asymptotic under alternate quantum-optics normalization, but such remote terminology remains a residual originality risk.

## References
1. Z. Van Herstraeten, N. J. Cerf, and U. Chabaud, “Wigner-positive quantum states can have lower entropy than the vacuum,” arXiv:2609.24670v1 (2026), especially Appendix A and Appendix B, Eqs. (A7), (B3), (B4), and (B12).
2. L. D. Abreu, U. Chabaud, N. Costa Dias, and J. N. Prata, “Inverse problems for the zeros of the Wigner function,” arXiv:2504.20324v1 (2025).
3. T. Bröcker and R. F. Werner, “Mixed states with positive Wigner functions,” Journal of Mathematical Physics 36 (1995), 62–75.
