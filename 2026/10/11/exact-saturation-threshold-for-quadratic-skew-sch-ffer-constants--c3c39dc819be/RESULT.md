# Exact saturation threshold for quadratic skew Schäffer constants on the Banaś–Frączek plane

## Finding
Let \(\lambda>1\) and let \(X_\lambda=(\mathbb R^2,N_\lambda)\) be the real Banaś–Frączek plane, where
\[
N_\lambda(u,v)=\max\{\lambda|u|,\sqrt{u^2+v^2}\}.
\]
For \(0\le\tau\le1\), define its quadratic skew Schäffer constant
\[
\mathcal S_\lambda(\tau)^2
=\inf_{N_\lambda(x)=N_\lambda(y)=1}
\frac{N_\lambda(x+\tau y)^2+N_\lambda(\tau x-y)^2}{2}.
\]
Write \(\alpha=\lambda^{-1}\in(0,1)\), \(\beta=\sqrt{1-\alpha^2}\), and \(g=(\sqrt5-1)/2\). Define
\[
\tau_c(\lambda)=
\begin{cases}
\sqrt{1+\alpha^2}-\alpha,&0<\alpha^2\le g,\\
\alpha\sqrt{1-\alpha^2},&g\le\alpha^2<1.
\end{cases}
\]
The two branches agree at \(\alpha^2=g\). The exact lower-envelope saturation theorem is
\[
\boxed{\quad
\mathcal S_\lambda(\tau)^2=\frac{(1+\tau^2)(1+\lambda^{-2})}{2}
\quad\Longleftrightarrow\quad\tau_c(\lambda)\le\tau\le1.\quad}
\]
For \(0\le\tau<\tau_c(\lambda)\), the inequality is **strict**:
\[
\mathcal S_\lambda(\tau)^2>\frac{(1+\tau^2)(1+\lambda^{-2})}{2}.
\]
In particular, the previously used sufficient threshold \(\beta=\sqrt{1-\lambda^{-2}}\) is strictly greater than the actual onset \(\tau_c(\lambda)\) for every finite \(\lambda>1\). The active extremal configuration changes at \(\lambda=\sqrt{(1+\sqrt5)/2}\): on one side it occurs at a limiting flat-side coordinate, and on the other at the interior maximizer of a strictly concave one-variable function.

## Assumptions and scope
All vectors and norms are **real**. The parameter \(\lambda>1\) is arbitrary, and \(0\le\tau\le1\). The theorem computes the exact onset of equality in a natural universal lower bound; it does **not** claim an explicit formula for \(\mathcal S_\lambda(\tau)\) in the strict regime.

For brevity write \(N=N_\lambda\), \(E(z)^2=z_1^2+z_2^2\), \(F(z)^2=\alpha^{-2}z_1^2\), and \(\kappa=\beta/\alpha\). Then \(N^2=\max\{E^2,F^2\}\), and a nonzero vector lies in the Euclidean-dominant cone precisely when \(|z_2|\ge\kappa|z_1|\). A point \(z\) on the \(N\)-unit sphere lies on a vertical flat side \(|z_1|=\alpha, |z_2|\le\beta\), or a Euclidean circular arc \(E(z)=1, |z_1|\le\alpha\), with the two descriptions overlapping only at their common endpoints.

## Proof
**Step 1: the universal envelope.** For any two \(N\)-unit vectors \(x,y\), the Euclidean parallelogram identity applied to the skew transform gives
\[
\begin{aligned}
N(x+\tau y)^2+N(\tau x-y)^2
&\ge\max\big\{F(x+\tau y)^2+F(\tau x-y)^2,\\
&\hspace{34mm}E(x+\tau y)^2+E(\tau x-y)^2\big\}\\
&=(1+\tau^2)\max\{\alpha^{-2}(x_1^2+y_1^2),E(x)^2+E(y)^2\}.
\end{aligned}
\]
The last maximum is at least \(1+\alpha^2\). Indeed, if both input points lie on flat sides, its first entry is \(2\); if both lie on circular arcs, its second entry is \(2\). In the remaining case one input lies on a flat side and the other on a circular arc, whence the second entry is at least \(\alpha^2+1\). Thus
\[
\mathcal S_\lambda(\tau)^2\ge\frac{(1+\tau^2)(1+\alpha^2)}2.
\]
The unit sphere is compact, so the infimum in this expression is attained for every parameter.

