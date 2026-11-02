# Scientific review

## Correctness — PASS

The universality index equals the number of greedy completed two-letter arches. A prefix/suffix argument proves both inequalities, including the empty word and the possibility of an empty residual suffix. The three-state run-length automaton is exhaustive and yields exactly the stated rational function. Formal coefficient extraction gives the finite binomial formula, and the simple, unique positive dominant pole at \((\sqrt5-1)/2\) yields the first two cumulants and a Gaussian limit. A standalone exhaustive checker compares independent definitions and formulas through length \(16\), with `VERIFY_OK` recorded. The checker supplements rather than replaces the infinite proof.

## Originality — PASS, with residual priority risk

Closest work is the published general regular-language counting algorithm of Adamson et al. (2023), https://arxiv.org/abs/2311.10658, Section 4. It implies the ability to calculate the finite counts from an automaton; therefore computational decidability of those counts is not new. However it does not state the explicit run-two bivariate rational function, closed coefficients or the fixed-source Gaussian law. Adamson's 2023 unrestricted-word enumeration, https://arxiv.org/abs/2304.04583, and the published unrestricted binary-word distribution, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-closed-form-law-for-binary-subsequence-universality--e77c4e8d9f37, have different hypotheses and counts, and neither implies the present restricted-source statistical constants without new analysis. A 2013 Simon-congruence paper and the 2015 Karandikar–Schnoebelen richness-factorization paper (https://arxiv.org/abs/1511.01807) establish the older conceptual foundations; a 2020 edit-distance paper adds algorithms but do not cover the claim. Literature searches did not reveal a specific covering run-two result; unindexed sources remain a risk. Priority is not independently certified.

## Value — PASS

The absence of homogeneous runs of length three is a standard, naturally motivated constrained binary source. The theorem provides the complete joint finite distribution and a quantitative stochastic universality benchmark, changing the mean rate from the unrestricted \(1/3\) to \(1/\sqrt5\) and the variance coefficient from \(2/27\) to \(1-11\sqrt5/25\). The all-length exact law and nondegenerate central-limit theorem give a specific useful structural statistic, not an arbitrary finite slice.

## Limits

The proof covers only linear binary run-two words sampled uniformly at fixed length. A general regular-language counting algorithm already exists. Extensions to weighted or cyclic sources and larger run limits are not claimed; an independent review is outstanding.

Self-review: passed. Independent audit: not yet performed.
