# Sharp minimum-blocker cutoff in \(K_{a,2}\) fractional hedonic games

## Finding

**Theorem (complete phase diagram and sharp blocker-size threshold).** For each integer \(a\ge 2\), consider the simple symmetric fractional hedonic game on \(K_{a,2}\). For any partition \(\pi\), let \(s(\pi)\) denote the minimum size of a coalition strictly improving the payoff of every participating agent, and set \(s(\pi)=\infty\) if there is no such coalition.

The value of \(s(\pi)\) is exactly as follows, regardless of the grouping of agents in coalitions that contain no agent of the two-vertex type.

1. If the two agents of the two-vertex type belong to one coalition with \(p\) of the \(a\) opposite-type agents, write \(r=a-p\). Then \(\pi\) is core-unstable if and only if \(r\ge\lfloor p/2\rfloor+1\), and in this case
   \[
   s(\pi)=\lfloor p/2\rfloor+2.
   \]
2. If those two agents belong to different coalitions with \(p\ge q\ge0\) opposite-type agents, respectively, write \(r=a-p-q\). Then \(\pi\) is core-unstable if and only if
   \[
   p\ge q+2\quad\text{or}\quad r\ge q+1,
   \]
   and in this case \(s(\pi)=q+2\).

In particular, the maximum smallest blocking-coalition size over **all core-unstable partitions** of \(K_{a,2}\) is
\[
\boxed{\max_{\pi:s(\pi)<\infty}s(\pi)=\left\lfloor\frac a2\right\rfloor+1.}
\]
This cutoff is sharp for every \(a\ge2\). More precisely, put \(q=\lfloor(a-2)/2\rfloor\), \(p=q+2\), and \(r=a-p-q\in\{0,1\}\). Form a coalition with the first special agent and \(p\) ordinary agents, one with the second special agent and \(q\) ordinary agents, and keep the \(r\) remaining agents as singletons. The complete family of blocking coalitions is: the second special agent together with an arbitrary set of \(q+1\) agents outside its initial coalition. Consequently **every** blocking coalition has size \(q+2=\lfloor a/2\rfloor+1\), and their number and uniform probability among all nonempty subsets are exactly
\[
\boxed{\binom{p+r}{q+1}\,,\qquad
\frac{\binom{p+r}{q+1}}{2^{a+2}-1}=O(a^2 2^{-a}).}
\]
Thus linear-size profitable deviations can be exponentially rare.

## Assumptions and scope

The agents consist of \(A\), with \(|A|=a\ge2\), and \(B\), with \(|B|=2\). Pair valuations equal \(1\) between different types and \(0\) within each type (including self-valuations). The utility of an agent in a nonempty coalition \(C\) equals the number of opposite-type agents in \(C\) divided by \(|C|\), **not** divided by \(|C|-1\). A blocking coalition is nonempty and every participant must *strictly* prefer it to its original coalition. Coalitions are unrestricted subsets of agents, not necessarily existing blocks and not graph-theoretic cliques. Partitions may contain arbitrary additional all-\(A\) blocks; these do not affect the theorem because their agents have initial utility zero.

A coalition with \(x\) agents of type \(A\) and \(y\) of type \(B\), with \(x,y>0\), gives new utilities \(y/(x+y)\) to each \(A\)-agent and \(x/(x+y)\) to each \(B\)-agent. Hence comparing the *type-\(A\) density* \(x/(x+y)\) is equivalent to requiring that all participating \(B\)-agents strictly **increase** that density relative to their initial blocks while all participating \(A\)-agents strictly **decrease** it relative to their initial blocks.

## Proof

**Only mixed blocking coalitions matter.** A coalition with one type has zero utility for all participants, so cannot strictly block. Since \(|B|=2\), a potential blocking coalition contains exactly one or exactly two \(B\)-agents. Every \(A\)-agent in an all-\(A\) original block has initial utility \(0\), and hence always strictly improves in a mixed coalition.

