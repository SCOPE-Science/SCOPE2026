---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

C PASS: Explicit Fourier inversion for the Binomial(h,p) residue distribution modulo three yields d_h=(2/3)r^h max_k |cos(hθ-2πk/3)|. The exact change x=θ−π/3 gives r=1/(2cos x), x in [−π/3,π/3], p=1/2+tan x/(2sqrt3). The phase maximum is bounded below by sqrt3/2, with equality at |hx|=π/6; for |x|≥π/(6h), the denominator 2^h cos(x)^h yields a strict global bound except at ±π/(6h). For 0<|x|<π/(6h), logarithmic derivative h(tan x−tan(hx))<0. Thus precisely two minima for every h>=2. A direct one-step computation establishes [1/3,2/3]; eigenvalue modulus minimizes uniquely at p=1/2; strict ratio and asymptotics use elementary expansion. Independently reconstructed the binomial law and confirmed 9009 grid comparisons across 9 horizons; grid does not prove global optimization.

## originality

PASS

O PASS qualified: finite-horizon TV minimization is mathematically distinct from spectral-gap optimization on cycles or fastest mixing within reversible transition matrices. The exact two-optimizer phase formula and limiting constant sqrt3/2 are absent from the inspected cited spectral results; an unindexed finite-horizon/cyclic convolution optimization is still possible.

## value

PASS

V PASS: The exact all-horizon optimizer distinguishes finite-time distributional error from an asymptotic eigenvalue criterion in the smallest directed nonreversible cycle; the optimal tuning shift and persistent relative advantage are natural algorithmic quantities, not a single arbitrary numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
