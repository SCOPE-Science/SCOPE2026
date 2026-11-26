---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

In dimensionless time Jt the dissipator is q times the sum of the site-projector Lindblad terms. Trace and positivity are preserved. An independent exact matrix-unit construction, python3 /workspace/checks/02_spectral_certificate.py (SymPy), gave the stated full characteristic polynomial and verified the cubic discriminant, both shifted Hurwitz identities, the q=3 branch test and the cyclic Krylov spaces of the two specified deviations. The cubic discriminant is strictly negative for every q>0, and evaluation at −2q/3 orders its unique real root and the conjugate pair's real part on the two sides of 3. At 3 just real parts coincide. The odd quadratic is defective at 2√2; all other scalar or quadratic spectator real parts equal −q and cannot dominate. Shifting the cubic by the leading odd root real part gives positive A,B,C and AB>C both below the odd exceptional point and above it with b in (0,√2]; hence strict spectral separation without sampling. Zero is simple and all nonzero modes are stable. Cyclicity excites the full leading generalized eigenspace in each active block; spectral projection and finite-dimensional Jordan form give the claimed norm log-slopes even on real-part ties and at the odd exceptional point. Near the stationary state the natural-log entropy deficit is (3/2)Tr(X²)+O(||X||³), doubling the log-slopes. The initial pure deficit is log 3 and the near state has strictly interior spectrum and nonzero deficit for the given ε. Strict separation of the log-slopes yields an eventual ordering for each fixed set of parameters, not a uniform time estimate. Expansion of the simple cubic root near q=0 gives −3q/4+O(q³); substitution r=uR, u=1/q, gives R=−6+O(u²) at large q. With the odd formula these give limits 5/4 and 3. The frozen 387-check count is recorded evidence, not the independent replay.

## originality

PASS

The open-chain generator, entropy diagnostic and parity-related suppression mechanism are precedented. Credit only the exact finite-q three-site rates, their strict all-q comparison and the resulting statement for the explicit pair. The closest verified statements do not give that comparison.

## value

PASS

The open three-site path is the smallest reflection-symmetric open line with a center site and an independent odd diagonal perturbation. The theorem resolves whether the entropy acceleration persists outside the previously motivated strong-dephasing regime in that minimal example. It provides exact rates, two distinct spectral events without gap closing, and finite limiting acceleration factors useful for validating approximations. It does not claim an all-chain theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
