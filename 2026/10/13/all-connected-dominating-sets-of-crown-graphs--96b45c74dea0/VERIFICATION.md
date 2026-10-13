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
The arbitrary-\(n\) statement is established symbolically. The critical steps are: (1) a connected dominating set must select at least two vertices from each bipartition class; (2) those size inequalities already imply domination; (3) the induced selected graph is disconnected only when exactly two indices are selected on each side and the two index sets coincide; and (4) any larger connected dominating set admits a vertex deletion preserving the criterion, so every inclusion-minimal one has size \(4\).

The standalone checker `verify.py` constructs each crown graph directly and tests domination and induced connectivity without using the symbolic characterization as its graph-property oracle. It exhaustively checks every subset for \(3\le n\le9\), compares direct graph truth with the theorem's criterion, rebuilds the polynomial coefficients, checks the minimum multiplicity and total count, and separately tests inclusion-minimality.

Replay command:

`python3 verify.py`

Expected output:

`VERIFY_OK n_range=3..9 subset_checks=349504 criterion_checks=349504 coefficient_checks=91 minimal_checks=2786 max_order=18`

The finite computation is a stress test only and is not an exhaustive proof for all \(n\). No independent audit has been performed.
