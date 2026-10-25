# Scientific review

## Correctness — PASS
The exact fourth-step projected candidate identity follows by multiplying the orthogonal third-vector decomposition by the inverse matrix. A nonzero third mixed residual follows from the nonzero inverse Rayleigh quotient. Four distinct active eigenvalues are necessary and sufficient for a nonzero fourth split residual by a degree-three polynomial-root argument. The intermediate-value proof constructs positive spectral weights with inverse and direct Rayleigh product exactly one on every symmetric indefinite spectrum with at least four values. The explicit condition-three four-dimensional witness has all required residual squares verified exactly by `check.py`.

## Originality — PASS, with bibliographic risk
The 2026 motivating manuscript defines both channels, proves definiteness-based preference, and discusses indefinite numerical behavior. Its algebra and the existing third-step cancellation mechanism are treated as prior work. The new claim concerns a successful third step followed by exact fourth-step premature breakdown, together with the necessary-and-sufficient spectral characterization and the dimension-four, well-conditioned witness. Targeted research-record searches and published-source searches did not identify a statement covering these additional conclusions. Earlier articles about extended Krylov recurrences were accessible in abstract only, so unknown equivalent prior formulations are a material residual risk; independent literature review remains appropriate.

## Mathematical value — PASS
This supplies a structural failure mode not diagnosed by third-step cancellation: even a starting vector that successfully builds three basis vectors can cause a spurious stop on the next mixed-channel expansion while the underlying extended space has grown. It gives the exact spectral complexity at which the phenomenon becomes possible and rules out poor conditioning as a necessary cause. The result is narrowly about exact local residuals, not guaranteed floating-point failure or global accuracy.

## Source comparison and limits
Lund–Schweitzer (arXiv:2610.21603v1, Algorithms 1–2, Section 3, Appendix A) supplies the channel definitions and local robustness framework. Jagels–Reichel (2011) and Mertens–Vandebril (2015) concern recurrence structures; their abstracts alone do not determine whether they state the same fourth-step exceptional condition. All statements apply only to real nonsingular symmetric matrices with the specified inverse-leading ordering.

Self-review: passed. Independent audit: not yet performed.
