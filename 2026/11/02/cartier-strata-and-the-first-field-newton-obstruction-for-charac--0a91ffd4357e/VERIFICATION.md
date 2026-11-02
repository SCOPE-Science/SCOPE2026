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
# Reproducibility
Run `python3 verify.py` using Python 3 and its standard library only. The exact script enumerates every coefficient tuple over \(\mathbb F_2\) and \(\mathbb F_4\), including all \(48\) rank-zero models over \(\mathbb F_4\), and computes \(\#C(\mathbb F_{4^j})\) for \(j=1,2,3,4\). Binary polynomial bases of degrees \(2,4,6,8\) are explicit in the source. It determines the genus-four zeta numerators by integer Newton identities and the curve functional equation and reconstructs each \(2\)-adic Newton polygon. The recorded output reports \(8\) and \(192\) smooth coefficient tuples over the two base fields, ranks \(4/4\) and \(48/144\), and \(15/51\) distinct Weil polynomials for the \(\mathbb F_4\) rank strata, ending in `VERIFY_OK`.

The all-perfect-field statement is proved from the Cartier formulas and the coprimality argument, not by code. The field enumeration does not establish geometric novelty, or the Newton polygon for rank-zero curves outside \(\mathbb F_4\). No independent audit has been performed.
