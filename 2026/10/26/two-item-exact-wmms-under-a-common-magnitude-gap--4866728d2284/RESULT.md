# Two-item exact WMMS under a common magnitude gap

## Finding

Let agents \(1,2\) have positive entitlements \(w_1,w_2>0\), and let the indivisible items be \(x,y\). Valuations are additive and each singleton value belongs to \(\{-1\}\cup[1,\infty)\): an item is either worth exactly \(-1\) or is worth at least \(1\) to each agent. For the weighted maximin share

\[
W_i=w_i\max_{(P_1,P_2)}\min\left\{\frac{v_i(P_1)}{w_1},\frac{v_i(P_2)}{w_2}\right\},
\]

where \((P_1,P_2)\) ranges over ordered partitions of \({x,y}\) and empty parts are allowed, there is always a complete allocation \(A=(A_1,A_2)\) such that \(v_i(A_i)\ge W_i\) for both agents. Therefore, for the restricted alphabet \(\{-1,1,r\}\) with \(r>1\), a two-agent failure of exact WMMS needs at least three items; a three-item failure is already known.

## Assumptions and scope

There are exactly two agents and two indivisible items. Each entitlement is strictly positive; they need not sum to one. Valuations are additive, and every singleton value is either \(-1\) or at least \(1\). No zero singleton values are allowed. The WMMS definition uses ordered, entitlement-labelled partitions and permits an empty bundle. An allocation is complete: each item is assigned to exactly one agent. The result does not claim existence for arbitrary mixed-manna valuations, for more than two items, or for more than two agents.

## Proof

Write \(W_i\) for agent \(i\)'s WMMS and \(j\ne i\) for the other agent. For every partition, the minimum of the two normalized bundle values is at most their weighted average, so

\[
W_i\le \frac{w_i}{w_1+w_2}\bigl(v_i(x)+v_i(y)\bigr). \tag{1}
\]

Also, if agent \(i\) has at least one singleton value \(-1\), then \(W_i\le0\): a split partition has a negative-valued singleton in one part, while a partition with an empty part has minimum at most zero.

**Case 1: both items are positive for at least one agent.** If exactly one agent, say \(i\), values both items positively, give both items to \(i\) and leave \(j\) empty. By (1), \(W_i\le \frac{w_i}{w_1+w_2}(v_i(x)+v_i(y))<v_i(x)+v_i(y)\); meanwhile \(W_j\le0\). The allocation is WMMS-fair.

If both agents value both items positively, let \(p_i=\max\{v_i(x),v_i(y)\}\) and \(q_i=\min\{v_i(x),v_i(y)\}\). Directly evaluating the two split partitions gives

\[
W_i=\begin{cases}
\min\{p_i,(w_i/w_j)q_i\},&w_i\ge w_j,\\
\min\{q_i,(w_i/w_j)p_i\},&w_i\le w_j.
\end{cases}
\tag{2}
\]

Thus \(W_i\le p_i\) for every agent, and \(W_i\le q_i\) for an agent whose entitlement is no larger than the other's. If the agents have different favorite items, give each their favorite. If they have a common weakly preferred item, give that item to an agent with the larger entitlement and the other item to the lower-entitlement agent. Formula (2) verifies both WMMS inequalities, including ties.

**Case 2: neither agent values both items positively, but some agent has one positive item.** Such an agent has values \(p,-1\) with \(p\ge1\), so the total value is nonnegative. Putting both items in one part and leaving the other part empty gives WMMS at least zero; every split has a negative part, hence this agent's WMMS is exactly zero. Give both items to this agent. The other agent has WMMS at most zero and receives the empty bundle, so both inequalities hold.

**Case 3: all four singleton values equal \(-1\).** Relabel agents so that \(q=w_1/w_2\ge1\). Evaluating the two split partitions and the two partitions with an empty part gives

\[
W_1=-\min\{2,q\},\qquad W_2=-\min\{1,2/q\}. \tag{3}
\]

If \(q\ge2\), give both items to agent \(1\): their utility is \(-2=W_1\), while agent \(2\) receives zero, at least \(W_2\). If \(1\le q\le2\), split the items one each. Both utilities are \(-1\), which is at least \(W_1=-q\) and equals \(W_2=-1\). The case \(w_2>w_1\) follows by relabeling. These cases exhaust all permitted valuation profiles.

The three-item sharpness statement follows from the explicit example in Teh (2026): for any \(r>1\), entitlements \(w_1=1/(2r+1)\), \(w_2=2r/(2r+1)\) and valuations \(v_1=(-1,1,r)\), \(v_2=(1,r,r)\) have \(W_2=2r\) and \(W_1>0\). To give agent \(2\) value at least \(2r\), the allocation must give that agent both \(r\)-valued items (or all three); agent \(1\) then receives value \(-1\) or zero, below \(W_1\). Thus the two-item theorem makes three the minimum obstruction size in this alphabet.

## Verification

The proof evaluates all four ordered partitions in each sign case; no numerical approximation is used in (1)--(3). The bundled \(`verify.py`\) performs a finite exact-arithmetic sanity check over all \(3^4=81\) valuation matrices from \(\{-1,1,2\}\) and seven rational entitlement ratios. This finite test is supplementary only and is not used to infer the theorem for all real weights or all positive magnitudes. The three-item obstruction is verified algebraically from the cited source; no independent audit has been performed.

## Relationship to prior work

Teh's 2026 paper proves that exact WMMS can fail for two agents and three items with singleton values in \(\{-1,1,r\}\), for every \(r>1\), but does not state the two-item guarantee proved here. Aziz, Chan, and Li (2019) give a two-agent, two-item counterexample for unrestricted chore valuations; their negative singleton magnitudes differ across items/agents, so that example lies outside the present restriction. The current theorem is deliberately narrow: it establishes a sharp item-count boundary for the recent three-item example, not a general two-item WMMS theorem.

## Limitations

The result depends on the common negative magnitude and the gap between \(-1\) and all positive singleton values. The older two-item chore counterexample shows that two-item exact WMMS can fail once these restrictions are removed. No claim is made for valuation alphabets containing unequal negative magnitudes, values strictly between \(-1\) and \(1\), zero values, or for more than two items or agents. The literature search was bounded; absence of an exact-match search result is not proof of novelty.

## References

1. Nicholas Teh, *Weighted Fair Division of Indivisible Mixed Manna*, arXiv:2609.01580v2 (2026), definition of WMMS and Proposition 4.7, especially the three-item construction. Earliest public version: arXiv:2609.01580v1, 2026-09-01.
2. Haris Aziz, Hau Chan, and Bo Li, *Weighted Maxmin Fair Share Allocation of Indivisible Chores*, arXiv:1906.07602v1 (2019), Section 4, two-agent/two-item chore counterexample.
