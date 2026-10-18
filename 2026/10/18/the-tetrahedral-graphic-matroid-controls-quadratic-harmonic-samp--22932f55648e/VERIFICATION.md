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
The analytic proof in RESULT.md starts from a full-rank nine-column real harmonic polynomial evaluation matrix, checks a three-dimensional left-kernel certificate, and relates each deleted node to a signed edge-difference vector in a tetrahedron. Standard graph-incidence rank gives the exact stated formula, independently of numerical tests.

The companion standard-library Python program `verify_cuboctahedral_erasure.py` is complete and standalone. Run `python3 verify_cuboctahedral_erasure.py` in the same directory. Its initial checks establish the 12-by-9 evaluation matrix rank, the 12-by-3 left-kernel rank, and all 27 zero scalar products. It then examines each of 4096 node-deletion masks by exact Fraction Gaussian elimination and compares directly against connected-component counts. Finally it checks the entire thirteen-row rank histogram. Its observed output was PASS for all checks; no floating point is used.

The computation is a **complete finite verification** for this fixed twelve-node object but is not a general theorem for arbitrary spherical node sets. No expert or independent audit is claimed.
