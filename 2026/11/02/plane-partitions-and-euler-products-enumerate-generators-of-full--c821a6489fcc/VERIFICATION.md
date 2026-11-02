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

The independent-audit channel is not yet performed; evidence is null. The two ordinary Python 3 scripts in `artifacts/` reproduce the following separate computational comparisons without third-party packages:

- `python3 artifacts/orbit_formulas.py` computes the formal Euler transforms and enumerates all admissible pairs modulo simultaneous conjugation for \(1\le n\le5\). The exact observed rank-three orbit counts are \(0,0,1,4,15\), in agreement with the derived series; corresponding total no-two-cycle orbit counts are \(1,3,7,17,37\).
- `python3 artifacts/verify_essential.py` independently constructs permissible pairs for \(n=5,6\), identifies all rank-two pairs that are squares of a rank-three parent, and computes full simultaneous-conjugacy orbits. For \(n=5\), there are \(3106\) permissible pairs and \(1260\) essential rank-two pairs, with \(17\) essential rank-two and \(15\) rank-three conjugacy orbits. For \(n=6\), there are \(37783\) permissible pairs and \(12210\) essential rank-two pairs, with \(37\) essential rank-two and \(46\) rank-three orbits. All counts agree with the coefficient formulas.

The test output ends in `VERIFY_OK` in both scripts. This verifies only finite cases; the all-dimension claim depends on the complete red-fiber bijection, square-root equivalence, and the previously proved structural characterization. The literature comparison establishes no absolute publication-priority guarantee.
