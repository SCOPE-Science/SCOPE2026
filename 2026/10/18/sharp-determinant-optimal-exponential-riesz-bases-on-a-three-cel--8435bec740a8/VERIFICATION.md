---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Repaired repairs/1/RESULT.md corrects frozen RESULT.md line 11: for a regular phase triple based at tau the exponent-three row is e^(6πi tau) times the exponent-zero row, not literally identical at arbitrary tau. The zero determinant and the optimal theorem do not change. Fiber Parseval with raw squared norm 3 identifies VV* as the analysis Gram matrix; synthesis is invertible precisely for det V!=0. Expanding the generalized Vandermonde after rotating z_0 to 1 gives the polynomial F on the whole cosine square. Y=±1 gives zero; at X=1 the nonzero critical values come from 6Y²+4Y−1=0 and the opposite edge is equivalent. Every positive interior maximum has Y!=0 and X=−(1+2Y²)/(6Y). Substitution reduces F to 4(1−s)(1+8s)^3/(27s) at s=Y²>0; its derivative vanishes only when 24s²−16s+1=0. Both branches give the same two candidate values D_± as the edge. D_+ is attained and positive, so restricting to distinct phases or invertible bases does not lose it. At an interior D_+ maximizer X=4Y³−3Y and Y²=cos²(t_*/2), so u=±3v modulo 2π and the nodes are a rotation or permutation of the symmetric edge triple. At unit z the factor 1+z+z³ cannot vanish: 1 and the other two unit terms would have to be the cube roots of unity, incompatible with z³=1 for primitive z. This excludes orthogonality and tightness. Inspected frozen RESULT.md, VERIFICATION.md, checker.py and checker_output.txt without executing the supplied script; independent numeric evaluation of the four edge/interior critical candidates agrees, but the exact derivative and boundary enumeration establish the maximum. The repair also describes the recorded eigenvalue-product calculation as a reported discrepancy and the fiber test as a pointwise matrix check, not as a rerun or formal proof.

## originality

PASS

The supported distinct claim is the sharp unrestricted three-node unit-circle optimization for modes {0,1,3}, with the full rotation/permutation orbit and determinant-optimal fiber interpretation. The factorization and finite Riesz fiber framework are known. The strongest actual catalogue overlap matches the value and geometry for one regime of a related, later maximin design, but has a narrower phase family and a different objective; it does not establish the unrestricted stationary classification.

## value

PASS

Determinant measures the product of the exact squared analysis singular values for a natural minimal nonconsecutive fiber. The complete exact optimizer has two equal short gaps while the usual equidistributed triple is singular, a useful concrete distinction in sparse Fourier basis design. The global unrestricted identification, not just calculation at a candidate or Hadamard's coarse ceiling, supplies the scientifically meaningful result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
