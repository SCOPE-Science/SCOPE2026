# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260914-007`

Disposition: **PASSED**

## Correctness — PASS

Independent symbolic reconstruction gives \(H_t(w)=w(3w^2+2t-3)/(3w^2-1)\), \(H_t'(w)=(9w^4-6tw^2+3-2t)/(3w^2-1)^2\), and \(H_t''(w)=36(t-1)w(w^2+1)/(3w^2-1)^3\). For \(t>1\) their only simultaneous real zero is \((t,w)=(3/2,0)\). The cubic discriminant is \(12(9x^4+(3t^2-36t+27)x^2+(3-2t)^3)\); its sign structure gives two bands below \(3/2\) and one above. At \(t=3/2\), \(H(w)=-3w^3+O(w^5)\) and \(G_\mu(w)=1/(3w)+O(w)\), yielding the density constant \(3^{5/6}/(6\pi)\) times \(|x|^{-1/3}\). Huang's atom formula gives mass \(1-2t/3\) at each original atom for \(1<t<3/2\).

## Originality — PASS

General free-power support and subordination results were inspected, but no located source states the solved three-atom phase diagram, the critical value, or the pole constant. The exact law was not found in an independent table or worked example; obtaining the result requires solving the concrete rational critical equations and discriminant.

## Scientific value — PASS

The law is the simplest symmetric three-atom example with a genuine topology-and-atom transition. The complete classification isolates a natural critical time where atoms disappear and a cubic degeneracy produces a density pole rather than a cubic-root zero. This is a motivated boundary phenomenon rather than an arbitrary finite slice.

## Literature and prior-coverage checks

- **Supports of Measures in a free additive convolution semigroup** — https://arxiv.org/abs/1205.5542. framework, not exact coverage: The paper treats arbitrary measures and gives support/density machinery; it does not state the audited three-atom constants.
- **Density of the free additive convolution of multi-cut measures** — https://arxiv.org/abs/2209.15607. related but not exact coverage: The paper studies local singular behavior for multi-cut measures with endpoint power-law hypotheses.

## Limitations and residual risk

- The square-root edge statements use the standard free-convolution boundary regularity framework after the explicit algebraic critical-point check.
- Originality is best-of-knowledge; Huang supplies a strong general framework.
- The exact calculation is a specialization of a strong general support framework, so an unlocated worked example in the free-probability literature could reduce originality.
