# Transition memory creates stable partial cooperation below both static public-goods returns

## Finding
Consider fast state transitions within public-goods groups of size \(g\ge2\), with strategy changes governed by infinite-population well-mixed replicator dynamics. **Without transition memory** (identical sensitivities of high and low game states), the selection gradient is strictly increasing at every composition. Consequently, stable partial cooperation is impossible for **all** group sizes and positive reward factors. Even with memory, two-person games cannot support an attracting mixed equilibrium. Yet the memoryful three-person model admits a robust bistability of full defection and stable partial cooperation even when the normalized synergy factors in **both** component games are below one.

For three-person groups, let \(u=p_1\), \(v=p_2\) be equilibrium probabilities of the high-value environmental state when one or two of three group members cooperate. Put \(\Delta=r_H-r_L>0\), \(H=(1-r_L)/\Delta\), and
\[
F(x)=u+4(v-u)x+3(1+u-2v)x^2.
\]
The evolutionary equation is
\[
\dot x=\Delta x(1-x)[F(x)-H],\qquad 0\le x\le1.
\]
It has two simple mixed equilibria, with the lower repelling, the upper attracting and both full-defection and full-cooperation boundary gradients negative, **if and only if**
\[
4v>3+u,\qquad \max\{u,3-2v\}<H<u+\frac{4(v-u)^2}{3(2v-1-u)}.
\]
Thus in this regime \(x=0\) and the upper interior equilibrium are stable, separated by the lower interior equilibrium; \(x=1\) is repelling from the left.

The sharp group-size witness is
\[
(g,\alpha_1,\alpha_2,r_L,r_H)=(3,1/100,7,3/10,9/10).
\]
Its two mixed equilibrium fractions are approximately \(x_-=0.4651700646\) and \(x_+=0.9719826501\). Both component games have normalized synergy factor less than one, so with a **fixed** environmental game state the cooperative strategy has a negative payoff advantage. The stable mixed state arises from state-dependent group feedback, not from either fixed game.

## Assumptions and scope
A population is infinitely large and well mixed. Each focal individual belongs to independently sampled groups of \(g\) participants, with \(g-1\) co-players independently cooperating at frequency \(x\). Let \(j\) be the number of cooperators in a group. Its state is high (\(H\)) or low (\(L\)); the benefit per cooperator contributed to the *common per-participant payoff* is the normalized factor \(r_H\) or \(r_L\). A cooperator pays cost one. Thus an individual of strategy \(s\in\{0,1\}\) in a group of \(j\) cooperators receives \(r_{\mathrm{state}}j-s\).

At fixed group composition \(j\), environmental transitions are sampled repeatedly and equilibrate before strategies change. A high-state group remains high with probability \((j/g)^{\alpha_1}\); a low-state group becomes high with probability \((j/g)^{\alpha_2}\), where \(\alpha_1,\alpha_2>0\). At intermediate \(j\), this two-state chain is ergodic. At \(j=0,g\), the low and high states, respectively, are absorbing. The resulting high-state stationary probability is
\[
p_j=\frac{(j/g)^{\alpha_2}}{1-(j/g)^{\alpha_1}+(j/g)^{\alpha_2}},\quad 1\le j\le g-1,\qquad p_0=0,\ p_g=1.
\]
We assume \(r_H>r_L>0\), define \(\Delta=r_H-r_L\), and let selection follow \(\dot x=x(1-x)(\pi_C-\pi_D)\). This is a separate **annealed rapid-environment reduction**, not an exact limit theorem for the finite random-hypergraph maximum-earner imitation rule in Wei et al.

## Proof
**Step 1: general gain.** For a focal cooperator with \(k\) cooperating co-players, the expected payoff is \((r_L+\Delta p_{k+1})(k+1)-1\); for a focal defector it is \((r_L+\Delta p_k)k\). Since \(k\sim\mathrm{Bin}(g-1,x)\), their mean difference is
\[
G_g(x)=r_L-1+\Delta\sum_{k=0}^{g-1}\binom{g-1}{k}x^k(1-x)^{g-1-k}d_k,\qquad d_k=(k+1)p_{k+1}-kp_k.
\]
No stationary-distribution averaging is performed at a mixed group composition: every \(p_j\) refers to the actual **integer** group composition, before the binomial co-player average. This distinction is essential.

**Step 2: memoryless obstruction at all group sizes.** If \(\alpha_1=\alpha_2=\alpha>0\), then \(p_j=(j/g)^\alpha\) at every group composition. Hence
\[
d_k=\frac{(k+1)^{\alpha+1}-k^{\alpha+1}}{g^\alpha}.
\]
The function \(t\mapsto t^{\alpha+1}\) is strictly convex on nonnegative reals, so \(d_{k+1}>d_k\) for every \(k\). Differentiating the Bernstein polynomial gives
\[
G'_g(x)=(g-1)\Delta\sum_{k=0}^{g-2}\binom{g-2}{k}x^k(1-x)^{g-2-k}(d_{k+1}-d_k)>0
\]
for every \(0\le x\le1\), including endpoints by continuity. Every interior root, if present, has positive derivative and is repelling. This proves the all-size no-attracting-partial-cooperation statement.

**Step 3: two-player obstruction independent of memory.** For \(g=2\), \(p_0=0\), \(p_2=1\), and \(0<p_1<1\). Thus \(d_0=p_1\), \(d_1=2-p_1>d_0\). The gain is strictly increasing and has no attracting interior zero for **any** positive sensitivities.

