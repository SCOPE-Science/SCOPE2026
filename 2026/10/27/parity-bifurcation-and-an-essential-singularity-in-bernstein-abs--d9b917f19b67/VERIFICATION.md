---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Symmetry follows by k↔n−k and the normalized binomial variance at r=2 is p(1−p)/n. On the compact p interval and a compact r interval bounded away from 1, first derivatives are jointly continuous, including at zero deviations and as one-sided derivatives at endpoints. Their uniform convergence to (1−2p)/n gives strict outer derivative signs for any fixed small center neighborhood. For odd n, choose its radius below 1/(2n); the smooth second derivatives are then uniformly near −2/n, so symmetry and strict concavity give uniqueness. For even n take δ=p−1/2 and isolate W(δ)|δ|^r, with W=b_n(1−4δ²)^(n/2). The remainder H_r is even and smooth in a fixed radius less than 1/n. Put A_r=−H_r''(0)/2; subtraction at r=2 gives A_r→A=b_n+1/n. For δ>0 the derivative divided by δ is Q_r=δ^(r−2)B_r−D_r, with B_r=rW+δW'=r b_n+O(δ²), D_r=−H_r'/δ=2A_r+O(δ²), and B_r',D_r'=O(δ) uniformly by evenness and smoothness. For r≥2, A>b_n makes Q_r negative up to a fixed small radius. For r=2−ε, it diverges positively at zero. With L=log(A/b_n)>0 and t=exp(−L/(2ε)), Q_r is strictly negative for t≤δ≤h by δ^(−ε)≤sqrt(A/b_n) and the uniform coefficient gap. For 0<δ≤t, the derivative's negative leading term −ε δ^(−ε−1)B_r dominates errors O(δ^(1−ε)+δ), whose relative size is O(t²/ε). This proves one crossing and two symmetric global maxima below two. At the positive crossing d, division by B_r yields r b_n d^(−ε)=2A_r+O(d²). The log displacement limit follows, and inserting the same identity in H_r(d)−H_r(0)+W(d)d^r gives A_r ε d²/r+O(d⁴). Since d²=o(ε), the claimed prefactor and doubled log rate follow. This includes n=2 and does not take a degree limit.

## originality

PASS

The supported distinct claim is fixed-degree optimizer parity close to the quadratic exponent, with a specific essential-singularity rate and gain prefactor. Integer signed-moment formulas, first absolute moments, or expansions in powers of 1/n do not give this conclusion. The most pertinent 2015 Bernstein absolute-moment paper remains an access risk; the assessment does not classify uninspected full texts as noncovering.

## value

PASS

The global maximizer of a natural Bernstein-kernel moment governs its worst-case size. A parity effect becomes visible only by resolving the exponentially small scale, where ordinary pointwise perturbation of the variance or a fixed numerical grid would miss the change in the optimizing position. Quantifying both the displacement and the gain gives information beyond bounds on the moment or a local failure of maximality at the center.

The dated certificate retains the supplied scientific assessment, sources and limitations.
