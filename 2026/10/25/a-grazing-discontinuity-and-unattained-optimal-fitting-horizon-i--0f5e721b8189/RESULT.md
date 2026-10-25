# A grazing discontinuity and unattained optimal fitting horizon in affine event-triggered control

## Finding

For an exactly matched scalar integrator with affine event-triggered parameterized control, optimizing the **first inter-event duration** over every finite least-squares fitting horizon has a finite strict supremum but **no maximizer**. The obstruction is a first-contact grazing event: at one critical fitting horizon an earlier tangential contact fires, whereas arbitrarily nearby shorter fitting horizons evade that contact and fire strictly later. The resulting discontinuity is compatible with exact geometric convergence and positive uniform inter-event times.

Here is the exact theorem. Fix any \(\\(\lambda>0\)\), \(\sigma\in(0,1)\), and put \(\theta=\sqrt{\sigma/2}\in(0,1/\sqrt2)\). At each event with state \(x_k\ne0\), fit the model feedback \(-\lambda x_k e^{-\lambda\tau}\), for \(0\le\tau\le T\), by an affine control \(u_k(\tau)=a_0+a_1\tau\) minimizing the **unweighted** integral of squared errors, with the exact initial-value constraint \(a_0=-\lambda x_k\). Apply that affine control until the first \(\tau>0\) satisfying \(\lvert u_k(\tau)+\lambda x(t_k+\tau)\rvert\ge\lambda\theta\lvert x(t_k+\tau)\rvert\), and repeat with the same positive fitting horizon \(T\).

For \(z=\lambda T>0\), define
\[
 \kappa(z)=\frac{3}{z^3}\left(\frac{z^2}{2}-1+(1+z)e^{-z}\right),
 \qquad s=\lambda\tau.
\]
The coefficient \(\kappa(z)\) runs continuously and strictly decreasingly through the entire interval \((0,1)\) as \(z\) runs through \((0,\infty)\). Define
\[
 a_\theta=\frac{\theta+\sqrt{\theta(2+\theta)}}{1+\theta},\qquad
 k_\theta=\frac{1+\theta}{1+\theta+\sqrt{\theta(2+\theta)}}.
\]
Let \(s_-(k)\) be the smaller positive root of
\[
 \frac{k(1+\theta)}2s^2+(k-1-\theta)s+\theta=0,
\]
and let \(s_+(k)\) be the unique positive root of
\[
 \frac{k(1-\theta)}2s^2+(k-1+\theta)s-\theta=0.
\]
Then every inter-event duration is exactly \(s_\theta(\kappa(z))/\lambda\), where
\[
 s_\theta(k)=
 \begin{cases}
 s_-(k),&0<k\le k_\theta,\\
 s_+(k),&k_\theta<k<1.
 \end{cases}
\]
At the critical coefficient, \(s_-(k_\theta)=a_\theta\), whereas
\[
 S_\theta:=s_+(k_\theta)>a_\theta,
 \qquad
 \boxed{\displaystyle\sup_{T>0}(t_{k+1}-t_k)=\frac{S_\theta}{\lambda}}
\]
and **no finite \(T\) attains this supremum**. The critical horizon \(T_\theta\) is the unique solution to \(\kappa(\lambda T_\theta)=k_\theta\). More precisely,
\[
 \lim_{T\uparrow T_\theta}(t_{k+1}-t_k)=S_\theta/\lambda,
 \qquad
 (t_{k+1}-t_k)|_{T=T_\theta}=a_\theta/\lambda.
\]
The dimensionless supremum \(S_\theta\) is the unique positive root of
\[
 \frac{k_\theta(1-\theta)}2 S_\theta^2+
 (k_\theta-1+\theta)S_\theta-\theta=0.
\]
For every finite \(T>0\), the event state obeys \(x_{k+1}=R_Tx_k\) with \(0<R_T<1\), independently of \(k\) and of the nonzero initial condition; thus no Zeno accumulation occurs and the state converges geometrically at the events. For the same event rule, zero-order hold has duration \(\theta/[\lambda(1+\theta)]\), strictly shorter than the affine scheme at every finite horizon. Moreover,
\[
 S_\theta\sim(2+\sqrt2)\sqrt\theta,
 \qquad
 \frac{S_\theta}{\theta/(1+\theta)}\sim\frac{2+\sqrt2}{\sqrt\theta}
 \quad(\theta\downarrow0).
\]
This is a sharp horizon-design statement for this specific model and cost, not a claim about optimal controllers generally.

