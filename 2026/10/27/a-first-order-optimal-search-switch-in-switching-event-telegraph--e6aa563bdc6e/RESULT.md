# A first-order optimal-search switch in switching-event telegraph resetting

## Finding

Consider a particle initially at the origin with velocity \(+v\) that moves with velocity \(\pm v\), where \(v>0\). At the events of a homogeneous Poisson clock of fixed rate \(\lambda>0\), it independently either returns immediately to position zero with velocity \(+v\), with probability \(p\in(0,1]\), or reverses its velocity without relocating, with probability \(1-p\). Let \(T_L\) be the first hitting time of a target at \(+L\), for \(L>0\), and set \(q=\lambda L/v\). The exact mean completion time is

\[
\lambda\mathbb E[T_L]=F_q(p):=\frac{\exp\!\big(q\sqrt{p(2-p)}\big)-1}{p}.
\]

The optimization of this time over the Bernoulli reset fraction \(p\in(0,1]\), **holding the total decision-event rate \(\lambda\) fixed**, has precisely one first-order switch. A universal threshold \(q_c=3.7295732243919928\ldots\) separates two strategies:

* For \(0<q<q_c\), the unique optimum is \(p=1\): all decision events reset the particle into the favorable direction, and none reverse it.
* At \(q=q_c\), exactly two distinct global optima coexist: \(p=1\) and \(p=p_c=0.1204656388350102\ldots\).
* For \(q>q_c\), there is exactly one global optimum, an interior fraction \(p=p_-(q)<p_c\), strictly decreasing in \(q\).

There is also a distinct metastability threshold \(q_s=2.9938108746030780\ldots<q_c\): for \(q<q_s\) the objective strictly decreases in \(p\); at \(q_s\) it develops one stationary inflection; and for \(q>q_s\) it has exactly two interior stationary points, first a strict local minimum \(p_-(q)\), then a strict local maximum \(p_+(q)\). Thus the globally optimal reset fraction jumps discontinuously from \(1\) to \(p_c\) as the target-to-persistence distance \(q\) increases through \(q_c\).

Writing \(b_0\) for the unique positive solution of \(b_0=2(1-e^{-b_0})\), namely \(b_0=1.5936242600400400\ldots\), the large-distance optimum obeys

\[
q^2p_-(q)\longrightarrow\frac{b_0^2}{2},\qquad
\frac{\lambda\min_p\mathbb E[T_L]}{q^2}\longrightarrow
\frac{2(e^{b_0}-1)}{b_0^2}=3.0882773047417401\ldots.
\]

The last limit recovers the diffusion-scale search regime from the competing ballistic-reset strategy.

## Assumptions and scope

Events form one Poisson process with rate \(\lambda\) throughout the motion and have independent identically distributed Bernoulli marks. The particle travels continuously at speed \(v\) between events. A reset consumes zero time, restores both the initial position and the initial **positive** velocity, and starts an independent continuation. At a non-reset event the velocity sign flips. The only absorbing target is at \(+L\), and the process on the left is unbounded. The first target hit terminates motion. The parameter \(p=0\) is excluded from the optimization because its mean hitting time is infinite for the symmetric unrestarted telegraph process. All claims hold for \(\lambda,v,L>0\), not merely for selected dimensionless values.

The model specializes the exponential-intertime Bernoulli-decision telegraph motion introduced by Di Crescenzo, Iuliano and Verasani (2026). Neither their position distribution, stationary law, moment formulas nor Kac-scaling results are claimed as new. The focus here is the half-line first-passage objective under a *fixed total switch-or-reset event budget*, especially its unique discontinuous global optimizer.

## Proof

**1. Exact first-passage mean.** Independent marking of one rate-\(\lambda\) Poisson clock produces independent resetting and velocity-flip clocks with rates \(r=\lambda p\) and \(\kappa=\lambda(1-p)\). Before its first reset, the particle is an ordinary symmetric telegraph particle initially pointing toward the target. For \(s>0\), let \(h_\pm(x;s)\) be the Laplace transform of its first target-hitting time when the initial velocity at \(x<L\) is \(\pm v\). For \(\kappa>0\) the bounded solution of the backward system

\[
\begin{aligned}
v\partial_x h_++\kappa(h_--h_+)&=s h_+,\\
-v\partial_x h_-+\kappa(h_+-h_-)&=s h_-
\end{aligned}
\]

with outgoing boundary condition \(h_+(L;s)=1\) is

\[
h_+(x;s)=\exp\!\left[-\frac{L-x}{v}\sqrt{s(s+2\kappa)}\right],\quad
h_- = \frac{s+\kappa-\sqrt{s(s+2\kappa)}}{\kappa}\,h_+.
\]

Indeed substitution verifies both ODEs; the positive spatial root is the unique bounded mode as \(x\to-\infty\). The \(\kappa=0\) result follows directly from ballistic motion or continuously from this expression. Thus the no-reset success-time transform is \(\widehat f_0(s)=\exp[-(L/v)\sqrt{s(s+2\kappa)}]\). The standard first-renewal decomposition at the independent rate-\(r\) clock gives

