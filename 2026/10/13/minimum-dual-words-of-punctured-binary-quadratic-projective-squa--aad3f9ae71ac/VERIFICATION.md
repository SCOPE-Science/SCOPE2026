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

The theorem is proved symbolically for every \(m\ge2\).  The critical reduction is exact: after puncturing zero columns, a column indexed by \(S\subseteq[m+1]\), \(|S|\ge2\), is the binary incidence vector of the edges of the clique on \(S\).  A dependence among selected columns is equivalent to pairwise orthogonality of the associated vertex-membership patterns.

`artifacts/verify.py` is a finite independent replay of the low-size consequences.  It uses only the Python standard library, constructs the generator columns directly from the definition, proves computationally that no dependent triple occurs for \(3\le m+1\le6\), enumerates every dependent four-set, and checks exact equality with the two predicted support families and the count \(\binom{m+2}{4}\).  Successful replay prints `VERIFY_OK`.

The computation is not used as an infinite proof.  No claim is made about dual words of weight above four or about nonbinary or higher-degree analogues.
