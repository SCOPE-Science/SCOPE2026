# Unbounded scheduling-excess ratio for a two-agent LQG transmission auction

## Finding
For the auction-inspired, current-score communication policy defined by Hashemi and Maity [1, Equation (20) and Algorithm 1], no uniform multiplicative approximation factor exists **for the nonnegative schedule-dependent part** of the certainty-equivalent LQG objective [1, Equation (10)]. Two agents and two control stages already suffice, and both open-loop plant matrices are strictly stable. More precisely, for every real \(0<\varepsilon\le1/10\), the construction below gives
\[
\frac{F_{\mathrm{auction}}}{F_{\mathrm{opt}}}
=\frac{\varepsilon/3+\varepsilon^3}{\varepsilon^2/[16(1+\varepsilon^2)(5+4\varepsilon^2)]+2\varepsilon^3}
\sim\frac{80}{3\varepsilon}\longrightarrow\infty.
\]
The numerator and denominator are costs measured against the **same** cost decomposition; this is not a claim about a ratio of full LQG objectives containing the additive schedule-independent term.

## Assumptions and scope
There are two independent scalar systems and stages \(k\in\{0,1\}\), with terminal time \(2\). In each system, \(x_{i,k+1}=\tfrac12x_{i,k}+u_{i,k}\); process noise is identically zero, a permitted zero-covariance case. The initial states are independent, with \(x_{1,0}\) equiprobably \(+1\) or \(-1\), and \(x_{2,0}\) equiprobably \(+\sqrt\varepsilon\) or \(-\sqrt\varepsilon\). Both have mean zero. Measurements, when transmitted, are exact, and at most one transmission is allowed per time \(k\). The scheduler knows the current states; regardless of their signs, their innovation squares equal \(1\) and \(\varepsilon\).

In the usual horizon-two quadratic objective [1, Equation (4)], agent 1 has stage state weight \(Q_1=0\), control weight \(R_1=\varepsilon^2>0\), terminal weight \(Q_{1,2}=1\). Agent 2 has \(Q_2=2\), \(R_2=1\), terminal weight \(Q_{2,2}=0\). Both have transmission penalty \(\lambda_i=\varepsilon^3>0\). All state weights are nonnegative and the same stable open-loop scalar coefficient \(A_i=1/2\) is used in both systems. Controls are optimal certainty-equivalent LQG controls [1]. The scheduling objective \(F\) excludes the **schedule-independent** part \(J_{\mathrm{const}}\) in [1, Equation (10)].

## Proof
For scalar \(A=1/2\), \(B=1\), let \(P_{i,2}=Q_{i,2}\) and apply the finite-horizon Riccati identities
\[
P_{i,k}=Q_i+\frac{A^2R_iP_{i,k+1}}{R_i+P_{i,k+1}},\qquad
\Gamma_{i,k}=\frac{A^2P_{i,k+1}^2}{R_i+P_{i,k+1}}.
\]
These follow directly from \(P_k=Q+A^2P_{k+1}-A^2P_{k+1}^2/(R+P_{k+1})\) and \(\Gamma_k=L_k^2(R+P_{k+1})\), \(L_k=AP_{k+1}/(R+P_{k+1})\). Substitution gives
\[
\begin{aligned}
P_{1,1}&=\frac{\varepsilon^2}{4(1+\varepsilon^2)},
&\Gamma_{1,1}&=\frac1{4(1+\varepsilon^2)},
&\Gamma_{1,0}&=\frac{\varepsilon^2}{16(1+\varepsilon^2)(5+4\varepsilon^2)},\\
P_{2,1}&=2,
&\Gamma_{2,1}&=0,
&\Gamma_{2,0}&=\frac13.
\end{aligned}
\]
Put \(a=\Gamma_{1,0}\), \(b=\Gamma_{1,1}/4=1/[16(1+\varepsilon^2)]\), \(c=\varepsilon\Gamma_{2,0}=\varepsilon/3\), and \(\ell=\varepsilon^3\). If \(s_{ik}\in\{0,1\}\) records a transmission and \(s_{1k}+s_{2k}\le1\), the exact no-process-noise error recursion \(e_{i,0}=(1-s_{i0})x_{i,0}\) and \(e_{i,1}=(1-s_{i1})e_{i,0}/2\) gives
\[
F(s)=a(1-s_{10})+b(1-s_{10})(1-s_{11})+c(1-s_{20})
+\ell(s_{10}+s_{20}+s_{11}+s_{21}).\tag{1}
\]
In particular, no term involving \(s_{21}\) reduces estimation error because \(\Gamma_{2,1}=0\); it is strictly wasteful to send a packet to agent 2 at time 1.

