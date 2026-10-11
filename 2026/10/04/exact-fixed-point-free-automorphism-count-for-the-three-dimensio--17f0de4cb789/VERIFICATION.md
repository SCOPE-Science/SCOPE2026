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

For the three-dimensional Heisenberg Lie algebra, the center and derived algebra are both the one-dimensional span of \(z\). Every automorphism therefore induces \(A\in\mathrm{GL}_2(\mathbb F_q)\) on the quotient, has two independent central shifts, and sends \(z\) to \(\det(A)z\). Thus there are \(q^2\) automorphisms above each quotient matrix and \(|\mathrm{Aut}|=q^3(q-1)^2(q+1)\). The matrix of \(\varphi-I\) is block triangular, so fixed-point-freeness is exactly \(\det(A-I)\ne0\) and \(\det A\ne1\). For fixed \(\delta\in\mathbb F_q^\times\setminus\{1\}\), the determinant fiber has \(q(q^2-1)\) matrices. Those with eigenvalue one have characteristic polynomial \((t-1)(t-\delta)\) with distinct roots and hence form the conjugacy class of \(\mathrm{diag}(1,\delta)\), whose centralizer has order \((q-1)^2\); the excluded class therefore has size \(q(q+1)\). This leaves \(q(q+1)(q-2)\) admissible matrices per determinant and \(q(q+1)(q-2)^2\) quotient matrices in total; multiplying by the shifts gives \(q^3(q+1)(q-2)^2\). The assigned verifier exhaustively reproduces the quotient count over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7\); those finite checks corroborate rather than replace the all-prime-power conjugacy argument.

## originality

PASS

Burde and Dekimpe's full current primary paper studies existence and possible orders of fixed-point-free automorphisms over characteristic-zero Lie algebras; its low-dimensional Heisenberg discussion supplies explicit complex examples but no finite-field enumeration. Liu and Tang study automorphism groups of Heisenberg Lie algebras and thus provide the natural structural background, but no exact finite-field fixed-point-free count was located. Resultary's exact semantic query returns the assigned Heisenberg formula as the same-object record and a separate general theorem for finite abelian groups; the latter counts a different algebraic category and does not imply the determinant-twisted Heisenberg condition. The formula therefore survives best-of-knowledge originality.

## value

PASS

The three-dimensional Heisenberg algebra is the canonical smallest nonabelian nilpotent Lie algebra, and fixed-point-free automorphisms are a standard structural property. An exact finite-field count, including the sharp \(q=2\) exception and asymptotic proportion, is a natural algebraic invariant. The determinant-fiber argument makes the result reusable rather than a table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
