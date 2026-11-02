# Review of the sharp arcsine-node positive cubature law

## Correctness: PASS
For independent arcsine samples, exact positivity is characterized geometrically by the target moment point lying strictly inside the convex hull of the sampled parabola. Conditioning on extreme and nearest opposite-sign nodes gives two disjoint failure integrals. The inner integral has one nondegenerate maximum at \(\arcsin\sqrt q\), and standard Laplace analysis yields the stated sharp \(\sqrt m\) coefficient. The outer integral has two endpoint contributions: one appears directly in the formula and the other at the endpoint \(a=1\), each asymptotic to the same exponential. Their exponents cross uniquely at \(q=1/3\). A separate finite two-variable probability integral, 1,200 independent linear-program feasibility comparisons, and numerical replays check normalizations. No finite experiment substitutes for the analytic limit argument.

## Originality: PASS (provisional scholarly priority)
The 2026 Neumayer–Schäfer–Ullrich primary paper establishes general high-probability positive-weight existence but not an exact finite \(m\) law for arcsine nodes, the two competing asymptotic exponents, or the polynomial-critical crossover. The 2018/2019 van den Bos–Sanderse–Bierbooms–van Bussel work builds sample-based positive rules rather than deriving this fixed-target support probability. The 2026 Bělík–Narayan–Turnage paper on randomized least squares is relevant but only abstract-level material was accessible; this limits the strength of the priority comparison. The classical centrally symmetric Wendel formula does not cover the noncentrally symmetric lifted parabola law. Earlier uniform-node quadratic cubature probabilities, the opposite-sign geometric criterion, and the uniform-node \(2/3\) exponent are prior work, not asserted novel here. A specialized historical equivalent could remain undiscovered.

## Mathematical value: PASS
Positive exactness is a prerequisite for stable, monotonic weighted cubature on prescribed node sets. The result resolves how the success probability depends sharply on a natural nonuniform sampling density, explains the mechanism switch with target second moment, and identifies the critical \(\sqrt m\) loss exactly at the normalized uniform target. It yields a quantitative leading-order reduction in random node budget for the same small failure probability compared with uniform-node sampling. It does not assert importance-weight stability, algorithmic construction cost, higher-degree exactness, or floating-point reliability.

## Limitations and independent status
The asymptotic fixes \(0<q<1\); positive weights are unrestricted and real-arithmetic exact. Broader prior literature may contain equivalent results; the Bělík–Narayan–Turnage full paper was not accessible. Numerical checks are finite corroboration, not independent certification.

Self-review: passed. Independent audit: not yet performed.
