# A harvesting-feasibility barrier to predator persistence in an Allee impulsive fishery

## Finding
For the Xu–Zou predator–prey model with a weighted state-dependent harvest and no predator restocking, a strictly positive predator population cannot be periodic at **any** order if the accessible prey range lies below the predator's break-even feeding level. More precisely, if
\[
\delta:=\mu-\frac{ea(h_l/\eta)}{1+aq(h_l/\eta)}>0,
\]
then every feasible positive solution satisfies
\[
0<y(t)\le y(0)e^{-\delta t}(1-p_2E_l)^{N(t)}\le y(0)e^{-\delta t}.
\]
Here \(N(t)\) counts harvesting events by time \(t\). Hence no strictly positive equilibrium or positive periodic orbit of any impulse order can exist.

This barrier can hold even when the unharvested equations have two distinct positive coexistence equilibria and all three explicit inequalities in case (1) of Xu and Zou's Theorem 2.2 hold. The exact parameter witness given below has \(\delta=5/12\), the coexistence equilibria \((5,1)\) and \((20/3,7/9)\), and \(p_2=1/100<\bar p_2=1/19\). Thus that theorem's case (1) cannot guarantee a **strictly positive** order-one cycle, as its accompanying proof seeks to establish. The literal phrase “an order-1 periodic solution” is ambiguous because a predator-free order-one cycle already exists here; the finding explicitly does **not** deny that semitrivial cycle.

## Assumptions and scope
Prey density \(x\) and predator density \(y\) evolve while \(H=\eta x+(1-\eta)y<h_l\) under
\[
\dot x=rx(1-x/K)-\frac{axy}{1+aqx},\qquad
\dot y=y\left(\frac{eax\psi(y)}{1+aqx}-\mu\right).
\]
At first hitting of \(H=h_l\), the harvest jump is
\[
x^+=(1-p_1E_l)x^-,\qquad y^+=(1-p_2E_l)y^-+\tau_l.
\]
Assume \(r,K,a,q,e,\mu,\eta,h_l,E_l,p_1,p_2>0\), \(0<e<1\), \(0<\eta<1\), \(0<p_iE_l<1\) for \(i=1,2\), and \(\tau_l=0\). The Allee function \(\psi:[0,\infty)\to[0,1]\) is continuous and locally Lipschitz, as in the motivating work (which additionally assumes increasing concavity and \(\psi(0)=0\)). Solutions start with \(x(0),y(0)>0\) and \(H(0)<h_l\). We interpret pulses as first outward hits from within the feasible triangle; no pulse is applied at an interior point.

For the rational witness choose
\[
r=2,\ K=10,\ a=2,\ q=1/10,\ e=1/2,\ \mu=5/4,\quad
\eta=1/2,\ h_l=1/2,\ E_l=1,\ p_1=1/2,\ p_2=1/100,\ \tau_l=0,
\]
with \(\psi(y)=y/(1+y)\), which obeys all three source Allee conditions.

## Proof
**Invariant triangle and positive solutions.** Between harvests, the feasible triangle \(x\ge0,\ y\ge0,\ H\le h_l\) gives \(0\le x\le h_l/\eta\) and \(0\le y\le h_l/(1-\eta)\). Both differential equations contain their respective density factors, so strictly positive coordinates remain strictly positive over every finite flow segment. A pulse with \(\tau_l=0\) multiplies each coordinate by a positive number below one. Consequently
\[
H^+\le\kappa h_l,\qquad\kappa=\max(1-p_1E_l,1-p_2E_l)<1.
\]
On the compact feasible triangle, \(\dot H\) is uniformly bounded in absolute value by some finite \(M\). Any two consecutive pulses are therefore separated by at least \((1-\kappa)h_l/\max\{1,M\}>0\). There are no finite-time pulse accumulations. Smooth local flow and boundedness on the triangle then extend every feasible positive hybrid solution for all \(t\ge0\).

**Global predator decay.** The Holling feeding factor \(f(x)=ax/(1+aqx)\) is strictly increasing for \(x\ge0\). As \(x\le h_l/\eta\) and \(0\le\psi(y)\le1\), the continuous logarithmic predator growth satisfies
\[
\frac{d}{dt}\log y=e\psi(y)f(x)-\mu\le e f(h_l/\eta)-\mu=-\delta.
\]
Integration over each flow leg contributes at most \(e^{-\delta\Delta t}\); each pulse contributes the exact multiplier \(1-p_2E_l\) to \(y\). Multiplying yields the displayed global bound. A strictly positive periodic orbit would have \(y(t+T)=y(t)>0\) for some \(T>0\), contradicting the strict exponential decrease. A positive equilibrium would contradict \(\dot y<0\) even without pulses. This proves the full quantified statement.

