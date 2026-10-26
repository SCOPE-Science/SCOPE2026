# Sharp five-delegate breakdown of neutral-prior sincerity under conditional coalition rewards

## Finding

Consider the conditional proportional sharing rule (CPSR) for an odd number of delegated representatives: a representative is paid a share proportional to effort only when belonging to the weighted-majority winning coalition **and** that coalition contains a strict majority of representatives. Suppose the two underlying states have equal prior probability, each private signal identifies the state with conditional probability \(1/2+x_i\), the positive effort \(x_i\) also determines voting weight, signals are conditionally independent, and the other representatives vote their signals. A vote is sincere precisely when it follows the representative's private signal.

**Sharp committee-size theorem.** In every three-representative committee and at every positive effort vector \(\boldsymbol{x}\in(0,1/2]^3\), sincere voting is a **strict** best response for every representative at each private signal of positive probability. The conclusion includes weighted-majority ties resolved by a fair coin. It fails for five representatives, even with all efforts strictly between zero and one half, all five signals strictly informative, a neutral prior, sincere voting by the four opponents, and **no** possible weighted-majority tie.

An exact counterexample uses
\[
\boldsymbol{x}=\left(\frac25,\frac25,\frac1{100},\frac1{100},\frac1{100}\right).
\]
For either high-effort representative, the expected gross-payment advantage of voting for the state \(G\) over voting for \(B\), conditional on the true state being \(G\), divided by the reward budget \(B>0\), is
\[
K=-\frac{616489}{33459375}<0.
\]
After that representative receives a good signal, the **conditional** advantage of accepting rather than rejecting is
\[
\frac{U(A\mid g)-U(R\mid g)}B
=\frac45 K=-\frac{2465956}{167296875}<0.
\]
Thus the representative strictly prefers to cast the **opposite** of an informative signal. By state and ballot symmetry, the same reversal holds after a bad signal. The failure persists on an open neighborhood of this effort vector.

## Assumptions and scope

There are \(N=2r+1\) representatives, each with a fixed effort \(0<x_i\le1/2\), independent binary signal \(s_i\in\{g,b\}\) conditional on an equiprobable hidden state \(S\in\{G,B\}\), with \(\Pr(g\mid G)=\Pr(b\mid B)=1/2+x_i\). Normalized voting weights are \(w_i=x_i/\sum_jx_j\). A weighted majority determines the chosen alternative, with a fair independent coin in case of equal total voting weights. Write \(W\) for the winning side after that coin, including any loser-to-winner switch determined by the coin. With a fixed budget \(B>0\), the gross payment to representative \(i\) is
\[
f_i(W)=\begin{cases}
B\,x_i/\sum_{j\in W}x_j,& i\in W\text{ and }|W|\ge r+1,\\
0,&\text{otherwise}.
\end{cases}
\]
Conditional voting-stage comparisons hold effort and its cost fixed; no effort-equilibrium, equilibrium-selection, or mechanism-design optimality assertion is made. Every other representative follows their own signal when checking a unilateral vote deviation. For \(0<x_i<1/2\), both private signals occur with positive probability; for \(x_i=1/2\), only the state-consistent signal occurs conditional on either state.

## Proof

**1. State-symmetry reduction.** Fix \(i\) and the other representatives' sincere signal-voting strategy. Let \(K_i B\) be the expectation, conditional on \(S=G\), of the difference between \(i\)'s gross payment when voting \(A\) and when voting \(R\). Exchanging states and reversing every ballot changes this conditional advantage to \(-K_i B\) in state \(B\). By Bayes' rule with neutral prior, a good signal gives posterior \(\Pr(G\mid g)=1/2+x_i\), and a bad signal gives \(\Pr(G\mid b)=1/2-x_i\). Therefore
\[
U_i(A\mid g)-U_i(R\mid g)=2Bx_iK_i,\qquad
U_i(A\mid b)-U_i(R\mid b)=-2Bx_iK_i.
\]
Sincere voting is uniquely optimal at both feasible signals if and only if \(K_i>0\). Costs disappear from this comparison because effort is fixed.

**2. Exact proof for three representatives.** Write the target's effort as \(a>0\) and the other two efforts as \(b\ge c>0\); put \(T=a+b+c\). For each realization of the two opponents' signals, compare the target's payment from acceptance and rejection. If both opponents accept, the action difference divided by \(B\) is \(a/T\); if both reject, it is \(-a/T\). If the effort-\(b\) opponent accepts while the effort-\(c\) opponent rejects, it is \(a(J_b-J_c)\), where
\[
J_b=\frac1{a+b},\qquad
J_c=\begin{cases}
0,&a+c<b,\\
1/[2(a+c)],&a+c=b,\\
1/(a+c),&a+c>b.
\end{cases}
\]
The reverse split has the opposite action difference. The probabilities of these four opponent patterns under \(G\) yield exactly
\[
\frac{K_i}{a}=\frac{b+c}{T}+(b-c)(J_b-J_c).
\]
If \(a+c<b\), then \(J_b>J_c=0\). If \(a+c=b\), then \(a+b=2b-c<2b=2(a+c)\), hence again \(J_b>J_c\). These cases give \(K_i>0\). If \(a+c>b\), then
\[
\frac{K_i}{a}=\frac{b+c}{T}-\frac{(b-c)^2}{(a+b)(a+c)}>0.
\]
For the last inequality, \(a>b-c\) and \((a+b)(a+c)=aT+bc>aT\); when \(b>c\), the subtracted term is strictly below \((b-c)/T\), which is below \((b+c)/T\). When \(b=c\), the subtracted term is zero. This proof covers every positive effort vector and explicitly handles exact weight ties.

