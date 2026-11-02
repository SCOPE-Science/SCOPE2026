# Sharp justified-representation price for two-alternative temporal elections

## Finding

For every pair of integers \(n\ge2\) and \(\ell\ge n\), consider complete offline temporal approval elections with exactly two alternatives per round, the same two alternatives in all rounds, and arbitrarily time-varying nonempty approval sets. Let \(W^*\) denote maximum unconstrained utilitarian welfare, and \(W^{\mathrm{JR}}\) maximum welfare subject to temporal justified representation (JR), in which every voter must obtain positive satisfaction over the horizon. Then

\[
\max_E\frac{W^*(E)}{W^{\mathrm{JR}}(E)}
=\frac{\ell(n-1)}{\ell(n-1)-(n-2)}.
\]

Every unconstrained welfare-maximizing outcome either satisfies JR already or can be made JR-feasible by changing **one round only**. For \(n\ge3\), equality in the displayed price holds if and only if there is a fixed voter \(i_0\) who in every round exclusively approves the option opposed by all other \(n-1\) voters. The majority-approved option may change from round to round. For \(n=2\), the price is one for every election.

## Assumptions and scope

Fix voters \(N=\{1,\dots,n\}\), two alternatives \(P=\{A,B\}\), and rounds \(T=\{1,\dots,\ell\}\). Each voter \(i\) submits a set \(S_{it}\in\{\{A\},\{B\},\{A,B\}\}\) in each round \(t\). A feasible outcome chooses one candidate \(o_t\in P\) per round. Satisfaction is \(s_i(o)=|\{t:o_t\in S_{it}\}|\), and utilitarian welfare is \(W(o)=\sum_i s_i(o)\). Since every singleton agrees in all \(\ell\ge n\) rounds, temporal JR implies \(s_i(o)\ge1\) for every voter. Conversely, if all voters have positive satisfaction, every nonempty group's total satisfaction is positive, so JR holds. Hence these conditions are equivalent in the specified domain; we do **not** impose PJR, EJR, or FJR+.

## Proof

Choose an unrestricted maximum-welfare outcome \(o\), so in each round the chosen alternative has a maximum number of approvals. Let \(a_t\) be its approval count; nonempty two-alternative ballots give \(a_t\ge n/2\). If everybody is already satisfied, there is nothing to prove. Otherwise let \(U=\{i:s_i(o)=0\}\) and \(u=|U|\ge1\). Let \(C\) be the voters with satisfaction exactly one, and put \(c=|C|\). At most \(c\) rounds contain the *unique* satisfactory occurrence of some member of \(C\). Call those rounds critical. Every other round is noncritical. Because \(\ell\ge n\) and \(c\le n-u\), at least one noncritical round exists.

In every noncritical round, no voter in \(U\cup C\) approves the chosen option: members of \(U\) never do, and the unique approval round of any member of \(C\) is necessarily critical. Thus the chosen approval count is at most \(n-u-c\). Put \(d=u+c\). Since the chosen option is a per-round welfare maximizer and at least half of voters approve it, \(1\le d\le n/2\).

Switching the winner in **any** noncritical round from one of the two alternatives to the other satisfies every voter in \(U\), because their nonempty ballots exclude the old winner and therefore contain the other alternative. The switch cannot remove the last satisfied round of a previously satisfied voter: the only voters at such risk would belong to \(C\), and they do not approve the old winner in a noncritical round. Hence the switched outcome satisfies JR.

Choose a noncritical round \(t_0\) minimizing the chosen approval count among noncritical rounds, and let \(a=a_{t_0}\). Then \(n/2\le a\le n-d\). If the alternative candidate in \(t_0\) has \(b\) approvals, completeness gives \(a+b\ge n\). The welfare loss of switching is therefore \(\Delta=a-b\le2a-n\), and the switched outcome has welfare \(W^*-\Delta\). There are at most \(c\) critical rounds. Every noncritical round has welfare at least \(a\); every critical round has welfare at least \(n/2\). Since \(a\ge n/2\),

\[
W^*\ge (\ell-c)a+\frac{cn}{2}.
\]

Consequently,

\[
0\le\frac{W^*-W^{\mathrm{JR}}}{W^*}
\le\frac{\Delta}{W^*}
\le\frac{2a-n}{(\ell-c)a+cn/2}
\le\frac{n-2d}{(\ell-c)(n-d)+cn/2}.
\]

