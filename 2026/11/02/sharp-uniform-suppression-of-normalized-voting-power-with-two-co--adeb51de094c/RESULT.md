# Sharp uniform suppression of normalized voting power with two competing proxies

## Finding
Let \(m=2s-1\ge1\) be odd and let \(p\in[0,1]\). There are two permanent direct-voting proxies \(A,B\) and \(m\) otherwise identical delegators, each of unit voting weight. The proxies cast independent fair binary ballots. Each delegator independently casts a direct positive or negative ballot with probability \((1-p)/2\) each, or delegates to either proxy with probability \(p/2\) each. The outcome is strict majority among the \(m+2\) effective ballots. A voter's absolute pivotal probability is the probability that replacing only that voter's action by a direct positive versus direct negative ballot changes the outcome; any votes delegated to that voter follow its counterfactual ballot.

Write \(H_{m,p}\) for the absolute pivotality of either proxy and \(D_{m,p}\) for that of any delegator. Put \(q=(1-p)/2\), \(a=(1+p)/2\), and \(b=(1-p)/2\). Then
\[
H_{m,p}=\frac12-\sum_{j=s+1}^{m}\binom mjq^j(1-q)^{m-j},
\]
\[
D_{m,p}=\frac12\frac{\binom{m-1}{s-1}}{2^{m-1}}+
\begin{cases}
\frac12\binom{m-1}{s-2}a^{s-2}b^s,&s\ge2,\\
0,&s=1.
\end{cases}
\]
The normalized power share of either proxy is \(R_{m,p}=H_{m,p}/(2H_{m,p}+mD_{m,p})\). For every admissible parameter,
\[
\boxed{R_{m,p}\le R_{m,1}=\frac1{2+m\binom{m-1}{s-1}2^{-(m-1)}}},
\]
with equality only at \(p=1\) if \(m\ge3\); if \(m=1\) equality holds at all \(p\). Consequently the *sharp uniform* upper envelope satisfies
\[
\lim_{\substack{m\to\infty\\m\text{ odd}}}\sqrt m\,\sup_{p\in[0,1]}R_{m,p}=\sqrt{\frac\pi2}.
\]
In particular, for **every sequence** of delegation propensities \(p=p_m\), the normalized power of each permanent proxy tends to zero. For each fixed \(p>0\), the upper envelope is asymptotically attained: \(H_{m,p}\to1/2\), \(D_{m,p}\sim1/\sqrt{2\pi m}\) and \(R_{m,p}\sim\sqrt{\pi/(2m)}\). At \(p=0\), all voters are exchangeable and \(R_{m,0}=1/(m+2)\).

## Assumptions and scope
There are precisely two distinguished, nondelegating proxy voters and an **odd** positive number of indistinguishable delegators. Each proxy has no outgoing delegation; each delegator may directly vote or delegate to either proxy, with the independent probabilities stated above. There are no delegation chains of length greater than one, no abstentions, no delegation cycles, and no heterogeneity in voting weights. The majority is strict and therefore never tied since the total number \(m+2\) of unit ballots is odd. The pivotality definition is the a-priori Penrose–Banzhaf counterfactual measure of Colley, Delemazure and Gilbert, not expected ballot weight or a realized fixed-delegation-game index. Normalization divides each voter’s absolute measure by the sum of all such measures.

## Proof
Let \(m=2s-1\), so the positive-vote majority threshold is \(s+1\). A given delegator's effective ballot is the direct vote if direct, and the current ballot of its selected proxy otherwise.

**Proxy formula.** Condition first on \(B\) voting positively. Among the \(m\) delegators, let \(X\) count those voting directly positively or delegating to \(B\), and let \(Z\) count those voting directly negatively. The marginal laws are \(X\sim\operatorname{Bin}(m,1/2)\) and \(Z\sim\operatorname{Bin}(m,q)\), while \(X+Z\le m\) in every outcome. If \(A\) is forced negative, there are \(1+X\) positive effective ballots. If \(A\) is forced positive, there are \(m+2-Z\) positive effective ballots. Thus \(A\) is critical precisely when \(X\le s-1\) and \(Z\le s\). The excluded events \(X\ge s\) and \(Z\ge s+1\) are disjoint since their simultaneous occurrence would force \(X+Z\ge2s+1>m\). By the fair-binomial median identity \(\Pr(X\ge s)=1/2\), the conditional pivotal probability equals \(1/2-\Pr(Z\ge s+1)\). When \(B\) is negative, global sign inversion gives the same probability. This proves the expression for \(H_{m,p}\).

**Delegator formula.** Force one distinguished delegator's direct ballot to positive or negative. The election changes outcome exactly when the aggregate signed vote of all other \(m+1\) people is zero. With probability \(1/2\), the two independent proxies vote oppositely. Their two ballot weights cancel, and every one of the remaining \(m-1\) delegators has an independent fair effective ballot. The probability of a zero sum is \(\binom{m-1}{s-1}/2^{m-1}\). With probability \(1/2\), the proxies agree. Their two ballots have identical signs; each other delegator then matches that sign independently with probability \(a=(1+p)/2\), and opposes it with probability \(b=(1-p)/2\). Cancellation of the two proxy votes requires exactly \(s-2\) matching ballots and \(s\) opposing ballots, hence the second displayed binomial term when \(s\ge2\); when \(s=1\) cancellation is impossible. This proves \(D_{m,p}\).

