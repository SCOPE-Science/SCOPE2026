# Scientific review: exact Gaussian-sketch first-pivot law and sharp runner-up principle

## Correctness — PASS

The Gaussian-column-independence reduction requires all input columns to be mutually orthogonal and the sketch to have jointly Gaussian independent rows; these hypotheses are explicit. Conditioning on the leading column's independent chi-squared norm yields the exact gamma integral for all positive sketch heights. Inclusion–exclusion and finite integer-gamma CDF expansions establish the even-height expression, without numerical extrapolation. The single-competitor beta tail has a sharp endpoint-Laplace asymptotic; the common-leading-column dependence is controlled by a two-competitor Chernoff exponent that is strictly larger for every squared-norm ratio above one. Non-runners have strictly larger one-event rates. These points prove the full leading constant, including repeated second-largest columns, and the small-risk sketch-height expansion. The packaged code passed 80 exact, symbolic, integrated, direct-sketch and asymptotic checks. Its finite tests are corroboration, not the proof of infinite claims.

## Originality — PASS, with stated publication-priority risk

The relevant established ingredients are independent chi-squared norms under orthogonal Gaussian sketches, the symmetric beta ratio identity, and gamma/order-statistics integration. The narrower assessed statement is their application to the **whole first-pivot event** of a Gaussian-sketched QR factorization with multiple competitors, plus the sharp runner-up multiplicity constant proved despite simultaneous events sharing a random first-column norm. The 2023 CQRRPT primary source studies pivot quality via embedding, structural and stability guarantees and numerical trials; the 2018 randomized QRCP analysis supplies Johnson–Lindenstrauss reliability bounds, not this precise law; the 2015/2017 randomized QRCP analysis studies marginal and conditionally truncated chi-squared norms, not the all-competitor first-pivot identity and runner-up asymptotic. A separate previously known two-candidate fixed-sketch-row calculation is not claimed here as new. Related gamma-order-statistic papers outside the numerical linear algebra literature may contain equivalent formulations; this is a residual publication-priority risk. The supplied work does not claim independent priority certification.

## Value — PASS

The canonical orthogonal-column model isolates sketch-induced pivot mistakes from genuine column dependence. The exact probability formula is a reproducible benchmark for numerical QR pivot-selection experiments and sketch-size calibration, while the sharp asymptotic replaces the loose dependence on all columns by the top/runner-up norm gap and its multiplicity. The proof explicitly quantifies why dependence through the shared winning norm does not invalidate first-order addition of rare runner-up failures. The sample-complexity correction of order \(\log\log(1/\varepsilon)\) is a further measurable design quantity. These are complete natural rank-selection invariants on a motivated matrix class, not a proposed generic QR error theorem.

## Sources and scientific limitations

- Melnichenko et al., *CholeskyQR with Randomization and Pivoting for Tall Matrices*, arXiv:2311.08316v1 (2023-11-14), Sections 1.4, 2.2–2.3 and 4.
- Duersch and Gu, *Randomized QR with Column Pivoting*, arXiv:1509.06820v2, Section 3.
- Xiao, Gu and Langou, *Fast Parallel Randomized QR with Column Pivoting Algorithms for Reliable Low-rank Matrix Approximations*, arXiv:1804.05138v1, Section III-C.

The theorem does not treat later pivots, nonorthogonal inputs, sparse sketches, floating-point effects, growing candidate count or approximation-error guarantees. The external mathematical review has not been performed.

Self-review: passed. Independent audit: not yet performed.
