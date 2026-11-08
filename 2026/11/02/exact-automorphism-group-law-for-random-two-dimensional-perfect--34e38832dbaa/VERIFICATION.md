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

Invertibility of the structure matrix forces automorphisms to be monomial, solving the diagonal and swapped polynomial equations exhaustively. Matrices with 3 nonzero entries are rigid; all-4-nonzero swapped locus satisfies a³c=bd³ and t²≠1, yielding (q−1)²(q−1−h); diagonal two-support gives s C2; antidiagonal support produces C2 for gcd(3,q−1)=1 and C3 or S3 counts 2s/3,s/3 when gcd=3. This proves exact 1/C2/C3/S3 distribution, probability (q+1−h)/(q(q+1)), h=gcd(2,q−1), and simple conditional probability (q−h)/(q²−q+1) from bc≠0. Independent exhaustive GL2(F_p) checked p=2,3,5,7, including C3,S3 at 7. A finite list is not the all-field proof; support stratification is.

## originality

PASS

Published Wei–Zou two-dimensional isomorphism-class counts and Cabrera Casado classifications use same objects and possible automorphism groups, but the inspected primary tables do not assert the full uniformly labelled stabilizer-group frequency histogram or simple-conditional distribution. Existing Burnside counts are a weighted aggregate, not enough to uniquely recover all field-rational stabilizer frequencies. Stabilizer tables in related literature might encode an equivalent finer census; priority qualified.

## value

PASS

Uniform labelled random perfect evolution algebras naturally ask how often automorphisms survive, not just how many isomorphism classes exist. This exact all-finite-field classification identifies arithmetic cube-root symmetry transitions and rigidity rates, including simple subclass, a useful refined structural invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
