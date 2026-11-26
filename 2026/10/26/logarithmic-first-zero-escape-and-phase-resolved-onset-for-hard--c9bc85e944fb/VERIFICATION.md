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

Subtracting the two Gaussian tails from the full Fourier transform gives the stated real-erf identity. With x=L+v/L the endpoint integral has remainder at most 1/(4L^2) in the bracket and partial-xi derivative O(L^-3), by the integrable v^2 and v^3 exponential bounds. Substituting the boundary coordinate y gives the factor sqrt(pi) exp(-y), amplitude 1/sqrt(2), phase shift pi/4 and the compact-uniform error, also for the y derivative. The Gaussian term dominates the global bound on both tails through y=-2 for large L; a point with cosine one between y=4 and 4+2pi is strictly negative. Thus the first zero is in a bounded y-window. Simultaneous profile and derivative vanishing require y=log(2sqrt(pi)) and theta=-y mod 2pi; the second derivative is 1 there. At that phase, to the left of this point twice the profile is exp(u)-cos(u)-sin(u)>0 for u>0. At every other phase the first profile zero crosses, and the global lower bound and uniform convergence exclude earlier zeros. There is no assertion of convergence at the exceptional phase. At each fixed L, integrating by parts in the exact formula for xi F_L and separately in its derivative provides eventual sine and cosine dominance, giving one simple zero per lattice neighborhood and only finitely many remaining zeros. The packaged check.py and check_output.txt were inspected, not rerun. Numerical examples are corroboration only; all decisive claims were checked analytically.

## originality

PASS

The supportable distinction is the matched first-real-zero law and phase-selected first-zero limit with a single explicitly identified tangency of the limiting profile. The Gaussian transform identity, endpoint asymptotics as a method, the zero-free sector |xi|<=2L, and the elementary fixed-cutoff endpoint census are not the basis of this originality judgment. Neither the closest inspected special-function result nor the strongest related same-day indexed theorem covers the onset and phase selection for this hard cutoff. This is a bounded comparison, with a specific unresolved risk in earlier finite Fourier transform work.

## value

PASS

This locates the first failure of the positive Gaussian Fourier profile caused by a sharp aperture. The moving first crossing is not captured by the classical fixed-aperture large-frequency census. The exact log-scale displacement, phase dependence, and isolated possible tangency describe quantitatively why a naive constant-offset or universally continuous phase limit is inadequate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
