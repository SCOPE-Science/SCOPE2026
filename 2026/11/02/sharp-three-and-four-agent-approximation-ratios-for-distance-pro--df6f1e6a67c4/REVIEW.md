# Scientific assessment: finite-population Global Pair approximation factors

## Correctness — PASS

The proof treats every metric space and repeated reports, separately handles \(Z=0\) and zero optimal cost, and never requires an optimal comparator facility pair to be attained. For three clients the exact weighted numerator reduces to \(u(2v+w)\) for ordered side lengths \(u\le v\le w\), and the optimum equals \(u\). For four clients, any comparison facilities lead to nonempty \((1,3)\) or \((2,2)\) clusters. The \((1,3)\) bound uses the explicitly proved triangle-weight lemma; the \((2,2)\) bound uses direct pair-cost accounting. The limiting line configurations independently establish sharpness. The attached exact-integer checker passed all indicated finite experiments, including a fifth possible facility point. Risk: the finite enumeration does not certify universal correctness; that burden is borne by the written proof.

## Originality — PASS, with residual literature risk

The exact claims were compared with the primary definitions, approximation theorems, proof arguments, and relevant specializations in Ma–Peng (arXiv:2608.09061), Chan–Lin–Wang (arXiv:2608.22484), and Jia (arXiv:2608.19633). These sources provide global factor-four bounds for the same two-facility sampling rule, including a demonstration of asymptotic tightness as populations grow; none of their identified statements supplies the separate sharp \(n=3\) and \(n=4\) factors. The available bibliographic searches for small-population two-facility distance-proportional sampling did not identify a matching assertion; their closest retrieved records concerned different metric invariants or assignment rules. Risk: nonindexed, inaccessible, or differently named exact small-population results could exist. Neither negative searches nor partitioning demonstrate absolute novelty.

## Mathematical value — PASS

The parameter is the standard worst-case efficiency factor of a prominently studied strategyproof-location sampling rule, not an arbitrary special-case statistic. The exact small-population theorem shows that the known factor-four general bound is not predictive even for four agents; the four-agent bound applies in arbitrary metric geometry and requires a new weighted triangle inequality. Sharp real-line instances show the constants cannot be improved. Risk: the result does not extend to five agents or imply broader strategic incentives; these are explicit scope restrictions, not hidden claims.

## Relationship and limitations

The contribution is a precise finite-population efficiency refinement rather than a new algorithm, strategyproofness claim, or general population result. Source links and reproducibility instructions appear in `RESULT.md`. Independent review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
