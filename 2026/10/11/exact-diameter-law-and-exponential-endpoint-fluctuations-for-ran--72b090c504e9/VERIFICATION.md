---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

All generic section vertices are precisely crossed signed edges of the ℓ1 unit ball; central symmetry makes diameter twice the maximum Euclidean vertex norm. Pairwise norms are sqrt(a²+b²)/(a+b), maximized by the most unequal normal-coordinate moduli since f′(q)=(q−1)/((1+q)²sqrt(1+q²))≤0. Haar normal Gaussianization and conditioning on the maximum half-normal coordinate give the full finite-n CDF for n≥2. The minimum has n m_n⇒Exp(sqrt(2/pi)), the maximum satisfies M_n/sqrt(2log n)→1 in probability, giving n sqrt(log n)(2−D_n)⇒Exp(1/sqrt(pi)). For all fixed k, on M_n≥sqrt(log n) the scaled deficit is ≤2n m_n, whose moments are uniformly bounded by concavity of H near zero and Gaussian tails; the complement has superpolynomially small probability, so uniform integrability establishes k!pi^(k/2), mean and variance. n=2 is included; the CDF endpoints r=0,1 and support [sqrt(2),2] are correct. Finite independent brute-force checks cannot prove n→∞, which is analytically established.

## originality

PASS

The arbitrary-dimensional Euclidean Haar section diameter CDF and the n sqrt(log n) exponential deficit limit, including every fixed positive integral moment, are not implied by the inspected prior mathematical statements. A separately published regular-octahedron theorem already gives precisely the dimension-three case and the same extremal-normal-coordinate mechanism; no novelty is claimed for n=3. The closest 2026 random diameter manuscript was materially inspected in full rather than judged from its abstract. Its universal/random-ellipsoid estimates do not include this entire fixed-codimension-one distributional classification. Priority remains best-of-knowledge.

## value

PASS

For the canonical ℓ1 cross-polytope, Euclidean diameter of a Haar central hyperplane section is a natural geometric-probability invariant closely tied by polarity to cube projection inradii. The theorem gives the entire finite-n law for the natural unbounded dimension family and an exact non-Gaussian endpoint scaling, rate and convergence of all fixed moments, information not determined by available concentration bounds or the n=3 spherical table. The min/max Gaussian coordinate reduction is a reusable structural mechanism; future researchers comparing random section inequalities can use its exact calibration of distributional tails. There is no claim of arbitrary codimension, arbitrary bodies, or a novel n=3 CDF.

The dated certificate retains the supplied scientific assessment, sources and limitations.
