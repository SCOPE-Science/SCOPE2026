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

The embedded `verify.py` reconstructs \(K_{1,0}\), checks that its order complex has 48 one-simplices and 32 two-simplices, verifies explicit cycles \(t,x\), an integer two-chain \(S\) with \(\partial S=2t\), a mod-two cocycle detecting \(t\), an integral cocycle detecting the primitive free class \(x\), and the boundary ranks
\[
\operatorname{rank}_{\mathbb Q}d_1=15,\qquad
\operatorname{rank}_{\mathbb Q}d_2=32,\qquad
\operatorname{rank}_{\mathbb F_2}d_2=31.
\]

It then exhaustively enumerates all order-preserving self-maps, computes the induced triples \((k,\delta,\varepsilon)\), checks the exact ten multiplicities, and independently compares bijectivity with integral-\(H_1\) isomorphism.

Run `python3 verify.py`. The expected summary is:
`VERIFY_OK`
`continuous_self_maps=7678760`
`induced_H1_endomorphisms=10`
`bijective_self_maps=16`
`H1_isomorphism_maps=16`
`free_multipliers=-1,0,1`
`opposite_model_same_result=true`

The literature comparison is not machine-certified. The model classification was checked against arXiv:1512.06088v1 and the unrestricted classical self-map normal forms against DOI 10.1155/FPTA/2006/75848. Search cannot prove absolute novelty.
