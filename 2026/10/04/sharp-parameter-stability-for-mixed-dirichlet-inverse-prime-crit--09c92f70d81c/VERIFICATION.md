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

The prime and \(n=1\) evaluations are exact. Squarefree composites split by Möbius sign: odd support removes the parameter and the product difference is strictly larger than two, while even support gives a uniform positive margin surviving all \(t>-2\). If a prime cube divides \(n\), both the inverse divisor term and Möbius term vanish and positivity is immediate. In the cube-free nonsquarefree case \(n=ab^2\), the only delicate odd-\(\mu(a)\) branch reduces to proving \(J_k(a)J_k(b)>\sigma_k(a)\); the Euler-product bound \(\sigma_k(a)/J_k(a)<\zeta(k)^2/\zeta(2k)\le5/2<3\le J_k(b)\) proves this strictly. Fresh exact arithmetic through \(n=2000\), \(2\le k\le5\), and several rational \(t>-2\) reproduced prime-only zeros.

## originality

PASS

Liu explicitly publishes both endpoint criteria \(t=0\) and \(t=1\), and its full proof gives the factorization cases. However, in the crucial cube-free nonsquarefree case that proof uses only divisibility/integrality to exclude one target value; it does not establish the strict sign needed to interpolate an arbitrary real coefficient. The new Euler-product sign lemma is therefore not implied by the published zero classifications. Resultary search found the audited interval itself but no earlier theorem giving a parameter-stability region.

## value

PASS

The result identifies the maximal coefficient-stability region joining two published prime characterizations and locates its exact first obstruction. The required strict sign lemma clarifies which part of the original factorization proof is robust under perturbation, making this more than a cosmetic interpolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
