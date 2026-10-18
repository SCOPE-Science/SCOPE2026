---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS: The algebra has basis 1,x_i,y_ij and J^3=0. Differentiating skew relations kills scalar generator images (c_ij!=1) and square relations kills off-diagonal linear terms (c_ij!=-1). Every derivation then has D(x_i)=a_i x_i+sum b_ij,i y_ij and D(y_pq)=(a_p+a_q)y_pq. D²=D forces a_i in {0,1}, a_p+a_q in {0,1}, (a_i+a_p+a_q-1)b_pq,i=0. Odd characteristic permits at most one a_i=1; characteristic 2 permits all subsets. Admissible b coefficients are removed by shear with denominator (a_i-a_p-a_q)=±1. Algebra automorphism on J/J² must be monomial and parameter-preserving from square and skew relations, yielding exact subset orbits. Rank= r plus number of mixed eigen-one y terms; independently summing allowed b parameters reproduces odd and even characteristic rank polynomials for q=4,5,7 and n=2..5. These normal-form computations are not a substitute for the structural derivation.

## originality

PASS

PASS (best of knowledge): Quantum complete-intersection and Hochschild-derivation literature supplies the algebraic setting and generic derivation context, but inspected primary sources do not classify composition-idempotent derivations modulo quadratic shears and parameter-preserving automorphisms or give their full finite-field rank enumerators. Could overlap specialized weight-one gradings or 2-step nilpotent algebra literature under other terminology.

## value

PASS

PASS: The rank spectrum of idempotent derivations and exact conjugacy-support orbit classification are natural structural invariants of a broad parameter-generic radical-cube-zero algebra family. The sharp characteristic-two versus odd dichotomy and parameter-independence of labeled counts give meaning beyond routine diagonal-matrix classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
