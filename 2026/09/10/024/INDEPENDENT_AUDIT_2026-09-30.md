# Independent scientific audit — SCOPE-20260910-024

Audited: 2026-09-30 UTC

Disposition: **passed**

## Correctness

**PASS** — Fresh exact reconstruction confirms both discrete random-walk spectra have second eigenvalue 1/3. For the contracted seven-vertex graph the characteristic polynomial is (lambda-1)(3lambda-1)(3lambda+1)(9lambda^2+3lambda-1)(9lambda^2+6lambda-1)/729. Independent interval checks place theta=arccos(1/3) between the committed rational endpoints, giving 12 theta in [14.77151256,14.77151352], 11 theta in [13.54055318,13.54055406], and a certified lower endpoint gap 1.2309585. The equilateral spectral-reduction argument and branch exclusions in the package are consistent with these values.

## Originality

**PASS** — Best-of-knowledge comparison found the general fixed-topology spectral-gap optimization framework but no earlier statement of this exact Q3 equilateral-versus-one-edge-contracted center comparison.

## Value

**PASS** — The comparison eliminates a canonical codimension-one contraction-center competitor in a natural open fixed-topology optimization problem. It is a motivated structural boundary check, not an arbitrary parameter slice, and the exact shared arccos parameter makes the comparison reusable.

## Sources and residual risk

- https://arxiv.org/abs/1608.00520 — Full arXiv text, including optimization setup and main examples; full-text searches for cube/hypercube returned no match. Assessment: General framework; not covering the exact Q3 paired inequality.
- https://github.com/Resultary/2026/tree/main/2026/9/10/SCOPE024 — Published title and summary returned by semantic search. Assessment: Same finding; not independent prior coverage.

Residual risks:
- A differently indexed computation or unpublished topology table could exist; originality is best-of-knowledge, not a universal proof of absence.

The detailed machine-readable audit is in `INDEPENDENT_AUDIT_2026-09-30.json`.
