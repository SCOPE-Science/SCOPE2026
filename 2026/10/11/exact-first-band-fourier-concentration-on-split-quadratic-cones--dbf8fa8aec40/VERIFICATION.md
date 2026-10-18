---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For Q(x,y)=x·y, the normalized Fourier coefficient of 1_X follows by additive orthogonality: F(0)=1/q+(q-1)/q^(m+1), F(ξ,η)=b if nonzero and ξ·η=0, and -q^(-m-1) otherwise. Therefore on the coordinate-character set E the Gram matrix is a I+b J-c A, with A the m disjoint K_(q-1,q-1) bipartite pair graphs and an isolated zero frequency. Block contrasts (dimension 2m(q-2)), antisymmetric pairs (m), symmetric pair contrasts (m-1), plus the 2x2 block exhaust 1+2m(q-1); their eigenvalues and equality spaces follow. Exact numerical checks across q=3,5,7,9,11 and m=2..10 corroborated strict ordering, but field-wide result rests on exact character sums valid for all odd prime powers. At m=1 equality dimension two and min q^-2 as stated.

## originality

PASS

Iosevich–Koh 2008 studies restriction/extension bounds on nonzero quadratic levels with surface-normalized measures; this result treats the zero split cone, ambient normalization, and exact first-Hamming-band compressed Gram spectrum with multiplicities. Vinh studies quadratic-form graphs, but such broad spectra do not supply a checked statement dominating this restricted sharp concentration problem. Potential association-scheme character tables pose a nontrivial residual priority risk.

## value

PASS

The zero locus of a split bilinear quadratic form is canonical, and first-coordinate Fourier signals form the natural smallest nontrivial Hamming band. An exact all-q,m spectral decomposition, best concentration, min singular value and dimension-boundary perfect-localization classification are meaningful quantitative harmonic-analytic facts rather than a routine test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
