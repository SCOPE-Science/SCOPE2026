# Sharp cancellation frontier for second-order real-shift exponential resolvents

## Finding
For a real-shift rational approximation of the exponential, the requirements of local second-order accuracy and real poles in a prescribed compact interval impose a **sharp, unavoidable cancellation cost**. The complete optimum has a two- versus three-shift phase transition and is attained by an explicitly specified signed quadrature rule.

Let \(0<a<b\), \(t\in[a,b]\), and consider any finite signed Borel measure \(\mu\) on \([a,b]\). Impose the moments
\[
\int_{a}^{b}1\,d\mu=1,\qquad
\int_{a}^{b}s\,d\mu=t,\qquad
\int_{a}^{b}s^2\,d\mu=\frac{t^2}{2}.
\]
The negative mass \(\lambda=\mu^-([a,b])\) satisfies \(\|\mu\|_{\mathrm{TV}}=1+2\lambda\). Define
\[
c=\frac{a+b}{2},\qquad h=\frac{b-a}{2},\qquad d=t-c,\qquad \delta=\frac{t^2}{2}.
\]
The sharp optimum is
\[
\boxed{
\lambda_*(a,b,t)=
\begin{cases}
\dfrac{\delta}{(h+|d|)^2-\delta},&\delta\le d^2+|d|h,\\[7pt]
\dfrac{\delta-d^2}{h^2},&\delta\ge d^2+|d|h.
\end{cases}}
\]
Both branches agree at their common boundary. The optimal measure has two atoms in the strict first regime and three atoms in the strict second regime, and is unique as a signed measure. These statements include endpoint times \(t=a,b\). The exact minimum coefficient total variation is \(\boxed{1+2\lambda_*}\).

For the symmetric shift window \([t-h,t+h]\), with \(0<h<t\), the optimum reduces to the particularly transparent law
\[
\boxed{\|\mu\|_{\mathrm{TV,min}}=1+\frac{t^2}{h^2}}.
\]
This is a sharp quadratic growth in inverse relative shift bandwidth, independent of the number of resolvent terms.

## Assumptions and scope
A real simple-pole resolvent sum has the form
\[
R_t(z)=\sum_{j=1}^{n}\frac{w_j}{1+s_jz},\quad
s_j\in[a,b],\quad w_j\in\mathbb R.
\]
Repeated nodes can be combined; alternatively allow any finite signed measure \(\mu\) and write \(R_t(z)=\int(1+sz)^{-1}\,d\mu(s)\). Because \(a>0\), every pole \(-1/s\) is real and strictly negative. The expansion at zero is
\[
R_t(z)=\int 1\,d\mu-z\int s\,d\mu+z^2\int s^2\,d\mu+O(z^3),
\qquad e^{-tz}=1-tz+\frac{t^2z^2}{2}+O(z^3).
\]
Thus the three moments above are precisely **local order two**. This is not a claim of uniform approximation for \(z\ge0\), nor a guarantee that any individual prescribed set of shift nodes admits the optimum. We optimize the locations within \([a,b]\), as well as the real signed weights. Normalization is exactly \(R_t(0)=1\), and total variation measures absolute coefficient mass after identical poles are combined.

## Proof
**1. Elementary dual lower bound.** A real quadratic \(q(s)\) with \(|q(s)|\le1\) for every \(s\in[a,b]\) gives, for every feasible signed measure,
\[
\|\mu\|_{\mathrm{TV}}\ge \int q\,d\mu.
\]
The integral on the right depends only on the three fixed moments. A dual polynomial that achieves equality with a feasible signed atomic measure proves global optimality even among arbitrary signed measures, not just a fixed number of atoms.

**2. Interior three-shift phase.** Suppose \(\delta\ge d^2+|d|h\), and set
\[
\lambda=\frac{\delta-d^2}{h^2},\qquad
\mu=-\frac{\lambda+d/h}{2}\,\delta_a
 +(1+\lambda)\,\delta_c
 -\frac{\lambda-d/h}{2}\,\delta_b.
\]
Here \(\delta_s\) denotes unit mass at \(s\), not the scalar \(\delta=t^2/2\). The phase inequality implies \(\lambda\ge |d|/h\), so both endpoint coefficients are nonpositive. Direct substitution yields total mass one, first moment \(t\), and second moment
\[
\int s^2\,d\mu=(c+d)^2-(d^2+\lambda h^2)=t^2-\delta=\delta.
\]
The quadratic
\[
q(s)=1-2\left(\frac{s-c}{h}\right)^2
\]
lies in \([-1,1]\) on \([a,b]\) and equals \(-1\) at each endpoint and \(+1\) at the midpoint. Hence
\[
\int q\,d\mu=1+2\lambda=\|\mu\|_{\mathrm{TV}},
\]
so \(\lambda\) is the sharp minimum. Equality in the dual bound confines positive mass to \(c\) and negative mass to \(a,b\), forcing precisely the stated weights by the moment equations.

**3. Exterior two-shift phase.** Suppose \(\delta\le d^2+|d|h\), set \(D=h+|d|\), and put
\[
\lambda=\frac{\delta}{D^2-\delta},\qquad
v=\begin{cases}a,&d\ge0,\\b,&d<0,\end{cases}
\qquad
u=\frac{t+\lambda v}{1+\lambda}.
\]
The denominator is positive because \(\delta\le d^2+|d|h<D^2\). Also the phase condition is equivalent to \(\lambda\le |d|/h\), which implies \(u\ge c\) if \(d\ge0\) or \(u\le c\) if \(d<0\). Thus the distance \(\rho=|u-v|\) is at least \(\max\{u-a,b-u\}\).

