# Sharp two-community oscillation threshold in a coevolving public-goods opinion network

## Finding

The synchronous best-response dynamics of Davidson, Zino, Cao, and Ye (2026) can have an **attracting, genuinely nonconvergent period-two orbit** even when the social influence network is symmetric, loopless, complete, and aperiodic. In the homogeneous two-community family below, a sharp mixing threshold separates existence from nonexistence of a specified alternating block-constant cycle. The two consensus equilibria also attract open sets of initial opinions. Therefore, the motivating paper's proposed unrestricted convergence statement does not hold under its permitted synchronous activation schedule.

**Theorem.** Let \(s\ge2\), \(n=2s\), \(1<r<n\), and \(\alpha,\beta,\lambda>0\) with \(\alpha+\beta+\lambda=1\). Define
\[
p=\frac{\beta}{\beta+\lambda},\qquad
\theta=\frac12+\frac{\alpha(1-r/n)(\beta+\lambda)}{\beta\lambda},
\]
and suppose \(\theta<1\). Partition the agents into two classes of size \(s\). For \(0<\varepsilon<1\), let the row-stochastic, symmetric, zero-diagonal influence matrix have off-diagonal entries
\[
w_{ij}=\begin{cases}
\varepsilon/(s-1),&i\ne j\text{ in the same class},\\
(1-\varepsilon)/s,&i,j\text{ in different classes}.
\end{cases}
\]
Let
\[
D=1-p+2p\varepsilon,\qquad
H=\frac{1-p+p\varepsilon}{D},\qquad
L=\frac{p\varepsilon}{D},\qquad
\varepsilon_*=\frac{(1-\theta)(1-p)}{1-2p(1-\theta)}.
\]
Then \(0<\varepsilon_*<1/2\), and a two-cycle which alternates each class between full cooperation/opinion \(H\) and full defection/opinion \(L\), with the two classes in opposite phases, exists **if and only if** \(0<\varepsilon<\varepsilon_*\). It is unique among two-cycles with this specific constant-on-class action and opinion pattern, and is locally exponentially attracting. If an initial opinion vector is within sup-norm distance
\[
\eta<\delta:=\min\left\{\theta-\frac{\varepsilon}{D},\ 1-\frac{\varepsilon}{D}-\theta\right\}
\]
of either phase, then, irrespective of initial actions, the resulting orbit follows the alternating action pattern from the next update and the opinion error is at most \(p^t\eta\) after \(t\) synchronous steps. The all-defection and all-cooperation consensus states are likewise locally exponentially attracting. The sharp threshold statement concerns **this alternating block-constant cycle**; it does not exclude other cycles or other dynamics when \(\varepsilon\ge\varepsilon_*\).

## Assumptions and scope

The model is the discrete-time coevolving public-goods-game/Friedkin--Johnsen best-response model in Davidson et al. [1], their equations (2)--(4) and (10)--(12), with the permitted all-active schedule, zero prejudice \(\gamma_i=0\), and common strictly positive coefficients. Each player has action \(x_i\in\{0,1\}\) and opinion \(y_i\in[0,1]\). Cooperation means \(x_i=1\). All agent weights sum to one and there are no self-loops. At an exact action tie the update selects defection, as specified in [1]. The network of the theorem is primitive because all off-diagonal entries are positive and \(n\ge4\). No assumption about the initial action vector is needed to enter the basin stated above.

Writing \(m_i(y)=\sum_jw_{ij}y_j\), the synchronous dynamics simplifies exactly to
\[
x_i(t+1)={\bf1}_{\{m_i(y(t))>\theta\}},\qquad
y_i(t+1)=p\,m_i(y(t))+(1-p)x_i(t+1).
\]
Here \(1/2<\theta<1\), so both consensus action/opinion profiles satisfy the update equations.

## Proof

**Step 1: best-response threshold.** For a fixed tentative action \(a\in\{0,1\}\), optimizing the player's strictly concave quadratic opinion payoff gives \(u_a=(\beta m_i+\lambda a)/(\beta+\lambda)\). Subtracting the resulting maximized payoffs for cooperation and defection yields
\[
\Delta_i=\alpha\left(\frac rn-1\right)+\frac{\beta\lambda}{\beta+\lambda}\left(m_i-\frac12\right).
\]
Thus the unique selected best-response action away from equality is \({\bf1}_{\{m_i>\theta\}}\), with the opinion update displayed above. This derives the required map from the original game, rather than imposing a separate threshold rule.

**Step 2: any alternating block-constant candidate is rigid.** Let \(H\) denote the opinion of the cooperating class at one phase, and \(L\) that of the defecting class. At the next phase the opinions and the actions swap by hypothesis. The mean opinion at successive phases is the same, and applying the affine opinion update averaged across agents gives \((H+L)/2=p(H+L)/2+(1-p)/2\); hence \(H+L=1\). The opinion update for the class that defects next is
\[
L=p\bigl(\varepsilon H+(1-\varepsilon)L\bigr).
\]
Solving these two equations gives \(L=p\varepsilon/D\) and \(H=(1-p+p\varepsilon)/D\), uniquely. In particular \(H-L=(1-p)/D>0\), so a successful orbit genuinely has least period two.