**3. Exact five-representative witness.** Let the two high efforts equal \(t=2/5\) and the three low efforts equal \(s=1/100\). Fix one high-effort representative \(i\), let \(p=1/2+t=9/10\), \(q=1/2+s=51/100\), and write \(M\sim\mathrm{Bin}(3,q)\) for the number of the three low-effort representatives voting \(A\) conditional on \(G\). The other high-effort representative votes \(A\) with probability \(p\). Since \(t>3s/2\), the target voting \(A\) is eligible for a payment precisely in these cases: the other high representative votes \(A\) and \(M\ge1\), or the other high representative votes \(R\) and \(M\ge2\). The respective shares are \(t/(2t+Ms)\) and \(t/(t+Ms)\).

Define
\[
H(u,v)=u\sum_{m=1}^3\binom3m v^m(1-v)^{3-m}\frac{t}{2t+ms}
+(1-u)\sum_{m=2}^3\binom3m v^m(1-v)^{3-m}\frac{t}{t+ms}.
\]
State symmetry identifies the acceptance payment under state \(B\) with \(H(1-p,1-q)\), and the rejection payment under state \(G\) with this same quantity. Direct exact-rational evaluation gives
\[
K_i=H(p,q)-H(1-p,1-q)=-\frac{616489}{33459375}.
\]
The total effort is \(83/100\), while every subset effort sum is an integer multiple of \(1/100\). No subset can have exactly half the total effort, since twice an integer cannot equal \(83\). Hence no weighted-majority tie is possible, for any ballot profile. The negative posterior incentive difference follows from Step 1. Because the inequalities are strict and there are no weighted ties, the same failure occurs for every effort vector in some open neighborhood of the witness.

The source model permits odd committees of sizes \(3,5,7,\ldots\), so the universal three-member guarantee and the five-member violation establish the sharp first committee size for this neutral-prior, all-signals-contingent failure.

## Verification

The standalone `verify_cpsr.py` uses only the Python standard library and exact `fractions.Fraction` arithmetic. It separately computes CPSR payments by enumeration of ballot profiles, checks the binomial formula and the precise negative rational above, checks all \(32\) possible weighted-majority splits for absence of ties, and compares the analytic three-member formula against direct enumeration on \(5184\) representative-profile cases, including weighted ties. Invoke `python3 verify_cpsr.py` in the extracted directory. The all-parameter three-member conclusion rests on the proof in Step 2, not on the finite enumeration.

## Relationship to prior work

Beccuti and Schneider (2026) introduce this CPSR rule and prove strict sincere-voting incentives for **symmetric** positive effort profiles. Their Appendix B.2 shows asymmetric failure at a **nonneutral** prior when some other representatives' sincere votes no longer depend on signals; it also gives a positive informative-signal example at three representatives. The present statement instead identifies the precise first odd committee size at which CPSR can fail **at the neutral prior with every other vote signal-contingent**. Neither the symmetric theorem nor their nonneutral-prior counterexample implies the sharp positive three-member result together with the strict five-member failure.

Birmpas et al. (2024) analyze effort-dependent weights and rewards based on delegated power, but do not use the same winning-coalition-cardinality payment and conditional vote-choice incentive criterion. Caragiannis and Schwartzbach (2023) analyze strategic jurors paid according to the **fraction of agreeing votes** rather than effort-weighted winning-coalition shares with a separate headcount quorum. Their possible incentive reversal is related in spirit but does not determine the present five-versus-three boundary for CPSR.

## Limitations

The theorem is confined to the given CPSR payment definition, conditionally independent symmetric-precision signals, neutral prior, simultaneous binary votes, and fixed positive efforts. It proves conditional best-response statements, **not** that the five-member effort vector is a Nash equilibrium or that a strategic committee actually selects insincere voting in equilibrium. The three-member guarantee need not hold for nonneutral priors, as existing work already illustrates. The negative five-member certificate is exact; the size-five existence does not classify all failing weight vectors or all larger committees. Historical priority beyond the inspected primary literature and search results is not independently certified.

## References

1. Juan Beccuti and Manvir Schneider, *Rewarding Informed Voting in PoS Governance*, arXiv:2610.07959v1 (first public October 6, 2026), Sections 2–4 and Appendices A–B. https://arxiv.org/html/2610.07959v1
2. Georgios Birmpas, Philip Lazos, Evangelos Markakis, and Paolo Penna, *Reward Schemes and Committee Sizes in Proof of Stake Governance*, arXiv:2406.10525 (2024), Sections 2–4. https://arxiv.org/abs/2406.10525
3. Ioannis Caragiannis and Nikolaj I. Schwartzbach, *Outsourcing Adjudication to Strategic Jurors*, arXiv:2201.06597 (2022); IJCAI 2023, Sections 2–3. https://arxiv.org/abs/2201.06597
