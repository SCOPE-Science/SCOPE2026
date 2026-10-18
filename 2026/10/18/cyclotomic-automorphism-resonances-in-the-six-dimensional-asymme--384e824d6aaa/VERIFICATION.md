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

# Verification of the six-dimensional automorphism normal form

The script `verify.py` implements the six-monomial multiplication rule from first principles. It enumerates **all** normalized candidate pairs with \(a=g=1\) in the tested finite fields and checks \(X^2=0\), \(Y^3=0\), and \(YX=\lambda XY\) by direct multiplication; every \(29\)th valid candidate additionally has the induced six-by-six linear map checked for invertibility.

Reproduction: `python3 verify.py`. No third-party Python package is required. Successful execution prints `VERIFY_OK` after the completed case list. The tests cover \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), \(\mathbb F_5\), with commutative, primitive-cube-root, primitive-fourth-root, and generic conditions; the executable also includes a primitive cube root over \(\mathbb F_7\).

The exhaustive part is only exhaustive for the explicitly listed finite fields and normalized coefficient spaces; no computational assertion for all fields is made. The unrestricted arbitrary-field theorem follows from the displayed defining-relation coefficient identities and the finite radical-filtration surjectivity argument, not from these experiments.
