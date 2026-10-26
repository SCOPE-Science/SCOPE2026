# A sharp rainfall-sequencing law for a Green–Ampt infiltration model

## Finding

In the instantaneous-runoff, single-wetting-front Green–Ampt model, placing more intense rainfall earlier maximizes infiltration for a fixed rainfall-intensity distribution, while placing it later minimizes infiltration. More precisely, for every bounded nonnegative measurable rainfall intensity \(r\) on \([0,T]\), with its nonincreasing and nondecreasing rearrangements \(r^{\downarrow}\) and \(r^{\uparrow}\),
\[
F_{r^{\downarrow}}(T)\ge F_r(T)\ge F_{r^{\uparrow}}(T).
\]
Consequently, since all three storms have equal rainfall volume, their total direct runoff is ordered in the opposite direction.

The equality boundary is sharp for two unequal positive constant-rate blocks. Let \(0<\ell<h\) have durations \(v>0\) and \(u>0\), respectively; denote by \(F_{HL}\) the terminal infiltration with the high block first and by \(F_{LH}\) that with the low block first. If \(h\le K\), the terminal infiltrations are equal. If \(h>K\), put
\[
F_h=\frac{KB}{h-K},\qquad
F_\ell=\begin{cases}\frac{KB}{\ell-K},&\ell>K,\\ +\infty,&0<\ell\le K.\end{cases}
\]
Then the complete strictness criterion is
\[
\boxed{F_{HL}>F_{LH}\quad\Longleftrightarrow\quad F_0<F_\ell\ \text{ and }\ F_0+hu+\ell v>F_h.}
\]
Equality holds in all remaining cases. No strictness statement is claimed for arbitrary multiblock storms.

## Assumptions and scope

Fix \(T>0\), saturated hydraulic conductivity \(K>0\), suction-storage parameter \(B>0\), and initial cumulative infiltration \(F_0\ge0\). The only state is cumulative infiltration \(F(t)\) and the process is governed almost everywhere by
\[
\frac{dF}{dt}=\min\left\{r(t),K\left(1+\frac{B}{F(t)}\right)\right\},\qquad F(0)=F_0.
\]
At \(F=0\), the capacity is interpreted as \(+\infty\), so the right-hand side equals the finite rainfall rate. The rate \(r\) is any essentially bounded nonnegative measurable function. Excess rainfall leaves immediately as runoff: there is no surface detention or re-infiltration. Soil conductivity and suction are constant; there is no wetting-front redistribution, evaporation, groundwater interaction, or inter-event drying. Cumulative infiltration is nondecreasing even when rainfall ceases.

The quantity \(r^{\downarrow}\) is the equimeasurable nonincreasing rearrangement of \(r\), and \(r^{\uparrow}(t)=r^{\downarrow}(T-t)\), up to null sets. Final direct runoff is \(J_r=\int_0^T r(t)\,dt-F_r(T)+F_0\). These results concern this particular reduced infiltration law, not all hydrological infiltration models or a ponded Green–Ampt model.

## Proof

**Existence and comparison.** For bounded rainfall, the flux \(G_r(F)=\min\{r,K(1+B/F)\}\) is bounded by \(r\), continuous and nonincreasing in \(F\ge0\), where the value at zero is defined by continuity. The Carathéodory solution exists uniquely, is nonnegative and absolutely continuous. Nonincrease in the state also yields the stability estimate
\[
\sup_{0\le t\le T}|F_r(t)-F_s(t)|\le\int_0^T |r(t)-s(t)|\,dt.
\]
Indeed, at almost every time where the signed difference of the two solutions is nonzero, the contribution from differing states has sign opposed to that difference, while \(|G_r(F)-G_s(F)|\le|r-s|\); integrate the upper Dini derivative of the absolute difference.

**Two-block interchange.** Fix \(0<\ell<h\) and let \(g_h(F)=\min\{h,K(1+B/F)\}>0\). Define the increasing high-rate clock
\[
z=Z(F)=\int_{F_0}^{F}\frac{ds}{g_h(s)},\qquad F=Z^{-1}(z).
\]
In \(z\)-coordinates a high-intensity block produces \(\dot z=1\); a low-intensity block produces \(\dot z=w(z)\), where
\[
w(z)=\frac{\min\{\ell,K(1+B/Z^{-1}(z))\}}{\min\{h,K(1+B/Z^{-1}(z))\}}.
\]
As \(z\) increases, capacity decreases, so \(w\) is nondecreasing: it starts at \(\ell/h\) when capacity exceeds \(h\), rises strictly as capacity falls from \(h\) to \(\ell\), and equals \(1\) once capacity falls below \(\ell\). Let \(\Psi_v(z)\) be the low-rate flow for duration \(v\). Its derivative with respect to its starting point is
\[
\frac{\partial\Psi_v(z)}{\partial z}=\frac{w(\Psi_v(z))}{w(z)}\ge1,
\]
by differentiating \(\int_z^{\Psi_v(z)} ds/w(s)=v\). Hence
\[
\Psi_v(u)-\Psi_v(0)\ge u,
\]
which is exactly the terminal-coordinate comparison between high-then-low and low-then-high. Because \(Z^{-1}\) is strictly increasing, this proves \(F_{HL}\ge F_{LH}\). Zero-intensity blocks follow from continuity as \(\ell\downarrow0\), with equality because they leave \(F\) unchanged.

