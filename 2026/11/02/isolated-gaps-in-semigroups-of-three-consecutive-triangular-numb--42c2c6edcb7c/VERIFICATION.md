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

Factor the triangular triple as (Ad,Bd,Be) with gcd(A,B)=gcd(d,e)=1 and relations Ab=Ba and dc=eb. Each residue modulo a=Ad has exactly one rectangular Apéry representative yb+zc for 0<=y<A,0<=z<d; reduction modulo d and then A proves uniqueness, while relations prove completeness. Identity a+c=2b+1 yields exact neighboring-residue coordinates. Interior 1<=z<=d-2 contributes only top two y rows, one gap each; z=0 contributes none and z=d-1 contributes B-1 gap levels for each top row. Edge cases n=3,4,6 handled with degenerating A. Count 2[(d-2)+(B-1)] gives stated parities and complete set. Independent Dijkstra-based residue enumeration and direct gap-neighbor tests checked every n from 3 through 33, but infinite correctness rests on the rectangular proof.

## originality

PASS

Robles-Pérez and Rosales explicitly treat the same consecutive triangular generators and their telescopic/free nature, Apéry and Frobenius properties. Those facts underlie but do not evaluate the isolated-gap set because neighbor membership in adjacent residues is additional information. Moreno-Frías–Rosales study perfect semigroups (zero isolated gaps) and Singh–Ram dimension two. The closest Smith paper is inaccessible beyond abstract, so priority risk is stated.

## value

PASS

A complete exact local gap classification for a canonical embedding-dimension-three numerical semigroup is a motivated structural invariant, not a routine re-count of the already known Frobenius number. The parity-dependent sharp linear formulas and explicit full sets identify precisely where gaps have neighboring members, useful for perfect semigroup and Apéry-based classifications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
