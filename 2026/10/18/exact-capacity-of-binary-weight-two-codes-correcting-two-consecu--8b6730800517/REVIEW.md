# Scientific review

## Correctness — PASS

The theorem specifies its alphabet, exact-two-adjacent-deletion channel, fixed Hamming weight and blocklength range. The upper bound uses exactly \(n-2\) available weight-one outputs: adjacent supports each consume at least one, gap-two supports consume one, and larger gaps consume two. All adjacent supports also share the all-zero output. A second, independent weight-two-descendant collision prohibits near supports with starting indices two apart; their starts form the independent sets of two disjoint paths. The resulting ceiling is \(\lfloor3(n-1)/4\rfloor\). The constructive lower bound lists all output-weight possibilities and has eight mutually exclusive ordered residue patterns for surviving weight-two supports, while its weight-one supports are disjoint. The cardinality of the resulting code is exact for all lengths. The executable checks actual strings but the proof supplies the infinite quantifiers.

## Originality — PASS, with explicitly limited evidence

The most directly relevant primary works establish unrestricted burst-deletion code constructions and bounds (Schoeny et al.; Wang et al.), or constant-weight approaches for ordinary *non-burst* deletion models (Cullina et al.). Their inspected statements, definitions, theorems, and construction descriptions do not imply this optimum for one **exact length-two contiguous deletion** and weight-two source words. The related known weight-two one-deletion capacity formula concerns a different confusability graph. For example, source supports \((0,1)\) and \((2,3)\) at length four are confusable under a two-position burst but not under a one-position deletion; supports \((0,2)\) and \((1,3)\) exhibit the reverse distinction. No equivalent exact all-length fixed-weight-two burst capacity was identified in targeted published-record or terminology searches. This is a best-evidence novelty judgment, not a global literature certification; an unindexed equivalent or omitted section remains possible.

## Mathematical value — PASS

The value is a sharp, infinitely quantified capacity theorem for a natural sparse constant-composition code under a precisely specified synchronization channel. It gives a constructive optimum and a reusable two-tier packing obstruction combining singleton-weight descendants with a path-graph restriction. This is not an arbitrary table increment or merely an alternative parametrization of a known single-deletion bound; the two channel graphs differ in both directions. The result neither determines other weight strata nor characterizes all maximizing codes.

## Closest literature and limitations

Wang, Sima and Farnoud, ISIT 2021, DOI `10.1109/ISIT45174.2021.9517917`; Wang et al., arXiv:2210.11818; Schoeny et al., arXiv:1602.06820; Cullina et al., arXiv:1211.4056. A full-scope novelty certification is not asserted. Exact finite optimization and direct enumeration support numerical boundary tests, not proof beyond their tested ranges. Independent mathematical validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