\[
\mathbb E[T_L]=\frac{1-\widehat f_0(r)}{r\widehat f_0(r)}.
\]

This identity follows, without assuming a finite no-reset mean, by separating the first attempt according to whether target arrival precedes the next exponential reset; each unsuccessful attempt incurs its elapsed duration and restarts the same problem. Substituting \(r=\lambda p\) and \(\kappa=\lambda(1-p)\) gives the stated \(F_q(p)\). As \(p\downarrow0\), \(F_q(p)\sim q\sqrt{2/p}\to\infty\); hence an optimal reset fraction exists in \((0,1]\).

**2. Complete stationary-point classification.** Set

\[
a(p)=\sqrt{p(2-p)},\quad b=qa(p),\quad
\psi(b)=\frac{1-e^{-b}}b,\quad h(p)=\frac{1-p}{2-p}.
\]

Direct differentiation yields

\[
\operatorname{sgn}\bigl(\partial_pF_q(p)\bigr)
=\operatorname{sgn}\bigl(h(p)-\psi(b)\bigr).
\]

For \(0<p<1\), a stationary point requires \(\psi(b)<1/2\). The function \(\psi\) decreases strictly from \(1\) to \(0\). Its level \(1/2\) is attained at the unique positive \(b_0\) above. For \(b>b_0\), the equations \(h(p)=\psi(b)\) and \(b=qa(p)\) can be solved parametrically:

\[
p=p(b):=\frac{1-2\psi(b)}{1-\psi(b)},\qquad
q=Q(b):=\frac{b(1-\psi(b))}{\sqrt{1-2\psi(b)}}.
\]

The function \(p(b)\) is strictly increasing from \(0\) to \(1\). We show that \(Q(b)\) has a **unique** minimum. Introduce

\[
\begin{aligned}
A(b)&=1-(b+1)e^{-b},& B(b)&=b-1+e^{-b},\\
D(b)&=1-e^{-b},& C(b)&=b-2+2e^{-b},\\
H(b)&=\frac{A(b)D(b)}{B(b)C(b)}.
\end{aligned}
\]

All four factors are strictly positive for \(b>b_0\); differentiation simplifies to

