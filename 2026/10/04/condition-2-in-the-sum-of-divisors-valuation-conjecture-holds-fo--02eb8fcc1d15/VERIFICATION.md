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
The infinite claim is established by the symbolic case analysis in `RESULT.md`; no finite experiment is used as an infinite proof.

The accompanying `verify.py` is a regression check only. It recomputes \(\sigma(q^a)\) exactly for every prime \(q<500\), every \(1\le a\le80\), and \(p=3,5\), and checks
\[
\nu_p(\sigma(q^a))\le\left\lfloor\log_p(q^a)\right\rfloor
\]
whenever \(q>p\).

The critical non-computational ingredients are the source paper's exact prime-power valuation formula and the elementary inequalities displayed in the proof.
