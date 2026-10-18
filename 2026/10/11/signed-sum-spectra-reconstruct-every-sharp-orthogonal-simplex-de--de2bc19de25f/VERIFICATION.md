---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Assume exact Jiang–Lim–Parvatikar equality classification (orthogonal r-vector orthonormal remainder plus m=n-d centered regular simplices of positive even dimensions k_i). For each k-simplex block, pair inner products -1/k imply squared signed-sum norm ((k+1)^2-s^2)/k and maximal k+2; with |s|=2t+1 the defect is 4t(t+1)/k of multiplicity 2 binom(k+1,k/2-t). Orthogonal blocks yield exact convolution and 2^r multiplicity factor. Largest block K has uniquely least positive defect 8/K, first-positive-to-zero multiplicity q K/(K+4) where q largest blocks: this exactly recovers K,q. Positive finite Laplace transforms permit exact division/cancellation and induction over remaining blocks; total mass 2^n and largest squared norm 2n-d recover n,d and r. Independently checked direct exact sign enumerations for simplex sizes 2 through 14 and the first positive defect ratios. Edge m=0 has only constant spectrum and n=d, so is recovered directly. Finite check supports but does not prove infinite theorem; the analytic inverse argument does.

## originality

PASS

Earlier Jiang–Lim–Parvatikar theorem is credited for equality structure and each block signed norm; Pinasco handles one simplex. Neither available statement supplies the convolution law as a complete invariant or inversion via least defect, zero/first multiplicity and iterative Laplace cancellation. Target addresses a genuine new structural inverse question on all sharp configurations, with exact complete classification. Best-of-knowledge PASS with consequential inaccessible original full text caveat.

## value

PASS

Inside a natural sharp equality class with several genuinely distinct orthogonal simplex partitions having the same signed-sum maximum, the full signed-sum spectrum is an exact complete observable and reconstructible invariant. Recovery from just the two top levels and successive cancellations is a nontrivial structural rigidity phenomenon and could be used by researchers to identify equality types from norm measurements; no downstream general theorem is needed to justify this precise mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
