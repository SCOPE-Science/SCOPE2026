# Scientific review

## Correctness (PASS)

The claim concerns a fully specified conditional last-preference probability law. The initial parking-shuffle weights count successful first-stage preferences by the unique remaining vacancy; the final car's one-coin factor yields equation (1). Subtracting adjacent entries gives equation (2) exactly. Factorial cancellation proves the weight ratio (3), and differentiation of \((x-1)\log(1+1/x)\) establishes strict monotonicity without numerical assumptions. This proves the entire finite classification, ties, and endpoint behavior. A uniform interior Taylor expansion and monotone threshold squeezing justify the \(1/n\) scaling limit, not just pointwise numerical evidence. Direct enumeration of the parking process with rational coins for \(2\le n\le6\) independently reproduces the conditional mass formula; the checker passes 6,849 assertions. Boundary cases \(n=2\), \(p=0\), \(p=1\), and exact threshold ties are covered.

## Originality (PASS; material caveat)

The primary 2022/2023 source already determines every finite probability mass and is explicitly credited. Its results concern that mass formula, the first moment, and total-variation rates, not the exact one-trough shape classification, strict ordering of all shape boundaries, countable boundary-layer transitions, or fine \(1/n\) location profile. A 2025 paper gives an even broader conditional mass formula for unequal numbers of cars and spaces, which likewise implicitly permits the equal-size calculation but does not articulate this structural threshold theorem in the text examined. The new result requires a separate strict log-convexity argument and an interior scaling inversion; it is not claimed that the underlying enumeration is original. Search comparisons with related published records did not locate an explicit covering shape-and-scaling theorem. Residual priority risk is substantial because the entire exact mass law is known, and an earlier analyst may have made the same deduction without indexing its conclusion.

## Value (PASS)

The object is the principal conditional statistic introduced to measure the effect of randomizing parking directions. The exact shape diagram explains a qualitative feature not resolved by the previously emphasized mean and total-variation estimates: the distribution can be globally increasing, globally decreasing, or have a unique trough. The two outer critical parameters converge to the universal logistic constants, yet infinitely many microscopic transition parameters accumulate at \(1/2\). A distinct \(1/n\) window transports the trough across a nontrivial fraction of the street, even while the marginal is close to uniform. This is a natural complete distribution-shape classification and a new finite-to-asymptotic boundary structure, not an arbitrarily selected value of a statistic.

## Closest literature and limitations

Most relevant: Durmić et al., arXiv:2211.00536v1, Theorem 3 and Section 2.4; Harris et al., arXiv:2502.00269, Theorem 2.7 and Section 3; Tian and Treviño, arXiv:2111.12850, Section 2. This theorem does not extend to excess spaces or nonuniform preferences. Independent mathematical audit and historical priority confirmation have not been performed.

Self-review: passed. Independent audit: not yet performed.
