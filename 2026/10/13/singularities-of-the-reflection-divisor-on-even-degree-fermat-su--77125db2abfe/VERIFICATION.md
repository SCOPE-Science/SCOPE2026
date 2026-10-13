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

# Verification of the reflection-divisor singularity basket

Execute `python3 check_reflection_divisor.py` with SymPy available. Its expected terminal marker is `REFLECTION_DIVISOR_VERIFY_OK`.

The script constructs all \(28\) quartic mirrors exactly over \(\mathbb Q(i)\), enumerates \(378\) distinct pairs of planes, groups their intersection lines by Pluecker coordinates, and obtains \(6\) six-plane flats, \(64\) three-plane flats, and \(96\) two-plane flats. It computes the restriction of the quartic to each pair-intersection line as a binary quartic and checks squarefreeness, including infinity, by the polynomial gcd. The checker also verifies as polynomial identities the general \(d\)-parameter pair-incidence, point-count, local delta-invariant and arithmetic-genus equations.

**Proof boundary.** The calculation for degree four is exact but does not establish the infinite even-degree statement. The latter depends on the exhaustive four-case support classification of reflection-plane pairs and the rank-three-flat avoidance lemma in `RESULT.md`, neither of which is inferred from a finite test. The scope is over \(\mathbb C\), even \(d\ge4\). No independent audit is recorded.
