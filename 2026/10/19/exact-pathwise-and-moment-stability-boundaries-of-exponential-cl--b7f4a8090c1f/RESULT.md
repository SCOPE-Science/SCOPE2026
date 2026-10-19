# Exact pathwise and moment stability boundaries of exponential-clock Euler

## Finding

For the exponential-random-timestep forward Euler approximation of the stable scalar ordinary differential equation \(\dot u=-a u\), \(a>0\), put \(\xi=ah\), where \(h\) is the mean random timestep. There is a **unique sharp pathwise stability threshold**
\[
\xi_{\mathrm c}=\frac{1}{z_{\mathrm c}}=2.6845103508207076525023826404\ldots,
\qquad \operatorname{Ei}(z_{\mathrm c})=0,\ z_{\mathrm c}>0.
\]
At all \(0<\xi<\xi_{\mathrm c}\), the entire piecewise-linear random Euler trajectory decays exponentially almost surely, despite exponentially *growing signed mean* once \(\xi>2\), and despite exponentially *growing second moment* already at \(\xi>1\). For \(\xi>\xi_{\mathrm c}\), the jump-chain magnitudes diverge almost surely, although the continuous interpolation still crosses zero infinitely often; at equality the knot values fluctuate between arbitrarily large and arbitrarily small magnitudes almost surely.

In fact, the exact physical-time upper logarithmic growth rate and the full positive-moment classification follow from one formula:
\[
\limsup_{s\to\infty}\frac{1}{s}\log\frac{|V(s)|}{|u_0|}
=\frac{-e^{-1/\xi}\operatorname{Ei}(1/\xi)}{h}\quad\text{almost surely};\qquad
\mathbb E|\widehat V_k|^p=|u_0|^p\mu_p(\xi)^k,
\]
where \(\mu_p(\xi)=\int_0^\infty e^{-x}|1-\xi x|^p\,dx\) for every \(p>0\). For \(\xi<\xi_{\mathrm c}\), there is a unique positive \(p_*(\xi)\) at which \(\mu_{p_*}(\xi)=1\); moments decay strictly below that exponent and grow strictly above. For \(\xi\ge\xi_{\mathrm c}\), every positive absolute moment grows. The precise first- and second-moment stability ranges are \(0<\xi<1/\log2\) and \(0<\xi<1\), respectively.

## Assumptions and scope

Take \(a>0\), \(h>0\), \(u_0\in\mathbb R\setminus\{0\}\) and independent exponential random variables \(X_j\) of mean one. Define independent positive timesteps \(H_j=hX_j\), knot times \(T_0=0\), \(T_k=\sum_{j=1}^k H_j\), and the forward-Euler knot recurrence
\[
\widehat V_0=u_0,\qquad \widehat V_k=(1-aH_k)\widehat V_{k-1}.
\]
The continuous stochastic Euler trajectory is the **linear interpolant**: for each \(k\ge1\) and \(0\le s\le H_k\),
\[
V(T_{k-1}+s)=\widehat V_{k-1}(1-as).
\]
These are mathematical exact-arithmetic statements. At the zero times of \(V\), interpret \(\log|V|=-\infty\). Statements about moments concern **knot values** \(\widehat V_k\); only the logarithmic rate and qualitative convergence statements concern the entire interpolant. The random clock is an external iid exponential timestep model, not an Euler--Maruyama discretization of a Brownian stochastic differential equation.

Use the real exponential integral at \(z>0\), defined unambiguously by
\[
\operatorname{Ei}(z)=\gamma+\log z+\sum_{n=1}^\infty\frac{z^n}{n\,n!},
\]
where \(\gamma\) is Euler's constant. Its sole positive real zero is \(z_{\mathrm c}\).

## Proof

