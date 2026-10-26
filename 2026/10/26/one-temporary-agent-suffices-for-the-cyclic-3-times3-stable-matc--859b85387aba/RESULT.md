# One temporary agent suffices for the cyclic \(3\times3\) stable-matching obstruction

## Finding

For the complete strict marriage market below, the middle stable matching is impossible under histories using only the six terminal agents, even if those agents may repeatedly enter and exit. It becomes reachable when exactly one temporary woman is allowed to enter and then exit. Thus the minimum temporary population for this specific market-target pair is exactly \(1\).

Write the men as \(m_1,m_2,m_3\) and the women as \(w_1,w_2,w_3\). The original preference lists, from best to worst with the unmatched option last, are

\[
\begin{aligned}
m_1 &: w_1\succ w_2\succ w_3\succ\emptyset,\\
m_2 &: w_2\succ w_3\succ w_1\succ\emptyset,\\
m_3 &: w_3\succ w_1\succ w_2\succ\emptyset,\\
w_1 &: m_2\succ m_3\succ m_1\succ\emptyset,\\
w_2 &: m_3\succ m_1\succ m_2\succ\emptyset,\\
w_3 &: m_1\succ m_2\succ m_3\succ\emptyset.
\end{aligned}
\]

The three stable matchings are
\[
\begin{aligned}
\mu_A&=\{(m_1,w_1),(m_2,w_2),(m_3,w_3)\},\\
\mu_0&=\{(m_1,w_2),(m_2,w_3),(m_3,w_1)\},\\
\mu_B&=\{(m_1,w_3),(m_2,w_1),(m_3,w_2)\}.
\end{aligned}
\]
Every agent receives their second-ranked original partner in \(\mu_0\).

## Assumptions and scope

A matching is stable if it is individually rational and no unmatched man-woman pair both prefer each other to their current assignments. All nine original cross-side pairs are acceptable. A terminal-agent history starts empty, changes the active population by one original agent at a time, and after each entry or exit applies the proposal-chain continuation until the active market is stable. In an augmented history, one additional woman \(a\) may participate temporarily, with the relative order of every original agent's preferences over original partners and \(\emptyset\) unchanged; \(a\) must be absent at the terminal date.

The result is specific to this one \(3\times3\) market and target \(\mu_0\). It is not a general bound for larger markets or for many-to-one matching.

## Proof

**No temporary agent is insufficient.** The full market has exactly the three stable matchings listed above. The other three perfect matchings, \(\{(m_1,w_1),(m_2,w_3),(m_3,w_2)\}\), \(\{(m_1,w_2),(m_2,w_1),(m_3,w_3)\}\), and \(\{(m_1,w_3),(m_2,w_2),(m_3,w_1)\}\), are blocked respectively by \((m_3,w_1)\), \((m_2,w_3)\), and \((m_1,w_2)\); a stable matching cannot leave an original man and woman both unmatched. For each of the six five-agent submarkets, direct stability checks give the unique stable matching in the table. The final column is the result of the entering agent's proposal chain.

| Missing terminal agent | Unique stable matching in the five-agent submarket | Outcome when the missing agent enters |
|---|---|---|
| \(m_1\) | \(\{(m_2,w_2),(m_3,w_3)\}\) | \(\mu_A\) |
| \(m_2\) | \(\{(m_3,w_3),(m_1,w_1)\}\) | \(\mu_A\) |
| \(m_3\) | \(\{(m_1,w_1),(m_2,w_2)\}\) | \(\mu_A\) |
| \(w_1\) | \(\{(m_1,w_3),(m_3,w_2)\}\) | \(\mu_B\) |
| \(w_2\) | \(\{(m_2,w_1),(m_1,w_3)\}\) | \(\mu_B\) |
| \(w_3\) | \(\{(m_3,w_2),(m_2,w_1)\}\) | \(\mu_B\) |

For example, if \(m_1\) is missing, both remaining men must be matched; otherwise an unmatched man and an unmatched acceptable woman block. Women \(w_2\) and \(w_3\) cannot be unmatched because \(m_2\) and \(m_3\) respectively rank them first and would block with them. Thus the unique stable matching is \(\{(m_2,w_2),(m_3,w_3)\}\). If \(w_1\) is missing, \(m_1\) cannot be unmatched because \(m_1\) and \(w_3\) block, and \(m_3\) cannot be unmatched because \(m_3\) and \(w_2\) block. The two women must therefore be matched to \(m_1\) and \(m_3\); the alternative assignment \(m_1-w_2,m_3-w_3\) is blocked by \((m_2,w_3)\). Hence the unique stable matching is \(\{(m_1,w_3),(m_3,w_2)\}\), leaving \(m_2\) unmatched. Cyclic relabeling gives the other four rows.

