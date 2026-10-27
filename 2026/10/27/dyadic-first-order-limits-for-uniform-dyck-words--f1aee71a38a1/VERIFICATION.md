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
# Verification of the Dyck-word first-order limit theorem

The reproducible checker is `check_dyck_fo.py`, run with Python 3 without third-party dependencies. Output from the current package: `DYCK_FO_EXACT_OK 6917 1083 4704 121`.

The first stage enumerates all \(6917\) Dyck words through semilength nine and checks \(1083\) exact endpoint-cylinder/reflection identities. The second stage checks subset-sum completeness for even prefix lengths \(4,6,8,10,12,14\), examining \(4704\) numerator weights. The last stage compares \(121\) exact reflected bridge ratios at semilength \(5000\) with the independent-boundary limit, using an absolute tolerance of \(0.0008\).

The proof of unbounded-\(n\) convergence relies instead on reflection and Stirling asymptotics, conditional pattern saturation, effective bounded-degree Hanf locality, and the sorted-coin subset-sum argument. Finite enumeration does not establish the infinite theorem; it only checks structural identities and small cases. Independent audit and external validation were not performed.
