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

The complete parameter-uniform proof is in `RESULT.md`. The standalone `verify.py` uses only standard Python libraries and independently verifies for each \(4\le n\le10\) that the Alexander dual has \(6n\) triangles and \(n\) tetrahedra, no five-vertex simplex, boundary ranks \(5n\) and \(n\) over \(\mathbb F_2\), and first Betti number \(2n(n-4)+1\).

For \(4\le n\le8\), it also enumerates the original ordinary cut complex completely, constructs an exhaustive acyclic discrete-Morse matching, checks every directed Hasse incidence, and verifies that the critical two-level integral attaching row has gcd one. This yields the predicted wedge homotopy type in these five finite cases. The verification is exact for the tested inputs, but only the written proof establishes all integers \(n\ge4\). Run `python3 verify.py` and require the terminal line `VERIFY_OK`.
