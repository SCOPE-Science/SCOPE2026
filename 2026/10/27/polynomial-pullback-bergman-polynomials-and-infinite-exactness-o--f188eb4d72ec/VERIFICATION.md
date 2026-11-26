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

For a regular value w, partial fractions identify the z^{-1} coefficient at infinity of s(z)/(P(z)−w) with the sum of s(ζ)/P′(ζ) over the fiber; the polynomial part contributes nothing. Expanding in w, the term of index j is s(z)/P(z)^{j+1} times w^j. With deg s≤d(m+1)−2, all j≥m are O(z^{-2}); the trace is polynomial of degree <m, identically zero for m=0. The real Jacobian |P′|² leaves precisely this trace when testing against P′ Q_m^E(P)/d. Critical values are a finite null set, and the area formula is valid for Borel targets without boundary hypotheses. It also gives d regular preimages a.e. and the squared norm factor d/d²; boundedness and positive area follow from properness and that same area formula. Positive definiteness proves uniqueness. For the disk the monomial w^{k−1} has squared norm πR^{2k}/k in dx dy, hence the unique monic derivative divided by n=dk is P′P^{k−1}/d. Integration gives exactly P^k+c and the squared derivative minimum πnR^{2k}. The exterior Green function gives cap=R^{1/d}, including disconnected or critical-level lemniscates. The proof includes degree one and m=0 (vacuous testing if the Bergman degree is zero). Inspected but did not run verify.py; an independent check via direct rational simple-fiber sums and reciprocal Taylor coefficients (python3 reproductions/frozen_math_checks.py, pullback) passed 60 finite comparisons, which do not establish the universal result.

## originality

PASS

Pass on the arbitrary-positive-area Borel target transfer with its stated degree and norm, together with its general equality application. Credit prior exact rotationally symmetric lemniscates and the prior capacity inequality. The disk-target corollary is not distinct from the filled-disk specialization of a later mirrored annular-lemniscate result. No inspected evidence covers the full arbitrary-target statement.

## value

PASS

The identity transfers a uniquely determined full Bergman minimization, not just orthogonality in a restricted subspace, across arbitrary positive-area targets. It explains sharpness of a motivated capacity bound on a natural infinite-degree equality class, including disconnected and noncircular examples, with explicit equality conditions for the minimizers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
