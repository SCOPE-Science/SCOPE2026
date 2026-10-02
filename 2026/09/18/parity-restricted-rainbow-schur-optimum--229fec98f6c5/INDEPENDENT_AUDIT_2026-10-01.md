# Independent mathematical audit — 2026-10-01

## Final finding

The parity-restricted rainbow-Schur theorem passes correctness, originality, and scientific value.

## Correctness

For \(n=2m\), let \(A\subseteq[m]\) index one of the two colors on odd integers and write \(a=|A|\). The rainbow count is exactly twice
\[
a(m-a)+\operatorname{cut}_{H_m}(A),
\]
where \(H_m\) has edges \(\{i,j\}\) with \(i<j\) and \(i+j\le m+1\). Splitting according to membership of the two extreme vertices gives the stated two-step fixed-cardinality cut recurrence.

The piecewise quadratic comparison function has Bellman residual at most \(1/2\) in every integer state. On \(0\le a\le m/2\), away from the transition this residual is \(1/2\) on the low-density branch and \(0\) on the middle branch. Writing \(k=3a-m\) at the transition reduces the remaining cases to explicit quadratic residuals; their maximizing branch stays between \(-1/8\) and \(1/2\). Symmetry covers the other half. Induction therefore gives the uniform \(O(m)\) error, with the stated \(m/4\) upper error.

The continuum objective is \(2x-rac52x^2\) for \(0\le x\le1/3\) and \(rac32(1-x)-rac{11}{8}(1-x)^2\) for \(1/3\le x\le1/2\). Its only maximizers are \(5/11\) and \(6/11\), with value \(9/22\). This also gives the color-balance stability statement.

## Originality

### Equivalent formulations

Searches covered “rainbow Schur triples”, “parity-restricted rainbow Schur”, “monochromatic evens”, “odd/even coloring”, “9/22”, and the threshold-graph fixed-cardinality maximum-cut formulation. No earlier equivalent statement of the parity-restricted optimum or its stability statement was located.

### Broader coverage

Hegde, Kumar and Pratibha, *A somewhat sure note on an un-Schur problem*, arXiv:2609.18474, was inspected in full. It proves the unrestricted lower bound \(9/22\), gives the parity-and-interval construction realizing that bound, proves an upper bound \(8/15\), and asks whether the unrestricted optimum is \(9/22\). It does not prove optimality over arbitrary two-colorings of the odd integers with all evens monochromatic.

Parczyk and Spiegel, *An Unsure Note on an Un-Schur Problem*, Electronic Journal of Combinatorics 33(1), P1.45 (2026), DOI 10.37236/13554, supplies earlier asymptotic anti-Ramsey Schur bounds rather than the restricted optimum.

### Exact database or table

No finite database or tabulated classification controls this asymptotic theorem. The relevant exact finite computation is the threshold-graph recurrence itself; finite checks in the record are supporting evidence only and are not used as novelty evidence.

### Claim versus prior implication

The known \(9/22\) construction is an existence lower bound inside this parity-restricted class. It does not imply that every parity-restricted coloring has density at most \(9/22\). The audited maximum-cut recurrence and its uniform Bellman estimate provide that missing implication, so the theorem is not a corollary of the inspected prior bounds.

## Scientific value

The restriction is structurally motivated because it contains the best known \(9/22\) construction. The theorem rules out every improvement that preserves a monochromatic even class, gives an exact threshold-graph reduction, and identifies the only possible limiting odd-color balances for near extremizers. It is therefore a meaningful boundary result even though it does not settle the unrestricted problem.

## Residual risks

The motivating preprint is recent, so unindexed contemporaneous work remains possible. No specific inaccessible source with a theorem plausibly dominating this restricted optimum was identified.
