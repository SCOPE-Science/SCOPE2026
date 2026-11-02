# Scientific review

## Correctness — PASS

The claim is finite and exhaustively resolved. The verifier enumerates all \(46{,}656\) labeled three-pair profiles, all six perfect matchings for each, and all twelve single-agent adjacent swaps, yielding \(559{,}872\) scenarios. It directly reconstructs stability from every possible blocking pair after each swap, independently tests the previously established local shift criterion for every original stable matching, and asserts their agreement. Exact counters reproduce the eight joint cells, position-conditioned failures and two-pair comparison. Its complete loops establish exhaustiveness; no inference from sampled cases or floating point arithmetic is required.

## Originality — PASS, with residual priority risk

The closest full texts, Mai–Vazirani (2018) and Gangam–Mai–Raju–Vazirani (2026), cover the *same perturbation model* and prove structural/algorithmic robustness and the local blocking-pair criterion. Their results do not specify the simultaneous-stability joint census, the \(245/1944\) failure law or the top-versus-bottom failure asymmetry. This is a new exact finite statistic rather than a new algorithm or proof of the known shift lemma. Existing small-market stable-matching counts address the initial number of stable matchings but do not determine their intersection after a shock. A more obscure prior exact enumeration cannot be excluded.

## Value — PASS

Robustly preserving at least one stable outcome under minimal preference changes is a direct, economically motivated question. The first market with up to three stable outcomes permits a nontrivial joint classification: robustness failure drops from \(1/4\) in the two-pair market to \(245/1944\) with three pairs; a top-rank change is substantially more destructive than a lower-rank change; and no three-stable market loses all robust outcomes. The result is a complete exact probability law for this natural small-market boundary, not an arbitrary extracted digit or an unsupported prediction about larger markets.

## Closest literature and limitations

Primary sources: https://arxiv.org/html/1804.00553v4 and https://arxiv.org/html/2601.07959v1. The sources establish robustness under adjacent promotions; the present contribution is the exact finite probability distribution. The result assumes strict, complete preferences, independent uniformly distributed labeled rankings and one uniformly chosen adjacent swap; it does not extrapolate to larger or correlated markets. Independent literature priority and independent scientific validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
