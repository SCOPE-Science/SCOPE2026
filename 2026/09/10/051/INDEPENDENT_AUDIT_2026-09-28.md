# Independent Audit — 2026-09-28

**Record:** `2026/09/10/051`  
**Title:** Kronecker coefficient counterexample at n=24: 134682  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `d042c9fd070575bba3f9d7f6c1216a3f19064d3a`  
**Disposition:** **PASSED**

## Independent checks

- Implemented rim-hook enumeration and Murnaghan–Nakayama recursion independently from repository artifacts.
- Summed χ^A_μχ^B_μχ^C_μ/z_μ exactly over every partition μ of 24.
- Compared the exact triple against current atomic/vector-partition literature and Resultary records.

## Three-axis assessment

- **Correctness — PASS**: A completely separate Murnaghan–Nakayama implementation recomputed the exact character sum over all 1575 partitions of 24 and obtained g((9,7,5,3),(8,7,5,4),(7,6,6,5))=134682 with 671 nonzero class contributions. Exact Fraction arithmetic eliminates rounding. Since the target asserted vanishing for every even m≥6, this m=6 value is a decisive counterexample.
- **Originality — PASS**: The exact triple/value was not found in targeted web or Resultary searches. Mishna–Rosas–Sundaram and Mishna–Trandafir provide atomic/vector-partition machinery and vanishing conditions, but the retrieved statements do not tabulate this n=24 coefficient or imply its value. Originality is limited to the exact counterexample/value, not to Murnaghan–Nakayama computation itself.
- **Scientific Value — PASS**: The coefficient is a decisive falsification of the proposed infinite vanishing ray at its first allowed parameter and provides a useful deep four-row benchmark. Its broader value is moderate because the conjecture was an internal target rather than an established published conjecture, but the exact large positive coefficient is independently retrievable data.

## Findings

- Current main tree equals assigned SHA.
- Independent exact computation gives 134682 and 671 contributing conjugacy classes among 1575 partitions of 24.
- Small sanity checks and identity-character dimensions are consistent with the implementation.
- Only the proposed even-m ray is falsified; no conclusion is drawn about other rays or odd m.

## Sources compared

- Repository record 051 RESULT.md: https://github.com/SCOPE-Science/SCOPE2026/blob/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/10/051/RESULT.md — States the n=24 coefficient and target-ray refutation.
- Mishna–Rosas–Sundaram, Vector partition functions and Kronecker coefficients: https://arxiv.org/abs/1811.10015 — Introduces atomic Kronecker coefficients/vector-partition machinery; it does not give this exact coefficient.
- Mishna–Trandafir, Estimating and computing Kronecker coefficients: a vector partition function approach: https://arxiv.org/abs/2210.12128 — Provides vanishing conditions and computation framework; the retrieved statements do not cover this exact deep four-row triple.

## Limitations

- The independent recomputation still uses the classical Murnaghan–Nakayama rule rather than a second CAS such as Sage/GAP, though it was written separately from the repository code.
- Novelty is claimed only for the exact value/counterexample after targeted searches, not for the general character-sum method.

This audit is independent of the repository’s pre-existing audit material. GitHub was read only as evidence; no repository changes were made by this audit run.
