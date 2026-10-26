# Scientific review: exact six-voter fair tie-resolution repairs

## Correctness — PASS

The domain is precisely the \(1024\) monotone, candidate-neutral, resolute six-voter rules that agree with strict majority, identified by ten independent complementary middle-layer choices. For a voter occurring in \(t_i\) of the ten winning triples, the full pivotal count is \(2t_i\), so Banzhaf influence is \(t_i/16\) and Shapley–Shubik influence is \(t_i/30\). Equality under either index is equivalent to all six triple degrees being five. The finite certificate lists all twelve balanced words, checks all 1024 nearest-fair distances and its histogram, and verifies the twelve extremal cases and complete crown adjacency. The exact standalone program passed every assertion; its finite loops do not stand for an infinite search.

## Originality — PASS, with historical-priority uncertainty

The full available 2026 paper by Dhar–Mittal–Thomas gives existence, index formulas, complementary balanced families and the known `Icos` rule, but not the claimed all-orientations repair radius or histogram. The 1999 six-point trade classification already covers possible trade volumes \(4,6,10\) between biplanes, and earlier uniqueness/transitivity of `Icos` is acknowledged; neither conclusion directly classifies distance from the \(1012\) nonfair orientations to the fair locus. Relevant research-record searches concern Banzhaf/Shapley rankings or unrelated codes, without an implication-equivalent full repair profile. Loeb–Conway (2000) was accessible only through abstract and secondary descriptions, and other covering-code literature may provide equivalences. These remain genuine source-coverage risks, not evidence of demonstrated global uniqueness.

## Mathematical value — PASS

This computes the exact minimum number of tie-pair decisions that must be amended to restore both canonical equal-power criteria while leaving every strict-majority outcome intact. The sharp repair radius five, exact repair histogram, exceptional tie-voter characterizations, and fair-rule reconfiguration graph jointly answer a natural finite policy design/robustness question. The result is not the already known existence of a six-player equitable voting game, and does not claim an infinite-family guarantee.

## Scope and limitations

The result is for six **labeled** voters and two alternatives, neutral and monotone rules with strict-majority agreement. An edit changes both complementary tied profiles. The counts cannot be reinterpreted as individual-profile edits or as statements for arbitrary voting rules. The computations use exact integer arithmetic and are reproducible by the embedded checker. Historical priority and independent corroboration remain open.

Self-review: passed. Independent audit: not yet performed.