**1. Exact multiplicative logarithmic exponent.** Since \(X_1\) has density \(e^{-x}\) on \((0,\infty)\),
\[
L(\xi):=\mathbb E\log|1-\xi X_1|
=\int_0^\infty e^{-x}\log|1-\xi x|\,dx.
\]
The log singularity at \(x=1/\xi\) is integrable (even square-integrable), and the exponentially decaying tail renders every log moment finite. Put \(c=1/\xi\). Integration by parts on the two sides of \(c\), sending an equal exclusion radius to zero, and using the Cauchy principal-value exponential-integral representation gives
\[
\int_0^\infty e^{-x}\log|x-c|\,dx
=\log c-e^{-c}\operatorname{Ei}(c).
\]
Adding \(\log\xi\) proves the exact identity
\[
L(\xi)=-e^{-1/\xi}\operatorname{Ei}(1/\xi).
\]
The derivative \(\operatorname{Ei}'(c)=e^c/c>0\) and limits \(\operatorname{Ei}(0+)=-\infty\) and \(\operatorname{Ei}(+\infty)=+\infty\) show the unique positive zero. Hence \(L(\xi)<0\) precisely when \(\xi<\xi_{\mathrm c}\), and \(L(\xi)>0\) precisely when \(\xi>\xi_{\mathrm c}\).

The event that some \(1-\xi X_j\) equals zero has probability zero. Thus, outside this null event,
\[
\log\frac{|\widehat V_k|}{|u_0|}
=\sum_{j=1}^k \log|1-\xi X_j|.
\]
The strong law of large numbers gives an almost-sure limit of the left side divided by \(k\) equal to \(L(\xi)\). Consequently the knots converge exponentially to zero for \(\xi<\xi_{\mathrm c}\) and diverge in magnitude exponentially for \(\xi>\xi_{\mathrm c}\).

At \(\xi=\xi_{\mathrm c}\), the summands are iid, centered, have finite strictly positive variance and are nondegenerate. The law of the iterated logarithm therefore shows that their partial sums have liminf \(-\infty\) and limsup \(+\infty\). Exponentiating proves \(\liminf_{k\to\infty}|\widehat V_k|=0\) and \(\limsup_{k\to\infty}|\widehat V_k|=+\infty\).

**2. Continuous physical-time paths.** By the strong law, \(T_k/k\to h\) almost surely. On the \(k\)-th segment,
\[
|V(s)|\le |\widehat V_{k-1}|(1+aH_k).
\]
Exponential tails give \(H_k/k\to0\) almost surely by Borel--Cantelli, hence \(\log(1+aH_k)=o(k)\). With \(s/k\to h\) for any \(s\in[T_{k-1},T_k]\), the preceding inequality gives an upper bound \(L(\xi)/h\) for the physical-time logarithmic limsup. Evaluating at the knots gives the matching lower bound, proving
\[
\limsup_{s\to\infty}s^{-1}\log|V(s)/u_0|=L(\xi)/h.
\]
When \(L(\xi)<0\), the upper bound implies global exponential decay of the interpolated trajectory. For any \(\xi>0\), the independent event \(H_k>1/a\) has positive probability \(e^{-1/\xi}\) and therefore occurs infinitely often by the second Borel--Cantelli lemma. On each such segment the nonzero affine interpolant crosses exactly through zero, so \(\liminf_{s\to\infty}|V(s)|=0\) even when the knots diverge. At and above the critical threshold, the knot subsequences supply \(\limsup_{s\to\infty}|V(s)|=\infty\), and at criticality the described oscillation already holds for the knots.

**3. All positive knot moments.** Independence implies, for every integer \(k\ge0\) and real \(p>0\),
\[
\mathbb E|\widehat V_k|^p=|u_0|^p\left(\int_0^\infty e^{-x}|1-\xi x|^p\,dx\right)^k.
\]
Let \(Q_\xi(p)=\log\mu_p(\xi)\). The law of \(\log|1-\xi X|\) is nondegenerate and admits exponential moments at every nonnegative order. Therefore \(Q_\xi\) is strictly convex, \(Q_\xi(0)=0\), and \(Q_\xi'(0)=L(\xi)\). Since \(\Pr(|1-\xi X|>1)>0\), \(Q_\xi(p)\to+\infty\) as \(p\to\infty\). Thus if \(L(\xi)<0\), strict convexity and continuity give exactly one root \(p_*(\xi)>0\) besides zero, with \(Q_\xi(p)<0\) for \(0<p<p_*\) and \(Q_\xi(p)>0\) for \(p>p_*\). If \(L(\xi)\ge0\), strict convexity gives \(Q_\xi(p)>0\) for every \(p>0\). At the critical exponent \(p=p_*\), the exact moment stays constant and equal to \(|u_0|^p\).

Splitting the absolute-value integral at \(1/\xi\) yields
\[
\mu_1(\xi)=1-\xi+2\xi e^{-1/\xi};\qquad
\mu_2(\xi)=1-2\xi+2\xi^2.
\]
The respective strict contraction ranges are exactly \(\xi<1/\log2\) and \(\xi<1\). Also \(\mathbb E\widehat V_k=(1-\xi)^k u_0\). That last signed-mean identity is prior established work and is included solely for comparison. In particular, for \(2<\xi<\xi_{\mathrm c}\), almost every physical-time path decays exponentially although the signed mean and every integer-order positive absolute moment grow exponentially. This proves the full claim.

## Verification

The accompanying program `verify.py` (run with Python and the `mpmath` version specified in `requirements.txt`) evaluates both sides of the logarithmic integral and the first two absolute-moment formulas at nine distinct positive values of \(\xi\). It also checks the sign and the high-precision unique numerical zero of \(\operatorname{Ei}\), and solves a noninteger moment threshold at \(\xi=1.2\). The 39 approximate numerical assertions pass; the recorded output is included as `verification_output.txt`. These numerical checks confirm the calculations but do not establish almost-sure or all-\(k\) statements; those follow from the proof above.

## Relationship to prior work

Latz's *The random timestep Euler method and its continuous dynamics* (first public version 2024-08-02) defines the same exponential waiting-time forward-Euler recurrence and piecewise-linear stochastic Euler dynamics. Its scalar stability section supplies exact signed-mean and second-moment recursions and sufficient conditions for mean-square and continuous-time Lyapunov stability. The present result **does not claim the method or those two moment identities as new**. Its separate assertion is the sharp exponential-integral **almost-sure** phase boundary, the full physical-time pathwise conclusion including critical and supercritical cases, and the continuous family of absolute-moment cutoffs.

Abdulle and Garegnani's earlier randomized-timestep integration analysis addresses finite-time convergence and random-time geometric integration, not the above sharp exponential-clock scalar pathwise threshold. Generic iid random-product theorems underlie the strong-law and moment arguments, but by themselves do not compute this method's exponential-integral boundary or distinguish its physical-time spline path. The potential presence of an equivalent sharp criterion in other stochastic-integration or random-products literature remains an originality limitation.

## Limitations

The theorem applies only to one real scalar linear stable ODE with iid exponential timesteps, exact arithmetic, and the specified continuous linear spline. It does not assert the same threshold for bounded or correlated timestep laws, nonlinear ODEs, vector systems, other numerical integrators, or finite precision. The physical-time exponent is a **limsup** because exact zero crossings occur infinitely often; it is not a pointwise logarithmic limit of the full interpolant. No independent mathematical audit has been performed.

## References

1. J. Latz, *The random timestep Euler method and its continuous dynamics*, arXiv:2408.01409 (first submitted 2024-08-02), https://arxiv.org/abs/2408.01409; journal version, *IMA Journal of Numerical Analysis*, DOI:10.1093/imanum/draf096.
2. A. Abdulle and S. Garegnani, *Random time step probabilistic methods for uncertainty quantification in chaotic and geometric numerical integration*, arXiv:1801.01340 (2018), https://arxiv.org/abs/1801.01340.
3. D. J. Higham, X. Mao and C. Yuan, *Almost Sure and Moment Exponential Stability in the Numerical Simulation of Stochastic Differential Equations*, *SIAM Journal on Numerical Analysis* (2007), DOI:10.1137/060658138. Its abstract is relevant as broader conceptual context for distinguishing almost-sure from moment stability, but a full-text equivalence comparison was not completed.
