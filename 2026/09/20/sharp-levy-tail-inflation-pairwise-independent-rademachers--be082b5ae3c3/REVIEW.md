# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The upper bound uses only facts forced by the hypotheses. Pairwise independence and symmetric Rademacher marginals imply zero covariances and hence E[S_n^2]=n. For odd n, S_n is odd, so outside {|S_n|>=2} one has S_n^2=1; on the event, S_n^2<=n^2. This yields P(|S_n|>=2)>=1/(n+1), and the maximal-event probability is at most one.

The extremizer is an explicit finite-field character system. Distinct nonzero vectors in F_2^m define pairwise-independent symmetric Rademacher characters. The first six vectors are e1,e2,e1+e2,e3,e4,e3+e4. If no two-step block reached absolute partial sum 2, each pair would have opposite signs, forcing three affine parity equations whose left-hand coefficient vectors sum to zero while their right sides sum to one, an impossibility. Thus the maximal event occurs for every seed. Character orthogonality gives terminal sum n at the zero seed and -1 at every nonzero seed, so the terminal tail probability is exactly 1/(n+1). The ratio is therefore n+1 and saturates the universal bound.

Exact exhaustive checks for m=4,...,9 verify all marginals, all pairwise joint tables, the maximal event, and the terminal distribution. These checks agree with the proof.

## Originality — PASS, to the best of our knowledge

The classical Lévy inequality under mutual independence is old and standard. The failure of Kolmogorov-type maximal inequalities under pairwise independence is also known; Thành (2023) explicitly notes that such an inequality is unavailable and develops maximal WLLNs without it. Révész--Wschebor (1964) studies pairwise-independent Walsh functions and gives detailed behavior of their natural-order partial sums. Tao's book gives the same finite-field/Walsh family used here for an extremal terminal-sum concentration example.

Those sources make both ingredients—the Walsh character family and the general danger of maximal inequalities under limited independence—known. The located sources do not, however, state the exact threshold-2 maximal-to-terminal ratio, the universal upper factor n+1, or a finite prefix forcing the maximal event with probability one while retaining the minimum possible terminal tail. Targeted searches under Lévy/Ottaviani, pairwise-independent Rademacher, Walsh/Hadamard, maximal partial sum, final/terminal sum, and best/sharp constant terminology did not locate an equivalent result.

The closest residual risk is older Walsh or orthogonal-system literature: the 1964 Révész--Wschebor paper uses the same character system and could make related separations implicit under another ordering or notation. Its inspected theorem concerns the natural Walsh ordering, not the extremal ratio proved here. Hoffmann-Jørgensen (2002/2003) develops weaker notions of independence for extending stochastic inequalities to non-measurable random elements; the inspected descriptions are not pairwise-independence claims and do not contradict the construction. Because an equivalent folklore observation may exist, originality is asserted only to the best of our knowledge.

## Value — PASS

The result gives a sharp quantitative boundary rather than merely another counterexample: along infinitely many dimensions, the best threshold-2 Lévy-type factor for pairwise-independent Rademachers is exactly n+1. It cleanly separates what survives from second moments (a linear finite-dimensional cap) from what mutual independence supplies (the classical constant 2), and it does so in the smallest bounded symmetric marginal class. The six-vector forcing gadget is reusable in limited-independence constructions where one wants an early path excursion together with an extremally concentrated terminal sum.

## Scientific limitations

The exact optimum is proved only at threshold 2 and for n=2^m-1, m>=4; even lengths and other odd lengths are not classified. No claim is made for higher-wise independence, conditional independence, martingale differences, mixing assumptions, general symmetric marginals, or vector-valued increments. The literature search cannot exclude an older equivalent formulation under Walsh-function or orthogonal-system terminology.
