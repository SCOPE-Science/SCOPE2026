# A sharp charge threshold for the direction of finite-horizon optimal battery loading

## Finding

A two-state stochastic battery with fixed positive excitation gap admits a **unique** constant load maximizing expected net useful work during every prescribed finite discharge horizon. Surprisingly, the maximizing load can move either upward or downward as that horizon lengthens. The direction is determined by a sharp prepared-occupation threshold, independent of the horizon and of the kinetic barrier:

\[
p_{\mathrm{crit}}=\frac12+\frac{\beta E}{4}.
\]

When the initial charged occupation is below this threshold, the optimal load increases strictly with discharge time. Above the threshold, it decreases strictly. At equality, the optimal load is exactly the intrinsic energy gap \(E\) for **every** discharge duration. The decreasing branch is physically accessible only when \(\beta E<2\). Finite charging can cross this threshold, while thermal leakage during storage crosses it in the opposite direction, yielding explicit charge-time and hold-time switching laws.

The result applies to a **constant** load held throughout each discharge. It does not assert optimality against time-varying load controls.

## Assumptions and scope

Fix inverse temperature \(\beta>0\), excitation energy \(E>0\), discharge kinetic rate \(k>0\), and a prepared upper-state occupation \(p\) satisfying

\[
p_{\mathrm{eq}}=\frac{1}{1+e^{\beta E}}<p<1.
\]

The battery has lower and upper energies \(0\) and \(E\). A load \(w\) awards net work \(w\) per \(1\to0\) jump, minus \(w\) per \(0\to1\) jump. During a discharge of duration \(T>0\), the two transition rates are fixed at

\[
k_{10}(w)=k e^{\beta(E-w)/2},\qquad
k_{01}(w)=k e^{-\beta(E-w)/2}.
\]

These rates are the symmetric local-detailed-balance splitting of the active-matter battery's loaded Markov kinetics. Define the generalized initial voltage, load-dependent relaxation rate and loaded stationary population by

\[
\Phi=E+\beta^{-1}\log\frac{p}{1-p}>0,\qquad
\lambda(w)=2k\cosh\!\left(\frac{\beta(E-w)}2\right),\qquad
q(w)=\frac{1}{1+e^{\beta(E-w)}}.
\]

The physically positive-work, constant-load domain is \(0<w<\Phi\). Define \(W_T(w)\) as the expected net delivered work in this interval, including backward transitions. No externally controlled modulation of the load, running cost of the active charger, or leakage during the actual discharge is assumed beyond these rates.

**Theorem.** For every admissible \((\beta,E,k,p,T)\),

\[
W_T(w)=w[p-q(w)]\left(1-e^{-\lambda(w)T}\right)
\]

is strictly **log-concave** in \(w\in(0,\Phi)\) and has a unique global maximizer \(w_T\). Let \(p_{\mathrm{crit}}=1/2+\beta E/4\). Then

\[
\begin{array}{ll}
p<p_{\mathrm{crit}}:& 0<w_T<E,\quad \frac{d w_T}{dT}>0,\\
p=p_{\mathrm{crit}}:& w_T=E\quad\text{for all }T>0,\\
p>p_{\mathrm{crit}}:& E<w_T<\Phi,\quad \frac{d w_T}{dT}<0.
\end{array}
\]

The equality and upper branches are interpreted only for occupations actually inside \((p_{\mathrm{eq}},1)\). In particular, if \(\beta E\ge2\), the upper branch is impossible. For \(p\ne p_{\mathrm{crit}}\), let \(w_0=\lim_{T\downarrow0}w_T\) and \(w_\infty=\lim_{T\to\infty}w_T\). They are the respective unique roots

\[
\frac1{w_0}=\frac\beta2\coth\!\left(\frac\beta2(\Phi-w_0)\right),
\qquad
\frac1{w_\infty}=\frac{\beta q(w_\infty)[1-q(w_\infty)]}{p-q(w_\infty)}.
\]

Moreover, the strict horizon-ordering is

\[
p<p_{\mathrm{crit}}:\quad w_0<w_T<w_\infty<E,
\qquad
p>p_{\mathrm{crit}}:\quad E<w_\infty<w_T<w_0.
\]

At \(p=p_{\mathrm{crit}}\), all three loads equal \(E\).

**Preparation and retention corollary.** Consider active charging with affinity \(a>0\), kinetic relaxation \(\lambda_c>0\), and stationary charged occupation \(p_a=[1+e^{\beta(E-a)}]^{-1}\), starting at \(p_{\mathrm{eq}}\). The decreasing-with-discharge-horizon regime is reachable after a finite charging time if and only if \(p_a>p_{\mathrm{crit}}\), equivalently \(\beta E<2\) and

\[
a>E+\beta^{-1}\log\frac{p_{\mathrm{crit}}}{1-p_{\mathrm{crit}}}.
\]

The unique time at which all horizon-optimal loads equal \(E\) is

\[
t_c^*=\lambda_c^{-1}\log\frac{p_a-p_{\mathrm{eq}}}{p_a-p_{\mathrm{crit}}}.
\]

