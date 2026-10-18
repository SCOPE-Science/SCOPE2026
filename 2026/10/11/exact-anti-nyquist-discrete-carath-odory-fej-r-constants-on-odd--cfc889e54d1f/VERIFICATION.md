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

For every integer m≥4 and N=2m+1, α=π/N, positivity at j=m,m−1 gives two inequalities with b coefficient signs s sin(α/2) and −s sin(3α/2), s=(−1)^m. Multiplying by positive complementary sine factors eliminates b and bounds a≤cos(α/2)/[cosα cos(3α/2)]. At equality b=s·2sinα/cos(3α/2) is forced. Set j=m−r, x_r=(2r+1)α/2∈(0,π/2], and y=sin x_r. Feasibility values split as q_+(y)=2Ay²+By+1−A (even r) and q_−(y)=2Ay²−By+1−A (odd r). The plus quadratic is increasing for y≥0 and vanishes at first even sample; the minus quadratic has roots of opposite sign and vanishes at first odd sample. Thus ALL sampled inequalities hold; finite tests are not the infinite proof. Independent floating-point tests passed m=4..200 (197 whole grids), two contacts and dual bound. Source RESULT has literal BEL control characters in place of LaTeX \alpha; semantic mathematics is recoverable, but the public text is malformed.

## originality

PASS

The exact anti-Nyquist diagonal m=(N−1)/2 and unique higher-harmonic coefficient are not covered by inspected general positive-definite frameworks or previously published fixed-harmonic formula records. Earlier low-degree results give m=2 or m=3 only; sampling-rigidity implies strict improvement rather than the present exact value. All comparisons are best-of-knowledge because Resultary was unavailable.

## value

PASS

On an odd cyclic grid, the largest nonredundant frequency m=(N−1)/2 is a canonical Nyquist boundary. The new theorem closes the full infinite diagonal with exact sharp value, unique coefficient, two-sample extremal certificate, and explicit N^(−2) sampling gain. This is a natural finite-group harmonic-analysis invariant rather than an arbitrary finite slice or a known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
