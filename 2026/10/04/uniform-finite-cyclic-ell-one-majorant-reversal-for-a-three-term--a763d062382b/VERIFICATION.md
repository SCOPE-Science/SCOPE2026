---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Both norms depend only on the character order \(L\). For the positive trinomial, \(|1+z+z^2|=|1+2\cos\theta|\); the quartic \(q(x)=15/32+9x^2/16-x^4/32\) majorizes \(|x|\) on \([-1,3]\) by the two exact factorizations in the package. For \(L\ge5\), root-of-unity orthogonality gives mean \(x^2=3\) and mean \(x^4=19\), hence norm at most \(25/16\). For the signed trinomial, multiplication by \(z^{-1}\) gives magnitude \(\sqrt{1+4\sin^2\theta}\); concavity places this above its endpoint chord, and mean \(\sin^2\theta=1/2\) for every \(L\ge3\), giving the lower bound \((1+\sqrt5)/2\). The two bounds are strictly separated. Direct root-of-unity evaluation yields the \(L=3,4\) values. Fresh independent numerical evaluation for every \(3\le L\le1000\) reproduced strict reversal, while the algebraic inequalities provide the all-\(L\) proof.

## originality

PASS

Krenedits proves the corresponding continuous-circle three-term majorant reversal; that integral inequality does not determine every finite root-of-unity average. Bonami--Révész treat \(L^1\) idempotent concentration on finite cyclic groups but not this signed-versus-positive consecutive-trinomial comparison. Resultary also contains an exact formula for the positive three-frequency projection norm and a different finite-cyclic majorant reversal for \(1+z\pm z^3\) at the third moment; neither implies the signed \(p=1\), consecutive-frequency theorem. Direct searches for \(1+z-z^2\) on roots of unity found no prior all-orders comparison.

## value

PASS

The result shows that the smallest classical three-frequency majorant counterexample persists on every nondegenerate finite cyclic quotient, not merely asymptotically, and supplies a modulus-independent analytic gap. This is a natural finite-group strengthening with a clean uniform certificate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
