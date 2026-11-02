# Sharp three-delegate Bayesian accuracy loss under effort-proportional voting

## Finding

Consider a binary decision with equally likely states \(S\in\{-1,+1\}\). Three independent representatives choose positive precision efforts \(0<x_i<1/2\). Conditional on the state, representative \(i\) observes a binary signal \(Y_i\) satisfying \(\Pr(Y_i=S\mid S)=1/2+x_i\), and sincerely casts that signal as a vote. The actual decision is the sign of \(\sum_i x_iY_i\), with an independent fair coin at a zero-weight sum. Compare this decision with the Bayes-optimal decision based on the three signals and their known precisions.

Write \(x\ge y\ge z>0\) for the three efforts, let \(s=y+z\), and put
\[
 t=\frac{y+z}{1+4yz}.
\]
The precise difference \(\Delta\) between Bayes-optimal and effort-proportional decision accuracy is
\[
\Delta(x,y,z)=
\begin{cases}
\displaystyle\frac{x(1+4yz)-y-z}{2},&t<x<s,\\[4pt]
\displaystyle xyz,&x=s,\\[4pt]
0,&\text{otherwise.}
\end{cases}
\]
Consequently \(0\le\Delta<1/16\) for all interior three-representative effort profiles, and the supremum is exactly \(1/16\) (6.25 percentage points), but is not attained. With one or two conditionally independent binary signals, effort-proportional weighting is always Bayes-optimal. Thus three is the first committee size with any such aggregation loss.

## Assumptions and scope

The three efforts are deterministic and publicly known for the purpose of the statistical benchmark; all strictly lie between zero and one half. Signal accuracies are \(1/2+x_i\), and the signals are conditionally independent given the state. The prior is symmetric. The signal-contingent sincere-voting rule is assumed, not derived as a strategic equilibrium. Voting power is proportional to effort, so normalization by \(\sum_i x_i\) does not affect the decision. Both the actual rule and its performance comparator count a randomized tie as half a success. The Bayes comparator observes all three reports and uses the known signal precisions; it need not be implementable under the same transfer or information constraints as a strategic payment mechanism.

The result concerns the unconditional probability of selecting the correct binary state. It does not optimize effort choices or infer them from a payment game; it does not address correlated signals or nonsymmetric priors. No asymptotic limit in the number of representatives is claimed.

## Proof

**1. Bayes weights.** For a signal \(Y_i\in\{-1,+1\}\) and the uniform prior, the posterior log-likelihood ratio of the positive to the negative state is
\[
 L(Y)=\sum_{i=1}^{3}Y_i\lambda(x_i),\qquad
 \lambda(u)=\log\!\frac{1+2u}{1-2u}=2\operatorname{arctanh}(2u).
\]
The Bayes decision is \(\operatorname{sgn}L(Y)\), with arbitrary resolution of posterior ties. This follows by multiplying the state-conditional likelihoods and taking logarithms, and does not assume that effort-proportional weights are statistically optimal.

**2. Only one opposing-coalition pattern matters.** Sort efforts as \(x\ge y\ge z\). Both \(u\mapsto u\) and \(u\mapsto\lambda(u)\) are strictly increasing. Whenever the representative with effort \(x\) agrees with at least one other representative, the two decision rules agree: the positive total weight of those two exceeds the weight of the sole dissenter under both weighting schemes. They also agree when all signals coincide. Therefore, disagreement is possible only on the opposite signal patterns \((+1,-1,-1)\) and \((-1,+1,+1)\), ordered by \((x,y,z)\).

The actual weighted majority follows the two weaker representatives precisely when \(x<y+z=s\); it follows the stronger representative when \(x>s\), and uses its fair tie-breaking coin at \(x=s\). To determine the Bayes decision, the addition law for hyperbolic tangent gives
\[
\lambda(x)>\lambda(y)+\lambda(z)
\quad\Longleftrightarrow\quad
 x>\frac{y+z}{1+4yz}=t.
\]
Because \(y,z>0\), we have \(t<s\). Thus the two decisions differ with positive probability exactly when \(t<x<s\), and disagree with probability one half on the relevant patterns when \(x=s\). A Bayes tie at \(x=t\) carries no accuracy loss.

**3. Exact excess accuracy.** Under the positive state, the probabilities of the two exceptional signal patterns \((+1,-1,-1)\) and \((-1,+1,+1)\) are respectively
\[
 b=(1/2+x)(1/2-y)(1/2-z),\qquad
 a=(1/2-x)(1/2+y)(1/2+z).
\]
The same two probabilities are exchanged under the negative state. In the open disagreement region, the Bayes rule follows the strongest signal and the actual rule follows the other two. The difference in correct-decision probabilities is therefore \(b-a\), under either state, and hence under their equal mixture. Direct expansion gives
\[
 b-a=\frac{x(1+4yz)-y-z}{2}.
\]
On the weighted tie surface \(x=s\), the fair coin loses half this advantage, giving \((b-a)/2=xyz\). In all remaining regions the same decisions are taken, or any Bayesian tie leaves expected accuracy unchanged. This proves the complete piecewise formula, including its boundary surfaces.

