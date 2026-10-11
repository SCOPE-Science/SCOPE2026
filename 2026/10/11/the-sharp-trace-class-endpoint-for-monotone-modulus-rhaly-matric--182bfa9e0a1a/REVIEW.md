# Review of the monotone-modulus Rhaly trace-class endpoint

## Correctness — PASS

The exact singular values of the triangular all-ones matrix follow from inversion of its tridiagonal Gram inverse, yielding \(\|L_N\|_1\asymp N\log(N+1)\). Dyadic decomposition proves trace-class sufficiency by summing internal triangular and external rank-one blocks. Pinching to disjoint dyadic diagonal blocks proves necessity with uniform lower bounds using monotonicity. Weighted condensation converts the dyadic condition into the logarithmic series. No finite-dimensional data are invoked as infinite-dimensional proof.

## Originality — PASS, with identified limitations

Bellavita–Dellepiane–Stylogiannis, arXiv:2503.21930v1, Theorems 1.3 and 5.8, explicitly restrict their complete Schatten criterion to \(1<q<\infty\); their full text was read, including the necessity argument and the \(q>1\) summation. Galanopoulos–Girela's 2026 full journal article cites the same restricted Schatten range and itself addresses boundedness and compactness. The June 2026 related arXiv:2606.15875 is a plausible overlap risk: its abstract and available technical summary were inspected, but complete primary text was inaccessible. Targeted source searches and a search of existing findings did not reveal an equivalent monotone-modulus trace-class criterion. Absence from searches is not a proof of uniqueness.

## Mathematical value — PASS

The trace endpoint is structurally exceptional: each dyadic lower-triangular block adds a harmonic singular-value sum, producing an extra logarithm not predicted by the \(q>1\) dyadic Besov criterion. The result gives a necessary-and-sufficient, two-sided norm theorem and a sharp \(r=2\) threshold for standard regularly varying coefficients. This directly clarifies the strict limiting boundary of a contemporary Schatten-class classification rather than merely calculating one isolated example.

## Limits and independent validation

The result requires nonincreasing coefficient moduli and leaves the unrestricted \(\mathcal S_1\) case, optimal constants, and the inaccessible June 2026 full-text comparison open. The finite standard-library verifier is a diagnostic supplement, not external proof certification.

Same-model review: passed. Independent audit: not yet performed.
