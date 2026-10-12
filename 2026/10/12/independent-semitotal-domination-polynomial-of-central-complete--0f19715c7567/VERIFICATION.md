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

# Verification record

Run `python3 verify.py` with a standard Python 3 installation. The bundled verifier reconstructs all central graph edges and computes all shortest-path distances from scratch, then independently tests each possible selected subset for independence, domination, and distance-two witnesses.

The recorded execution compared every subset for 36 complete multipartite profiles having central-graph order at most 18, testing a total of 2,272,392 vertex subsets; each full set of results matched the formula. Four additional larger instances had every predicted subset checked against the actual graph. Examples include \(J_{K_{2,2}}(z,1)=8z^3+z^4\) and \(J_{K_{2,2,2}}(z,1)=8z^6+12z^7+6z^9+z^{12}\).

The computation is finite and does not prove the infinite theorem. It does not check inaccessible papers or establish priority. The mathematical proof in `RESULT.md` verifies all parameters and boundaries.
