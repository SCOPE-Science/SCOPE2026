---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For Fourier vectors with entries exp(2πikj/n), the forward shift has eigenvalue exp(−2πik/n), so the signs in the stated H give eigenvalue E_k=2cos(2π(k+α)/n). The normalized finite-window probability is the double sum with kernel G(−T(E_k−E_l)); l=k contributes 1/n and the only extra zero-flux degeneracies are distinct l=−k. Their signed gap is −4 sin(2πk/n) sin(2πα/n), giving the displayed argument. All other gaps stay nonzero for fixed n and contribute O_n(1/T) by |G(z)|≤2/|z|. Since |G′|≤1/2, the replacement error of the resonant arguments is O_n(|αT−τ|+Tα³); the last term is O_K(T⁻²) on the stated window. Reality, positivity and normalization follow by the probability-vector limit. Fourier uniqueness separates nonzero frequencies 2k for odd n, requiring z_k∈2πZ minus zero; for even n the frequency collides with k+n/2 and the kernel sum is 2 sin(z_k)/z_k, requiring z_k∈πZ minus zero. For odd n≥5 and even n≥8 the ratio of the k=2 and k=1 arguments would be the rational algebraic integer 2cos(2π/n). This is in (0,2), equals 1 only for n=6, and hence is impossible there. Direct substitution for n=3,4,6 yields the three stated time lattices. At τ=0 the starting-vertex deviation counts a nonempty set of modes; as τ→∞ every retained argument diverges in magnitude. At fixed generic flux, distinctness of E_k follows from k+l+2α not being a multiple of n, leaving only the diagonal in the infinite-time limit. All estimates are for fixed n; exact flattening is asserted for the limiting profile only. The supplied script was inspected, not executed.

## originality

PASS

The distinct result is the zero-total-flux, all-vertex weak-flux limit together with its complete finite-parameter flattening classification. The Fourier spectral formula, inverse-detuning scale and kernel-suppression mechanism are prior (especially the indexed half-flux result); the inspected statements do not settle the zero-flux coefficient coincidences or the n=3,4,6 classification.

## value

PASS

At fixed size the limiting distribution resolves the two incompatible orders of limits quantitatively. The classification answers a finer natural question than the known inverse-detuning scale: whether the entire time-averaged profile can equal uniformity already at finite scaled observation time. The odd/even frequency coincidences change the exact kernel zeros, and the algebraic gap-ratio obstruction explains why only the three specified sizes can realize them.

The dated certificate retains the supplied scientific assessment, sources and limitations.
