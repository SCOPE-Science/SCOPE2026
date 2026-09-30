# Independent audit — 2026-09-29

**Record:** `2026/09/12/080`  
**Disposition:** **repaired**  
**Audited tree:** `30e4eb8634bb7b0af104c77f4493e025270f4267`

## Correctness
The exact constant-force Verlet identity is sound and archived finite runs reproduce very large projection-induced drift, but the filed statement quantified over every h in (0,0.01] and every datum in an open set. The record itself admits that the Gronwall/Taylor remainder and RK4 integral are not interval-enclosed; sampled step sizes and sampled initial conditions cannot prove that universal theorem. The repair narrows the claim to the exact algebraic identity and the actual finite computations.

## Originality
The projection-work decomposition and this benchmark data are potentially useful, but no defensible priority claim is made. Standard SHAKE/RATTLE and geometric-integration literature already provides the surrounding framework.

## Scientific value
As a reproducible benchmark showing how a naive projection baseline can accumulate large energy error while the constant-force unprojected step preserves H exactly, the corrected record is useful; its value does not depend on the unsupported universal lower bound.

## Findings
- Universal all-h/all-data lower bound was not rigorously certified by the supplied evidence.
- The proof paragraph had inconsistent force/sign notation; the archived code uses p <- p - h grad U and the corrected file states the identity consistently.
- Repository artifact paths are `artifacts/...`, not `output/artifacts/...`.

## Independent checks
- Verified the current record did not change after the assignment inventory commit.
- Inspected exact implementation of the projected step and archived table.
- Checked the algebraic constant-force energy identity independently.

## Limitations
- No interval enclosure of the whole initial-data neighborhood or continuum of step sizes was available.

## Sources
- repository:2026/09/12/080/RESULT.md
- repository:2026/09/12/080/artifacts/core.py
- repository:2026/09/12/080/artifacts/table_anchor.json
- https://lagrange.mechse.illinois.edu/pubs/We2004/We2004.pdf
