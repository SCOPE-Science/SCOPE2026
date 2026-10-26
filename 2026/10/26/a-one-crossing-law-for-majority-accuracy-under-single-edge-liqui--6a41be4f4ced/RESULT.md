# A one-crossing law for majority accuracy under single-edge liquid delegation

## Finding

The exact effect of a single vote delegation on majority correctness in a two-state, conditionally independent epistemic voting model has a two-exponential form. When all ordinary voters have the same state-dependent accuracy, this form admits **at most one population-size reversal** in whether the delegation helps or hurts. An exact example reverses between three and five voters even though the delegate is strictly more competent than the delegator in **both** signal states.

For an odd electorate of \(2m+1\) voters, define
\[
A_b=(1-q_b)c_b(1-a_b)-q_b a_b(1-c_b),\qquad
\lambda_b=q_b(1-q_b).
\]
The ex-ante difference between correctness under delegation and direct voting is
\[
\boxed{\Delta_m=\binom{2m-1}{m-1}\sum_{b=0}^1\pi_b A_b\lambda_b^{m-1}.}
\]
This is an exact finite-population identity, not an approximation. In each state, delegation is nonharmful if and only if
\[
\frac{c_b}{1-c_b}\ge\frac{a_b}{1-a_b}\frac{q_b}{1-q_b}.
\]

## Assumptions and scope

There are \(n=2m+1\) voters for an integer \(m\ge1\) and a binary ground truth. The public state \(b\in\{0,1\}\) is sampled **after** delegation, with prior \(\pi_0,\pi_1>0\) summing to one. Conditional on the public state, individual votes are independent Bernoulli correctness indicators. Designated voters \(s\) and \(t\) have conditional correctness probabilities \(a_b,c_b\in(0,1)\), and the remaining \(2m-1\) voters have common conditional correctness probability \(q_b\in(0,1)\). The parameters are fixed as \(m\) varies. Unconditional votes may be correlated through the state.

Direct voting gives all voters one voting unit. In the comparison outcome, only \(s\) delegates to \(t\), so \(s\) has weight zero, \(t\) has weight two, and each other voter has weight one. All outcomes are decided by weighted strict majority of the original \(2m+1\) units, so no tied outcomes occur. The directed awareness graph need only allow \(s\to t\). No equilibrium assumption or algorithmic rule choosing the edge is claimed. The probability of correctness is defined relative to the objectively correct binary option.

## Proof

Fix state \(b\), and write \(X_s,X_t\) for the designated correctness indicators and \(S\) for the number of correct votes among the \(2m-1\) ordinary voters. Under direct voting the outcome is correct if and only if
\[
S+X_s+X_t\ge m+1.
\]
Under the single delegation the outcome is correct if and only if
\[
S+2X_t\ge m+1.
\]
The two outcomes have the same correctness status except in two disjoint events. Delegation creates a win where direct voting loses exactly when \(S=m-1,\ X_t=1,\ X_s=0\); it creates a loss where direct voting wins exactly when \(S=m,\ X_t=0,\ X_s=1\). Conditional independence therefore gives
\[
\Delta_m^{(b)}=c_b(1-a_b)\Pr_b(S=m-1)-a_b(1-c_b)\Pr_b(S=m).
\]
Since \(S\sim\operatorname{Bin}(2m-1,q_b)\), the two adjacent coefficients are equal:
\[
\binom{2m-1}{m-1}=\binom{2m-1}{m}.
\]
Factoring the binomial masses yields
\[
\Delta_m^{(b)}=\binom{2m-1}{m-1}[q_b(1-q_b)]^{m-1}
[(1-q_b)c_b(1-a_b)-q_b a_b(1-c_b)].
\]
Averaging over the public state proves the boxed formula. The same strictly positive prefactors yield the statewise odds criterion.

To establish the one-crossing assertion, divide the bracket of the formula by \(\lambda_1^{m-1}>0\): its sign is that of
\[
\pi_0 A_0(\lambda_0/\lambda_1)^{m-1}+\pi_1 A_1.
\]
If the two \(\lambda\)'s coincide, the expression is constant. If they differ, the exponential term is strictly monotone, so the entire expression is strictly monotone when \(A_0\ne0\); it has at most one real zero, and its sign on positive integers can reverse at most once. If either \(A_b\) vanishes, a fixed sign remains. When \(A_0A_1<0\) there is one real zero, at
\[
m_*=1+\frac{\log[-\pi_1 A_1/(\pi_0 A_0)]}{\log(\lambda_0/\lambda_1)}.
\]
Only positive integer \(m\) correspond to electorates. If the dominant \(\lambda\) has nonzero \(A_b\), it determines the sign for all sufficiently large \(m\). The magnitude still tends to zero, since a one-edge delegation has a difference supported on central binomial outcomes and \(\lambda_b\le1/4\).

