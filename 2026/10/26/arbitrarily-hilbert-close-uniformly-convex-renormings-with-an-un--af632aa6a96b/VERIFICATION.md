---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and limits
The proof checks the following infinite-dimensional claims analytically:

1. \(\gamma\) is a continuous seminorm, with \(\gamma(s,x)=\max\{|s+\|x_+\|_2|,|s-\|x_-\|_2|\}\), and \(\gamma(s,x)^2\le2(s^2+\|x\|_2^2)\).
2. Convexity of \(\gamma^2\) and the Hilbert parallelogram law give the exact quadratic modulus bound \(\delta_{N_\beta}(\varepsilon)\ge\varepsilon^2/[8(1+2\beta)]\).
3. The points \((0,2^je_j)\) lie in the affine slice and have norms \(2^j\sqrt{1+\beta}\to\infty\).
4. An unbounded localization sequence has \(g_n=x_n/\|x_n\|_2\rightharpoonup0\). Its explicitly defined support functional satisfies \(\|F_n\|_{N_\beta^*}=1\) and \(F_n(p-y)\to\beta(1-b)/\sqrt{1+\beta}>0\), contradicting localization.
5. The fixed-point implication then applies by the cited Kirk–Ray theorem and the classical bounded-set uniformly convex fixed-point theorem.

No finite numerical tests or computer-assisted proofs are required for the universal statement. The existence of a historical predecessor cannot be excluded by finite source searches. Independent validation has not been conducted.
