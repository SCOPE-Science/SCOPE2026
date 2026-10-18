---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Translate and apply an invertible odd multiplier to A={a,a+p,c} in Z2p to obtain {0,p,1}. The three off-diagonal entries of the complex 3x3 frame operator are exactly Fourier moments for site differences 1,p,p-1. They imply Z_even+Z_odd=0, M_even-M_odd=0, conj(Z_even-Z_odd)=0; hence each parity complex moment zero and parity masses equal. Each parity samples a rotated odd regular p-gon, so no one or two positive roots can sum to zero; at least 3 per parity. Exactly three strictly positive masses solve origin-in-triangle iff each positive cyclic gap <=(p-1)/2; unique normalized solution has opposing-sine weights. Gap-composition inclusion–exclusion yields p(p²−1)/24 triangles for each parity, squared supports across two independent parities. Minimal polynomial Phi_p forces any nonempty equal-1 root vanishing set to be all p per parity, so equal-weight minimum 2p. Independently checked all triples for p=3,5,7,11 with admissible per-parity counts 1,5,14,55 and support counts 1,25,196,3025; these finite checks do not replace analytic all-p derivation.

## originality

PASS

Finite spectral and tiling sets in Malikiosis require unweighted orthogonal bases, not sparse redundant Parseval frames with variable strictly positive weights; Dutkay–Ranasinghe use weighted Fourier frames for self-affine measures but their general matrix isometry relation is not a sharp three-site antipodal cyclic 2p support-count and weight classification. Lam–Leung vanishing sums have integer coefficients, not arbitrary positive real. Resultary a three-consecutive-site Fourier sampling record has different sampling-site geometry and thresholds (3,4,5), not antipodal-pair six. Classical positive quadrature convex geometry supplies the triangle lemma, but comparison found no previously expressed exact parity-split uniqueness and T_p² frequency-support enumeration.

## value

PASS

The distinction between equal-weight spectral bases requiring 2p frequencies and positive weighted tight frames requiring 6 is sharp and grows with prime size. Complete classification of all minimizer supports and unique weights via independent triangles supplies exact design options for sparse finite harmonic sampling; this motivated extremal Fourier-frame problem is not merely a numerical p-table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
