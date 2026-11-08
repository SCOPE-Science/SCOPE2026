---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For each n≥3, translate an anticode S in F2^n to include 0. Each other support has size≤2; its 2-element supports form a pairwise intersecting graph-edge family, which is a star or triangle. This forces S into a radius-one ball, a coordinate square, or an even-parity plane on three coordinates. Maximality follows from distance-three witnesses; different maximal classes intersect in at most three vertices. Thus every face of size≥4 has a unique maximal container, yielding the exact claimed F_n(z) by counting faces of balls plus squares/parity planes at z^4; pairs/triples count separately. Independent brute force enumerated every subset for n=3 and n=4 and reproduced (1,8,24,32,16) and (1,16,80,160,120,16). The closed form F_n(1)=1+2^{2n+1}+2^{n−2}(binom(n,3)−binom(n,2)−6n−4) and asymptotic 2·4^n follow algebraically; the proof, not the finite checks, covers all n≥3.

## originality

PASS

Horlemann–Ravi arXiv:2610.31618 provide a binary diameter-two asymptotic cardinality bound 2^{Θ(n)}, but their inspected Proposition 3.4 does not give the full exact face polynomial; the exact displayed formula there concerns diameter one. Bukh–Saatashvili address maximal fixed-diameter structures more generally, Adamaszek–Adams Rips homotopy types, Briggs–Feng–Wells facets; those checked statements do not determine all face counts. Earlier clique-polynomial or coding-theory computations remain a possible alternative formulation.

## value

PASS

Diameter-two anticodes are standard coding-theoretic objects, and F_n(z) is exactly the f-polynomial of the scale-two Vietoris–Rips complex of the binary cube / clique polynomial of its square graph. The full coefficient distribution, classification of maximal faces and uniqueness of containing maximal faces at size≥4 are natural complete structural invariants useful beyond the known maximum-cardinality result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
