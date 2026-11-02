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

Parity bounds all three evaluation images to the 2^{d−1} Walsh characters with |S|≡d mod2. At degree d+2, sign averaging H against the full Walsh character yields H_top=(∏_i x_i)Σ a_i x_i²; harmonicity enforces 6Σ a_i∏x_i=0, so all evaluations on cube corners vanish in this one direction. Explicit disjoint-coordinate harmonic blocks A4=u⁴−6u²v²+v⁴, B6=(231u⁶−315u⁴R²+105u²R⁴−5R⁶)/16, B7=(429u⁷−693u⁵R²+315u³R⁴−35uR⁶)/16 evaluate to nonzero multiples of 1,1,u at sign corners. The case distinctions m=d−|S| even (m=2, m=4a, m=4a+2), full S, and d=3 produce exact-degree harmonic interpolants for every other compatible Walsh character at degree d+2 and all at d,d+4. Independently checked all block Laplacians and exact Gegenbauer-Walsh eigenvalue ranks for d=3..8 (42 bounded assertions); finite evidence corroborates the explicit all-d construction.

## originality

PASS

Bannai–Okuda–Tagami (2013) and Zhu et al. (2015) develop harmonic-index spherical design and addition-formula methods, not full Walsh-image ranks of exact-degree solid harmonics restricted to all cube vertices. The strongly titled Bellet–Brachet–Croisille (2023) spherical-harmonic interpolation paper concerns equiangular cubed-sphere nodes on S², not the 2^d equal-sign vertices of S^{d−1}; its full body was not available here, so this difference is based on explicit geometry in its abstract, with residual reading risk. Relevant Resultary Hamming-sphere Fourier sampling results fix nonbinary shells and finite-group Fourier bands, distinct restriction operators. No inspected stronger all-degree cube-vertex harmonic-rank theorem implies the three quantified ranks.

## value

PASS

The antipodally compatible data space has dimension 2^{d−1}; precisely identifying one lost full-parity Walsh mode at degree d+2 and its complete recovery at d+4 is a natural nonmonotone interpolation phenomenon in every dimension. Exact-degree harmonic sampling is important for representation theory and spherical interpolation, and the proof supplies reusable constructive interpolants rather than isolated computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
