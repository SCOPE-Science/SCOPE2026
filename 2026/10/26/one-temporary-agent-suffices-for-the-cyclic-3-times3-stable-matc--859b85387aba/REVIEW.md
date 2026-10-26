# Review

## Correctness

The stated market has exactly three stable matchings. Each of its six five-agent submarkets has a unique stable matching, and the last terminal agent's entry produces only the men-optimal or women-optimal matching. The explicit temporary-woman history reaches the middle matching, and her later exit leaves it unchanged. The proof is stated in full in `RESULT.md`; `verification/check_history.py` reproduces the finite checks.

## Originality

The primary paper proves a terminal-agent obstruction and gives a larger general augmentation, but explicitly leaves minimization of temporary-agent counts open. The closest earlier random-order mechanism uses entry-only histories; auxiliary agents in its complexity construction remain in the terminal instance. The exact one-temporary-agent history is not implied by those results. Semantic database searches are supporting evidence only, not proof of novelty.

## Value

This resolves the primary paper's quantitative question for its canonical cyclic \(3\times3\) obstruction: the sharp minimum is \(1\). It is a meaningful, exact case-specific bound, not a general minimum-augmentation theorem.

## Closest literature and limitations

Yang, *Stable Matchings and Their Histories: Historical Reachability under Population Shocks*, arXiv:2609.20176v1, §§3–4 and §6.3. Cheng, *On the Stable Matchings That Can Be Reached When the Agents Go Marching in One By One*, DOI 10.1137/140996690. Ma, *On randomized matching mechanisms*, DOI 10.1007/BF01211824 (abstract checked; full text not obtained). The result is limited to the stated complete strict \(3\times3\) market and target. The primary preprint page's displayed date string conflicts with the identifier month; either interpretation remains in the recent two-year window.

Self-review: passed. Independent audit: not yet performed.
