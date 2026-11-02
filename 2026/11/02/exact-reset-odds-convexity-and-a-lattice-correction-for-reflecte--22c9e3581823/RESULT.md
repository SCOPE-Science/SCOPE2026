# Exact reset-odds convexity and a lattice correction for reflected-path cover times

## Finding

For every integer \(L\ge1\), consider a simple random walk on the path with vertices \(\{-L,-L+1,\ldots,L\}\), initially at \(0\). At each discrete step it resets to \(0\) with probability \(r\in[0,1)\), independently of everything else; otherwise it moves uniformly to a graph neighbor, hence deterministically inward at an endpoint. Resets consume one step. Let \(C_L(r)\) denote the first time all vertices have been visited.

Write \(\mathsf T_L\) for the degree-\(L\) Chebyshev polynomial of the first kind. The exact mean for \(0<r<1\) is
\[
\mathbb E C_L(r)=\frac{3Z_L-1-2/Z_L}{r},\qquad Z_L=\mathsf T_L((1-r)^{-1}).
\]
At \(r=0\), \(\mathbb E C_L(0)=5L^2\), and
\[
\left.\frac{d}{dr}\mathbb E C_L(r)\right|_{r=0+}
=\frac{L^2(25-7L^2)}6.
\]
In the resetting odds \(u=r/(1-r)\), the mean is **strictly convex for every \(L\ge2\)** and strictly increasing (affine) when \(L=1\). Consequently, the three-vertex path (\(L=1\)) is uniquely fastest without resetting, whereas **every odd path with at least five vertices** (\(L\ge2\)) has a unique strictly positive optimal resetting probability \(r_L^*\in(0,1)\).

There is also a precise lattice-to-diffusion correction. Define, for \(\alpha>0\),
\[
\begin{split}
 t&=\sqrt{2\alpha},\\
 f(\alpha)&=\frac{3\cosh t-1-2\operatorname{sech}t}{\alpha},\\
 h(\alpha)&=\frac{5t\sinh t}{12}\bigl(3+2\operatorname{sech}^2t\bigr),
\end{split}
\]
with \(f(0)=5\). On each compact subinterval of \((0,\infty)\), uniformly in \(\alpha\),
\[
\mathbb E C_L(\alpha/L^2)
=L^2 f(\alpha)+h(\alpha)+O(L^{-2}).
\]
The function \(f\) has a unique minimizer \(\alpha_*\in(0,\infty)\); thus
\[
L^2r_L^*\longrightarrow\alpha_*,\qquad
\min_{0\le r<1}\mathbb EC_L(r)
=L^2 f(\alpha_*)+h(\alpha_*)+O(L^{-2}).
\]
Numerically, \(\alpha_*=0.884895423128587\ldots\), \(f(\alpha_*)=4.612508373932379\ldots\), and \(h(\alpha_*)=3.401322957695871\ldots\). These are numerical evaluations of the explicit functions, not certified decimal bounds.

## Assumptions and scope

The underlying graph is precisely the unweighted path of \(2L+1\) vertices. The initial and resetting vertex is the central vertex \(0\). Reset decisions are independent Bernoulli trials at each time step, and a reset is recorded as a time step but does not erase the vertices already visited. The endpoint walk transition is to the unique neighbor when no reset occurs. All statements about \(L\) are quantified over positive integers; the asymptotic bounds concern \(L\to\infty\) and fixed positive \(\alpha\) in compact sets. No claim is made for biased or noncentral restarting, other graph families, or arbitrary renewal reset times.

## Proof

**1. A hitting-time renewal identity.** For the reset-free reflected walk, let \(\tau\) be the first hitting time of a fixed nonempty target set, and set \(F_x(s)=\mathbb E_x[s^\tau]\) for \(s=1-r\). The probability of reaching the target before the first reset is \(F_x(s)\); the mean length of the first attempt, including a possible resetting step, is \((1-F_x(s))/r\). If a failed attempt begins again at vertex \(0\), renewal and first-step conditioning give the exact reset-process hitting-time mean
\[
H_x^r=\frac{1-F_x(s)}{rF_0(s)}.
\]
The identity applies also when the walker starts from another vertex \(x\), but all future resets are to \(0\). Its use does not assume that failed excursions erase previously achieved coverage: each phase ends upon hitting one specified previously unvisited endpoint.

