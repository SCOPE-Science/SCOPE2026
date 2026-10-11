---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Direct multiplication gives commutation exactly when the determinant of \(\rho(A)=(a-c,b)\) and \(\rho(B)\) vanishes. Each nonzero \(\rho\)-fiber is a clique, so the problem reduces to the largest set of nonzero vectors with pairwise nonzero determinants. Every nonzero vector is a scalar multiple of a unimodular vector after Chinese-remainder decomposition; hence each chosen vector can be assigned a projective line, and two determinant-independent vectors cannot share one. Conversely, unimodular generators of distinct projective points have nonzero determinant, since a basis change sends one to \((1,0)\). Thus the maximum is \(|\mathbb P^1(\mathbb Z/n\mathbb Z)|\), whose standard unimodular-vector count is Dedekind's psi function. The inspected verifier independently checks projective geometry through n=40, the matrix criterion through n=10, and exact branch-and-bound optima through n=6.

## originality

PASS

The 2024 primary source explicitly poses the independence-number problem over \(\mathbb Z/n\mathbb Z\) and proposes \(n\varphi(n)(2n-\varphi(n))\). Its nearby prime-power claim yields the same incompatible value at \(n=4\). The audited determinant/projective-line argument therefore does not restate prior coverage; it corrects a published/proposed composite-modulus formula while agreeing with the source's finite-field boundary. A dedicated Resultary search returned the assigned record as the only direct exact match.

## value

PASS

The result gives a uniform exact solution to a concrete published problem, identifies the governing projective geometry, and corrects a proposed formula that fails already at the smallest nonfield example. It is an all-modulus theorem with a natural invariant, not a small numerical counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
