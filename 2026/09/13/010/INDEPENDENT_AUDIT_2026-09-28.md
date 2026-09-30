# Independent audit — SCOPE-20260913-010

Date: 2026-09-28 (UTC)  

## Disposition: REPAIRED

### Correctness
Independent exact Groebner computations over Q reproduce the global Jacobian colength 136 and Tjurina colength 101. Kouchnirenko’s Newton-number calculation gives the local Milnor number μ=120 because the exponent (3,2,1) lies strictly above the Fermat face. The lexicographic Jacobian elimination contains z^12(81z^8+13671875), and the remaining equations give 16 distinct nonzero critical points; therefore each is Morse and the origin contributes 120. The local gap is μ-τ=19. Hess(f)(0)=0 and the Behrend critical-locus formula gives ν(0)=120.

The filed Hochschild sentence was underspecified and its proof incorrectly invoked the Koszul complex as if it directly computed Hochschild homology of the derived critical locus. The correct standard statement is categorical: for the matrix-factorization dg category MF(f) of an isolated hypersurface singularity, Hochschild homology is identified with the Jacobian algebra up to the usual parity convention, so its total dimension is μ=120. The repaired record states only the numerical equality dim HH_*(MF(f))=ν(0)=120. The nonstandard use of “positive modality” is removed. Artifact paths are corrected to `artifacts/...`.

### Originality
The general theorems are classical; the record’s contribution is the explicit arithmetic for this particular polynomial. No priority claim beyond that explicit worked example is supported.

### Scientific value
Moderate as a reproducible example linking Newton, Milnor–Tjurina, vanishing-cycle/Behrend and matrix-factorization calculations, provided the categorical scope is stated correctly.

### Sources
- Kouchnirenko, Invent. Math. 32 (1976), DOI 10.1007/BF01389769.
- Dyckerhoff, arXiv:0904.4713.
- Behrend, Ann. of Math. 170 (2009), DOI 10.4007/annals.2009.170.1307.
