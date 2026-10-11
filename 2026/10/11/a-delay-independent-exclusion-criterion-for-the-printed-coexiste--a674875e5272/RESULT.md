# A delay-independent exclusion criterion for the printed coexistence equilibrium
## Finding
Consider the delayed susceptible-prey/infected-prey/predator system printed by Wu and Meng, with strictly positive parameters and refuge fractions \(0\le m,m_1<1\). Put \(q=1-m\), \(q_1=1-m_1\), and
\[
G(s)=\frac{c\alpha q_1\sqrt{s}}{1+k_1q_1\sqrt{s}}.
\]
If \(G(d_2/\beta)>d_3\), then every strictly positive equilibrium must satisfy the necessary inequality
\[
r-d_1>\frac{b+\beta}{\xi\delta q}\left(G(d_2/\beta)-d_3\right).
\]
Consequently, if the reverse weak inequality holds, the printed system has no strictly positive equilibrium for any delay \(\tau\ge0\).

For the parameter values printed in Section 7.2 of the source, this necessary inequality fails by a large exact margin. Hence the printed system has no positive equilibrium at those values for any delay. In particular, the reported point \((0.6002,0.0355,0.0971)\) is not an equilibrium of the printed equations, and local-stability or Hopf-bifurcation conclusions centered at that point cannot describe the printed model with that parameter set.

## Assumptions and scope
The printed system is
\[
\dot X_S(t)=\frac{rX_S(t-\tau)}{1+k_2Y(t-\tau)}-(b+\beta)X_S(t)X_I(t)-\frac{\alpha q_1\sqrt{X_S(t)}Y(t)}{1+k_1q_1\sqrt{X_S(t)}}-d_1X_S(t),
\]
\[
\dot X_I(t)=X_I(t)\left[\beta X_S(t)-\delta qY(t)-d_2\right],
\]
\[
\dot Y(t)=Y(t)\left[\frac{c\alpha q_1\sqrt{X_S(t)}}{1+k_1q_1\sqrt{X_S(t)}}-\xi\delta qX_I(t)-d_3\right].
\]
All population coordinates are required to be strictly positive. At an equilibrium the delayed variables equal the present variables, so the existence calculation is independent of \(\tau\).

The Section 7.2 parameter values are taken literally as the exact terminating decimals printed by the source:
\[
(r,k_2,b,\beta,\alpha,k_1,d_1,d_2,\delta,c,\xi,d_3,m_1,m)
=\left(\frac{17}{100},10,\frac12,\frac35,\frac35,1,\frac1{100},\frac9{10},\frac32,\frac{89}{100},\frac7{50},\frac15,\frac15,\frac{21}{50}\right).
\]
The claim concerns the equations and parameter values as printed. It does not identify whether the discrepancy arose from simulation code, typesetting, or a different unpublished parameterization.

## Proof
Let \((X_S,X_I,Y)\) be a strictly positive equilibrium. Dividing the infected-prey equilibrium equation by \(X_I>0\) gives
\[
\beta X_S=\delta qY+d_2,
\]
and therefore
\[
X_S>\frac{d_2}{\beta}.
\]
The function \(G\) is strictly increasing on \((0,\infty)\): writing \(t=\sqrt{s}\), one has \(G=A t/(1+Bt)\) with \(A=c\alpha q_1>0\) and \(B=k_1q_1>0\), whose derivative with respect to \(t\) is \(A/(1+Bt)^2>0\).

Dividing the predator equilibrium equation by \(Y>0\) yields
\[
X_I=\frac{G(X_S)-d_3}{\xi\delta q}.
\]
If \(G(d_2/\beta)>d_3\), monotonicity and \(X_S>d_2/\beta\) imply
\[
X_I>\frac{G(d_2/\beta)-d_3}{\xi\delta q}.
\]
Finally, dividing the susceptible-prey equilibrium equation by \(X_S>0\) gives
\[
\frac{r}{1+k_2Y}=(b+\beta)X_I+d_1+\frac{\alpha q_1Y}{\sqrt{X_S}(1+k_1q_1\sqrt{X_S})}.
\]
Because \(Y>0\), both \(r/(1+k_2Y)<r\) and the final term on the right are positive. Hence
\[
r-d_1>(b+\beta)X_I>\frac{b+\beta}{\xi\delta q}\left(G(d_2/\beta)-d_3\right),
\]
which proves the criterion.

For the Section 7.2 values, \(d_2/\beta=3/2>1\), so monotonicity gives \(G(d_2/\beta)>G(1)\). Exact arithmetic gives
\[
G(1)=\frac{89}{375},\qquad
G(1)-d_3=\frac{14}{375},\qquad
\xi\delta q=\frac{609}{5000}.
\]
Thus any positive equilibrium would have to satisfy
\[
X_I>\frac{80}{261}.
\]
The susceptible-prey balance would then require
\[
r>(b+\beta)\frac{80}{261}+d_1,
\]
but the exact difference between the printed left side and this strict lower bound is
\[
\frac{17}{100}-\frac{11}{10}\frac{80}{261}-\frac1{100}
=-\frac{1156}{6525}<0.
\]
This contradiction proves nonexistence of a strictly positive equilibrium at the printed Section 7.2 parameter set for every \(\tau\ge0\).

## Verification
A dependency-free exact-arithmetic script, `verify.py`, checks the rational identities used in the Section 7.2 contradiction. It also evaluates the infected-prey equilibrium residual at the reported point \((0.6002,0.0355,0.0971)\). With the printed decimals treated exactly,
\[
\beta X_S-\delta(1-m)Y-d_2=-\frac{624357}{1000000},
\]
so
\[
\dot X_I=-\frac{44329347}{2000000000}\ne0.
\]
This direct residual is only a consistency check; the proof above is stronger because it excludes every positive equilibrium at the printed parameter values rather than only the reported point.

## Relationship to prior work
Wu and Meng derive the equilibrium equations for this delayed system and give a general positive-equilibrium condition, then use the Section 7.2 parameter set to report the positive equilibrium \((0.6002,0.0355,0.0971)\), local stability for one delay, and a supercritical Hopf threshold near \(\tau=1.059\). The exclusion criterion above is a direct consequence of the same printed equilibrium balances but is not stated there; at the Section 7.2 parameters it rules out the prerequisite positive equilibrium entirely.

The earlier Saha–Samanta herd-behavior/refuge eco-epidemiological model is structurally related but uses a different system. It does not imply the delay-independent contradiction for the Wu–Meng equations and parameter set.

## Limitations
The result is an exact statement about the printed equations and the printed Section 7.2 parameter values. It does not invalidate the source's general equilibrium algebra or Hopf analysis for other parameter sets that actually admit a positive equilibrium. It also does not determine what parameter set or implementation, if any, generated the source's numerical figures. No claim is made about boundary equilibria, transient dynamics, or periodic solutions of a corrected or differently parameterized model.

## References
1. S.-X. Wu and X.-Y. Meng, “Dynamics of a delayed predator-prey system with fear effect, herd behavior and disease in the susceptible prey,” *AIMS Mathematics* 6 (2021), 3654–3685. DOI: 10.3934/math.2021218. First published 25 January 2021.
2. S. Saha and G. P. Samanta, “Analysis of a predator-prey model with herd behavior and disease in prey incorporating prey refuge,” *International Journal of Biomathematics* 12 (2019). DOI: 10.1142/S1793524519500074.
