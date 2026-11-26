---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

With the stated shadow and zero start, the first residual is (I−A/n)(I−A/m)b, with m the b_i²-weighted spectral mean and n the mean with weights b_i² λ_i(λ_i−m)². Hence an active coordinate has ratio η=1−(1−λ/m)(1−λ/n). Both means lie in [μ,L]. Completing the square in λ and maximizing the ratio of the means gives the upper constant. Concavity in λ reduces the lower bound to the endpoints: at L the ratio is nondecreasing in both means, at μ nonincreasing in both; the lower of the resulting bounds is κ(2−κ). For sharpness scale μ=1. In the lower family the squared residual-mean weights of the two low modes are of order δ² while the positive high-mode weight is o(δ²), so both means tend to 1. In the upper family the high-mode contribution to the second mean is of order ε and the other two are O(ε²), giving m→1, n→κ at an active midpoint. With two distinct active eigenvalues a<c and normalized squared weights p,q, m+n−c=a+pq(c−a)²/(qa+pc)>0. This proves class-wide nonnegativity through κ=2 and actual sign loss for each κ>2. The two-mode positivity is strict on the active coordinates; inactive coordinates remain zero. κ=1 and a single active spectral value terminate at the half-step and do not furnish a nontrivial completed cycle. Independent exact witness replay: 106s=(19,−34,−22), 106As=(19,−68,−88), giving ω=4609/12729 and x_{1,3}=−7955/14842014.

## originality

PASS

The first-cycle polynomial and the bounded-root mechanism for the sufficient κ≤2 guarantee are standard or close to the catalogued CG argument. The supported distinct claim is the joint sharp component envelope for the two BiCGSTAB means, with its necessary frontier and two-distinct-active-mode protection. The closest indexed CG record treats a different polynomial and cannot transfer its extremizers or two-mode behavior to the residual-minimizing BiCGSTAB stabilizer.

## value

PASS

Residual-norm decrease does not certify the sign or relative size of individual solution components. The exact dimension-free interval, the sharp sign boundary, and the minimal number of active spectral values for loss of sign give complementary usable limits in a natural positive diagonal test class. The simultaneous sharpness is more informative than quoting a bound on each weighted mean separately.

The dated certificate retains the supplied scientific assessment, sources and limitations.
