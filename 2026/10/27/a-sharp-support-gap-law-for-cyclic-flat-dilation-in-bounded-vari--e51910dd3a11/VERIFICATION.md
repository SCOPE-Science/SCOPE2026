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

The derivative of each dilated coordinate along the two-input segment is the perturbation at a maximizing index almost everywhere; identical affine pieces have the same slope. Cyclic variation of the integral is bounded by the integral of selector variations. For proper consecutive windows the rightmost lifted maximizer is nondecreasing and winds once, so its arcs charge each input edge once. A spike attains one; the whole window is constant and has factor zero. For two taps each adjacent selected pair lies on a three-edge lifted arc, giving factor three. The coarea inequality bounds selector variation by 2 floor(n/2) times input oscillation, and input variation is at least twice that oscillation; this gives two for n=4,5 and one for n=3, also a shifted interval. The given strict comparisons select the indicated Boolean perturbations, with output variation respectively 2,4,4,6 on input variation 2, and stay fixed at small displacement, including at the wrap for n=6 and n>6. The one-input estimate follows from the max/min sorting inequality and a spike has two separated sites for n>=4. An independently written bounded check enumerated realizable strict selector graphs, using acyclicity and exact arc tests at n=3 through 9, and reproduced the sharp two-tap factors; the universal statements rely on the analytic estimates, not this sweep.

## originality

PASS

Flat dilation and related variation bounds are standard, and the width-two consecutive special case is directly covered in the catalogue. The strongest looked-up results do not cover the support-gap comparison or its exact cyclic gapped classification. Equal factors for a three-point median are not equivalent statements for dilation. No priority conclusion rests on catalogue dates.

## value

PASS

The contiguous interval versus the first genuinely separated two-tap support tests whether ordinary variation stability also governs perturbations. The exact small-cycle cutoff, attained amplification three with a one-input factor two, and proof across arbitrary cycle lengths distinguish two natural stability notions. This is a structural boundary example, not a claim about all disconnected windows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
