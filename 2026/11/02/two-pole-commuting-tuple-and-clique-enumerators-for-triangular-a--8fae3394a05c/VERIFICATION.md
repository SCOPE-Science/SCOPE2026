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

# Verification summary

Run `python verify.py` with Python 3 and its standard library only. The verifier constructs addition and multiplication tables of \(\mathbb Z/p^\ell\mathbb Z\) and \(\mathbb F_p[t]/(t^\ell)\), enumerates commuting tuples using determinants evaluated in those rings, enumerates two-generated isotropic submodules independently, and enumerates unordered size-two and size-three cliques directly. It also checks 360 integer-valued parameter identities. These checks are on actual embedded code, not a prior package or an external certificate.

Expected success lines: `TUPLE_CENSUS_OK 10`; `MAXIMAL_CLIQUES_OK 9`; `FORMULA_IDENTITY_OK 360`; `CLIQUE_F_VECTOR_OK 8`. In the chain-ring case \((q,\ell)=(2,2)\), it checks \(25{,}600\) ordered commuting triples and \(672\) pairs plus \(3{,}584\) triples of distinct commuting vertices.

This finite replay does not independently certify the unlimited ring parameters. The displayed shell proof supplies the general argument. Self-review correctness, originality and value review is reported separately; no independent audit has been performed.
