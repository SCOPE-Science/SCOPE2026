# Scientific review of the finite paperfolding attractor profile

## Correctness — PASS

The word is uniquely fixed by its one-based odd-part definition, while every attractor position is explicitly zero-based. Upper bounds follow from exact enumeration of every factor at every length and checking that an occurrence crosses one of the displayed positions. Lower bounds follow from a transparent weighted occurrence-span inequality: each factor forces an attractor hit, while the listed load of any position is bounded by the shared denominator. The executable checkers recompute every factor occurrence and position load from the explicit certificates, independent of how the certificates were discovered. They establish the four claims by finite exhaustive tests, not by extrapolating experiments to unbounded lengths. Two implementations, including one using integer bitsets, returned their respective success markers on the shipped files.

## Originality — PASS, subject to the stated literature risk

The closest publicly inspected dyadic-prefix benchmark (September 8, 2026) reports exact paperfolding minima only up to length 64. At the four claimed lengths it reports the nonmatching intervals [4,7], [4,8], [4,10], [4,9], rather than the exact values 5,6,6,7. The full public benchmark's result and limitation sections were inspected. Banbara et al. (arXiv:2602.16152; full CPM 2026 HTML inspected) classify attractors for Fibonacci and period-doubling words, not regular paperfolding. Cassaigne et al. (2024) treat infinite-word profiles and other explicit classes, not the four exact paperfolding parameters. Searches for equivalent paperfolding, automatic-sequence, finite-prefix and dyadic-attractor statements found no stronger same-parameter result. The risk of an unindexed independent enumeration remains; searches alone do not prove novelty.

## Value — PASS

String-attractor size is a natural, established compression-oriented combinatorial invariant. The four dyadic lengths are the first unresolved steps of a previously published regular-paperfolding census, not arbitrary handpicked sizes. These exact values finish that finite table up to length 1024, identify two exact plateaus and two increases, and provide unusually compact independently replayable lower-bound certificates. No new infinite-family theorem is claimed or required for this meaningful finite result.

## Scientific limitations and sources

The proof makes no claim about asymptotic growth, uniqueness of attractors or arbitrary prefix lengths. The closest source is the public September 2026 dyadic-prefix benchmark (GitHub published-finding corpus public record 2026/9/8/SCOPE079), alongside Schaeffer–Shallit arXiv:2012.06840, Banbara et al. arXiv:2602.16152 and Cassaigne et al. DOI:10.1016/j.jcta.2024.105936. This is a review of the stated new finite claim and not an independent external audit.

Self-review: passed. Independent audit: not yet performed.
