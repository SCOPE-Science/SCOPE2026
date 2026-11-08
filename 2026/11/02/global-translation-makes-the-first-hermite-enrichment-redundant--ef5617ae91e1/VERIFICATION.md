---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

PASS. Gaussian translation integrals give c0(b)>0, c1(b)=∫(t-b)e^{-(t-b)^2/4}dν/√2, c2(b)=∫(t-b)^2e^{-(t-b)^2/4}dν/(2√2)≥0. Dominated convergence for finite positive ν yields smoothness and coefficient decay as |b|→∞ so maximal projected energies exist. Derivative identities c0'=c1/√2 and c1'=c2-c0/√2 imply Q0'=√2 c0 c1, Q1'=2c1 c2. Any maximizer of Q1 has c1=0: if c2=0 positivity forces single delta at b and therefore c1=0. Thus max Q1<=max Q0 while Q1>=Q0 pointwise, and both argmax sets coincide via Q0 stationarity. For non-atomic/non-singleton ν, c2>0 at optimal b makes Q2 strictly larger. Symmetric doublet stationary b=a tanh(ab/2) yields unique 0 center up to a²<=2, then ± nonzero centers; signed φ1 violates positivity hypothesis. Independent quadrature/derivative and center checks match these equations; arbitrary-measure assertions rely on analytic positivity/compactness, not discrete tests.

## originality

PASS

PASS with qualifications. Chou–Shao–Xia (2022), Xia–Shao–Chou (2020) study moving/rescaled Hermite basis spectral methods, not the exact globally optimized one-versus-two-mode identity for arbitrary positive Gaussian location mixtures. General Gaussian kernel mean-shift/stationarity already supplies b=a tanh(ab/2), which is explicitly not assigned independent originality. Resultary semantic query found no claim-level equivalent or stronger all-positive-measure projection result. Conceivably coherent-state and variation-diminishing approximation theory imply the identity; that implicit-coverage risk is recorded.

## value

PASS

PASS. The initially counterintuitive fact that an extra orthogonal basis function never helps after optimal global translation, while the next enrichment always helps for a genuine positive mixture, is a useful exact structural distinction for adaptive Hermite approximation. Sharp width/positivity boundaries and two-component bifurcation motivate the invariant beyond a routine coefficient calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
