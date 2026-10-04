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

The proof was checked at the level of definitions, quantifiers, and boundary cases.

* Domain: odd integers \(m\ge3\), binary \(\mathrm{RM}_2(1,m)\), all stored coordinates.
* Generator normalization: coordinate \(x\) uses column \((1,x)^T\); affine transitivity makes the target irrelevant.
* Recovery-size check: every minimized nontrivial recovery set has odd size at least three.
* Triple correspondence: a recovery triple is exactly a translate of the three nonzero vectors of a two-dimensional subspace.
* Existence: the Năstase--Sissokho partial-spread theorem at \(q=2,t=2,r=1\) gives \((2^m-5)/3\) pairwise disjoint triples.
* Upper bound: one additional nontrivial set would force all sets to be triples and leave exactly one nonzero vector uncovered; XOR of plane triples and of all nonzero vectors gives a contradiction.
* All-symbol conversion: the target singleton contributes exactly one additional disjoint recovery set.

`verify_rm_asp.py` performs independent finite sanity checks at \(m=3\) and \(m=5\), including explicit maximum-size partial two-spread witnesses and every target coordinate, and checks the general formula arithmetic for further odd dimensions.

Unproved limits: no classification of maximum families is claimed; no claim is made for all-symbol batch recovery, higher-order Reed–Muller codes, or nonbinary fields. The finite script is corroborative and does not replace the cited infinite partial-spread existence theorem.