**Case I: both \(B\)-agents in one block.** Their common initial block contains \(p\) agents of type \(A\), so its \(A\)-density is \(p/(p+2)\). A coalition containing one \(B\)-agent and \(x\) agents of type \(A\) strictly improves its \(B\)-agent exactly when \(x/(x+1)>p/(p+2)\), equivalently \(x>p/2\). Any original \(A\)-agent from that mixed block would require the reverse comparison on \(A\)-density and therefore cannot participate. Consequently a one-\(B\) blocker exists exactly when the \(r=a-p\) outside agents suffice to supply \(t=\lfloor p/2\rfloor+1\) agents, and its minimum size is \(t+1\).

For a putative two-\(B\) blocker with \(x\) agents of type \(A\), each \(B\)-agent strictly improves exactly when \(x/(x+2)>p/(p+2)\), i.e. \(x>p\). No agent of type \(A\) from the original mixed block can then strictly improve, so all \(x\) must be among the \(r\) outside agents. If this is possible, then \(r>p\ge\lfloor p/2\rfloor+1-1\), which also implies existence of a **smaller** one-\(B\) blocker of size \(t+1\). Thus the stated instability criterion and exact minimum are exhaustive, including \(p=0\).

**Case II: the two \(B\)-agents in different blocks.** Call them \(b_p\) and \(b_q\), where the first has \(p\) same-block \(A\)-agents and the second \(q\), with \(p\ge q\ge0\); the remaining \(r=a-p-q\) agents belong to all-\(A\) blocks. Their current type-\(A\) densities are \(p/(p+1)\) and \(q/(q+1)\), respectively. A one-\(B\) coalition containing \(b_q\) and \(x\) agents of type \(A\) strictly improves \(b_q\) if and only if \(x>q\). Such a coalition may draw its \(A\)-agents from the \(p\)-block only when \(x<p\), because these agents' new utility \(1/(x+1)\) must strictly exceed \(1/(p+1)\). It cannot draw any from the \(q\)-block, since \(x>q\) contradicts their required \(x<q\). Agents in all-\(A\) blocks are eligible without restriction. Therefore, a blocker with \(b_q\) exists if and only if \(p\ge q+2\) or \(r\ge q+1\): if the former holds, take \(q+1\) agents from the \(p\)-block; if the latter, take \(q+1\) from outside. Conversely, if \(p\le q+1\) and \(r\le q\), a coalition with \(b_q\) cannot gather the necessary \(q+1\) eligible agents.

A one-\(B\) blocker containing \(b_p\) requires \(x>p\); agents from either existing mixed block then cannot improve, so its \(A\)-agents must be from the \(r\) outside agents and \(r\ge p+1\ge q+1\). Hence its existence implies the already-listed \(b_q\) blocker. A two-\(B\) blocker requires \(x>2p\) from the preference of \(b_p\). At that density no \(A\)-agent from either mixed original block can strictly improve, so all \(x\) are outside and \(r>2p\ge q\), again implying \(r\ge q+1\). No other blockers exist. Finally any blocker with \(y\in\{1,2\}\) agents of type \(B\) must strictly improve at least one \(B\)-agent whose current density is at least \(q/(q+1)\); hence \(x/(x+y)>q/(q+1)\), so \(x>qy\) and \(x+y\ge q+2\). This matches the explicit \(b_q\) blocker above and proves the exact minimum and phase diagram.

**Sharp global cutoff.** In Case I, the existence of a blocker gives \(a=p+r\) with \(r\ge\lfloor p/2\rfloor+1\). For positive even \(p=2u\), this yields \(a\ge3u+1\ge2u+2\), and for odd \(p=2u+1\) it yields \(a\ge3u+2\ge2u+2\). The boundary \(p=0\) gives the minimum \(2\le\lfloor a/2\rfloor+1\). Thus \(\lfloor p/2\rfloor+2\le\lfloor a/2\rfloor+1\) whenever the partition is unstable. In Case II, if \(p\ge q+2\), then \(a\ge p+q\ge2q+2\). Otherwise instability requires \(r\ge q+1\) and hence \(a\ge3q+1\ge2q+2\) for \(q\ge1\); for \(q=0\), the assumed \(a\ge2\) suffices. Thus \(q+2\le\lfloor a/2\rfloor+1\).

