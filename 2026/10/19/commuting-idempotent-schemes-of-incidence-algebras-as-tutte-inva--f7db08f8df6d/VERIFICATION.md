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

Execute `python3 verify.py` with Python 3.8+. The code constructs each finite incidence algebra by listing all comparable intervals and forming the actual multiplication constants, then enumerates every idempotent and every commuting idempotent pair over \(\mathbb F_2\) and \(\mathbb F_3\). It checks the entire vector of diagonal-label fiber cardinalities, not just total cardinality. It separately checks the Potts subset expansion against exhaustive colorings for \(Q=2,4,8\) and \(q=2,3,5\).

Observed totals (idempotents, commuting ordered pairs): four-point star and alternating path (54, 1372) over \(\mathbb F_2\), (128, 4000) over \(\mathbb F_3\); diamond (114, 4132) and (416, 23872); three-point chain (26, 340) and (56, 976). All tested color fibers and Potts identities agree; final output `VERIFY_OK`.

The exact proof is the polynomial projector conjugator, a denominator-free triangular factorization of the incidence-unipotent group, the graph-edge expansion, and polynomial interpolation. Exhaustive small finite fields do not establish the all-characteristic, arbitrary-poset claims, and no independent external mathematical validation is asserted.