**Step 4: sharp three-player criterion.** For \(g=3\), \(d_0=u\), \(d_1=2v-u\), and \(d_2=3-2v\). Taking the binomial average yields the displayed quadratic \(G_3=\Delta(F-H)\). An attracting full-defection state and a repelling full-cooperation state require strict negative boundary gains: \(H>\max\{F(0),F(1)\}=\max\{u,3-2v\}\). Two simple interior zeros with positive gain between them must have a concave quadratic with its vertex in \((0,1)\). The latter is equivalent to \(4v>3+u\), because \(F'(1)=2(3+u-4v)\) and this condition also implies \(F'(0)=4(v-u)>0\). The vertex is
\[
x_{\mathrm v}=\frac{2(v-u)}{3(2v-1-u)}\in(0,1)
\]
and the maximum is \(F(x_{\mathrm v})=u+4(v-u)^2/[3(2v-1-u)]\). The intermediate-value theorem and strict quadratic concavity show that two distinct roots occur **exactly** when the threshold \(H\) is below this maximum and above both boundary values. Their simple crossing derivatives have signs positive then negative, yielding the four equilibrium stability types stated. Equality gives a boundary collision or a double interior root and is deliberately excluded.

**Step 5: exact subunit witness.** Put \(\alpha_1=1/100\), \(\alpha_2=7\). Then
\[
u=\frac{1/2187}{1-3^{-1/100}+1/2187},\qquad v=\frac{128/2187}{1-(2/3)^{1/100}+128/2187}.
\]
We show \(u<1/20\) and \(v>11/12\) without numerical assumptions. Since \(\log3>1\), one has \(1-3^{-1/100}>1-e^{-1/100}>1/101>19/2187\), implying \(u<1/20\). Since \(\log(3/2)<1/2\), one has \(1-(2/3)^{1/100}<1/200\), and \(128/2187>11/200\), implying \(v>11/12\). For \(r_L=3/10\), \(r_H=9/10\), one finds \(\Delta=3/5\), \(H=7/6\). Therefore
\[
F(0)=u<1/20<7/6,\qquad F(1)=3-2v<7/6,
\]
whereas
\[
F(1/2)=3/4+v/2-u/4>287/240>7/6.
\]
As \(F\) is a quadratic, this proves the existence of exactly two simple roots, one on either side of \(1/2\), and all claimed stability conclusions. All inequalities are strict, hence the regime survives sufficiently small parameter changes. The numerical root approximations merely locate the rigorously established roots.

## Verification
The accompanying standard-library Python program independently constructs the Markov stationary values and the three exact gain coefficients; checks agreement of the Bernstein and expanded quadratic forms; confirms the witness interval inequalities and the strict stability signs; and checks the strict-convexity finite-difference inequality for sample group sizes. The full all-size theorem and irrational power inequalities are proved analytically above, not by finite computation. Run `python3 verify.py` with Python 3; no external dependencies are needed.

## Relationship to prior work
Wei, Xiong, Li, Feng and Szolnoki (2026), arXiv:2603.22967, equations (2.1), (2.6), (2.7), introduce the two-state hyperedge game with strategy-dependent transition exponents and study a **different**, finite-population maximum-earner imitation model by simulations. Their analysis motivates, but does not establish, the stated exact annealed fast-state replicator theorem. Su, McAvoy, Wang and Nowak (2019) show that game transitions can favor cooperation in graph-structured weak-selection fixation theory; this known qualitative effect is not claimed. Peña, Lehmann and Nöldeke (2014) develop the general Bernstein/gain-sequence classification for multiplayer replicator games; the standard Bernstein representation, derivative test and general possibility of two interior equilibria are their known framework. The present claim is the **model-specific transition-memory obstruction across every group size**, the exact memoryful three-person parameter window, and the admissible subunit-synergy realization. The proof explicitly reduces to and credits the general gain-sequence method rather than claiming that generic method is new.

## Limitations
The fast environmental equilibrium and random well-mixed grouping are assumptions, not consequences of Wei et al.'s finite-hypergraph stochastic imitation process. The theorem gives local one-dimensional stability and basins for the annealed replicator only; it does not predict network clustering, finite-population fixation, noise-activated transitions, or an exact limiting equivalence to the simulation model. Existing general multiplayer-game theory covers the overarching polynomial method. Earlier application of it to the same Markov stationary game could affect originality; independent review remains outstanding.

## References
1. N. Wei, X. Xiong, Q. Li, M. Feng, A. Szolnoki, “Cooperation in public goods games over uniform random hypergraphs with game transitions,” *J. R. Soc. Interface* 23 (2026), 20251319, doi:10.1098/rsif.2025.1319; first preprint arXiv:2603.22967 (24 March 2026).
2. J. Peña, L. Lehmann, G. Nöldeke, “Gains from switching and evolutionary stability in multi-player matrix games,” *J. Theor. Biol.* 346 (2014), 23–33, doi:10.1016/j.jtbi.2013.12.016; arXiv:1310.0498.
3. Q. Su, A. McAvoy, L. Wang, M. A. Nowak, “Evolutionary dynamics with game transitions,” *PNAS* 116 (2019), 25398–25404, doi:10.1073/pnas.1908936116; arXiv:1905.10269.
