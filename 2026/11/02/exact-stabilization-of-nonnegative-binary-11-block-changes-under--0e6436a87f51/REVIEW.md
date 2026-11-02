# Scientific review

## Correctness — PASS

The eight-state binary-addition matrix has entries defined directly by the carry rule and the local adjacent-ones change. The explicit infinite zero-suffix expectation is a convergent geometric carry calculation. Exact rational multiplication produces the seven required nonnegative generating polynomials and the proper-rational difference between the seventh and eighth shifts. The characteristic polynomial and Cayley–Hamilton relation propagate the vanishing nonnegative part of this difference to every larger shift. The standalone checker independently reconstructs the matrices, proves the finite algebraic identities symbolically, and runs direct integer comparisons. The existence of natural densities follows by periodic approximation with a geometrically vanishing unresolved-carry probability; direct finite counts alone are not used as an infinite proof.

## Originality — PASS within inspected evidence

Sobolewski–Spiegelhofer [1] gives a general recursion for conditional distributions and a Gaussian theorem for shifts with many one-blocks. It does not state or display the exact seven-gap stabilization or its four fixed nonnegative masses for shifts with two separated one-bits. The broader follow-up [2] similarly concerns a many-block asymptotic regime, while the digit-sum work [3] studies a different statistic. OEIS A014081 [4] provides values of the underlying count, not its exact sparse-shift change law. Targeted source, formula, digit-pattern-alias, and mathematical-record searches did not locate an equivalent result. Because a prior general recursion can compute each finite case, a previously unnoticed specialization or unindexed proof remains a genuine priority risk.

## Mathematical value — PASS

The simplest nontrivial sparse two-one-bit shifts form a naturally motivated hard finite-block regime of digit-change problems. The theorem does not simply compute an isolated parameter: it proves a sharp point of exact stabilization for the entire nonnegative probability law across infinitely many increasingly separated shifts, with an exact Cusick-type positivity density of \(175/256\). The negative distribution remains parameter-dependent, making the one-sided stabilization structurally informative.

## Scientific limitations

The result is restricted to the `11` block count and shifts \(2^a+1\), with \(a\ge1\). The negative-law and general-shift problems are not solved; bibliographic priority is not independently certified. The base-2023 paper's conditional recurrences are broader algorithms, and the originality assertion is about the new explicit uniform stability theorem rather than the existence of a recurrence.

Self-review: passed. Independent audit: not yet performed.
