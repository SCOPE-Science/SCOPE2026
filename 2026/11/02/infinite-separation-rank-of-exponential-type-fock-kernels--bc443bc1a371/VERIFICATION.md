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

# Verification of the kernel rank theorem

The main proof is analytical and requires no computational certificate. It separately verifies: (i) Cauchy derivative bounds for all Taylor orders, (ii) the exact Fourier--Borel translation identity via the binomial series, (iii) the connectedness of the exterior of finitely many disjoint disks, (iv) analytic gluing to extend a chosen Borel transform, and (v) the finite evaluation-matrix characterization of functional linear independence. Each holds for arbitrary finite sample size and uniform exponential type, not by testing only a bounded set of examples.

For the operator corollary, Liu--Qin--Huang, arXiv:2610.30209v1 (2026-10-21), Theorem 1.2 and equations (4.2)--(4.3) were inspected: their \(V\) belongs to the joint exponential-type class and is nonzero when every harmonic symbol is nonzero. Their domain contains each coherent state, so all columns in the proof are legitimate. Their theorem is a cited premise; the new infinite-rank deduction is directly proved here. No extra code dependency or outside computational artifact is required.

An independent mathematical audit has not been performed. The result has no independent validation certificate.
