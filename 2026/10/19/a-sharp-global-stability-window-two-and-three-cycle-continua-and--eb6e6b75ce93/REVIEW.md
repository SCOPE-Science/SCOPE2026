# Self-review

## Correctness — PASS
The proof handles both branch conventions at the switching line, all real initial coordinates, and every allowed value of \(a>0\), \(b\ge0\), \(d>0\). Direct case analysis establishes entry into the positive horizontal ray within four steps. Exact ray returns have factors \(ab-d\) (two steps) and \(a(d-ab)\) (three steps), with zero at equality. The uniform bound on finitely many entrance and intermediate matrices establishes global exponential stability when the return factor is below one. Ray periodic or expanding examples prove both boundary sharpness and necessity. A separate sign refinement proves \(F^5=0\) on \(d=ab\), and an explicit nonzero fourth iterate proves minimal uniform collapse time. The included exact-arithmetic script independently sanity-checks rational samples; it is not substituted for the proof.

## Originality — PASS, residual priority uncertainty
The most relevant source is Simpson, arXiv:2408.04790, §§1 and 4–6. It explicitly declines to classify \(\mu=0\) origin stability, and its attraction diagrams concern \(\mu=\pm1\). Its expressions involving \(\tau_L\tau_R-\delta_R\) overlap with the first two-step factor but do not establish the complete homogeneous classification and global deadbeat phenomenon. Simpson, arXiv:1612.02932, gives general homogeneous-map stability theory, while its detailed two-dimensional specialization does not cover this singular-left-determinant region. Simpson, arXiv:2606.08901, treats a different, nonzero-offset return-map regime. Published-record and equivalence searches found related period and extinction results for different maps rather than this full claim. An unindexed or differently parameterized antecedent remains possible; no claim of exhaustive priority is made.

## Mathematical value — PASS
This solves a natural critical-parameter problem omitted by the source, with necessary and sufficient global stability inequalities across a three-parameter cone rather than an isolated computation. It identifies distinct codimension-one neutral continua of two- and three-cycles and an exact finite-time-death surface between them. The \((2,1,2)\) example shows that switching yields five-step global annihilation even when neither branch is individually stable, a motivated structural phenomenon relevant to piecewise-smooth bifurcations and switching dynamics.

## Scientific limitations
The theorem is restricted to zero switching offset, left determinant zero, \(a>0\), \(b\ge0\), \(d>0\). The published literature may contain an equivalent statement under another normal form or as an implicit corollary. The finite checker is supplementary and cannot independently validate the quantified theorem.

Self-review: passed. Independent audit: not yet performed.
