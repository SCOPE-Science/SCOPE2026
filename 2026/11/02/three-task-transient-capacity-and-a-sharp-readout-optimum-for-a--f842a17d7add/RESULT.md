# Three-task transient capacity and a sharp readout optimum for a two-channel stochastic switch

## Finding

A two-state Markov switch with two input-biased reaction channels can implement **three** of the four Boolean labelings of two inputs if its initial state is prepared away from the uniform distribution. At any fixed positive classification margin the exact number of attainable labelings is given below. Moreover, jointly optimizing the initial preparation and the observation time has a unique time optimum, and it requires a *pure*, rather than mixed, initial state. The optimal time has a logarithmic weak-driving divergence, while the optimal margin has a control-range-dependent fractional-power correction.

Fix positive parameters \(k,b,f,T\). The Markov state is \(n\in\{0,1\}\), and the input and control are \(x\in\{-1,+1\}\) and \(\theta\in[-b,b]\). The two distinct transition channels have rates
\[
W_{\pm1}(\theta,x)=k e^{\theta\pm fx/2},\qquad
W_{\pm2}(\theta,x)=k e^{-\theta\mp fx/2},
\]
where \(+\) means a transition from state zero to state one, and \(-\) the reverse transition. The same initial probability \(\rho\in[0,1]\) of state one is used for both inputs and every control setting. Define \(\delta=\rho-1/2\), and classify the mean terminal output \(q(\theta,x;T)=\Pr(n_T=1\mid\theta,x)\) at threshold \(1/2\). A Boolean labeling \(y:\{-1,+1\}\to\{-1,+1\}\) is attainable at margin \(\gamma>0\) if a *single* allowed \(\theta\) satisfies
\[
y(x)[q(\theta,x;T)-1/2]\ge\gamma\quad\text{for both inputs.}\]

Put
\[
\begin{gathered}
a=4kT\cosh(f/2),\qquad c=\cosh b>1,\qquad H=\tanh b\,\tanh(f/2)\in(0,1),\\
C=|\delta|e^{-a},\qquad
B=\frac H2(1-e^{-ca})-|\delta|e^{-ca}.
\end{gathered}
\]
**Complete task-count theorem.** The number of distinct attainable labelings is exactly
\[
\boxed{N(\gamma)=\mathbf 1_{\{\gamma\le C\}}+2\mathbf 1_{\{\gamma\le B\}}\qquad(\gamma>0).}
\]
If \(\delta>0\), the possible constant labeling is \(y\equiv+1\); if \(\delta<0\), it is \(y\equiv-1\); for \(\delta=0\), neither constant labeling is attainable. Whenever \(B\ge\gamma\), both copying \(y(x)=x\) and inversion \(y(x)=-x\) are attainable. Four labelings are impossible for all allowed parameters. In particular, \(N=3\) is possible exactly when \(\gamma\le\min\{C,B\}\).

**Global three-task design theorem.** Fix \(k,b,f>0\) but permit arbitrary common initial distribution \(\rho\in[0,1]\) and readout time \(T>0\). Let \(z_*\in(0,1)\) be the unique solution of
\[
\boxed{z_*+(1+H)z_*^c=H.}
\]
Then the largest single margin supporting three attainable labelings is
\[
\boxed{\gamma_*=\frac{z_*}{2},\qquad T_*=\frac{\log(1/z_*)}{4k\cosh(f/2)}.}
\]
The margin is attained **only** at \(T=T_*\) with either \(\rho=0\) or \(\rho=1\). The three control settings can be chosen as \(\theta=0\) for the constant labeling and \(\theta=\pm b\) for copying and inversion. Thus finite preparation memory increases task count from two to three, but attempting three tasks indefinitely is impossible because initial bias relaxes away.

**Weak-driving endpoint law.** With \(b>0\) fixed, let \(f\downarrow0\), equivalently \(H\downarrow0\) with fixed \(c>1\). The optimum obeys
\[
\boxed{z_*=H-H^c+o(H^c),\quad
\gamma_*=\frac H2-\frac{H^c}{2}+o(H^c),}
\]
and
\[
\boxed{T_*=\frac{1}{4k\cosh(f/2)}\left[\log(1/H)+H^{c-1}+o(H^{c-1})\right].}
\]
The correction exponent \(c=\cosh b\) is generally noninteger. In particular, \(\gamma_*\sim f\tanh b/4\) while \(T_*\sim\log(1/f)/(4k)\).

