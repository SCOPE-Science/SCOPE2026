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

# Reproducibility and verification

Execute `python3 verify.py` using Python 3.9 or later with no third-party dependencies. The companion `verification_output.txt` is the actual recorded output of the standalone script.

The script computes the formula for \(Q_{r,s}\) and \(P_{r,s}\), then checks both counts by direct enumeration of labelled vertex-bit strings under independently coded synchronous strict-neighbour majority with tie retention. A separate enumerator instead traverses each population vector \((t_1,\ldots,t_r)\) and weights it by \(\prod_i\binom{s}{t_i}\). All three agree for 20 pairs \((r,s)\) with \(r\ge2,s\ge1,rs\le16\), comprising 167,116 individually traversed labelled configurations. The bit-level loop also tests the identity \(\(F^5(x)=F^3(x)\)\) for every visited configuration. A separate population example for \(r=s=5\) verifies first entry at time three. The final printed marker is `VERIFY_OK`.

This finite computation is an independent implementation check within the same research package, not an exhaustive verification of all \(r,s\). The universal formulas, period classification, and sharp global bound depend on the explicit proof in RESULT.md. The asymptotics rely on Stirling's formula and a one-dimensional Laplace estimate and are not numerically certified by the script. No external or independent audit has occurred.
