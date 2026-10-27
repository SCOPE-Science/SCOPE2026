# An initial-stock crossover for two-rate logistic fishery schedules

## Finding
Consider a single-species logistic fishery under two fixed proportional-fishing efforts, applied for prescribed positive durations in either order. There is exactly one positive initial-biomass threshold at which the two orders produce equal **cumulative catch**. Below it, low effort followed by high effort catches strictly more; above it, high effort followed by low effort catches strictly more. The threshold is **exactly the unharvested carrying capacity** when the lower effort is zero, and is **strictly above carrying capacity** when both efforts are positive. Meanwhile, high effort first always leaves strictly more terminal biomass, regardless of the initial stock. The cumulative-catch and final-stock orderings are therefore genuinely different.

In particular, below carrying capacity, delaying the high-effort interval strictly increases catch while decreasing terminal stock; at carrying capacity, the catches tie only when the lower effort is zero (otherwise delaying high effort strictly increases catch). This is a finite-horizon, prescribed-effort comparison; it is **not** an unrestricted optimal-control policy or a periodic-equilibrium yield result.

## Assumptions and scope
Let \(r,K>0\) be constant intrinsic growth rate and carrying capacity, \(h>\ell\geq 0\) the two nonnegative fishing-mortality rates, \(u,v>0\) their respective durations, and \(X_0>0\) initial biomass. During each constant-effort interval, biomass solves
\[
\frac{dX}{dt}=rX\left(1-\frac{X}{K}\right)-eX,
\]
with effort \(e=h\) or \(e=\ell\), while cumulative catch increases at rate \(eX\). The alternatives are \(HL\) (rate \(h\) for duration \(u\), followed by \(\ell\) for duration \(v\)) and \(LH\) (rate \(\ell\) for duration \(v\), followed by \(h\) for duration \(u\)). The shared horizon is \(u+v\).

Scale time by \(r\) and biomass by \(K\):
\[
z=\frac{X_0}{K}>0,\quad H=\frac hr,\quad L=\frac\ell r,\quad U=ru,\quad V=rv,\quad d=H-L>0.
\]
For \(a\geq0\) and \(w>0\), write
\[
J_a(w)=\int_0^w e^{(1-a)t}\,dt
=\begin{cases}\frac{e^{(1-a)w}-1}{1-a},&a\ne1,\\w,&a=1.\end{cases}
\]
Define the positive constants
\[
p=J_H(U),\quad q=J_L(V),\quad
m=p+e^{(1-H)U}q,\quad n=q+e^{(1-L)V}p.
\]
For all the stated parameters, there exists a unique \(z_{\mathrm{crit}}>0\) such that, writing \(Y_{HL},Y_{LH}\) for cumulative catch,
\[
\operatorname{sgn}(Y_{HL}-Y_{LH})
=\operatorname{sgn}(z-z_{\mathrm{crit}}).
\]
Moreover,
\[
z_{\mathrm{crit}}=1\quad (L=0),\qquad
z_{\mathrm{crit}}>1\quad (L>0),
\]
and the final biomasses always satisfy \(X_{HL}(u+v)>X_{LH}(u+v)\). Uniqueness is for fixed \(H,L,U,V\); it does not claim the threshold is constant across parameter values when \(L>0\).