**Sharp normalization.** The upper binomial tail in \(H_{m,p}\) decreases as \(p\) increases, so \(H_{m,p}\) is nondecreasing. For \(s\ge2\), the only nonconstant term in \(D_{m,p}\) is proportional to \((1+p)^{s-2}(1-p)^s\), whose logarithmic derivative for \(0\le p<1\) equals \(-[2+(2s-2)p]/(1-p^2)<0\). Thus \(D_{m,p}\) decreases strictly for \(s\ge2\). Since \(R_{m,p}=1/(2+mD_{m,p}/H_{m,p})\), it is strictly increasing in \(p\) for \(m\ge3\). For \(m=1\), both pivotalities equal \(1/2\) independently of \(p\), proving the stated equality condition. At \(p=1\), the tail in \(H\) and the second term in \(D\) both vanish, giving \(H_{m,1}=1/2\), \(D_{m,1}=\binom{m-1}{s-1}/2^m\), and the exact upper bound.

**Asymptotics.** The central-binomial estimate \(\binom{m-1}{s-1}2^{-(m-1)}\sim\sqrt{2/(\pi m)}\) yields the sharp upper-envelope limit. The bound holds uniformly in \(p\), so it implies convergence to zero for any sequence of parameters. For fixed \(p>0\), \(q<1/2\), and a binomial upper-tail large-deviation bound shows \(H_{m,p}\to1/2\). Relative to the central binomial term, the second term of \(D_{m,p}\) has ratio
\[
\frac{s-1}{s}(1+p)^{s-2}(1-p)^s,
\]
which tends to zero exponentially in \(m\) for fixed \(p>0\). Therefore \(D_{m,p}\sim1/\sqrt{2\pi m}\), and substitution proves the normalized asymptotic. If \(p=0\), all \(m+2\) votes are independent fair ballots, and symmetry gives \(R_{m,0}=1/(m+2)\).

## Verification
The accompanying `CHECK.py` computes the formulas with exact rational arithmetic and independently enumerates all delegation/direct-vote actions for \(m\in\{1,3,5,7\}\) and \(p\in\{0,1/4,1/2,3/4,1\}\). Every comparison matches. Further exact-formula tests check the sharp upper envelope, monotonicity and zero-delegation limit over larger sizes, while numerical checks compare the scaled upper envelope to its asymptotic constant. To reproduce: run `python CHECK.py` from this document's directory. These finite tests are corroboration; the proof above establishes the infinite statements.

For example, at \(m=3\) and \(p=1\), the proxy and delegator absolute pivotalities are \(1/2\) and \(1/4\), so the normalized proxy share is \(2/7\), while it is \(1/5\) at \(p=0\). Despite each proxy receiving approximately \(pm/2\) delegated ballots on average, its normalized pivotal-power share vanishes as the number of delegators grows.

## Relationship to prior work
Colley, Delemazure and Gilbert (2023, sections 2 and 4) introduce the counterfactual LD Penrose–Banzhaf measure and a general exact computability scheme on bipartite proxy graphs; this theorem uses that model, not a different measure. Their numerical results (section 6 and appendix A.5) include multiple proxy counts at a fixed electorate size; they do not give the two-proxy all-size formulas or the sharp **uniform normalized power suppression** proved here. The general computation theorem permits evaluating a fixed instance but does not itself assert a uniform asymptotic bound. Their appendix A.4 studies mandatory delegation and defines a different intervention for delegators (switching their selected proxy). At \(p=1\), that intervention coincides in pivotality for this particular two-proxy case, but the present theorem consistently uses the direct-ballot counterfactual of Definition 4.

Zhang and Grossi (2021) study a delegative Banzhaf index for an already fixed delegation profile, rather than averaging over independently sampled delegation actions; their index is not interchangeable with the measure used here. One-proxy results cannot be substituted for the two-proxy argument: the event that the two permanent voters disagree produces a distinct fair-binomial pivotality contribution that dominates the normalization.

## Limitations
The theorem is restricted to two permanent representatives with a common, independent delegation propensity and odd \(m\). It does not characterize more than two permanent proxies, heterogeneous delegator preferences, correlated delegate choices, delegation cycles, nonmajority quotas or even total electorate size. A general dynamic algorithm can compute fixed instances of this model, so the claimed contribution is the exact analytic formulas and the sharp uniform all-size normalized bound, **not** computational decidability or the definition of the index. Publication-priority uncertainty remains for specialized treatments not identified in inspected literature. No independent external audit has been performed.

## References
1. R. Colley, T. Delemazure, and H. Gilbert, *Measuring a Priori Voting Power—Taking Delegations Seriously*, arXiv:2301.02462, first version January 6, 2023. https://arxiv.org/abs/2301.02462 ; open-access full text https://arxiv.org/pdf/2301.02462 . Related IJCAI 2023 publication: doi:10.24963/ijcai.2023/290.
2. Y. Zhang and D. Grossi, *Power in Liquid Democracy*, AAAI 2021, doi:10.1609/aaai.v35i6.16729, https://ojs.aaai.org/index.php/AAAI/article/download/16729/16536 .
3. American Mathematical Society and zbMATH, *MSC2020*, 91B12 Voting theory, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=91-10 .