**Step 2: necessary structure of any equality pair.** Since \(\alpha<1\), the cases with both inputs on flat sides or both on circular arcs cannot give equality. Exactly one input must lie on a flat side and the other on a circular arc. The Euclidean branch sum must equal \(1+\alpha^2\), so the flat-side input has zero second coordinate. The first-coordinate branch sum must not exceed \(1+\alpha^2\); consequently, the circular-arc input has first coordinate \(a\) satisfying \(|a|\le\alpha^2\).

The skew objective is invariant under \((x,y)\mapsto(y,-x)\) and under simultaneous coordinate reflections. We may therefore write an equality pair as
\[
x=(a,b),\qquad y=(\alpha,0),\qquad |a|\le\alpha^2,
\qquad b=\sqrt{1-a^2}\ge0.
\]
Here the unweighted Euclidean sums already attain the envelope. Equality in the first displayed inequality additionally requires **both** outputs \(x+\tau y\) and \(\tau x-y\) to be Euclidean-dominant. For the second output this says
\[
\tau b\ge\kappa|\tau a-\alpha|.
\]
Because \(0\le\tau\le1\) and \(a\le\alpha^2<\alpha\), this implies
\[
\tau\left(\sqrt{1-a^2}+\kappa a\right)\ge\beta.
\]
Therefore \(\tau\ge\beta/m\), where
\[
m=\max_{-\alpha^2\le a\le\alpha^2}
\left(\sqrt{1-a^2}+\kappa a\right).
\]

**Step 3: exact minimax evaluation and phase transition.** The function \(r(a)=\sqrt{1-a^2}+\kappa a\) is strictly concave on the indicated interval, and its unconstrained critical point is \(a=\beta\). Therefore its unique maximum occurs at
\[
a_*=\min\{\beta,\alpha^2\}.
\]
The inequality \(\beta\ge\alpha^2\) is equivalent to \(\alpha^2\le g\), since \(g\) is the positive root of \(g^2+g=1\). If \(\alpha^2\le g\), then
\[
m=\sqrt{1-\alpha^4}+\alpha\beta
=\beta\bigl(\sqrt{1+\alpha^2}+\alpha\bigr),
\quad\frac\beta m=\sqrt{1+\alpha^2}-\alpha.
\]
If \(\alpha^2\ge g\), then
\[
m=\sqrt{1-\beta^2}+\kappa\beta=\frac1\alpha,
\quad\frac\beta m=\alpha\beta.
\]
Thus any equality pair requires \(\tau\ge\tau_c(\lambda)\).

**Step 4: explicit equality pairs at every admissible parameter.** First, \(\tau_c(\lambda)<\beta\) for every \(\alpha\in(0,1)\): in the second branch this follows from \(\alpha<1\), and in the first it follows by squaring \(\sqrt{1+\alpha^2}<\alpha+\beta\), valid because \(\alpha^2\le g<4/5\).

For \(\beta\le\tau\le1\), choose \(x=(0,1)\) and \(y=(\alpha,0)\). Both outputs are Euclidean-dominant, so their squared norms sum to \((1+\tau^2)(1+\alpha^2)\).

For \(\tau_c\le\tau\le\beta\), let \(a\in[0,a_*]\) be the unique solution of
\[
\sqrt{1-a^2}+\kappa a=\frac\beta\tau.
\]
Such a solution exists because the left side increases continuously from \(1\) to \(m=\beta/\tau_c\) on \([0,a_*]\), while \(\beta/\tau\in[1,m]\). Put \(b=\sqrt{1-a^2}\), \(x=(a,b)\) and \(y=(\alpha,0)\). Then \(x,y\) are \(N\)-unit vectors, \(|a|\le\alpha^2\), and
\[
\tau(b+\kappa a)=\beta,
\]
so \(\tau x-y\) lies on the boundary of the Euclidean-dominant cone. Moreover,
\[
(b-\kappa a)(b+\kappa a)
=1-\frac{a^2}{\alpha^2}\ge1-\alpha^2=\beta^2,
\]
whence \(b-\kappa a\ge\beta\tau\). Equivalently, \(b\ge\kappa(a+\tau\alpha)\), proving that \(x+\tau y\) also lies in that cone. Hence both output norms equal their Euclidean norms and
\[
\frac{N(x+\tau y)^2+N(\tau x-y)^2}{2}
=\frac{(1+\tau^2)(E(x)^2+E(y)^2)}2
=\frac{(1+\tau^2)(1+\alpha^2)}2.
\]
This proves sufficiency including \(\tau=\tau_c\). Necessity plus attainment of the sphere minimum gives a **strict** gap for \(\tau<\tau_c\), completing the proof.

