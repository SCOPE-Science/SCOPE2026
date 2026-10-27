# A sharp two-threshold phase diagram for independent delegation to one expert

## Finding

Consider five voters deciding a binary question with a definite correct answer. One always-voting expert has independently correct signal probability \(q\); four other voters each have independently correct signal probability \(p\), where \(1/2<p<q<1\). Each ordinary voter, independently of all signals and other decisions, delegates their ballot to the expert with the same probability \(d\in[0,1]\), otherwise casting their own signal. The expert casts their signal, with one unit of weight for themselves and one for each received delegation; the weighted majority has total weight five and no ties. Write \(F_{p,q}(d)\) for the probability the majority is correct.

Set
\[
Q_2(p)=\frac{p^2}{p^2+(1-p)^2},\qquad
Q_3(p)=\frac{p^3}{p^3+(1-p)^3}.
\]
Then \(p<Q_2(p)<Q_3(p)<1\), and the unique maximizer of \(F_{p,q}\) over \(0\le d\le1\) is
\[
 d_{\rm opt}=\begin{cases}
0,&p<q\le Q_2(p),\\
\dfrac{B-A}{4B-A},&Q_2(p)<q<Q_3(p),\\
1,&Q_3(p)\le q<1,
\end{cases}
\]
where \(A=P_0-q\) and \(B=P_1-q\), with
\[
P_0=q\Pr\{\operatorname{Bin}(4,p)\ge2\}+(1-q)\Pr\{\operatorname{Bin}(4,p)\ge3\},
\quad
P_1=q[1-(1-p)^3]+(1-q)p^3.
\]
In the open middle region the optimum is strictly interior, unique, and has strictly greater accuracy than either universal direct voting or universal delegation:
\[
F_{p,q}(d_{\rm opt})>\max\{F_{p,q}(0),F_{p,q}(1)\}.
\]
Five is the smallest odd electorate in this one-expert, identically competent, independently randomizing setting for which a strictly beneficial interior common delegation probability can occur: with three voters, every optimum can be attained at an endpoint.

The thresholds have an information-theoretic interpretation: \(Q_j(p)\) is the posterior correctness probability needed to outweigh \(j\) unanimously agreeing ordinary signals when the expert disagrees (equal binary priors).

## Assumptions and scope

All signal correctness events are independent conditional on a fixed binary truth; correctness probabilities are constant across states. Delegation choices are independent Bernoulli draws with common probability \(d\), made without conditioning on signal realization. Four ordinary voters have identical competence \(p\). The expert has competence \(q>p>1/2\) and never delegates. Vote weights are integer numbers of original ballots, all five original ballots counted exactly once. The accuracy optimization is over the one-dimensional family of anonymous independently randomized delegation policies only. No equilibrium of selfish individual delegation choices, correlation, communication, asymmetric policies, or vote-weighted Bayesian aggregation is asserted.

## Proof

Let \(K\sim\operatorname{Bin}(4,d)\) count delegations. If no one delegates, the expert has weight one. Conditional on expert correctness, at least two of the four ordinary voters must be correct; conditional on expert error, at least three ordinary voters must be correct. Therefore conditional accuracy is \(P_0\) as defined above.

With one delegation, the expert has weight two and three ordinary voters cast their independent ballots. Conditional on expert correctness, at least one remaining ordinary signal must be correct; conditional on expert error, all three must be correct. This gives \(P_1\). With at least two delegations, the expert has weight at least three, so its signal settles the five-ballot majority: conditional accuracy is \(q\).

Set \(A=P_0-q\), \(B=P_1-q\). Averaging over the binomial delegation count and cancelling all terms with \(K\ge2\) yields exactly
\[
F_{p,q}(d)=q+A(1-d)^4+4B d(1-d)^3
=q+(1-d)^3[A+(4B-A)d].
\]
Differentiation gives
\[
 F'_{p,q}(d)=4(1-d)^2\big[(B-A)-(4B-A)d\big].
\]
The two decisive affine values have signs determined by
\[
 B-A=3p(1-p)\big(q[p^2+(1-p)^2]-p^2\big),\qquad
 B=p^3-q[p^3+(1-p)^3].
\]
Thus \(B-A\) is negative/zero/positive as \(q\) is below/equal/above \(Q_2(p)\), whereas \(B\) is positive/zero/negative as \(q\) is below/equal/above \(Q_3(p)\). The derivative's bracket equals \(B-A\) at \(d=0\) and \(-3B\) at \(d=1\). Its dependence on \(d\) is affine. For \(q\le Q_2\), both endpoints are nonpositive and the second is strictly negative, so \(F\) decreases strictly on \((0,1)\). For \(Q_2<q<Q_3\), the first endpoint is positive and the second negative, so the unique zero is \(d_{\rm opt}=(B-A)/(4B-A)\in(0,1)\); the derivative changes from positive to negative there. For \(q\ge Q_3\), both endpoints are nonnegative and the first is strictly positive, so \(F\) increases strictly on \((0,1)\). These arguments establish the unique maximizer and strict superiority in the middle region, including both threshold boundaries.