Consider the first time a terminal-agent history reaches the full six-agent market with matching \(\mu_0\). Its immediately preceding event must be the entry of the last missing agent into one of these five-agent submarkets. The table shows that this entry always yields \(\mu_A\) or \(\mu_B\), never \(\mu_0\). Earlier exits and re-entries cannot change this final-entry obstruction. Hence zero temporary agents cannot suffice.

**One temporary woman is sufficient.** Add \(a\), with preference list \(m_1\succ\emptyset\succ m_2\succ m_3\), so that she finds only \(m_1\) acceptable. Extend the men's lists to
\[
\begin{aligned}
m_1 &: w_1\succ w_2\succ a\succ w_3\succ\emptyset,\\
m_2 &: w_2\succ a\succ w_3\succ w_1\succ\emptyset,\\
m_3 &: w_3\succ a\succ w_1\succ w_2\succ\emptyset.
\end{aligned}
\]
These insertions preserve the original order of all original partners and the unmatched option. The original women's lists remain unchanged.

Enter \(m_1,m_2,m_3\), then \(w_1,w_2,w_3\). The women enter by proposing to their respective top choices, producing \(\mu_B\). Next, let \(a\) enter. Her proposal chain is
\[
a\to m_1\ (\text{accept}),\quad
w_3\to m_1\ (\text{reject}),\quad
w_3\to m_2\ (\text{accept}),\quad
w_1\to m_2\ (\text{reject}),\quad
w_1\to m_3\ (\text{accept}),\quad
w_2\to m_3\ (\text{reject}),\quad
w_2\to m_1\ (\text{accept}),\quad
a\to m_1\ (\text{reject}).
\]
The accepted proposals displace the previous partners in the displayed order. At the end, the matching is \(\mu_0\) and \(a\) is unmatched. She has no other acceptable partner, so the chain ends. This augmented matching is stable: \(\mu_0\) is stable among original agents; \(m_1\) prefers \(w_2\) to \(a\); and although \(m_2\) and \(m_3\) rank \(a\) above their target partners, \(a\) finds them unacceptable. Exit \(a\) next. Since she is unmatched, the matching does not change and remains stable. The terminal market is exactly the original market with matching \(\mu_0\).

The no-temporary-agent obstruction and the one-agent construction together prove the exact minimum \(1\).

## Verification

The standalone checker `verification/check_history.py` uses only the Python standard library. It enumerates all matchings and filters them by individual rationality and absence of blocking pairs; verifies the three full-market stable matchings and uniqueness of all six five-agent submarkets; applies the entry proposal chain to each missing terminal agent; and checks the explicit one-temporary-woman history after every population event. It completed with:

`PASS: exactly three stable matchings; all six five-agent submarkets have unique stable matchings; every terminal-agent final-entry transition misses the middle matching; one temporary woman realizes it; the minimum temporary-agent count is exactly 1.`

The mathematical proof above supplies the infinite-history exclusion: it quantifies over any finite terminal-agent history by considering its first full-market occurrence of \(\mu_0\). The finite checker is a reproducibility aid for the explicitly defined finite market, not a substitute for that argument.

## Relationship to prior work

Yang's *Stable Matchings and Their Histories: Historical Reachability under Population Shocks* proves that terminal-agent histories can fail to reach a stable matching and gives a preference-preserving construction using a larger temporary population. Its discussion explicitly leaves minimization of the number of historical agents open. The present claim sharpens that count to exactly one for its cyclic \(3\times3\) obstruction pattern.

Cheng's work on the random-order mechanism studies entry-only histories and includes the same cyclic stable-marriage profile; the auxiliary agents in its complexity construction remain in the terminal instance. That result does not imply reachability using a temporary agent who exits before termination. Ma's earlier random-order result likewise concerns the entry-only mechanism, not the augmented history used here. This is a case-specific quantitative refinement, not a solution to the general minimum-augmentation problem.

## Limitations

The exact minimum is established only for the stated strict complete \(3\times3\) profile and target \(\mu_0\). No general minimum-agent formula, asymptotic bound, common augmentation for all stable matchings, or extension to general hospital choice functions is claimed. The primary preprint record's displayed date string conflicts with the month encoded by its identifier; the explicit displayed date is retained, and either interpretation lies in the same recent-date window.

## References

1. Yi-You Yang, “Stable Matchings and Their Histories: Historical Reachability under Population Shocks,” arXiv:2609.20176v1 (2026), §§2–6.
2. Christine T. Cheng, “On the Stable Matchings That Can Be Reached When the Agents Go Marching in One By One,” *SIAM Journal on Discrete Mathematics* 30 (2016), 2047–2063. DOI: 10.1137/140996690.
3. Jinpeng Ma, “On randomized matching mechanisms,” *Economic Theory* 8 (1996), 377–381. DOI: 10.1007/BF01211824.