## Proof
**1. Exact flow and catch.** In dimensionless time, a constant-effort segment obeys \(x'= (1-a)x-x^2\). Its time-\(w\) map and normalized catch are, for any initial \(x>0\),
\[
\Phi_a^w(x)=\frac{xe^{(1-a)w}}{1+xJ_a(w)},\qquad
\int_0^w a\,\Phi_a^t(x)\,dt=a\log(1+xJ_a(w)).
\]
The second formula follows by differentiating the logarithm of the denominator (and also holds at \(a=1\)). Composing the segments yields
\[
\frac{X_{HL}(u+v)}K=\frac{ze^{(1-H)U+(1-L)V}}{1+mz},\qquad
\frac{X_{LH}(u+v)}K=\frac{ze^{(1-H)U+(1-L)V}}{1+nz}.
\]
Since \(e^{(1-a)w}=1+(1-a)J_a(w)\),
\[
n-m=(H-L)pq=dpq>0.
\]
Consequently the \(HL\) terminal stock is strictly greater, for every \(z>0\).

Adding the catch on both intervals gives the exact cumulative-catch difference
\[
\frac{Y_{HL}-Y_{LH}}K=
 d\log\frac{(1+pz)(1+qz)}{1+nz}
 -L\log\frac{1+nz}{1+mz}
 =d A(z)-L B(z),
\]
where the two displayed logarithms define \(A\) and \(B\). Here \(B(z)>0\) because \(n>m\). Put \(s=1-L\). A direct expansion gives
\[
(1+pz)(1+qz)-(1+nz)=pqz(z-s),
\]
so \(A(z)\) has the sign of \(z-s\).

**2. Uniqueness of the catch crossover.** First suppose \(L>0\). For \(z>\max\{0,s\}\), both \(A(z)\) and \(B(z)\) are positive. Since \(n-m=dpq\), differentiation gives
\[
B'(z)=\frac{dpq}{(1+mz)(1+nz)}>0,
\qquad
\frac{A'(z)}{B'(z)}=
\frac1d\frac{1+mz}{1+pz}
\frac{2z+nz^2-s}{1+qz}.
\]
The first factor \((1+mz)/(1+pz)\) is strictly increasing because \(m-p=e^{(1-H)U}q>0\). The second is nonnegative on \(z>\max\{0,s\}\), with strictly positive derivative proportional to
\[
2+qs+2nz+nqz^2,
\]
which is strictly positive because \(1+qs=e^{(1-L)V}>0\). Thus \(A'/B'\) is strictly increasing on this domain. If \(s\le0\), then \(A(0)=B(0)=0\), so the monotone l'Hôpital argument proves \(A/B\) strictly increasing for \(z>0\). If \(s>0\), then \(A(s)=0<B(s)\), and the same conclusion on \(z>s\) follows by averaging the increasing positive slope \(A'/B'\) against the positive measure \(dB\), with the initial \(B(s)>0\) providing a zero-slope contribution. More explicitly, \(A(z)/B(z)=[B(z)-B(s)]/B(z)\) times \(A(z)/[B(z)-B(s)]\); both factors are strictly increasing and positive.

When \(s\le0\), the limiting quotient at zero is
\[
\lim_{z\downarrow0}\frac{A(z)}{B(z)}=\frac{L-1}{d}<\frac Ld.
\]
When \(s>0\), the quotient starts at zero when \(z=s\), and the catch difference is negative for \(0<z\le s\). In every case, as \(z\to\infty\), \(A(z)=\log z+O(1)\) while \(B(z)\to\log(n/m)>0\). Hence \(A(z)/B(z)\to\infty\). There is therefore exactly one root of \(dA-LB=0\), and its sign is negative below and positive above that root.

For \(L=0\), the catch difference reduces to \(H A(z)\), while \(s=1\). Thus its sign is exactly the sign of \(z-1\), proving the effort- and duration-independent threshold \(z_{\mathrm{crit}}=1\).

**3. Location of the threshold for strictly positive lower effort.** At \(z=1\), put \(C=1+m\), \(D=1+n\) and \(P=pq>0\). Then \((1+p)(1+q)=C+HP\) and \(D=C+dP\). Therefore
\[
\frac{Y_{HL}-Y_{LH}}K
=d\log(C+HP)+L\log C-H\log(C+dP).
\]
Since \(D=C+dP=(d/H)(C+HP)+(L/H)C\), strict concavity of the logarithm makes this expression strictly negative for \(L>0\). Combining with the already proved unique sign crossover yields \(z_{\mathrm{crit}}>1\). This completes all quantified claims.

## Verification
The identities can be independently recomputed using the standalone file `verify_harvest.py` (only Python standard library). It checks the exact two-block formula against separately composed flows and their catch integrals for 2,000 reproducibly generated parameter combinations, plus terminal-stock and threshold signs. These numerical checks corroborate, but do not replace, the analytic proof.

For example, \(r=K=1\), \(h=0.9\), \(\ell=0.1\), and \(u=v=1\) give \(z_{\mathrm{crit}}\approx1.01826439366675\). At initial stock \(z=0.6\), the normalized cumulative catch difference \((Y_{HL}-Y_{LH})/K\approx-0.099326033822\), while the terminal stocks are approximately \(0.602626862894\) for \(HL\) and \(0.462667756112\) for \(LH\). At \(z=2\), the catch difference becomes approximately \(+0.234080994137\) while the \(HL\) terminal stock remains greater.

## Relationship to prior work
The logistic catch-per-unit-effort model is classical; this note does not claim a new population law. Yu, Tang and Lou (2016, article 14), equations (2.2)--(2.6) and Theorem 2.2, derive the closed/open-season logistic flow and study **long-run periodic-stock and maximum annual-sustainable yield** versus closure length. Their fixed-periodic-attractor objective does not determine the finite-horizon cumulative-catch order for every **fixed initial biomass**, and does not state a unique crossover for **two strictly positive efforts** or the exact \(K\)-boundary when one rate vanishes. Their analytic one-rate solution is an important antecedent; the simpler zero-low-rate boundary also follows with additional algebra from the classical formula.

Córdova-Lepe, del Valle and Robledo (arXiv:1110.6413v1, 2011), especially sections 2--4, consider discrete instantaneous catches with subsequent closure durations depending on catch and derive persistence thresholds. Their impulse model and sustainability objective do not imply this continuous two-rate, fixed-duration, finite-horizon catch-order classification. The FAO's Gordon--Schaefer exposition explains the foundational logistic fishery and long-run stock/yield context, not this order-sensitive initial-value theorem.

## Limitations
This theorem is **only** about the deterministic single-stock logistic approximation, two contiguous prescribed effort blocks, proportional catch, constant growth parameters, and undiscounted aggregate catch. It does not establish an optimal schedule among all possible histories, nor extend to age structure, fluctuating recruitment, stock-assessment error, price discounting, multi-stock ecology, or random environmental forcing. In ordinary unstocked logistic recovery, initial stock may not exceed carrying capacity, so the upper-crossing regime may require transient overstocking or changing habitat conditions. The precise root for \(L>0\) is implicit; uniqueness, location and sign are exact. Broader optimal-control and fisheries-scheduling literature may contain an equivalent comparison not recovered by the targeted searches; independent literature review remains important.

## References
1. D. Yu, S. Tang and Y. Lou, *Revisiting logistic population model for assessing periodically harvested closures*, Communications in Mathematical Biology and Neuroscience **2016**, article 14 (public 2016-10-14), https://scik.org/index.php/cmbn/article/download/2419/1442 .
2. F. Córdova-Lepe, R. del Valle and G. Robledo, *A pulse fishery model with closures as function of the catch: Conditions for sustainability*, arXiv:1110.6413v1 (public 2011-10-13), https://arxiv.org/pdf/1110.6413 .
3. FAO, *Bioeconomic Models: The Gordon--Schaefer model*, https://www.fao.org/4/w6914e/w6914e02.htm .
