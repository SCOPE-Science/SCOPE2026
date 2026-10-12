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

Run `python3 verify.py` with Python 3 and no third-party packages.

The program reconstructs all twenty length-six binary words of Hamming weight three and their one-deletion shadows. It verifies the five-bin transversal certificate directly. On all \(190\) unordered pairs it checks that direct shadow intersection agrees with a separate dynamic-programming longest-common-subsequence test.

It exhaustively examines all \(15504\) five-subsets, finds exactly eight valid maxima, and separately checks every six-subset to confirm none is valid. It then recomputes reverse-complement invariance, the four orbits under reversal and complement, and the deletion-shadow coverage distribution.

Expected first output line:

`VERIFY_OK vertices=20 pair_checks=190 upper_certificate_bins=5 maximum=5 labeled_maxima=8 natural_group=4 orbits=4 orbit_sizes=2x4 reverse_complement_fixed=8 coverage=18x4,20x4 layer_perfect=4 maxima_sha256=6467d017b83742475c63ad33f708c912a1cc96363823f64828a16e97bb9a24ce`

The verifier is complete for this finite domain. It establishes no analogous classification for other lengths, weights, or deletion radii.
