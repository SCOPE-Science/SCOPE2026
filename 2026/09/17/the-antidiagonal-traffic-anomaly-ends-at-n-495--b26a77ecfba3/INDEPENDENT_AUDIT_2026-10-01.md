# Independent audit — SCOPE-20260917-013

Audit date (UTC): 2026-10-01 (UTC)

## Final claim

The antidiagonal traffic anomaly in the cited grid-obstruction problem has its last occurrence at n=495: the paper's ratio rho(n) is strictly below one for every integer n at least 496, while the n=495 witness is strictly above one.

## Correctness

**PASS** — The proof was reconstructed from the explicit ratio. The consecutive admissible-k ratio has a strictly decreasing sign polynomial, so the finite maximum occurs at one computable parity-compatible mode. A fresh exact-integer implementation, independent of the committed verifier, checked every n from 496 through 2999 and found no failure; the tightest case was n=497, k=15 with ratio approximately 0.999955284137033, while n=495, k=15 is approximately 1.000024070891585. For the tail, the Robbins central-binomial bounds, even/odd off-centre product estimate, continuous maximization, and monotonicity of the envelope were checked algebraically. The envelope at n=3000 is approximately 0.993774873143844 and decreases thereafter.

## Originality

**PASS** — The primary 2026 grid-traffic paper explicitly leaves disappearance beyond n=495 as Conjecture 7.4 and reports computation only through a finite range. The audited record supplies the missing analytic tail plus an exact finite bridge. No later proof or stronger theorem was found in the published-results or web searches.

### Equivalent formulations

Searches included the ratio notation, the threshold values, the conjecture number, and the lattice-path obstruction formulation. Evidence: The only exact published-results match was this record. The primary paper's accessible review identifies Conjecture 7.4 as the unproved eventual-disappearance statement.

### Broader coverage

Existing reduction lemmas are inputs, not a theorem covering the final threshold. Evidence: The primary paper proves the reduction and unimodality ingredients but stops at the conjecture. No stronger published inequality was located that directly yields the all-n threshold.

### Exact database or table

The exact finite bridge is independently reproduced, but originality depends on the analytic tail that closes all larger n. Evidence: The primary source reports a finite computational window, whereas the audited claim is infinite and cannot be established by a table alone.

### Claim versus prior implication

The final theorem is not mechanically implied by the source because the source explicitly leaves it as a conjecture. Evidence: The source ratio and unimodality reduce the problem but do not imply the required uniform inequality without a tail estimate. The audited Robbins/off-centre envelope supplies precisely the missing implication.

## Value

**PASS** — The result resolves a concrete published conjecture with a sharp threshold and replaces a finite experimental range by an all-n proof. The finite bridge and analytic tail jointly establish a natural extremal boundary rather than an arbitrary computation.

## Sources inspected

- Points of maximal traffic on a grid with obstruction — https://arxiv.org/abs/2609.01562. NOT_COVERING and directly establishes the open-problem status at that version: The source reduces the antidiagonal comparison to an explicit ratio, observes finite anomalies through 495, checks a finite range, and conjectures that no anomaly occurs from 496 onward.
- Committed proof note and verifier — repository artifacts/research_note.md and artifacts/verify.py at the assigned commit. SUPPORTS the complete theorem: The exact finite mode scan and the decreasing Robbins-based envelope jointly cover every n at least 496.

## Residual risks and limitations

- A not-yet-indexed revision or simultaneous proof of the September 2026 conjecture may affect priority.
- The proof uses classical quantitative binomial bounds; an older inequality may shorten the argument, though none was found that already states the sharp 496 threshold.
- The fresh finite scan covered the finite bridge exactly; the infinite part rests on the independently checked analytic envelope, not on extrapolation from computation.
- Originality is best-of-knowledge relative to the very recent conjecture.

## Disposition

**PASSED**
