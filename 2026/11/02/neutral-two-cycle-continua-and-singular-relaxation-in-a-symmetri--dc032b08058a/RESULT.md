# Neutral two-cycle continua and singular relaxation in a symmetric mobilization map

## Finding
Consider the symmetric two-candidate threshold-response map of Fontanari [1], restricted to its fully mobilized line (the two candidate fractions sum to one) and with cross-rejection parameter exactly \(\gamma=2\). Write \(p=1/\lambda>0\) for the inverse threshold-shape exponent and \(z_n=\rho_A^{(n)}-\rho_B^{(n)}\in[-1,1]\). Set
\[
J_p(z)=2^{-p}\big((1+z)^p-(1-z)^p\big).
\]
The exact induced iteration is \(z_{n+1}=-J_p^{-1}(z_n)\), where the inverse is on \([-1,1]\). The following classification is exhaustive.

For \(1<p<2\), every trajectory with \(0<|z_0|<1\) approaches the balanced fixed point \(z=0\), alternating sign with strictly decreasing magnitude. For \(0<p<1\) or \(p>2\), every such trajectory approaches the endpoint period-two orbit \(\{1,-1\}\), alternating sign with strictly increasing magnitude. The boundary pair \(\{1,-1\}\) is a period-two orbit for every \(p>0\). For \(p=1\) **and** \(p=2\), every nonzero \(z_0\) has an exactly neutral period-two orbit \(\{z_0,-z_0\}\), while \(z=0\) is fixed; hence there is a continuum of interior period-two trajectories with unit two-step derivative. The two exceptional exponents correspond to \(\lambda=1\) and \(\lambda=1/2\).

At each exceptional exponent \(p_0\in\{1,2\}\) this continuum has a sharp finite-amplitude slow-time unfolding. Define, for \(0<s<1\),
\[
H_{p_0}(s)=\frac{(1+s)^{p_0}\log((1+s)/2)-(1-s)^{p_0}\log((1-s)/2)}{2^{p_0}}.
\]
Fix \(s_0=|z_0|\in(0,1)\), \(T>0\), and a sign \(\eta\in\{-1,1\}\). As \(\delta\to0\) through values with \(\operatorname{sgn}\delta=\eta\), the amplitude trajectory
\[
 s^\delta(t)=|z_{\lfloor t/|\delta|\rfloor}|\quad\text{under }p=p_0+\delta
\]
converges uniformly for \(0\le t\le T\), with error \(O_{s_0,T,p_0}(|\delta|)\), to the solution of
\[
\dot S=-\eta H_{p_0}(S),\qquad S(0)=s_0.
\]
The drift has a strict sign: \(H_1(s)>0\) and \(H_2(s)<0\) on \((0,1)\). Thus \(p\downarrow1\) from above and \(p\uparrow2\) from below drive toward balance; the other two one-sided approaches drive toward endpoint oscillation.

In particular, for fixed \(0<a<b<1\), if \(N_\delta\) denotes the first discrete passage from amplitude \(a\) to \(b\) on the endpoint-moving side, or from \(b\) to \(a\) on the balance-moving side, then
\[
\lim_{\delta\to0,\ \operatorname{sgn}\delta=\eta}|\delta|N_\delta
=\int_a^b\frac{du}{|H_{p_0}(u)|},
\]
with the passage direction determined by \(\operatorname{sgn}(-\eta H_{p_0})\). This is an exact, nonzero finite coefficient for the diverging transition times near both neutral continua.

## Assumptions and scope
The original model has candidate fractions \(\rho_A,\rho_B\ge0\), abstention fraction \(\rho_0=1-\rho_A-\rho_B\ge0\), symmetric shape exponent \(\lambda>0\), and symmetric cross-rejection \(\gamma=2\). We start on the invariant line \(\rho_A+\rho_B=1\). The model's overlapping-activation rule selects the unique \(u\in[0,1]\) satisfying \(u^{1/\lambda}-(1-u)^{1/\lambda}=U_A-U_B\), with \(U_A=\rho_A+\gamma\rho_B\), \(U_B=\rho_B+\gamma\rho_A\). No empirical assumptions or global two-dimensional attraction are used. The slow-limit statement fixes the initial interior amplitude and a finite rescaled time horizon before taking \(\delta\to0^\pm\). The crossing-time limit fixes its two interior amplitude levels.

## Proof
**Exact reduction.** On the line \(\rho_A+\rho_B=1\), at \(\gamma=2\) one has \(U_A=1+\rho_B\ge1\) and \(U_B=1+\rho_A\ge1\), so the overlapping branch applies at every iterate. With \(z=\rho_A-\rho_B\) and updated \(w=2u-1\), the surplus equation is \(J_p(w)=U_A-U_B=-z\). Since \(J_p\) is continuous, odd, strictly increasing, and maps the endpoints to themselves for every \(p>0\), this uniquely gives \(w=-J_p^{-1}(z)\), and hence the claimed return map.

