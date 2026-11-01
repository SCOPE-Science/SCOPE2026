# Critical-density Gabor phase diagram for shifted cubic-gamma windows

## Finding

Fix \(\lambda>0\) and \(c>0\). Define the unnormalized causal cubic-gamma window
\[
 g_{\lambda,c}(t)=\begin{cases}(t+c)^3e^{-\lambda t},&t\geq0,\\0,&t<0.\end{cases}
\]
On the critical rectangular lattice \(\mathbb Z\times\mathbb Z\), consider \(\{e^{2\pi i mt}g_{\lambda,c}(t-n):m,n\in\mathbb Z\}\). Put \(r=e^{-\lambda}\in(0,1)\) and
\[
 P_r(u)=((1+r)u-r)^3-3r((1+r)u-r)+r^2-r.
\]
Let \(u_+(r)\) be the **largest positive real root** of \(P_r\). It exists uniquely above \((r+\sqrt r)/(1+r)\). Then
\[
 \boxed{\mathcal G(g_{\lambda,c},\mathbb Z^2)\text{ is a Gabor frame}\quad\Longleftrightarrow\quad c>u_+(e^{-\lambda}).}
\]

All zeros of the Zak transform in the open fundamental cell lie on the frequency line \(\omega=1/2\). A second positive candidate zero appears exactly when \(r>r_0=2-\sqrt3\). More precisely:

* If \(0<r<r_0\), the polynomial \(P_r\) has just one positive root \(u_+(r)\in(0,1)\).
* If \(r=r_0\), its nonnegative roots are \(0\) and \(u_+(r)=1\).
* If \(r_0<r<1\), it has exactly two positive roots \(0<u_-(r)<1<u_+(r)\), which satisfy \(u_+(r)-u_-(r)<1\).

For \(r>r_0\), away from boundary equalities, the number of zeros in the open Zak cell rises from one to two and falls to one before becoming zero as \(c\) passes through
\[
 0<c<u_+(r)-1,\quad u_+(r)-1<c<u_-(r),\quad
 u_-(r)<c<u_+(r),\quad c>u_+(r).
\]
At equality parameters a zero may lie on the one-sided boundary rather than in the open cell, but the lower frame bound is still zero whenever \(c\le u_+(r)\).

Write \(A_{\lambda,c}\) for the **optimal squared lower frame bound** when \(c>u_+(r)\), and let
\[
 v_+(r)=(1+r)u_+(r)-r>\sqrt r.
\]
There is \(\varepsilon_r>0\) such that for \(0<\delta<\varepsilon_r\),
\[
 A_{\lambda,u_+(r)+\delta}
 =\frac{P_r(u_+(r)+\delta)^2}{(1+r)^8}
 =\frac{9(v_+(r)^2-r)^2}{(1+r)^6}\delta^2+O_r(\delta^3).
\]
In particular, the loss of frame stability at the critical jump amplitude is exactly quadratic, with a strictly positive explicit coefficient.

## Assumptions and scope

All parameters are real, \(\lambda>0\) and \(c>0\). The window is not normalized, and the time and frequency shifts have unit spacings, with modulation \(e^{2\pi i mt}\). The Zak transform is
\[
 Zg(x,\omega)=\sum_{j\in\mathbb Z}g(x+j)e^{2\pi i j\omega},\qquad 0\le x<1,\ 0\le\omega<1.
\]
The precise value of a window at one isolated point does not change the frame property. We use the continuous one-sided extension of the Zak expression to \(x=1\) when evaluating essential infima. No optimal upper frame bound, general noncritical lattice, or numerical reconstruction algorithm is asserted.

## Proof

**1. The scalar Zak multiplier.** At \(0\le x<1\) put \(u=c+x\) and \(z=r e^{2\pi i\omega}\). Since only nonnegative indices occur,
\[
 Zg_{\lambda,c}(x,\omega)
 =e^{-\lambda x}\sum_{j\ge0}(j+u)^3z^j
 =e^{-\lambda x}F_u(z),
\]
where the absolutely convergent geometric-moment formula is
\[
 F_u(z)=\frac{u^3}{1-z}+\frac{3u^2z}{(1-z)^2}
 +\frac{3uz(1+z)}{(1-z)^3}
 +\frac{z(1+4z+z^2)}{(1-z)^4}.
\]
At critical density the unitary Zak transform maps the frame operator onto multiplication by \(|Zg|^2\). Thus the system is a frame exactly when this multiplier has strictly positive essential minimum. It is always bounded above because \(|z|=r<1\) and \(0\le x\le1\).

