# A unique Laplace-order reversal between sticky-wall desorption protocols

## Finding
For a run-and-tumble searcher with a sticky partially absorbing wall, the entire positive-discount ordering of two physically distinct desorption protocols has **at most one sign reversal**. This theorem is a precise phase classification; it is not a claim that one full first-passage-time distribution is always stochastically smaller.

Write \(\mathcal L_N(s)=\mathbb E e^{-sT_N}\) for desorption directly from the wall and \(\mathcal L_R(s)=\mathbb E e^{-sT_R}\) for desorption by resetting to the bulk initial state. The two protocols use precisely the same bulk resetting, wall holding time, and adsorption-to-absorption decision.

**Theorem.** For every \(s>0\), the sign of \(\mathcal L_N(s)-\mathcal L_R(s)\) is independent of the absorption probability and of the distribution of the wall holding time. It is positive throughout for an initially right-moving searcher. For an initially left-moving searcher, set
\[
c=\frac{\alpha x_0}{v}.
\]
If \(c\ge1\), the sign is positive throughout. If \(0<c<1\), let \(t_c>0\) solve the *unique* equation
\[
\frac{t_c}{\sinh t_c}=c,\qquad r_c=\alpha(\cosh t_c-1).
\]
For \(r\ge r_c\), the sign is positive throughout. For \(0<r<r_c\), it is negative on \((0,r_c-r)\), zero at the single crossing \(s=r_c-r\), and positive on \((r_c-r,\infty)\).

The reversal is operationally meaningful: with finite mean wall holding time and initially left-moving reset orientation, \(r<r_c\) gives \(\mathbb E T_R<\mathbb E T_N\), while for **every** \(s>r_c-r\) it gives \(\mathcal L_N(s)>\mathcal L_R(s)\). These two distributions consequently are not ordered by first-order stochastic dominance.

## Assumptions and scope
Fix \(v,x_0,\alpha,r>0\), an initial orientation \(\kappa\in\{+,-\}\), and \(p\in(0,1)\). In the bulk \(x>0\), the particle moves at velocity \(\pm v\) and switches velocity sign at rate \(\alpha\). Independently, at rate \(r\), it resets to the fixed state \((x_0,\kappa)\). The first bulk arrival at \(0\) occurs with leftward velocity and starts an adsorption episode. There it waits an independent \(W\), finite almost surely and nonnegative. At the end, it is permanently absorbed with probability \(p\); otherwise it returns to the bulk according to N (\((0,+)\)) or R (\((x_0,\kappa)\)). All wall waits, absorption decisions, bulk tumbles, and bulk resets are freshly independent between episodes, and the wall state itself is not bulk-reset. Time to permanent absorption is \(T_N\) or \(T_R\), measured from the common initial bulk state. There is no bulk translational Brownian noise.

No finite moment of \(W\) is required for the transform-order theorem; the mean-time comparison additionally requires \(\mathbb E W<\infty\). The splitting parameter \(p\) must be strictly between zero and one to obtain strict comparisons. The positive bulk reset rate makes each adsorption time finite almost surely.

## Proof
**1. Bulk adsorption transforms.** For \(s>0\), put
\[
u=r+s,\quad K=\sqrt{u(u+2\alpha)},\quad q=K/v,\quad \vartheta=\frac{\alpha}{u+\alpha+K},\quad E=e^{-qx_0}.
\]
Write \(a_-=1\) and \(a_+=\vartheta\). With no bulk resets, the Laplace transforms of first adsorption starting at \((x,+)\) and \((x,-)\) are, respectively, \(\vartheta e^{-qx}\) and \(e^{-qx}\). This follows by solving the two-by-two backward telegraph equations with boundary condition \(F_-(0)=1\) and boundedness at infinity.

With bulk resetting, write \(f_\kappa(s)\) for the transform of adsorption time from the bulk reset state. The backward equations are
\[
\sigma v\,F_\sigma'(x)+\alpha(F_{-\sigma}(x)-F_\sigma(x))+r(f_\kappa-F_\sigma(x))=sF_\sigma(x),
\quad F_-(0)=1.
\]
The bounded solution is
\[
F_-(x)=\frac{r f_\kappa}{u}+\left(1-\frac{r f_\kappa}{u}\right)e^{-qx},\qquad
F_+(x)=\frac{r f_\kappa}{u}+\vartheta\left(1-\frac{r f_\kappa}{u}\right)e^{-qx}.
\]
The self-consistency condition \(f_\kappa=F_\kappa(x_0)\) gives
\[
\boxed{f_\kappa(s)=\frac{u a_\kappa E}{s+r a_\kappa E}}.
\]
The corresponding transform from the wall immediately moving right is
\[
\boxed{g_\kappa(s)=F_+(0)=\vartheta+\frac r u(1-\vartheta)f_\kappa(s)}.
\]
These expressions are in \((0,1)\) for every \(s>0\).

**2. Absorption renewal and exact sign factorization.** Let \(\widehat w(s)=\mathbb E e^{-sW}\), so \(0<\widehat w(s)\le1\). At each wall visit, the same independent waiting time is incurred. The number of failed adsorption episodes before permanent absorption is geometric with success probability \(p\). Conditioning on each episode yields
\[
\mathcal L_N(s)=\frac{p\widehat w(s) f_\kappa(s)}{1-(1-p)\widehat w(s)g_\kappa(s)},\qquad
\mathcal L_R(s)=\frac{p\widehat w(s) f_\kappa(s)}{1-(1-p)\widehat w(s)f_\kappa(s)}.
\]
The denominators are positive. Subtracting demonstrates that the strict sign is exactly that of \(g_\kappa-f_\kappa\), irrespective of \(p\) and \(\widehat w\). Direct elimination gives the decisive identity
\[
\boxed{g_\kappa(s)-f_\kappa(s)=\frac{s(\vartheta-a_\kappa E)}{s+r a_\kappa E}}.
\]
For \(\kappa=+\) this is \(s\vartheta(1-E)/(s+r\vartheta E)>0\).

