# Cyclic stable matchings: exact historical selection and a one-person rescue

## Finding

For every integer \(n\geq 3\), there is a fully acceptable strict \(n\)-by-\(n\) marriage market with exactly \(n\) stable matchings but only two reachable from an initially empty market by any history that repeatedly enters or exits **only terminal agents**, with stable proposal-chain repair after each event. The reachable proportion is exactly \(2/n\), arbitrarily close to zero. A single temporary man, with an extension preserving every terminal agent's relative order of terminal partners, suffices to reach the first interior matching. For that interior target the minimum number of temporary historical participants is therefore exactly one. At \(n=3\), the same fixed augmentation reaches every stable matching by choosing different histories.

The three claims are simultaneous statements about the **same** explicitly defined family and the **same** historical transition rule. The temporary-man result does not assert that one temporary agent suffices for every interior matching when \(n>3\).

## Assumptions and scope

Fix \(n\geq3\). Indices are elements of \(\mathbb Z/n\mathbb Z\), represented by \(0,\ldots,n-1\). The terminal men are \(m_0,\ldots,m_{n-1}\), and terminal women are \(w_0,\ldots,w_{n-1}\). Every original man and woman finds every opposite-sex terminal agent acceptable; preferences are strict. For each \(i,j\), the preference orders are

\[
 m_i:\quad w_i\succ w_{i+1}\succ\cdots\succ w_{i+n-1},\qquad
 w_j:\quad m_{j+1}\succ m_{j+2}\succ\cdots\succ m_{j+n-1}\succ m_j.
\]

A matching is stable if it is individually rational and no mutually acceptable pair strictly prefers each other to their present partners, treating being unmatched as worse than any acceptable match. Let \(\mu_r(m_i)=w_{i+r}\), for \(0\leq r<n\).

A **terminal-agent history** starts with the empty active set and empty matching. Each step enters one currently absent terminal agent or exits one currently present terminal agent. The current stable matching is repaired by the standard proposal chain: an entering unmatched agent, or the abandoned former partner after an exit, proposes to acceptable active agents in descending order; an acceptor keeps its preferred partner, displacing the former partner to continue the chain, until no proposal remains. The process is required to be stable after each event. An outcome is terminally reachable when all \(2n\) terminal agents are present and the matching has the stated value. Arbitrarily many exit/reentry events are allowed, but no additional agents.

An **augmented history** may also contain temporary agents absent at termination. Adding temporary agents may insert their names into terminal preference lists but may not change the relative order of two terminal partners. The number of temporary agents counts distinct extra people, not entries.

## Proof

**1. The terminal market has exactly the \(n\) shifts.** Each \(\mu_r\) is stable. Under \(\mu_0\) every man has his first choice. For \(1\le r<n\), a man \(m_i\) prefers \(w_{i+s}\) to his assigned \(w_{i+r}\) exactly when \(0\le s<r\). Woman \(w_{i+s}\) is assigned to \(m_{i+s-r}\); in her preference order this current partner precedes \(m_i\), since its cyclic offset from her index is \(n-r\), whereas the offset of \(m_i\) is \(n-s\) when \(s>0\), and is the last position when \(s=0\). Thus she cannot form a blocking pair.

Conversely, a stable matching is perfect: if there were an unmatched man and an unmatched woman, they would block. For each man write his partner as \(w_{i+r_i}\) with the unique displacement \(r_i\in\{0,\ldots,n-1\}\). Let \(r=\min_i r_i\), attained at \(i=a\). If \(r=n-1\), all displacements are \(n-1\). Otherwise the woman \(w_{a+r}\) is married to \(m_a\) and prefers \(m_{a-1}\) to \(m_a\). Relative to \(m_{a-1}\), this woman is at displacement \(r+1\). If \(r_{a-1}>r+1\), they block; if \(r_{a-1}=r+1\), both men would be assigned to \(w_{a+r}\), which is impossible. Hence \(r_{a-1}\le r\), forcing equality by minimality. Apply the same argument around the cycle to obtain \(r_i=r\) for every \(i\). Therefore every stable perfect matching is one of the \(\mu_r\).

