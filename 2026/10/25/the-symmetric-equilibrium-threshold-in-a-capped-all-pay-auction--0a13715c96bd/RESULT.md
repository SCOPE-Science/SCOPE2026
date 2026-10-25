# The symmetric equilibrium threshold in a capped all-pay auction with a reserve

## Finding

For every integer \(N\ge2\), reserve \(r\in(0,1)\), and common valuation \(V>0\), the complete-information all-pay auction with bids in \([0,1]\), eligibility only for bids \(b\ge r\), full payment of every bid, and uniform tie-breaking has a unique symmetric Nash equilibrium. For \(V>r\), its continuous bidding component exists exactly when \(V<V_c(N,r)\), where \(V_c(N,r)=N/S_N(q_c)=r/q_c^{N-1}\), \(S_N(q)=\sum_{j=0}^{N-1}q^j\), and \(q_c\in(0,1)\) uniquely solves \(rS_N(q_c)=Nq_c^{N-1}\). For fixed \(r\), \(V_c(N,r)\to r+a_r\) as \(N\to\infty\), where \(a_r>0\) uniquely solves \(r(e^{a_r}-1)=a_r\).

Write \(S_N(q)=\sum_{j=0}^{N-1}q^j\). The threshold parameter \(q_c\) is well-defined because \(S_N(q)/q^{N-1}=\sum_{k=0}^{N-1}q^{-k}\) decreases strictly from infinity to \(N\) on \((0,1)\), while \(N/r>N\).

## Assumptions and scope

There are \(N\ge2\) identical, risk-neutral bidders with common value \(V>0\). Each chooses a bid \(b\in[0,1]\), pays that bid regardless of outcome, and is eligible to win only if \(b\ge r\), where \(r\in(0,1)\). The highest eligible bid wins one prize; ties are resolved uniformly. The result classifies symmetric mixed-strategy Nash equilibria only. It does not classify all asymmetric equilibria or make an equilibrium-selection claim.

## Proof

A positive bid below \(r\) loses and costs money, so it is strictly worse than bidding zero. In any symmetric equilibrium no positive atom can occur at an eligible bid below the cap: a sufficiently small overbid wins the positive tie mass at a cost increase that can be made arbitrarily small. Thus any interior eligible support is continuous. Bidding zero gives payoff zero, so any equilibrium with positive mass at zero has equilibrium payoff zero. At a continuous support point \(b\in[r,1)\), the probability of winning is \(F(b)^{N-1}\), where \(F\) is the common bid CDF. Indifference therefore gives

\[
V F(b)^{N-1}-b=0,\qquad F(b)=\left(\frac{b}{V}\right)^{1/(N-1)}.
\]

If \(r<V\le1\), the cap has no positive atom, and the support ends at \(V\). The CDF is \(F(b)=0\) for \(b<0\), \(F(b)=(r/V)^{1/(N-1)}\) for \(0\le b<r\), \(F(b)=(b/V)^{1/(N-1)}\) for \(r\le b\le V\), and \(F(b)=1\) for \(V<b\le1\). Every bid in the continuous support and bid zero yield payoff zero; bids below \(r\) or above \(V\) yield no larger payoff.

For \(V>1\), a symmetric equilibrium below \(V=N\) must place mass at the cap. Let \(q=F(1-)\), the probability an opponent bids below one. If exactly \(k\) of the other \(N-1\) bidders choose the cap, a cap bidder receives a tie share \(1/(k+1)\). Averaging over the binomial number of cap bids gives

\[
\Pr(\text{win by bidding }1)=\frac{1-q^N}{N(1-q)}=\frac{S_N(q)}{N}.
\]

Indifference between bidding one and bidding zero forces \(S_N(q)=N/V\), which has a unique \(q\in(0,1)\) for \(1<V<N\). The upper endpoint of any continuous component is \(b_*=Vq^{N-1}\). If \(b_*>r\), the equilibrium CDF has mass \((r/V)^{1/(N-1)}\) at zero, follows \(F(b)=(b/V)^{1/(N-1)}\) on \([r,b_*]\), remains equal to \(q\) on \((b_*,1)\), and jumps to one at the cap. Bids in the gap \((b_*,1)\) yield payoff \(b_*-b<0\), while bids in the continuous component yield zero.

