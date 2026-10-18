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

# Reproducibility of the planar quantile-Kaczmarz identity

Run `python3 verify.py` with Python 3 and no nonstandard packages. The program produces the exact recorded line in `verification_output.txt` upon success. The code builds the stated unit projective-angle frame, chooses rows under the inclusive numerical order-statistic cutoff, applies the orthogonal row projection, and compares explicit predicted factors against direct conditional expectations.

The recorded execution performed 39,420 checks. Coverage includes the tight-frame Gram identity for \(2\le m\le23\), all integer cutoff ranks \(1\le r\le m\) in that range, the sharp first-step orientation, every post-projection grid-perpendicular orientation, and exact transition-energy enumeration over four iterations. It also checks many non-extremal starting orientations and asymptotic sine-limit relations at larger \(m\).

These are deterministic floating-point checks with explicit tolerances and are only supplementary evidence. They cannot prove the asserted infinitely many frame sizes or all iteration counts. The proof in `RESULT.md` supplies the exact finite sine identity, the inclusive tie argument, the invariant grid orientation, the iteration conditioning identity and the convergence argument; these are the steps needed to independently reconstruct the theorem. Floating-point tie handling is not an exact arithmetic certificate. No independent audit has been performed.
