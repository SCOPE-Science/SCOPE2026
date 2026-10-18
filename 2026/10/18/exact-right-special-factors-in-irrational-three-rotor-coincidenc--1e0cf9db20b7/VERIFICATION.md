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

# Reproducibility and scope

Run `python3 verify.py` beside this document; it has no dependencies outside the Python standard library. The program reports `VERIFY_OK: 7 exact quadratic slopes; independent crossing merger; all right-special factors and complexities through n=80; 24080 checks`.

For seven distinct nonsquare integers \(d\), the arithmetic branch uses \(\lfloor j/(1+\sqrt d)\rfloor=\bigl\lfloor(\lfloor j\sqrt d\rfloor-j)/(d-1)\bigr\rfloor\), evaluated using integer square root. The other branch independently enumerates physical horizontal/vertical crossing order by comparing the integers \(h^2\) and \(dv^2\), without floating point. Their first 3,200 event letters agree for each parameter. A second test enumerates factor extension sets of the one-sided decorated rotor word through length 80 and checks the unique reversed-prefix factor together with word complexity \(n+3\).

These finite checks detect indexing or implementation mistakes but do **not** certify all irrational parameters or unbounded word lengths. Universal validity is supplied by the symbolic-dynamics proof in `RESULT.md`. Neither a separate mathematical audit nor independent verification has been performed.
