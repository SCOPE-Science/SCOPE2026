---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For Hilbert–Schmidt T with T^4=0, direct multiplication gives R*R=t^2T*T+s^2TT*+ts(e^{2iθ}T^2+e^{-2iθ}T*^2). Squaring and tracing, the fourth harmonics vanish because Tr(T^4)=0; cyclic trace identities yield the stated constant term and 4ts(t^2+s^2)Re(e^{2iθ}Tr(T^3T*)). Maximizing and minimizing the real part gives the exact radius and oscillation. The kernel filtration K_j=ker T^j makes T strictly block upper triangular; Tr(T^3T*) is the Hilbert–Schmidt inner product of A12 A23 A34 with A14. The four-factor Hilbert–Schmidt bound and AM–GM give |gamma|<=||T||_2^4/16. Equality in each inequality forces the unused blocks to vanish and the four remaining blocks to be aligned rank-one maps of equal Hilbert–Schmidt norm, giving the four-dimensional path-plus-shortcut form. CHECKER.py was inspected; its finite matrix diagnostics are corroboration only.

## originality

PASS

Resultary's closest hit, 'Sharp weighted Schatten-fourth radii of nilpotent shifts', is a one-step weighted-shift extremum and does not cover arbitrary fourth-order nilpotents. The full accessible Pal–Chandok paper was inspected through its weighted-radius definitions and main inequality statements; it gives general Aluthge-transform bounds and matrix examples, not the exact phase profile or equality rigidity. A published circle-covariant moment result cited by the package has a narrower covariance hypothesis; the shortcut witness has a nonconstant phase profile. Sahoo's 2025 full text was not retrieved in this pass, so that plausible source remains a risk, not an automatic failure.

## value

PASS

The phase trace is a natural invariant, and the sharp 1/16 interference bound plus complete equality structure is a nontrivial operator-classification result at the first nilpotency order allowing nonzero phase oscillation. It is not just the easy trace expansion: the sharp bound and rigidity explain the extremal mechanism and give an exact boundary for weighted Schatten-fourth radius.

The dated certificate retains the supplied scientific assessment, sources and limitations.
