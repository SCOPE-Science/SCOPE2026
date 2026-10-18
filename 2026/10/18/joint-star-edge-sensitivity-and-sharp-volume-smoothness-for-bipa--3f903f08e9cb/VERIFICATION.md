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

Run `python3 verify_volume.py` using Python 3 without third-party packages. The checker constructs the Lipschitz difference constraints directly for every test configuration and counts integer points in the dilates of the rational defining polytope. It obtains the volume as the highest Ehrhart coefficient from degree-\(d\) exact finite differences. This uses the standard fact that difference-constraint matrices are totally unimodular, after clearing the denominator of the exceptional length. The checker does **not** implement the beta integral, range distribution, or section-polynomial proof.

Eight configurations were executed and passed, including exceptional lengths \(1\), \(3/2\), \(2\), \(3\), both endpoint cases, and graphs with two or three exceptional edges. In particular, \((p,q,k,h)=(2,3,2,3/2)\) has independently recovered anchored volume \(395/32\), and \((3,4,3,3)\) has volume \(128/5\).

The mathematical proof in `RESULT.md` is required to justify every real \(h\) and unbounded graph sizes; finite lattice experiments are merely independently organized consistency checks. The proof includes the degenerate regular-class case \(p=2\), boundary \(h=1\), and redundant-edge boundary \(h=3\). All results are for ordinary coordinate volume with anchor at an unaffected first-class vertex. No independent scientific audit has been performed.
