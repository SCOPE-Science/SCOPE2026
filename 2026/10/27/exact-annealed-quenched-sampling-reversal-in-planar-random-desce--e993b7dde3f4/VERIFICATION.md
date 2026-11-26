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

Whitening by the Gram square root makes exact least-squares line search an orthogonal projection onto the perpendicular sketch line. Hence energy after the first step multiplies by squared cosines of consecutive angles. Integrating the elliptical Gaussian radially gives the Poisson density on the doubled angle with parameter q; the doubled angle difference has parameter q² by Fourier multiplication. Integrating log(|1+exp(i·)|²/4) against this density gives 2 log((1+q²)/2) by the Poisson formula (the logarithmic singularity is integrable); the log products obey the stationary ergodic strong law. For the mean, the cosine-squared kernel acts on 1 and cos(2φ) with entries 1/2, q/2, q/2, (1+q²)/4 and on sin(2φ) by (1−q²)/4. Its larger block eigenvalue is the displayed G_mean. The principal function can be chosen as 1+β cos(2φ) with 0<β<1, since the irreducible block's larger eigenvalue is strictly below its maximum row sum (1+q)/2; positivity bounds all iterates of the constant function by multiples of that eigenfunction times the exponential rate. Every nonzero start has positive first-step mean energy. For signs the Gram entries give the stated absolute line overlap r; the map from line labels to the first label and the successive switch bits is a bijection, so the independent fair switches give the exact binomial moment and almost-sure factor. Orthogonal lines terminate almost surely upon switching, whereas a start parallel to one nonorthogonal sign line has a positive first-step zero event. The comparisons reduce to the endpoint sign identities in Proof: at u=0 and u=1 the mean rankings are opposite for every 0<q<1, while at u=1 the typical-path equality has the stated strictly increasing quintic factor (with equality at q_* only on that endpoint). Independent bisection gave q_*=0.13160844685660672 and spectral ratio 1.6980918606931625; the rational witness checks by substitution. Replay: frozen RESULT.md Proof and verify.py lines 11–78, read but not executed. The conclusions are asymptotic rates of squared residual, for nonzero starts and the stated sign exceptions, not one-step bounds or rates for inconsistent/higher-dimensional models.

## originality

PASS

The supported distinct claim is the exact sector-dependent Gaussian-versus-sign comparison of the two asymptotic notions, including an all-angle typical-path advantage below a sharp conditioning threshold together with a strict opposite expected ranking in a nonempty sector. The Gaussian expected factor is indexed elsewhere and the rank-one exponent principle is already known; neither is credited as new in isolation.

## value

PASS

Choosing sketch directions is a genuine algorithmic decision; typical squaring rates and rates of expected squared residual answer different questions. The exact two-dimensional phase boundaries delimit when those criteria prescribe different distributions, including the robust small-anisotropy regime and a fully exact positive witness. This is a motivated comparison, independent of novelty of the inherited update and not an assertion about wall-clock efficiency or higher dimensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
