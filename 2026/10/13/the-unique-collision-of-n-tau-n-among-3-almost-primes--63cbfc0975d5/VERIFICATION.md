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
# Verification

The proof is symbolic and exhaustive. For \(\Omega(n)\le3\), the possible divisor counts are exactly \(1,2,3,4,6,8\). Ordering a nontrivial collision by \(m<n\) forces one of the ten strict divisor-count pairs recorded in `case_table.json`; `RESULT.md` eliminates nine and shows that \((6,4)\) yields only \((18,27)\).

`verify.py` independently enumerates every input through \(10^6\) with \(\Omega\le3\). Its replay output is `VERIFY_OK limit=1000000 low_omega_inputs=539387 nontrivial_fibers={108: [18, 27]}`.

The finite cutoff is not used to infer the theorem; completeness comes from the symbolic case split.