**2. First endpoint.** Put \(\kappa=\operatorname{arcosh}(1/s)\). The recurrence \(F_x=s(F_{x-1}+F_{x+1})/2\) in the interior, with \(F_{\pm L}=1\) at the two targets, gives \(F_0=\operatorname{sech}(L\kappa)\). The expected time from the center to the first endpoint is therefore \((\cosh(L\kappa)-1)/r\).

**3. Opposite endpoint.** Suppose that \(+L\) was first visited. To hit \(-L\), the reset-free Laplace generating function for a start at \(x\) solves the same second-order interior recurrence with boundary values \(F_{-L}=1\), \(F_L=sF_{L-1}\). Therefore
\[
F_x(s)=\frac{\cosh(\kappa(L-x))}{\cosh(2L\kappa)}.
\]
In particular \(F_L=1/\cosh(2L\kappa)\) and \(F_0=\cosh(L\kappa)/\cosh(2L\kappa)\). The renewal identity makes the second-phase mean \((\cosh(2L\kappa)-1)/(r\cosh(L\kappa))\). The strong Markov property at the first endpoint, together with reflection symmetry, allows addition of the two phase means. Using \(\cosh(2x)=2\cosh^2x-1\) gives the claimed exact formula. For \(r\downarrow0\), the expansion \(\cosh(L\kappa)=1+L^2r+O_L(r^2)\) gives \(5L^2\).

**4. Strict convexity and the finite-path threshold.** Set \(u=r/(1-r)\), so that \(s=(1+u)^{-1}\), and \(Z=\mathsf T_L(1+u)\). Rearranging the exact answer gives
\[
M_L(u):=\mathbb EC_L\bigl(u/(1+u)\bigr)
=3(1+u)\frac{Z-1}{u}
+2(1+u)\frac{1-Z^{-1}}u.
\]
The first summand is a polynomial with nonnegative coefficients: \(Z=1+\sum_{j=1}^L a_j u^j\), \(a_1=L^2\), and the Chebyshev differential equation yields
\[
a_{j+1}=\frac{L^2-j^2}{(j+1)(2j+1)}a_j>0
\qquad(0\le j<L),\quad a_0=1.
\]
The second summand is exactly twice the discounted tail of the reset-free time \(\tau_L\) to hit \(\{-L,L\}\) from the center:
\[
(1+u)\frac{1-Z^{-1}}u
=\sum_{j=0}^\infty\Pr(\tau_L>j)(1+u)^{-j}.
\]
Every summand is convex in \(u\ge0\); if \(L\ge2\), the \(j=1\) summand has strictly positive weight and is strictly convex. The series and its derivatives converge on compact intervals, since a finite-path hitting time has an exponential tail. The first polynomial is strictly convex for \(L\ge2\) as well, so \(M_L\) is strictly convex. For \(L=1\), \(Z=1+u\) and \(M_1(u)=5+3u\), which is strictly increasing (affine rather than strictly convex). **Thus the precise assertion is strict convexity for \(L\ge2\), and strict monotonicity for \(L=1\).**