**Exhaustive phase portrait.** For \(0<z<1\), direct differentiation yields
\[
J_p''(z)=p(p-1)2^{-p}\big((1+z)^{p-2}-(1-z)^{p-2}\big).
\]
The sign is that of \((p-1)(p-2)\). For \(p<1\) or \(p>2\), the graph is strictly convex between \((0,0)\) and \((1,1)\); consequently \(J_p(z)<z\), so \(J_p^{-1}(z)>z\) for each interior positive \(z\). For \(1<p<2\), strict concavity reverses both inequalities. At \(p=1,2\), algebra gives the exact identity \(J_p(z)=z\). Because the amplitude iteration is \(s_{n+1}=J_p^{-1}(s_n)\), the noncritical amplitudes are strictly monotone and bounded. Any limit must be a fixed point of \(J_p\); strict convexity or concavity leaves only \(s=0,1\). The stated alternatives follow. At the two degenerate exponents the signed map is exactly \(z\mapsto-z\), so every interior nonzero point has prime period two and the derivative of the two-step map equals one.

**Unfolding coefficient.** At \(p=p_0\in\{1,2\}\), one has \(J_{p_0}(s)=s\), \(J_{p_0}'(s)=1\). Differentiating with respect to the exponent gives \(\partial_pJ_p(s)|_{p=p_0}=H_{p_0}(s)\). The inverse-function theorem, uniformly on compact subintervals of \((0,1)\), gives
\[
J_{p_0+\delta}^{-1}(s)=s-\delta H_{p_0}(s)+O(\delta^2),
\]
with a uniform \(C^1\) remainder on each such compact set. Direct differentiation shows
\[
H_1''(s)=-\frac{s}{1-s^2}<0,\qquad
H_2''(s)=\frac12\log\frac{1+s}{1-s}>0.
\]
Both functions vanish at \(s=0\) and \(s=1\) by continuous extension; strict concavity of \(H_1\) and strict convexity of \(H_2\) therefore give the claimed opposite signs.

**Uniform slow limit.** Put \(h=|\delta|\), with fixed sign \(\eta\). The amplitude update reads \(s_{n+1}=s_n-h\eta H_{p_0}(s_n)+O(h^2)\), uniformly on compact subsets of \((0,1)\). The limiting ODE has unique interior trajectories for every finite time: both drift functions are smooth in the interior, vanish linearly at zero, \(H_2\) is Lipschitz at one, and \(H_1(1-v)=O(v|\log v|)\), whose reciprocal has divergent integral as \(v\downarrow0\). Thus any finite-horizon limiting trajectory is contained in a compact interior subinterval. A standard discrete Grönwall estimate for the Euler scheme on that compact interval gives an \(O(h)\) error uniformly through \(n\le T/h\). This also proves the stated uniform convergence of the piecewise-constant interpolation.

**Passage-time constant.** The limiting ODE is strictly monotone between any prescribed interior levels \(a<b\); its hitting time is obtained by separation of variables as \(\int_a^b|H_{p_0}(u)|^{-1}du\). Uniform trajectory convergence on a finite interval extending beyond that hitting time and strict monotonicity of the discrete amplitude sequence give convergence of first-passage times after multiplication by \(h\). The integral is finite and positive because \(H_{p_0}\) is continuous and has no zero on \([a,b]\).

## Verification
Run `python verify.py` in an environment with SymPy and SciPy. The standalone script checks the exact neutral identities, the two curvature identities, finite examples of strict monotonicity and inverse-branch consistency, the small-exponent inverse expansion, and sample crossing-time constants. It reports 179 finite assertions and identities. In particular, for amplitude levels \(a=1/4\), \(b=3/4\), the predicted slow-time constants are approximately \(4.207740802102\) at \(p_0=1\) and \(7.363093797459\) at \(p_0=2\). These computations are consistency tests, not substitutes for the global proof or the asymptotic limit.

## Relationship to prior work
Fontanari [1] introduces the exact two-dimensional threshold-response model and the symmetric one-dimensional fully mobilized rule (its equations (7), (14), and (17)). It describes a generic flip threshold and period-two oscillations. The present result uses the **same** physical rule at the special coupling \(\gamma=2\), but distinguishes two entire neutral continua, determines the exact direction of selection on either side of both exceptional exponents, and gives the nonlocal slow-time ODEs and first-passage coefficients. These facts are not stated in the accessible complete source. Venegeroles [2] studies a different strategic-positioning model of two parties, rather than this iterative surplus-cut rule. Borghesi and Galam [3] study contrarians in a different group-majority map. General inverse-map perturbation and Euler-limit methods are standard tools, but their use alone does not identify this model's two special exponents or explicit drift functions.

## Limitations
The theorem is entirely about the fully mobilized invariant line at \(\gamma=2\). It makes no assertion about the basin of attraction of this line from states with abstention, about other coupling values, about stochastic or empirical election behavior, or about a uniform-in-time approximation as \(t\to\infty\). The near-neutral limit uses \(p=1/\lambda\), not an additive perturbation in \(\lambda\); that change of coordinate matters for the numerical time coefficient. Historical priority of the explicit slow-limit formula has not been independently audited; specialized unindexed literature remains a residual risk.

## References
[1] J. F. Fontanari, *Negative partisanship drives anti-frontrunner volatility in election dynamics*, arXiv:2610.25210v1 (18 October 2026), https://arxiv.org/html/2610.25210.

[2] R. Venegeroles, *Beyond the Median Voter: A Model of How the Ideological Dimension Shapes Party Polarization*, arXiv:2410.11512 (initially 15 October 2024), https://arxiv.org/abs/2410.11512.

[3] C. Borghesi and S. Galam, *Chaotic, staggered, and polarized dynamics in opinion forming: The contrarian effect*, Physical Review E 73, 066118 (2006), https://doi.org/10.1103/PhysRevE.73.066118.
