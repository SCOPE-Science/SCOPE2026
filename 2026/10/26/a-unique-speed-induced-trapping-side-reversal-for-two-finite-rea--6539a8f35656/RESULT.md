# A unique speed-induced trapping-side reversal for two finite reactive regions

## Finding

A one-dimensional run-and-tumble particle moves with velocities \(+v\) and \(-v\), with \(v>0\), and reverses its velocity at rate \(\alpha/2\), where \(\alpha>0\). It is irreversibly captured at spatially constant Poisson rates \(\kappa_{\mathrm L}>0\) and \(\kappa_{\mathrm R}>0\) when in two finite reactive intervals
\[
I_{\mathrm L}=[-a-L_{\mathrm L},-a],\qquad
I_{\mathrm R}=[a,a+L_{\mathrm R}],
\]
with \(a,L_{\mathrm L},L_{\mathrm R}>0\). There is no capture outside these intervals. Initially the particle is at \(x=0\), with each velocity sign equally likely. Let \(P_{\mathrm R}(v)\) be the probability of eventual capture in the right interval.

Define the positive dimensionless impedances
\[
A_i=\sqrt{\frac{\alpha+\kappa_i}{\kappa_i}},\quad
B_i=L_i\sqrt{\kappa_i(\alpha+\kappa_i)},\quad
R_i(v)=A_i\coth\left(\frac{B_i}{v}\right),
\qquad i\in\{\mathrm L,\mathrm R\}.
\]

**Exact splitting law.** For every finite \(v>0\), capture occurs almost surely and
\[
\boxed{P_{\mathrm R}(v)=
\frac{R_{\mathrm L}(v)+\alpha a/v}
{R_{\mathrm L}(v)+R_{\mathrm R}(v)+2\alpha a/v}.}
\tag{1}
\]
For an arbitrary initial location \(x\in(-a,a)\), with mean initial velocity sign \(m\in[-1,1]\), the corresponding probability is
\[
\boxed{P_{\mathrm R}(v;x,m)=
\frac{R_{\mathrm L}(v)+\alpha(x+a)/v+m}
{R_{\mathrm L}(v)+R_{\mathrm R}(v)+2\alpha a/v}.}
\tag{2}
\]

**Complete crossover classification.** The preferred capture side changes exactly once, at a unique finite particle speed, **if and only if**
\[
\boxed{(\kappa_{\mathrm R}-\kappa_{\mathrm L})
(\kappa_{\mathrm R}L_{\mathrm R}-\kappa_{\mathrm L}L_{\mathrm L})<0.}
\tag{3}
\]
In that case there is exactly one \(v_*>0\) with \(P_{\mathrm R}(v_*)=1/2\), and the sign of \(P_{\mathrm R}(v)-1/2\) reverses across it. Its location is equivalently the unique solution of
\[
A_{\mathrm L}\coth(B_{\mathrm L}/v_*)=
A_{\mathrm R}\coth(B_{\mathrm R}/v_*).
\tag{4}
\]
If (3) fails and the two reactive intervals are not identical in strength and length, no finite speed produces an equal capture probability. If \(\kappa_{\mathrm L}=\kappa_{\mathrm R}\) and \(L_{\mathrm L}=L_{\mathrm R}\), then \(P_{\mathrm R}(v)=1/2\) for every speed.

**Endpoint laws.** For fixed positive parameters, including \(a>0\),
\[
P_{\mathrm R}(v)=\frac12+
\frac{A_{\mathrm L}-A_{\mathrm R}}{4\alpha a}\,v+o(v)
\qquad (v\downarrow0),
\tag{5}
\]
while
\[
\lim_{v\to\infty}P_{\mathrm R}(v)=
\frac{\kappa_{\mathrm R}L_{\mathrm R}}
{\kappa_{\mathrm L}L_{\mathrm L}+\kappa_{\mathrm R}L_{\mathrm R}}.
\tag{6}
\]
Thus the existence of a reversal depends only on the opposition between the ranking of local capture rates and that of integrated capture strengths. The criterion is independent of \(\alpha\) and of the gap \(2a\); the numerical crossover speed is not.

## Assumptions and scope

The particle's position is continuous, its velocity sign is a two-state Markov chain, and its sign flips at rate \(\alpha/2\), so the velocity autocorrelation decays at rate \(\alpha\). Capture is independent conditional on the particle path, with local hazard \(\kappa_{\mathrm L}\mathbf1_{I_{\mathrm L}}+\kappa_{\mathrm R}\mathbf1_{I_{\mathrm R}}\). Upon capture the particle remains irreversibly immobilized and carries the label of its reactive interval. There are no reflecting walls or drift forces. All seven geometric and dynamic parameters \(v,\alpha,a,L_{\mathrm L},L_{\mathrm R},\kappa_{\mathrm L},\kappa_{\mathrm R}\) are finite and strictly positive. Formula (2) additionally allows arbitrary initial velocity bias in the central gap, but the one-crossover classification refers to the centered, unbiased initial condition of formula (1).

