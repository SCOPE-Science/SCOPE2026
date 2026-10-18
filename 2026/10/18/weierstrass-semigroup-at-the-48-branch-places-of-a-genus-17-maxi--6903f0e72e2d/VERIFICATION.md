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

# Exact verification procedure

The artifact `verify_semigroup.py` requires Python 3 and no third-party packages. In a folder containing both it and `CERTIFICATE.json`, execute:

`python3 verify_semigroup.py CERTIFICATE.json`

**Recorded result:** `VERIFY_OK`.

The checker recomputes the coefficient matrices directly from the seven character-square polynomials over \(\mathbb F_{11}[\alpha]/(\alpha^2+1)\); checks the decomposition \(ABCD=1-x^{12}\), the ramified/unramified local normalization at \(x=-1\), square-root coefficient identities, and all twelve branch values in \(\mathbb F_{121}\). It checks transitivity of the two published rational transformations on the branch values (their lifts to the curve are proved in the cited originating paper). It then performs elimination on the \(11\times14\) even and \(6\times8\) odd matrices and compares every coefficient and pivot against the certificate. All \(17\) canonical orders, the seventeen gaps, the five minimal semigroup generators, the conductor, and \(\ell(18P)=5\) are checked exactly.

**Proof boundary:** The executable check is finite and conclusive for these coefficient matrices because the proof independently establishes that the character differentials form the *entire* \(17\)-dimensional canonical space. The code does not test arbitrary curves, prove the originating maximality theorem, or replace the theorem establishing the lifts of the displayed base transformations. It does not constitute an independent audit.
