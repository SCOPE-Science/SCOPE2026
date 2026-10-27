# Square-root retention and a noncommuting zero-penalty equilibrium limit in a three-person delegation cycle

## Finding

Consider the three-person fractional-delegation game defined below. It has no pure-strategy Nash equilibrium at zero delegation penalty, even though each agent may choose **any real self-retention fraction** in \([0,1]\). For every positive penalty \(0<\varepsilon<1\), it has exactly one **symmetric** pure-strategy Nash-equilibrium retention level. Writing \(t=1-\varepsilon\), this level is

\[
q_\varepsilon=\begin{cases}
\dfrac{\sqrt{(t-t^3)^2+t^3(1-t^3)}-(t-t^3)}{t^3},&0<\varepsilon<1/2,\\[4pt]
1,&1/2\le\varepsilon<1.
\end{cases}
\]

In particular, \(q_\varepsilon/\sqrt\varepsilon\to\sqrt3\) as \(\varepsilon\downarrow0\). Although these equilibria converge to the all-delegate (all-zero-retention) profile, at which all three votes are void in the unpenalized model, their actual penalized voting weights converge to one vote for **each** agent and zero void votes. Thus taking an equilibrium and removing the regularization cannot be interchanged with removing the regularization first.

## Assumptions and scope

There are three agents indexed cyclically, with successor \(i+1\) and predecessor \(i-1\), indices modulo three. The available **pure strategic choices** for agent \(i\) comprise a continuous segment: choose \(r_i\in[0,1]\), retain fraction \(r_i\) of any voting mass reaching them, and delegate the remaining fraction \(1-r_i\) to their successor. The directed trust network restricts them to these actions; no agent can directly delegate to their predecessor.

At each visit to an agent, a particle of voting mass is sent to a null sink with probability \(\varepsilon\), and otherwise performs that agent's retain-or-delegate action. Retention means consumption by the agent. For \(0<\varepsilon<1\) this is the per-step geometric penalty in Bersetche's fractional-delegation voting weight measure. At \(\varepsilon=0\), any mass caught in a closed nonretaining cycle counts as null voting mass, as in that paper's limiting measure \(V\).

Each agent's payoff concerns the destination of **their own unit of originating voting mass**, not the aggregate voting power of all origins: value \(2\) for consumption by the successor, value \(1\) for consumption by oneself, and value \(0\) for consumption by the remaining agent or the null sink. These are nonnegative, cyclically symmetric and place each agent's trusted successor above herself. The Nash concept holds the other agents' retention fractions fixed under unilateral deviation. A symmetric equilibrium has \(r_1=r_2=r_3\); uniqueness below is asserted **only within this symmetric class**.

## Proof

**1. Exact utility.** Write \((a,b,c)=(r_1,r_2,r_3)\) and \(t=1-\varepsilon\). Starting from agent 1, the first consumption probabilities at agents 1 and 2 respectively are \(ta\) and \(t^2(1-a)b\). After a complete unconsumed circuit the particle returns to agent 1 with survival weight \(t^3(1-a)(1-b)(1-c)\). Summing the geometric series, for \(0<\varepsilon<1\),

\[
U_1^{\varepsilon}(a,b,c)=\frac{ta+2t^2(1-a)b}{1-t^3(1-a)(1-b)(1-c)}.
\]

The other two payoffs are obtained by cyclically permuting \((a,b,c)\). The denominator is strictly positive for every profile when \(\varepsilon>0\). For \(\varepsilon=0\), the same formula holds at every profile other than \((0,0,0)\); at that exceptional profile the entire circulation is void and all three payoffs are zero.

**2. Exact best-response sign.** Differentiating with respect to agent 1's own retention gives

\[
\frac{\partial U_1^\varepsilon}{\partial a}=
\frac{t\bigl[1-t^3(1-b)(1-c)-2tb\bigr]}
{\bigl[1-t^3(1-a)(1-b)(1-c)\bigr]^2}.
\]

Thus the player's derivative has a sign independent of their own retention. At \(\varepsilon=0\), for profiles where the denominator is defined, the sign reduces to that of
\[
G_1=c(1-b)-b,\quad G_2=a(1-c)-c,\quad G_3=b(1-a)-a.
\]

Whenever a best-responding player chooses positive retention, the corresponding \(G_i\) must be nonnegative; whenever the player chooses zero retention and can vary it within a nonsingular neighborhood, \(G_i\) must be nonpositive.

**3. Nonexistence at zero penalty.** The all-zero profile fails Nash stability: any player may retain her vote and raise her payoff from \(0\) to \(1\). At a profile with exactly one positive retention, say \(a>0,b=c=0\), player 2 has \(G_2=a>0\) and can profitably change from \(b=0\) to \(b>0\). At a profile with exactly two positive retentions, say \(a,b>0,c=0\), player 1 has \(G_1=-b<0\) and can profitably lower \(a\). At a profile with all retentions positive, Nash stability requires \(G_1,G_2,G_3\ge0\), hence
\[
b\le \frac{c}{1+c}<c,\qquad c\le\frac{a}{1+a}<a,\qquad a\le\frac{b}{1+b}<b,
\]

an impossibility. Cyclic relabeling exhausts all possible supports. Therefore there is no unpenalized equilibrium anywhere in the full strategy cube \([0,1]^3\).

**4. Positive-penalty symmetric equilibrium.** Set the two opponents' fractions to \(q\). The common own-action derivative has sign
\[
F_t(q):=1-t^3(1-q)^2-2tq.
\]

