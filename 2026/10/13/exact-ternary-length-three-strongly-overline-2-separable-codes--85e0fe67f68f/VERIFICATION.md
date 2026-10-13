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

Run `python3 verify.py` with a standard Python 3 interpreter.

The verifier constructs all \(27\) ternary length-three words. For every unordered pair, it enumerates every coalition inside that pair's descendant box whose descendant is identical but which omits one endpoint. Inclusion-minimizing all such witnesses gives exactly \(891\) minimal forbidden sets, each of size \(4\). A code is strongly \(\overline{2}\)-separable exactly when it contains none of these sets.

Independent symbol permutations in each coordinate are transitive on the \(27\) words, so any nonempty code can be normalized to contain `000`. The verifier performs a complete include-or-exclude search over the remaining \(26\) words and proves that the largest normalized code has size \(10\). It enumerates exactly \(20\) such normalized maxima.

The verifier expands them by all coordinatewise symbol permutations and obtains exactly \(54\) labeled maxima. It independently checks the identity \(20\cdot27=54\cdot10\), then replays the original strong-separability definition on all \(54\) maxima by enumerating every nonempty coalition and intersecting all coalitions with a prescribed singleton or pair descendant.

Finally it applies the complete standard Hamming-isometry group \((S_3)^3\rtimes S_3\), verifies that the \(54\) maxima form a single orbit, and recomputes the coordinate, Hamming-distance, and descendant-box profiles. The verifier does not claim a formula for any other alphabet size or coalition parameter.

Expected terminal line:

`VERIFY_OK vertices=27 forbidden_minimal=891 forbidden_size=4 search_nodes=160998 maximum=10 normalized_maxima=20 labeled_maxima=54 natural_group=1296 orbits=1 orbit_size=54 stabilizer=24 coordinate_profile=4,3,3x3 hamming_profile=1x3,2x30,3x12 pair_box_profile=2x33,3x12 representative=000,001,012,022,102,110,121,202,211,220 forbidden_sha256=ff82cf6ad78340117b66c796a36321b3ee4d2e6885cc0f513bfcb25cd2623a92 normalized_sha256=fbabe79c8208e6eb434e66a140d6ea25644ebf3e61e5d8f995fbcbafc7e706c0 labeled_sha256=9f5c2de392d26f636c02b9e938b3b637e73f0e7eb4908e67cffeef3753e8f616`
