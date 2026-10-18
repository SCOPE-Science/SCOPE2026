# A universal logarithmic horizon penalty under disk-valued reachability uncertainty

## Finding
Fix a constant \(0<r<(1+\sqrt{2})^{-1}\). In the three-state reachability model below, let \(H_t\) be the best success probability by time \(t\) among **time-homogeneous** kernels, and let \(D_t\) be the best success probability by time \(t\) among **time-dependent** admissible Markov controls. For integers \(t\to\infty\),
\[
1-H_t=\frac{\log(2rt)+1+o(1)}{2rt},\qquad
1-D_t\sim\frac{2}{rt},\qquad
\frac{1-H_t}{1-D_t}\sim\frac{\log t}{4}.
\]
This separates the two finite-horizon deficits by a diverging logarithmic factor, despite their common infinite-horizon supremum of one. The exact adaptive deficit recursion is
\[
e_0=1,\quad e_t=1-D_t,\quad
e_{t+1}=e_t-r\frac{e_t^2}{\sqrt{e_t^2+(1-e_t)^2}+1-e_t}.
\]
For every fixed homogeneous kernel, the unconditional expected success-hitting time is infinite, including the kernel that never leaves the initial state.

## Assumptions and scope
The state space is \(\{x,s,f\}\), where \(x\) is active and \(s\) (success) and \(f\) (failure) are absorbing. The initial state is \(x\). The row from \(x\) is
\[
P_{a,b}(x,\cdot)=(1-a-b,a,b),\qquad
K_r=\{(a,b):a\ge0,\ a^2+(b-r)^2\le r^2\}.
\]
The disk lies in \(b\ge0\), and \(a+b\le r(1+\sqrt2)<1\). Thus every specified row is stochastic. The set of complete matrices is compact, convex, and has separately specified rows (the remaining two rows are fixed).

Write \(\tau_s=\inf\{n\ge0:X_n=s\}\), with \(\inf\varnothing=+\infty\). For each integer \(t\ge0\), \(H_t\) is the maximum of \(\Pr_{P_{a,b}}(\tau_s\le t\mid X_0=x)\) over one matrix \(P_{a,b}\) held fixed at all times. The quantity \(D_t\) is the supremum over all admissible, possibly history-dependent policies selecting rows in \(K_r\) on each visit to \(x\) at each time. The optimizing policy may depend on the prescribed horizon \(t\). Both maxima are attained for each finite \(t\), but this does not assert a single policy optimizing every horizon.

## Proof
**1. Homogeneous reduction.** For \(a+b>0\), the probability of success by time \(t\) is
\[
p_t(a,b)=a\sum_{j=0}^{t-1}(1-a-b)^j
=\frac{a}{a+b}\left(1-(1-a-b)^t\right).
\]
At \((a,b)=(0,0)\), it is zero. For fixed \(a\), each summand in the displayed sum is nonincreasing in \(b\). Consequently the best admissible \(b\) is the lower disk boundary
\[
\beta(a)=r-\sqrt{r^2-a^2}
=\frac{a^2}{r+\sqrt{r^2-a^2}},\qquad 0\le a\le r.
\]
Define \(g_t(0)=1\) and, for \(a>0\),
\[
g_t(a)=\frac{\beta(a)}{a+\beta(a)}+
\frac{a}{a+\beta(a)}(1-a-\beta(a))^t.
\]
Continuity at zero is immediate from the geometric sum, and \(1-H_t=\min_{0\le a\le r}g_t(a)\).

**2. Sharp stationary asymptotics.** Put \(c=(2r)^{-1}\). As \(a\downarrow0\),
\[
\beta(a)=ca^2+O(a^4),\qquad
\frac{\beta(a)}{a+\beta(a)}=ca+O(a^2).
\]
Set \(a_*=\log(t/c)/t\), which belongs to \((0,r)\) for all sufficiently large \(t\). Substitution yields \(g_t(a_*)=O(\log t/t)\); this proves an upper bound for the minimum.

