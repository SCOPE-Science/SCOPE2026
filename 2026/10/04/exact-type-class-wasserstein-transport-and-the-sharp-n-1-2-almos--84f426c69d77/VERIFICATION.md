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

For a word with count vector \(k\), each coordinate edit can remove at most one surplus and one deficit, so its minimum Hamming distance to the target type class is exactly \(\frac12\sum_x|k_x-m_x|\). This gives the universal coupling lower bound. Conversely, repair exactly the surplus coordinates into deficits using a coordinate-permutation-equivariant random kernel. Since the product input law is exchangeable and the repaired output lies on the single coordinate-permutation orbit of the type class, the output is uniform; the coupling therefore attains the lower bound. The variance/Cauchy--Schwarz bounds and multinomial CLT with uniform integrability give the finite and asymptotic formulas. Independent full optimal-transport linear programs for several binary/ternary small types reproduced the identity, and the balanced binary formula follows from the standard central binomial absolute-deviation identity. The quantum inequality follows by the cited local preparation-channel contraction, with equality for orthogonal signal states.

## originality

PASS

Originality passes. Girardi--De Palma--Lami prove the same type-class-to-product approximation only with normalized upper bound \(\sqrt{(N-1)\log(n+1)/(2n)}\), and their remark heuristically predicts Hamming displacement of order \(\sqrt n\). The audited equivariant repair coupling identifies the exact optimum, removes the logarithm, and gives the sharp fixed-type asymptotic constant. Constant-composition distribution matching studies different divergences/rate loss, and the quantum Wasserstein source supplies only the metric/data-processing framework.

## value

PASS

The result sharpens a quantitative step in very recent almost-i.i.d. information theory from \(\sqrt{\log n/n}\) to the correct normalized order \(n^{-1/2}\), identifies the exact finite classical transport cost, and provides the sharp fixed-type constant. Orthogonal quantum signals show the improved scale is genuinely optimal. This is a directly motivated strengthening of an active theorem, not a detached exact calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
