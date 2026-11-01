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
# Reproduction and limits

Run `python3 verify_orbit_homology.py` using Python 3.10 or later; no third-party modules are required. The script exhaustively constructs every flag of nonempty faces in the inclusive cycle-power clique complex at sizes \(3k=6,9,12\), identifies orbits under vertex rotations, and computes exact finite-field matrix ranks of the barycentric quotient boundaries. Because barycentric chains have no inversions, those boundary matrices represent the true geometric orbit space. The expected outputs for \(k=2,3,4\) and primes two and three appear in `verification_output.txt`.

The infinite-family theorem follows from the paper's direct combinatorial argument: maximal cliques are cyclic arcs and one orbit of equilateral triangles; the cyclic-arc part admits a rotation-equivariant collapse to the rim; the triangle orbit is a disk whose attaching map winds \(k\) times. The test cases are evidence but not an exhaustive proof for arbitrary \(k\). The source texts inspected for overlap were the relevant complete sections of arXiv:1104.0433 and arXiv:1503.03669 and the accessible arXiv rendition of arXiv:1911.00732; no independent validation was performed.
