---
audit_date: 2026-10-01
status: passed
---

# Scientific audit

## Final claim

For every integer \(f\ge5\), the strict greedy 2-sumfree sequence \(S_{f,2f+1}\) has the stated residue description modulo \(5f+1\), minimal preperiod length \(f+1\), and minimal difference-period length \(f+2\).

## Correctness — PASS

The residue proof was reconstructed: displayed tail residues are disjoint from all allowed sums of distinct prefix/tail residues, while every omitted integer in each complementary gap has an explicit representation as a sum of two distinct earlier displayed terms. The resulting difference block has length \(f+2\); the exceptional initial gap and the unique large gap in the period force minimal preperiod and period. An independent greedy implementation checked the exact membership formula and repeating difference block for every \(5\le f\le20\); this finite check corroborates but does not replace the modular proof.

**Evidence.** RESULT.md; artifacts/verify.py blob 63c1ebaf7f413f1b26c609a5858bbd8316795195; van Berkel–Bosma, arXiv:2609.18522

**Residual risk.** The theorem proves one off-diagonal family, not the full eventual-periodicity conjecture.

## Originality — PASS

The full primary paper arXiv:2609.18522 was inspected. It says the proven family reaches \(g\le2f\) and conjectures period/preperiod formulas beyond that boundary; the audited line \(g=2f+1\) is therefore the first adjacent unproved line for \(f\ge5\). Public-corpus searches found later dated results extending or repeating this line on 2026-09-19 and 2026-09-20, but those postdate the 2026-09-17 record and do not establish prior coverage. No earlier paper proving the all-\(f\) line was located.

**Equivalent formulations.** The modular-residue formulation and the period/preperiod formulation are equivalent descriptions of the same sequence.

**Broader coverage.** The known family stops exactly one line before the audited theorem and hence does not imply it.

**Exact database or table.** The audited infinite modular proof supplies what the tables do not.

**Claim versus prior implication.** A conjectural table entry does not imply the all-parameter theorem.

### Source inspections

- **van Berkel and Bosma, arXiv:2609.18522** — full paper through the conjecture and computed period/preperiod sections. States proofs through \(g\le2f\) and leaves the neighboring line within the conjectural regime.
- **later public findings dated 2026-09-19 and 2026-09-20** — search-result scientific summaries. Contain stronger/repeated neighboring-line results but postdate this record.

**Checked sources.** https://arxiv.org/abs/2609.18522; https://arxiv.org/abs/2609.16843; semantic search of the public findings corpus

**Residual risk.** The topic was moving rapidly in September 2026; simultaneous external work not yet indexed remains a modest priority risk.

## Value — PASS

The result proves an infinite parameter line immediately beyond a newly published boundary, with a complete residue description and minimal periods rather than empirical confirmation. It advances a natural two-parameter periodicity conjecture in the most adjacent unresolved direction.

**Residual risk.** Later work already extends the result further, so its enduring value is as the first boundary step rather than the final classification.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
