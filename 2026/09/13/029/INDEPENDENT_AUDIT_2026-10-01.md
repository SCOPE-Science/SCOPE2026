# Independent mathematical audit — SCOPE-20260913-029

Disposition: **PASSED**.

## Correctness
**PASS** — The two-atom moment inversion is complete across the nonregular and regular strata. For positive degree variance, the first three star moments recover the unordered block sizes and block degrees; P4 then recovers the cross density and hence the diagonal densities. On the regular stratum, the triangle recovers the unique real cube-root parameter and the diamond recovers the block-size product unless the graphon is constant. Boundary edge probabilities do not break these polynomial identities.

## Originality
**PASS** — Targeted Resultary and literature comparison found only broader per-stepfunction finite-forcibility results, not a parameter-independent connected-graph cutoff of four for all two-block graphons.

### Equivalent formulations
The claim is equivalent to injectivity, modulo block swap and the constant degeneration, of the six-density map on the 2-block parameter space.

### Broader coverage
Generic stepfunction forcibility does not imply one parameter-independent family of connected graphs on at most four vertices for every 2-block graphon.

### Exact database or table
This is a theorem/inversion statement rather than a standard tabulated invariant.

### Claim versus prior implication
No inspected stronger theorem mechanically implies the stated explicit uniform cutoff.

## Value
**PASS** — A uniform explicit forcing cutoff for the basic nontrivial stochastic-block/step-graphon class is a natural structural identification theorem, not an arbitrary finite calculation.

## Source inspections
- **Finitely forcible graphons** (arXiv:0901.0929): Abstract/theorem-level statements located through search; compared with the record's uniform explicit cutoff. Assessment: BROADER_BUT_NOT_COVERING. Individual stepfunction finite forcibility is weaker than a single four-vertex forcing family for all two-block graphons.
- **Record artifact verify_identities.py** (repository blob 0e797bcc2aecef0d564e3d62f6570cbfa65506de): Complete source file. Assessment: SUPPORTS_CORRECTNESS. Moment identities and regular/nonregular reconstruction are algebraically consistent.

## Residual risks
- Targeted searches did not locate an exact prior statement; that absence is not treated as a proof of novelty.
- The artifact inventory used an obsolete output/artifacts prefix; the actual verifier is under artifacts/ and the metadata plan corrects that path.