\[
\frac{Q'(b)}{Q(b)}=\frac{1-H(b)}b.
\]

Now \(A/B\) is strictly decreasing, since

\[
\frac{A(b)}{B(b)}
=\frac{\int_0^b t e^{-t}\,dt}{\int_0^b(1-e^{-t})\,dt},
\]

and the ratio of the integrands \(t/(e^t-1)\) is strictly decreasing for positive \(t\). This weighted-average argument is an elementary monotone form of l'Hôpital's rule. Furthermore

\[
\frac{d}{db}\frac{D(b)}{C(b)}=-\frac{A(b)}{C(b)^2}<0.
\]

Consequently \(H=(A/B)(D/C)\) strictly decreases from \(+\infty\) at \(b\downarrow b_0\) to \(0\) at infinity. Exactly one \(b_s>b_0\) satisfies \(H(b_s)=1\); the curve \(Q\) strictly decreases up to \(b_s\), then strictly increases. Its minimum \(q_s=Q(b_s)\) is therefore unique. At a fixed \(q>q_s\), the equation \(Q(b)=q\) has precisely two solutions; the corresponding \(p_-(q)<p_+(q)\) are respectively a strict local minimum and a strict local maximum of \(F_q\), since its derivative is negative near \(p=0\) and near \(p=1\). When \(q\le q_s\), the derivative is nonpositive everywhere, vanishing only once at \(q=q_s\); the endpoint \(p=1\) remains the unique global optimum.

**3. Exactly one first-order global switch.** For fixed \(0<p<1\), compare a candidate interior policy with the all-reset policy using

\[
R_p(q)=\frac{F_q(p)}{F_q(1)}
=\frac{e^{qa(p)}-1}{p(e^q-1)}.
\]

The function \(m(z)=z/(1-e^{-z})\) is strictly increasing for \(z>0\), so

\[
\partial_q\log R_p(q)=\frac{m(qa(p))-m(q)}q<0
\qquad(0<p<1).
\]

For \(q>q_s\), let \(R_*(q)=R_{p_-(q)}(q)\). The lower stationary branch is smooth and, by the envelope identity (the derivative with respect to \(p\) vanishes there), \(R_*\) is strictly decreasing. At \(q_s\), \(F_{q_s}\) is decreasing except at its single stationary inflection, so its interior value is strictly larger than \(F_{q_s}(1)\): \(R_*(q_s)>1\). At the other extreme, the lower branch satisfies \(Q(b_-(q))=q\) and \(b_-(q)\downarrow b_0\); it follows that \(F_q(p_-(q))=O(q^2)\) while \(F_q(1)=e^q-1\). Thus \(R_*(q)\to0\). There is exactly one \(q_c>q_s\) at which \(R_*(q_c)=1\). For \(q<q_c\) the endpoint is the unique global minimizer; for \(q=q_c\) the endpoint and the lower stationary branch are exactly the two global minimizers; and for \(q>q_c\) the lower branch is uniquely optimal. Since \(p_-(q_c)<1\), the change in the optimal reset fraction is discontinuous. The branch \(p_-(q)\) decreases strictly because \(p(b)\) increases and \(Q\) decreases on the lower branch.

The constants are defined without dependence on numerical root finding: \(q_s=Q(b_s)\), where \(H(b_s)=1\), and \((p_c,q_c)\) is the unique solution with \(0<p_c<1\) and \(q_c>q_s\) of

\[
\begin{aligned}
q_c\sqrt{p_c(2-p_c)}\frac{1-p_c}{2-p_c}
&=1-e^{-q_c\sqrt{p_c(2-p_c)}},\\
\frac{e^{q_c\sqrt{p_c(2-p_c)}}-1}{p_c}&=e^{q_c}-1.
\end{aligned}
\]

**4. Large-target asymptotics.** On the lower stationary branch, \(b_-(q)\downarrow b_0\). Since \(p=1-\sqrt{1-(b/q)^2}\), this implies \(q^2p_-(q)\to b_0^2/2\), while \(qa(p_-)=b_-(q)\to b_0\). Substitution into \(F_q(p)\) gives the second asymptotic in the finding. This is consistent with optimizing Brownian search at effective diffusivity \(D=v^2/(2\lambda)\), but the sharp finite-distance switch is not supplied by that limit.

## Verification

The standalone `verify.py` evaluates symbolic backward-equation residuals and the stationary derivative identity, brackets both thresholds, checks the stationary branches and the global comparison at representative parameter values, and tests the asymptotic coefficients. Run with Python 3 after installing the versions in `requirements.txt`:

```bash
python -m pip install -r requirements.txt
python verify.py
```

The executed program reported **329 deterministic checks passed**. The exact uniqueness and global-optimality conclusions follow from the analytical monotonicity proof above, not from numerical sampling. Approximate decimal digits are orientation aids; exact constants are defined by the unique equations in the proof.

## Relationship to prior work

Di Crescenzo, Iuliano and Verasani (2026) introduce the Bernoulli choice between resetting and velocity reversal and give position distributions, moments, stationary results and diffusion scaling for exponential and Erlang intertimes. The exponential case is exactly the process used here; our first-passage objective and its fixed-total-intensity optimization are different observables. Classical Poisson thinning and renewal formulas, not new results, supply the mean identity. Evans and Majumdar (2018) establish run-and-tumble first-passage methods under independent Poisson resetting, but their stated reset-velocity rules differ from relaunch at a fixed positive velocity, and they do not state the fixed-decision-budget transition. Baouche and collaborators (2025) optimize orientation-reset active Brownian search in two dimensions, a distinct process. Li, Wang and Xu (2026) analyze finite-interval transition-path times with independently controlled resetting and reversible velocity marks, not the half-line fixed-total-rate budget. The existence of first-order optimum jumps in *other* resetting models is established earlier and is not claimed as a new general principle.

Equivalent formulation: two independent Poisson clocks with \(r+\kappa=\lambda\), where the former restores \((0,+v)\) and the latter flips the sign. The novel assertion is the complete sharp phase diagram **under this fixed sum constraint**. No broad claim of new telegraph hitting transforms, Poisson renewal, or general first-order resetting transitions is made.

## Limitations

The result does not cover asymmetric velocities, initial motion away from the target, a bounded left endpoint, imperfect or delayed resets, unequal event hazards in the two velocity states, or non-exponential decision intervals. It is an exact statement about the *mean* target-hitting time, not an optimization of its variance or a finite-horizon success probability. The new transition is conditional on holding the total decision rate fixed; if the tumble rate is held fixed and reset rate separately tuned, the optimization differs. Although the closest accessible primary sources do not state this phase diagram, implicit coverage by a broader unpublished or uninspected first-passage optimization remains an originality risk; no independent audit has been performed.

## References

1. A. Di Crescenzo, A. Iuliano, G. Verasani, *A Generalized Telegraph Process with Resetting to the Origin Driven by Bernoulli Trials*, Journal of Statistical Physics 193, 97 (2026), DOI: 10.1007/s10955-026-03670-7. First verified public date: 2026-07-18; full open-access HTML available at https://link.springer.com/article/10.1007/s10955-026-03670-7.
2. M. R. Evans, S. N. Majumdar, *Run and tumble particle under resetting: a renewal approach*, Journal of Physics A 51, 475003 (2018), DOI: 10.1088/1751-8121/aae74e; accepted author manuscript metadata at https://www.research.ed.ac.uk/en/publications/run-and-tumble-particle-under-resetting-a-renewal-approach/.
3. Y. Baouche et al., *Optimal first-passage times of active Brownian particles under stochastic resetting*, Soft Matter (2025), DOI: 10.1039/D5SM00340G; full text at https://pubs.rsc.org/en/content/articlehtml/2025/sm/d5sm00340g.
4. H. Li, Z. Wang, Y. Xu, *Optimal transition path time of run-and-tumble particles with stochastic resetting*, Physical Review E 114, 024120 (2026), DOI: 10.1103/xy11-ztd3; public abstract at https://journals.aps.org/pre/abstract/10.1103/xy11-ztd3.
