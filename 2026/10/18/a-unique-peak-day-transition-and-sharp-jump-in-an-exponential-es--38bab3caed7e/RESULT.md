# A unique peak-day transition and sharp jump in an exponential-escape discrete SIR model

## Finding

For the fully specified mass-conserving discrete-time SIR system below, the cumulative fraction ever infected **at the earliest global maximum of infection prevalence** has exactly one downward jump as the transmission strength increases over the stated interval. This is an exact peak-day transition, not an observed finite-time fluctuation.

Set \(q=\exp(-\lambda/4)\), \(q\in[1/4,1/2]\), and define
\[
F(q)=18q-7-12q^{9/2-3q}.
\]
There is exactly one \(q_*\in(1/4,1/2)\) satisfying \(F(q_*)=0\). Let \(\lambda_*=-4\log q_*\). For \(4\log2\leq\lambda<\lambda_*\), the unique prevalence peak is on day \(2\); for \(\lambda_*<\lambda\leq8\log2\), it is on day \(1\). At \(\lambda=\lambda_*\), days \(1\) and \(2\) tie at the global maximum, and no other day ties.

Writing \(H(\lambda)=1-S_{t_*}(\lambda)\), where \(t_*\) is the **earliest** global prevalence-peak day, gives the exact branch formula
\[
H(\lambda)=\begin{cases}
1-\frac34q^{9/2-3q},&q>q_*,\\
1-\frac34q,&q\leq q_*.
\end{cases}
\]
The strictly downward jump as \(\lambda\) increases through \(\lambda_*\) is
\[
J=\lim_{\lambda\uparrow\lambda_*}H(\lambda)
-\lim_{\lambda\downarrow\lambda_*}H(\lambda)
=\frac7{16}-\frac{3q_*}{8}>\frac14.
\]
(The upward/downward arrows indicate approaches to \(\lambda_*\) from the lower/higher transmission side, respectively.) Numerically \(q_*\approx0.436005299103462\), \(\lambda_*\approx3.320403527199752\), and \(J\approx0.273998012836202\). The one-sided values are approximately \(0.946994038508605\) and \(0.672996025672404\). These decimals are illustrations; the preceding root characterization and inequalities are exact.

## Assumptions and scope

The state is \((S_t,I_t,R_t)\), with nonnegative fractions summing to one. Define the synchronous exponential-escape update for all integers \(t\geq0\):
\[
\begin{aligned}
S_{t+1}&=S_t e^{-\lambda I_t},\\
I_{t+1}&=\tfrac12 I_t+S_t(1-e^{-\lambda I_t}),\\
R_{t+1}&=R_t+\tfrac12 I_t,
\end{aligned}
\qquad (S_0,I_0,R_0)=(\tfrac34,\tfrac14,0).
\]
The transmission strength satisfies \(4\log2\leq\lambda\leq8\log2\); the recovery fraction is exactly \(1/2\) each period. Newly infected individuals enter the infectious class at the next census, and half of previously infectious individuals leave it at each update. This is a discrete-time mass-action **exponential escape** map, not forward Euler's method or a finite stochastic contact-network simulation. Susceptible density decreases strictly, infected density remains positive, total mass is exactly preserved, and recovered density increases. The proxy \(H\) is the share ever infected by the census at the earliest prevalence peak; it is not a vaccination coverage threshold or a claim about real-world herd protection.

## Proof

**Exact reduction to two peak candidates.** Set \(q=e^{-\lambda/4}\in[1/4,1/2]\). The first census values are
\[
S_1=\tfrac34q,\quad I_1=\tfrac78-\tfrac34q,\quad R_1=\tfrac18.
\]
In particular \(I_1\geq1/2>I_0=1/4\). Because \(\lambda=-4\log q\), the next susceptible fraction is
\[
S_2=\tfrac34q\exp(-\lambda I_1)
=\tfrac34q^{9/2-3q}.
\]
On the stated interval \(9/2-3q\geq3\), so \(S_2\leq3q^3/4\). The elementary function \(-q^3\log q\) is strictly increasing on \([1/4,1/2]\), since its derivative is \(q^2(-3\log q-1)>0\) there. Consequently
\[
\lambda S_2\leq-3q^3\log q\leq\tfrac38\log2<\tfrac12.
\]
For every \(t\geq2\), \(S_t\leq S_2\) and \(1-e^{-x}\leq x\) for \(x\geq0\), hence
\[
I_{t+1}-I_t=S_t(1-e^{-\lambda I_t})-\tfrac12I_t
\leq(\lambda S_2-\tfrac12)I_t<0.
\]
Therefore \(I_1\) or \(I_2\), and no other time, attains the global maximum.