After preparing \(p_c>p_{\mathrm{crit}}\), thermal storage with a fixed positive leakage relaxation \(\lambda_s\) produces \(p_h=p_{\mathrm{eq}}+(p_c-p_{\mathrm{eq}})e^{-\lambda_s h}\). The optimal-load horizon response reverses from decreasing to increasing at the unique hold time

\[
h^*=\lambda_s^{-1}\log\frac{p_c-p_{\mathrm{eq}}}{p_{\mathrm{crit}}-p_{\mathrm{eq}}}.
\]

At each equality the optimum is exactly \(E\), independently of the discharge kinetic scale.

## Proof

**Step 1: Markov counting identity.** For a constant load \(w\), the upper-level probability \(p_w(t)\) satisfies

\[
\dot p_w=k_{01}(w)[1-p_w]-k_{10}(w)p_w
=-\lambda(w)[p_w-q(w)],\qquad p_w(0)=p.
\]

Therefore \(p_w(T)=q(w)+[p-q(w)]e^{-\lambda(w)T}\). Each downward jump contributes \(+w\) and each upward jump contributes \(-w\); the net number of downward minus upward jumps equals the decrease of the binary occupation, path by path. Taking expectations yields the displayed \(W_T\). Since \(q(w)<p\) exactly when \(w<\Phi\), the work is positive in the stated open interval and vanishes at both endpoints.

**Step 2: A strictly log-concave finite-duration response kernel.** Write \(c=\beta/2\) and

\[
K_T(\lambda)=\int_0^T e^{-\lambda s}\,ds,
\qquad
J_0(w)=k\bigl[p e^{c(E-w)}-(1-p)e^{-c(E-w)}\bigr].
\]

An exact factorization is

\[
W_T(w)=wJ_0(w)K_T(\lambda(w)),\qquad
J_0(w)=2k\sqrt{p(1-p)}\sinh[c(\Phi-w)].
\]

For \(\lambda,T>0\), let \(\mu_{\lambda,T}\) and \(v_{\lambda,T}\) be the mean and variance of \(s\) under the probability density \(e^{-\lambda s}/K_T(\lambda)\) on \([0,T]\). With \(u=\lambda T\), direct integration gives

\[
\mu_{\lambda,T}=\lambda^{-1}-\frac{T}{e^u-1},\qquad
v_{\lambda,T}=\lambda^{-2}-\frac{T^2e^u}{(e^u-1)^2},
\]

and the exact strict inequality

\[
\frac{\mu_{\lambda,T}}{\lambda}-v_{\lambda,T}
=\frac{u\bigl[(u-1)e^u+1\bigr]}{\lambda^2(e^u-1)^2}>0.
\]

Indeed, \((u-1)e^u+1\) vanishes at zero and has derivative \(u e^u>0\) for \(u>0\). Differentiation through the finite integral establishes

