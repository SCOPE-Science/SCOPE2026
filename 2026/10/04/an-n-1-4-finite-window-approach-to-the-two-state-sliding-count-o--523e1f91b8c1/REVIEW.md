# Same-model review

## Correctness
PASS. The chain's stationary law and right spectral gap are explicit. The proof derives the complete first-order rare-entrance path types, projected edge conductances, and resulting energy/variance coefficients. The finite-window sums are exact. Their balanced expansion gives the stated correction, while the explicit choice \(u_n=\exp(-n^2)\) makes all higher-entrance corrections superalgebraically negligible. The spectral-gap statement uses only the Rayleigh variational upper bound. `verify.py` independently reproduces the first-order identities and asymptotic coefficient.

## Originality
PASS. The closest primary source, arXiv:2609.27836v1, obtains the two-state \(1/4\) obstruction through ordered limits and explicitly states that its argument gives no quantitative convergence rate for finite witnesses. The present result narrows to that two-state family but supplies an explicit finite sequence and its first correction. Targeted semantic searches for aliases, rare-state formulations, projected birth--death kernels, and an \(n^{-1/4}\) rate found no equivalent published record. The earlier arXiv:2608.08678 concerns fixed-kernel strict-positivity bounds according to the later primary paper; its full text was not directly retrievable, so this remains a stated access risk.

## Value
PASS. The construction resolves a mathematically motivated finite-realization issue identified by the source itself. The \(n^{-1/4}\) correction is not just a numerical fit: it comes from balancing persistence approach against subcritical test truncation, and the leading coefficient is exactly optimized within the resulting natural two-parameter scaling.

## Closest literature and limitations
Xiang and Zhang, arXiv:2609.27836v1, is the decisive closest source. Its qualitative diagonal construction is broader in state-space size but weaker in finite-witness quantification. This result does not prove \(c_2^\star=1/4\), does not identify the exact gap of the projected kernel, and does not claim the rate is globally optimal. The earlier arXiv:2608.08678 could not be fully inspected, leaving a residual access risk recorded in `AUDIT.json`.

Same-model review: passed. Independent audit: not yet performed.
