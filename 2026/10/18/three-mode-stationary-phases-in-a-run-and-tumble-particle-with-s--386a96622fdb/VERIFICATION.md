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

For an integrable stationary state, bounded speeds make the constant total flux integrable and hence zero. The two state fluxes then equal a single positive J with J'/J = gamma_-/v_- - gamma_+/v_+. This integrand is odd with a strictly negative limit at +infinity; the bounded inverse-speed prefactor is even, so the normalized positive density exists, is even, and has exponential tails. Differentiating the prefactor gives the k*t*(1-t^2) term. Applying tanh(2s)=2 tanh(s)/(1+tanh(s)^2) twice gives the fourfold identity, so on x>0 the logarithmic derivative has exactly the sign of Q(t^2). Q''=-2(5k+m)-6ky<0 and Q(1)=-8m-2n<0. Thus a positive interior hump following Q(0)<0 gives precisely two simple positive-side critical points, a minimum then a maximum; a zero hump produces no sign change. Q(0)>0 or Q(0)=0<Q'(0) gives one positive-side maximum and a central minimum; in all other cases the center is a strict maximum (including Q(0)=Q'(0)=0). At the witness, the three signs are exact and the central curvature ratio is -3/2. For independent changes of g and u, nondegeneracy preserves the two positive critical points and the central curvature. To exclude new points, use a uniform negative derivative sign near zero, uniform negativity in the far tail from k*(1-t^2)<m, and a compact sign gap away from the two simple roots. Independent bisection reproduces x_-=0.070608603683463302 and x_+=0.197881464185248041 (python3 /workspace/review-evidence/check_tree_and_particle.py). The supplied VERIFY.py and verification notes were inspected as recorded checks, not executed; the reproduction is not the trichotomy proof.

## originality

PASS

The distinct accepted claim is the complete strict-maxima classification for every admissible choice on g=4u, including degenerate boundaries, with an explicit robust exact-three witness. Neither the general stationary law nor existence of multiple peaks by itself is credited as new. The closest prior paper supplies the extremum equation but assumes a two-maxima bound for its unimodal/bimodal criterion; related indexed results overlap in existence but do not classify this slice. This is a bounded best-of-knowledge comparison, not a priority certification.

## value

PASS

The solvable fourfold slice gives an exact global diagnostic for the actual model, including transitions that origin curvature misses. The robust witness demonstrates that a central peak can coexist with two outer peaks, invalidating the unrestricted two-maxima assumption without relying on a singular speed limit. The trichotomy is not asserted off the slice, and the open witness is an exact result rather than a numerical plot.

The dated certificate retains the supplied scientific assessment, sources and limitations.
