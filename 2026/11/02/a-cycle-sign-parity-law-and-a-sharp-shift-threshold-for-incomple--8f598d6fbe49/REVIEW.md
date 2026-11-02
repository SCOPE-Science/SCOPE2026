# Scientific review of signed-cycle incomplete Cholesky thresholds

## Correctness (PASS)

The statement fixes natural order, original-pattern zero fill, exact arithmetic, all signed simple cycles of size \(n\ge4\), and the two sign-product classes. A diagonal sign gauge proves the input eigenvalue extremes. The IC(0) recurrence has exactly two contributions to its final pivot, versus one to each intermediate pivot. The continuant identity \(p_n=D_{n+1}/D_{n-1}\) is reconstructed algebraically. The first two zeros of the path continuant, together with the input positive-definiteness endpoint, determine exactly when the final pivot vanishes or becomes negative. Rescaling gives the strict optimal shift condition. Extremal eigenvalue ratios and Taylor expansion establish the condition-number boundary and the cubic asymptotic. The exact four-vertex witness and 3,667 independent arithmetic checks are consistent with the proof. Numerical evidence is not treated as a proof for all sizes.

## Originality (PASS, with priority qualification)

The inspected 2024 Scott–Tůma primary study already establishes the broad issue of IC(0) breakdown on positive-definite inputs and studies shifts, including exact-arithmetic examples. The 2012 Ferronato survey describes M-matrix safety, non-M-matrix breakdown, and stabilization. The present statement is not a claim to invent those general mechanisms. It is the exact simultaneous classification of **input positive definiteness by cycle-sign parity**, **the sign-blind zero-fill pivot threshold**, **the full breakdown interval**, and **the sharp global shift/condition-number boundaries** for all cycle lengths. Neither inspected full text states these precise formulas. Searches using signed-cycle, cyclic-tridiagonal, Chebyshev, and zero-fill terminology did not locate a directly covering published statement or table. Source lists, formulas and individual risks appear in `AUDIT.json`.

The older Eijkhout existence survey could be located and its abstract read, but the full archive PDF could not be retrieved. This is a publication-priority risk, not proof of absence. A further specialized literature check by another researcher could change the originality assessment; no independent audit is claimed.

## Value (PASS)

The result supplies a natural all-size sparse numerical-linear-algebra boundary where incomplete-factor success and positive definiteness diverge. The input is a minimal nonchordal graph, the sign product is its switching invariant, and the required global shift is exactly computable rather than a heuristic. At four vertices a strictly positive-definite matrix of moderate condition number has a negative IC(0) pivot. For larger cycles, the quantitative boundary reveals the cubic conditioning scale at which failure first becomes possible. These facts can be used to verify implementations and reason about dropping and diagonal compensation, without implying performance for arbitrary sparse systems.

## Closest literature and limitations

Relevant literature: Scott–Tůma (2024), arXiv:2403.13123; Ferronato (2012), DOI:10.5402/2012/127647; classical symmetric M-matrix guarantee (Meijerink–van der Vorst, 1977); Eijkhout's 1999 LAPACK Working Note 144 (only metadata/abstract accessible). The finding is limited to equal edge magnitudes, simple cycles, natural vertex order and exact unchanged-pattern IC(0). No statements about roundoff, alternate ordering, modified incomplete factorizations, or preconditioned solver iteration counts are made.

Self-review: passed. Independent audit: not yet performed.
