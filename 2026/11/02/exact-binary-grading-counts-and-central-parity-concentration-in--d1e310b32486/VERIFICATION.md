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

For an ordered Z/2-grading the center and derived line are graded, since brackets of terms of different degree with a fixed homogeneous argument cannot cancel and the derived space is spanned by homogeneous brackets. A central plane of the appropriate dimension through K is counted in Z/K by a Gaussian coefficient; its complements are graphs giving q^{t(c-t)}. For fixed quotient and central decompositions, the two lift maps go from V_i into Z/Z_i, giving exactly the exponent of q in each term. When K is even, V_0 and V_1 are orthogonal and each nondegenerate, so the ordered pair count is the Sp orbit divided by the product stabilizer. When K is odd, both are Lagrangian; choosing dual bases gives an Sp orbit with GL_n stabilizer, whose order quotient is q^{n(n+1)/2} times the product of (q^i+1), also in characteristic two. With k=2b-n the normalized even exponent is t(c-t)-k^2+(c-2t)k = (t+k)(c-t-k). The map (t,k)->(r-t,1-k) sends t+k to c-(t+k), preserves the weight and switches parity. The normalized Sp product ratio tends to 1/C_q along either parity and is uniformly bounded by C_q^{-2}; Gaussian tails justify both limits. The odd normalization carries an extra q^n and product tending to D_q, so expansion of O/(O+E) gives the stated constant and rate at fixed q,r. Direct independent finite-field enumeration by span extension and bracket tests matched all six frozen cases, plus GF(4) at (n,r)=(1,0),(1,1), yielding (17,80),(385,1600). Replay /workspace/review-work/small_checks.py grading; output grading_results.txt. The unrestricted result, including r=0 as a boundary, rests on the proof, not the finite trials.

## originality

PASS

Pass for centrally stabilized labeled gradings (r>=1) and their fixed-(q,r) derived-line parity law. The ordinary Heisenberg boundary in characteristic two is already known quantitatively, not merely qualitatively: Resultary afcaae70dd75 gives the two counts refined by projection rank. This is not credited as a new part of the finding. The inspected sources do not enumerate the additional central and lift choices or the resulting stabilized asymptotic.

## value

PASS

For an infinite class of two-step Lie algebras with a distinguished derived line, the theorem gives exact proportions under the natural uniform measure on literal gradings. The standard quotient orbit counts do not on their own give the parity-independent theta constant or distinguish an n-parity oscillation from a sharp odd-derived concentration law. The stabilized counts and rate are substantive apart from the already covered boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