## Assumptions and scope

All four individual channel rates are positive and constant during each run. The input \(x\) influences rates but not the common initial preparation \(\rho\), the observation time \(T\), or the chosen control interval. The control may be retuned between classification tasks but not separately for the two input values within a task. A margin is imposed on ensemble-average terminal occupation, not on a single stochastic trajectory. Only one terminal observation is used; no feedback or intermediate intervention occurs. No assertion is made for input-dependent preparations, other graph topologies, more than two inputs, or arbitrary time-dependent controls.

The model and uniform-preparation baseline come from Aslyamov and Esposito (2026), equations (27), (28), and (32). The present exact task count, joint preparation/readout optimum, and weak-driving boundary law concern the **nonuniform common preparation** not analyzed in their switch example. The rates and normalization are kept unchanged.

## Proof

**1. Direct two-state evolution.** Summing the channels gives the forward and reverse total rates
\[
u=2k\cosh(\theta+fx/2),\qquad v=2k\cosh(\theta-fx/2).
\]
Their sum is \(u+v=4k\cosh\theta\cosh(f/2)=:\lambda(\theta)\), while the instantaneous stationary probability of state one is
\[
\frac{u}{u+v}=\frac12+\frac x2\tanh\theta\tanh(f/2).
\]
The scalar forward equation \(\dot q=u-(u+v)q\), with \(q(0)=1/2+\delta\), therefore gives for every \(\theta,x,T\)
\[
\boxed{q(\theta,x;T)-\tfrac12=\delta e^{-\lambda(\theta)T}+\frac x2\tanh\theta\tanh(f/2)(1-e^{-\lambda(\theta)T}).}\tag{1}
\]
This remains valid at deterministic preparations \(\rho=0\) and \(\rho=1\). The first term is input-independent transient memory; the second is input-antisymmetric steady-state response modified by relaxation.

**2. Exact attainability of each labeling.** Write \(m(\theta)=\delta e^{-\lambda(\theta)T}\) and \(s(\theta)=\tfrac12\tanh\theta\tanh(f/2)(1-e^{-\lambda(\theta)T})\). The centered responses at inputs \(+1\) and \(-1\) are \(m+s\) and \(m-s\), respectively. For \(\theta\ge0\), \(s(\theta)\) is strictly increasing: both factors \(\tanh\theta\) and \(1-e^{-a\cosh\theta}\) are nonnegative and increasing, and the former is strictly so. Also \(|m(\theta)|=|\delta|e^{-a\cosh\theta}\) decreases. Both copying inequalities hold exactly when \(s(\theta)-|m(\theta)|\ge\gamma\). Thus copying is possible exactly when this expression at \(\theta=b\) is at least \(\gamma\), which is \(B\ge\gamma\). For \(\theta<0\), copying is impossible because \(s<0\). Reflection \(\theta\mapsto-\theta\) similarly shows inversion is possible exactly when \(B\ge\gamma\), with optimum at \(-b\).

For constant-plus classification, the smaller centered response is \(m(\theta)-|s(\theta)|\). It cannot be positive if \(\delta\le0\), and if \(\delta>0\), it is maximized at \(\theta=0\), with value \(\delta e^{-a}\). Constant-minus classification similarly requires \(\delta<0\) and has largest margin \(-\delta e^{-a}\). Hence only the constant matching the sign of the initial bias can occur, and precisely if \(C\ge\gamma\). This proves the task-count formula, all equality cases, and the impossibility of four tasks.

**3. Joint optimization.** Put \(d=|\delta|\in[0,1/2]\), \(z=e^{-a}\in(0,1)\), and \(S(z)=\tfrac H2(1-z^c)>0\). The simultaneous margin for all three labelings, allowing a negative value to indicate infeasibility, equals
\[
G(d,z)=\min\{dz,\ S(z)-dz^c\}.
\]
For fixed \(z\), the first argument increases strictly in \(d\), whereas the second decreases strictly. Their crossing is at \(d_0=S(z)/(z+z^c)\). If \(d_0\le1/2\), the maximizer is \(d_0\), with value \(S(z)/(1+z^{c-1})\). Otherwise the maximizer is \(d=1/2\), with value \(z/2\). Thus
\[
\max_{0\le d\le1/2}G(d,z)=
\begin{cases}
\displaystyle\frac{H(1-z^c)}{2(1+z^{c-1})},& z+(1+H)z^c\ge H,\\[5pt]
\displaystyle z/2,& z+(1+H)z^c\le H.
\end{cases}\tag{2}
\]
The function \(z+(1+H)z^c\) is strictly increasing from zero to \(2+H\) as \(z\) varies from zero to one. Hence there is exactly one \(z_*\in(0,1)\) giving equality to \(H\). As physical time increases, \(z\) decreases. In the first branch of (2), the numerator strictly increases while the denominator strictly decreases, so the optimized margin strictly increases with time. In the second branch it is \(z/2\), strictly decreasing with time. Its global maximum occurs only at \(z_*\). There \(d_0=1/2\), establishing the two deterministic initial preparations and the unique time in the statement.

