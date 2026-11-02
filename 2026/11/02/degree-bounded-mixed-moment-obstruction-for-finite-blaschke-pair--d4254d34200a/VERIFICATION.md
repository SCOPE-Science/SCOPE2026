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
# Verification of the finite-degree mixed-moment theorem

The proof is self-contained except for the standard defining properties of a polynomial resultant and the elementary Gershgorin diagonal-dominance theorem. For the first, the resultant of degree-\(d\) and degree-\(e\) polynomials is homogeneous of degree \(e\) and degree \(d\) in their respective coefficient vectors. The two rational functions can share a value pair only on a one-dimensional algebraic locus, so the resultant is not the zero polynomial. Substitution yields an exact linear relation among \((e+1)(d+1)\) distinct-index Hardy vectors (the vectors need not be distinct as functions).

The second ingredient requires explicitly checking the row degree in the rectangular index poset: for \(0\le j\le e\), \(0\le k\le d\), exactly \(j(d-k)+(e-j)k\) opposing indices can have nonzero correlations. Its maximum is \(de\), establishing strict diagonal dominance whenever every prescribed moment is less than \(1/(de)\). The Gram matrix must be singular by the resultant relation, proving the bound. For \(d=e=1\), the bound is attained. For coprime positive degrees, monomials have no nonzero cross-moment before \((m,n)=(e,d)\).

The optional `CHECK.py` executes finite combinatorial and monomial consistency tests using only the standard Python library. These tests do not establish the general result independently, and no external or independent mathematical audit has been performed.
