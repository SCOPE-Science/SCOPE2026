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

# Verification and scope

The bundled `verify.py` is a standalone Python 3 script using only standard-library integer arithmetic, `fractions.Fraction`, and combinatorial iterators. It regenerates both rank-three deleted-set families and verifies the exact Johnson-neighborhood multiplicities and angular-moment identities for every integer \(7\le n\le11\). For \(n=7\) and \(n=8\) it independently maximizes a weighted basis functional across all surviving bases for each of the \(n!\) strict coordinate rankings, using exact powers of two as score values; all predicted exposure counts agree. This comprises \(5040\) and \(40320\) rankings per family. It also exhaustively checks basis exchange and rank-based Tutte-polynomial coefficient equality for these two dimensions.

To reproduce, run `python3 verify.py` in the directory containing this document and the script. Successful execution ends with `ALL CHECKS PASSED; finite verification does not certify arbitrary n.`. The universal normal-cone law, the f-vector equivalence, and the higher-order separation are proved mathematically in `RESULT.md`. Direct finite computations are not an exhaustive proof of the infinite family. The equality of whole face vectors uses the published connected sparse-paving theorem identified in the references; the other combinatorial and Gaussian-angle steps are reproduced in the proof.

No external or independent mathematical audit is claimed. The scientific results are self-reviewed only.