**4. Sharp global upper bound.** In the only region with positive open-chamber loss, \(x<s\) and \(x<1/2\). If \(s\le1/2\), then
\[
\Delta< 2syz\le \frac{s^3}{2}\le\frac1{16},
\]
where \(yz\le s^2/4\) is arithmetic-geometric mean. If \(s\ge1/2\), then
\[
\Delta<\frac{(1/2)(1+4yz)-s}{2}
 =(1/2-y)(1/2-z)
 \le\frac{(1-s)^2}{4}\le\frac1{16}.
\]
The tied-weight case satisfies \(xyz\le x^3/4<1/32\); the other cases have zero loss. Every interior profile therefore has strictly smaller loss than \(1/16\).

For any integer \(N>10\), take \(x=1/2-1/N\) and \(y=z=1/4\). Then \(t=2/5<x<s=1/2\), and the exact loss is
\[
\Delta=\frac1{16}-\frac5{8N}\longrightarrow\frac1{16}.
\]
This proves sharpness and nonattainment.

**5. The two-signal boundary.** With at most two independent binary reports, if their signs agree both rules follow that sign. When the reports differ, effort weighting follows the stronger effort, while Bayes weighting follows the stronger log-odds; since \(\lambda\) is strictly increasing, these decisions are the same. Equal efforts give ties under both schemes. Thus the Bayesian aggregation loss vanishes at all one- and two-signal profiles.

## Verification

Run `python3 verify.py` with Python 3 (standard library only). The checker independently computes, using exact rational arithmetic, the conditional probabilities of every binary signal vector. It compares the Bayes action selected by state likelihoods against the actual effort-weighted action (with half credit for ties), rather than reconstructing the proof's sign-pattern classification. It checks all 1,330 sorted triples drawn from the 19-point strictly interior precision lattice \(\{1/40,2/40,\ldots,19/40\}\), all 576 ordered two-signal precision pairs on a separate lattice, and five members of the sharpness family. It reports 257 three-signal triples with positive loss on that finite grid. All comparisons and the sharpness-family equalities are exact fractions.

This finite verification corroborates the formula but is not used to prove the all-real-parameter result; the preceding argument supplies the infinite quantifiers and boundary analysis.

## Relationship to prior work

Beccuti and Schneider, *Rewarding Informed Voting in PoS Governance* (first posted October 6, 2026), specify the effort-to-signal-precision relation, effort-proportional endogenous voting power, independent signals, neutral-prior sincere voting and independent fair tie-breaking used here. Their results examine payment incentives, equilibrium effort, and accuracy at symmetric profiles. The present result instead quantifies the fixed-effort, asymmetric aggregation loss against the optimal signal-likelihood rule. It does not modify their equilibrium claims.

Birmpas, Lazos, Markakis and Penna (2024) study the antecedent effort-dependent vote-weight model and budget-constrained committee design; the inspected full text does not compare its rule with Bayes signal aggregation or optimize a three-delegate regret expression. The optimal log-odds aggregation rule is classical, going back to Nitzan and Paroush and the Neyman–Pearson formulation; Berend and Kontorovich provide a modern treatment of its finite-sample behavior. The known optimality principle is used as a premise and is not claimed as new. The contribution is the explicit three-representative disagreement chamber, exact loss over the full continuous effort cube, and sharp \(1/16\) performance frontier for effort-proportional weighting.

## Limitations

The bound is conditional on sincere signal-following votes and on the symmetric prior. It is not an equilibrium inefficiency bound, and the Bayes benchmark may require more information than the original protocol exposes. The maximum is a supremum approached by an almost perfectly informed representative whose effort is just below the combined effort of the other two. If a different deterministic tie convention replaces the independent fair coin, the exact formula on \(x=y+z\) changes. No claim is made about committees of four or more or about correlation, heterogeneous signal structures, nonlinear effort costs, or transfers.

## References

1. Juan Beccuti and Manvir Schneider, *Rewarding Informed Voting in PoS Governance*, arXiv:2610.07959v1, October 6, 2026. https://arxiv.org/html/2610.07959v1
2. Daniel Berend and Aryeh Kontorovich, *A Finite Sample Analysis of the Naive Bayes Classifier*, Journal of Machine Learning Research 16 (2015), pp. 1519–1545. https://jmlr.org/papers/volume16/berend15a/berend15a.pdf
3. Shmuel Nitzan and Jacob Paroush, *Optimal Decision Rules in Uncertain Dichotomous Choice Situations*, International Economic Review 23 (1982), pp. 289–297 (classical log-odds weighting, as cited by reference 2).
4. Georgios Birmpas, Philip Lazos, Evangelos Markakis and Paolo Penna, *Reward Schemes and Committee Sizes in Proof of Stake Governance*, arXiv:2406.10525, first posted June 2024. https://arxiv.org/pdf/2406.10525
