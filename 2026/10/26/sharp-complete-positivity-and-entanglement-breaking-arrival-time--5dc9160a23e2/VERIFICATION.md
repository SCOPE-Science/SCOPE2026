---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For α>0, |β|<1 write p=e^(−αt), q=e^(−t), c=β(1−q), s=√(1−β²). Reconstructed normalized 4×4 Choi matrix has two 2×2 blocks with determinant difference 4q(1−p)≥0, so CP iff |p−q|≤s(1−q). Partial transpose swaps off-diagonal blocks; PPT=EB for two qubits, and EB iff p+q≤s(1−q). Rα(t)=|p−q|/(1−q) strictly falls from |α−1| to0 by comparison of exponential-weighted interval means; (p+q)/(1−q) strictly falls from infinity to0. This proves unique arrival and strict CP-before-EB. Fixed α≠1, slower decay m=min(α,1) gives tCP,tEB~log(1/s)/m and gap (2/m)s^{|α−1|/m}; critical α=1+u/log(1/s), fixed u≠0 yields log coth(|u|/2). Degenerate β=±1, α=0, α=1 endpoints are explicitly distinguished. Independent 250 Choi/PPT eigenvalue comparisons agreed (5 parameter pairs ×25 times ×2).

## originality

PASS

Full original source Eq.(41), Section 4.3 and Appendices C-D establish generator GKSL/positivity phase diagram, but do not derive finite-time Choi/PPT arrival or the singular gap. Szczygielski–Chruściński full online 2024 text defines eventual EB and studies general examples; qualitative eventual EB is already known. Same-semigroup precise two-threshold and crossover are not implied by that qualitative theorem. Choi/PPT tools are standard.

## value

PASS

Non-GKSL qubit evolution can enter CP at finite elapsed time and become EB strictly later, which are distinct physically meaningful regimes. Exact two-parameter thresholds and a nonuniform pure-state limit determine how the entanglement-preserving time window collapses, beyond merely verifying the Choi determinant at a sample time.

The dated certificate retains the supplied scientific assessment, sources and limitations.
