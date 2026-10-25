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

Run `python3 verify.py` using Python's standard library only. The checker reconstructs hypersimplex integer points directly; calculates the gcd of coordinate differences over every unordered pair; compares it to the closed segment formula; and separately checks that residue classes modulo the dilation factor form the expected cliques with the maximum size \(\binom dk\). It covers 63 parameter triples with \(2\le d\le7\), \(1\le k\le d-1\), \(1\le n\le3\).

For the even-parity binary tetrahedron, the checker independently applies its facet inequalities and counts all diameter pairs for each \(1\le n\le14\), verifying the parity function and direction counts. This does not establish the all-parameter conclusions on its own; the detailed geometric and counting proofs in `RESULT.md` do so. The rational-Ehrhart decomposition is a mathematical argument requiring only basic rational Ehrhart theory, not exhaustive enumeration of all binary polytopes. The formulas have no claimed extension to arbitrary integer vertex coordinates. No independent expert audit has been conducted.