At time zero the auction scores [1, Equation (20)] are \(a+b-\ell\) for agent 1 and \(c-\ell\) for agent 2. They are strictly positive and ordered as
\[
a+b-\ell>c-\ell>0\tag{2}
\]
for the stated range. Indeed, \(b\ge 1/(16\cdot1.01)>1/17\), while \(c\le1/30\), and \(c>\ell\). Therefore agent 1 consumes the sole slot at \(k=0\). Its future innovation then vanishes because process noise vanishes; agent 2 has \(\Gamma_{2,1}=0\). Both recomputed auction scores at \(k=1\) equal \(-\ell\), so no second packet is sent. Inserting this schedule into (1) yields \(F_{\mathrm{auction}}=c+\ell\).

For global optimality, exclude \(s_{21}=1\) since removing it strictly reduces (1). If \(s_{10}=1\), further packets do not reduce error and the best cost is \(c+\ell\). If \(s_{20}=1\), then a packet to agent 1 at time 1 costs \(a+2\ell\), while none costs \(a+b+\ell\). If neither agent transmits at time zero, agent 1's time-one transmission yields \(a+c+\ell\) and no time-one transmission yields \(a+b+c\). Hence the global minimum is among the five exact values
\[
c+\ell,\quad a+2\ell,\quad a+b+\ell,\quad a+c+\ell,\quad a+b+c.
\]
For \(0<\varepsilon\le1/10\), the elementary strict inequalities \(\ell<b\), \(\ell<c\), and \(a+\ell<c\) hold. The last follows from \(a\le\varepsilon^2/80\) and
\(\varepsilon^2/80+\varepsilon^3\le \varepsilon(1/800+1/100)<\varepsilon/3=c\).
These three inequalities prove \(a+2\ell\) is strictly smaller than each competing cost. Thus the unique optimum sends agent 2 at time zero and agent 1 at time one.

Finally \(a\sim\varepsilon^2/80\) and \(\ell=\varepsilon^3=o(\varepsilon^2)\) as \(\varepsilon\downarrow0\), while \(c=\varepsilon/3\), giving the claimed asymptotic ratio. The plants are strictly stable independently of \(\varepsilon\), completing the proof.

## Verification
The accompanying standalone `verify.py` uses rational arithmetic to recompute both agents' Riccati gains, calculate all nine capacity-feasible two-stage schedules, check the unique optimizer, and verify the auction choice at six rational values of \(\varepsilon\). It also checks the derived exact identities against an independent Riccati recursion. Running `python verify.py` produces `All exact checks passed.` These finite computations verify representative instances only; the preceding inequalities establish the theorem for all real \(\varepsilon\) in the specified interval.

## Relationship to prior work
Hashemi and Maity [1, Sections III-B and III-C] already establish the shared-capacity objective and introduce the one-step auction score; their examples find it close to the centralized benchmark, but their conclusion explicitly leaves theoretical auction suboptimality analysis for future work. The theorem here is **not** a new optimal-control reduction or a rediscovery of the MILP: it is a worst-case approximation-separation theorem comparing the newly introduced auction policy with that established MILP objective. Hashemi and Maity [2] establish the related single-agent lossless MILP, while [3] analyzes a single-agent lossy channel; neither introduces the present multi-agent capacity-one auction comparison. Standard counterexamples to general greedy scheduling cannot by themselves establish that all values in this construction come from admissible stable scalar LQG Riccati recursions. The literature comparison is bounded, not a global novelty certificate.

## Limitations
Only the **schedule-dependent excess** \(F=J-J_{\mathrm{const}}\) admits the proved unbounded ratio. The result does not imply that the full expected LQG costs have an unbounded ratio, or that the auction performs poorly on the source's simulation benchmark. The family uses two scalar agents, horizon two, exact/noiseless transmissions, vanishing process noise, unequal stage/terminal/control weights, and a small positive communication charge. No claims about arbitrary noisy systems or different heuristics are made.

## References
[1] Z. Hashemi and D. Maity, *Multi-Agent Event-Triggered LQG Control under Shared Communication Constraints*, arXiv:2609.21974 (first public version 2026-09-18), https://arxiv.org/abs/2609.21974. Equations (4), (9)–(11), (18), (20), and Algorithm 1.

[2] Z. Hashemi and D. Maity, *A Linear Programming Framework for Optimal Event-Triggered LQG Control*, arXiv:2509.10671 (first public version 2025-09-12), https://arxiv.org/abs/2509.10671.

[3] Z. Hashemi and D. Maity, *Linear Reformulation of Event-Triggered LQG Control under Unreliable Communication*, arXiv:2604.06060 (first public version 2026-04-07), https://arxiv.org/abs/2604.06060.
