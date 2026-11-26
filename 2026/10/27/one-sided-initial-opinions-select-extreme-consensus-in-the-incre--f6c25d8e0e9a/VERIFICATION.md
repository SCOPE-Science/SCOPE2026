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

In cut coordinates the probability simplex is convex, and averaging the cut-field Jacobian along a segment between feasible distributions gives a Metzler matrix by the off-diagonal formula. The resulting comparison preserves cumulative order, so reflection gives m≤0. For comparison against a frozen-rate chain at bias v, the nonlinear cut field minus the frozen cut field at the nonlinear law equals (v−m)(p_j+p_(j+1))/(2k), nonnegative when m≤v. In particular the unbiased chain is an upper comparator in stochastic order. Its Neumann cosine modes have eigenvalues −(1−cos(sπ/(2k+1))); the one-sided initial law has strictly positive first coefficient and every nonterminal first-mode prefix sum is positive. The faster remaining modes therefore leave every cut strictly above its uniform cumulative mass after some finite time. In these centered cut coordinates the discrete parabola i(2k+1−i) has centered second difference −1 and sum (2k+1)·2k(k+1)/3, so its small feasible multiple is a strict constant subsolution with first-order cut drift (2k−1)/3>0, also at k=1. Comparison yields a persistent negative mean gap. For fixed r=(k+v)/(k−v), the numerator of the stationary-mean difference has coefficients 2d−2k−1 at r^d for 1≤d≤2k and factors as in (6), strictly negative on (0,1). If the limiting upper mean L exceeded −k, freezing successively at v>L and taking v down to L would give L≤f(L)<L. Mean saturation gives convergence to the endpoint, and reflection gives the other endpoint; δ₀ remains unbiased and converges to uniform. The motivating equation and precise support class match. Bibliographic correction only: the expectation is in the last remark before §4, not in §4 itself. The supplied verifier was inspected, not executed.

## originality

PASS

The originating paper states the exact support-class result as an expectation, not a theorem. Earlier same-model work proves convergence to a trichotomy and gives a sufficient entropy barrier but does not select the limit for all one-sided laws. A later strict stochastic-order criterion overlaps, but one-sided support by itself does not give that initial order. The proof establishes eventual strict order and persistence, and selects the extreme for every k≥1. No inspected earlier statement entails the full conclusion without substantive additional comparison.

## value

PASS

The theorem solves the source's concrete all-k basin question on a natural class that includes means arbitrarily near zero, outside the strict extreme-mean threshold. It controls long-time selection rather than just identifying stationary points or citing unstable linear modes. It makes no finite-agent fixation claim and leaves mixed-sign support open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
