# Heterogeneous three-representative sincerity under conditional winner sharing

## Finding

For exactly three informed delegates, conditional proportional sharing (CPSR) supports strictly sincere, signal-following voting at **every** positive, possibly fully unequal effort profile whenever the common prior makes each private signal decision-relevant. A stronger individual statement holds: if the other two delegates follow their signals, posterior-sincere voting is a uniquely optimal vote at every non-tie posterior, for any interior prior and any positive own effort.

Writing the focal effort as \(a\), and the two opponent efforts as \(b,c\), let \(S=a+b+c\), and define the tie-adjusted weighted-majority indicator

\[
\lambda(u,v)=\begin{cases}1,&u>v,\\1/2,&u=v,\\0,&u<v.\end{cases}
\]

With reward budget \(B>0\) and posterior state probability \(\pi\) for the focal delegate, the exact conditional payment advantage of acceptance over rejection is

\[
\Delta(\pi)=Ba(2\pi-1)Q(a;b,c),\quad
Q(a;b,c)=\frac{b+c}{S}+(b-c)\left(\frac{\lambda(a+b,c)}{a+b}-\frac{\lambda(a+c,b)}{a+c}\right)>0.
\]

Therefore, if \(\pi>1/2\) acceptance is uniquely optimal, and if \(\pi<1/2\) rejection is uniquely optimal. At posterior \(\pi=1/2\) both actions tie. All comparisons are voting-stage, with efforts fixed.

## Assumptions and scope

There are exactly three delegates \(i,j,k\). Delegate \(\ell\) has fixed private-information effort \(x_\ell\in(0,1/2]\), receives signal \(s_\ell\in\{G,B\}\), and observes the true binary state correctly with probability \(1/2+x_\ell\); the signals are independent conditional on the binary state. The common prior \(\mu\) lies strictly between zero and one. Delegates know all efforts, the prior and the reward rule. Weighted voting uses weight \(x_\ell/S\), with a fair coin on exact total-weight ties. A budget \(B>0\) is paid only to a winning coalition containing at least two delegates; among eligible winning voters, transfers are proportional to their respective efforts. An ineligible winner triggers no transfers. Effort cost does not depend on the subsequent ballot and cancels in voting comparisons.

For a full strict signal-following voting-stage equilibrium, require \(|\mu-1/2|<\min_{\ell}x_\ell\). This is equivalent to each delegate's posterior being strictly above one half after \(G\) and strictly below one half after \(B\). These hypotheses are sufficient, not claimed necessary for every profile.

## Proof

Fix the focal effort \(a\) and the other efforts \(b,c\). Suppose the other delegates vote their signals. Set \(p_b=1/2+b\) and \(p_c=1/2+c\). If both opponents accept, accepting yields \(Ba/S\) and rejecting yields zero (the lone dissenter fails the headcount requirement); if both opponents reject the payoff difference is \(-Ba/S\). If the \(b\)-delegate accepts and the \(c\)-delegate rejects, accepting is worth \(Ba\lambda(a+b,c)/(a+b)\), while rejecting is worth \(Ba\lambda(a+c,b)/(a+c)\); the reverse signal configuration gives the negative difference. This remains exact when a two-person coalition has exactly half of the total voting weight: its expected conditional payment uses the fair-coin factor \(1/2\).

Conditional on the true state \(G\), independence gives

\[
\Pr(GG)-\Pr(BB)=p_b+p_c-1=b+c,\qquad
\Pr(GB)-\Pr(BG)=p_b-p_c=b-c.
\]

Consequently, expected acceptance minus rejection transfer conditional on state \(G\) is \(BaQ(a;b,c)\). Under state \(B\), interchanging every good and bad signal makes this the negative of that quantity. Conditioning on the focal posterior \(\pi\) establishes \(\Delta(\pi)=Ba(2\pi-1)Q\).

It remains to establish \(Q>0\) for every \(a,b,c>0\). Relabel opponents so \(b\ge c\), and put \(d=b-c\ge0\). Since \(a+b>c\), the first \(\lambda\) equals one. If \(a+c<b\), the second equals zero, and \(Q=(b+c)/S+d/(a+b)>0\). In the boundary case \(a+c=b\), the second equals one half, hence \(Q\) is at least its value with this indicator replaced by one. If \(a+c\ge b\), then \(a\ge d\). The function

\[
F(a)=(a+b)(a+c)-(a+b+c)d
\]

has derivative \(F'(a)=2a+2c>0\), and \(F(d)=bc>0\). Thus \((a+b)(a+c)>Sd\). For \(d>0\) it follows that

\[
Q\ge\frac{b+c}{S}-\frac{d^2}{(a+b)(a+c)}
>\frac{b+c-d}{S}=\frac{2c}{S}>0.
\]

When \(d=0\) the formula directly gives \(Q=2c/S>0\). This proves positivity also at both possible pair-weight tie surfaces. Therefore, for any posterior other than one half, following the posterior-majority direction uniquely maximizes the focal expected transfer. Applying this argument to all three delegates proves the signal-following profile is a strict voting-stage Bayesian equilibrium whenever \(|\mu-1/2|<\min\{a,b,c\}\). This does not establish an equilibrium in the preceding effort choice.

## Verification

The reproducible standalone Python program `verify.py` independently enumerates the eight profiles of the two opponents' signals and both focal ballots in exact rational arithmetic, including half-probability coalition weight ties. On the \(10^3\) effort triples \((q_1,q_2,q_3)/20\) with every \(q_i\in\{1,\ldots,10\}\), it reports 6,000 state-conditional formula comparisons, 18,000 posterior-identity comparisons, and 270 focal tie cases. All assertions pass. This finite evidence checks algebraic encoding but is not a replacement for the universal inequality proved above.

## Relationship to prior work

Beccuti and Schneider, *Rewarding Informed Voting in PoS Governance* (arXiv:2610.07959v1; first public October 6, 2026), introduce CPSR and establish strict sincere voting for symmetric positive effort profiles (Proposition 2), and for profiles with one unequal effort while the other two efforts coincide (three-delegate specialization of Lemma 1). Their Example 2 exhibits insincere incentives at an asymmetric profile under a prior that causes two delegates to pool on rejection. The present theorem covers arbitrary three-way effort heterogeneity **while all signal reports remain informative for sincere choices**, and gives a closed-form signed incentive coefficient valid even when weighted-majority coalitions tie. It neither claims sincerity for arbitrary priors nor contradicts Example 2.

## Limitations

Exactly three delegates, fixed positive efforts and conditionally independent symmetric-accuracy binary signals are essential to the stated proof. The theorem is about the voting continuation, not effort incentives, selection among multiple equilibria, overall welfare or arbitrarily large committees. Outside the signal-following-prior region the full profile may pool and the result does not apply. No exhaustive check of unpublished or unindexed research is possible; independent scientific audit has not been performed.

## References

1. J. Beccuti and M. Schneider (2026), *Rewarding Informed Voting in PoS Governance*, arXiv:2610.07959v1, https://arxiv.org/abs/2610.07959 (first publicly released October 6, 2026). Relevant primary text: Section 4.1, Proposition 2; Section 4.2, Lemma 1; Appendix A.6; Appendix B.2, Example 2.
