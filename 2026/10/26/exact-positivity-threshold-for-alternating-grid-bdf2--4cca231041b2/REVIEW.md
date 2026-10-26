# Review

## Correctness

The scalar recurrence is obtained by expanding the variable-step BDF2 formula with the actual adjacent-step ratio. The period-two ratio map has a quadratic fixed-point equation whose discriminant factors as \((r-1)^2z^2-4(r+1)z+4\). The startup ratio lies in the basin of the larger positive fixed point through the stated exact inequalities. Above the first discriminant root, no positive fixed point can sustain all positive iterates, so the sharp threshold is necessary as well as sufficient. The proof is exact; finite checks are supplementary.

## Originality

The closest inspected source is Liao, Tang, and Zhou (arXiv:2003.00421), whose full text treats nonlinear Allen–Cahn maximum-principle preservation under ratio and step-size restrictions. It does not give this scalar alternating-grid necessary-and-sufficient criterion. Wang, Mao, and Wang (arXiv:2003.03534) study variable-step BDF2 stability/error estimates; only the abstract was inspected here, so that comparison remains a risk rather than evidence of non-coverage. The constant-step case \(r=1\) is recovered, while the result for \(r>1\) supplies a distinct exact step-ratio law.

## Value

Positivity preservation matters when numerically integrating nonnegative decaying modes. Adaptive solvers can alternate between coarse and fine steps; the exact formula quantifies the sharp tradeoff for this common periodic pattern and shows that a long step can exceed the constant-step positivity limit only when paired with a sufficiently short step. The claim is deliberately limited to that pattern.

Self-review: passed. Independent audit: not yet performed.
