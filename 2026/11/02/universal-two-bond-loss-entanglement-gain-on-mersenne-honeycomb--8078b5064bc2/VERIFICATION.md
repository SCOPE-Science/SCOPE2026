---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Graph-state entropy equals GF(2) cross adjacency rank. Over F2[x,y]/(x^L−1,y^L−1), M is multiplication by 1+x+y and Q=coker M has dimension L−1 by roots α∈F_{2^k}\{0,1}. Two different monomials in Q cannot agree: α↦1+α forces u=v mod L; α↦1/α then forces L|3u; a polynomial of degree 2L/3<L−1 excludes the remaining nonzero case for L≥7. This is also true for transposed M. Distinct deleted row/column unit vectors are independent in the two cokernels, forcing ker(M+UVᵀ)=ker M∩ker Vᵀ and exact rank increase r≤2. Full independent GF2 rank enumeration of all 10,437 legal pairs at L=7 agrees, without extrapolating to all k.

## originality

PASS

Qualified PASS: Hein–Eisert–Briegel cut rank and Rule-60 Mersenne kernel ranks are existing inputs. The pairwise monomial-cokernel rigidity and universal placement-independent two deleted CZ bonds are additional to the inspected source statements, including the complete Mersenne Rule60 configuration study.

## value

PASS

A controlled-Z gate omission is a natural circuit fault. Its maximal two-bit increase for every disjoint placement is a nontrivial collective statement stronger than generic rank-one perturbation bounds; L=3 and three-fault obstructions sharply delineate scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