**2. No off-axis Zak zeros.** We prove that for every \(u>0\), all zeros of \(F_u\) in \(|z|<1\) are negative real. Let \(w=z/(1-z)\) and \(y=w+1/2\); then
\[
 |z|<1\quad\Longleftrightarrow\quad\operatorname{Re}y>0,
\]
and \(F_u(z)=(1+w)H_u(y)\), with
\[
 H_u(y)=6y^3+(6u-3)y^2
 +(3u^2-3u-\tfrac12)y
 +u^3-\tfrac32u^2+\tfrac14.
\]
For \(0<u<1/2\), the discriminant of this real cubic is \(-12E(u)\), where
\[
 E(u)=18u^4(1-u)(2-u)+18u^3-12u^2-6u-1.
\]
Since \(0<u<1/2\),
\[
 E(u)\le36u^4+18u^3-12u^2-6u-1
 \le6u^2-6u-1<0.
\]
Hence every root of \(H_u\) is real and simple. At \(u=1/2\), the polynomial is \(y(6y^2-5/4)\), so the same reality conclusion holds.

For \(1/2<u<(1+\sqrt3)/2\), the constant term of \(H_u\) is negative, its quadratic coefficient is positive, and its linear coefficient can have either sign. Descartes' sign rule therefore gives **exactly one positive root, counted with multiplicity**. The other two roots are either nonpositive reals or a conjugate pair whose real part is negative, since the sum of all roots equals \(-(6u-3)/6<0\). At \(u=(1+\sqrt3)/2\), the constant term vanishes; the remaining roots have nonpositive real parts. For larger \(u\), all coefficients of \(H_u\) are positive, and the cubic Routh–Hurwitz determinant is
\[
 (6u-3)(3u^2-3u-\tfrac12)
 -6(u^3-\tfrac32u^2+\tfrac14)
 =6u(u-1)(2u-1)>0.
\]
All its roots then have negative real part. Thus any zero of \(F_u\) in the unit disk corresponds to a **real** \(y>0\), hence a real \(z\in(-1,1)\). The series \(F_u(z)>0\) for real \(0<z<1\), so every such zero must be real negative. In particular, on \(|z|=r\), zeros can occur only at \(z=-r\), i.e. \(\omega=1/2\).

**3. The exact root geometry.** Substituting \(z=-r\) gives
\[
 F_u(-r)=\frac{P_r(u)}{(1+r)^4}.
\]
Set \(s=1+r\) and \(v=su-r\). The derivative is
\[
 P_r'(u)=3s(v^2-r).
\]
On \(u>0\), the cubic first decreases and then increases, with its unique positive critical point at \(u_*=(r+\sqrt r)/s<1\). It is negative there, since \(P_r(u_*)=-r(2\sqrt r+1-r)<0\). Moreover
\[
 P_r(0)=-r(1-4r+r^2),\qquad P_r(1)=1-4r+r^2.
\]
The positive sign change of \(1-4r+r^2\) occurs at \(r_0=2-\sqrt3\), which proves the stated root counts, positions and the existence of a unique largest positive root \(u_+>u_*\).

For \(r>r_0\), let \(u_-\in(0,u_*)\) denote the smaller positive root. The generating-function shift identity
\[
 F_{u+1}(z)=\frac{F_u(z)-u^3}{z}
\]
implies \(F_{u_-+1}(-r)=u_-^3/r>0\). Since \(u_-+1>1>u_*\) and \(F_u(-r)\) is strictly increasing for \(u>u_*\), its larger root satisfies \(u_+<u_-+1\). This proves the strict gap bound and ensures the two nonframe parameter intervals overlap.

