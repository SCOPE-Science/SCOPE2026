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

PASS. Δ=4κ−α²>0 makes p(v)=1−αv+κv² strictly positive. K(v)=∫0^v u/p(u)du is coercive with unique minimum and gives a proper first integral H=x²/2+K(v), hence precisely one closed orbit through (A,0) for A>0. Original physical period is T=2∫_{v−}^{v+}dv/[p(v)√(A²−2K(v))]. Writing F(t)=1/v+(t)−1/v−(t) yields A·T=2∫_0^{A²/2}F(t)/√(1−2t/A²)dt; F=O(t^−1/2) near zero, exponentially decaying at infinity. Dominated moment expansion and exponentially small endpoint give two terms with O(A^−5) absolute period remainder; angular integration yields I0=2π/√Δ and C=I1/I0 as claimed, strictly positive via κC=log2−(1/2)log(1+z²)+z arctan z. K(v) logarithmic constants give v+/|v−|→exp(−πα/√Δ). Local analytic angular expansion agrees with known coefficient; sign plus T→0 yields finite interior maximum, while α=0 monotonicity follows from decreasing w/v(w). Verified derivations in inspected checker, not its exit line alone.

## originality

PASS

Global-center classification is prior; Rousseau–Toni already computed the reduced Kukles local period coefficient; Christopher–Zhang–Zhang prove broad qualitative non-isochronicity using boundary passage-time orders. None of the inspected same-system results supplies this explicit full-parameter physical-time two-term high-amplitude coefficient together with velocity-extrema ratio. The derived period-maximum implication is not claimed as an independent earlier-local novelty.

## value

PASS

PASS. A complete explicit high-amplitude physical-time period expansion and large-orbit asymmetric speed ratio for a natural whole open family sharpen known qualitative global-center results. The interpolation with a known local coefficient yields a motivated interior-maximum existence boundary, without overclaiming uniqueness. These are dynamical observables, not arbitrary parameter slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