If \(b_*\le r\), the continuous component is absent and the equilibrium places mass \(q\) at zero and mass \(1-q\) at one. Every intermediate eligible bid \(b<1\) then yields \(Vq^{N-1}-b=b_*-b\le r-b\le0\); bidding one yields zero by the cap-indifference equation. For \(V=N\), this formula has \(q=0\) and all bidders choose one. For \(V>N\), all bidders choosing one is the symmetric equilibrium, with payoff \(V/N-1>0\); any lower bid loses and costs a nonnegative amount.

The cutoff occurs when \(b_*=r\). Combining \(S_N(q_c)=N/V_c\) and \(V_cq_c^{N-1}=r\) gives

\[
rS_N(q_c)=Nq_c^{N-1},\qquad V_c=\frac{N}{S_N(q_c)}=\frac{r}{q_c^{N-1}}.
\]

Because \(b_*=N/[S_N(q)/q^{N-1}]\) decreases strictly as \(V\) increases (the equation \(S_N(q)=N/V\) makes \(q\) decrease, while \(S_N(q)/q^{N-1}\) decreases with \(q\)), the crossing \(b_*=r\) is unique. It satisfies \(1<V_c<N\). This pins down the symmetric distribution in each parameter regime and proves uniqueness within symmetric strategies.

For the large-population limit, set \(q_c=e^{-a_N/N}\). The cutoff equation becomes

\[
\frac1N\sum_{k=0}^{N-1}e^{a_N k/N}=\frac1r.
\]

The left side is increasing in \(a_N\) and converges on bounded intervals to \((e^a-1)/a\). Hence \(a_N\to a_r\), the unique positive solution of \((e^{a_r}-1)/a_r=1/r\), equivalently \(r(e^{a_r}-1)=a_r\). A second Riemann-sum limit gives \(S_N(q_c)/N\to(1-e^{-a_r})/a_r\), so

\[
V_c(N,r)\longrightarrow\frac{a_r}{1-e^{-a_r}}=r+a_r.
\]

## Verification

The normalization, cap tie probability, support endpoints, and all bid ranges are checked algebraically above. The cutoff equation was numerically checked for \(N\in\{2,3,4,5,10,25,100\}\) and \(r\in\{0.1,0.4,0.8,0.99\}\); these spot checks are sanity checks, not the proof. At \(N=2\), the threshold reduces to \(V_c=2-r\). No non-symmetric equilibrium classification is claimed.

## Relationship to prior work

Muratov's 2021 full-text working paper characterizes the reserve-plus-cap model for two and three players; the general-\(N\) symmetric formula and its large-\(N\) cutoff are not stated there. Pastine and Pastine treat general constrained all-pay contests and equilibrium payoffs, but their framework explicitly identifies minimum-bid cases as outside its model and imposes genericity restrictions that exclude identical binding constraints. Szech studies bid caps and tie-breaking in a two-bidder model without the reserve threshold. The present statement is restricted to the natural symmetric class with both the lower eligibility threshold and the common cap.

## Limitations

The result assumes complete information, identical values, uniform tie-breaking, one prize, and a normalized cap of one. It gives no classification of asymmetric equilibria, no equilibrium-selection result, and no revenue-optimality claim. The literature comparison is not an exhaustive survey of every unpublished thesis or non-indexed working paper.

## References

1. Oleg Muratov, “All-Pay Auctions with Reserve Price and Bid Cap,” University of Bern Discussion Paper 21-06, public version dated 23 April 2021. https://repec.vwiit.ch/dp/dp2106.pdf
2. Ivan Pastine and Tuvana Pastine, “Equilibrium existence and expected payoffs in all-pay auctions with constraints,” *Economic Theory* 75 (2023), 983–1007. https://doi.org/10.1007/s00199-022-01433-5
3. Nora Szech, “Tie-breaks and bid-caps in all-pay auctions,” *Games and Economic Behavior* 92 (2015), 138–149. https://doi.org/10.1016/j.geb.2015.05.008
