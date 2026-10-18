# Macroscopic expert delegation is optimal under persistent beta-binomial vote correlation

## Finding

In an odd truth-seeking electorate with one independently informed expert and exchangeable novices whose conditional signal accuracy has a beta distribution, the ex-ante optimal number of novice votes delegated directly to the expert grows **linearly** with electorate size. This contrasts with the established bounded-delegation result for independent novice signals. The result gives an exact beta-binomial success probability, a single-crossing rule for every finite electorate, and a sharp asymptotic delegation fraction.

Write the electorate size as \(N=2k+1\), with \(k\ge1\). Suppose a latent novice accuracy \(\Theta\sim\mathrm{Beta}(a,b)\) is drawn once per decision, where \(a>b>0\). Conditional on \(\Theta\) and the correct binary alternative, the \(2k\) novice votes are independent, each correct with probability \(\Theta\). The expert's correctness is independent of \(\Theta\) and all novice signals, with probability \(q\in(1/2,1)\). Before observing signals, exactly \(r\) novices directly delegate their entire vote to the expert, for integer \(0\le r\le2k\). Each of the remaining novices and the expert votes according to their signal; every original vote has unit weight and strict majority decides.

Let \(A_{k,r}\) be the probability of a correct decision, and put \(m=2k-r\). Define the beta-binomial tail \(T_{m}(t)=\sum_{j=\max\{0,t\}}^m \binom mj B(a+j,b+m-j)/B(a,b)\), with \(T_m(t)=0\) when \(t>m\). Then

\[
 A_{k,r}=q\,T_m(k-r)+(1-q)\,T_m(k+1).
\]

For \(0\le r<k\), define

\[
 C_{k,r}=\binom{2k-r-1}{k}\frac{B(a+k-r-1,b+k+1)}{B(a,b)}>0,
 \qquad R_{k,r}=\prod_{j=k-r-1}^{k}\frac{a+j}{b+j}.
\]

The exact marginal change is

\[
 A_{k,r+1}-A_{k,r}=C_{k,r}\bigl[q-(1-q)R_{k,r}\bigr].
\]

Since \(a>b\), \(R_{k,r}\) is strictly increasing in \(r\), so \(A_{k,r}\) is unimodal on \(0\le r\le k\), with at most two adjacent maximizers. All choices \(r\ge k\) give the expert an outright majority and have success probability exactly \(q\); hence restriction to \(0\le r\le k\) loses no possible improvement.

Let \(r_k\) be any maximizer among \(0,\ldots,k\). Then

\[
 \boxed{\displaystyle\lim_{k\to\infty}\frac{r_k}{k}
 =1-\left(\frac{1-q}{q}\right)^{1/(a-b)}=:\rho\in(0,1).}
\]

In particular, the proportion of the whole electorate delegating approaches \(\rho/2>0\), despite fixed positive marginal novice competence \(a/(a+b)>1/2\). Their pairwise correlation, conditional on the true alternative, is \(1/(a+b+1)>0\).

For the exact natural-parameter example \(a=3\), \(b=2\), and \(q=7/10\), the novice competence is \(3/5\), their correlation is \(1/6\), and

\[
 R_{k,r}=\frac{k+3}{k-r+1},\qquad
 \operatorname{sgn}(A_{k,r+1}-A_{k,r})=\operatorname{sgn}(4k-7r-2).
\]

For every \(k\ge2\), the optimal delegation count among *all* integers \(0\le r\le2k\) is

\[
 \boxed{r^*_k=\left\lceil\frac{4k-2}{7}\right\rceil,}
\]

uniquely unless \(k\equiv4\pmod7\), when \(r^*_k\) and \(r^*_k+1\) tie and are the only optima. At \(k=1\), both \(r=1\) and \(r=2\) cause expert dictatorship and maximize success. For larger electorates the optimal delegated share tends to \(2/7\). Under *independent* novice signals of the same marginal precision \(3/5\), keeping the same expert precision \(7/10\), the optimal count is instead exactly one for every \(k\ge2\) (or one or two, dictator-equivalent, at \(k=1\)); this independent benchmark is established in earlier literature, rather than asserted as a new result.

## Assumptions and scope