**Exact two-block strictness.** When \(h\le K\), the capacity is always at least \(h\), so the order cannot matter. Otherwise, the only interval where \(w\) grows strictly is \(F_h<F<F_\ell\). The derivative above exceeds one on a positive set of start points \(z\in(0,u)\) precisely when a low-flow path issuing from this interval of high-clock start points traverses a positive portion of that growth interval. Since both low and high flows are strictly increasing, this happens precisely when \(F_0<F_\ell\) and the high-then-low final state lies above \(F_h\). Before first reaching \(F_h\), both blocks infiltrate at their imposed rates, so the latter condition is exactly \(F_0+hu+\ell v>F_h\). If either condition fails, all relevant low-flow segments lie in flat parts of \(w\) and the derivative equals one throughout, proving equality. This establishes the stated if-and-only-if boundary, including equality at both threshold surfaces.

**Arbitrary rainfall sequences.** For a finite step storm, interchanging any adjacent inverted pair (a lower positive rate followed by a higher one) cannot decrease the final infiltration, by the two-block comparison applied at their current initial wetting-front state. Moreover, the scalar differential equation preserves the order of distinct current states under any common suffix of the storm. Repeated adjacent interchanges therefore yield the nonincreasing order as maximizer and the nondecreasing order as minimizer. Zero blocks commute trivially. For general bounded measurable \(r\), approximate it in \(L^1[0,T]\) by nonnegative step functions; their decreasing and increasing rearrangements converge in \(L^1\), because rearrangement is nonexpansive in \(L^1\). The solution stability estimate passes both inequalities to the limit.

## Verification

The standalone program `infiltration_order_checker.py` implements each constant-rate flow by solving the exact capacity-limited Green–Ampt primitive with monotone bisection (not an Euler time discretization). It reproduces the strict/equal two-block cases and checks 3000 reproducibly seeded random parameter choices. The program illustrates the theorem; the preceding arguments prove it for infinitely many possible inputs.

For \(K=B=1\), \(F_0=1/4\), \(h=3\), \(\ell=3/2\), and \(u=v=1/5\), the two final infiltrations are approximately \(F_{HL}=1.097721699\) and \(F_{LH}=1.009760758\). The high-first storm therefore infiltrates approximately \(0.087960941\) more, with equal total rainfall \(0.9\). The capacity thresholds are \(F_h=1/2\) and \(F_\ell=2\), so both strictness inequalities hold.

## Relationship to prior work

The Green–Ampt framework and variable-rainfall applications are classical. Gowdish and Muñoz-Carpena (2009) model uneven multistorm rainfall and redistribution, considering numerical agreement with more detailed infiltration laws; their model can include repeated wetting fronts. Lai and colleagues (2015) analyze stable infiltration-and-redistribution simulation under complex rainfall and shallow-water-table conditions. Neither inspected full-text treatment asserts an extremal theorem over all equimeasurable rainfall schedules or gives the two-block if-and-only-if strictness thresholds for the present scalar instantaneous-runoff equation. The comparison is about mathematical implications and explicitly does not identify the richer physical models with this simplified ODE.

Chu (1978) and Philip (1993) discuss variable rainfall and infiltration; their accessible abstracts are relevant context, but their full texts were not inspected here. In particular, Philip studies variable-head ponding, a different boundary condition, and a hidden equivalent special-case result remains possible. A general rearrangement theorem for monotone scalar flows might also imply the weak inequality, even without using hydrological terminology. The novelty assessment is therefore narrow and subject to independent literature review.

## Limitations

The result does **not** extend as stated to rainfall carried forward as ponded surface storage, infiltration with drying/redistribution during interstorm intervals, spatially variable conductivity, changing wetting-front suction, or unsaturated multiphase flow. Strictness is classified only for the two-block case. The numerical script is illustrative and does not certify novelty. The comparison with older inaccessible works and broad rearrangement theory is incomplete, so the originality assessment is provisional, not an independent audit.

## References

1. Gowdish, L. and Muñoz-Carpena, R. (2009), "An Improved Green–Ampt Infiltration and Redistribution Method for Uneven Multistorm Series," *Vadose Zone Journal* **8**, 470–479. DOI: `10.2136/vzj2008.0049`, first public 2009-05-01.
2. Lai, W., Ogden, F. L., Steinke, R. C., and Talbot, C. A. (2015), "An efficient and guaranteed stable numerical method for continuous modeling of infiltration and redistribution with a shallow dynamic water table," *Water Resources Research* **51**, 1514–1528. DOI: `10.1002/2014WR016487`, first public 2015-02-09.
3. Chu, S. T. (1978), "Infiltration during an unsteady rain," *Water Resources Research* **14**, 461–466. DOI: `10.1029/WR014i003p00461` (accessible abstract only).
4. Philip, J. R. (1993), "Variable-head ponded infiltration under constant or variable rainfall," *Water Resources Research*. DOI: `10.1029/93WR00748` (accessible abstract only).
