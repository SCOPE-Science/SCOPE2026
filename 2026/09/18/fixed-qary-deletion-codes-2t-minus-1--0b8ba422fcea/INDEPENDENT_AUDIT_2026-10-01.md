---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

For every fixed alphabet size \(q\ge2\) and fixed \(t\ge2\), there exist \(q\)-ary length-\(n\) codes correcting \(t\) deletions with redundancy \((2t-1)\log_q n+O_{q,t}(\log_q\log n)\).

## Correctness — PASS

The extension-specific proof was reconstructed from the assigned result. The collision probability for two q-ary length-k windows is exactly q^{-k}, including overlaps, so the chosen k leaves a constant-density k-unique family. The de Bruijn-spectrum argument is alphabet-independent. In the local bubble lemma the binary complement is not used: disjointness only needs the two run-boundary symbols to differ from the edited symbol. Exceptional alignments acquire only a q^d factor, and witness recovery acquires only q^{O_t(R)} local choices; for fixed q,t these are absorbed into the hash-label constant without changing the positional exponent (2t-1)R. These are exactly the alphabet-sensitive points needed to transfer the established binary witness argument.

**Checked sources.** Assigned RESULT.md at tree f484e96594997bfa5c2512e8e914687a37522c7a; E. En Gad, arXiv:2609.19493; W. Song and K. Cai, arXiv:2210.14006; published corroborating derivation dated 2026-09-18

**Residual risks.** The full text of the very recent En Gad preprint could not be retrieved through the available open-access route in this run; the binary theorem itself was therefore treated as the cited prior theorem while the q-ary transfer steps were checked from the assigned proof.

## Originality — PASS

The exact fixed-q coefficient was not located before this record. The motivating En Gad paper proves the binary coefficient only. A later same-day corroborating record explicitly identifies this assigned record as the earlier occurrence, and the next-day broader q-ary record postdates it. Earlier q-ary two-deletion constructions located in the primary literature have larger leading redundancy.

### Equivalent formulations

Equivalent terminology such as q-ary insertion/deletion codes and edit-distance codes was included; no earlier statement with the same asymptotic coefficient was located.

### Broader coverage

No stronger pre-record theorem located dominates the claim.

### Exact database or table

This check is inapplicable as a tabular lookup; the relevant comparison is theorem-level asymptotic coverage.

### Claim versus prior implication

No checked prior implication mechanically yields the q-ary theorem without those new transfer steps.

**Checked sources.** https://arxiv.org/abs/2609.19493; https://arxiv.org/abs/2210.14006; published corroborating record dated 2026-09-18; published q-ary generalization dated 2026-09-19

**Residual risks.** The source binary preprint is recent and its full text was unavailable in this run. Parallel work not indexed by the searched corpus may exist.

## Value — PASS

The theorem answers a natural fixed-alphabet extension of a new deletion-code coefficient improvement and shows that the one-power-of-n gain is not binary-specific. For t=2 it changes the fixed-q existential leading coefficient from the generic 4-style scale to 3, while keeping the proof mechanism structurally transparent.

**Residual risks.** The construction is existential and does not improve efficient q-ary code constructions.

## Limitations

- The theorem is existential and does not provide efficient encoding or decoding.
- The constants may depend on fixed \(q\) and \(t\); the claim is not uniform for growing alphabet size.
- The motivating binary preprint is extremely recent, so parallel unindexed work remains a residual originality risk.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
