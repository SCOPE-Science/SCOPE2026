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

The proof was checked directly against the standard \(k\)-forcing rule. The critical invariant is that a vertex in part \(V_i\) sees exactly the white vertices outside \(V_i\). Therefore the first force necessarily clears all outside whites, and every later unresolved white vertex lies in a single independent part. This reduces success to the three inequalities stated in the result.

The standalone `verify.py` script separately constructs complete multipartite graphs, simulates the literal rule to closure, and compares every initial subset with the theorem criterion. It also brute-forces the minimum size and minimum-set count and compares them with the closed formula and inclusion-exclusion expression. The exhaustive range is every ordered positive part-size profile of total order \(2\) through \(9\), every admissible number of parts, and every \(k\) from \(1\) through \(\min\{4,N\}\).

Replay output:

`VERIFY_OK profiles=502 parameter_checks=2003 subset_checks=694928 count_checks=2003 max_order=9 k_max=4`

The finite replay is not an infinite proof. Cases of larger order and \(k>4\) are justified by the symbolic first-force proof, not by enumeration. No claim of independent audit or independent validation is made.
