# Scientific assessment

## Correctness — PASS
The theorem concerns the time-dependent binary full shift with one forbidden adjacent pair per phase. The gauge \(b_i\mapsto b_i\mathbin{\mathrm{xor}}a_i\) transforms every phase matrix into exactly \(L\) or \(F\), and the monodromy is conjugate because the gauge is periodic. The zero-defect case forbids only \(01\), yielding precisely \(n+2\) prefixes of length \(n+1\). For positive defect count, the monodromy is primitive. The explicit strict entrywise replacement of \(FL^aF\) by \(L^{a+1}F\), followed by Perron–Frobenius comparison, proves the sharp lower spectral radius, with equality exactly at one defect. The polynomial, zeta and schedule counts follow from the two-state graph. The standalone checker verifies every period-\(1\)-through-\(7\) schedule and independent direct finite-prefix and periodic-point counts in small periods; finite checks do not replace the proof for arbitrary \(p\).

## Originality — PASS, conditional on inspected evidence
The primary motivating paper, Livorati–Georgiou–Dettmann–Leonel (arXiv:1312.7030), treats moving and breathing holes and gives numerical approximations and analytical overlap corrections, but not the cyclic two-bit forbidden-word compatibility classification or the exact sharp first-positive-entropy bound. The related Cheriyath–Agarwal static-cylinder theory (arXiv:1905.11767, including Section 4) fixes a union of forbidden words at every iteration, so its correlation-comparison results do not directly imply the periodically changing single-hole theorem. Indexed results on symmetric negative doubling holes, modular gap shifts and dyadic gap shifts address different objects. Extensive historical exhaustiveness is not claimed: an earlier equivalent matrix-product optimization under different terminology is a residual risk.

## Value — PASS
The same hole size, one quarter of phase space at every time, can yield either a countable zero-entropy survivor with exactly polynomially corrected maximal-rate escape or a positive-entropy survivor. The theorem classifies all \(4^p\) periodic schedules for zero entropy, proves that an entire interval of escape rates is impossible for each fixed period, and identifies the precise unique-minimal-defect regime with a closed zeta function and sharp dimension. The all-period lower bound and equality mechanism are a nontrivial structural statement, not merely a numerical table for a fixed short period.

## Limits and priority risk
The binary length-two hole model is essential; higher-memory or nonperiodic holes are not covered. Periodic point claims are for the symbolic system, not ambiguous dyadic endpoint representatives. No independent validation or exhaustive historical priority audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
