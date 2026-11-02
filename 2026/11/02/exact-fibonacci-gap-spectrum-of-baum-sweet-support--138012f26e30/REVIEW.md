# Review of the exact Baum–Sweet support gap spectrum

## Correctness

PASS. Accepted binary words have the canonical language \(1(1\mid00)^*\), with the number of fixed-length words equal to a Fibonacci number. Every adjacent same-length pair splits at a legal binary prefix; comparing maximal zero-branch and minimal one-branch completions yields the unique formula for each gap, and every pair is exhausted. Cross-length boundaries are separately enumerated. Exact Fibonacci sums complete the histogram; the limiting distribution and divergent mean follow from justified asymptotic ratios. Direct enumeration for all \(2\le M\le16\) passed with support-size, sum-of-frequencies and weighted-sum checks.

## Originality

PASS, qualified. OEIS A060142 already defines the precise set of accepted integer indices and gives its self-generating rule. Merta (2018) studies the same support indices via a Fibonacci-word parity theorem and a recursion for fixed-bit-length sets; its exact differences theorem is for the **different** positions of ones in a formal-power-series inverse. The 2000 Kimberling generator differs, and the 2015 hypertranscendence result treats another invariant. Direct source comparisons and semantic scientific searches found no theorem implying the exact all-dyadic histogram and limiting tail law. This is not a claim that the support itself is new. Complete historical priority is unresolved because the full original 1976 paper could not be inspected.

## Value

PASS. Return gaps between successive ones of an automatic word form a natural and nontrivial local-recurrence invariant. Here a complete Fibonacci multiplicity law for every dyadic cutoff yields an infinite explicit distance spectrum and a heavy-tailed limiting distribution of infinite mean. The structural classification is stronger than finite enumeration or the support's recursive definition.

## Limitations

Only dyadic cutoffs, accepted-one support, and consecutive distances are classified. Frequencies under arbitrary truncations and other automatic sequences are not covered. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
