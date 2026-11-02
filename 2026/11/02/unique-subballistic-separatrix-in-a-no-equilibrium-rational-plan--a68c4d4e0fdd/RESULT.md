# Unique subballistic separatrix in a no-equilibrium rational planar map

## Finding

Consider the rational planar map
\[
(x,y)\longmapsto\left(x+\frac{ax}{1+y^2},\ y+cx+d\right),
\qquad a,c,d>0.
\]
For each fixed initial height \(y_0\ge0\), there is **exactly one** negative initial coordinate \(x_*(y_0)\in(-d/c,0)\) for which the orbit escapes upward at a subballistic rate. Write
\[
A=\left(\frac{9ad}{2}\right)^{1/3}.
\]
The unique critical orbit satisfies
\[
y_n\sim A n^{2/3},\qquad
x_n=-\frac dc+\frac{2A}{3c}n^{-1/3}+o(n^{-1/3}).
\]
For \(x_*(y_0)<x_0<0\), the orbit escapes upward with finite strictly positive velocity \(\lim y_n/n>0\). For \(x_0<x_*(y_0)\), it escapes downward with finite strictly negative velocity \(\lim y_n/n<0\). No orbit from this negative-initial-coordinate slice is bounded. The orbit at \(x_0=x_*(y_0)\) is the exact boundary between these two escape regimes.

## Assumptions and scope

Parameters satisfy \(a,c,d>0\). The statement classifies all \(x_0<0\) at any fixed \(y_0\ge0\); no assertion is made for \(x_0\ge0\), \(y_0<0\), or arbitrary nonzero horizontal forcing. Write \(u_n=-cx_n/d>0\). The dynamics becomes
\[
u_{n+1}=u_n\left(1+\frac{a}{1+y_n^2}\right),\qquad
y_{n+1}=y_n+d(1-u_n).
\]
All limits are as the discrete time \(n\to\infty\). The critical initial value is characterized uniquely by the stated dynamical property; no closed elementary expression for it is asserted.

## Proof

**1. The two ballistic classes.** Every \(u_n\) is strictly increasing. If some \(u_m\ge1\), the next iterate satisfies \(u_{m+1}>1\); subsequently \(y_n\) decreases at a fixed positive minimum rate, so \(y_n\to-\infty\) at least linearly. Hence \(\sum_n(1+y_n^2)^{-1}<\infty\), and the multiplicative recurrence gives a finite limit \(U=\lim u_n>1\). The Cesàro theorem applied to the height increments yields \(y_n/n\to d(1-U)<0\).

If \(u_n<1\) for every \(n\), then \(y_n\) increases and \(u_n\) has a limit \(U\le1\). The height cannot remain bounded: otherwise the multiplier in the recurrence for \(u_n\) stays uniformly larger than one. Thus \(y_n\to+\infty\). If \(U<1\), Cesàro gives \(y_n/n\to d(1-U)>0\). The remaining possibility \(U=1\) is critical.

**2. Exactly one critical initial value.** A strictly ballistic-upward orbit exists for sufficiently small \(u_0>0\). Indeed, until \(u\) reaches \(1/2\), one has \(y_n\ge y_0+dn/2\); consequently
\[
\log\frac{u_n}{u_0}\le
\sum_{j\ge0}\log\left(1+\frac{a}{1+(y_0+dj/2)^2}\right)<\infty.
\]
Small enough \(u_0\) makes crossing \(1/2\) impossible. Conversely every \(u_0\ge1\) lies in the downward class.

Both ballistic classes are open in initial \(u_0\). Downward escape is witnessed by a finite strict crossing of \(1\). For upward escape, take a sufficiently late state with \(u_N\le1-3\eta\) and \(y_N\) large. Nearby states have \(u_N\le1-2\eta\); as long as \(u\le1-\eta\), their heights increase by at least \(d\eta\), so the remaining logarithmic multiplier is bounded by a tail \(\sum_{j\ge0}a/[1+(y_N+d\eta j)^2]\), made small enough to preclude reaching \(1-\eta\). Thus the upward class is open. Connectedness of \((0,\infty)\) implies existence of a critical initial \(u_0\in(0,1)\).