**3. The unique reversal for the left-moving state.** Take \(\kappa=-\), so \(a_-=1\). Set \(t=\operatorname{arcosh}(1+u/\alpha)>0\) and \(c=\alpha x_0/v\). Then
\[
K=\alpha\sinh t,\qquad \vartheta=e^{-t},\qquad E=e^{-c\sinh t},
\]
so the sign of \(\vartheta-E\) is exactly the sign of \(c\sinh t-t\). The continuous function \(h(t)=t/\sinh t\) satisfies \(h(0+)=1\), \(h(\infty)=0\) and
\[
h'(t)=\frac{\sinh t-t\cosh t}{\sinh^2t}<0\quad(t>0),
\]
since \(t\cosh t-\sinh t\) starts at zero and has derivative \(t\sinh t>0\). Consequently if \(c\ge1\) the sign is always positive. If \(0<c<1\) there is a unique \(t_c>0\) with \(h(t_c)=c\). Since \(u=\alpha(\cosh t-1)\) is strictly increasing in \(t\), the sign is positive precisely when \(u=r+s>r_c=\alpha(\cosh t_c-1)\), and negative precisely when \(u<r_c\). This proves every boundary case and uniqueness of the positive-frequency crossing.

**4. Mean consequence and stochastic-order obstruction.** If \(\mathbb EW<\infty\), the geometric-renewal formula gives
\[
\mathbb ET_N-\mathbb ET_R=\frac{1-p}{p}\bigl(\mathbb E\tau_N-\mathbb E\tau_R\bigr)
=\frac{1-p}{pr}\left(1-\frac{\vartheta_r}{E_r}\right),
\]
where \(E_r=\exp[-x_0\sqrt{r(r+2\alpha)}/v]\) and \(\vartheta_r=\alpha/(r+\alpha+\sqrt{r(r+2\alpha)})\). The second identity follows from \(g_--f_-=s(\vartheta-E)/(s+rE)\) upon differentiation at \(s=0\). At \(r<r_c\), \(\vartheta_r<E_r\), hence \(\mathbb ET_N>\mathbb ET_R\). But the strict reversed transform ordering for \(s>r_c-r\) rules out stochastic dominance of N or R in either direction (a first-order stochastic order would impose one unchanging Laplace-transform sign). At \(r=r_c\), the finite means agree although the transforms differ at all \(s>0\). For infinite-mean wall time no mean assertion is made.

## Verification
The self-contained `verify.py` uses Python standard-library arithmetic to compare the rational transform and factorization identities, check positivity and strict sign in many regimes, and independently test the two backward equations and reset-state boundary conditions by centered finite differences. At packaging, it passed 12,118 deterministic numerical checks. These finite calculations corroborate algebra, not the proof of the global assertion. A symbolic consistency check separately confirmed the exact factorization for either orientation. Reproduce with `python verify.py` on Python 3.10 or newer. The monotonicity, unique crossing, and heavy-tail-wait independence are established analytically above, not by parameter-grid sampling.

## Relationship to prior work
Bressloff and Linn, *Renewal theory for a run-and-tumble particle with stochastic resetting and a sticky boundary* (arXiv:2602.02446v1; Phys. Rev. E 113, 054122, 2026), establish the underlying telegraph-reset model, general renewal identities and the individual absorption-time Laplace transforms (their §IV, especially equations (4.4), (4.6) and (4.15)). They also compare **mean** absorption times and give numerical phase plots (Figures 9–10). Those formulas and the mean comparison are pre-existing, not novel here. The additional claim here is a quantified and globally exhaustive **strict Laplace-transform ordering**, its unique positive-discount reversal, an explicit analytic reset-rate boundary, and its distribution-free holding-time robustness. It follows from a new sign factorization and a global hyperbolic-ratio monotonicity argument applied to those existing renewal transforms. Any interpretation of those general transforms as already fully covering every derived sign consequence would reduce its originality; that is a genuine boundary of the claim, not concealed.

For context, Bressloff, *Random search with stochastic resetting: When finding the target is not enough* (Phys. Rev. E 111, 054127, 2025), develops related adsorption/absorption renewal equations in a Brownian-search setting; the two-orientation telegraph protocol comparison and its single-crossing frequency law are not statements of that work. Earlier run-and-tumble resetting renewal analyses treat different boundary models.

## Limitations
This result holds for a one-dimensional two-velocity telegraph process, not translationally diffusive or interacting active particles. Strict inequalities require nonzero bulk resetting and a genuine chance of both desorption and absorption. Laplace-transform order alone does **not** imply first-order stochastic dominance; no such inference is made. The complete absorption-time distributions are already available implicitly through the source's renewal formulas, and the present uniqueness classification is an analytical consequence of those formulas; its degree of independent novelty should be assessed with this fact in view. No independent external audit has been conducted.

## References
1. P. C. Bressloff and S. Linn, *Renewal theory for a run-and-tumble particle with stochastic resetting and a sticky boundary*, arXiv:2602.02446v1 (first public 2026-02-02), *Physical Review E* **113**, 054122 (2026), DOI:10.1103/dcnh-bhwc. https://arxiv.org/abs/2602.02446
2. P. C. Bressloff, *Random search with stochastic resetting: When finding the target is not enough*, *Physical Review E* **111**, 054127 (2025).
3. M. R. Evans and S. N. Majumdar, *Run and tumble particle under resetting: A renewal approach*, *Journal of Physics A* **51**, 475003 (2018).