For an explicit sharp three-to-five reversal, take
\[
(a_0,a_1)=(3/5,3/5),\quad(c_0,c_1)=(4/5,4/5),\quad
(q_0,q_1)=(3/5,4/5),\quad(\pi_0,\pi_1)=(1/3,2/3).
\]
Here \(A_0=7/125\), \(A_1=-4/125\), \(\lambda_0=6/25\), and \(\lambda_1=4/25\). Therefore
\[
\boxed{\Delta_m=\frac{1}{375}\binom{2m-1}{m-1}
\left[7(6/25)^{m-1}-8(4/25)^{m-1}\right].}
\]
At \(m=1\) this is \(-1/375\). At \(m=2\) it is \(2/625\). For every \(m\ge2\), positivity follows from \(7(3/2)^{m-1}>8\). There are no smaller odd electorates than three admitting a nontrivial single delegation with an uncommitted third voter, so three and five are consecutive relevant sizes for this reversal.

## Verification

The included standalone `verify.py` evaluates the direct-versus-delegated decision by complete enumeration of all correctness vectors for sampled rational competence configurations, compares these with an independently convolved pivotal-mass formula, and tests the homogeneous binomial identity. It checks 220 independently generated heterogeneous parameter configurations, 216 homogeneous parameter cases, the two-state witness at sizes three through eleven, and twenty successive odd-electorate signs using exact rational arithmetic. Its output records the two exact fractions \(-1/375\) and \(2/625\). Computations corroborate the formulas; the preceding algebraic proof establishes the all-size result.

## Relationship to prior work

Gilbert, Schmid, Schnell, Svoboda and Yeo (2026) introduced the same two-state common-signal framework and proved asymptotic guarantees and counterexamples for broader delegation mechanisms. Their paper explicitly distinguishes improved voter competence from improved majority correctness. The result here focuses instead on a *single fixed edge*, derives its exact finite-\(n\) gain, and classifies how the **sign** of that gain can change as homogeneous-background electorate size varies. Their numerical finite-size examples use different all-to-one or matched-pair delegation designs and do not state this one-crossing formula.

Kahng, Mackenzie and Procaccia (2021) study independent scalar competences and impossibility/possibility of delegation mechanisms; their scalar setting contains no two-state population-size competition between conditional pivotal probabilities. Abramowitz and Mattei (2024) analyze a different representative-delegation model, chiefly comparing outcomes with the original voter majority instead of an objective ground truth. The one-crossing assertion does not follow as a stated result from those comparisons. This is a claim of mathematical distinction from the inspected formulations, not a proof of global historical priority.

## Limitations

The structural one-crossing law uses exactly **two** signal states and a homogeneous background **within each state**. Heterogeneous-background populations obey the more general two-pivotal-mass identity but need not have the same two-exponential reduction. Multiple delegations, even electorates and non-majority social-choice rules are not classified. Delegation along the selected edge is imposed, not shown to be chosen by any particular local mechanism. When the public state is informative about which option is objectively correct, its effect is represented only through stipulated conditional competence probabilities; no model of strategic signal acquisition is claimed. External historical priority cannot be certified by a finite literature search.

## References

1. S. Gilbert, S. Schmid, S. Schnell, J. Svoboda and M. Yeo, *Liquid democracy under vote correlation: On the fallacies of averaging and the excluded middle*, arXiv:2608.16738v1, 17 August 2026. https://arxiv.org/html/2608.16738v1
2. A. Kahng, S. Mackenzie and A. D. Procaccia, *Liquid Democracy: An Algorithmic Perspective*, Journal of Artificial Intelligence Research 70 (2021), DOI 10.1613/jair.1.12261. https://www.jair.org/index.php/jair/article/view/12261
3. B. Abramowitz and N. Mattei, *Flexible representative democracy: An introduction with binary issues*, Social Choice and Welfare (first published 9 September 2024), DOI 10.1007/s00355-024-01543-0. https://link.springer.com/article/10.1007/s00355-024-01543-0