Let \(a_t\) minimize \(g_t\). The first nonnegative term in \(g_t\) is bounded away from zero on any closed interval \([\delta,r]\), so the upper bound forces \(a_t\to0\). Near zero it is bounded below by a positive constant times \(a\), and therefore \(a_t=O(\log t/t)\). If \(t a_t\le\tfrac12\log t\), the elementary inequality \(\log(1-z)\ge-z/(1-z)\) for \(0\le z<1\), applied to \(z=a_t+\beta(a_t)\), makes the second term of \(g_t(a_t)\) at least \(t^{-1/2-o(1)}\), contradicting \(O(\log t/t)\). Thus the minimizer lies, for sufficiently large \(t\), in
\[
\tfrac12\log t\le t a_t\le C\log t
\]
for some finite \(C\) depending only on \(r\).

Throughout this interval, with \(u=ta\), uniformly
\[
g_t(u/t)=\frac{cu}{t}+e^{-u}+o(t^{-1}).
\]
Indeed, the rational boundary error is \(O((\log t)^2/t^2)\), while the exponential correction is at most \(O(t^{-1/2}(\log t)^2/t)=o(t^{-1})\). The comparison function \(cu/t+e^{-u}\) has its unique global minimum at \(u=\log(t/c)=\log(2rt)\), with value \(c[\log(t/c)+1]/t\). The trial point lies in the same interval for large \(t\), so minimizing the uniform approximation proves
\[
1-H_t=\frac{\log(2rt)+1+o(1)}{2rt}.
\]

**3. Exact finite-horizon adaptive recursion.** Let \(D_0=0\) and \(e_t=1-D_t\). At the first step, the state moves to success with probability \(a\), failure with probability \(b\), and otherwise remains active, where it can use the optimal remaining-horizon policy. Bellman's principle gives
\[
D_{t+1}=D_t+\max_{(a,b)\in K_r}\{a e_t-b(1-e_t)\}.
\]
For \(0<e_t\le1\), the support of the disk in this direction lies on its \(a\ge0\) half, and its value is
\[
r\left(\sqrt{e_t^2+(1-e_t)^2}-(1-e_t)\right).
\]
Rationalizing the square-root difference proves the stated exact recursion. An optimal action when \(m\ge1\) steps remain is explicitly
\[
a_m=\frac{r e_{m-1}}{\sqrt{e_{m-1}^2+(1-e_{m-1})^2}},\quad
b_m=r\left(1-\frac{1-e_{m-1}}{\sqrt{e_{m-1}^2+(1-e_{m-1})^2}}\right).
\]
Since the support gain is positive for \(e_t>0\), \((e_t)\) strictly decreases. Since every gain is at most \(r e_t\), the sequence stays positive. Its limit must be zero: a positive limit would imply a positive limiting decrement. With
\[
d_t=\sqrt{e_t^2+(1-e_t)^2}+1-e_t\to2,
\]
the exact difference of reciprocals satisfies
\[
\frac1{e_{t+1}}-\frac1{e_t}
=\frac{r}{d_t(1-r e_t/d_t)}\longrightarrow\frac r2.
\]
Summing these increments and dividing by \(t\) gives \(1/(t e_t)\to r/2\), hence
\[
1-D_t=e_t\sim\frac{2}{rt}.
\]
Combining the two asymptotics proves \((1-H_t)/(1-D_t)\sim (\log t)/4\).

**4. Infinite-horizon nonattainment.** The only disk point with \(b=0\) is \((a,b)=(0,0)\). If \(a>0\), then \(b>0\), the chance of ever reaching \(s\) equals \(a/(a+b)<1\), and \(\Pr(\tau_s=+\infty)>0\); consequently \(\mathbb E\tau_s=+\infty\). If \(a=0\), success is unreachable and the expectation is again infinite. But with \(b=\beta(a)\), \(\beta(a)/a\to0\) as \(a\downarrow0\), so \(\sup_{K_r}\Pr(\tau_s<\infty)=1\), without an attaining homogeneous matrix.

