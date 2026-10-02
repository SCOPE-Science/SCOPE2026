# Independent mathematical audit — 2026-09-30

## Outcome

**PASSED** for the final finding as stated.

## Correctness — PASS

The matrix exponential formula is exact because the nilpotent superdiagonal shift truncates after degree \(n-1\). The committed verifier was read in full: it encloses \(e^{-t}\) by an alternating-series remainder, obtains lower bounds from rational test vectors, covers every time in \([0,30]\) by a \(0.01\)-grid Frobenius bound plus \(\lVert T_n\rVert_F\)-controlled growth, and proves the tail decreases entrywise for \(t\ge30\). An independent direct singular-value calculation at the five stated rational test times gave approximately 25.1451, 89.1061, 323.3773, 1192.4493 and 4447.7307, all inside the claimed intervals. The interval division therefore also certifies the stated dimension-growth ratio.

Checked sources:
- a
- c
- t
- u
- a
- l
-  
- c
- o
- m
- m
- i
- t
- t
- e
- d
-  
- `
- a
- r
- t
- i
- f
- a
- c
- t
- s
- /
- v
- e
- r
- i
- f
- y
- .
- p
- y
- `
-  
- a
- n
- d
-  
- `
- a
- r
- t
- i
- f
- a
- c
- t
- s
- /
- v
- e
- c
- t
- o
- r
- s
- .
- j
- s
- o
- n
- `
- ;
-  
- i
- n
- d
- e
- p
- e
- n
- d
- e
- n
- t
-  
- s
- p
- e
- c
- t
- r
- a
- l
- -
- n
- o
- r
- m
-  
- r
- e
- c
- o
- m
- p
- u
- t
- a
- t
- i
- o
- n

Residual risks:
- The upper certificate uses Decimal arithmetic with an explicit slop margin rather than formal directed-rounding interval arithmetic, as already disclosed.
- The certified intervals are intentionally coarse and do not locate the exact maximizing times.

## Originality — PASS

The exact five certified peak intervals and their enclosed cross-dimension ratio were not found in the inspected transient-growth literature or published-result search. The surrounding literature treats Kreiss constants, pseudospectra, and general mechanisms for nonnormal transient growth rather than this finite certified table.

### equivalent_formulations

Searches: Resultary semantic search: transient peak \(T_n=-I+2N\), Jordan-block matrix exponential, certified peak intervals; Reuter, arXiv:1909.05931, transient growth and invariant subspaces

Evidence: The only exact semantic hit was the audited record. Reuter gives sufficient structural conditions for transient growth, not these maxima.

Reasoning: Aliases such as stable Jordan block, truncated exponential Toeplitz semigroup and transient amplification were compared; none of the inspected statements is equivalent to the five interval table.

### broader_coverage

Searches: Mitchell, Computing the Kreiss Constant of a Matrix, arXiv:1907.06537; Reuter, arXiv:1909.05931

Evidence: These works address general computation/structure of transient growth and Kreiss-type quantities.

Reasoning: General Kreiss or pseudospectral bounds do not imply the concrete two-sided maxima without additional computation; no dominating theorem producing the five values was identified.

### exact_database_or_table

Searches: Resultary search for the exact matrix family and dimensions; Search for Jordan-block transient peak tables

Evidence: No external or published-result database/table with these five certified values was found.

Reasoning: The record is not a re-tabulation of an inspected standard numerical table.

### claim_vs_prior_implication

Searches: Comparison with general transient-growth sufficient conditions and Kreiss bounds

Evidence: The general results establish possibility or bounds, not the exact finite peak intervals or the quoted ratio.

Reasoning: No inspected prior theorem mathematically entails the final certified table as a direct corollary.

### source_inspections

- **Transient growth in stable linear systems and invariant subspaces** (https://arxiv.org/abs/1909.05931): trigger=Same nonnormal stable-matrix phenomenon and Jordan/invariant-subspace mechanism.; material read=Accessible full arXiv HTML sections stating the transient-growth setup and sufficient-condition theorem.; method=Primary full-text inspection.; assessment=RELATED, NOT COVERING.; evidence=The theorem gives structural sufficient conditions for transient growth; it does not evaluate the audited finite maxima.
- **Computing the Kreiss Constant of a Matrix** (https://arxiv.org/abs/1907.06537): trigger=Closest general numerical framework cited by the record.; material read=Accessible abstract/metadata and stated scope.; method=Primary-source inspection.; assessment=RELATED, NOT COVERING.; evidence=It develops computation of the Kreiss constant, a different quantity from the audited five global matrix-exponential peaks.
- **Committed transient-peak verifier** (artifacts/verify.py): trigger=Critical finite certificate.; material read=Complete source file plus complete rational-vector file.; method=Line-by-line source inspection and independent numerical replay at the five witness times.; assessment=Supports the finite C claim; it is not novelty evidence by itself.; evidence=All independently recomputed witness norms lie strictly inside the certified intervals.

### checked_sources

- arXiv:1909.05931
- arXiv:1907.06537
- Resultary semantic search
- committed verifier and vectors

### residual_risks

- A specialized numerical-linear-algebra table not indexed by the searched sources could overlap.
- Best-of-knowledge originality is not a priority certificate.

## Scientific value — PASS

A canonical stable Jordan-block family is a standard stress test for nonnormal transient amplification. Certified global peak intervals across several dimensions, together with an enclosed growth ratio, provide a reproducible benchmark for algorithms that otherwise rely on local optimization or pseudospectral surrogates. The object and invariant are motivated independently of the computation.

Checked sources:
- transient-growth/Kreiss literature cited above

Residual risks:
- The family is a toy benchmark rather than a fluid-mechanics discretization; the result should not be generalized beyond the stated sequence.

## Limitations

- The result is restricted to \(n\in\{8,10,12,14,16\}\) for \(T_n=-I+2N\).
- The upper proof uses a Frobenius envelope and deliberate numerical slack rather than formal interval arithmetic.
- The repository stores the inspected artifacts at `artifacts/...`; older prose/metadata still use the legacy `output/artifacts/...` prefix. This is a packaging-reference defect, not a mathematical defect.