**2. Every one-agent-deleted terminal market has a unique stable matching.** Delete a man \(m_a\). Exactly one woman is unmatched. It must be \(w_a\): if \(w_j\) were unmatched for \(j\ne a\), the present man \(m_j\), who ranks \(w_j\) first, would block. Because \(w_a\) is unmatched, \(m_{a-1}\), whose first and second choices are \(w_{a-1}\) and \(w_a\), must have \(w_{a-1}\). Repeating backward, with higher choices either already occupied or the unmatched \(w_a\), forces \(m_i\) to match \(w_i\) for every \(i\ne a\). This restriction of \(\mu_0\) is stable (restriction of a stable matching), so it is the unique stable submarket outcome.

Delete a woman \(w_a\). Exactly one man is unmatched, and it must be \(m_{a+1}\): if \(m_k\) were unmatched with \(k\ne a+1\), the present woman \(w_{k-1}\), who ranks \(m_k\) first, would block. The unmatched \(m_{a+1}\) is acceptable to every woman. Woman \(w_{a-1}\), who ranks \(m_a\) first and \(m_{a+1}\) second, must receive \(m_a\); otherwise she and the unmatched \(m_{a+1}\) block. Next \(w_{a-2}\) must receive \(m_{a-1}\): her only preferred alternatives to unmatched \(m_{a+1}\) are \(m_{a-1}\) and \(m_a\), and the latter is occupied. Continuing backward determines every matched pair and yields precisely the restriction of \(\mu_{n-1}\), with \(m_{a+1}\) unmatched. The last pair, if not forced by a blocking inequality, is forced by one-to-one feasibility. The restriction is stable, so the submarket outcome is unique.

**3. Historical reachability equals the two extremes.** In any terminal-only history, a full terminal state first appears only after the entry of the last absent terminal agent. Immediately before this final entry, there are \(2n-1\) terminal agents. Section 2 says its matching is uniquely a restriction of \(\mu_0\) if a man is absent, or of \(\mu_{n-1}\) if a woman is absent. The arriving man in the first case takes \(w_a\), his top choice, and no proposal continues; the arriving woman in the second case takes \(m_{a+1}\), her top choice, and no proposal continues. The full matching is thus \(\mu_0\) or \(\mu_{n-1}\). This reasoning applies to **every** reappearance of the full market, however many previous entries and exits have occurred. Both extremes actually occur: enter all women first and then all men to obtain \(\mu_0\), or enter all men and then all women to obtain \(\mu_{n-1}\). Thus exactly two of the \(n\) stable terminal matchings are reachable under terminal-only histories.

**4. An explicit one-person preference-preserving rescue.** Add one temporary man \(t\). He finds only \(w_0\) acceptable. Woman \(w_0\) finds him acceptable and inserts him immediately before her least preferred original man \(m_0\), so that

\[
 w_0:\quad m_1\succ m_2\succ\cdots\succ m_{n-1}\succ t\succ m_0.
\]

No other ranking is altered. Enter all original women, then \(t\), then original men in order \(m_0,m_1,\ldots,m_{n-1}\). Initially \(t\) holds \(w_0\). Upon entering, \(m_0\) is refused by \(w_0\), which prefers \(t\), and takes unmatched \(w_1\). For \(1\le i\le n-2\), man \(m_i\) first proposes to \(w_i\), then held by \(m_{i-1}\), whom \(w_i\) prefers to \(m_i\); he is rejected and takes still-unmatched \(w_{i+1}\). Finally \(m_{n-1}\) is rejected by \(w_{n-1}\) and proposes to \(w_0\), which prefers him to \(t\). He displaces \(t\), leaving \(t\) unmatched. This gives exactly \(\mu_1\) on original agents. Exit the unmatched \(t\); the terminal matching stays \(\mu_1\).

