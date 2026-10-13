---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The theorem was checked in two complementary ways.

First, the proof derives an exact local witness condition. For an omitted \(a_i\), any witness \(b_j\) has omitted neighborhood \(\{a_k:k\in I,\ k\ne j\}\). This immediately bounds \(|I|\) by two and forces index disjointness when equality holds; symmetry supplies the same conditions on \(J\). The converse explicitly chooses witnesses, with \(n=3\) handled separately.

Second, `verify_super_crown.py` exhaustively enumerates all subsets of the crown graph for \(3\le n\le8\), tests the defining super-domination condition directly, compares that result with the theorem's criterion, checks every coefficient of the bivariate enumerator, and checks the minimum size and number of minimum sets. Replay output is:

`VERIFY_OK n_range=3..8 subset_checks=87360 classification_checks=87360 coefficient_checks=51 minimum_checks=6 max_order=16`

The exhaustive range is finite and therefore is not evidence for the unbounded quantifier by itself. The all-order conclusion rests on the symbolic witness proof. The literature comparison also has one explicit access limitation: the 2024 super-domination-polynomial chapter was not available in full text, so its uninspected contents remain a residual originality risk.
