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
The proof is symbolic and valid for every integer \(n\ge1\). Its critical step is the complete classification of nonempty skew-stalled white sets. For every page, the degree-two neighborhoods \(N(x_i)=\{a,y_i\}\) and \(N(y_i)=\{b,x_i\}\) force the paired membership relations \(y_i\in W\iff a\in W\) and \(x_i\in W\iff b\in W\). This leaves exactly the two bipartition classes and their union as nonempty stalled sets.

The standalone checker `verify.py` independently constructs the graph and simulates the skew color-change process rather than using the proof's stalled-set reduction. It exhaustively tests every initial subset for \(1\le n\le8\), compares with the stated if-and-only-if criterion, reconstructs all polynomial coefficients, and checks the minimum and maximum-failed statistics.

Replay command:

`python3 verify.py`

Expected output:

`VERIFY_OK n_range=1..8 subset_checks=349520 criterion_checks=349520 coefficient_checks=96 minimum_checks=24 max_order=18`

The computation checks only the displayed finite range and is not an exhaustive proof for arbitrary \(n\). No independent audit has been performed.
