---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The unique maximum independent set consists of h and all attached leaves and has size d. Classifying size d−1 sets with/without h gives c_{d−1}−c_1=I(H[A];1)−1−a=sum_{j>=2}i_j(H[A]); its nonnegative vanishing is exactly the clique condition. If A is a clique, decomposing independent core subsets U in B and optionally one allowable A vertex proves I(W;x)=(1+x)^d I(H-h;x/(1+x)^2) as a polynomial identity. All gamma coefficients are i_j(H-h)>=0. For every negative real root tau of I(H-h;t), tau(1+x)^2=x has two distinct negative roots, and the converse follows by preimages of roots; real-rootedness iff. Independent literal enumeration of all small rooted H for 244 cases, checking the top coefficients and symmetry, agreed.

## originality

PASS

Hibi–Kara–Vien (2026) Proposition 3.1 is a fully general leaf-profile polynomial formula that includes this one-hole graph, and its symmetry Theorem 3.2 assumes every core vertex gets at least one leaf, so it does not state or directly classify this boundary. Stevanović’s condition supplies the positive/sufficient direction, and generalized two-whisker gamma identities are prior; this claim adds a *necessary and sufficient* simplicial-vertex condition and nonnegative exact obstruction. The novelty is narrow and qualified because the general formula may make the coefficient extraction an approachable corollary.

## value

PASS

Omitting precisely one leafless core vertex is a natural first boundary outside the all-positive-whisker palindrome classification; the exact local clique obstruction and full gamma polynomial identify all graphs with symmetric independence polynomial in this profile, an infinite structural classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
