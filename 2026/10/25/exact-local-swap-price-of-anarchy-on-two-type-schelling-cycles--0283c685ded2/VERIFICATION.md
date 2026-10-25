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

The analytical result applies for every integer \(n\ge3\) and every positive composition \(a+b=n\); finite calculations support but do not certify the infinite quantification.

Run `python3 verify.py` in the same directory as `certificate.json` and compare the resulting standard output byte-for-byte with `certificate.json`. The standalone script imports only Python standard-library modules and prints one JSON line followed by a newline; no external data, package download or network call is required. All generation is deterministic.

The verifier (i) directly checks both individuals' changed payoff on every adjacent swap, and separately tests the four-position alternating-word characterization, across 131,036 nonmonochromatic cyclic binary words with \(3\le n\le16\); (ii) groups local equilibria by composition into 119 classes and confirms the exact maximal run count; (iii) constructs 6,215 explicit extremal configurations for \(3\le n\le112\), independently tests their stability and run count; and (iv) reports selected exact welfare values.

These checks cannot establish all-n optimality or scientific novelty. The proof and complete scopes are given in `RESULT.md`. No independent audit has been performed.