The truth is one of two alternatives with symmetric signal-error probabilities. The probability statements are conditional on either true alternative, so its prior does not enter. The beta latent variable represents *shared question difficulty*: it is drawn afresh for each question, not once per voter, and the expert's signal remains independent even after conditioning on truth. Exact delegation counts are chosen before seeing any signals; which novices delegate is immaterial by exchangeability. Delegation transfers the original vote's full weight, does not count the novice's unused signal, and is not recursively transmitted. No voter strategically misreports, no one abstains, and the total number of counted votes is always odd.

For \(a>b>0\), novelties concern the ex-ante optimal restricted one-expert architecture, not equilibrium incentives or unconstrained statistically optimal decision rules. The beta distribution permits some questions on which the novices' conditional correctness is less than one half, explaining why a lone independent expert can retain substantial informational value even in very large groups.

## Proof

**1. Mixture and voting thresholds.** Conditional on \(\Theta=\theta\), after \(r\) delegations the number \(X\) of correct directly cast novice signals has distribution \(\operatorname{Bin}(2k-r,\theta)\). If the expert is correct, the expert-controlled block supplies \(r+1\) correct ballots, so the novices must supply at least \(k-r\). If the expert is wrong, at least \(k+1\) correct novice votes are required. Integrating \(\theta^{j}(1-\theta)^{m-j}\) against the beta density proves the displayed \(A_{k,r}\) formula. At \(r\ge k\) the expert block contains a strict majority, proving \(A_{k,r}=q\).

**2. Marginal effect as two pivotal events.** For \(0\le r<k\), couple the policies with \(r\) and \(r+1\) delegations by removing one further novice's direct ballot and transferring it to the expert. If the expert's signal is correct, the decision changes from wrong to correct only when that novice was wrong and exactly \(k-r-1\) of the other \(2k-r-1\) novices were correct. If the expert's signal is wrong, the decision changes from correct to wrong only when that novice was correct and exactly \(k\) of those other novices were correct. The two binomial coefficients coincide:

\[
 \binom{2k-r-1}{k-r-1}=\binom{2k-r-1}{k}.
\]

Integrating the two probabilities gives

\[
 A_{k,r+1}-A_{k,r}=
 \frac{\binom{2k-r-1}{k}}{B(a,b)}
 \bigl[q\,B(a+k-r-1,b+k+1)
 -(1-q)\,B(a+k+1,b+k-r-1)\bigr].
\]

The gamma recurrence \(\Gamma(x+1)=x\Gamma(x)\) shows that the ratio of the second beta function to the first is \(R_{k,r}\). This establishes the asserted exact difference, including all endpoints \(r=0\) and \(r=k-1\).

**3. Unique sign change.** Since \(a>b\), every factor \((a+j)/(b+j)\) exceeds one. Raising \(r\) to \(r+1\) adds the extra factor \((a+k-r-2)/(b+k-r-2)>1\) whenever \(r+1<k\). Thus \(R_{k,r}\) is strictly increasing, and the bracket \(q-(1-q)R_{k,r}\) is strictly decreasing in sign. There can be at most one zero marginal difference, yielding the one-peak, at-most-two-adjacent-maximizers classification on \([0,k]\).

**4. Linear scaling.** Uniformly whenever \(r/k\) stays in a compact subinterval of \([0,1)\),

\[
 \log R_{k,r}=\sum_{j=k-r-1}^{k}\log\left(1+\frac{a-b}{b+j}\right)
 =(a-b)\log\left(\frac{k}{k-r}\right)+o(1)
\]

for sequences \(r/k\to t<1\). Indeed \(\log(1+u)=u+O(u^2)\) uniformly for \(u=O(1/k)\), and the relevant harmonic sum has the stated logarithmic limit. Consequently \(R_{k,r}\to(1-t)^{-(a-b)}\). The equation \((1-t)^{-(a-b)}=q/(1-q)\) has the unique solution \(\rho\in(0,1)\). For each fixed \(\epsilon>0\) with \(\rho\pm\epsilon\in(0,1)\), marginal differences are eventually positive below \((\rho-\epsilon)k\) and negative above \((\rho+\epsilon)k\). Single crossing traps every optimizer between these scales, proving \(r_k/k\to\rho\). In particular \(r_k<k\) for all sufficiently large \(k\), so the infinitely many dictator-equivalent policies \(r\ge k\) never affect the asymptotic optimizer claim.