**Exact witness.** For the selected parameters, the prey nullcline at positive \(x\) is
\[
y=(1-x/10)(1+x/5).
\]
Substitution into the positive-predator nullcline gives the quadratic \(3x^2-35x+100=(x-5)(3x-20)=0\), with the two strictly positive equilibria
\[
(x_1^*,y_1^*)=(5,1),\qquad (x_2^*,y_2^*)=(20/3,7/9).
\]
The smaller-prey coexistence equilibrium has harvest weight \(h^*=\eta x_1^*+(1-\eta)y_1^*=3\), whereas \(\eta K=5\). Therefore \(h_l=1/2\le\min\{h^*,\eta K\}\). The source's parameter \(\bar p_2=p_1h_l/[\eta K-(1-p_1E_l)h_l]\) equals \(1/19\), and \(0<p_2=1/100<1/19\). Also \(\tau_l=0\). All the explicit hypotheses in Theorem 2.2(1) are met. Yet \(h_l/\eta=1\), so
\[
\frac{ea(h_l/\eta)}{1+aq(h_l/\eta)}=\frac56<\frac54=\mu,
\qquad\delta=\frac5{12}.
\]
Hence no positive order-one cycle, indeed no positive periodic cycle of any order, is possible at these parameters. The two positive equilibria of the **unharvested** ODE lie outside the accessible harvest triangle: each has \(x>1\).

## Verification
The included `verify.py` uses Python standard-library exact fractions. Running `python verify.py` prints `VERIFY_OK` and independently checks all numeric hypotheses, both coexistence equilibria directly in the two differential equations, their nullcline polynomial, \(h^*\), \(\bar p_2\), the impulse feasibility inequalities, and \(\delta\). The infinite-time assertion follows from the comparison proof above, **not** from finite simulation. No numerical integration, external solver, or unpublished certificate is needed.

## Relationship to prior work
Xu and Zou [1] state a case-(1) order-one existence criterion and use a successor-function argument intended to obtain a nontrivial positive orbit; the printed theorem's bare wording could also include the semitrivial orbit. The present result identifies a missing *feasible feeding* condition and proves a global no-positive-cycle barrier. A separate prior calculation concerns only the local Floquet multiplier of the predator-free periodic cycle; local stability alone cannot exclude a disjoint positive periodic orbit, so the present global bound and witness are not corollaries of that local result. Tian, Gao, and Sun [2] analyze weighted harvesting in an anti-predator system with a different predator equation; their results do not imply this precise parameter inconsistency. Xiao and Dai [3] analyze state-dependent pulses and periodic solutions for a different predator–prey model. Tian, Liu, and Sun [4] instead use an Allee effect in prey and bilateral intervention.

## Limitations
This is a deterministic mathematical statement about equations and controls, not an ecological prediction. It assumes zero predator restocking; \(\tau_l>0\) invalidates the multiplicative predator-decay argument. The barrier is sufficient, not asserted necessary or sharp. It gives no existence classification when \(\delta\le0\), no orbit stability classification, and does not refute existence of the semitrivial order-one cycle. In particular, the literal conclusion “some order-1 periodic solution” in [1] can still be true through the predator-free orbit; the contradiction is to an interpretation/construction of a **strictly positive** cycle under the printed criterion. Prior literature on general state-dependent impulses can contain broad principles not fully surveyed here; originality concerns the specific model, global obstruction, and exact counterexample rather than the elementary logarithmic-comparison technique.

## References
[1] J. Xu and T. Zou, “Dynamics of a predator-prey model with the Allee effect for the predator induced by weighted harvesting strategy,” *AIMS Mathematics* 11 (2026), 578–593, DOI: 10.3934/math.2026025, published 2026-01-08. https://www.aimspress.com/aimspress-data/math/2026/1/PDF/math-11-01-025.pdf

[2] Y. Tian, Y. Gao, and K. Sun, “A fishery predator-prey model with anti-predator behavior and complex dynamics induced by weighted fishing strategies,” *Mathematical Biosciences and Engineering* 20 (2023), 1558–1579, DOI: 10.3934/mbe.2023071. https://www.aimspress.com/aimspress-data/mbe/2023/2/PDF/mbe-20-02-071.pdf

[3] Q. Xiao and B. Dai, “Periodic Solutions Generated by Impulses for State-Dependent Impulsive Differential Equation,” (2015), DOI: 10.1155/2015/816325.

[4] Y. Tian, Y. Liu, and K. Sun, “Complex dynamics of a predator-prey fishery model: The impact of the Allee effect and bilateral intervention,” *Electronic Research Archive* 32 (2024), 6379–6404, DOI: 10.3934/era.2024297.

[5] Q. Zhu, H. Wang, and Z. Ouyang, “The state-dependent impulsive control for a general predator-prey model,” (2021), DOI: 10.1080/17513758.2021.1937721. Related general framework; complete primary text was not accessible during the comparison.
