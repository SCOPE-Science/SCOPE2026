---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Resetting the inner guess gives E_k=I-(I+rP) sum_{j=0}^{k-1}(-P)^j. Symmetry reduces its norm and convergence to the scalar polynomial g_k. At +1 the eigenvalue is 1 for even k (and the tested right-hand side gives a zero correction on every refresh) and −r for odd k. At −1 it is 1−k(1−r). For odd k write delta=1−r. On nonnegative λ one has g=−λ^k+delta·λ(1+λ^k)/(1+λ), so g≥−r using λ^k≤λ and g≤delta; for k≥3 with delta(k+1)≤2 the latter is at most r, while k=1 gives g=−rλ directly. On λ=−t, g=t^k−delta sum_{j=1}^k t^j≤rt^k. Summing the secant bound for t^j on j=0,...,k gives g+r≥(1+t^k)(1−delta(k+1)/2). Dropping the j=0 term instead gives g≥(1−k·delta/2)t^k−k·delta/2, strictly above −1 when k·delta<2. The nonnegative half also lies strictly between −1 and 1, and the −1 spectral endpoint proves necessity and the sharp rate deterioration when present. The predecessor of 1/d is (1−2^(-p))/d for dyadic d, so the midpoint and ties-to-even direction are as stated. The stochastic graph coupling has the +1 eigenvector and the sign vector gives −1 for bipartite instances; r<1 keeps the original operator SPD.

## originality

PASS

Best-of-knowledge pass for the combination of the uniform sharp odd-sweep estimate and parity split under the exact-residual/stored-coupling mismatch, realized by literal binary ties-to-even storage. Truncated Neumann polynomials, graph endpoints, and midpoint rounding alone are standard. The closest inspected schemes do not supply the mismatch with this boundary spectrum and do not state the resulting sharp scalar bound.

## value

PASS

The exact boundary separates three practically distinguishable behaviors of a motivated correction architecture: every even count can stall, a long range of odd counts does not improve the worst-case contraction, and excessive odd counts can destabilize a positive-definite target. Exact binary round-to-nearest witnesses show that the mismatch need not be an arbitrary perturbation. The uniform sharp estimate over the symmetric spectral interval, not just the scalar stagnation, supplies the substantive result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
