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

`verify.py` reconstructs the ordinary \(3\)-cut complex of the cube directly from the graph definition. It checks all \(32\) disconnected triples, all faces, the chain identity \(\partial^2=0\), and exact rational boundary ranks \((7,21,35,28)\), giving Betti vector \((1,0,0,1,4)\).

The certificate supplies one integral \(3\)-cycle \(z\) and one integral \(3\)-cocycle \(c\) with \(c(z)=1\). The verifier enumerates the \(48\) affine cube automorphisms and checks that they exhaust the full graph automorphism group by the vertex-and-neighbor upper bound. For every \(g_{\sigma,b}\), it verifies \(c(gz)=\operatorname{sgn}(\sigma)(-1)^{|b|}\).

For degree \(4\), the verifier computes the signed trace on every simplicial chain group and applies the Lefschetz identity. It checks for all \(48\) automorphisms that the resulting trace is \((-1)^{|b|}\) times the number of fixed long body diagonals. These exhaustive finite checks establish the displayed rational characters. No claim is made about integral representation lattices or higher-dimensional hypercubes.
