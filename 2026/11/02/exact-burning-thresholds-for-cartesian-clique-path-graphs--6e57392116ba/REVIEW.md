# Self-review

## Correctness — PASS

The exact product distance identifies full-column intervals of length at most \(2r-1\) and two possible one-row tips. Each unfilled column consumes an endpoint-overlap unit when the clique width is at least four, and all but at most one consume such a unit at width three. The columnwise charging argument proves the lower bounds; constructive tilings and a three-row tip junction attain them. The separate two-round case is checked. The included standard-library verifier independently checks 236 constructive samples, 30 exact burning instances, and 891 endpoint charging cases. This is a proof of all parameter values, not an extrapolation of the tests.

## Originality — PASS, with priority risk

Mitsche, Prałat and Roshanbin (2018), Theorem 7, establish bounds that leave a one-round gap in general; their exactness observation already settles the square-order paths for radius-one factors. Those covered cases are explicitly credited. Antony et al. (2024) treat general structural bounds and computational questions, not an all-order clique–path classification. Other accessible tables cover the width-two ladder, which is excluded. Targeted literature and mathematical research-record comparisons located no exact complete theorem for \(m\ge3\). The complete author-hosted 2018 PDF was not retrievable, although its relevant published theorem and square-case paragraph were compared from indexed original text. Unindexed equivalent work remains possible.

## Mathematical value — PASS

The result solves an infinite two-parameter graph-family invariant exactly and exposes a sharp width-three transition explained by a structural charging principle. This resolves genuinely undecided nonsquare cases beyond the prior general Cartesian-product bounds; merely known square-order instances are not presented as new contributions.

## Limits

Only ordinary vertex burning on \(K_m\square P_n\) with \(m\ge3\), \(n\ge1\) is asserted. No extension to ladder width two, general clique-replaced bases, strong products or other burning variants. Priority remains subject to fuller literature review.

Self-review: passed. Independent audit: not yet performed.