**4. Singular weak-driving expansion.** At fixed \(c>1\), the root equation implies \(0<z_*<H\) and \(0<H-z_*=(1+H)z_*^c\le(1+H)H^c\). Consequently \(z_*/H\to1\), so \(z_*=H-H^c+o(H^c)\). Taking a logarithm yields \(\log(1/z_*)=\log(1/H)+H^{c-1}+o(H^{c-1})\). Substitution gives all displayed weak-driving formulas. These steps prove an asymptotic result for a continuum of positive driving parameters, not a finite enumeration.

## Verification

A dependency-free verification program, `verify.py`, reconstructs the jump rates independently, solves the two-state forward equation, checks the population identity on parameter grids, enumerates all four labelings on dense control grids, verifies the unique defining root and the global upper bound across preparation/time grids, and probes the fractional-power weak-driving law. Run it with `python3 verify.py` from the package directory; it prints its actual assertion total and raises an exception on failure. Exact globality, uniqueness, and asymptotics rest on the proof above, not on the finite tests. A representative design with \(k=b=f=1\) has \(z_*\approx0.2206514321\), \(T_*\approx0.3350337567\), and \(\gamma_*\approx0.1103257160\).

## Relationship to prior work

Aslyamov and Esposito, *Physical limits to stochastic classifiers* (arXiv:2610.20481v1, October 14, 2026), introduce the two-channel kinetic switch and prove the exact margin for copying/inversion under **uniform preparation**; their equation (28) then has no constant shift, and their equation (32) optimizes over control with the preparation and readout duration held fixed. The present nonuniform-preparation problem is not that result with parameters renamed: it creates a third attainable labeling and requires a joint minimax optimization over an initially biased state and a relaxation time. Equation (1) uses their same rate model, which is acknowledged as prior art rather than new physics.

Floyd, Dinner, Murugan, and Vaikuntanathan, *Limits on the computational expressivity of non-equilibrium biophysical processes* (arXiv:2409.05827v1; later Nature Communications 16, 7184), prove constraints on classification by **steady-state** occupations in broader networks; arbitrary initial bias and an optimal finite readout time are inapplicable to that steady-state framework. General two-state Markov relaxation is elementary prior knowledge; the evaluated contribution is the sharp task-count classification and globally optimized three-task margin for this motivated switch, together with its singular weak-driving design law. A specialization hidden in earlier general transient-classification work cannot be excluded without exhaustive human literature review.

## Limitations

The three-task result is specific to two inputs, the stated two-channel switch, one common state preparation, one fixed shared control per labeling, a fixed threshold \(1/2\), and an ensemble-mean margin. Allowing input-specific initialization, input-specific controls, feedback, or a different graph changes the capacity question. The optimal preparation is deterministic and may have physical preparation costs not counted in the margin. The result does not quantify entropy production, single-run classification error, or the cost of waiting, and does not claim a universal three-task bound for general stochastic classifiers. The exact optimizer is a mathematical design optimum for this Markov idealization; experimental realization and literature-wide priority have not been established.

## References

1. T. Aslyamov and M. Esposito, *Physical limits to stochastic classifiers*, arXiv:2610.20481v1 (first submitted October 14, 2026), https://arxiv.org/html/2610.20481v1. See the two-channel switch, equations (27)–(32), and Appendix C.
2. C. Floyd, A. R. Dinner, A. Murugan, and S. Vaikuntanathan, *Limits on the computational expressivity of non-equilibrium biophysical processes*, arXiv:2409.05827v1 (September 9, 2024), https://arxiv.org/html/2409.05827v1; Nature Communications 16, 7184 (2025). See the steady-state occupation and network-expressivity formulation.