## Verification
The algebraic proof above is independent of numerical experiments. A self-contained executable diagnostic accompanies this result. Its exact rational case uses \(\alpha=4/5\), \(\beta=3/5\), the sharp parameter \(\tau_c=12/25\), and the exact equality pair
\[
x=(3/5,4/5),\qquad y=(4/5,0),
\]
for which the squared objective is exactly \(31529/31250\). This equals the lower envelope \((1+\tau_c^2)(1+\alpha^2)/2\), and the second output lies exactly on the Euclidean/flat-cone boundary. The same diagnostic also checks a second rational-parameter branch with high-precision arithmetic. These are **finite checks only**; the exact global parameter threshold, strict below-threshold inequality, and attainment for all \(\lambda\) are consequences of Steps 1–4, not computational extrapolations.

## Relationship to prior work
Ying Xu and Qi Liu, *Skew Schäffer Type Constants*, arXiv:2610.03050v1 (publicly posted 2026-10-02), introduce the infimal skew constant and prove in Example 3.5 the lower-envelope formula on the sufficient range \(\sqrt{1-\lambda^{-2}}\le\tau\le1\). Their fixed test pair becomes extremal at that endpoint. The present theorem determines the **smallest permissible parameter for any extremizing pair** and shows that their sufficient threshold is never sharp for \(\lambda>1\). This is not a restatement of that fixed-pair construction: a continuous family of tilted circular-arc witnesses is essential below its endpoint.

Chen, Liu, Tan, and Wang, *Skew generalized von Neumann-Jordan constant for the Banaś-Frączek space*, arXiv:2412.11665v1, study a **supremal** skew quotient with a different normalization and, for their exact formula, additional parameter assumptions. A supremum does not determine the constrained unit-sphere **infimum** above or the contact threshold. Earlier Banaś–Frączek James and von Neumann–Jordan calculations address different constants. Closely related exact results on Ptolemy constants, Euclidean Banach–Mazur distances, and the supremal Euler–Lagrange envelope likewise do not imply the sharp infimal saturation boundary.

## Limitations
The theorem gives the complete equality-versus-strictness phase diagram for the established lower envelope, **not** the exact skew Schäffer value below the transition. It is restricted to the real two-dimensional Banaś–Frączek norm and the quadratic exponent. The golden-ratio switch concerns the maximizing parameter in the contact-cone condition, not a new universal Banach-space modulus. A mathematical literature search cannot exclude an unindexed equivalent equality analysis, and no independent human or external audit is represented here.

## References
1. Y. Xu and Q. Liu, *Skew Schäffer Type Constants*, arXiv:2610.03050v1, first posted 2026-10-02. Full HTML: https://arxiv.org/html/2610.03050v1, especially Definition (2) and Example 3.5.
2. L. Chen, Q. Liu, X. Tan, and Y. Wang, *Skew generalized von Neumann-Jordan constant for the Banaś-Frączek space*, arXiv:2412.11665v1, first posted 2024-12-16. Full HTML: https://arxiv.org/html/2412.11665v1.
3. J. Banaś and K. Frączek, *Deformation of Banach spaces*, Comment. Math. Univ. Carolinae 34 (1993), 47–53.
4. C. Yang and X. Yang, *On the James type constant and von Neumann-Jordan constant for a class of Banaś–Frączek type spaces*, J. Math. Inequal. 10 (2016), 551–558. DOI: 10.7153/jmi-10-43.