For \(0<t<1\), the function is strictly decreasing in \(q\in[0,1]\), because \(F_t'(q)=2t^3(1-q)-2t<0\); moreover \(F_t(0)=1-t^3>0\) and \(F_t(1)=1-2t\).

If \(0<\varepsilon<1/2\) (equivalently \(t>1/2\)), these endpoint signs are opposite, so a unique root lies in \((0,1)\). Because the own-action derivative is identically zero at this root, **every own retention fraction is a best response**, including \(q\) itself. Solving the quadratic equation
\[
t^3q^2+2(t-t^3)q-(1-t^3)=0
\]

gives the displayed \(q_\varepsilon\). If \(1/2\le\varepsilon<1\), \(F_t(1)\ge0\), so retaining everything is a best response to opponents who retain everything. Strict monotonicity excludes any interior symmetric fixed point. At \(\varepsilon=1/2\) the unique symmetric fixed point is again \(q=1\). This proves the entire symmetric phase diagram, without claiming that asymmetric equilibria are unique or absent.

**5. Sharp small-penalty scaling.** As \(\varepsilon\downarrow0\), \(1-t^3=3\varepsilon+O(\varepsilon^2)\) and \(t-t^3=2\varepsilon+O(\varepsilon^2)\). Substituting into the exact root formula yields
\[
q_\varepsilon=\sqrt{3\varepsilon}+O(\varepsilon),
\qquad\lim_{\varepsilon\downarrow0}\frac{q_\varepsilon}{\sqrt\varepsilon}=\sqrt3.
\]

**6. The noncommuting voting-power limit.** At the symmetric profile each agent receives one unit of fresh originating mass, and the total expected mass reaching each agent before consumption is the common value \([1-t(1-q_\varepsilon)]^{-1}\). Thus each individual real voting weight, and the total null voting weight, are respectively
\[
V_i^\varepsilon=\frac{tq_\varepsilon}{\varepsilon+tq_\varepsilon},\quad(i=1,2,3),
\qquad
V_{\mathrm{null}}^\varepsilon=\frac{3\varepsilon}{\varepsilon+tq_\varepsilon}.
\]

Since \(\varepsilon/q_\varepsilon\to0\), the voting-weight vector tends to \((1,1,1,0)\). More precisely, \(1-V_i^\varepsilon=\sqrt{\varepsilon/3}+O(\varepsilon)\). But the retention profiles tend to \((0,0,0)\); at exactly that profile the zero-penalty measure assigns \((0,0,0,3)\), because no particle can ever be retained. These limits differ, as asserted.

## Verification

The accompanying standalone Python checker, `verify_fractional_cycle.py`, uses symbolic algebra to confirm the derivative numerator, its unpenalized reduction and the symmetric indifference polynomial. It also checks four positive-penalty roots, unilateral-payoff constancy, two supercritical endpoint tests, and all 124 nonzero profiles on a five-point rational grid against the necessary zero-penalty best-response signs. The exact arguments in Sections 2–6, not finite enumeration or floating-point output, establish the universal theorems. Reproduction: install the dependency in `requirements.txt` and run `python verify_fractional_cycle.py`.

## Relationship to prior work

Bersetche, *Generalizing Liquid Democracy to multi-agent delegation: A Voting Power Measure and Equilibrium Analysis* (first arXiv submission September 28, 2022, arXiv:2209.14128), defines the fractional delegation measure, the per-hop penalty and its zero-penalty limit. Its Theorem 4.1 guarantees existence for every positive penalty; Remark 6 allows convex network-restricted delegation faces. Its Appendix A.3 already exhibits **nonexistence of an unpenalized fractional-delegation equilibrium in a different two-agent example with some negative utility weights**. Therefore neither regularized existence nor generic zero-penalty nonexistence is claimed as new here.

Escoffier, Gilbert and Pass-Lanneau, *The Convergence of Iterative Delegations in Liquid Democracy in a Social Network* (arXiv:1904.05775), already provide a three-agent cyclic guru-preference example with **no equilibrium in the binary classical-delegation model**. The cyclic qualitative preference obstruction is thus also prior work. The present result pertains instead to the continuous self-retention strategy cube with nonnegative cardinal values and gives the explicit **positive-penalty symmetric equilibrium branch, square-root law, critical penalty and noncommuting equilibrium/voting-weight limits**. We did not identify those quantitative statements in the inspected primary texts. The underlying network restriction and cardinal payoffs are essential.

Brill and coauthors, *Liquid Democracy with Ranked Delegations* (2022, DOI:10.1609/aaai.v36i5.20417), consider ranked fallback delegates and delegation selection, not the same geometric damping plus fractional-retention equilibrium branch.

## Limitations

The result classifies **symmetric** equilibria for positive penalties, not all asymmetric equilibria. The zero-penalty nonexistence statement assumes the specified directed trust graph and cardinal preferences; it is not an assertion about all delegation games or all nonnegative utilities. Voting weights are those of the absorbing fractional-delegation rule, not election-outcome probabilities. The asymptotic statement concerns \(\varepsilon\downarrow0\), not the convergence of best-response learning dynamics. The literature comparison supports best-knowledge originality, not independent proof of global priority.

## References

1. F. M. Bersetche, *Generalizing Liquid Democracy to multi-agent delegation: A Voting Power Measure and Equilibrium Analysis*, arXiv:2209.14128, first submitted September 28, 2022, https://arxiv.org/abs/2209.14128 (Sections 2–4, Appendix A.3).
2. B. Escoffier, H. Gilbert, A. Pass-Lanneau, *The Convergence of Iterative Delegations in Liquid Democracy in a Social Network*, arXiv:1904.05775, https://arxiv.org/abs/1904.05775 (Example 2, Observation 1).
3. M. Brill, T. Delemazure, A.-M. George, M. Lackner, U. Schmidt-Kraepelin, *Liquid Democracy with Ranked Delegations*, AAAI 2022, DOI:10.1609/aaai.v36i5.20417.