\[
\frac{d^2}{dw^2}\log K_T(\lambda(w))
=v_{\lambda,T}[\lambda'(w)]^2
-\mu_{\lambda,T}\lambda''(w).
\]

The hyperbolic relaxation rate obeys

\[
\lambda''(w)=c^2\lambda(w),\qquad
[\lambda'(w)]^2=c^2[\lambda(w)^2-4k^2].
\]

Using \(v_{\lambda,T}<\mu_{\lambda,T}/\lambda\), its logarithmic curvature is strictly negative:

\[
\frac{d^2}{dw^2}\log K_T(\lambda(w))
\le-\frac{4c^2k^2}{\lambda(w)}\mu_{\lambda,T}<0.
\]

Finally, \(\log w\) and \(\log\sinh[c(\Phi-w)]\) are strictly concave on \((0,\Phi)\). Hence \(\log W_T\), their sum with \(\log K_T\) and a constant, is strictly concave. Continuity and vanishing endpoint values prove existence, uniqueness, and nondegeneracy of its interior maximizer.

**Step 3: Critical occupation.** The derivative of the logarithm is

\[
F_T(w):=\frac{d}{dw}\log W_T(w)=
\frac1w-c\coth[c(\Phi-w)]-
\lambda'(w)\mu_{\lambda(w),T}.
\]

If \(p\le1/2\), then \(\Phi\le E\) and necessarily \(w_T<E\). For \(p>1/2\), the interior point \(w=E\) satisfies \(\lambda'(E)=0\), and \(\tanh[c(\Phi-E)]=2p-1\). Therefore

\[
F_T(E)=\frac1E-\frac{\beta}{2(2p-1)},
\]

independent of \(T\) and \(k\). Because \(F_T\) is strictly decreasing and crosses zero exactly once, its sign at \(E\) puts the optimizer strictly below or above \(E\), with equality exactly at \(p=1/2+\beta E/4\). Since \(p<1\), the upper regime requires \(\beta E<2\).

**Step 4: Strict horizon monotonicity and endpoints.** Differentiating the truncated-exponential mean with respect to its upper support endpoint gives

\[
\partial_T\mu_{\lambda,T}=
\frac{e^{-\lambda T}}{K_T(\lambda)}(T-\mu_{\lambda,T})>0.
\]

At the unique optimum, the implicit-function theorem applies because \(\partial_wF_T(w_T)=\partial_w^2\log W_T(w_T)<0\). Thus

\[
\frac{dw_T}{dT}=
\frac{\lambda'(w_T)\partial_T\mu_{\lambda(w_T),T}}
{\partial_wF_T(w_T)},
\]

which has the opposite sign to \(\lambda'(w_T)=-2kc\sinh[c(E-w_T)]\). The location classification from Step 3 therefore gives the claimed strict increase or decrease. At equality \(w_T=E\) for every \(T\).

As \(T\downarrow0\), \(K_T(\lambda)/T\to1\) uniformly on the compact load interval \([0,\Phi]\), so the unique maximizer converges to that of \(wJ_0(w)\), yielding the displayed equation for \(w_0\). As \(T\to\infty\), \(\lambda(w)\ge2k\) gives uniform convergence of \(W_T(w)\) to \(w[p-q(w)]\); differentiating its logarithm produces the equation for \(w_\infty\). Strict horizon monotonicity then yields the two strict orderings.

**Step 5: Exact preparation and aging thresholds.** The charging master equation gives \(p_c(t)=p_{\mathrm{eq}}+(p_a-p_{\mathrm{eq}})(1-e^{-\lambda_c t})\), strictly increasing from \(p_{\mathrm{eq}}\) to \(p_a\). It crosses \(p_{\mathrm{crit}}\) at a finite time precisely when \(p_a>p_{\mathrm{crit}}\); solving this equality gives \(t_c^*\) and the stated affinity condition. During unforced storage the occupation decreases exponentially to \(p_{\mathrm{eq}}\). When it starts above \(p_{\mathrm{crit}}\), it crosses the same threshold once, at the displayed \(h^*\), reversing the sign conclusion from Step 4. This completes the proof.

## Verification

The standalone `verify.py` uses only the Python standard library. Execute `python3 verify.py` in the directory containing this file. It checks direct master-equation evolution against the counting-work formula, numerical first-order conditions and load maxima, horizon orderings, the truncated-exponential variance inequality, the fixed intrinsic-gap optimum, and the charge/hold threshold crossings. In the recorded test run it passed 6636 bounded checks across 108 parameter families, including prepared occupations on both sides of the threshold.

These finite calculations are consistency tests. The statements for all positive parameters and all discharge horizons follow from the analytical argument in the Proof section, not from a finite grid or numerical extrapolation.

## Relationship to prior work

Lin, Liu and Ma (2026) give the same two-state active-matter battery and symmetric loaded transition rates. Their discharge optimization maximizes **instantaneous** power at a fixed occupation (their equations 11–15), and their total-work bound allows quasistatic **state-dependent** loads. The present result instead optimizes a *single load fixed over an entire prescribed finite discharge window* and classifies its motion with the window length. The zero-time limit of the new theorem recovers, rather than replaces, their known instantaneous optimum.

Liu, Lin and Ma (2026) analyze finite-time battery discharge using resistor/capacitor circuit models and multistage constant-current scheduling. The accessible article description, introduction, summary, and appendix extracts concern circuit and scheduling results rather than the present binary Markov response. They do not establish the load-dependent binary Markov relaxation formula, strict finite-horizon log-concavity, or sharp occupation threshold; a complete independent full-text comparison was not possible. General stochastic-thermodynamic optimal-control theories usually allow time-varying controls or optimize different work/entropy objectives; the present constant-load classification should not be read as a theorem about those larger policy classes.

## Limitations

The result assumes a two-state, Markovian, isothermal device with symmetric rate splitting, a fixed kinetic rate scale during discharge, and a *constant* load. It concerns **expected net** work, not gross forward-jump energy, work fluctuations, stochastic reliability, or a global optimal-control policy. Time-varying loading, feedback, load-dependent barrier changes, non-Markovian active baths, and full cycle fuel costs lie outside the theorem. The preparation and hold formulas describe ideal Markov stages with constant rates; real barrier manipulation may incur additional costs.

Originality has been assessed against the accessible primary works and related mathematical records, but broader unpublished or unlocated theorems may subsume pieces of the log-concavity argument. No independent mathematical or publication-priority validation is claimed.

## References

1. Y.-Q. Lin, R.-H. Liu, and Y.-H. Ma, *Active-Matter Battery*, arXiv:2610.00428v1, first public submission 2026-09-30. https://arxiv.org/html/2610.00428v1 . Full main text and Appendices A–C examined.
2. R.-H. Liu, Y.-Q. Lin, and Y.-H. Ma, *Finite-Time Thermodynamics of Battery Discharging: Power–Efficiency Trade-Off and Optimization*, arXiv:2607.03157 (first public submission 2026-07-03); *Entropy* 28 (2026), 852. https://www.mdpi.com/1099-4300/28/8/852 . Accessible journal abstract, introduction, summary, and appendix extracts examined; complete retrieval was limited.
3. T. Schmiedl and U. Seifert, *Optimal finite-time processes in stochastic thermodynamics*, *Phys. Rev. Lett.* 98 (2007), 108301, https://arxiv.org/abs/cond-mat/0701554 . General time-dependent optimal-control context; distinct objective and controls.
