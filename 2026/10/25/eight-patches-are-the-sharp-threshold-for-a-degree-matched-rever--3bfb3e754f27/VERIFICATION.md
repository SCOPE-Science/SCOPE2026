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
# Reproducing the finite classification

Run `python3 verify.py > reproduced.json` and compare the resulting UTF-8 bytes with `certificate.json` (for example, `cmp reproduced.json certificate.json`). Python 3 standard-library modules suffice; no external datasets or hidden package files are needed.

The checker enumerates every unlabeled tree with at most eight vertices by leaf extensions and a canonical isomorphism code, enumerates all surviving-vertex sets to obtain the exact no-isolate generating polynomial, and independently recomputes it by a root-state dynamic program. It logs every pair of equal-degree nonisomorphic trees, each polynomial coefficient difference, and its exact sign classification. The witness edge sets are independently checked against the unique mixed-sign class.

The checker does not prove anything about trees above eight vertices and its finite counts are not evidence for such a theorem. Algebraically, \(t=p/(1-p)\) maps the entire interval \(0<p<1\) bijectively onto positive \(t\), coefficientwise single-sign differences cannot vanish there, and \(t^5(1-t^2)\) changes sign exactly at \(t=1\). Conditioning on a nonempty surviving set divides the difference by a strictly positive denominator. The displayed expectation formula is independently obtained by indicator linearity.

No independent external scientific audit has been conducted.
