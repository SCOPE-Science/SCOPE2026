# Self-review

## Correctness

PASS. The continuous spore-production term evaluates \(IH\) at delayed time, while the printed finite-difference sum uses the current \(IH\) outside the history sum. Its zero-mesh limit is therefore a different integral operator. With \(\alpha\equiv1\) and \(IH(t)=t\), the difference is exactly the positive first moment of the sporulation kernel. The bundled symbolic checker verifies a strict shifted-gamma witness.

## Originality

PASS. Consistent quadrature of a Volterra integral is standard. The accepted contribution is the source-specific diagnosis that the published rice-blast update converges to the wrong memory law and that the mismatch survives mesh refinement. The direct predecessor repeats the same indexing but does not identify it as an error. Exact-source, equation-number, correction, and delayed-product searches found no published repair.

## Value

PASS. The paper states that equation (2.28) is used for its simulations and then uses those simulations to fit the spore-deposition fraction and evaluate disease-severity agreement. The wrong continuum operator therefore bears directly on the central numerical and biological conclusions rather than on a cosmetic formula.

## Closest literature and limitations

The closest source is the authors' 2022 predecessor, which already prints the same structural replacement of a delayed host product by a current host product. That is prior art for the formula, not for the consistency diagnosis.

Unavailable implementation code could have silently corrected the time indices. The finding therefore establishes a publication-level reproducibility and mathematical-consistency defect, without asserting what an unpublished implementation did.

Self-review: passed. Independent audit: not yet performed.
