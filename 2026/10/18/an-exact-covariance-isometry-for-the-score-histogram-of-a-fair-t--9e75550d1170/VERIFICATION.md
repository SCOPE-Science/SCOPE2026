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

The analytical proof establishes the covariance-isometry identity for every integer \(n\ge2\) using only independent fair game orientations, a shared-edge conditioning identity and binomial size bias. Exact orthogonal projection supplies the complete finite-dimensional spectrum and the Krawtchouk diagonalization.

Run `python verify.py` beside this file with standard Python 3. The implementation exhausts all labeled tournaments for orders \(2\) through \(6\), compares every entry against the rational closed formula, and checks polynomial projection, score constraints, Pearson expectation and normalized higher Krawtchouk modes through order \(8\). The performed run reported `PASS: 871 exact identities; 33866 exhaustively enumerated tournament orientations (n=2..6); symbolic score algebra n=2..8`.

The finite enumeration does not certify the infinite family independently. There is no assertion that the Pearson statistic has a chi-square distribution, no large-sample limit theorem, and no independent audit.
