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

# Reproducible finite checks
The unnormalized Walsh transform has integer coefficients, and its squared magnitude is the Walsh transform of the pair-difference autocorrelation; Fourier inversion uses the standard \(2^{-d}\) factor. Every claim concerns all indexed frequencies, not unordered spectra.

The analytic reconstruction uses only elementary facts about affine independence in characteristic two, pair differences, line-graph cliques, and the exact five-tuple counting argument. All affine ranks for supports of size at most six are exhausted. No numerical stability, larger cardinalities, or generic weighted vectors are claimed.

From this directory, run `c++ -O2 -std=c++17 checker.cpp -o checker && ./checker`. The expected output is:

```
k=1 translation_classes=1 power_spectrum_fibers=1 ambiguous_fibers=0 classes_in_ambiguous_fibers=0
k=2 translation_classes=31 power_spectrum_fibers=31 ambiguous_fibers=0 classes_in_ambiguous_fibers=0
k=3 translation_classes=155 power_spectrum_fibers=155 ambiguous_fibers=0 classes_in_ambiguous_fibers=0
k=4 translation_classes=1240 power_spectrum_fibers=1240 ambiguous_fibers=0 classes_in_ambiguous_fibers=0
k=5 translation_classes=6293 power_spectrum_fibers=6293 ambiguous_fibers=0 classes_in_ambiguous_fibers=0
k=6 translation_classes=28861 power_spectrum_fibers=28024 ambiguous_fibers=31 classes_in_ambiguous_fibers=868
CHECK_PASS
```

Every search space is finite and enumerated without heuristics or floating-point tolerance. The calculation cross-checks the general theorem but the proof does not assume the enumeration generalizes to higher dimensions.

Scientific limitations: binary indicator supports only; exact noiseless data; at most six elements. Earlier classical construction of six-point difference sets is acknowledged. Independent mathematical audit has not been performed.
