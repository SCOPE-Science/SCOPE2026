# Review of acute-triangle law for rectangle boundaries

## Correctness — PASS
For any fixed base sample, the ordered-pair obtuse-angle measure was partitioned into bottom-including, vertical–top, opposite-vertical and top–top classes, all with explicit dot-product inequalities. Integration gives the exact piecewise aspect law. The coefficient of the emerging interval is \(-16/105\) for the unnormalized side integral, becoming \(4/945\) for the probability; thin-aspect cancellation leaves \((3\log r-3/2)/r^2\). The supplied `verify.py` checks the raw, unintegrated side-pair integrals independently and tests actual random Cartesian triples for multiple aspects. Random trials do not prove the theorem.

## Originality — PASS relative to inspected evidence
The square value \(23/96\) is explicitly previously known from a 2012 Mathematics Stack Exchange answer and is not claimed as a contribution. Read the relevant full answer text, arXiv:1501.03053 (Gaussian random-triangle models), bibliographic/abstract evidence for Portnoy (1994), and compared published-finding corpus mathematical statements on related but different pair-distance and polygon sampling statistics. Actual equivalence/alias/broader-coverage searches found no parameter law or aspect-two fractional-power transition. The publicly available Portnoy text was abstract-only, and the answer edit history leaves a publication-timing uncertainty; historical priority is not certified.

## Mathematical value — PASS
The full one-parameter law of strict acuteness under perimeter sampling is a natural geometric probability invariant, and gives a sharp mechanism-driven aspect-two transition in differentiability together with a logarithmically enhanced thin-rectangle decay. These features are not entailed by the known square value, measure conventions, or pairwise-distance moments. No claim is made for interior sampling, arbitrary convex bodies or a global monotonicity theorem.

## Independent validation
Not performed. The analytic proof and reproducible program are suitable for subsequent independent inspection.

Self-review: passed. Independent audit: not yet performed.
