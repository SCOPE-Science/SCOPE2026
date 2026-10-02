# Independent mathematical audit — 2026-10-01

## Final claim

For every \(g>1\), the greedy strict 2-sumfree sequence \(S_{1,g}\) has the stated closed form; for even \(g\ge8\) its eventual characteristic sequence has modulus \(4g+3\) and the stated residue set, and the resulting preperiod and period lengths are exactly the \(f=1\) cases conjectured by van Berkel--Bosma.

## Correctness — PASS

PASS. The infinite proof was reconstructed from the modular identities, not from the saved success log. For even \(g\ge8\), the proposed residue set \(R_g\) modulo \(4g+3\) is disjoint from \(R_g+R_g\), while translates by the four selected prefix values \(1,g,2g,2g+3\) cover every complementary residue. Together with the explicitly verified initial block, these two identities give the greedy induction for all later integers. The circular gap pattern has trivial translational stabilizer, so the eventual characteristic period is minimal; the final exceptional selected term forces the stated minimal preperiod. Odd \(g\) and \(g=2,4,6\) reduce to the displayed elementary cases. Independently, I regenerated the sequence for every \(2\le g\le80\) well beyond multiple predicted periods and rechecked the residue identities for every even \(8\le g\le100\), with no discrepancy.

## Originality — PASS

PASS. Van Berkel--Bosma's full primary preprint explicitly labels the general period and preperiod formulas as conjectures, proves only other parameter ranges, and reports finite computations through large boxes. Its \(f=1\), \(g>1\) column is not covered by the proved theorems. The audited result proves that entire infinite column and supplies a closed modular description, so it is not a corollary of the finite computational evidence. Exact/synonymous searches and the published-record repository search found no independent prior proof of the \(4g+3\) residue theorem.

### Equivalent formulations

A proof of the full \(f=1\) column is mathematically stronger than finite confirmation of the conjectured values.

### Broader coverage

Those theorems do not determine the audited \(f=1\) sequence for arbitrary \(g\), nor the exact minimal period/preperiod.

### Exact database or table

Finite tables cannot establish the infinite claim, and the proof supplies the missing universal argument.

### Claim versus prior implication

The audited residue identities are new field-specific input required to settle this column.

## Scientific value — PASS

PASS. This proves an infinite natural one-parameter family inside two principal conjectures, gives every term explicitly, and determines minimal preperiod and period rather than merely eventual periodicity. The sum-avoiding residue set plus finite translate cover is a reusable mechanism for greedy additive sequences and clearly exceeds a finite table computation.

## Sources inspected

- **Daan van Berkel and Wieb Bosma, Periodicity Conjectures for All 2-Sumfree Sequences** (arXiv:2609.18522): DIRECT_CONJECTURAL_MOTIVATION_NOT_COVERAGE. The paper leaves the general formulas conjectural, proves other slices, and verifies finite ranges computationally; it does not prove the complete \(f=1\) column.

## Residual risks

- The motivating papers are extremely recent, so contemporaneous unindexed work remains a residual originality risk.
- The finite verification range is evidence only; correctness of the universal theorem rests on the modular proof.

## Disposition

**passed**
