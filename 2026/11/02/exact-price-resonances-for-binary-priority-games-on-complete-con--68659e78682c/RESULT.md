# Exact price resonances for binary priority games on complete conflict graphs

## Finding

For every integer \(n\ge 2\), consider the complete-conflict priority game with bids \(s_i\in\{0,1\}\), fixed-index tie breaking, and a uniform positive price \(c\) per high-priority bid. The total number \(E_n(c)\) of pure Nash equilibria is exactly
\[
E_n(c)=\begin{cases}
2,&c\in\{1,\ldots,n-1\},\\
1,&c>n-1,\\
0,&0<c<n-1\text{ and }c\notin\mathbb Z.
\end{cases}
\]
For each integer price \(r\in\{1,\ldots,n-1\}\), the two equilibria can be written explicitly as follows. A word of type Z has a prefix of \(t\) zeros followed by the alternating word \(1,0,1,0,\ldots\). Include this word for each \(t\in\{2r-n+1,2r-n+2\}\cap\{1,\ldots,n\}\). A word of type O has a prefix of \(t\) ones followed by \(0,1,0,1,\ldots\). Include this word for each \(t\in\{n-2r,n-2r-1\}\cap\{1,\ldots,n-1\}\). Exactly two of these possibilities are valid, with no duplicates. In the Z family, \(t=n\) denotes the all-zero profile.

## Assumptions and scope

There are \(n\ge2\) distinct agents indexed \(0,1,\ldots,n-1\). Every pair conflicts, so all agents appear in a common service order. Agent \(i\) chooses a priority level \(s_i\in\{0,1\}\). Larger levels are served earlier; agents choosing equal levels are ordered by ascending index. Let \(r_i(s)\) denote the number of agents preceding \(i\) in this order. With fixed \(c>0\), the utility of agent \(i\) is \(u_i(s)=-r_i(s)-cs_i\). A pure Nash equilibrium is a profile from which no agent can strictly increase their utility by switching their own level. Indifference is therefore permitted. Both payoff units and the tie-breaking convention are essential to the stated thresholds.

## Proof

For a fixed opponent profile define the integer
\[
A_i(s)=\#\{j<i:s_j=0\}+\#\{j>i:s_j=1\}.
\]
Raising agent \(i\)'s level from zero to one overtakes precisely the earlier-index agents at zero and later-index agents at one. Therefore, independently of \(s_i\),
\[
u_i(1,s_{-i})-u_i(0,s_{-i})=A_i(s)-c.
\]
Consequently, a profile is an equilibrium precisely when
\[
s_i=0\implies A_i(s)\le c,
\qquad s_i=1\implies A_i(s)\ge c.
\tag{1}
\]
A direct cancellation gives the adjacent-index identity
\[
A_{i+1}(s)-A_i(s)=1-s_i-s_{i+1}.
\tag{2}
\]

Suppose the profile contains a switch between adjacent indices. At a switch the two adjacent values of \(A\) are equal by (2). Since one index bids zero and the other bids one, (1) forces that common value to equal \(c\). Because it is an integer, every equilibrium containing a switch has an integer price \(c=r\). Moreover the profile must alternate from the first switch onward: after a \(0,1\) transition at \(A=r\), repeating the one would make the next \(A\) equal to \(r-1\), violating (1); after a \(1,0\) transition, repeating the zero would make the next \(A\) equal to \(r+1\), also violating (1). Applying the same reasoning successively proves alternation for the entire suffix.

Thus any equilibrium with a switch is either a prefix of \(t\ge1\) zeros followed by \(1,0,1,\ldots\), or a prefix of \(t\ge1\) ones followed by \(0,1,0,\ldots\). In the first case, the transition value is
\[
A_{t-1}=t-1+\left\lceil\frac{n-t}{2}\right\rceil
=\left\lfloor\frac{n+t-1}{2}\right\rfloor.
\]
It equals \(r\) precisely for \(t=2r-n+1\) or \(t=2r-n+2\). In the second case the transition value is
\[
A_{t-1}=\left\lfloor\frac{n-t}{2}\right\rfloor,
\]
which equals \(r\) precisely for \(t=n-2r\) or \(t=n-2r-1\). For these words, \(A_i\) rises through the all-zero prefix or falls through the all-one prefix to \(r\) and stays at \(r\) throughout the alternating suffix. Every candidate within the specified range consequently satisfies (1). These are all the switched equilibria.

