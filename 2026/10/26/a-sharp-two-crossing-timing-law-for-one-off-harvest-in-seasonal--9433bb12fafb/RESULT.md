# A sharp two-crossing timing law for one-off harvest in seasonal Ricker recruitment

## Finding

Let \(F_i(x)=R_i x\exp(-a_i x)\), with \(R_i,a_i>0\) for seasons \(i=1,2\). A single proportional removal retains a fraction \(0<s<1\) of the current stock. From the same initial stock \(x>0\), compare removal **before season 1**, giving \(E(x)=F_2(F_1(sx))\), with removal **between seasons**, giving \(L(x)=F_2(sF_1(x))\). Both policies have precisely two recruitment steps and one identical proportional removal.

Define the dimensionless cross-season pressure \(\rho=a_2R_1/a_1\), and the critical pressure and unique critical stock
\[
\rho_c(s)=s^{-1/(1-s)},\qquad x_m=\frac{-\log s}{a_1(1-s)}.
\]
The *complete timing classification* for positive initial stock is:

1. If \(\rho<\rho_c(s)\), then \(E(x)>L(x)\) for every \(x>0\).
2. If \(\rho=\rho_c(s)\), then \(E(x)\ge L(x)\) for every \(x>0\), with equality at precisely \(x=x_m\).
3. If \(\rho>\rho_c(s)\), there are precisely two stocks \(0<x_-<x_m<x_+\) satisfying \(E(x_\pm)=L(x_\pm)\). The strict inequality \(E(x)<L(x)\) holds exactly when \(x_-<x<x_+\); outside that closed interval, \(E(x)>L(x)\). The thresholds are specified uniquely by
\[
\exp(-s a_1x)-\exp(-a_1x)=\frac{1-s}{s\rho}.
\]

At a small supercritical excess \(\rho=\rho_c(s)(1+\varepsilon)\), \(\varepsilon\downarrow0\), the thresholds split according to
\[
x_\pm=x_m\pm\frac{1}{a_1}\sqrt{\frac{2\varepsilon}{s}}+O(\varepsilon/a_1),
\]
for fixed \(s\in(0,1)\). The entire comparison is *independent* of the terminal season's uncrowded recruitment multiplier \(R_2\), but generally depends on its crowding coefficient \(a_2\). A one-recruitment-step comparison, by contrast, has no stock-dependent reversal: \(F_i(sx)>sF_i(x)\) for all \(x>0\). Thus two recruitment steps are the shortest horizon with this three-region timing pattern.

## Assumptions and scope

Stock is deterministic and strictly positive. Seasons are consecutive, each with exactly one density-regulated Ricker recruitment update. There is exactly one instantaneous proportional harvest, at one of the two specified dates; no other removal or feedback action occurs. The comparison is terminal stock after season 2, not catch, average long-run stock, extinction probability, or a cost-adjusted objective. Parameters \(R_1,R_2,a_1,a_2\) are any positive real numbers, \(s\in(0,1)\), and \(x\in(0,\infty)\). The parameter \(a_i\) has reciprocal-stock units. The pressure \(\rho\) is dimensionless.

## Proof

Direct composition, with every factor positive, gives
\[
E(x)=R_1R_2s x\exp\!\left(-a_1s x-a_2s R_1x\exp(-a_1s x)\right),
\]
\[
L(x)=R_1R_2s x\exp\!\left(-a_1x-a_2s R_1x\exp(-a_1x)\right).
\]
Put \(z=a_1x>0\). Dividing the two expressions produces the **exact identity**
\[
\log\frac{E(x)}{L(x)}=z\left[(1-s)-s\rho\bigl(\exp(-sz)-\exp(-z)\bigr)\right].\tag{1}
\]
In particular the common positive factor \(R_2\) cancels; no monotonicity of the potentially overcompensatory map \(F_2\) is assumed.

Set \(h(z)=\exp(-sz)-\exp(-z)\). We have \(h(0)=0\), \(h(z)>0\) for \(z>0\), and \(h(z)\to0\) as \(z\to\infty\). Its derivative is \(h'(z)=\exp(-z)-s\exp(-sz)\). Consequently \(h'\) has the unique zero \(z_m=-\log(s)/(1-s)\), with \(h\) strictly increasing up to \(z_m\) and strictly decreasing thereafter. At that point, \(\exp(-z_m)=s\exp(-sz_m)\), so
\[
h(z_m)=(1-s)s^{s/(1-s)}.
\]

The sign of (1) is the sign of \((1-s)-s\rho h(z)\). Its minimum is nonnegative precisely when \(s\rho(1-s)s^{s/(1-s)}\le1-s\), equivalently \(\rho\le s^{-1/(1-s)}\). Strict monotonicity of \(h\) on either side of its unique maximum proves the exact zero counts and strict signs in all three regimes. Equality at the critical parameter occurs only at \(z=z_m\), giving the specified \(x_m\).

