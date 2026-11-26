---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Lebesgue initialization makes binary digits iid fair; modulo null endpoints the threshold label compares the length-r window as an integer to k. Shifting the r-bit window and appending a fair bit makes a finite-state Markov chain; c=1/2 simply reads one fair bit at a time (also with an unreduced representation). For the selected constant label a, among prefixes of length L=qr+t each disjoint r-block must be one of s allowed blocks, giving the upper count s^q 2^t. Concatenating independently b^r or (1−b)b^(r−1), followed by a b-tail, gives 2^q strings; a non-b-leading window only starts at one of the special blocks and its numerical value 2^(r−1)−1 or 2^(r−1) lies on the required side. Thus valid for all n≥1. Stationarity and the finite-order definition would make the extension probability of the positive-probability constant histories eventually constant, including order zero. Twice that probability is the eventual count ratio u/v; integrality at every future length forces v^j to divide a fixed positive count for all j, so v=1. The integer ratio 1 is excluded by unbounded growth, and every ratio ≥2 by s^(1/r)<2. This proves all orders are excluded, not just orders below a tested bound. Independent exact midpoint evaluations of the actual doubling map (python /workspace/replay.py 2) checked 260 finite cases; at both quarters the first five counts are 3,5,8,13,21, and unreduced denominators multiply them by the expected power of two. Bounds concern the specified dominant label only. Nondyadic sensors and other invariant input laws are not addressed.

## originality

PASS

The binary coding, finite-state presentation, and general Markov recognition methods are old. The best-supported additional contribution is the evaluated all-dyadic dichotomy, including both sides of one-half, together with explicit uniform persistence bounds and their arithmetic obstruction to finite memory.

## value

PASS

Across a natural nested family of threshold sensors, the result distinguishes the existence of a finite hidden-state realization from finite observable Markov memory. It isolates a single iid exceptional cutoff and gives a constructive quantitative obstruction uniform in the choice of dyadic representation. The use of exact growth bounds rather than finite-order tests for a list of cutoffs makes it a structural result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
