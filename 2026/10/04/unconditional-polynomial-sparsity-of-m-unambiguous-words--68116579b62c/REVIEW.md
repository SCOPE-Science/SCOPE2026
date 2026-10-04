# Same-model review

## Correctness
PASS. The proof uses only the defining Parikh-matrix entry formula and a counting injection. For every consecutive alphabet block of length \(\ell\), its matrix entry is a scattered-subword count bounded by \(\binom{n}{\ell}\) on words of length at most \(n\). There are \(s-\ell+1\) such entries. Therefore the entire image up to length \(n\) has at most
\[
\prod_{\ell=1}^{s}\left(\binom{n}{\ell}+1\right)^{s-\ell+1}
\]
elements. Every \(M\)-unambiguous word is a singleton fiber, so the number of such words cannot exceed the image size. The polynomial exponent and density limit then follow algebraically.

The bundled verifier tests the exact Parikh-signature implementation on all binary words through length \(9\) and ternary words through length \(7\), reproduces the known binary count \(6m-10\) for exact lengths \(4\le m\le9\), and checks the exponent identity. These computations are sanity checks, not the infinite proof.

## Originality
PASS. Teh's 2020 Theorem 3.1 proves the density-zero conclusion only under Şerbănuţă's conjecture and explicitly leaves the unconditional statement open. The inspected 2023 full text of Hahn, Cheon, and Han completely characterizes the ternary case but states that the general-alphabet characterization remains elusive; it contains no density statement. The journal expansion retains the ternary scope in its abstract. Semantic-index and literature searches under density, sparsity, polynomial-count, image-size, and \(M\)-unambiguity aliases found no publication implying the all-fixed-alphabet theorem.

A residual originality risk remains because the argument is short enough to have appeared as an unindexed observation.

## Value
PASS. This is not a routine finite increment: it resolves a named published open problem for every fixed ordered alphabet and strengthens the desired zero-density statement to a polynomial upper bound
\[
O_s\!\left(n^{\binom{s+2}{3}}\right).
\]
It also bypasses the conjectural print-based mechanism on which the prior conditional theorem depended.

Same-model review: passed. Independent audit: not yet performed.