## Proof

**1. Existence of the absorption probabilities.** At successive pairs of velocity-flip epochs, the uncaptured process has independent centered displacements equal in distribution to the difference of two exponentially distributed run lengths. These displacements form a one-dimensional symmetric random walk with finite, nonzero variance and are recurrent. Thus, before killing, the particle crosses each reactive interval inward infinitely often almost surely. At an inward crossing of a given interval of width \(L>0\), the conditional probability of capture before either tumbling or exiting that interval is at least
\[
\exp\!\left(-\frac{\alpha L}{2v}\right)
\left(1-\exp\!\left(-\frac{\kappa L}{v}\right)\right)>0.
\]
The strong Markov property at successive crossings therefore implies almost-sure eventual capture. Standard first-event conditioning identifies the right-capture probabilities with the unique bounded solution of the backward generator equations.

**2. Backward equations.** Let \(u_\pm(x)\) be the probability of right capture from \(x\) with velocity \(\pm v\). On any interval with local hazard \(\kappa\) and right-capture reward \(q\in\{0,1\}\), the equations are
\[
\pm v u_\pm'(x)
+\frac{\alpha}{2}\bigl(u_\mp(x)-u_\pm(x)\bigr)
+\kappa\bigl(q-u_\pm(x)\bigr)=0.
\tag{7}
\]
For a zone with reward zero, the column \(U=(u_+,u_-)^{\mathsf T}\) obeys \(U'=M_\kappa U\), with
\[
M_\kappa=\frac1v\begin{pmatrix}
\kappa+\alpha/2&-\alpha/2\\
\alpha/2&-\kappa-\alpha/2
\end{pmatrix},\quad
M_\kappa^2=\frac{\kappa(\alpha+\kappa)}{v^2}I.
\tag{8}
\]
For reward one, \(1-u_\pm\) satisfies the same homogeneous equation. Hence the transfer matrix through a zone of width \(L\) is
\[
\exp(LM_\kappa)=\cosh z\,I+
\frac{\sinh z}{\sqrt{\kappa(\alpha+\kappa)}/v}\,M_\kappa,
\quad z=\frac{L\sqrt{\kappa(\alpha+\kappa)}}v.
\tag{9}
\]

**3. Effective reactances of finite zones.** On either unbounded exterior, bounded solutions of the free equation must have \(u_+=u_-\), because otherwise their common mean would grow linearly with \(x\). Write \(d=u_+-u_-\) in the central gap; equation (7) with \(\kappa=0\) gives \(d'=0\) and
\[
\frac{d}{dx}\frac{u_++u_-}{2}=\frac{\alpha d}{2v}.
\tag{10}
\]
Starting from an equal-orientation value on the far left and transferring across the left reactive region by (9), the inner left mean equals \(d R_{\mathrm L}(v)/2\). Applying the analogous transfer to the right-capture failure probability \(1-u\) from the far right, the inner right mean equals \(1-dR_{\mathrm R}(v)/2\). Integrating (10) over the gap of length \(2a\) yields
\[
d=\frac{2}{R_{\mathrm L}(v)+R_{\mathrm R}(v)+2\alpha a/v}.
\tag{11}
\]
The mean at any \(x\in(-a,a)\) is its left-boundary value plus \(\alpha d(x+a)/(2v)\), and an initial mean sign \(m\) contributes \(md/2\). Substituting (11) proves (1) and (2).

**4. Strict one-crossing property.** Equation (1) gives
\[
P_{\mathrm R}(v)-\frac12=
\frac{R_{\mathrm L}(v)-R_{\mathrm R}(v)}
{2\left(R_{\mathrm L}(v)+R_{\mathrm R}(v)+2\alpha a/v\right)}.
\tag{12}
\]
Let \(t=1/v\). Direct logarithmic differentiation shows
\[
\frac{d}{dt}\log\frac{R_{\mathrm L}(1/t)}{R_{\mathrm R}(1/t)}
=-\frac{2B_{\mathrm L}}{\sinh(2B_{\mathrm L}t)}
+\frac{2B_{\mathrm R}}{\sinh(2B_{\mathrm R}t)}.
\tag{13}
\]
For each fixed \(t>0\), the function \(B\mapsto B/\sinh(2Bt)\) is strictly decreasing on \((0,\infty)\); its derivative has the sign of \(\sinh z-z\cosh z<0\), \(z>0\). Thus, if \(B_{\mathrm L}\ne B_{\mathrm R}\), the ratio in (13) is strictly monotone in \(t\). If the two \(B_i\) agree, the ratio is constant in \(t\). A strict one-crossing theorem follows after computing its two endpoint values:
\[
\lim_{v\downarrow0}\frac{R_{\mathrm L}(v)}{R_{\mathrm R}(v)}
=\frac{A_{\mathrm L}}{A_{\mathrm R}},\qquad
\lim_{v\to\infty}\frac{R_{\mathrm L}(v)}{R_{\mathrm R}(v)}
=\frac{\kappa_{\mathrm R}L_{\mathrm R}}{\kappa_{\mathrm L}L_{\mathrm L}}.
\tag{14}
\]
The first ratio lies above one exactly when \(\kappa_{\mathrm R}>\kappa_{\mathrm L}\), and the second lies above one exactly when \(\kappa_{\mathrm R}L_{\mathrm R}>\kappa_{\mathrm L}L_{\mathrm L}\). Opposite strict endpoint signs are therefore necessary and sufficient for exactly one crossing, giving (3). An endpoint equality does not produce an interior crossing under strict monotonicity. If the ratio is identically one, both \(A_i\) and \(B_i\) agree; equality of the \(A_i\) forces equality of the \(\kappa_i\), and then equality of the \(B_i\) forces equality of the \(L_i\). This proves the full degeneracy classification.

**5. Boundary asymptotics.** For \(v\downarrow0\), \(\coth(B_i/v)=1+O(e^{-2B_i/v})\); substituting in (12) and using \(a>0\) gives (5). For \(v\to\infty\), \(\coth(B_i/v)=v/B_i+O(v^{-1})\), so \(R_i(v)=v/(\kappa_iL_i)+O(v^{-1})\); inserting these in (1) gives (6).

## Verification

The standalone program `VERIFY.py` evaluates the exact expression and separately integrates the unnormalized, piecewise-constant backward differential system through both reactive zones using matrix exponentials. It performed 400 reproducible random-parameter transfer comparisons (maximum absolute difference \(1.62\times10^{-13}\)), 300 strict logarithmic-derivative tests, and 110 numerical checks of the reversal/no-reversal classification. Endpoint limits and identical-trap symmetry were also checked. These finite tests support but do not replace the general analytic proof.

A concrete reversal occurs for \(\alpha=1\), \(a=2\), \(\kappa_{\mathrm L}=0.2\), \(L_{\mathrm L}=10\), \(\kappa_{\mathrm R}=1\), \(L_{\mathrm R}=1\). The unique crossover is \(v_*\approx2.216128237000\). The right-capture probabilities are \(P_{\mathrm R}(0.5)\approx0.543178093879\) and \(P_{\mathrm R}(5)\approx0.397691176621\).

To reproduce: install Python 3 with NumPy and SciPy, then run `python VERIFY.py` from the package directory. The script has no data-file dependencies.

## Relationship to prior work

Angelani's *Run-and-tumble motion in trapping environments* [1], especially section V and equations (61)--(76), develops exact forward equations for two **symmetric** finite reactive zones and derives the stationary spatial capture profile and temporal tails. The backward transfer in (8)--(11) exploits the same telegraph-plus-killing dynamics, but the asymmetric two-zone splitting law and sharp speed-reversal classification are not stated there.

Bressloff's *Encounter-based model of a run-and-tumble particle II* [2], especially section 5, equations (5.15)--(5.20), includes splitting between two inequivalent, **sticky endpoint** traps on a confined finite interval. The two penetrable finite-width zones here are distinct: a particle can traverse either active zone without being absorbed and later return from the exterior, producing the effective \(\coth\) impedances. General splitting formulas and transfer methods themselves are prior knowledge; the claim of contribution is the concrete full finite-zone phase classification (3).

Angelani's generic-wall analysis [3] covers varying wall absorption and turning rates and reports exit-time laws, but does not give the two-penetrable-zone speed-reversal classification. Jeon, Go, and Kim [4] examine optimal mean search time for a single partially reactive target in a confined region, rather than competition between two finite targets. The present result does not claim a new general backward-equation technique or a complete theory of all possible multi-zone trapping landscapes.

## Limitations

The result assumes exactly two disjoint finite intervals, constant capture hazards within them, constant speed and spatially homogeneous tumbling, no additional diffusion, and no drift or confinement. It concerns the *probability of which trap captures first*, not the mean trapping time or all first-passage-time distributions. The equality criterion refers to a centrally released, initially fair particle; asymmetric initial data generally shift the comparison. Nearly degenerate trap parameters may produce crossover speeds far outside experimentally accessible ranges. The originality comparison cannot exclude equivalent unpublished or unidentified results; independent scientific validation has not been performed.

## References

1. L. Angelani, *Run-and-tumble motion in trapping environments*, arXiv:2303.03078, first version publicly submitted 2023-03-06. https://arxiv.org/abs/2303.03078
2. P. C. Bressloff, *Encounter-based model of a run-and-tumble particle II: absorption at sticky boundaries*, arXiv:2302.01158 (2023). https://arxiv.org/abs/2302.01158
3. L. Angelani, *One-dimensional run-and-tumble motions with generic boundary conditions*, J. Phys. A 56, 455003 (2023), doi:10.1088/1751-8121/ad009e. https://doi.org/10.1088/1751-8121/ad009e
4. E. Jeon, B. Go and Y. W. Kim, *Searching for a partially absorbing target by a run-and-tumble particle in a confined space*, arXiv:2310.04016 (2023). https://arxiv.org/abs/2310.04016