## Assumptions and scope

The plant is the scalar integrator \(\dot x=u\) on \(\mathbb R\) with ideal state feedback \(\gamma(x)=-\lambda x\), zero plant/model disturbance, exact feedback state access at each event, and exact arithmetic. At each reset the ideal model solves \(\dot{\hat x}=-\lambda\hat x\), initialized from the actual event state. The affine basis is \(\{1,\tau\}\) and the constrained fit is specifically the *unweighted* \(L^2([0,T])\) fit, matching equation (4) in the openly available 2024 journal formulation of Rajan--Tallapragada. This matters: the first arXiv preprint version explicitly uses a discount weight \(\delta^\tau\), not analyzed by this theorem. Its public-posting date is used solely to identify the earliest verified appearance of that source paper.

The exact initial match is \(\eta\equiv0\), an allowed setting of the endpoint inequality constraint. To embed the trigger in the source Lyapunov construction take \(V(x)=x^2/2\), \(\alpha_3(r)=\lambda r^2/2\), \(\rho_1(r)=r^2/(2\lambda)\), and \(\epsilon=0\). Young's inequality gives \(\dot V\le-\alpha_3(\lvert x\rvert)+\rho_1(\lvert e\rvert)\), and the source condition \(\rho_1(\lvert e\rvert)\ge (\sigma/2)\alpha_3(\lvert x\rvert)\) becomes exactly the threshold stated above. This result concerns strict first hitting of a **closed** threshold (equality triggers), not threshold crossing with strict inequality. Assume \(x_0\ne0\); the initial equilibrium \(x_0=0\) simply remains zero and generates no positive-time events.

## Proof

**1. Exact least-squares coefficient.** The affine fit with \(a_0=-\lambda x_k\) may be written \(u_k(\tau)=-\lambda x_k(1-c(T)\tau)\). The strictly convex one-variable objective is minimized when
\[
 c(T)=\frac{3}{T^3}\int_0^T\tau(1-e^{-\lambda\tau})\,d\tau=\lambda\kappa(\lambda T).
\]
The alternative integral representation
\[
 \kappa(z)=3\int_0^1v^2\frac{1-e^{-zv}}{zv}\,dv
\]
shows \(0<\kappa(z)<1\). The function \((1-e^{-w})/w\) is strictly decreasing for \(w>0\) (because \(e^w>1+w\)). Dominated convergence at both endpoints gives \(\kappa(0^+)=1\) and \(\kappa(\infty)=0\), proving the asserted bijection.

**2. The exact first-contact problem.** With \(s=\lambda\tau\) and \(k=\kappa(\lambda T)\), integrate the actual plant on one hold interval:
\[
 \frac{x(t_k+\tau)}{x_k}=X_k(s)=1-s+\frac{k}{2}s^2,
 \qquad
 \frac{u_k(\tau)+\lambda x(t_k+\tau)}{\lambda x_k}
 =E_k(s)=s\left(k-1+\frac{k}{2}s\right).
\]
Note the useful identity \(X_k'=-X_k+E_k\). Prior to the first event, \(\lvert E_k\rvert<\theta\lvert X_k\rvert\). Since \(X_k(0)=1\), comparison with the scalar differential inequalities \( -(1+\theta)X_k<X_k'<-(1-\theta)X_k\) proves \(X_k(s)>0\) throughout the pre-event interval and at its finite endpoint. Thus the trigger before first contact is exactly \(-\theta X_k<E_k<\theta X_k\). Its two boundary equations are respectively
\[
 k=L_\theta(s):=\frac{(1+\theta)s-\theta}{s[1+(1+\theta)s/2]},\qquad
 k=U_\theta(s):=\frac{\theta+(1-\theta)s}{s[1+(1-\theta)s/2]}.
\]
There is no trigger at time zero, since the initial error vanishes. Finite contact follows from the explicit quadratics, as analyzed next.

