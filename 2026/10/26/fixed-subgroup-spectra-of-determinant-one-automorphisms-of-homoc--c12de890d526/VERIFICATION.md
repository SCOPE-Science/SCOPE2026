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
The standalone checker `verify_sl2_profiles.py` enumerates all matrices of determinant one for \(p=2\) and \(a=1,2,3,4\), for \(p=3\) and \(a=1,2\), and for \(p=5\) and \(a=1\). It verifies the complete Smith-invariant profile against independent counts. Five configurations also directly enumerate all fixed points of each map and independently identify the invariant factors from torsion counts.

Reproduction command: `python3 verify_sl2_profiles.py`. Its actual output appears in `verification_output.txt`.

The tests cover exactly 4302 determinant-one matrices, including 1110 independent fixed-subgroup reconstructions. They do not exhaust all prime powers and do not establish the infinite proof by themselves.
