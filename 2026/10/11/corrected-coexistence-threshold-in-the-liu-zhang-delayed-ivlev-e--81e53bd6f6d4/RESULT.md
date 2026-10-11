# Corrected coexistence threshold in the Liu–Zhang delayed Ivlev example

## Finding
For the delayed Ivlev predator–prey model
\[
\dot x(t)=r x(t)\left(1-\frac{x(t)}K\right)-\alpha y(t)\left(1-e^{-\beta x(t)}\right),
\]
\[
\dot y(t)=-s y(t)+Y\alpha e^{-s\tau}y(t-\tau)\left(1-e^{-\beta x(t-\tau)}\right),
\]
Liu and Zhang's Section 4.1 parameters
\[
r=1,\quad K=1,\quad \alpha=5,\quad s=0.02,\quad Y=0.6,\quad \beta=0.1
\]
admit a strictly positive coexistence equilibrium exactly for
\[
0\le \tau<\tau_*=50\log\!\bigl(150(1-e^{-0.1})\bigr)
=132.923341652608\ldots.
\]
At \(\tau=\tau_*\), the coexistence formula reaches \(x^*=K=1\) and \(y^*=0\), so the positive branch terminates at the predator-free equilibrium. Thus the numerical statement in Section 4.1 that the coexistence equilibrium exists for \(\tau<250\) is not compatible with the source's own equilibrium criterion. The source's reported transcritical value \(\tau_3=132.9233\) is, to four decimals, the actual coexistence endpoint.

## Assumptions and scope
All six biological parameters are positive and \(\tau\ge0\). The finding concerns the specific parameter vector printed for system (4.2) and the positivity of the equilibrium given in Proposition 3.1. It does not alter the model equations, the Hopf calculations below the corrected coexistence endpoint, or the separate chaotic example in Section 4.2.

A coexistence equilibrium means \(x^*>0\) and \(y^*>0\). Merely having a real algebraic value of \(x^*\) is not sufficient.

## Proof
At a positive equilibrium, the predator equation gives
\[
s=Y\alpha e^{-s\tau}\left(1-e^{-\beta x^*}\right),
\]
so
\[
x^*=-\frac1\beta\log\!\left(1-\frac{s e^{s\tau}}{\alpha Y}\right).
\]
The prey equation then yields the source's formula
\[
y^*=\frac{rYx^*}{s e^{s\tau}}\left(1-\frac{x^*}K\right).
\]
Every prefactor outside the last parenthesis is positive whenever \(x^*>0\). Therefore \(y^*>0\) is equivalent to \(x^*<K\). Because \(x^*\) is strictly increasing in \(\tau\), this is equivalent to
\[
\frac{s e^{s\tau}}{\alpha Y}<1-e^{-\beta K},
\]
or
\[
\tau<\frac1s\log\!\left(\frac{\alpha Y(1-e^{-\beta K})}s\right).
\]
Substitution of the Section 4.1 parameters gives
\[
\tau_*=50\log\!\bigl(150(1-e^{-0.1})\bigr)
=132.923341652608\ldots.
\]
At equality, \(x^*=K\) and hence \(y^*=0\), establishing the branch collision.

There is a second, weaker threshold obtained only from requiring the logarithm defining \(x^*\) to remain real:
\[
\tau<\frac1s\log\!\left(\frac{\alpha Y}s\right)
=50\log(150)=250.531764704813\ldots.
\]
Between the two thresholds, \(x^*>K\) and therefore \(y^*<0\). For example, at \(\tau=250\), direct substitution gives
\[
x^*=45.4889011125\ldots,\qquad y^*=-409.077854460\ldots,
\]
so the algebraic branch there is not a positive coexistence equilibrium.

## Verification
The accompanying checker recomputes both thresholds directly from the printed parameter vector, verifies that the corrected endpoint agrees with the source's \(\tau_3=132.9233\) to four decimals, and evaluates the equilibrium formula at \(\tau=250\). The checker is arithmetic support only; the proof above establishes the positivity criterion symbolically.

## Relationship to prior work
Liu and Zhang's Proposition 3.1 states the general coexistence condition
\[
\tau<\frac1s\log\!\left(\frac{\alpha Y(1-e^{-\beta K})}s\right)
\]
and gives the formulas for \(x^*\) and \(y^*\). In Section 4.1 the same article then states that system (4.2) has a coexistence equilibrium for \(\tau<250\), while separately reporting a transcritical value \(\tau_3=132.9233\). The calculation above reconciles the general theorem with the transcritical value and shows that \(250\) cannot be the positivity threshold.

The closely related 2020 Beddington–DeAngelis delay paper uses a different predator response and a different delayed survival expression. Its inspected full text discusses local stability, paired Hopf branches, and numerical predator extinction, but does not state or imply this source-specific correction. A 2020 stage-structured Ivlev model likewise has different state variables and delays.

## Limitations
This finding corrects the admissible positive-equilibrium interval for the printed Section 4.1 example. It does not recompute the paper's Hopf frequencies, periodic orbits, or chaotic trajectories. It also does not claim that every figure point beyond the transcritical collision was numerically continued as a positive branch; the correction is to the explicit coexistence-existence and stability-interval statements.

No independent audit has been performed.

## References
1. Q. Liu and X. Zhang, “Chaos detection in predator-prey dynamics with delayed interactions and Ivlev-type functional response,” *AIMS Mathematics* 9 (2024), 24555–24575. DOI: 10.3934/math.20241196.
2. X. Zhang, R. Shi, R. Yang, and Z. Wei, “Dynamical Behaviors of a Delayed Prey–Predator Model with Beddington–DeAngelis Functional Response: Stability and Periodicity,” *International Journal of Bifurcation and Chaos* 30 (2020), 2050244. DOI: 10.1142/S0218127420502442.
3. D. Hu, Y. Li, M. Liu, and Y. Bai, “Stability and Hopf bifurcation for a delayed predator–prey model with stage structure for prey and Ivlev-type functional response,” *Nonlinear Dynamics* 99 (2020), 3323–3350. DOI: 10.1007/s11071-020-05467-z.