**3. A single negative lobe and the later positive contact.** On \(s>0\), \(L_\theta\) first increases and then decreases. Differentiating and multiplying by the positive denominator gives the derivative numerator
\[
 \theta+(1+\theta)\theta s-\frac{(1+\theta)^2}{2}s^2.
\]
Its unique positive zero is \(a_\theta\), and the maximum is precisely \(L_\theta(a_\theta)=k_\theta\). Also \(U_\theta\) strictly decreases from \(+\infty\) to \(0\); after clearing its positive denominator, its derivative numerator is
\[
 -\theta-(1-\theta)\theta s-\frac{(1-\theta)^2}{2}s^2<0.
\]
For every \(0<s<2\), \(L_\theta(s)<U_\theta(s)\), and \(a_\theta<2\). In particular \(U_\theta(a_\theta)>k_\theta\). If \(0<k<k_\theta\), the first contact is the increasing-branch solution \(L_\theta(s)=k\), strictly before \(a_\theta\); no positive-error contact can precede it because \(U_\theta(s)>k\) up to that time. At \(k=k_\theta\) the same boundary is touched tangentially at \(a_\theta\), which triggers by the non-strict threshold rule. If \(k>k_\theta\), the negative boundary is never met, and the first contact is the unique positive-error root \(U_\theta(s)=k\). Since \(U_\theta(2)=1/2<k_\theta\), this positive root is below \(2\). These facts establish the piecewise formula, including all equality cases.

**4. Optimization and nonattainment.** The lower-contact branch is strictly increasing as \(k\uparrow k_\theta\), with endpoint \(a_\theta\). The upper-contact branch is strictly decreasing as \(k\uparrow1\) and approaches \(S_\theta=U_\theta^{-1}(k_\theta)>a_\theta\) as \(k\downarrow k_\theta\) from above. Every upper-branch value is strictly below \(S_\theta\); every lower-branch value, including the grazing coefficient, is at most \(a_\theta\). Therefore \(S_\theta\) is the sharp strict supremum. Since \(k=\kappa(\lambda T)\) is a strictly decreasing bijection, the critical coefficient gives exactly one critical positive horizon, approached from below along the upper-contact branch. At that horizon the earlier grazing event is present, producing the asserted downward jump and nonattainment.

**5. Repeated events and asymptotics.** The threshold is homogeneous in \(x_k\), so the same \(k\), first-contact \(s_\theta(k)\) and state multiplier \(R_T=X_k(s_\theta(k))\) recur on every nonzero event state. The differential comparison above yields
\[
 e^{-(1+\theta)s_\theta(k)}\le R_T\le e^{-(1-\theta)s_\theta(k)}<1.
\]
Thus \(0<R_T<1\), and each event interval has the same positive length; there is no finite accumulation and \(x_k=R_T^kx_0\to0\). For zero-order hold, set \(k=0\); then \(X_0=1-s\), \(E_0=-s\), and the first contact is \(s=\theta/(1+\theta)\). The lower-contact root is strictly larger than this because \(L_\theta(\theta/(1+\theta))=0\) and \(k>0\). On the upper branch, the first positive root is also later, since at the zero-order-hold contact the affine control has \(-\theta X_k<E_k<\theta X_k\) for all \(k>0\), using \(s<2\). Finally \(k_\theta=1-\sqrt{2\theta}+O(\theta)\). Substitute \(S_\theta=C\sqrt\theta+o(\sqrt\theta)\) into its defining quadratic to obtain \(C^2/2-\sqrt2 C-1=0\); the unique positive root is \(C=2+\sqrt2\), giving the two asymptotics.

## Verification

