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

The analytical argument appears in `RESULT.md` and proves the full result for every integer \(p,q\ge2\) and real \(h\in[1,3]\). The separate standard-library Python file `verify.py` enumerates integer height assignments satisfying the actual weighted graph edge constraints. Grouping integer coordinate vectors by their extreme values allows exact counts without floating-point integration.

For integer \(h\), the \(d\)-th forward difference of Ehrhart counts at dilations \(0\) through \(d\) equals \(d!\) times the volume. The difference-constraint matrix is totally unimodular, so these are integral polytopes. For rational \(h=r/s\), first dilate the convex body by \(s\) and divide its computed volume by \(s^d\). A finite experiment cannot certify all real parameters; it is supplementary to the proof.

Executed with `python3 verify.py`: 33 integer-height configurations and six rational-height configurations passed with exact Fraction arithmetic. All rational-height tests used \(h=3/2\) or \(h=5/2\). Selected exact volume checks include \(V_{2,2}(1)=16/3\), \(V_{2,2}(2)=23/3\), \(V_{2,2}(3)=8\), \(V_{3,4}(3/2)=27943/1920\), and \(V_{3,3}(5/2)=1877/160\).

The exact formula's basis-dependent anchored volume normalization and restriction to a single varying cross edge are essential. Independent scientific audit: not performed.
