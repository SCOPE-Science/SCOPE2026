# The exact cost frontier for one-shot social-norm seeding

## Finding
A single intervention which purchases silent support and vocal advocacy has an exact, generally unattained cost threshold for triggering a social-norm outbreak. For all \(\beta>\gamma>0\) and all strictly positive marginal seeding costs, the unique limiting cost-optimal seed changes from a mixed silent/vocal allocation to an all-vocal allocation at an explicit marginal-cost ratio. A Lambert-W threshold occurs when \(\beta=1\). All claims concern one-time modification of the initial fractions in the unforced social-norm system, not ongoing control.

Write \(r=\gamma/\beta\in(0,1)\), \(\lambda=c_s/c_v>0\), and define \(g:[0,r]\to[0,\infty)\) by
\[
 g(x)=\begin{cases}
 1-r+(1-x)\bigl(\log\frac{1-x}{1-r}-1\bigr),&\beta=1,\\
 1-r+\frac{\beta(1-x)-(1-r)^{1-\beta}(1-x)^\beta}{1-\beta},&\beta\ne1.
 \end{cases}
\]
There is a unique \(a\in(0,r)\) with \(g(a)=a\). Define \(\lambda_c=-g'(a)>0\). When \(0<\lambda<\lambda_c\), put
\[
 t_\lambda=\begin{cases}e^\lambda,&\beta=1,\\
 \bigl(1+(\beta-1)\lambda/\beta\bigr)^{1/(\beta-1)},&\beta\ne1,
 \end{cases}\qquad
 x_*=1-(1-r)t_\lambda,\qquad y_*=g(x_*).
\]
Then \(a<x_*<r\), \(0<y_*<x_*\), and the sharp cost is \(C_*=c_sx_*+c_vy_*\). When \(\lambda\ge\lambda_c\), the optimal limiting seed is instead \((x_*,y_*)=(a,a)\), with \(C_*=(c_s+c_v)a\). This is the unique minimizer among all *non-successful boundary seeds* against which success can be approached.

For any fixed budget \(B\ge0\), there is an initially feasible seed \((x,y)\) costing at most \(B\) and converging to full support \((1,1-r)\) **if and only if** \(B>C_*\). In particular, exactly \(B=C_*\) is insufficient: the infimum is not attained by a successful intervention.

At \(\beta=1\), define \(w=W_0(r/(1-r))\), the positive principal real Lambert-W value. Then \(\lambda_c=w\) and \(a=1-r/w\). In the mixed regime,
\[
 \frac{C_*}{c_v}=\lambda+(1-r)(1-e^\lambda).
\]
For \(r=1/2\), the phase transition is exactly \(\lambda_c=W_0(1)\approx0.5671432904097838\). At \(\lambda=1/5\), \((x_*,y_*)\approx(0.3892986209199151,0.0114388967359320)\), with \(C_*/c_v\approx0.0892986209199150\). At \(\lambda=1\), \(x_*=y_*\approx0.1183885828240517\) and \(C_*/c_v\approx0.2367771656481033\).

## Assumptions and scope
The three population fractions are non-supporters \(1-x\), silent supporters \(x-y\), and vocal advocates \(y\). After a single instantaneous intervention at time zero, they evolve under
\[
 \dot x=(1-x)y,\qquad \dot y=\beta y(x-y-r),\qquad 0\le y\le x\le1,
\]
with real \(\beta>0\), \(\gamma>0\), and \(r=\gamma/\beta<1\). Initially no one supports the norm; intervention chooses any physically admissible initial \((x,y)\), paying \(c_s>0\) per unit of total newly seeded support and a further \(c_v>0\) per unit of vocal advocacy. Interventions do not modify the dynamics thereafter. Success means convergence to the positive-outbreak equilibrium \((1,1-r)\), not merely temporary growth or approach to the critical saddle. The infimum ranges over all continuous population fractions, with no integral-person constraint.

## Proof
**1. Exact outcomes.** The triangle \(0\le y\le x\le1\) is forward invariant: \(y=0\) is invariant, \(x=1\) has zero outward flux, and on \(y=x>0\), \(\dot y-\dot x=-y[\beta r+1-x]<0\). For positive \(y\), the differential quotient is
\[
 \frac{dy}{dx}=\frac{\beta(x-r-y)}{1-x}.
\]
The function \(g\) above solves this linear differential equation, with \(g(r)=0\), so
\[
 Q(x,y)=\frac{y-g(x)}{(1-x)^\beta}
\]
is constant along trajectories while \(x<1\), \(y>0\). This first integral and the phase-separating curve are already established by Wang et al.; they are recalled to derive the new cost optimization, not presented as independently novel dynamics.

If an orbit with \(y(0)>0\) has \(x(t)\to x_\infty<1\), integration of \(\dot x/(1-x)=y\) gives \(\int_0^\infty y(t)dt<\infty\). Boundedness and uniform continuity of \(y\) imply \(y(t)\to0\). Also \(x_\infty\le r\), for otherwise \(\dot y/y\) would eventually be bounded below by a positive constant. As \(g(x)>0\) on \([0,r)\), conservation of \(Q\) now proves: an initial point with \(x<r\), \(0<y<g(x)\) converges to \((x_\infty,0)\) with \(x_\infty<r\); one with \(y=g(x)\) tends to \((r,0)\); one with \(y>g(x)\) cannot have \(x_\infty<1\). Likewise, any \(x\ge r\), \(y>0\), forces \(x_\infty=1\) (positive \(y\) instantly increases \(x\)). When \(x\to1\), comparison with scalar logistic equations in \(\dot y=\beta y(x-r-y)\) gives \(y\to1-r\). Seeds with \(y=0\) never succeed.

**2. Feasible frontier.** Direct differentiation yields
\[
 g'(x)=\begin{cases}-\log\frac{1-x}{1-r},&\beta=1,\\
 \frac{\beta}{1-\beta}\left[\left(\frac{1-x}{1-r}\right)^{\beta-1}-1\right],&\beta\ne1,
 \end{cases}
\qquad
 g''(x)=\beta(1-r)^{1-\beta}(1-x)^{\beta-2}>0.
\]
Thus \(g\) strictly decreases from \(g(0)>0\) to \(g(r)=0\); the line \(y=x\) meets it at exactly one \(a\in(0,r)\). Physically feasible successful seeds below \(r\) therefore satisfy \(x>a\), \(y>g(x)\), \(y\le x\), and the infimum of their costs is at least the minimum of \(F(x)=c_sx+c_vg(x)\) over \([a,r]\). Successful seeds with \(x\ge r\) have cost strictly greater than or equal to \(c_sr=F(r)\), while the forthcoming minimizer has cost strictly below \(F(r)\).

**3. Unique optimum and cost transition.** Since \(F''=c_vg''>0\), its minimizer on \([a,r]\) is unique. At the right endpoint, \(F'(r)=c_s>0\); at the left, \(F'(a)=c_v(\lambda-\lambda_c)\). For \(\lambda\ge\lambda_c\), the minimum is at \(x=a\), where \(y=a\). For \(0<\lambda<\lambda_c\), the minimum satisfies \(-g'(x_*)=\lambda\), giving the displayed formula for \(t_\lambda\), with \(a<x_*<r\) and \(0<g(x_*)<x_*\). In either regime, the optimum point is on the invariant non-successful separatrix. For any \(\varepsilon>0\), a sufficiently small increase in \(x_*\) when \(x_*<r\), retaining the same \(y_*\), or a sufficiently small physically feasible increase in \(y_*\) when \(y_*<x_*\), yields a successful seed with cost \(C_*+O(\varepsilon)\). At \((a,a)\), increase both fractions slightly along \(y=x\); this lies above \(g(x)\) and is successful. Consequently every \(B>C_*\) permits success, while strict convexity and invariance of the boundary exclude success for \(B\le C_*\).

**4. Lambert-W specialization.** For \(\beta=1\), the equation \(g(a)=a\), with \(t=(1-a)/(1-r)>1\), is \(t\log t=r/(1-r)\). Writing \(w=W_0(r/(1-r))\) yields \(t=r/[(1-r)w]\), hence \(a=1-r/w\) and \(\lambda_c=\log t=w\). Substitution of \(x_*=1-(1-r)e^\lambda\) into \(F\) gives the cost expression. No finite simulation is used to establish any continuum statement.

## Verification
Run `python check_social_campaign.py` after installing dependencies in `requirements.txt`. Direct numerical optimization was compared against the formulas at 48 parameter/cost choices; six independently integrated trajectories were checked on opposite sides of the invariant boundary; the Lambert-W identity was checked numerically. These finite checks supplement the analytic proof, not certify originality or any infinite quantifier.

## Relationship to prior work
Run Wang, Leonardo Cianfanelli, Giacomo Como, and Wenjun Mei (arXiv:2607.25586v1) derive the social-norm dynamics, its conserved quantity, the exact incubation/outbreak separatrix, and the convergence classification. These dynamic facts are prerequisites, not novel components. The present finding introduces an explicit two-cost one-shot intervention objective, solves the continuous-cost optimization completely for all admissible dynamical parameters, identifies the mixed/all-vocal allocation transition and non-attainment of the sharp success budget, and gives a Lambert-W transition formula. Cianfanelli, Messina, Como, and Fagnani (arXiv:2605.11337v1) study least-cost changes of thresholds for a *different*, discrete linear-threshold network model; their controls and success criterion do not imply this finite-dimensional continuous-state frontier.

## Limitations
This is one-shot *initial-condition* seeding with linear homogeneous marginal costs, continuous population fractions, and a well-mixed deterministic system. It does not solve dynamic optimal control, network-specific targeting, noisy diffusion, campaign duration, or discrete-agent seeding. Existing knowledge of the full separatrix makes the optimization reducible to strict convex one-variable calculus; mathematical originality here rests on the new motivated control objective and its exact all-parameter allocation frontier, not on a new phase portrait. A wider or differently named published intervention theorem could still imply this result; historical priority needs independent assessment. Boundary-optimal initial conditions do not themselves lead to an outbreak.

## References
1. Run Wang, Leonardo Cianfanelli, Giacomo Como, Wenjun Mei, *A Minimal Dynamical Model for Incubation-Outbreak Transitions in Social Norm Diffusion*, arXiv:2607.25586v1, first publicly posted 2026-07-28, https://arxiv.org/abs/2607.25586.
2. Leonardo Cianfanelli, Sebastiano Messina, Giacomo Como, Fabio Fagnani, *Optimal Interventions on the Linear Threshold Model in Large-Scale Networks*, arXiv:2605.11337v1, first publicly posted 2026-05-11, https://arxiv.org/abs/2605.11337.