The two constant words require separate consideration. For the all-zero word, \(A_i=i\), so (1) holds precisely if \(c\ge n-1\). In the all-one word, the last-index agent has \(A_{n-1}=0<c\), so the word is never an equilibrium at positive price. The valid Z formula permits \(t=n\) exactly when \(r=n-1\); thus the all-zero case at this boundary is already counted once.

Finally, count the candidates at each integer \(1\le r\le n-1\). Put \(h=2r-n\). If \(h\ge0\), the two valid Z-prefix lengths are \(h+1\) and \(h+2\), and no O-prefix length is valid. If \(h=-1\), the valid lengths are one Z length and one O length, both equal to one but producing different first bids. If \(h\le-2\), the valid O-prefix lengths are \(-h\) and \(-h-1\), and there is no valid Z length. Hence exactly two equilibria exist at each integer price. If \(c\) is noninteger, no switched equilibrium exists, leaving only all zeros when \(c>n-1\). At positive integers greater than \(n-1\) the all-zero word is likewise the only equilibrium. The displayed formula follows. \(\square\)

## Verification

The standalone file `verify.py` independently constructs the service order in every one-agent deviation and exhausts all binary profiles for \(2\le n\le11\) and half-integer price grids extending above the maximum threshold. Its expected equilibrium sets are generated separately from the explicit candidate-word formulas. It also checks the exact unilateral-gain identity for every profile with \(2\le n\le9\). Running `python3 verify.py` produced:

`VERIFY_OK game_instances=150 scanned_profiles=90104 exact_gain_identites=8192`

This finite computation is a consistency test, not a substitute for the proof covering all \(n\) and every real \(c>0\).

## Relationship to prior work

Lin, Lan, Nguyen and Kawahara define the same priced-priority model in their 2026 article. Their supplementary Proposition S44 proves nonexistence for \(0<c<1\) on any nonempty conflict graph and gives the exact condition for the all-zero profile to be an equilibrium. Their manuscript does not state the present complete-conflict, two-level phase diagram with a complete list and count of equilibria for all positive prices. In particular, their arbitrary-graph findings are not asserted to be new here. The distinct 2008 ranking-games study of Brandt, Fischer, Harrenstein and Shoham defines payoffs determined by ranking rather than an additional chosen-bid fee. The new statement is specific to a complete conflict graph, exactly two priority levels, deterministic index tie breaking, and a common linear bid fee.

## Limitations

The theorem does not classify partial conflict graphs, priority spaces with three or more levels, heterogeneous fees, non-index tie breaking, mixed equilibria, learning dynamics, or equilibrium welfare. The absence of an equivalent result in inspected literature is not proof of worldwide publication priority; unindexed or differently formulated results remain possible. The proof and verifier have not undergone independent mathematical audit.

## References

1. Z. Lin, J. Lan, A.-T. Nguyen and Y. Kawahara, *Priority Coordination Games: Hodge Decomposition and a Sharp Design Limit*, arXiv:2610.05832v1, first publicly posted 2026-10-05, Section II, Section III-B/C and Appendix S-D, Proposition S44. https://arxiv.org/html/2610.05832v1
2. F. Brandt, F. Fischer, P. Harrenstein and Y. Shoham, *Ranking Games*, preprint dated 2008-10-23, Sections 1 and 4. https://ai.stanford.edu/~shoham/www%20papers/rankinggames_journal.pdf
3. R. Hassin and M. Haviv, *Equilibrium Threshold Strategies: The Case of Queues with Priorities*, Operations Research 45 (1997), 966–973, doi:10.1287/opre.45.6.966. This stochastic-queue model is distinct from the deterministic complete-conflict allocation considered above.
