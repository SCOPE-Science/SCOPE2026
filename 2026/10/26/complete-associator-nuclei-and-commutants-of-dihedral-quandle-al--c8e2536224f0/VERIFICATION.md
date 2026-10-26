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

# Verification methodology

The proof reduces the left, middle and right associator identities to four exact cyclic-polynomial equalities, then solves the resulting coefficient equations. The crucial middle/right distinction is whether doubling permutes the even exponents: it does exactly when \(n\equiv2\pmod4\). When \(4\mid n\), coefficient comparison at exponent \(2\) forces the pair sum to vanish. Intersecting with the left nucleus shows why characteristic \(2\) restores two full-nucleus dimensions.

`verify.py` builds basis-product tables from \(e_i e_j=e_{2j-i}\), separately imposes all original associator and commutator identities on generic coefficient vectors, and computes ranks by modular elimination, with no use of the polynomial formulas to construct the constraint matrices. It checks the six predicted dimensions, explicit nucleus bases, the product law, and the odd-order commutant pattern for the displayed finite test range.

Execute `python3 verify.py`. Expected final line: `ALL_NUCLEUS_CHECKS_OK`. Only the directly tested orders and prime fields are certified by this program; no computational exhaustiveness beyond that range and no independent audit are claimed. The arbitrary-field conclusion follows from the written proof.
