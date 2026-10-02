---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

Lemma 2.7 of the primary source gives the exact kernel w_p(t)=t(2p-t). Translating f by a quadratic forces lambda=(3p-1)/48 because M-m is translation-invariant while both T_p and m+M shift linearly. Centering at (m+M)/2 then reduces the least possible constant to (1/16) integral_0^1 |w_p|, whose three regimes give exactly the displayed C(p). Every continuous profile G(t) in [m,M] is realized by a symmetric continuous second derivative, so continuous approximations to sign(w_p) prove sharpness rather than merely an upper bound. Differentiating the middle cubic gives the unique minimizer p=1/(2sqrt2); the uncentered case forces p=1/3.

## originality

PASS

Simić--Bin-Mohsin Theorem 2.8 already contains algebraically equivalent nonsharp lower/upper inequalities for every p, so the inequality envelope itself is prior-covered. What survives is the proof that those bounds are exact infimum/supremum envelopes for the full C^2 class, the uniqueness of the quadratic centering under curvature-oscillation control, and the global minimax parameter. Those optimality statements are not implied by a mere valid bound and were not stated in the inspected source; the Simpson p=1/3 sharp constant is separately prior-covered and excluded from novelty.

## value

PASS

Determining the exact sharp envelope for the full parameter family, proving the centering is forced, and locating the global minimax rule are natural optimality questions in a classical quadrature family. This is more than a routine numerical check and closes an explicit sharpness gap left by the motivating source.

The dated certificate retains the supplied scientific assessment, sources and limitations.