## Verification
The standalone Python 3 standard-library script `verify.py` checks the homogeneous geometric-sum identity by direct finite-state propagation at several horizons, checks the adaptive support-function recurrence against independent angular-grid optimization, and numerically evaluates horizon deficits through \(t=100000\) for \(r=1/4\). Its sample output includes \(t(1-H_t)-2\log(t/2)=1.931626332\) at \(t=10000\) and \(1.989037862\) at \(t=100000\), approaching the proved constant \(2\), and \(t(1-D_t)=7.944746314\) and \(7.992789271\), approaching \(8\). These finite computations test, but do not prove, the infinite-horizon asymptotics.

## Relationship to prior work
Sangalli, Quaeghebeur, and Krak (2026, Example 1) exhibit a different compact convex three-state uncertainty family whose upper eventual hitting probability is one but whose lower unconditional hitting time is infinite. Their example uses the points with success and failure probabilities \((1/n,1/n^2)\), and establishes **nonattainment**, not a finite-horizon stationary-versus-adaptive rate comparison. The present disk has smooth quadratic contact with the zero-failure axis; the exact horizon tradeoff and its universal logarithmic ratio are additional conclusions.

Krak, T'Joens, and De Bock (2019) establish general fixed-point characterizations and equivalence of **eventual** upper/lower hitting probabilities across several process semantics. Their Bellman-operator framework motivates the present recursion but does not state the disk support function, its inverse-deficit asymptotics, or the sharp optimized homogeneous boundary layer. Sangalli and colleagues' paper on computing hitting probabilities (arXiv:2512.16696) develops eventual-hitting iterative algorithms rather than this comparison. De Bock, Erreygers, and Persiau (2026) analyze qualitative convergence of upper transition operators using a related quadratic transition family; their illustrative network and theorem do not provide the logarithmic finite-horizon penalty here. Ashkenazi-Golan and coauthors (2020) study long finite-horizon overtaking optimality under a **finite action set**; the disk here offers uncountably many actions and nonattainment of eventual optimum.

## Limitations
The theorem applies to a specific three-state compact disk family for each fixed radius in the stated range; it does not establish a universal logarithmic law for every convex uncertainty set, nor any claim about a single policy that is optimal simultaneously for all horizons. The asymptotic \(o(1)\) terms are not supplied with a uniform error bound in the radius. The literature comparison does not rule out all unpublished, unindexed, or differently formulated prior results.

## References
1. M. Sangalli, E. Quaeghebeur, T. Krak, *Relation between Hitting Times and Probabilities for Imprecise Markov Chains*, arXiv:2603.16675v1 (first public 17 March 2026), https://arxiv.org/html/2603.16675v1 .
2. T. Krak, N. T'Joens, J. De Bock, *Hitting Times and Probabilities for Imprecise Markov Chains*, Proceedings of Machine Learning Research 103 (2019), 265–275, https://proceedings.mlr.press/v103/krak19a.html .
3. M. Sangalli, R. Reubsaet, E. Quaeghebeur, T. Krak, *Computing Lower and Upper Hitting Probabilities for Imprecise Markov Chains*, arXiv:2512.16696v2 (2026 revision), https://arxiv.org/html/2512.16696 .
4. J. De Bock, A. Erreygers, F. Persiau, *Characterising the Convergence of Imprecise Markov Chains*, PMLR 337 (2026), 620–639, https://proceedings.mlr.press/v337/de-bock26a.html .
5. G. Ashkenazi-Golan, J. Flesch, A. Predtetchinski, E. Solan, *Reachability and Safety Objectives in Markov Decision Processes on Long but Finite Horizons*, J. Optim. Theory Appl. 185 (2020), 945–965, https://arxiv.org/abs/1911.05578 .
