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

The analytic proof is independent of finite computation once the exact distance formula from arXiv:2603.18268v1 is taken as a cited premise.

The accompanying `verify.py` checks the algebraic parameter conversion \(p_r=2r/(r-2)\), the identities
\[
\frac1{r(2+h)}=\frac{h}{2(2+h)},\qquad
\frac1{r(2-h)}=\frac{h}{2(2-h)},
\]
and representative numerical instances of the recursive dominant-exponential recovery and the cusp slope. These checks guard against normalization and sign errors; they do not certify the universal limiting statements by enumeration.

The proof limit is explicit: exact local profile data determine only the multiset \(\{d_i\}\). No stability under measurement error and no recovery of summand isometry classes is claimed.
