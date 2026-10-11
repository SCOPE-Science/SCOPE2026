---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The Reid--Tai inequalities give canonicity exactly by \(d=b-a\le r\) and \(a\le r+d\), with terminality obtained by strict inequalities. Imposing Gorenstein divisibility on the two non-terminal boundary branches leaves the equal-weight point and \((c,c+r)\) with \(c\mid2r\). The weighted-simplex floor formula gives the exact displayed factorizations. When \(c\mid r\), writing \(m=r/c\) yields a product of geometric series, so all roots are roots of unity. When \(c\mid2r\) but \(c\nmid r\), put \(c=2p\) and \(t=2r/c=2m-1\); the remaining factor is \(C_t(z)=(1+z)(1+\cdots+z^t)+2z^m\). For a unit root, the submitted trigonometric identity forces \(\operatorname{Re}z\ge0\). If this monic constant-one factor were Kronecker, all of its roots would lie on the unit circle, so their real parts would sum nonnegatively, contradicting Vieta because the root sum is \(-2\). The inspected exact checker reconstructs the floor sum and both branch factorizations for every \(2\le r\le240\), as a regression check rather than the infinite proof.

## originality

PASS

Two published SCOPE records already classify the same Gorenstein boundary and give its exact \(h^*\)-polynomials, so those formulas were treated as prior art rather than novelty. The surviving claim is the unit-circle classification. Braun--Liu's full text makes three-supported Kronecker families an explicit exploratory problem and Question 6.9 asks for further general families; its concrete Section 6.5 families are different. The prior SCOPE unimodality theorem gives exactly the polynomial that must be analyzed on the odd branch but does not determine whether all roots have modulus one. The submitted unit-root/Vieta obstruction supplies that missing implication.

## value

PASS

Kronecker behavior is a central property in the cited weighted-projective-simplex literature, and the theorem gives a clean necessary-and-sufficient divisor criterion on a complete, geometrically natural boundary family. The negative branch is certified by a structural root argument rather than numerical root testing, so the result is a motivated exact classification rather than a table lookup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
