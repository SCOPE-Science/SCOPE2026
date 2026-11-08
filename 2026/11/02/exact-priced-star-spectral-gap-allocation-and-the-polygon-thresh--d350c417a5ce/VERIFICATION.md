---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Verified the zero-sum leaf-coordinate transformation Q=I-11^T/(m+1) and equivalence lambda_2>=1 iff diag(w)-Q is PSD. The SDP Gram dual with lengths sqrt(c_i) has minimal vector-sum norm Delta by polygon/triangle inequality. In the dominant regime the weighted Cauchy-Schwarz completion gives an explicit positive-semidefinite primal slack with exact cost C*. In both regimes zero dual gap and S(w)X=0 force every individual rate (X_ii=c_i>0 or rank-one vector with no zero coordinates). Kernel ranks yield multiplicities, including m=2. Independent eigenvalue/price checks on 1,089 root-price lists m=2..6 confirm the normalization. This numeric finite check is not the proof for arbitrary prices.

## originality

PASS

The unrestricted linear-cost graph Laplacian SDP and its maximum-variance Gram interpretation are established by Sun–Boyd–Xiao–Diaconis (2006); these are credited, not rediscovered. The published uniform-price star solution (Göring–Helmberg–Wappler, Example 6) is included as known. Their arbitrary edge-length embedding framework is more general as optimization machinery, but available results do not state or directly imply the explicit heterogeneously priced star polygon threshold and unique rates/multiplicity without a fresh optimization argument. Targeted Resultary comparison found adjacent spectral results rather than exact star rule. Best-of-knowledge PASS with risk from older specialized literature, notably Fiedler 1990 full text.

## value

PASS

A sharp nontrivial polygon-inequality phase boundary says heterogeneous prices sometimes optimally produce identical conductances; beyond it the exact rates and spectral-gap multiplicity change. This is an all-price exact design theorem for a canonical network rather than a substitution or a finite experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
