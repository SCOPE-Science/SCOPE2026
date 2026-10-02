# Independent audit — Prime-indicator parity in Tunnell-type comparison progressions

Audit date: 2026-10-01 (UTC) UTC

## Final claim assessed

The scientific claim in `RESULT.md` and `SLOGAN.txt` was assessed unchanged.

## Correctness — PASS

The proof was reconstructed row by row. For the three-square comparator, Gauss class-number formulas and genus theory yield the required composite evenness of \(r_3(n)/8\); the source prime lemmas give oddness at prime indices. For \(x^2+3y^2+5z^2\), the sign-orbit reduction and the class groups for discriminants \(-12\) and \(-60\) give the exact binary-representation parity, including the separate \(n=3m\) branch. An independent exact enumeration through 100000 reproduced 29,548 row-membership checks and the outside-row values at 39 and 111.

## Originality — PASS

The source supplies the prime case and comparison mechanism, but the all-square-free prime-indicator theorem requires an additional genus-theoretic synthesis.

### Equivalent formulations
The parity identity and its extra \((1+i)\)-divisibility formulation were compared as equivalents. Evidence: No direct prior match other than the audited record was found.

### Broader coverage
The broader comparison framework does not imply the composite statement without the additional genus/binary-form argument. Evidence: The source gives the all-index coefficient congruence and prime oddness, not composite parity.

### Exact database or table
The final claim is quantified over infinitely many indices, not a table lookup. Evidence: The tables define the rows but do not contain the all-square-free theorem.

### Claim versus prior implication
The new synthesis is required. Evidence: No single inspected prior theorem yields the all-twelve-row prime-indicator identity.

### Source inspections
- **Tunnell-type criteria for variants of the congruent number problem** — https://arxiv.org/abs/2609.19085. Trigger: Same comparators and residue rows. Material read: Relevant full-text Section 7, Proposition 7.1, Lemmas 7.2--7.3, and comparison tables. Assessment: The paper supplies the comparison congruences and prime oddness, not the all-square-free-composite theorem. Evidence: The parity lemmas are prime-index statements.

Checked sources: https://arxiv.org/abs/2609.19085; https://doi.org/10.1002/9781118400722; published scientific archive semantic search

Residual risks: The source is very recent, so concurrent unindexed work remains possible.

## Scientific value — PASS

The theorem gives a motivated structural boundary for the exact first congruence layer used in a current Tunnell-type method: it proves that the same layer cannot certify composite nonvanishing on the published rows.

## Reproducibility

An independent exact-integer replay through 100000 reproduced 29,548 row-membership checks and the two stated outside-row counterexamples.

## Disposition

**PASSED.** The unchanged final claim passes correctness, originality, and scientific value.
