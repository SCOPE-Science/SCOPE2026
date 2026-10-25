# A sharp finite-improvement dichotomy for multi-action conformist–rebel network games

## Finding

**Finite-improvement dichotomy.** Let \(G=(V,E)\) be any finite simple undirected graph, with vertices typed as conformists (C), rebels (R), or stubborn players (S). Every non-stubborn vertex chooses an action from the same finite set \(A\) of size \(m\ge3\); stubborn vertices have fixed actions. Suppose the distinct actions used by all stubborn vertices number at most \(m-2\). Conformists earn one per neighbor with an equal action, while rebels earn one per neighbor with a different action. Then this strategic game has the **finite improvement property** (every sequence of unilateral strictly profitable changes is finite) **if and only if no edge joins a conformist to a rebel**.

Moreover, the graph on three vertices with edges \(\{S,C\}\) and \(\{C,R\}\), a stubborn action \(0\), and action set \(\{0,1,2\}\) has both a pure Nash equilibrium and a directed four-step strict-improvement cycle. At most two vertices cannot exhibit this coexistence; for this same three-vertex graph with just two actions, every strict-improvement sequence terminates. Thus the game may have an equilibrium yet fail the finite improvement property, even in its smallest qualifying population.

## Assumptions and scope

A finite simple graph has vertex types \(\tau:V\to\{C,R,S\}\). Each vertex of type S is fixed to a specified color \(s_v\in A\), and every other vertex chooses one action \(x_v\in A\). For an edge \(\{v,w\}\), equality means the two endpoints have the same action. The utility of a conformist \(v\) is \(u_v(x)=\sum_{w\sim v}\mathbf1_{x_w=x_v}\). A rebel's utility is \(u_v(x)=\sum_{w\sim v}\mathbf1_{x_w\ne x_v}\). Stubborn vertices do not deviate. A strict-improvement step changes one non-stubborn action and strictly increases that player's payoff, with no restriction that the move be a *best* response. The finite improvement property (FIP) quantifies over **every** sequence of such steps and every starting profile; for finite games it is equivalent to absence of directed cycles in the strict-improvement graph. No independence, randomness, connectivity, or degree assumptions are made.

The cardinality bound on fixed stubborn actions means that there exist at least two distinct colors which no stubborn vertex uses. This condition, rather than the number of stubborn vertices, is needed for the converse. The assertion does not characterize cases with fewer than two such unused colors.

## Proof

**(1) No cross-type edge implies FIP.** Define

\[
\Phi(x)=\sum_{\{v,w\}\in E:\,\tau(v),\tau(w)\in\{C,S\},\ \{\tau(v),\tau(w)\}\ne\{S\}}\mathbf1_{x_v=x_w}
+\sum_{\{v,w\}\in E:\,\tau(v),\tau(w)\in\{R,S\},\ \{\tau(v),\tau(w)\}\ne\{S\}}\mathbf1_{x_v\ne x_w}.
\]

Here the first sum includes C–C and C–S edges, and the second R–R and R–S edges; S–S edges contribute no term. When no C–R edge exists, these cover every payoff-relevant edge. Upon changing the action of a non-stubborn vertex, all terms not incident to it cancel. Each incident term changes by exactly its contribution to that vertex's payoff, including on like-typed edges. Therefore \(\Delta\Phi=\Delta u_v\) for every unilateral move by a flexible player. In every strict-improvement step the integer \(\Phi\) increases by at least one. Since \(0\le\Phi\le |E|\), no such sequence can be infinite: FIP holds.

**(2) One cross-type edge prevents FIP.** Suppose \(\{u,v\}\in E\), where \(u\) is a conformist and \(v\) a rebel. Select distinct actions \(a,b\in A\) absent from the stubborn players' fixed actions. Because \(m\ge3\), choose a third action \(d\in A\setminus\{a,b\}\). Give every other flexible vertex action \(d\), leaving the stubborn vertices fixed. Thus no neighbor of either \(u\) or \(v\), other than the other endpoint, has action \(a\) or \(b\). Keeping all other actions fixed, consider the directed cycle

\[
(u,v)=(a,b)\to(b,b)\to(b,a)\to(a,a)\to(a,b).
\]

