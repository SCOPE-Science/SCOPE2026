# Scientific review: Brownian square-root-boundary coverage occupation

## Correctness (PASS)

For every \(z>0\), the Gaussian pair \((B_s/\sqrt s,B_t/\sqrt t)\) has correlation \(\sqrt{s/t}\) for \(s<t\). Fubini and the correlation change of variables reduce the second moment to \(2\int_0^1rq_z(r)dr\). The Gaussian correlation heat equation gives the explicit derivative of the centered rectangle probability and, by integration by parts, the claimed single integral. Two Laplace transforms with disjoint ordered supports yield a strictly increasing ratio: this proves the unique derivative zero and globally unimodal variance. At zero, the right derivative is \(2/\pi>0\); the ratio diverges at infinity. Laplace endpoint analysis proves the tail equivalent. The finite precision script reproduced the numeric root and variance using independently evaluated Gaussian rectangle integrals and high-precision quadrature; computations support but do not replace the proof. No claims of numerical interval certification are made.

## Originality (PASS, subject to historical priority)

Fischer--Glynn arXiv:2610.24668v1 Section 2 proves the coverage-time Brownian limit and gives a three-dimensional numerical second-moment integral, plus Table 1. That prior work determines numerical standard deviations at selected levels but does not imply *from a stated monotonicity or optimization result* the exact unique global maximizer and endpoint equivalents. Plackett 1954 supplies a standard derivative identity, which does not itself state the Gaussian occupation-variance optimization. A nearby research record on minimax square-root confidence horizon *width* addresses a different optimization (worst relative half-width over monitoring horizons), not occupation-time variance over nominal levels. Targeted searches found no equivalent statement; that absence is not proof of historical uniqueness. A broader unlocated Gaussian occupation functional theorem remains a residual risk.

## Mathematical value (PASS)

Nominal confidence level is the natural adjustable parameter in the motivating paper. Its Section 2 expressly computes and tabulates the time-coverage standard deviation and observes substantial pathwise randomness. A sharp classification answers which nominal confidence level is **worst** for run-to-run coverage-proportion volatility and gives a global sharp variance bound. The proof's positive-kernel transform also yields exact low- and high-coverage asymptotics and a stable one-dimensional numerical formula, replacing nested integration. This is a structural, motivated optimization of a natural invariant, not a numerical interpolation of the table or a generic Gaussian-calculus exercise.

## Closest literature and limits

- Fischer--Glynn (arXiv:2610.24668v1), Sections 2--3: limit occupation law, second-moment representation, numerical variances, stationary Ornstein--Uhlenbeck equivalent.
- Plackett (1954), Gaussian correlation differentiation; an accessible derivation appears in Appendix D, Lemma D.3, of *The Mathematics of Indirect Treatment Comparisons*.
- Closest text-search result: `2026/10/4/SCOPE-square-root-confidence-horizons-are-globally-minimax-for-worst-f--391568f89a70`; controls worst width of calibrated monitoring boundaries rather than fluctuation variance of the coverage fraction.

The theorem concerns the limiting Brownian functional, not the optimizer at finite sample sizes. Quantitative digits are approximate. Historical priority should be independently checked.

Self-review: passed. Independent audit: not yet performed.
