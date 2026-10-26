# Spectral dominance and delayed sign loss for the L-stable BDFL3 scheme

## Finding

Consider the A-stable, L-stable, second-order four-level formula BDFL3 (also called BDF2OPT(4)) specified in the cited papers. Apply it with a constant positive step to the scalar dissipative equation \(y'=-\lambda y\), where \(\lambda>0\), and write \(s=h\lambda>0\). Its exact recurrence is
\[
 (10+6s)y_{n+3}=15y_{n+2}-6y_{n+1}+y_n,\qquad n\ge0.
\]
A history is a real triple \((y_0,y_1,y_2)\). Say a history is *perpetually positive* when every term of its resulting sequence is strictly positive. Set \(s_*=15/16\).

**Exact spectral and positive-history threshold.** The characteristic polynomial
\[
 P_s(\zeta)=(10+6s)\zeta^3-15\zeta^2+6\zeta-1
\]
has one simple positive real root \(r(s)\) and a nonreal conjugate pair \(z(s),\overline{z(s)}\). Writing \(q(s)=|z(s)|\), one has
\[
 q(s)<r(s)\quad(0<s<s_*),\qquad q(s)=r(s)\quad(s=s_*),\qquad q(s)>r(s)\quad(s>s_*).
\]
For every \(0<s\le s_*\), the set of perpetually positive histories has nonempty interior in the strictly positive octant. For every \(s>s_*\), this set is **exactly** the ray
\[
 \{c(1,r(s),r(s)^2):c>0\}.
\]
More strongly, above \(s_*\) every real history outside the one-dimensional real-root eigenspace has infinitely many positive and infinitely many negative terms, even though all characteristic roots are in the open unit disk. Thus the sharp threshold concerns eventual sign behavior, **not** ordinary linear stability.

**Delayed sign loss with exact positive starting values.** Choose the exact solution for the initial history,
\[
 y_0=1,\qquad y_1=e^{-s},\qquad y_2=e^{-2s}.
\]
At \(s=s_*\), every generated term is strictly positive. For every \(s>s_*\), the generated sequence has infinitely many negative terms. Let \(N_-(s)\) be its first negative index; then
\[
 \boxed{\displaystyle\lim_{s\downarrow s_*}(s-s_*)N_-(s)=\frac{125}{96}\log H_*=4.579428036399280\ldots,}
\]
where, with \(t_*=e^{-15/16}\),
\[
 H_* =\sqrt{\frac{17}{20}}\,
 \frac{\sqrt{(t_*-7/25)^2+51/625}}{2/5-t_*}
 =33.6832517110737\ldots.
\]
Hence a fixed short simulation can appear positive arbitrarily far into the sign-oscillatory regime: immediately above the threshold, the first negative term is delayed on the reciprocal distance-to-threshold scale.

## Assumptions and scope

The step size \(h\) and dissipation rate \(\lambda\) are positive constants. Time stepping uses exact arithmetic, the constant-step BDFL3 coefficients in Table 1 of Jensen--Ketcheson--Lóczi (2026), and the scalar test equation stated above. The positive-history classification ranges over **all real initial triples**; the delayed-first-negative law applies only to the specified exact-solution triple. The polynomial roots are considered as complex algebraic functions of the real parameter \(s\). At \(s=s_*\), equal root *moduli* do not mean coincident roots; all three roots are simple. No norm instability or blow-up is asserted.

## Proof

**1. Derivation, root structure, and the exact crossing.** Substitution of \(f(y)=-\lambda y\) into the published scheme
\[
 y_{n+3}=\frac32 y_{n+2}-\frac35 y_{n+1}+\frac1{10}y_n+\frac35h f(y_{n+3})
\]
gives the displayed recurrence. Direct cubic expansion yields
\[
 \operatorname{disc}_\zeta(P_s)=-108(9s^2-12s+5)
 =-108\bigl(9(s-2/3)^2+1\bigr)<0.
\]
Since \(P_s(0)=-1\) and \(P_s(\zeta)\to+\infty\) as \(\zeta\to+\infty\), there is exactly one simple real root \(r>0\), and the others are nonreal conjugates. Evaluating \(P_s(1)=6s>0\) shows \(0<r<1\). At the unique real root \(\partial_\zeta P_s(r)>0\), hence implicit differentiation gives \(r'(s)<0\).

Vieta's formula gives \(rq^2=(10+6s)^{-1}\). Moreover, \(q^2<1\) is equivalent to \( (10+6s)r>1\), hence by the root equation to \(14r^2-6r+1>0\); the last quadratic has negative discriminant and a positive leading coefficient. Therefore **all three root moduli are strictly below one** for every \(s>0\). Inserting \(P_s(r)=0\),
\[
 (10+6s)r^3=15r^2-6r+1,
 \qquad q>r\ \Longleftrightarrow\ 15r^2-6r+1<1
 \ \Longleftrightarrow\ r<2/5.
\]
A direct substitution yields \(P_{15/16}(2/5)=0\); strict decrease of \(r(s)\) proves the complete three-regime classification. In particular
\[
 P_{s_*}(\zeta)=\frac{125}{8}(\zeta-2/5)
 \bigl(\zeta^2-(14/25)\zeta+4/25\bigr),
\]
so the two nonreal roots at the transition are
\[
 z_*=\frac{7+i\sqrt{51}}{25},\qquad
 \cos\theta_* =\frac{\operatorname{Re}z_*}{|z_*|}=\frac7{10}.
\]

**2. Complete classification of perpetually positive histories.** Since the roots are distinct, every real solution has a *unique* representation
\[
 y_n=c\,r^n+2\operatorname{Re}(d\,z^n),
 \qquad c\in\mathbb R,\ d\in\mathbb C.
\]
The real-linear map from \((c,\operatorname{Re}d,\operatorname{Im}d)\) to \((y_0,y_1,y_2)\) is invertible. If \(q\le r\), every triple with \(c>2|d|\) has
\[
 y_n\ge(c-2|d|)r^n>0\quad\text{for all }n\ge0.
\]
Such triples form an open neighborhood of each positive multiple of \((1,r,r^2)\). Conversely, if \(q>r\) and \(d\ne0\), division by \(q^n\) gives a vanishing real-root contribution plus a nonzero cosine of \(n\arg z+\arg d\). A nonconstant rotation on a circle takes the cosine to a fixed positive value and a fixed negative value infinitely often: for rational rotation angle the finite orbit has zero sum and is not identically zero; for irrational angle this follows from density. Thus the original sequence has both signs infinitely often. If \(d=0\), perpetual positivity requires \(c>0\), giving exactly the stated ray.

**3. Exact starting data and the boundary.** Put \(t=e^{-s}\). Partial-fraction/Lagrange decomposition of the first three geometric values yields
\[
 c(s)=\frac{|t-z|^2}{|r-z|^2}>0,\qquad
 d(s)=\frac{(t-r)(t-\bar z)}{(z-r)(z-\bar z)}.
\]
Therefore \(d(s)=0\) precisely when \(t=r\). To exclude that exception above the threshold, implicit differentiation and the root equation give
\[
 \frac{r'(s)}{r(s)}=-\frac{2r(s)^3}{5r(s)^2-4r(s)+1}.
\]
For \(0<r\le2/5\), the identity
\[
 5r^2-4r+1-2r^3=(1-r)^2(1-2r)>0
\]
implies \((\log(e^{-s}/r))'<0\). Already at \(s=s_*\), \(t_*=e^{-15/16}<2/5=r(s_*)\). Consequently \(t<r\) for all \(s>s_*\), and \(d(s)\ne0\), proving infinitely many sign changes.

For completeness, the strict inequalities \(39/100<t_*<2/5\) follow by bounding the exponential series: the cubic partial sum for \(e^{15/16}\) exceeds \(5/2\), while the cubic sum plus the geometric bound on its positive tail is below \(100/39\). At \(s_*\), the inequality \(c_*>2|d_*|\) is equivalent to \(H_*>1\), where
\[
 H_* =\frac{|\operatorname{Im}z_*|\,|t_*-z_*|}
 {|r_*-z_*|\,|t_*-r_*|}.
\]
Indeed \(|t_*-r_*|<1/100\), \(|t_*-z_*|\ge\sqrt{51}/25\), and \(|r_*-z_*|=\sqrt{60}/25\), giving \(H_*>204/\sqrt{60}>1\). Thus every term is positive at the critical parameter.

**4. Exact near-critical delay.** For \(s>s_*\), define
\[
 \epsilon(s)=\log(q(s)/r(s))>0,
 \quad H(s)=\frac{c(s)}{2|d(s)|}.
\]
The preceding formulas imply \(H(s)\to H_*>1\). Differentiating
\(\log(q/r)=-\frac12\log(10+6s)-\frac32\log r\)
at the critical root gives
\[
 r'(s_*)=-\frac{32}{125},\qquad
 \epsilon(s)=\frac{96}{125}(s-s_*)+o(s-s_*).
\]
For all integer indices satisfying \(n\epsilon(s)<\log H(s)\), the spectral decomposition yields \(y_n>0\). Therefore
\[
 \liminf_{s\downarrow s_*}(s-s_*)N_-(s)
 \ge\frac{125}{96}\log H_*.
\]
To prove the matching upper bound, write \(z=q e^{i\theta(s)}\) and \(d=|d|e^{i\phi(s)}\). Because \(2\cos\theta_*=7/5\) is rational but not an integer, \(\theta_*/\pi\) is irrational: if it were rational, \(2\cos\theta_*\) would be a rational algebraic integer and hence an integer. Irrational rotations visit any fixed open arc around angle \(\pi\) with **bounded waiting time from any phase**; compactness of the circle gives this property uniformly for angles sufficiently close to \(\theta_*\). Hence, for every fixed \(0<\eta<1\), within a bounded number of indices after
\[
 n_\eta(s)=\frac{\log(H(s)/(1-\eta))}{\epsilon(s)}
\]
there is an index with \(\cos(n\theta(s)+\phi(s))<-(1-\eta)\), and at that index \(y_n<0\). After multiplying by \(s-s_*\), the bounded waiting time disappears. Letting \(\eta\downarrow0\) proves the matching \(\limsup\) and the asserted limit.

## Verification

The self-contained `verify.py` uses only the Python standard library. Run `python verify.py`. It checks the exact critical factorization, cubic discriminant at rational test parameters, exact derivative constant, numerical agreement of the spectral formula with the original recurrence, positivity of the exact starter at the threshold, and near-critical first-negative indices. Example computed first-negative indices for \(s-s_*\) equal to \(0.015\), \(0.0075\), \(0.003\), and \(0.001\) are respectively \(301\), \(609\), \(1541\), and \(4567\). These finite checks corroborate, but do not replace, the universal algebraic and dynamical proof above.

## Relationship to prior work

Jensen, Ketcheson, and Lóczi (2026), Section 3 and Table 1, establish the optimized A-stable/L-stable formula and its local error constant. Vatsa, Carpenter, and Lockard (2010) analyze the same BDF2OPT(4) formula's A-stability and its aerodynamic performance. Those are the method's provenance, not discoveries claimed here. This finding instead classifies **which positive initial histories remain positive indefinitely** on scalar decay and computes the sharp eventual spectral transition and asymptotic first-negative index. Classical multistep root theory explains the solution decomposition but does not itself supply the exact threshold and delay constant for these coefficients. A related result on backward-Euler-started BDF2 establishes a different positivity and delay mechanism; it does not imply this three-step criterion.

## Limitations

The positivity cone here depends on the scalar linear decay problem, the fixed-step BDFL3 formula, and exact arithmetic. It does not claim that all positive histories stay positive below the transition (they do not), or that exact exponential starters remain positive for every subcritical parameter; the proven subcritical assertion is the nonempty *open* positive-history set. The asymptotic constant describes the first negative index only just above the transition. A-stability, L-stability, and convergence are not contradicted: oscillatory sequences still decay to zero. No general matrix, nonlinear, adaptive-step, or floating-point positivity claim is made. The result has not been independently audited.

## References

1. T. Jensen, D. I. Ketcheson, and L. Lóczi, *Optimized linear multistep methods for stiff problems*, arXiv:2610.22685v1 (first public release 2026-10-15), especially Sections 3 and 6 and Table 1. https://arxiv.org/abs/2610.22685
2. V. N. Vatsa, M. H. Carpenter, and D. P. Lockard, *Re-evaluation of an Optimized Second Order Backward Difference (BDF2OPT) Scheme for Unsteady Flow Applications*, AIAA Paper 2010-0122; accessible full text, NASA NTRS 20100002944. https://ntrs.nasa.gov/citations/20100002944
3. E. Hairer, S. P. Nørsett, and G. Wanner, *Solving Ordinary Differential Equations I*, Springer (standard root-condition and multistep background).
