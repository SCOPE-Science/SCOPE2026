# Scientific audit — SCOPE-20260911-061

Date (UTC): 2026-10-01

## Final claim

For the stated connected genus-zero refined floor-diagram problem on F0 in bidegree (3,4), exactly 80 connected diagrams contribute; the Laurent coefficient vector from exponents minus six through six is 1, 16, 140, 868, 4222, 16396, 44258, 16396, 4222, 868, 140, 16, 1, with value 87,544 at one and 18,424 at minus one.

## Correctness

**PASS** — A fresh enumeration from the stated three connected tree patterns independently reproduced 50 chain, 15 fan-from-first, and 15 fan-into-third diagrams, total marking count 26,422, the complete Laurent coefficient vector, value 87,544, signed specialization 18,424, and the three per-pattern unrefined contributions. The committed connected ledger and package counting code were also inspected.

## Originality

**PASS** — Published-search results locate this exact coefficient table only in the record. General refined floor-diagram theory supplies the counting framework and invariance but does not tabulate or directly imply the complete connected (3,4) ledger.

### Equivalent formulations
Searches by total, bidegree, genus, and coefficient-table formulation did not uncover an equivalent published table.

### Broader coverage
General theory does not mechanically output the 80-row finite table without enumeration.

### Exact database or table
No exact external database/table coverage was found.

### Claim versus prior implication
The general theorem defines the invariant but does not imply these numbers without the complete finite computation.

## Value

**PASS** — A full refined coefficient ledger for a natural low bidegree on P1 by P1 is a reusable exact benchmark for refined curve counting and specialization checks. It is a complete finite classification rather than an arbitrary parameter sample.

## Sources inspected

- Package result, connected ledger, and counting code: https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/11/061/RESULT.md — Supports the exact 80-diagram coefficient table.
- Refined curve counting with tropical geometry: https://arxiv.org/abs/1407.2901 — Supports the general framework but does not give the exact (3,4) connected table.
- Resultary published-results search: https://github.com/Resultary/2026/tree/main/2026/9/11/SCOPE061 — No independent exact table or dominating finite classification was found.

## Residual risks and limitations

- The audit verifies the connected combinatorial ledger; the interpretation of the minus-one specialization as a real enumerative count was not independently rederived.
- The package replay script writes to a historical absolute workspace path, while the committed connected ledger itself is present and was inspected.
- No independent published closed-form value for this exact bidegree was located.

## Disposition

PASSED
