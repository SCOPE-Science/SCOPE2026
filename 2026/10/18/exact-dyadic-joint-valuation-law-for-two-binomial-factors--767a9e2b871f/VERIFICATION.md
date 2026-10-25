---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For all L>=0 uniform n in [0,2^L), Kummer gives X=v2(binomial(2n,n))=s2(n), Y=v2(binomial(3n,n)) equal to binary carries when adding n and 2n. State (previous bit b_{j-1},incoming carry c_j), initialize (0,0), read L bits with weight u^{b_j}v^{c_{j+1}}, include one terminal zero-padded carry via f=(1,1,1,v). Thus P_L=e M^L f and sum z^L P_L=e(I−zM)^−1 f. Independently built symbolic 4x4 matrix, recomputed exact N and D via determinant/Cramer; both equal pinned polynomials. Differentiating formally at u=v=1 and partial-fraction coefficient extraction yields means E X=L/2, E Y=L/2−2/3+(3+(−1)^L)/(6*2^L) and mixed covariance 5L/12−4/9+(9+7(−1)^L)/(36*2^L). Independent direct integer valuations for all n<2^L, L=0..9, agree. The matrix proof, not bounded brute force, handles all L.

## originality

PASS

Kummer's theorem, Barat–Grabner binomial/digit-block transfer techniques, Spiegelhofer–Wallner valuation statistics within one Pascal row and Wan–Zudilin's occurrence of binomial(2n,n)binomial(3n,n) as an Apéry-like hypergeometric sequence are prior. General methods and a known univariate marginal Y do not determine the bivariate coupling or exact all-L mixed covariance. Prior general transfer matrices could be specialized to this example, leaving an explicit specialization-priority risk; no inspected theorem provides this exact joint enumerator.

## value

PASS

An exact joint law and covariance for two naturally paired binomial factors, which form a classical Apéry-like hypergeometric product, gives more than either marginal can provide. The all-length rational enumerator is a reusable finite-state object for joint divisibility statistics; the asymptotic covariance coefficient 5/12 quantifies a nontrivial dependence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
