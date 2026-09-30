# Independent Audit — 2026/09/18/multiplicity-sharp-chebyshev-sos-desingularization--c45dc5ae3e3c

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `76c71fff932d225eb63b95f6a9b2fbd14c3146b7`
- Disposition: **PASSED**

## Correctness

**PASS** — The exact-floor reduction is correct. For t<0, writing 1-2t=cosh u and y=nu/2 gives t=-sinh^2(y/n) and V_n(t)=-sinh^2 y. Because d-1 is even, the only region where t(1-V_n^(d-1)) can be negative is -1<V_n<0, exactly 0<y<asinh(1); taking the maximum of the resulting deficit is therefore necessary and sufficient. The stationarity equation follows from differentiation, with uniqueness from the opposing monotonic logarithmic-derivative terms. For fixed y in (0,A), 1-sinh(y)^(2(d-1)) increases strictly with odd d, giving the strict multiplicity monotonicity and the source floor as d->infinity. Convexity gives sinh(y/n)<=sinh(y)/n, and maximizing z(1-z^(d-1)) gives beta_d=(d-1)d^(-d/(d-1)); uniform sinh(y/n)~y/n gives the kappa_d limit. Independent numerical maximization for multiple n,d pairs reproduced strict delta<epsilon and zero contact at the maximizing t.

## Originality

**PASS** — Henrion-Safey El Din introduce the Chebyshev generator-recovery construction and use a multiplicity-blind floor sufficient for all odd powers. The audited result solves the one-dimensional floor optimization exactly at each odd multiplicity, identifies the published floor as the d-to-infinity envelope, and propagates the strictly smaller constants through the same degree argument. This does not claim a new convergence exponent or global certificate optimality. Searches of the source and nearby literature found no prior multiplicity-sharp formula of this form, so the precise finite-d refinement is distinct from the source theorem.

## Scientific value

**PASS** — Although the universal O(r^-2) exponent is unchanged, the result exactly quantifies how boundary multiplicity controls the constructive constant in the new univariate proof and can reduce the asymptotic floor substantially (for example, cubic degeneracy uses well under half the worst-multiplicity limiting constant). It also identifies the source's uniform constant as an envelope rather than a fixed-multiplicity optimum, which is useful for problem-specific certificate bounds and for comparing desingularization schemes.

## Sources

- Convergence rate of the moment-SOS hierarchy for univariate polynomial optimization (Didier Henrion; Mohab Safey El Din): https://arxiv.org/abs/2609.20544 — Primary source for the O(r^-2) theorem and Chebyshev approximate-generator construction.
- The Membership Problem for finitely generated quadratic modules in the univariate case (D. Augustin): https://doi.org/10.1016/j.jpaa.2012.02.004 — Structural univariate quadratic-module membership input underlying the source proof.

## Limitations

- Sharpness is only within the submitted Chebyshev ansatz, not among all Positivstellensatz or moment-SOS certificates.
- The relaxation exponent remains O(r^-2); only proof constants are improved.
- The propagated constants still depend on nonoptimized scaling and degree parameters from the source proof.
- The theorem is univariate and does not address the broader multivariate rate problem.

## Independent exact check

```json
{
  "implementation": "fresh grid maximization and transformed-contact evaluation",
  "pairs_checked": [
    [
      2,
      3
    ],
    [
      2,
      5
    ],
    [
      2,
      7
    ],
    [
      5,
      3
    ],
    [
      5,
      5
    ],
    [
      5,
      7
    ],
    [
      10,
      3
    ],
    [
      10,
      5
    ],
    [
      10,
      7
    ]
  ],
  "all_delta_strictly_below_source_floor": true,
  "max_abs_contact_residual": 5.551115123125783e-17,
  "all_ok": true
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence and no repository mutation was performed. Open-access/preprint sources were checked first; no needed source remained inaccessible, so Oxford Download was not required.