**Step 3: sharp best-response inequalities.** At the cooperating class the neighboring opinion average is
\[
m_{\rm coop}=\varepsilon H+(1-\varepsilon)L=\frac{\varepsilon}{D},
\]
while at the defecting class it is \(m_{\rm defect}=1-\varepsilon/D\). To swap actions, the former must be at most \(\theta\) and the latter must be strictly greater than \(\theta\). The second inequality is equivalent to
\[
\varepsilon<\frac{(1-\theta)(1-p)}{1-2p(1-\theta)}=\varepsilon_*.
\]
The denominator is positive because \(p<1\) and \(\theta>1/2\). It is also immediate that \(0<\varepsilon_*<1/2\). Thus throughout this range \(\varepsilon/D<1/2<\theta\), so the first best-response inequality holds strictly. For \(\varepsilon\ge\varepsilon_*\), the defecting class cannot switch to cooperation (including at equality, where defection wins the tie); uniqueness in Step 2 rules out the specified cycle. Substitution into the affine map verifies both phases when \(\varepsilon<\varepsilon_*\).

**Step 4: attraction and coexistence.** In the cycle regime the best-response margins are strictly positive and their minimum is \(\delta\). Because \(W\) is nonnegative and row-stochastic, \(\|Wv\|_\infty\le\|v\|_\infty\). Consequently, if \(\|y(0)-y^{\rm phase}\|_\infty\le\eta<\delta\), the very next actions agree with the cycle, and the next opinion error is bounded by \(p\eta\). Induction gives the specified alternating actions and \(p^t\eta\) error for all \(t\ge0\). This establishes an open basin and exponential attraction, independent of initial actions. If all initial opinions are below \(\theta\), all agents defect thereafter and opinions decay geometrically toward zero. If all initial opinions exceed \(\theta\), all agents cooperate thereafter and the opinion deviations from one decay geometrically. Both are open consensus basins.

**Exact witness.** For \(s=2\), \(n=4\), \(r=3\), \(\alpha=1/5\), \(\beta=\lambda=2/5\), \(p=1/2\), \(\theta=3/4\), and \(\varepsilon=1/8<\varepsilon_*=1/6\),
\[
W=\begin{pmatrix}
0&1/8&7/16&7/16\\1/8&0&7/16&7/16\\
7/16&7/16&0&1/8\\7/16&7/16&1/8&0
\end{pmatrix}.
\]
The orbit alternates
\[
\begin{aligned}
&x=(1,1,0,0),\quad y=(9/10,9/10,1/10,1/10),\\
&x=(0,0,1,1),\quad y=(1/10,1/10,9/10,9/10).
\end{aligned}
\]
At the first phase the neighbor averages are \((1/5,1/5,4/5,4/5)\); at the next phase these reverse. The smaller best-response margin is \(1/20\), so every opinion vector within distance \(1/20\) of either phase converges exponentially to this two-cycle.

## Verification

The companion standard-library Python program `verify.py` uses exact rational arithmetic. It reconstructs the original optimized player payoff, checks the action discriminant, verifies the two phases and their reversal, tests sharp cutoff examples beyond the threshold, and independently checks the four-agent weight matrix, strict margins, and perturbation contraction. Its execution reported `PASS: 116 exact cycle/critical/perturbation cases; explicit original-payoff comparisons; nondegenerate four-agent witness`. These finite tests do not establish the general theorem; Steps 1--4 above do.

## Relationship to prior work

Davidson et al. [1] explicitly permit synchronous all-agent updating (Assumption 1, Remark 2) and conjecture general convergence to an equilibrium in their conclusion. Their Theorem 2 proves convergence to all-defection only in a parameter regime where all actions must defect; it does not cover the coexistence regime \(1/2<\theta<1\) studied here. The stable two-cycle therefore answers the conjectural unrestricted convergence question negatively without contradicting the proved theorem.

Aghbolagh et al. [2] study coevolution under a **coordination game** with payoffs depending on neighbors' binary actions rather than the linear all-population public-goods incentive in [1]. Liang et al. [3] analyze coordination/anti-coordination networks and a different threshold that depends on neighbors' action states. Neither model is the best-response map of [1], and their results do not give this exact two-class cutoff or these locally attracting public-goods oscillations. The general phenomenon of two-cycles in synchronous threshold dynamics is not claimed as new; the claim is the sharp construction, attraction, and nonconvergence for the specific 2026 public-goods game.

## Limitations

The example requires a synchronous activation schedule (which is permitted, not required, by [1]); it proves nothing against convergence under a singleton asynchronous activation schedule. The sharp mixing cutoff is specific to the block-constant anti-phase orbit and does not classify all attractors. The result uses zero prejudices, homogeneous coefficients, two equal-sized communities, and symmetric complete weights; it does not claim the same conclusion for arbitrary networks. At the cutoff, the specified anti-phase branch fails because the tie-breaking rule chooses defection. A historical-priority review of the broader threshold-map and coordinated-opinion literature remains appropriate, although no implication-equivalent result was located in the inspected sources.

## References

[1] E. C. Davidson, L. Zino, M. Cao, M. Ye, *Modelling the coevolution of opinion dynamics and decision making in social dilemmas*, arXiv:2604.08840v1 (10 April 2026), https://arxiv.org/html/2604.08840v1 .

[2] H. Dehghani Aghbolagh, M. Ye, L. Zino, M. Cao, Z. Chen, *Coevolutionary Dynamics of Actions and Opinions in Social Networks*, arXiv:2206.07242 (2022), https://arxiv.org/abs/2206.07242 .

[3] H. Liang, M. Ye, L. Zino, W. Xia, *Coevolution of Actions and Opinions in Networks of Coordinating and Anti-Coordinating Agents*, arXiv:2505.03078 (2025), https://arxiv.org/html/2505.03078v1 .
