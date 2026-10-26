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

# Verification of optimum Italian-function counts

The supplied standalone `verify.py` uses only the Python standard library. Execute it with `python3 verify.py` from a directory containing the extracted file. The expected successful final line is `VERIFY_OK`; a captured run is included as `verify_output.txt`.

The script directly tests \(f:V(S_n)\to\{0,1,2\}\) against the sum-of-neighbor-labels condition, not against the proof's charged-pair description, for the complete finite spaces at \(n=3,4,5,6\). It separately enumerates all finite simple base graphs on \(2\), \(3\), and \(4\) vertices and computes their corona optimum counts directly. The formula is checked against subset enumeration for every cycle order \(3\le n\le14\).

No finite experiment certifies an unbounded claim. The unrestricted correctness argument is the explicit bijection, the lower bound from corona-pair charges, and the exhaustive three-residue cyclic gap classification in `RESULT.md`. Numeric minima of coronas were established in earlier literature and are not asserted as an original contribution.

No independent audit has been performed.