For \(1/2<p<1\), the odds \(p/(1-p)>1\), so raising the odds to powers two and three gives \(p<Q_2(p)<Q_3(p)<1\). These ratios are also the familiar Bayes posterior thresholds when two or three identical independent ordinary signals agree against the expert.

For the three-voter version (one expert, two ordinary voters), a single ordinary delegation already gives the expert weight two out of three; consequently \(F^{(3)}_{p,q}(d)=q+(1-d)^2(F^{(3)}_{p,q}(0)-q)\). This is monotonic in \(d\) unless constant, and therefore cannot have a *strict* interior maximizer. A one-voter electorate has no delegation choice. Since a five-voter middle-region example exists, five is minimal among odd electorates.

## Verification

The independent exact-rational script `verify.py` enumerates all \(2^4\) delegation configurations, both expert-signal correctness values, and all \(2^4\) ordinary correctness profiles and tests them against the closed polynomial. It checks 225 parameter/rate combinations, including both threshold equalities, strict comparison with both endpoints throughout sampled interior cases, the three-voter formula, and the exact rational witness below. This enumeration corroborates the derivation; the proof above, not finite experimentation, establishes the universal statement.

For \(p=7/10\) and \(q=9/10\), the thresholds are \(Q_2=49/58\), \(Q_3=343/370\), and the unique optimum is \(d_{\rm opt}=84/209\). Exact values are
\[
 F(0)=\frac{11123}{12500},\qquad F(1)=\frac9{10},\qquad
 F\big(\tfrac{84}{209}\big)=\frac{164718547}{182586580}
 =\frac9{10}+\frac{78125}{36517316}.
\]

## Relationship to prior work

Kahng, Mackenzie and Procaccia (2018, expanded 2021) formalize competence-based epistemic delegation and exhibit failures of local delegation mechanisms, especially on star-like networks, along with positive centralized guarantees. Their results do not supply this exact finite five-voter phase diagram for a common independent delegation probability.

Campbell, Casella, de Lara, Mooers and Ravindran (2022) analyze selective delegation to experts and explicitly study a five-voter, one-expert experimental treatment. They show that partial delegation can improve expected correctness under **heterogeneous** ordinary signal qualities and threshold strategies. Therefore the *qualitative fact that sparse delegation can help is already known* and is not a novelty claim here. Their full accessible preprint describes non-expert precisions uniformly distributed across an interval, not four fixed identical ordinary competences, and does not state the two explicit \(Q_2,Q_3\) boundaries separating direct, interior, and total delegation optima under anonymous signal-independent Bernoulli randomization. The present contribution is the **exact two-threshold competence phase diagram and its sharp minimal odd electorate within this different, fully specified model**.

Berinsky et al. (2021), Becker et al. (2021), Zhang and Grossi (2021), and Dhillon et al. (2023) address random delegation, efficient delegation selection, weighted proxies, or strategic equilibrium under other models. Those broader topics motivate this precise calibration question but their examined results do not state this two-threshold formula. A related discussion in Campbell et al. cites higher-welfare asymmetric expert-weight equilibria (Ravindran 2021), which are outside this anonymous-policy comparison. These distinctions do not prove global novelty; independent comprehensive bibliographic confirmation remains outstanding.

## Limitations

This is not a theorem that partial delegation always helps: it is optimal only in the strict competence wedge. It does not assert that an independent common rate is a Nash equilibrium, or that the optimal rate dominates heterogeneous, coordinated, or signal-dependent schemes. It does not extend unchanged to dependent signals, additional experts, or larger electorates. The entire qualitative observation that limited delegation can improve truth tracking is established prior work; only the precise homogeneous-model sharp calibration is advanced here. An equivalently parameterized result in unindexed literature may exist. No independent audit or validation has been performed.

## References

1. Kahng, A., Mackenzie, S., and Procaccia, A. D., *Liquid Democracy: An Algorithmic Perspective*, Proceedings of AAAI 2018. DOI: 10.1609/aaai.v32i1.11468. Public conference page dated 2018-02-08; expanded Journal of Artificial Intelligence Research version (2021).
2. Campbell, J., Casella, A., de Lara, L., Mooers, V. R., and Ravindran, D., *Liquid Democracy: Two Experiments on Delegation in Voting* (2022), arXiv:2212.09715; 2022 working paper, including Section 3, five-voter Section 4 and Appendix.
3. Berinsky, A. J., et al., *Tracking Truth with Liquid Democracy* (2021), arXiv:2107.11868.
4. Becker, R., et al., *When Can Liquid Democracy Unveil the Truth?* (2021), arXiv:2104.01828.
5. Zhang, Y., and Grossi, D., *Tracking Truth by Weighting Proxies in Liquid Democracy* (2021), arXiv:2103.09081.
6. Dhillon, A., et al., *Information Aggregation with Delegation of Votes* (2023), arXiv:2306.03960.
