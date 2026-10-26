# Sharp correction-sweep flip boundary for two-node positive deferred correction on logistic flow

## Finding

**Theorem (complete correction-sweep phase diagram).** Consider the scalar logistic differential equation
\[
\dot y=y(1-y),\qquad y(0)=a,\qquad 0<a<1,
\]
with exact positive flow \(y(h)=ae^h/(1-a+ae^h)\in(a,1)\). Apply the two-node Gauss–Lobatto exponential deferred-correction scheme with quadrature nodes \(\tau_0=0\), \(\tau_1=1\), endpoint trapezoidal weights \(Q_(1, 0)=Q_(1, 1)=1/2\), and any integer number \(k\ge0\) of endpoint corrections. Its predictor \(x_0\) and sweeps \(x_k\) satisfy
\[
x_0=a e^{h(1-a)},\qquad x_{k+1}=a\exp\left(h\left[1-\frac{a+x_k}2\right]\right).
\]
Define the dimensionless coefficient
\[
c=\frac{ha}2\exp\left(h\left[1-\frac a2\right]\right)>0,
\]
and let \(W_0\) denote the nonnegative real branch of the Lambert \(W\) function. The unique positive collocation endpoint is \(x_*=2W_0(c)/h\). For each \(0<a<1\), the predictor is strictly above \(x_*\). The exhaustive alternatives are:

1. **Subcritical**, \(0<c<e\): every correction sweep converges geometrically to \(x_*\), with asymptotic one-sweep multiplier \(-W_0(c)\).
2. **Critical**, \(c=e\): every correction sweep converges to \(x_*=2/h\), and the *signed* asymptotic rate is
   \[
   \lim_{k\to\infty}(-1)^k\sqrt{k}\left(\frac h2 x_k-1\right)=\sqrt6.
   \]
3. **Supercritical**, \(c>e\): the even and odd correction sequences converge to different positive values \(x_+>x_*>x_-\), respectively. There is exactly one primitive positive two-cycle. Parameterize it by the unique \(d>0\) satisfying
   \[
   c=\frac d{e^d-1}\exp\left(\frac{d e^d}{e^d-1}\right).
   \]
   Then
   \[
   x_-=\frac 2h\frac d{e^d-1},\qquad
   x_+=\frac 2h\frac{d e^d}{e^d-1},\qquad
   \left|\left(F^2\right)'(x_\pm)\right|=
   \left(\frac d{2\sinh(d/2)}\right)^2<1,
   \]
   where \(F(x)=a\exp(h[1-(a+x)/2])\).

For fixed \(a\in(0,1)\), the sharp stepsize at which repeated corrections stop converging is
\[
h_c(a)=\frac{2}{2-a}W_0\left(\frac{e(2-a)}a\right)>2.
\]
The collocation endpoint reaches the carrying capacity \(1\) only at
\[
h_r(a)=\frac{2\log(1/a)}{1-a}>h_c(a).
\]
Consequently the entire open interval \(h_c(a)<h<h_r(a)\) exhibits a stable two-cycle of correction sweeps despite \(0<x_*<1\). Uniformly over all \(0<a<1\), convergence of the infinitely repeated correction sweep holds for every such initial value if and only if \(0<h\le2\).

## Assumptions and scope

All variables are real and all arithmetic is exact. The logistic carrying capacity and intrinsic growth rate have been normalized to one; the physical step \(h\) is any strictly positive real number. The theorem concerns **one** time step, the predictor and any number of successive two-node Gauss–Lobatto corrections, at fixed \(a\) and \(h\). It does not assert analogous behavior for Gauss–Radau nodes, more than two interpolation nodes, negative initial data, or general nonlinear systems. The statement about the infinite-sweep limit is not a claim about the finite correction count conventionally chosen to match quadrature order.

## Proof

**1. Reduction.** The per-capita growth rate is \(f(y)/y=1-y\). At two Gauss–Lobatto nodes, the stage at zero is exactly \(a\), while the endpoint quadrature weights are both \(1/2\). Substitution in the exponential predictor and correction equations gives the displayed recurrence. Set \(b=h/2\), \(u_k=b x_k\), and \(A=a\exp(h[1-a/2])\). Then
\[
u_{k+1}=T(u_k),\qquad T(u)=c e^{-u},\qquad c=bA.
\]
The fixed-point equation \(u e^u=c\) has precisely one positive solution \(w=W_0(c)\). Since \(x_0>a\) and \(F(x_0)/x_0=\exp(h[a-x_0]/2)<1\), a decreasing-map crossing argument yields \(u_0>w\).

