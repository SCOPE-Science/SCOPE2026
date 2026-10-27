# Scientific review: ranked spectral staircase and hole thresholds

## Correctness — PASS

Fock radial moments give an exact diagonalization. The adjacent rank-\(N\) block difference is an explicit polynomial with strictly negative coefficients through degree \(k\), strictly positive coefficients thereafter, and exactly one simple positive root. Discrete unimodality orders those roots, classifies every optimal rank-\(N\) subspace and proves the exact positive one-sided derivative jump. The large-index formula follows from a uniform factorial-geometric-mean expansion, and the large-area law from the exact root equation. The packaged Python checker returned `CHECK_OK: 735 exact coefficients, 224 spectral tests, 18 asymptotic tests`; finite tests are support, not a general proof.

## Originality — PASS, with historical-priority uncertainty

Abreu (arXiv:2607.28376, 30 July 2026) proves disk maximality for Ky Fan sums, without annular spectral flow. Nicola--Riccardi--Tilli (arXiv:2503.07069, 10 March 2025) prove the radial fixed-area inequality and explicitly find the first eigenvalue-pair annulus: the known \(A_{0,1}(s)=s/(e^s-1)\). General radial Toeplitz diagonalization appears in Grudsky--Vasilevski (2002). These known facts and the simple special case are not claimed new. The inspected primary claims do not provide the full all-rank ordered staircase, exact one-root theorem and both sharp threshold asymptotics. Targeted indexed searches found no statement equivalent to the combined result, but unindexed historical overlap remains possible. See `AUDIT.json` for exact comparison queries and source inspections.

## Value — PASS

The natural Gaussian Ky Fan objective selects a finite family of Hermite modes from the complete radial spectrum. The theorem describes its *entire* phase diagram as a fixed-area annular hole grows, including strict spectral changes and a sharp tiny-hole crossover in the large-area regime. The exact asymptotic constants and general rank dependence are not simple restatements of the known first-eigenvalue annulus.

## Scientific limitations

One complex dimension, Gaussian window, concentric fixed-area annuli; the limits hold with the complementary parameters fixed. The result does not imply a global stability inequality for nonradial masks or a simultaneous double-scaling asymptotic. Unindexed descriptions of annular spectral ordering are a residual priority risk.

Self-review: passed. Independent audit: not yet performed.
