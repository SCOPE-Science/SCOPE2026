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

The accompanying script constructs \(\operatorname{Cr}_n\) directly and exhaustively checks all \(2^{2n}\) vertex subsets for \(3\le n\le8\). For each subset it evaluates secure total domination from the definition: first total domination, then every outside vertex and every possible adjacent defender, with the swapped set retested for total domination.

The same script independently evaluates the closed four-condition classification, compares both predicates subset by subset, forms the empirical cardinality distribution, and compares that distribution with
\[
\left(\sum_{k=3}^{n}\binom{n}{k}x^k\right)^2+2\binom{n}{2}x^{n+2}.
\]
It also checks the stated minimum sizes and minimum-set counts.

Finite exhaustive checks do not establish the theorem for all \(n\); the all-\(n\) guarantee comes from the proof in `RESULT.md`. The computation is a reproducibility and boundary-condition check.