At each prefix the displayed matching is stable. Every entered original man has either his second-choice woman or, before any men enter, is absent. His only preferred woman is his own-index woman, which is held by \(t\) (for \(m_0\)) or by \(m_{i-1}\), preferred to \(m_i\), until \(t\) is displaced. Following the displacement, \(w_0\) prefers \(m_{n-1}\) to \(m_0\), and \(t\) has no acceptable blocking partner. Thus each event is an admissible stable proposal-chain step and the final unmatched-agent exit changes no match.

By part 3, \(\mu_1\) is unreachable with zero temporary agents since \(n\ge3\). The displayed history uses exactly one, proving the minimum is one. The same augmented preference profile still admits histories using only terminal agents to reach \(\mu_0\) and \(\mu_{n-1}\) (simply never enter \(t\)). In particular at \(n=3\), when these are the only other stable matchings, one fixed temporary agent permits historical reachability of the entire stable set. \(\square\)

## Verification

The standalone file `verify_cyclic_histories.py` uses only the Python standard library. It independently enumerates every perfect matching for \(2\le n\le7\), proving by computation only for these finite sizes that the stable set is the set of shifts. It exhaustively enumerates all dynamically reachable intermediate states, allowing repeated exits and reentries, for \(3\le n\le6\) without the auxiliary agent, and for \(3\le n\le5\) with the auxiliary agent. It also replays the constructive one-person entry/exit sequence for \(3\le n\le50\), checking stability after every event and the final shift-one matching. The exact program output reports 10,886 counted finite checks; no computation is used as proof of the quantified all-\(n\) statements.

Reproduce with `python3 verify_cyclic_histories.py` from the same directory as this file.

## Relationship to prior work

Yang's *Stable Matchings and Their Histories: Historical Reachability under Population Shocks* (2026) proves a three-by-three terminal-only reachability obstruction and provides preference-preserving temporary-agent reachability for arbitrary targets using a larger construction. The three-by-three negative phenomenon is therefore **not** claimed as new. The present statement adds an all-size exact stable-set/reachable-set law, a vanishing exact reachable fraction, and a one-person **minimum** for the first interior target, with a common one-person augmentation covering all stable matchings in the three-by-three member.

Cheng's *On the Stable Matchings That Can Be Reached When the Agents Go Marching in One By One* (2016) studies reachability under entry-only random-order mechanisms and provides necessary conditions for such histories. Entry-only obstructions cannot by themselves establish impossibility under arbitrary repeated exit and reentry; the one-agent-deleted submarket argument establishes the latter. Ma's earlier ROM study similarly concerns entry-only reachability. A separate study of reachable stability lattices after population shocks addresses different one-sided many-to-many shock maps rather than the exact mixed-side, repeated-event histories here.

## Limitations

The exact \(2/n\) fraction concerns this explicitly constructed cyclic preference family, not all stable-marriage markets or random profiles. The one-person optimality concerns the single target \(\mu_1\), not every target in every market. The mechanism assumes strict preferences, all original cross-side pairs acceptable, entry/exit of one agent at a time, and stable proposal-chain continuation. A different history rule may have a different reachable set. Publication-priority risk remains because unindexed or not fully retrievable literature could contain an equivalent construction. No external independent mathematical audit is claimed.

## References

1. Yi-You Yang, *Stable Matchings and Their Histories: Historical Reachability under Population Shocks*, 2026, arXiv:2609.20176, https://arxiv.org/abs/2609.20176.
2. Christine T. Cheng, *On the Stable Matchings That Can Be Reached When the Agents Go Marching in One By One*, SIAM Journal on Discrete Mathematics 30 (2016), 2047–2063, DOI:10.1137/140996690.
3. Jin-Peng Ma, *On Randomized Matching Mechanisms*, Economic Theory 8 (1996), 377–381.
4. Yi-You Yang, *Reachable Stability Lattices after Population Shocks*, arXiv:2305.17948 (first public 2023, later revised).
