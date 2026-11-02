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
# Verification of the cut-cone distortion theorem

The complete all-parameter argument is in `RESULT.md`; its key independent steps are the four intersection-cardinality cases of the cut inequality, quadratic integer minimization, and the explicit nonnegative cut mixture. The metric under study has part sizes \(3\) and \(n\ge3\), with cross-distance \(1\) and same-part distance \(2\).

Run `python3 verify_k3n.py` from the same directory. It uses only Python's standard library. At preparation it returned:

`CHECK_OK 184728 exact rational assertions for n=3..300; direct cut enumeration n=3..9`

Checks include all cut profiles for every parameter from \(3\) through \(300\), the precise integer minimizer, the mod-three formula, both primal cut-orbit distances, exact complementary slackness, and independent direct enumeration of the constructed cut coordinates for the smaller parameters. Arithmetic is performed with exact rational fractions.

These finite checks are not an exhaustive infinite proof. The proof establishes the conclusion for every integer \(n\ge3\); no special numerical inference, external certificate, or formal proof assistant is required. No independent audit has been carried out.
