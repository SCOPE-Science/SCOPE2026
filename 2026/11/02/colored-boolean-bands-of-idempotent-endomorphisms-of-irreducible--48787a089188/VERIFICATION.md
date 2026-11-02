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

# Reproduction and boundaries

Execute `python3 artifacts/verify.py` in Python 3; it uses only standard-library modules.

For the fields \(\mathbb F_7\), \(\mathbb F_4\) and \(\mathbb F_{16}\), the script constructs finite-field arithmetic and the relevant semidirect products. In the first two examples it enumerates all admissible generator images, checks the group homomorphism relations and isolates idempotents by direct composition. In all three it checks every predicted idempotent product against composition on generators, directly builds all pairwise commuting edges and centralizer degrees, enumerates all inclusion-maximal cliques and verifies their predicted cardinalities and extremal sizes.

Test parameters and observed idempotent counts: \((q,m)=(7,6)\) gives \(23\), \((4,3)\) gives \(6\), and \((16,15)\) gives \(50\). Their graph-edge counts are respectively \(106\), \(9\), and \(385\). The first two full endomorphism counts are \(78\) and \(33\). The larger field case checks the parameterized idempotent set but does not enumerate all group endomorphisms.

Expected final line: `VERIFY_OK`.

The code is an exact finite computation for specific parameter sets, not an independent audit and not a proof for all prime powers. Deductive universal proof is in RESULT.md.
