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

`punctured_verify.py` constructs \(\operatorname{PG}(2,2)\), \(\operatorname{AG}(2,3)\), a cyclic order-thirteen Steiner triple system, and the binary projective order-fifteen system. Its checks include exact pair coverage, the full extension table, stabilization of equality-and-block three-variable logical refinement, and the four-variable free-witness threshold. All passed in the supplied output, with the final empty-position colors grouping the four complete structures together and the four punctures together, separately.

`deletion_extension_verify.py` is a second standalone implementation that deletes every point in the four parents, constructs each leave without using any refinement code, and exhaustively checks the predicted case-by-case extension counts. It passed for \(44\) punctures, \(5{,}640\) ordered anchor pairs, and \(69{,}744\) third-vertex choices. The four-variable threshold was verified for every deletion.

To reproduce, extract both scripts and run `python3 punctured_verify.py` and `python3 deletion_extension_verify.py` with Python 3. No third-party modules, external data, random seeds, or network access are required.

The checks cover only the listed finite designs and do not enumerate all Steiner triple systems of any order. The general all-depth assertion rests on the proved permanent three-pebble extension invariant; the sharp four-variable distinction rests on the universal witness count \(v-6\). Self-review has passed; independent audit has not been performed.