The last inequality holds because the preceding fractional expression is increasing in \(a\), with derivative \(n\ell/((\ell-c)a+cn/2)^2>0\). To compare the final expression with the desired bound, cross-multiplication by positive denominators reduces to

\[
\ell n(d-1)-c(n-2)\left(\frac n2-d\right)\ge0.
\]

This follows from \(c\le d-1\), \(d\le n/2\), and \(\ell\ge n\); indeed the left side is at least \((d-1)n(\ell-(n-2)/2)\). It is strictly positive if \(d>1\). Therefore

\[
W^{\mathrm{JR}}\ge W^*\left(1-\frac{n-2}{\ell(n-1)}\right),
\]

and the claimed ratio follows.

For sharpness when \(n\ge3\), fix one voter who approves only \(B\) in each round and let the other \(n-1\) voters approve only \(A\). The unrestricted optimum selects \(A\) always and has welfare \(\ell(n-1)\); an optimal JR outcome selects \(B\) exactly once and has welfare \(\ell(n-1)-(n-2)\). This attains the bound.

For equality classification when \(n\ge3\), equality in the price forces equality in every inequality above. The strictness established for \(d>1\) forces \(d=1\), hence \(u=1,c=0\). Because the fraction is strictly increasing in \(a\), equality further requires \(a=n-1\). Every round is now noncritical and its approval count lies between \(a=n-1\) and \(n-u=n-1\), so the unrestricted winner receives exactly \(n-1\) approvals in every round. If the other alternative obtained two or more approvals in some round, switching that round would satisfy the one unsatisfied voter with welfare loss strictly less than \(n-2\), contradicting equality. Thus the other alternative receives exactly one approval, necessarily from the same previously unsatisfied voter, in each round. The remaining \(n-1\) voters approve only the majority winner there. The converse was shown by the sharpness example. For \(n=2\), the ratio expression is one and every election attains it.

## Verification

The accompanying standalone Python 3 script `verify_binary_jr.py` uses exact integer arithmetic and rational comparisons. It checks all \(3^{9}=19{,}683\) complete profiles for \(n=\ell=3\), and all \(3^{12}=531{,}441\) for \(n=3,\ell=4\), optimizing over all possible two-alternative outcomes. The sharp-price equality occurs in precisely \(24\) and \(48\) profiles, respectively, exactly the predicted fixed-minority polarized instances. An additional 1,000 deterministic pseudo-random complete profiles at \(n=\ell=4\) passed. These finite checks corroborate the general proof; they do not certify the infinite domain by enumeration.

To replay: `python3 verify_binary_jr.py` (standard library only).

## Relationship to prior work

Teh (2026), Theorem 3.3, establishes a general bound \(\ell/(\ell-n+2\sqrt n-1)\) for temporal JR over unrestricted candidate sets. Its proof reserves many rounds to cover unsatisfied voters; the present result gives the exact **two-alternative** price, including all time-varying complete approval profiles, via a one-round repair and a characterization of equality. Teh's Proposition 3.4 uses many distinct alternatives and does not attain the present binary-candidate bound. Elkind, Neoh, and Teh (2024), Theorem 5.6, treats the worst-case price of **individual PROP** over unrestricted candidate sets, and its lower-bound construction uses many projects. In complete elections with \(\ell=n\), PROP coincides with JR, but neither unrestricted-candidate theorem gives the exact binary-agenda constant or equality cases. Prior work on static two-party FJR+ imposes a stronger proportionality condition, not the one-hit JR condition analyzed here.

## Limitations

The theorem is for **offline** two-alternative, complete approval profiles and \(\ell\ge n\). It does not establish the same price for three or more alternatives, for incomplete approval ballots, for stronger proportionality axioms, or for online prediction-free decisions. Bibliographic comparisons cannot exclude all unindexed earlier derivations. No independent scientific audit has been performed.

## References

- Nicholas Teh, *The Price of Proportional Representation in Temporal Voting*, first public arXiv submission 11 May 2026, arXiv:2605.11157, https://arxiv.org/abs/2605.11157 . Definitions 2.1, Theorem 3.3, Proposition 3.4, Appendix B.3.
- Edith Elkind, Tzeh Yuan Neoh, and Nicholas Teh, *Temporal Elections: Welfare, Strategyproofness, and Proportionality*, arXiv:2408.13637, https://arxiv.org/abs/2408.13637 . Theorem 5.6 and its proof.
