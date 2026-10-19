# Scientific review: weak-coupling period-two cycles in a memristive Lozi map

## Correctness — PASS

The full-space period-two recurrence forces opposite signed inputs; since \(b>0\) and \(k<1\), the two corresponding first coordinates have opposite signs. The resulting exact algebraic elimination gives the only possible cycles \((-t,t,z)\leftrightarrow(1,-t,z+t)\). Each sine-phase solution has one and only one positive amplitude because the scalar derivative has the global positive lower bound \((1-3k)/(1-k)\). This proves the complete \(0,1,2\) phase-quotient census. The two-step Jacobian's symbolic first-order coefficients prove the sink/repeller split for sufficiently small \(k>0\) at \(b=1\). The packaged checker passed 640 supplementary symbolic and numerical assertions. Neither numerical sampling nor this self-review substitutes for independent validation.

## Originality — PASS, subject to priority uncertainty

The closest work is Wang–Gu–Rong–Xu–Zhang, *Mathematics* 10 (2022), 3426, DOI 10.3390/math10193426: it defines the same three-dimensional map, proves no fixed point, and presents numerical period and attractor diagrams. Its reviewed sections do not contain the low-gain exact period-two phase wedge, unique-amplitude theorem, or two separate three-dimensional Floquet stability types. The later Lozi survey, *Algorithms* 16 (2023), 491, DOI 10.3390/a16100491, reproduces the map and numerical observations without a corresponding classification in the inspected passages. Similarity and bibliographic searches did not identify an implying result. An unindexed mathematical antecedent remains possible, and not every related full article was inspectable.

## Mathematical value — PASS

The first primitive period in a map with no equilibria is naturally motivated by numerical hidden periodic attractors. The exact parameter census replaces sample-based diagrams with an all-orbit theorem, while the coexistence of one hyperbolic sink and one hyperbolic repeller gives a concrete, genuinely three-dimensional stability distinction at identical parameter values. This is more substantive than recomputing a known sample cycle.

## Limitations

Only \(a=1\), \(b>0\), and \(0<k<1/3\) are fully counted. The stability dichotomy holds for sufficiently small positive coupling near the central line, and neither all longer periods nor all attractors are classified. Uniform high-gain behavior, optimality of the technical \(1/3\) bound and exhaustive priority are not claimed.

Self-review: passed. Independent audit: not yet performed.
