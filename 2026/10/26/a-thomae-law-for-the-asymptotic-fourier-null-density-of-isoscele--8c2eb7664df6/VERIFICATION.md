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

Horizontal integration gives Eq. (1) in angular frequency, with coefficients sin(u) and -i cos(u). At u=0 the real part can only vanish at v=kπ≠0, where the imaginary part is nonzero. Away from u=jπ/2 both sinc factors must vanish, hence the two integer indices are nonzero and distinct. On exceptional lines cross-multiplication gives Eq. (2); at v=±p the original expression is nonzero by |sinc(2p)|<1. If cos(p)≠0, no positive tangent pole can be a root and tan(v)/v and v tan(v) have strictly positive derivatives, by v>|sin(v)cos(v)|. Every full positive branch gives one root, with only bounded error at the two ends, the origin, the removed points and reflection. If cos(p)=0, the cosine zeros give the same count up to a bounded error. This proves local finiteness and the uniform vertical census, not just a linewise asymptotic. The lattice covolume is π²/(2α); the three removed lines cost O_α(R). Summation of 2sqrt(R²-u²)/π at step π/2 gives 2R²/π with O(R) error by bounded variation. For irrational α the lattice has no exceptional-line points; at α=p/q in lowest terms, lattice overlap is the index-q sublattice ℓ-k≡0 mod q, with the same deletions. This yields precisely the subtraction 2R²/(πq). Other rationals approaching a fixed point without repeating it have denominators tending to infinity; the rational defect is a downward point discontinuity. An independent integer-index count using j²+(2k+αj)²≤(2R/π)², j∈qZ excluding j=0 and k(k+αj)=0, gives overlaps 266 and 1186 at α=1/4 and 210 and 934 at α=2/5, for R=45 and 90 respectively, as in the archived output. The supplied sign-change checker was inspected, not run; its finite counts do not establish the theorem.

## originality

PASS

Known polygon Fourier formulas evaluate the transform, but the strongest inspected sources do not give the complete real zero census and the dimension-two rational overlap term for this trapezoid. Closest indexed arithmetic analogies change the domain, the shape or the frequency set. This is a bounded comparison, not an assertion of global priority.

## value

PASS

The exact census describes extinction of a simple polygon family at fixed area and identifies a discontinuous arithmetic invariant of its slope. It separates two geometrically different populations of zeros and proves the overlap loss and O_α(R) remainder, rather than merely evaluating a standard integral or plotting selected zero sets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