For the threshold-splitting law, \(h''(z_m)=-s(1-s)\exp(-s z_m)=-s h(z_m)\). Hence
\[
\frac{h(z_m+w)}{h(z_m)}=1-\frac{s}{2}w^2+O(w^3).
\]
At \(\rho=\rho_c(s)(1+\varepsilon)\), a threshold satisfies \(h(z)/h(z_m)=(1+\varepsilon)^{-1}\). Comparing expansions first yields \(w=O(\sqrt\varepsilon)\), then \(w=\pm\sqrt{2\varepsilon/s}+O(\varepsilon)\), with one root on each side by the previous monotonicity. Division by \(a_1\) gives the stated law.

Finally, for a single recruitment map \(F_i\),
\[
\frac{F_i(sx)}{sF_i(x)}=\exp(a_i(1-s)x)>1.
\]
One recruitment step cannot produce the two-reversal stock pattern.

**Exact witness and stable-map implication.** With \(a_1=a_2=1\), \(s=1/2\), \(R_1=5\), and any \(R_2>0\), the critical pressure is \(4\), while the two roots have the closed forms
\[
x_-=-2\log\frac{1+1/\sqrt5}{2},\qquad x_+=-2\log\frac{1-1/\sqrt5}{2}.
\]
At \(x=2\log(4/3)\), \(2\log2\), and \(2\log4\), respectively, the square-bracket factor in (1) is exactly \(1/32\), \(-1/8\), and \(1/32\), verifying all three strict regions without approximate arithmetic. The effect does not require unstable unharvested recruitment: choose \(s=4/5\), \(a_1=a_2=1\), \(R_1=4\). Then \(\rho=4>(5/4)^5=\rho_c(s)\), although the unharvested first-season Ricker equilibrium has multiplier \(1-\log4\in(-1,1)\).

## Verification

Execute the accompanying standalone, standard-library-only program as `python verify.py`. It compares independently evaluated two-stage compositions with (1) across 8,000 seeded positive parameter tuples, examines all three comparison regions for 2,207 supercritical tuples, and checks the exact rational signs of the witness. Its recorded result was `PASS`. These finite experiments check implementation and displayed examples, not the universal theorem, which follows from the preceding calculus argument.

## Relationship to prior work

Ricker's original stock–recruitment analysis [1] established the density-overcompensating ecological mechanism. Jonzén–Lundberg [2] and Abrams [3] studied why the ordering of mortality and density regulation matters; Liz–Hilker [4] compared ongoing pre- and post-recruitment proportional harvesting, including dynamical equivalence and long-run hydra effects. Grey et al. [5] studied time-varying harvesting controls and within-season mechanics. None of the materially inspected passages in [3]–[5] states the exact **single-pulse, two-consecutive-season, initial-stock-dependent** two-crossing classification or the universal parameter boundary \(\rho_c(s)\). The particular distinction is between choosing *which of two seasons receives the one-time pulse*, rather than choosing whether a recurrent annual policy acts before or after reproduction. It is possible that more general results imply this specialization; the inaccessible complete primary texts and that risk are recorded in the accompanying review.

## Limitations

This is a short finite-horizon comparison, not a general optimal policy for arbitrarily many seasons or multiple harvests. It says nothing about catch yield, cost, stochastic demographic variability, or discrete integer-valued stock. The final-season multiplier invariance is special to the exact exponential Ricker form and may fail for other recruitment families. Inaccessible relevant historical full texts and possible more general nonlinear-map rearrangement results limit any claim of historical novelty. No independent audit has been performed.

## References

[1] W. E. Ricker, "Stock and Recruitment," *Journal of the Fisheries Research Board of Canada* 11 (1954), 559–623, doi:10.1139/f54-039; first public date recorded as 1954-05-01.

[2] N. Jonzén and P. Lundberg, "Temporally structured density-dependence and population management," *Annales Zoologici Fennici* 36 (1999), 39–44, https://www.annzool.net/PDF/anzf36/anzf36-039p.pdf.

[3] P. A. Abrams, "When does greater mortality increase population size? The long history and diverse mechanisms underlying the hydra effect," *Ecology Letters* 12 (2009), 462–474, doi:10.1111/j.1461-0248.2009.01282.x.

[4] E. Liz and F. M. Hilker, "Harvesting and Dynamics in Some One-Dimensional Population Models," in *Theory and Applications of Difference Equations and Discrete Dynamical Systems* (2014), doi:10.1007/978-3-662-44140-4_3, https://www.dma.uvigo.es/~eliz/pdf/oman.pdf.

[5] S. Grey, S. Lenhart, F. M. Hilker, and D. Franco, "Optimal control of harvest timing in discrete population models," *Natural Resource Modeling* 34 (2021), e12321, doi:10.1111/nrm.12321.