**Unique switch.** Direct subtraction gives
\[
16(I_2-I_1)=18q-7-12q^{9/2-3q}=F(q).
\]
The endpoint signs are \(F(1/4)<0\) because \(18/4-7<0\), and \(F(1/2)=1/2>0\). To prove strict monotonicity rather than rely on a plotted curve, write \(\kappa=9/2-3q\geq3\). Then
\[
F'(q)=18-12q^\kappa\left(\frac\kappa q-3\log q\right).
\]
For \(0<q\leq1/2\), \(q^\kappa\leq q^3\), \(\kappa/q\leq9/(2q)\), and \(q^3\log(1/q)\leq(\log2)/8\); the last inequality follows because its derivative is \(q^2(3\log(1/q)-1)>0\). Thus
\[
F'(q)\geq 18-12\left(\tfrac92q^2+3q^3\log(1/q)\right)
\geq\tfrac92(1-\log2)>0.
\]
There is precisely one root \(q_*\). The sign of \(I_2-I_1\) is positive for \(q>q_*\) (equivalently \(\lambda<\lambda_*\)) and negative for \(q<q_*\). At the root it is zero, yielding exactly two tied days.

**Exact jump.** At the tie, the second-period infections equal the recoveries from the first infectious census:
\[
S_1-S_2=\tfrac12I_1=\tfrac7{16}-\tfrac{3q_*}{8}.
\]
Because \(S_2<S_1\), switching the measured peak day from \(2\) to \(1\) produces a downward discontinuity in \(1-S_{t_*}\) of exactly this amount. Since \(q_*<1/2\), the jump is strictly larger than \(1/4\). The explicit branch values follow from the formulas for \(S_1,S_2\); continuity of each branch proves the claimed one-sided limits.

## Verification

Run `python3 VERIFY.py` using Python's standard library. The script separately derives the first two census states with exact rational arithmetic, locates the unique root using high-precision decimal bisection, checks the jump identity, and tests the derivative and monotone-tail inequalities on \(401\) parameter values. The final script prints **3052 passed arithmetic assertions**, including mass balance, trajectories, and the precise critical-decimal bracket. Tests on finitely many values supplement rather than replace the proof of the universal and infinite-time statements above.

As an exact endpoint witness, \(q=1/2\) gives \((S_1,I_1)=(3/8,1/2)\) and \((S_2,I_2)=(3/32,17/32)\), so the maximum is on day \(2\) and \(H=29/32\). At \(q=1/4\), \((S_1,I_1)=(3/16,11/16)\); the peak is on day \(1\) and \(H=13/16\). Thus increasing transmission from \(4\log2\) to \(8\log2\) lowers the peak-time cumulative exposure fraction even at these explicitly verifiable endpoints.

## Relationship to prior work

Ozbay, Nielsen and Nguyen [1] established through finite network simulations and an Euler-discretized deterministic SIR comparison that peak-time cumulative exposure can display transmission-dependent gaps and nonmonotonicity. Their numerical peak-day mechanism is acknowledged; neither the qualitative phenomenon nor the HIT observable is claimed as new. Their deterministic discretization uses Euler updates, not the positive exponential-escape transition specified here. The assessed contribution is the complete **rigorous one-switch classification on an explicit parameter interval**, with a unique root equation and nonzero exact jump amplitude for a positive mass-conserving exponential-escape model.

Diekmann, Othmer, Planqué and Bootsma [2] developed a general discrete-time Kermack–McKendrick framework, including an exponential susceptible escape law and geometric infectious survival. The model structure is therefore established prior art. Their main comparisons concern incidence-peak sizes and generation-time assumptions rather than a theorem on this peak-prevalence timing transition and its exact cumulative-exposure jump. This result does not infer priority from lack of a text match and may be covered by broader, as-yet-unlocated general theory.

## Limitations

This theorem fixes one initial condition, one recovery fraction and a finite transmission interval. It does not classify every peak-day transition in the full parameter space, does not apply to Euler discretization, nor predict stochastic network-level HITs or optimal public-health policy. The abrupt change is in the *time-indexed measured cumulative-exposure proxy*; the underlying state at each fixed census depends continuously on transmission. A tie convention is specified explicitly. Both cited works anticipate the qualitative bifurcation mechanism, and independent priority checking remains appropriate.

## References

[1] S. A. Ozbay, B. F. Nielsen, and M. M. Nguyen. *Bifurcations in the Herd Immunity Threshold for Discrete-Time Models of Epidemic Spread.* First arXiv public release 14 December 2022, arXiv:2212.06995. https://arxiv.org/abs/2212.06995

[2] O. Diekmann, H. G. Othmer, R. Planqué, and M. C. J. Bootsma. *On discrete time epidemic models in Kermack–McKendrick form.* medRxiv, 26 March 2021, doi:10.1101/2021.03.26.21254385. https://www.medrxiv.org/content/10.1101/2021.03.26.21254385v1.full . Published as *The discrete-time Kermack–McKendrick model: A versatile and computationally attractive framework for modeling epidemics*, PNAS 118 (2021), e2106332118.
