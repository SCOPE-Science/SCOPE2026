# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

The central counterexample is exact. The matrices
\[
A=\begin{pmatrix}1&2\\0&-1\end{pmatrix},
\qquad
B=\begin{pmatrix}-1&0\\-2&1\end{pmatrix}
\]
are explicitly similar to real diagonal matrices with eigenvalues \(\pm1\). Similarity transfers the self-adjoint diagonal resolvent estimate to an estimate of the defining \(H\)-operator form, with a finite multiplicative condition number. Their sum has characteristic polynomial \(t^2+4\), hence nonreal spectrum, so it is not an \(H\)-operator.

The source article's Definition 3.1 defines a quasinorm on a real or complex linear space, and Definition 3.2 defines an approximation scheme with quasi-Banach ambient space. Definition 5.1 and Theorem 5.5 then set that ambient object equal to the set of all compact \(H\)-operators. Since the latter is not additive, the stated ambient-space requirement fails. The representation proof also uses differences and infinite sums, so additivity is materially used.

The separate typing observation is also direct: the paper's \(H\)-operator definition uses spectrum and \((T-\lambda I)^{-1}\) for an operator acting in one Banach space. For a general map \(T:X\to Y\) with \(X\ne Y\), those expressions have no canonical meaning.

The repair statement uses only the Markus inequalities quoted as Theorem 2.8 in the source. Their two-sided comparison yields pointwise equivalence, up to constants depending on the individual \(H\)-operator, between \(|\lambda_n(T)|\) and \(\alpha_n(T)\), which suffices for weighted sequence membership.

## Originality

The 2024 published article and its arXiv version were inspected at the relevant definitions and theorems. Searches were made for the exact title, DOI 10.2140/involve.2024.17.709, arXiv:2306.03633, Definition 5.1, Theorem 5.5, and synonymous combinations involving compact H-operators, quasi-Banach spaces, approximation schemes, corrections, errata, and failure of linear closure. No prior correction or equivalent objection was located.

The September 2026 preprint arXiv:2609.14381v1 is highly relevant because its abstract again advertises a quasi-Banach framework for compact \(H\)-operators between Banach and quasi-Banach spaces. Only its abstract was inspected; the full theorem statements were not inspected. Accordingly, this record does not claim that the 2026 preprint repeats the exact 2024 definitions or that its theorems fail.

The underlying fact that similarity to a real diagonal matrix gives an \(H\)-resolvent bound is standard, and non-additivity itself is elementary. The originality claim concerns identifying the concrete obstruction to the published approximation-space ambient construction and isolating a clean repair.

Originality status: pass, to the best of our knowledge, with the stated residual risk.

## Value

The obstruction is dimension two, explicit, and attacks a structural hypothesis rather than a numerical edge case. It distinguishes the valid per-operator spectral estimates from the invalid claim that all compact \(H\)-operators form a quasi-Banach approximation ambient space. The repair shows how the useful spectral comparison can survive inside a genuine linear operator space.

Because a new 2026 preprint explicitly extends the same H-operator approximation-space program, clarifying this boundary is timely.

## Scientific limitations

- No claim is made that every result of the 2024 paper is false. Set-theoretic consequences of Markus' estimates can remain valid after reformulation.
- No theorem-level judgment is made about arXiv:2609.14381v1 because only its abstract was inspected.
- An earlier correction using different terminology could have escaped the searches.
- The constants in the spectral/approximation-number comparison depend on the individual H-resolvent constant unless a uniform H-class is imposed.