It is unique. Suppose \(0<u_0<v_0<1\) both generated critical orbits, so their heights stay nonnegative. By induction \(u_n(v_0)>u_n(u_0)\) and \(y_n(v_0)<y_n(u_0)\). Because \(y\mapsto 1+a/(1+y^2)\) decreases on \([0,\infty)\), the ratio \(u_n(v_0)/u_n(u_0)\) is nondecreasing and always at least \(v_0/u_0>1\). It cannot tend to one, contrary to both critical limits being one. The same comparison implies every initial \(u_0\) smaller than the critical value is upward-ballistic and every larger value downward-ballistic. Reversing \(u_0=-cx_0/d\) gives the asserted ordering of \(x_0\).

**3. Sharp critical power laws.** On the critical orbit let \(w_n=1-u_n\), so \(w_n\downarrow0\), \(y_n\uparrow\infty\), and
\[
w_{n+1}=w_n-\frac{a(1-w_n)}{1+y_n^2},\qquad
y_{n+1}=y_n+dw_n.
\]
Telescoping the first equation gives
\[
w_n=\sum_{j\ge n}\frac{a u_j}{1+y_j^2}.
\]
Since \(u_j\ge u_n\to1\) and \(y_j\le y_n+d(j-n)\), comparison with an integral gives \(w_n\ge C/y_n\) for all sufficiently large \(n\), for some \(C>0\). In particular \(w_n y_n^2\to\infty\).

An exact difference quotient is
\[
\frac{w_n^2-w_{n+1}^2}{y_n^{-1}-y_{n+1}^{-1}}
=\left(\frac{2a u_n w_n}{1+y_n^2}
-\frac{a^2u_n^2}{(1+y_n^2)^2}\right)
\frac{y_n(y_n+dw_n)}{dw_n}
\longrightarrow\frac{2a}{d}.
\]
Both numerator and denominator telescope to zero, so their tail-sum ratio has the same limit. Thus \(w_n^2y_n\to2a/d\). Finally,
\[
y_{n+1}^{3/2}-y_n^{3/2}
\longrightarrow\frac32\sqrt{2ad},
\]
and Cesàro summation yields \(y_n\sim(9ad/2)^{1/3}n^{2/3}\). Substituting into \(w_n\sim\sqrt{2a/(dy_n)}\) gives \(w_n\sim2A/(3d)n^{-1/3}\) and the stated expansion for \(x_n\). All arguments apply to every admissible \(a,c,d,y_0\).

## Verification

The standalone script `verify.py` checks the coordinate conjugacy through twelve iterates using exact rational arithmetic, witnesses both escape regimes, and performs finite-horizon critical shooting for three horizons. Critical shooting imposes the analytically derived approximate terminal condition \(w^2y=2a/d\); it is numerical corroboration, not existence proof. The theorem, its uniqueness, and its asymptotic constants follow from the preceding argument rather than these finite tests.

## Relationship to prior work

Zhang, Liu, Wei, Jiang and Bi introduced the four-parameter rational map and examined parameter regions with no fixed points and hidden attractors, predominantly numerically. The present positive-feedback, zero-horizontal-forcing, positive-vertical-drift slice has no equilibria and instead exhibits a rigorous global two-basin separation, a unique nonballistic boundary orbit, and an exact \(2/3\)-power law. The simpler zero-vertical-drift regime \(d=0\) cannot exhibit the same cancellation and its ballistic escape analysis does not imply the present positive-drift result. Broad studies of rational maps and their attractors do not by themselves establish the stated unique separatrix or rate.

## Limitations

This is a theorem for one natural parameter sign sector and a fixed nonnegative initial height, not a classification of the entire four-parameter map. The initial critical coordinate is implicitly, rather than elementarily, specified. The exponent and coefficient describe \(n\to\infty\), not finite-time uniformity near the separatrix. Equivalent analyses in unindexed literature are not ruled out; independent mathematical audit has not been conducted.

## References

1. L.-P. Zhang, Y. Liu, Z.-C. Wei, H.-B. Jiang, Q.-S. Bi, *A class of two-dimensional rational maps with self-excited and hidden attractors*, Chinese Physics B **31** (2022), 030503, DOI: 10.1088/1674-1056/ac4025. Accepted manuscript publicly available 2021-12-05. https://cpb.cpsjournals.org/EN/10.1088/1674-1056/ac4025
