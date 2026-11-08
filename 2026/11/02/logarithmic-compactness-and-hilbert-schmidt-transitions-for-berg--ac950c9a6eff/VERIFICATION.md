---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Read the complete matrix proof. Expanding the kernel gives T_{nk}=m_n(γ) Γ(n−k+s)/(Γ(s)Γ(n−k+1)), k≤n, and Laplace scaling yields m_n≈Γ(s)n^−s(log n)^−γ. Consequently each output row square norm is (1+O(1/log n))/[(2s−1)n(log n)^{2γ}], with locally uniform error near γ=1/2; summation gives Hilbert–Schmidt thresholds and exact divergence coefficients. At γ=0, the matrix is the classical 1/s Cesàro matrix, whose sharp norm is acknowledged prior work; D_γ T_0 gives compactness for γ>0, translated weak-null blocks give noncompactness/unboundedness at γ≤0, logarithmic blocks show essential norm equals norm. Independently recalculated all s=2 γ=0 rows for n<200 with exact fractions and two logarithmically damped integral row asymptotics. No general Schatten-p assertion is made.

## originality

PASS

The primary Blasco–Pennanen paper defines this very operator and provides broad boundedness criteria, creating significant same-object priority risk. Its available abstract and related comparison establish that boundedness itself is prior art; the exact H² Hilbert–Schmidt logarithmic threshold, row trace constants, and pole are not stated there in accessible text. The complete primary article could not be inspected; the qualified best-of-knowledge conclusion does not assert whole-document noncoverage. Generalized Cesàro spectra in the published Resultary set use distinct kernels/spaces.

## value

PASS

The strict separation of compactness γ>0 and Hilbert–Schmidt γ>1/2, plus sharp trace and norm blow-up constants, is a natural phase diagram of a concrete established analytic operator family. It supplies useful operator-ideal information not mechanically implied by knowing boundedness alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
