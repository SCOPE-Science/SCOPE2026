# Exact mean–variance law and maturation-delay ceiling for oscillatory coexistence
## Finding
For the delayed hunting-cooperation predator–prey system of Enatsu, Roy and Banerjee, define
\[
G(n,p)=\frac{(1+\alpha p)n}{1+h_1(1+\alpha p)n}.
\]
For every strictly positive nonconstant \(T\)-periodic solution \((n(t),p(t))\), with
\[
\bar f=\frac1T\int_0^T f(t)\,dt,
\]
one has the exact identity
\[
\bar p=\sigma e^{-\beta\tau}\left(\bar n-\frac{\overline{n^2}}{\kappa}\right)
=\sigma e^{-\beta\tau}\left[\bar n\left(1-\frac{\bar n}{\kappa}\right)-\frac{\operatorname{Var}(n)}{\kappa}\right].
\]
Therefore
\[
0<\bar n<\kappa,
\qquad
0<\bar p<\frac{\sigma\kappa}{4}e^{-\beta\tau}.
\]
In addition, every such orbit must satisfy
\[
h_1e^{\beta\tau}<1.
\]
Thus \(h_1e^{\beta\tau}\ge1\) excludes strictly positive nonconstant periodic coexistence.

## Assumptions and scope
The parameters \(\sigma,\kappa,\alpha,h_1,\beta\) are positive, \(\tau\ge0\), and the solution is a classical strictly positive \(T\)-periodic solution of the source's delayed system (15). No commensurability between \(T\) and \(\tau\) is assumed. The result is a necessary constraint on positive periodic solutions; it does not prove that a periodic solution exists for any parameter choice.

## Proof
The source model can be rewritten as
\[
\dot n=\sigma n\left(1-\frac n\kappa\right)-G(n,p)p,
\]
\[
\dot p=e^{-\beta\tau}G(n(t-\tau),p(t-\tau))p(t-\tau)-p(t).
\]
Integrating the predator equation over one period and using periodicity to shift the delayed integrand gives
\[
0=e^{-\beta\tau}\overline{Gp}-\bar p,
\qquad
\overline{Gp}=e^{\beta\tau}\bar p.
\]
Integrating the prey equation over the same period gives
\[
0=\sigma\bar n-\frac{\sigma}{\kappa}\overline{n^2}-\overline{Gp}.
\]
Substitution yields
\[
\bar p=\sigma e^{-\beta\tau}\left(\bar n-\frac{\overline{n^2}}{\kappa}\right).
\]
Since \(\overline{n^2}=\bar n^2+\operatorname{Var}(n)\), the mean–variance form follows.

A nonconstant periodic solution must have nonconstant prey. Indeed, if \(n(t)\equiv n_0>0\), then the prey equation forces
\[
\Phi(p(t))=\frac{p(t)(1+\alpha p(t))}{1+h_1n_0(1+\alpha p(t))}
\]
to be constant. Its derivative is
\[
\Phi'(p)=\frac{(1+h_1n_0)(1+2\alpha p)+h_1n_0\alpha^2p^2}{[1+h_1n_0(1+\alpha p)]^2}>0,
\]
so \(p(t)\) is also constant. Hence for a nonconstant periodic orbit \(\operatorname{Var}(n)>0\). Because \(\bar p>0\), the exact balance then implies \(0<\bar n<\kappa\) and
\[
\bar p<\sigma e^{-\beta\tau}\bar n\left(1-\frac{\bar n}{\kappa}\right)
\le \frac{\sigma\kappa}{4}e^{-\beta\tau}.
\]
Finally, for positive \(n,p\),
\[
0<G(n,p)=\frac{(1+\alpha p)n}{1+h_1(1+\alpha p)n}<\frac1{h_1}.
\]
Therefore the integrated predator equation gives
\[
e^{\beta\tau}\bar p=\overline{Gp}<\frac{\bar p}{h_1}.
\]
Since \(\bar p>0\), this is exactly \(h_1e^{\beta\tau}<1\).

## Verification
The symbolic checker `verify.py` reconstructs the interaction term, verifies the algebraic cancellation between the two population equations, verifies the variance decomposition and logistic ceiling, and verifies positivity of \(\Phi'(p)\). It also checks the strict bound \(G<1/h_1\) symbolically after clearing positive denominators. Its stored output is `VERIFY_OK`.

The proof itself is analytic. No finite simulation is used to infer existence or nonexistence beyond the stated integral obstruction.

## Relationship to prior work
The 2024 source introduces the delayed system, studies equilibria and their local stability, and reports delay-induced oscillatory coexistence and eventual collapse of coexistence as maturation delay grows. It does not state the period-mean cancellation above in the material inspected. The exact identity here turns that qualitative delay effect into a finite-amplitude quantitative ceiling: every positive nonconstant cycle has mean predator density strictly below \(\sigma\kappa e^{-\beta\tau}/4\), independently of cooperation strength \(\alpha\) and depending on handling time \(h_1\) only through the separate necessary condition \(h_1e^{\beta\tau}<1\).

A 2025 paper with a closely related title studies a different model in which the delay is placed in the prey logistic term rather than in delayed predator recruitment; its Hopf and period-doubling results therefore do not imply this identity. A 2021 nonautonomous fear/refuge/cooperation model proves existence of positive periodic solutions for a different seasonally forced system, but the available material inspected does not provide this source-specific mean–variance law.

## Limitations
The theorem is only a necessary condition for strictly positive nonconstant periodic solutions of the printed delayed model. It does not establish existence, uniqueness, orbital stability, Hopf direction, or global persistence. The originality search is necessarily non-exhaustive, and an equivalent short averaging argument could exist in unindexed literature. No claim is made for nonperiodic recurrent dynamics in the delay phase space.

## References
1. Y. Enatsu, J. Roy, M. Banerjee, *Hunting cooperation in a prey–predator model with maturation delay*, Journal of Biological Dynamics 18 (2024), article 2332279. DOI: 10.1080/17513758.2024.2332279. Published online 22 March 2024.
2. C. Peng, J. Jiang, *Dynamical Regimes in a Delayed Predator–Prey Model with Predator Hunting Cooperation: Bifurcations, Stability, and Complex Dynamics*, Modelling 6 (2025), 84. DOI: 10.3390/modelling6030084.
3. P. K. Tiwari, M. Verma, S. Pal, Y. Kang, A. K. Misra, *A delay nonautonomous predator–prey model for the effects of fear, refuge and hunting cooperation*, Journal of Biological Systems 29 (2021), 927–969. DOI: 10.1142/S0218339021500236.
