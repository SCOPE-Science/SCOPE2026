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

The standalone `verify.py` uses only the Python standard library. It stores the two fifteen-edge quotient graphs together with their \(\mathbb F_2\) sheet-change labels, enumerates all \(32768\) edge subsets for each, tests locality by solving the vertex-potential equations, and expands the Boyle--Spyropoulos state sum exactly with integer arithmetic.

Expected replay output:

`VERIFY_OK k6_subgraphs=32768 k6_local=7204 p_subgraphs=32768 p_local=25564 psi_k6_11=1296 psi_p_11=2000 duality=PASS max_y=(5,3)`

The checks include equality with the complete coefficient dictionaries, \(\psi_H(1,1)=1296\), \(\psi_{H^\ast}(1,1)=2000\), and
\[
T_H(x,y)=\psi_H(x,y)+(y-1)\psi_{H^\ast}(y,x).
\]
The ordinary Tutte polynomial on the left is separately enumerated, so the duality test is not a comparison against a copied coefficient list.

The finite verification proves only the stated two graph computations. It does not establish any classification of embeddings or any literature-novelty claim by computation.
