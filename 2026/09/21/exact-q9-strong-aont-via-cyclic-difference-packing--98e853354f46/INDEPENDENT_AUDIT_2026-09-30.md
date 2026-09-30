# Independent audit — 2026-09-30

**Record:** `2026/09/21/exact-q9-strong-aont-via-cyclic-difference-packing--98e853354f46`  
**Repository:** `SCOPE-Science/SCOPE2026` at `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Audited tree:** `e72b103dc45e2e9eff3640a4b95915b69f10748b`  
**Disposition:** **PASSED**

## Correctness

**PASS.** The exponent-array reduction is exact: after row/column normalization, a nonzero 2×2 minor is equivalent to distinct coordinatewise differences of the corresponding exponent rows in Z8. Hence any hypothetical 7×7 defining matrix gives a CDPA(7,7;8), and ruling out five rows is sufficient. The Python verifier was inspected. It enumerates exactly 7·6!=5040 normalized nonzero rows, checks all seven canonical missing-residue cases, obtains 64 neighbors and 24 compatibility edges with no triangle in each case, and verifies an explicit four-row witness. Its independent finite-field arithmetic also verifies the published 6×6 F9 lower-bound matrix is nonsingular with every entry and every 2×2 minor nonzero.

## Originality

**PASS (literature-bounded).** Nasr Esfahani–Stinson leave the exact q=9 strong-AONT parameter at 6≤M_R([1,2],9)≤7. Yin's 2005 paper was obtained through authorized institutional access and all 12 pages were inspected: it proves the even-q column bound n≤q−1 for k≥3 and constructs CDPA(4,q−1;q) or q−2 families, but it does not state maximum row count four at (n,q)=(7,8) or exclude CDPA(5,7;8). Authorized retrieval of Yin's 2004 difference-packing paper timed out after open-route attempts, so that full text is not claimed as read and remains the principal residual priority risk.

## Scientific value

**PASS.** The result closes a documented one-unit AONT gap and isolates the obstruction as an exact small cyclic-difference-packing extremum rather than only a direct matrix nonexistence computation.

## Literature and evidence

- Nasr Esfahani and Stinson, Rectangular, Range, and Restricted AONTs: https://eprint.iacr.org/2021/1498
- Yin, Cyclic Difference Packing and Covering Arrays: https://doi.org/10.1007/s10623-004-3991-3
- Yin, Difference packing arrays and systematic authentication codes: https://doi.org/10.1360/03ys0037

## Limitations

- The CDPA upper bound is exact but parameter-specific and computer-assisted.
- Yin (2004) could not be fully retrieved in this run and is not claimed as read.
- The AONT conclusion is linear only.

This audit was performed independently of the same-model review. GitHub was used only as evidence; no repository write was made by the auditor.