A dependency-free Python 3 program, `verify.py`, implements the exact defining equations, both closed-form roots, the critical parameter, and event-state dynamics. It checks 143,100 strict pre-contact inequalities on deterministic test grids spanning 106 threshold choices and nine fit coefficients per threshold, tests the root identities and inequalities, and checks the dimensionless sample \(\theta=1/2\), including one-sided approach to grazing and the small-threshold law. The program prints an explicit completion marker and can be run with `python3 verify.py`.

For \(\theta=1/2\) (equivalently \(\sigma=1/2\)), the critical parameters are
\[
 k_\theta=\frac{9-3\sqrt5}{4}\approx0.572949016875,
 \qquad a_\theta=\frac{1+\sqrt5}{3}\approx1.078689325833,
 \qquad S_\theta\approx1.630974075664.
\]
The dimensionless fitting horizon is \(\lambda T_\theta\approx1.699797253526\); the zero-order-hold duration is \(1/(3\lambda)\). The program's finite checks are **not** used to certify the universal theorem or exclude all possible literature equivalents; the proof above supplies the infinite statements.

## Relationship to prior work

Rajan and Tallapragada introduce event-triggered parameterized control, constrained fitting of a model control signal and a relative actuation-error trigger; their 2024 paper proves general qualitative boundedness and non-Zeno behavior and explores fitting-horizon sensitivity numerically. The publicly accessible journal-author PDF (Sections III--V, especially equation (4), event rule (7) and the conclusion) uses the unweighted fitting cost considered here and lists analytical fitting-horizon design as a possible research direction. The original February 2024 arXiv v1 has an exponential weighting in its fit; this calculation is **not** claimed for that weighted version. A 2023 predecessor by the same authors analyzes parameterized stabilization of linear systems. Earlier planar event-triggered work studies angular dynamics of event times. None of the inspected accessible primary material establishes this scalar-affine, grazing-caused strict supremum and critical discontinuity.

The general theory of first-hit discontinuity at grazing, polynomial least-squares projection and scalar sample-and-hold stability is older and not claimed as novel separately. The contribution is their exact coupling in this horizon-design problem, including the closed-form optimizing limit and an explicit failure of attainment. The 2023 predecessor's complete full text was not accessible through attempted open sources; its possible additional special cases remain an explicit novelty risk.

## Limitations

Only the specified scalar integrator, ideal linear feedback, unweighted continuous-time constrained affine fit, equal-time reset policy, exact equality-triggering rule, zero disturbance and fixed \(\lambda\) and \(\sigma\) are covered. An arXiv version of the motivating paper uses a discounted fit; the theorem does not cover \(\delta^\tau\)-weighted fits, higher-degree bases, nonzero initial fit tolerance, quantified/noisy state feedback, hysteresis, sampled trigger checking, actuator constraints, transport delays, or numerical event-detection tolerances. Since \(T\) is a fit horizon rather than a guaranteed hold duration, actual event time may exceed \(T\) without invalidating the model. At finite numerical tolerance grazing will be delicate. The proof does not optimize a combined objective involving state decay, energy, packet length or computational cost. A distinct earlier analysis could imply some special cases despite unsuccessful searches; independent specialist validation is outstanding.

## References

1. A. Rajan and P. Tallapragada, *Event-Triggered Parameterized Control of Nonlinear Systems*, arXiv:2402.16337v1, first publicly posted 2024-02-26; https://arxiv.org/abs/2402.16337 . The February preprint uses discounted fitting.
2. A. Rajan and P. Tallapragada, *Event-Triggered Parameterized Control of Nonlinear Systems*, IEEE Control Systems Letters 8 (2024), 1673–1678, unweighted author version; https://cps.iisc.ac.in/~pavant/files/papers/J20.pdf ; DOI:10.1109/LCSYS.2024.3414290 .
3. A. Rajan and P. Tallapragada, *Event-Triggered Parameterized Control for Stabilization of Linear Systems*, IEEE CDC (2023), 3903–3910; DOI:10.1109/CDC49753.2023.10383836 .
4. A. Rajan and P. Tallapragada, *Asymptotic Behavior of Inter-Event Times in Planar Systems under Event-Triggered Control*, arXiv:2201.02090 (2022); https://arxiv.org/abs/2201.02090 .