For general \(L\), \(\mathsf T_L'(1)=L^2\) and \(\mathsf T_L''(1)=L^2(L^2-1)/3\) give
\[
M_L'(0)=\frac{L^2(25-7L^2)}6.
\]
This derivative equals the right derivative in \(r\) at zero because \(u=r+O(r^2)\). For \(L\ge2\) it is negative. Since \(Z\to\infty\) as \(u\to\infty\), \(M_L(u)\to\infty\), and strict convexity gives a unique interior minimum. For \(L=1\), monotonicity gives the minimum at \(r=0\).

**5. Diffusive limit and first lattice correction.** Uniformly for \(\alpha\) in a compact subset of \((0,\infty)\), when \(r=\alpha/L^2\), elementary Taylor expansion gives
\[
L\operatorname{arcosh}\left((1-\alpha/L^2)^{-1}\right)
=t+\frac{5\alpha t}{12L^2}+O(L^{-4}),\qquad t=\sqrt{2\alpha}.
\]
Consequently \(Z=\cosh t+(5\alpha t/12L^2)\sinh t+O(L^{-4})\). Substitute into the exact mean and differentiate the function \(3Z-1-2/Z\) with respect to \(Z\). This yields uniformly \(\mathbb EC_L(\alpha/L^2)=L^2 f(\alpha)+h(\alpha)+O(L^{-2})\), including uniform differentiated expansions near any positive \(\alpha\).

For uniqueness of the limiting minimum, write
\[
f(\alpha)=3\frac{\cosh\sqrt{2\alpha}-1}{\alpha}
+2\frac{1-\operatorname{sech}\sqrt{2\alpha}}\alpha.
\]
The first summand is strictly convex because its power series has positive coefficients, including a positive quadratic coefficient. The second is convex: if \(\tau_B\) is standard Brownian first exit from \((-1,1)\), then \(\mathbb E e^{-\alpha\tau_B}=\operatorname{sech}\sqrt{2\alpha}\), so the second summand is \(2\int_0^\infty e^{-\alpha t}\Pr(\tau_B>t)\,dt\), a Laplace transform of a nonnegative measure. Furthermore \(f'(0+)=-7/6<0\) and \(f(\alpha)\to\infty\) as \(\alpha\to\infty\); hence its minimizer \(\alpha_*\) exists, is positive, and is unique.

For tightness of scaled lattice optimizers, note \(\cosh\sqrt{2r}\le(1-r)^{-1}\) for \(0\le r<1\) (compare nonnegative power-series coefficients). Hence, with \(\alpha=L^2r\), \(Z\ge\cosh\sqrt{2\alpha}\) and
\[
\frac{\mathbb EC_L(r)}{L^2}
\ge\frac{3(\cosh\sqrt{2\alpha}-1)}{\alpha},
\]
which diverges for \(\alpha\to\infty\). At \(\alpha\to0\) the scaled means tend to \(5>f(\alpha_*)\). Therefore \(L^2r_L^*\to\alpha_*\). The uniform differentiated expansion and \(f''(\alpha_*)>0\) improve this to \(L^2r_L^*=\alpha_*+O(L^{-2})\); substituting back yields the displayed optimal-value expansion.

## Verification

The independent exact-rational finite-state checker `STANDALONE_CHECK.py` reconstructs the walk on states (current position, set of already visited endpoints), builds and solves the absorbing linear system, and compares the result against the Chebyshev expression for all \(1\le L\le5\) and resetting rates \(r\in\{0,1/7,1/4,1/2\}\). It also verifies Chebyshev coefficient recurrences through degree 17, the exact first derivative, and three independent finite-size numerical tests of the asymptotic coefficient. Running `python3 STANDALONE_CHECK.py` printed `PASS: 125 checks`. These are reproducibility tests; they are not used as a substitute for the analytic all-size proof.

## Relationship to prior work

Linn and Lawley [1] derived the exact mean cover time for Brownian motion on a reflecting interval (their §2.2, especially equation (11)), and frequent-resetting asymptotics for general discrete networks (their §4). The leading function \(f\) here agrees with that **already published continuum result**; no novelty is claimed for the continuum formula itself. Das and Giuggioli [2] derived general discrete-time resetting renewal and single-target first-passage formulas, including confined lattice examples; these underpin rather than contradict the renewal method used here. Michelitsch and collaborators [3] gave a general network resetting and first-hitting framework, again distinct from a finite-path two-endpoint coverage optimization. Pal and Prasad [4] studied resetting interval exit (first passage), not completing coverage of both endpoints.

The finding adds to those known frameworks: the explicit mean for the graph-neighbor reflected path at every size and reset rate, the strict-convexity and five-vertex optimality threshold, and the nonzero exact order-one lattice correction at the optimally tuned rate. Literature comparisons do not constitute definitive historical priority, and a broader unlocated lattice coverage theorem could still contain these consequences.

## Limitations

The vertex-centered odd-path model is essential to the stated formulas. The first-order continuum function was already available in [1] and is not presented as a new continuum theorem. The uniqueness and lattice-correction claims have been analyzed within this exact transition convention only. Numerical constants are illustrative approximations, not interval-certified. Independent verification and definitive historical-priority assessment have not been performed.

## References

[1] S. Linn and S. D. Lawley, *Cover times with stochastic resetting*, first posted 2024-06-17, https://arxiv.org/abs/2406.12154 (especially §§2.2, 4).

[2] D. Das and L. Giuggioli, *Discrete space-time resetting model: Application to first-passage and transmission statistics*, first posted 2022-09-17, https://arxiv.org/abs/2209.08330 (especially §§2–3).

[3] T. M. Michelitsch, G. D'Onofrio, F. Polito, and A. P. Riascos, *Random walks with stochastic resetting in complex networks: a discrete time approach*, first posted 2024-09-12, https://arxiv.org/abs/2409.08394 (especially §§1–2).

[4] A. Pal and V. V. Prasad, *First passage under stochastic resetting in an interval*, first posted 2018-12-07, https://arxiv.org/abs/1812.03009.
