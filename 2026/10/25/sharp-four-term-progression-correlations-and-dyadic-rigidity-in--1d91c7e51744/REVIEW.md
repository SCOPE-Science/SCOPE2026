# Mathematical assessment

## Correctness — PASS
The proof reduces all even spacings to their odd parts, uses an explicitly closed 30-state signed carry transducer to compute exact unrestricted Cesàro correlations, and proves a strict global norm bound after a complete 16-prefix partition and symbolic affine induction along the only two exceptional paths. `verify.py` reconstructs the states and checks all finite identities and the entire symbolic parameter half-line; the decisive induction is not a finite-range extrapolation. The needed terminal functional is a genuine fixed point, not an arbitrarily long numerical truncation.

## Originality — PASS under inspected evidence
Ravy's original paper (arXiv:1303.3792) motivates nontrivial Rudin–Shapiro four-point correlations, and Mazáč (arXiv:2211.01090, Sections 4 and 6) establishes all-order recursions and particular four-site families, notably unequal-offset adjacent-pair shapes. The result here isolates and maximizes the **equal-spacing** shape and proves that the unique maximizing spacings are powers of two. The consulted literature did not state this global extremal classification. Konieczny's Gowers-norm results concern aggregate uniformity rather than pointwise extremal spacings. Prior Rudin–Shapiro filter records concern different finite circulant objects. The corresponding known Thue–Morse extremum concerns a different automatic sequence and does not imply this result. Historical priority remains a genuine residual risk; semantic searches do not establish global novelty.

## Mathematical value — PASS
Four-point equal-spacing correlations are natural higher-order invariants of automatic symbolic systems. Their sharp global size and arithmetic classification give a meaningful boundary between two-point pseudorandomness and higher-order dependence in the Rudin–Shapiro system. Exact rigidity across all spacings is not merely a restatement of the general recursion, a finite table, or a microscopic improvement.

## Scope and residual risk
The \(1/2\) bound cannot be extended to arbitrary four-point offsets: Mazáč exhibits larger correlations for different shapes. The current result has not received independent priority or correctness review. Earlier papers may contain an equivalent but differently framed specialisation of correlation recurrences.

Self-review: passed. Independent audit: not yet performed.
