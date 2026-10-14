---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

Re-read the actual primary source six-compartment SDE (2.2) and Section 6.1 Milstein formula. The published model has b_I=φE−(μ+γ+φ1)I whereas the printed Milstein drift is b_I−βSI/N; their difference is exactly −βSI/N, nonzero when β,S,I>0,N>0. Independently reconstructed all six drift terms and simplified their sums: stated model gives Λ−μN−φ1 I, printed update gives the same minus βSI/N, proving a spurious total-population sink. Setting all stochastic coefficients to zero exhibits a deterministic Euler O(Δt) inconsistency, not a stochastic Milstein correction; a rational witness β=1/20,S=I=1,N=2 gives −1/40. The source later prints a correct ANN Euler infected drift without the extra incidence sink. The claim concerns print, not unknown program code.

## originality

PASS

This is a specific new diagnosis of contradictory equations inside the same 2026 primary article. The SDE, the erroneous Milstein line and the later correct Euler line are publicly present, but no explicit printed corrigendum or statement of their exact drift inconsistency was located. Identifying its O(Δt) character and population-balance effect is beyond restating the line.

## value

PASS

This exposes a structural, first-order discretization defect in a published six-compartment stochastic epidemic model, not merely a cosmetic typographical issue. An artificial susceptible-to-exposed incidence loss in the infected equation violates the model population-balance identity, so the printed numerical scheme approximates a different drift even with arbitrarily small steps. The exact term and minimal correction matter for mathematical and numerical reproducibility of this named model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