**4. Frame versus nonframe.** A zero or one-sided limiting zero of the Zak multiplier occurs precisely when \(P_r(u)=0\) for \(u\in[c,c+1]\). If \(r\le r_0\), the only positive root \(u_+\) lies in \((0,1]\); it belongs to \([c,c+1]\) exactly when \(0<c\le u_+\). If \(r>r_0\), the roots are \(u_-<1<u_+<u_-+1\). For \(c\le u_-\) the smaller root lies in \([c,c+1]\); for \(u_-<c\le u_+\), the larger root lies there because \(u_+-1<u_-<c\). For \(c>u_+\), neither root lies in the interval. Compactness of the one-sided Zak cell now proves the frame equivalence, including all boundary equalities.

**5. Sharp quadratic onset.** At \(c=u_+\), the sole zero of the one-sided Zak expression on \([0,1]\times\mathbb T\) is \((x,\omega)=(0,1/2)\). It is simple in the real variable \(u\), since \(P_r'(u_+)=3s(v_+^2-r)>0\), and simple in \(z\) by Step 2 (for \(u<1/2\) the cubic has three distinct real roots; for \(u\ge1/2\), it has only one positive right-half-plane root counted with multiplicity). Because the Zak coefficients are real on the negative real axis, its first-order local form has a nonzero real slope in \(u\) and a nonzero imaginary slope in \(\omega\). Reflection across \(\omega=1/2\) gives a strict local minimum there in the frequency direction for nearby \(x,c\); the positive \(u\)-slope makes \(|Zg(x,1/2)|^2\) strictly increasing from \(x=0\) in a fixed small neighborhood when \(c=u_++\delta\) and \(\delta>0\) is small. Away from the critical point, compactness gives a uniform positive bound. Thus the global essential minimum for sufficiently small \(\delta>0\) occurs at the one-sided boundary \((0,1/2)\), so
\[
 A_{\lambda,u_++\delta}=|Zg_{\lambda,u_++\delta}(0,1/2)|^2
 =P_r(u_++\delta)^2/s^8.
\]
Taylor expansion gives the claimed strictly positive quadratic coefficient.

## Verification

The self-contained standard-library program `checker.py` tests the generating-function identity using exact rational arithmetic, verifies numerical root positions and root ordering at twelve damping parameters, probes thousands of nonzero Zak samples in the stable region, and checks the quadratic coefficient for small positive shifts. Its output is `PASS: 6631 supplementary checks`. Such finite tests are illustrative; the theorem is proved by the preceding analytic argument.

## Relationship to prior work

Faulhuber and Shafkulovska, *Gabor frame bound optimizations* (first public arXiv version 6 April 2022), analyze sharp frame bounds and lattice optimization for ordinary one-sided and two-sided exponentials, hyperbolic secants and cut-off exponentials. The shifted cubic-gamma multiplier and its two-zero transition are different objects and are not implied by their stated theorems. Ghosh and Selvan (22 April 2023) study B-spline, totally positive and Hermite frame regions, mainly below critical density; they do not give this critical shifted-cubic classification. Kloos and Stöckler (28 November 2013) prove strong uniqueness-of-Zak-zero results for totally positive windows; the present positive-shift family can exhibit two zeros and therefore is not covered by that theorem. The general Zak criterion itself is classical, not presented as new.

## Limitations

The statement concerns the critical unit lattice and the fixed cubic causal polynomial window. The number of **distinct interior zeros** must be separated from one-sided endpoint zeros at equality parameters. The paper does not assert stability to perturbations of the window, upper-frame-bound formulas, noncritical frame sets, or uniformity as \(r\) tends to 0 or 1. The historic-priority comparison is limited to the listed inspected literature, available research records and exact-query searches; independent validation is not claimed.

## References

1. M. Faulhuber and I. Shafkulovska, *Gabor frame bound optimizations*, arXiv:2204.02917, first public version 6 April 2022; 2023 updated version, Sections 2.2–2.4 and 3. https://arxiv.org/html/2204.02917v2
2. R. Ghosh and A. Antony Selvan, *On Gabor frames generated by B-splines, totally positive functions, and Hermite functions*, arXiv:2304.11322, first public version 22 April 2023, Sections 1, 3–5. https://arxiv.org/html/2304.11322v1
3. T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359, first public version 28 November 2013, Sections 1 and 3. https://arxiv.org/abs/1311.7359
