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

Writing \(L_q=V\oplus Z\) with \(V=\langle x,y\rangle\), \(Z=\langle z,c\rangle\), every subalgebra is classified by its quotient image \(U\le V\), central intersection \(C\le Z\), and a graph map. The three image dimensions contribute \(q+3\), \((q+1)(q^2+q(q+1)+1)\), and \(q^2+1\), totaling \(2q^3+4q^2+3q+5\). Nonpermutability can occur only for distinct quotient lines. Then \([A,B]=\langle z\rangle\) and failure is exactly \(z\notin C+D\). The four allowed central-pair types give weighted total \(q^3(3q+1)\) per ordered pair of distinct lines, and there are \(q(q+1)\) such line pairs, yielding \(q^4(q+1)(3q+1)\). The formulas give 43/336 at \(q=2\) and 104/3240 at \(q=3\), matching the inspected exhaustive verifier's certified targets.

## originality

PASS

The complete Muhie--Otera--Russo primary paper introduces the invariant and computes it for the three-dimensional Heisenberg algebra with one-dimensional center; it does not treat the four-dimensional central stabilization. Published SCOPE work found by Resultary covers the nondegenerate finite Heisenberg family with one-dimensional center, including higher rank, but that family does not contain \(\mathfrak h_3\oplus\mathbb F_q\), whose center is two-dimensional and bracket form is degenerate. No inspected source gives the stabilized lattice count, nonpermutable-pair count, or limiting value \(1/4\).

## value

PASS

A one-dimensional central stabilization is the first degenerate extension of the basic finite Heisenberg algebra. The theorem shows that this minimal stabilization changes the large-field subalgebra commutativity degree from zero to \(1/4\) and gives the complete exact count responsible for that phase change. This is a motivated structural comparison of a standard invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