**5. Rational specialization and independent comparison.** When \((a,b)=(3,2)\), the product telescopes because \((a+j)/(b+j)=(j+3)/(j+2)\), giving \(R_{k,r}=(k+3)/(k-r+1)\). With \(q=7/10\) the sign bracket is \((4k-7r-2)/(10(k-r+1))\). The sharp integer optimizer and ties follow immediately. For independent novices with competence \(p=3/5\), the same pivotal-event coupling gives a sign bracket \(q-(1-q)(p/(1-p))^{r+2}\), positive at \(r=0\) and negative at \(r=1\) and thereafter, proving the quoted constant-one comparator (also consistent with the earlier optimal-weight results).

## Verification

The standalone `verify.py` evaluates beta-binomial tails with rational beta functions (for positive integer shape parameters), independently evaluates the pivotal-event difference and compares them for four parameter pairs and electorate half-sizes \(1\le k\le12\). It separately checks the entire maximizing set for the displayed rational example for \(1\le k\le29\), and checks the independent benchmark for the same range. The program uses standard-library exact fractions; its 418 assertions passed. It checks finite consequences only. The universal single-crossing and asymptotic results rest on the preceding analytical proof, not on those finite tests.

## Relationship to prior work

Mooers et al. [1] study delegation in epistemic voting and report overdelegation; their canonical model uses conditional signal independence. Their Appendix B.6.3 also explicitly studies a *three-voter* special model mixing perfect novice correlation with independent signals. Thus neither correlated votes nor expert delegation are introduced here; the new assessed object is a full beta-mixture family across arbitrary electorate sizes with a globally sharp finite optimizer and a positive limiting delegation fraction.

Dhillon et al. [2], especially Proposition 3 and its proof, characterize optimal one-expert delegation for independent novice signals using relative log-odds weights, obtaining numbers of delegations bounded in electorate size. That result is prior art and supplies the directly contrasted independent regime. Strnad [3] studies an epistemic framework explicitly allowing dependent votes, but the examined analysis does not state this beta-binomial single-crossing formula or proportional optimizer. Gilbert et al. [4] study vote correlation through a different, binary common-signal model and delegation mechanisms. Only its abstract was accessible for the comparison; its detailed possible implications therefore remain an unresolved publication-priority risk. Neither absence from search results nor differences of terminology independently establish novelty.

## Limitations

This is an ex-ante centralized choice of how many votes to transfer to **one independent expert**, not a Nash-equilibrium theory of decentralized delegation, nor a claim that all large correlated electorates should delegate a fixed fraction. The common latent beta mixture assumes persistent positive intraclass correlation as the electorate grows; letting \(a+b\) grow with the electorate can change the asymptotic regime. The expert's correctness is assumed independent of the shared novice difficulty. Only binary truth-seeking choices, sincere votes and strict simple majority are treated. The theorem does not evaluate fairness, expressive representation, strategic legitimacy or practical calibration of the latent distribution. Independent publication-priority audit and independent scientific validation have not been carried out.

## References

[1] V. Mooers, J. Campbell, A. Casella, L. de Lara, D. Ravindran, *Liquid Democracy. Two Experiments on Delegation in Voting* / revised *Liquid Democracy or Direct Democracy? One Theoretical Result and Two Experiments*, arXiv:2212.09715, first posted 2022-12-19, especially section 8 and Appendix B.6.3.

[2] A. Dhillon, G. Kotsialou, D. Ravindran, D. Xefteris, *Information Aggregation with Delegation of Votes*, arXiv:2306.03960, first posted 2023-06-06, Proposition 3 and its proof.

[3] J. Strnad, *Delegation and Participation in Decentralized Governance: An Epistemic View*, arXiv:2505.04136 (2025), especially sections 2.2.3 and 5.

[4] S. Gilbert, S. Schmid, S. Schnell, J. Svoboda, M. Yeo, *Liquid Democracy under Vote Correlation: On the Fallacies of Averaging and the Excluded Middle*, arXiv:2608.16738 (2026), abstract only available in this comparison.
