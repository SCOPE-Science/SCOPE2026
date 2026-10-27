# Moment-matched thresholds switch a binary resource game across three equilibrium regimes

## Finding

For the two-player binary extraction game with payoff \(u_i(h_i,h_j)=b h_i-L\Pr(\Theta_t\le h_i+h_j)\), where \(L>0\), \(b/L=19/50\), and
\[
(\Pr(\Theta_t=1),\Pr(\Theta_t=2),\Pr(\Theta_t=3),\Pr(\Theta_t=4))=(2/5-t,1/10+3t,3/10-3t,1/5+t),\qquad 0\le t\le1/10,
\]
every threshold law has mean \(23/10\) and variance \(141/100\). Nevertheless, the game is coordination for \(0\le t<1/50\), a strict Prisoner’s Dilemma for \(1/50<t<7/75\), and anti-coordination for \(7/75<t\le1/10\). At \(t=1/50\) and \(t=7/75\), one best-response comparison is tied.

## Assumptions and scope

Two players simultaneously choose \(h_i\in\{0,1\}\), where \(0\) means conserve and \(1\) means extract one unit. A common random threshold \(\Theta_t\) destroys the resource exactly when \(\Theta_t\le h_1+h_2\). Each extractor receives private benefit \(b\); each player incurs loss \(L\) if the resource is destroyed. Players maximize expected payoff and are risk-neutral. The claim is a result about this explicitly defined static game, not an empirical prediction about actual resource users.

## Proof

Write the four threshold probabilities as \(q_1=2/5-t\), \(q_2=1/10+3t\), \(q_3=3/10-3t\), and \(q_4=1/5+t\). On \(0\le t\le1/10\), all four are nonnegative. Their sum is one because the coefficient of \(t\) in the sum is \(-1+3-3+1=0\).

The first two moments are constant:
\[
\begin{aligned}
\mathbb E[\Theta_t]&=q_1+2q_2+3q_3+4q_4=23/10,\\
\mathbb E[\Theta_t^2]&=q_1+4q_2+9q_3+16q_4=67/10.
\end{aligned}
\]
In both expressions the coefficient of \(t\) vanishes. Hence \(\operatorname{Var}(\Theta_t)=67/10-(23/10)^2=141/100\) throughout the interval.

Let \(r=b/L=19/50\), \(p_1=\Pr(\Theta_t=1)=2/5-t\), and \(p_2=\Pr(\Theta_t=2)=1/10+3t\). The difference between extracting and conserving when the other player conserves is
\[
u_i(1,0)-u_i(0,0)=L(r-p_1),
\]
and the difference between extracting and conserving when the other player extracts is
\[
u_i(1,1)-u_i(0,1)=L(r-p_2).
\]
Thus the game class is determined by the signs of \(r-p_1\) and \(r-p_2\).

First, \(p_2<r<p_1\) is equivalent to \(t<7/75\) and \(t<1/50\), hence to \(0\le t<1/50\). Conservation is a best response to conservation, while extraction is a best response to extraction, giving the two diagonal pure equilibria of a coordination game.

Second, \(r>p_1\) is equivalent to \(t>1/50\), and \(r>p_2\) is equivalent to \(t<7/75\). Also \(p_1+p_2=1/2+2t>19/50=r\) throughout the parameter interval. Therefore, for \(1/50<t<7/75\), extraction strictly dominates conservation and mutual extraction yields payoff \(L(r-p_1-p_2)<0\), while mutual conservation yields zero. This is a strict Prisoner’s Dilemma.

Finally, \(p_1<r<p_2\) holds exactly when \(7/75<t\le1/10\), so extraction is optimal against conservation and conservation is optimal against extraction. This is anti-coordination. At \(t=1/50\), \(r=p_1\); at \(t=7/75\), \(r=p_2\), producing the stated best-response ties. The phase boundaries and moment identities are exact.

## Verification

The symbolic calculations above prove the claims over the full parameter intervals. The accompanying `verification.py` script uses exact rational arithmetic to check probability normalization, nonnegativity, both moments, and representative points at \(t=0,1/50,1/20,7/75,1/10\). The finite checks are supplementary; the interval classification follows from the displayed inequalities, not from enumeration.

## Relationship to prior work

Maas, Goemans, Manning, Kroll, and Brown (2017) study common-pool resources with uncertain tipping points and report that uncertainty can generate both coordination and Prisoner’s Dilemma incentives. The present claim does not assert that threshold uncertainty or either game class is new. It isolates a different implication: along one explicit family, the first two moments remain exactly fixed while the strategic class changes at exact parameter values. The accessible full text of Dannenberg et al. (2015) studies threshold uncertainty in a repeated public-goods experiment, including a uniform threshold law and an ambiguity treatment; the relevant model and equilibrium discussion do not establish this moment-preserving phase transition. The new statement is the exact moment-preserving family and its transition values, not the general fact that uncertain thresholds can affect coordination.

## Limitations

The result concerns a two-player, binary-action, risk-neutral expected-payoff model with a common threshold and a fixed collapse loss. It does not cover repeated extraction, learning, heterogeneous players, endogenous thresholds, policy instruments, or stochastic resource recovery. It shows that mean and variance alone do not identify the equilibrium regime in this model; it does not claim that these two moments are the only summaries used in applied environmental economics.

## References

1. A. Maas, C. Goemans, D. Manning, S. Kroll, and T. C. Brown, “Dilemmas, coordination and defection: How uncertain tipping points induce common pool resource destruction,” *Games and Economic Behavior* 104 (2017), 760–774. DOI: 10.1016/j.geb.2017.06.009. Official record: https://research.fs.usda.gov/treesearch/55296. First online: 2017-07-04.
2. A. Dannenberg, A. Löschel, G. Paolacci, C. Reif, and A. Tavoni, “On the Provision of Public Goods with Probabilistic and Ambiguous Thresholds,” *Environmental and Resource Economics* 61 (2015), 365–383. DOI: 10.1007/s10640-014-9796-6. Open full text: https://www.lse.ac.uk/granthaminstitute/wp-content/uploads/2014/05/ambiguity-ERE.pdf.