The mover is alternately \(u,v,u,v\). Conformist \(u\) acquires the match across \(\{u,v\}\) at its two moves, and rebel \(v\) acquires a mismatch across that edge at its two moves. At every step, matches or mismatches to all other neighbors remain unchanged (because those neighbors use neither \(a\) nor \(b\)). Accordingly each move increases its mover's utility by **exactly one**. All four joint profiles are distinct. This is an infinite strict-improvement trajectory by repetition, so FIP fails. Notice that this reasoning does not assert any absence of pure Nash equilibria.

**(3) Smallest coexistence witness.** Take a path \(S-C-R\), with the stubborn vertex fixed at \(0\), and actions \(\{0,1,2\}\). With vertex order \((S,C,R)\), profile \((0,0,1)\) is a pure Nash equilibrium: the conformist has one match from S and one mismatch from R, so actions \(0\) and \(1\) each yield payoff one (action \(2\) yields zero); the rebel receives one from mismatching the conformist, its maximum possible payoff. The four configurations

\[
(0,1,2)\to(0,2,2)\to(0,2,1)\to(0,1,1)\to(0,1,2)
\]

form a strict-improvement cycle of gain one at every step, as proved in (2). With at most two vertices, any nontrivial cross-type edge must be C–R and then the two endpoints require simultaneously equality and inequality to be satisfied; thus no pure Nash equilibrium exists. With no cross-type edge, the potential from (1) supplies FIP. An isolated or stubborn-only second vertex does not alter this dichotomy. Finally, on the same path with actions \(\{0,1\}\), the three nonabsorbing pairs \((C,R)=(1,1),(1,0),(0,0)\) admit the unique successive improvements \((1,1)\to(1,0)\to(0,0)\to(0,1)\). The fourth pair \((0,1)\) is an equilibrium; hence no improvement cycle is possible on this binary path.

This proves all assertions.

## Verification

The accompanying standalone `verify.py` checks the payoff changes independently from the defining neighbor sums. It enumerates \(6600\) graph/type/action combinations on two through four labeled vertices, including \(4812\) cross-type cyclic cases, and checks \(203904\) exact potential-difference identities. It additionally verifies the pure-equilibrium witness and both stated small-size boundaries. Run with `python3 verify.py` (only the Python standard library is required). These finite tests corroborate the argument but do not replace the arbitrary-graph proof above.

## Relationship to prior work

Pei, Cao, and Zhang, *On the Existence of Pure Nash Equilibria in Networks with Multi-Strategy Conformist and Rebel Players* (arXiv:2607.10997v1, first available 2026-07-13), define this general multi-action network model and prove static equilibrium statements, including sufficient exact-potential conditions when opposite types do not interact. The sufficient half of our dichotomy follows directly from that potential perspective. The distinguishing assertion here is the **necessity** of eliminating all C–R edges for the *universal, all-paths* FIP when two stubborn-unused actions exist, including coexistence of a stationary equilibrium and improvement cycles on the three-vertex path. It does not follow from a theorem guaranteeing existence of at least one equilibrium.

Cao, Sánchez, and Zhang, *Conformists, Rebels and Stubborn Agents: Opinion Dynamics in Social Networks* (arXiv:2607.05932v1), consider two actions and related network/opinion dynamics. The constructive necessity above is specific to the additional action freedom and is not implied by the binary model. Earlier binary best-response work, including Cao et al.'s *Dynamic matching pennies on networks*, makes cycles natural, but does not supply this exact universal multiaction-and-pinned-action characterization in the materials checked.

## Limitations

FIP is a worst-case property: an available strict-improvement cycle does not establish that a randomly scheduled trajectory enters it, nor that every starting profile cycles. The exhibited cycle uses strict improvements rather than requiring every move to be a maximally improving response. We do not classify arbitrary heterogeneous action sets, weighted or directed edges, games in which stubborn vertices consume all but one action, or all binary games. No unindexed-literature priority or independent certification is claimed.

## References

1. Pei, Cao, Zhang (2026), *On the Existence of Pure Nash Equilibria in Networks with Multi-Strategy Conformist and Rebel Players*, arXiv:2607.10997v1, https://arxiv.org/html/2607.10997v1 .
2. Cao, Sánchez, Zhang (2026), *Conformists, Rebels and Stubborn Agents: Opinion Dynamics in Social Networks*, arXiv:2607.05932v1, https://arxiv.org/abs/2607.05932 .
3. Cao et al. (2019), *Dynamic matching pennies on networks*, *International Journal of Game Theory*, DOI:10.1007/s00182-019-00665-5 .