Take \(\mu=(1+\lambda)\delta_u-\lambda\delta_v\). Its first moment is \(t\), and its second moment is
\[
(1+\lambda)u^2-\lambda v^2
=t^2-\frac{\lambda}{1+\lambda}(t-v)^2
=t^2-\delta=\delta,
\]
using \(|t-v|=D\). The dual quadratic
\[
q(s)=1-2\left(\frac{s-u}{u-v}\right)^2
\]
is bounded by one in absolute value throughout \([a,b]\), equals \(+1\) at \(u\) and \(-1\) at \(v\), and has integral \(1+2\lambda\). This proves sharpness. The points where \(q=\pm1\), together with the moments, give uniqueness. The two descriptions agree on the separating curve, where one of the three-shift endpoint masses is zero.

**4. Symmetric specialization and sharp conditioning law.** For \(a=t-h\), \(b=t+h\), \(c=t\), and \(d=0\), the interior phase applies and \(\lambda=t^2/(2h^2)\). Hence the three weights at \(t-h,t,t+h\) are
\[
\left(-\frac{t^2}{4h^2},\quad1+\frac{t^2}{2h^2},\quad-\frac{t^2}{4h^2}\right),
\]
with total variation \(1+t^2/h^2\). No increase in number of shifts can reduce this exact lower bound.

## Verification
The companion standalone Python file `check_residue_tradeoff.py` uses only the standard library and exact rational arithmetic. It reconstructs both branch extremizers and verifies all three moment constraints, coefficient signs, shift-range membership, the dual polynomial bound, and equality between the dual objective and total variation. A fixed-seed randomized rational sweep plus a separate edge sweep passed **2,560 tests** (504 two-shift cases and 2,056 three-shift cases). The symmetric instance \((a,b,t)=(4/5,6/5,1)\) yields \(\lambda=25/2\), weights \((-25/4,27/2,-25/4)\) and total variation \(26\). These finite tests support reproducibility; the dual construction above is the proof for all real parameters and all finite signed measures.

For a positive semidefinite matrix with a zero eigenmode, each resolvent term contributes \(w_j\) times that mode. Thus the absolute coefficient sum is its sharp termwise worst-case relative perturbation amplification at that mode, not an unconditional realized floating-point error. In the usual partial-fraction normalization \(\alpha_j/(z-\sigma_j)\), the change of variables is \(\sigma_j=-1/s_j\) and \(\alpha_j=w_j/s_j\).

## Relationship to prior work
Güttel and Shao (2026), particularly the real-pole shared-denominator representation in Section 1, the numerical stability discussion in Section 4, and the residue-growth discussion in Section 4.4, motivate the cancellation problem. Their Theorem 4.2 bounds the *upper* effect of residue roundoff by the sum of residue magnitudes weighted by shifted-solve norms. The inspected theorem statements and related sections do not provide a *sharp lower bound* on coefficient cancellation under exact local order-two matching and a fixed real-shift interval. The present theorem addresses that different constrained extremal problem; it does not claim to improve their global uniform approximation error or Cauchy-matrix conditioning theory.

Güttel and Shao (2025) treat repeated real poles and asymptotic global approximation, rather than simple resolvents with a bounded reciprocal-shift interval and a prescribed second Taylor jet. Yu and Townsend (2022) study a bound on the absolute sum of trigonometric quadrature weights on perturbed grids, not the optimal signed quadratic moment representation here. General signed-measure moment duality and elementary polynomial moment bounds are prior mathematical tools; the proposed contribution is the exact two-phase numerical-resolvent cancellation optimum and its sharp clustered-pole scaling.

## Limitations
The theorem concerns real coefficients, nonzero simple resolvents, freely chosen reciprocal shifts in a fixed positive interval, and the three local Taylor moment constraints. It does **not** establish uniform-in-time or uniform-in-spectrum approximation quality, nor a lower bound on actual observed rounding error when cancellation happens to be exact or correlated. Allowing polynomial terms, complex poles, higher-order repeated poles, or nonlocal approximation criteria changes the admissible class. Earlier general signed-moment or interpolation duality literature may contain equivalent formulations; priority remains conditional pending independent literature review. No independent audit has been performed.

## References
1. S. Güttel and S. Shao, *Uniform-in-time rational approximation of the matrix exponential with real poles*, arXiv:2607.18018, first public 2026-07-20, https://arxiv.org/abs/2607.18018.
2. S. Güttel and S. Shao, *Concentrated real-pole uniform-in-time approximation of the matrix exponential*, arXiv:2511.21858, first public 2025-11-26, https://arxiv.org/abs/2511.21858.
3. A. Yu and A. Townsend, *On the stability of unevenly spaced samples for interpolation and quadrature*, arXiv:2202.04722, first public 2022-02-09, https://arxiv.org/abs/2202.04722.
4. S. Güttel, *Rational Krylov approximation of matrix functions: numerical methods and optimal pole selection*, GAMM-Mitteilungen 36 (2013), https://doi.org/10.1002/gamm.201310002.