**Sharpness and exact rarity.** In the explicit construction, \(p=q+2\), \(r\le1\). By Case II, every blocker has size at least \(q+2\). A blocking coalition containing only \(b_q\) needs \(x>q\). It may use \(A\)-agents from the \(p\)-block only while \(x<p=q+2\); with at most \(r\le1\) other eligible agents, this forces \(x=q+1\). Any set of \(q+1\) agents chosen from the \(p+r\) agents outside the \(q\)-block is eligible, giving exactly \(\binom{p+r}{q+1}\) blockers. A blocker using only \(b_p\) would require at least \(p+1>r\) outside agents; a two-\(B\) blocker would require more than \(2p\) outside agents. Neither exists. Hence the blocker family is exact, not only a lower bound. Since \(p+r=q+2+r\) and \(r\in\{0,1\}\), its cardinality is at most \(\binom{q+3}{2}=O(a^2)\), proving the stated probability estimate and equality in the global cutoff.

## Verification

Run the standalone standard-library-only checker as `python verify.py`. It independently enumerates every set partition of the \(a+2\) **labeled** agents for \(2\le a\le6\), and every mixed candidate subset, checking strict utility inequalities by integer cross multiplication. It compares the actual minimum blocking size with both cases of the phase diagram, checks the sharp global maximum, and enumerates **every blocker** for the sharpness construction. Observed: 5,287 labeled partitions processed and 217,392 strictly blocking subsets identified; all assertions pass. The checker is a finite corroboration only; the proof above establishes the unbounded quantifiers.

## Relationship to prior work

Aziz et al. introduced the game and treated the complete multipartite “Bakers and Millers” setting, proving that equal type ratios suffice for strict-core stability and that the grand coalition lies in the strict core. Their characterization concerns **weakly** blocking deviations for the strict core and neither bounds the minimum **strictly** blocking coalition in an arbitrary unstable partition nor optimizes this minimum over partitions. Fanelli, Monaco and Moscardelli introduced coalition-size-relaxed core stability; their general convergence and welfare results do not establish this sharp two-special-agent cutoff. Demeulemeester and Peters analyze improvement factors conditional on coalition size; those estimates do not specify the size of the smallest strictly improving coalition on \(K_{a,2}\). Fioravanti et al. study uniformly sampled blockers and exponentially small fractional-core error on general games; their inspected relevant sections and appendices do not give this complete two-type phase diagram. An earlier general fixed-partition polynomial for the size-resolved number of strictly blocking coalitions on \(K_{a,b}\) can be specialized to compute the distribution for a **given** partition. The present claim concerns the sharp **global optimization across every partition** when one type has exactly two agents and provides its own direct proof; no new general fixed-partition counting formula is claimed.

## Limitations

The bound is specific to complete bipartite unit valuations with one side of exactly two agents, coalitions unrestricted by connectivity, utility normalized by total coalition size, and all deviations strictly beneficial. It makes no statement for arbitrary multipartite networks, asymmetric preferences, weak blocking or the denominator \(|C|-1\). The exact minimum for a stable partition is not finite by definition. Computation checks finite sizes only. Identical specialist precedence has not been ruled out, and independent external audit has not been performed.

## References

1. H. Aziz, F. Brandl, F. Brandt, P. Harrenstein, M. Olsen, D. Peters, *Fractional Hedonic Games*, arXiv:1705.10116 (first released 2017-05-29), §5.3, https://arxiv.org/abs/1705.10116 .
2. A. Fanelli, G. Monaco, L. Moscardelli, *Relaxed Core Stability in Fractional Hedonic Games*, IJCAI 2021, https://doi.org/10.24963/ijcai.2021/26 .
3. T. Demeulemeester, J. Peters, *Relaxed Core Stability for Hedonic Games with Size-Dependent Utilities*, MFCS 2023, https://doi.org/10.4230/LIPIcs.MFCS.2023.41 .
4. S. Fioravanti, M. Flammini, B. Kodric, G. Varricchio, *\(\varepsilon\)-fractional Core Stability in Hedonic Games*, arXiv:2311.11101 (first released 2023-11-18), https://arxiv.org/abs/2311.11101 .
