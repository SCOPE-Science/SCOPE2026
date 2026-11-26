---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Normalized Weyl matrices are an orthonormal basis of the complex Hilbert–Schmidt space; the orbit phases are distinct orthogonal characters of the N²-element phase space, giving eigenvalue N times the sum of the two squared ambiguities (N=q²). For a nonzero displacement (a,b) the first graph has one overlap iff a≠0, since b=2at−a²; the other has one iff b≠0. At zero displacement a nontrivial quadratic phase has squared sum q by expanding the square and summing in the difference variable; a nontrivial linear phase has zero sum. Thus the five distinct eigenvalues are 1,2,q,2q,2q² with the stated multiplicities, which partition all q⁴ Weyl labels. Minimum and maximum are attained, and their square-root ratio is √2 q. The first window's nonzero labels count q²q(q−1)+q(q−1)+1; the second is symmetric. Any ≤q-point support misses a nonzero difference because 1+q(q−1)<q², leaving a whole Weyl shift sector unseen by that window. This is a linear-matrix statement; injectivity on rank-one projectors follows for the pair but the obstruction for a single window is not asserted in that restricted problem. A fresh finite-field enumeration gave {1:1296,2:5184,9:16,18:64,162:1} for q=9; a separate dense lifted normal matrix gave {1:36,2:36,3:4,6:4,18:1} for q=3. Replay script and output: /workspace/branches/2e54cba5-28e8-44df-afe2-7cbc852cdf28/independent_spectrum_check.py and independent_spectrum_output.txt. Frozen verification material was inspected, not executed. The checks corroborate normalization and examples; the proof covers all odd prime powers.

## originality

PASS

Bounded pass for the specific transverse sparse construction and exact sharp spectral profile. The individual parabolas are relative difference sets and the Weyl-to-ambiguity reduction is established; neither receives independent originality credit. No inspected result constructs a pair with complementary displacement and modulation defects in this setting, attaining the lower window count with this five-level spectrum.

## value

PASS

Linear tomography using extremely sparse windows needs both identifiability and stable inversion. This explicit construction attains the minimum possible number of windows under a natural per-window support cap and gives all singular levels, not just full rank. It supplies a precisely conditioned deterministic design over every odd prime power, without making claims about globally best conditioning or pure-state minimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
