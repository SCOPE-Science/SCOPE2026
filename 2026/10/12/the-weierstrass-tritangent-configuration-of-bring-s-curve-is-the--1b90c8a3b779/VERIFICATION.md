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
The embedded `verify.py` uses exact finite combinatorics and exact symbolic arithmetic.

It checks all \(60\) ordered injective triples and all \(60\) tritangent blocks, proves each of the three twenty-block families partitions the point set, and verifies point valency three and block size three. It then checks that two points share a block exactly when their triples differ in one coordinate, giving \(A_{5,3}\). All maximal cliques are enumerated: there are exactly \(60\), all of size three, and they are exactly the tritangent blocks. Thus the block structure is recoverable from the point graph.

The graph automorphism enumeration is exhaustive and returns exactly \(720\) automorphisms. Independently, all \(120\cdot6=720\) maps obtained from symbol permutations \(S_5\) and coordinate-position permutations \(S_3\) are constructed and verified to preserve adjacency, so these exhaust the type-preserving incidence automorphisms.

For \(f(T)=T^3+2T^2+3T+4\), exact symbolic arithmetic verifies irreducibility over \(\mathbb Q\), discriminant \(-200\), and a Galois group of order six with element orders \(1,2,2,2,3,3\), hence \(S_3\).

A fresh execution of the artifact embedded in the finding package returned:

`VERIFY_OK points=60 blocks=60 incidence=60_3 point_graph=A(5,3) maximal_cliques=60 aut_type_preserving=720=S5xS3 cubic_disc=-200 cubic_galois=S3`

The computation does not assess incidences with class-(ii) tritangents, type-swapping dualities of the Levi graph, or projective realizability of the extra \(S_3\); these are outside the claim.
