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
The verifier `verify_wagner_matching.py` reconstructs the Wagner graph from its defining cycle and antipodal chords. It enumerates every face of the ordinary matching complex, reconstructs every cover in the face-poset Hasse diagram, replays the stated sequential element matching, and verifies acyclicity by a full directed-graph topological sort.

The verified counts are \(105\) nonempty faces, \(244\) Hasse covers, \(49\) matched pairs, and critical-cell vector consisting of one cell in dimension \(0\) and six cells in dimension \(2\). This is sufficient for the claimed wedge homotopy type.

As a separate check, the script constructs the simplicial boundary matrices over \(\mathbb F_2\). Their ranks are \(11\), \(31\), and \(7\) in dimensions \(1\), \(2\), and \(3\), yielding reduced Betti rank \(6\) only in degree \(2\).

The computation proves only the finite graph \(M_8\). It does not establish an all-Möbius-ladder formula. The saved output is `verification_output.json` and has status `VERIFY_OK`.
