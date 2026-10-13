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
The proof uses exact word identities, not numerical extrapolation. The key finite sign sums are complete combinatorial counts: two copies of each of two anticommuting letters give total sign \(2\) at order four; the \((4,2)\) anticommuting pattern gives \(3\) at order six; and the \((2,2,2)\) pattern gives \(90,30,18,6\) for induced three-vertex anticommutation graphs with respectively \(0,1,2,3\) edges.

The included checker independently enumerates all words of lengths four and six for every simple graph on four labeled vertices with a fixed nondegenerate integer coupling vector. It compares the direct signed-word moments with the symbolic formulas and checks the regular equal-coupling specialization. This finite replay is a consistency check only; the theorem is proved analytically for arbitrary finite \(m\).

The result does not verify or claim any higher-order cumulant formula. It also does not apply unchanged when redundancy relations permit a nonzero trace for a word containing an odd multiplicity.