**2. Exhaustiveness and global convergence.** The map \(T\) is strictly decreasing and sends positive inputs to \((0,c)\); therefore \(G=T\circ T\) is strictly increasing. Every even subsequence is monotone from its first comparison with \(G(u_0)\) and, after its first update, bounded in \((0,c)\); thus it converges to a fixed point of \(G\). The odd subsequence converges to its \(T\)-image. A nonfixed point of \(G\) belongs to a two-cycle \(v=T(z), z=T(v)\) with \(0<v<z\). Writing \(d=z-v>0\), division of the two cycle equations gives \(z/v=e^d\), hence
\[
v=\frac d{e^d-1},\quad z=\frac{d e^d}{e^d-1},\quad
c=v e^z.
\]
The logarithmic derivative of this last expression is
\[
\frac{d}{\mathrm d d}\log(v e^z)
=\frac{(e^d-1)^2-d^2e^d}{d(e^d-1)^2}>0,
\]
because \(2\sinh(d/2)>d\) for \(d>0\). Its limit is \(1\) as \(d\downarrow0\), and it diverges as \(d\to\infty\). Thus exactly one nontrivial two-cycle exists if and only if \(c>e\). Its two-step multiplier is \(vz=[d/(2\sinh(d/2))]^2<1\). If \(c\le e\), the only fixed point of \(G\) is \(w\), so both subsequences converge to \(w\). If \(c>e\), the fixed point \(w\) is repelling for \(G\), since \(G'(w)=w^2>1\). Because \(u_0>w\), monotonicity of \(G\) and the sign of \(G(u)-u\) immediately above \(w\) prevent convergence to \(w\); the even subsequence must tend to \(z\) and the odd to \(v\). The inequalities \(v<w<z\) follow from the strict decrease of \(T\).

**3. Rates.** At \(0<c<e\), \(0<w<1\) and \(T'(w)=-w\), yielding geometric convergence and its asymptotic multiplier. At \(c=e\), put \(u=1+\delta\). Direct Taylor expansion gives
\[
G(1+\delta)=\exp\left(1-\exp(-\delta)\right)
=1+\delta-\frac{\delta^3}6+O(\delta^4).
\]
Writing \(\delta_n=u_{2n}-1>0\), the global convergence proved above shows \(\delta_n\downarrow0\), while
\[
\delta_{n+1}=\delta_n-\frac{\delta_n^3}6+O(\delta_n^4),\qquad
\delta_{n+1}^{-2}-\delta_n^{-2}=\frac13+O(\delta_n).
\]
Cesàro averaging yields \(n\delta_n^2\to3\). Since \(u_{2n+1}-1=e^{-\delta_n}-1=-\delta_n+O(\delta_n^2)\), the stated alternating \(\sqrt{k}\) limit is \(\sqrt6\).

**4. Sharp stepsizes and the invariant interval.** The function \(c(h,a)=(ha/2)e^{h(1-a/2)}\) increases strictly from zero to infinity as \(h\) increases. Solving \(c=e\) gives the stated \(h_c(a)\). At \(h=2\), \(\log c=\log a+2-a<1\) for \(0<a<1\), by \(\log a<a-1\); hence \(h_c(a)>2\). As \(a\uparrow1\), the threshold tends to \(2\), proving the uniform frontier. The collocation endpoint is \(\le1\) precisely when \(F(1)\le1\), or \(h\le 2\log(1/a)/(1-a)=h_r(a)\), since \(F\) is decreasing and crosses the diagonal uniquely. At \(h=h_r(a)\), \(w=h_r(a)/2>1\) because \(-\log a>1-a\); thus \(c=w e^w>e\) and \(h_r(a)>h_c(a)\). This proves the nonempty two-cycle interval while the collocation endpoint is inside the invariant interval. \(\square\)

## Verification

Run `python3 verify.py` using the Python standard library. The script checks predictor/fixed-point identities, phase boundaries, the exact period-two equations, global sweep limits away from the threshold, a critical-rate approximation, and the nonempty carrying-capacity-safe cycling interval. These finite tests do not replace the all-parameter analytic proof above.

One reproducible interior example is \(a=1/2\), \(h=2.3\), for which \(c\approx3.2271995921>e\), \(x_*\approx0.9457578532<1\), and the limiting correction endpoints are \(x_-\approx0.2478106285\) and \(x_+\approx2.1103854250\). The exact differential equation remains within \((0,1)\) throughout the step.

## Relationship to prior work

Pezzella (2026), arXiv:2606.29523v1, introduces the general positive exponential integral deferred-correction update in Eq. (3), proves positivity of finite sweeps, develops small-step error bounds and studies nonlinear contractivity of collocation methods. The present theorem fixes the minimal two-node Gauss–Lobatto case and asks a different, fixed-step question: does the *actual explicit correction iteration* converge as the number of sweeps increases, and what is the exact threshold and limiting attractor? Positivity alone does not answer this question. Generic fixed-point/Picard stability criteria explain the local derivative, but do not themselves state the method-specific sharp stepsize, the global cycle classification, or the interval in which collocation is physically bounded while the explicit corrections cycle.

Other positive deferred-correction work concerns different flux or quadrature constructions; results for one correction on conservative exchange systems do not imply this logistic infinite-sweep classification. Equivalent specialized analyses may nevertheless exist outside the inspected literature.

## Limitations

Only a normalized scalar logistic field, a fixed initial value, and one two-node Gauss–Lobatto time step are treated. The theorem concerns increasing the number of sweeps *without reducing the step*, not the convergence of a time-marching method as \(h\to0\). The exact positive orbit and the collocation endpoint need not coincide. Higher-node schemes, more general systems, floating-point overflow, adaptive stopping, and roundoff are not classified. A prior-art search cannot prove historical uniqueness; independent mathematical and priority assessments have not been performed.

## References

- Mario Pezzella, *Stable Positive Integral Deferred Correction Methods for Positive Dynamical Systems*, arXiv:2606.29523v1 (first publicly posted 2026-06-28), especially Eq. (3), Sections 2, 4, 5.2. https://arxiv.org/abs/2606.29523
- Lorenzo Micalizzi and Davide Torlo, *New Efficient Implicit-Explicit Deferred Correction methods*, arXiv:2608.23919 (2026). Distinct additive/IMEX correction framework. https://arxiv.org/abs/2608.23919
