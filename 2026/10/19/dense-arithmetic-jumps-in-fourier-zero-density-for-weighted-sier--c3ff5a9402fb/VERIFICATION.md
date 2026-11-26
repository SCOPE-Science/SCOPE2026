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

Pass for repairs/4/RESULT.md. The original leading coefficient, fixed-weight count and zero classification are correct, but the explicit assertion of nonuniformity in the original scope and limitations is false. In the strict phase domain, the closest integer point to (u,v) is (0,1), and u+1-v>1/2 implies a root-to-lattice distance >1/(2√2); the boundary roots are at least 1/2 from the lattice. Thus no scale above 2√2 R can contribute, uniformly over every weighting. Counting translated square lattices by centered square cells gives a uniform per-coset error O(R/2^k+1); summing through the uniform cutoff and restoring the omitted main terms costs O(R+1), including at large finite h and at the boundary. The compact-local product tail is nonvanishing; strict mask roots have opposite nonsingular Jacobians; the single boundary root is a fold with nonzero linear term and local degree zero. Matching two scale cosets is precisely the signed congruence; matching absorbs all of the sparser coset. Reduction by h gives the disjoint first h levels, while half-integer roots give disjoint levels of one sign. Odd torsion characterizes return, bounded periods give a finite set, and odd denominators approximate any oriented root. Products of nonzero leading Taylor polynomials give the vanishing-factor count for the order, and reflection pairs the nonresonant indices. An independent integer-grid calculation at radius 140 reproduced 30,790, 38,502 and 40,424 for signed periods 1, 2 and 3 and confirmed equality of the truncated full and first-return unions.

## originality

PASS

For the corrected final claim, credit the known mask-product framework and exclude the equal-weight specialization as an originality claim. No inspected source proves the arbitrary-positive-weight dyadic real-frequency signed-return law, its discontinuity set and the repaired uniform estimate. Closely related indexed weighted density laws use different bases and/or dimensions, dependent weights, or lattice frequencies. The named equal-weight predecessor could not be verified independently, but even the full uniform-weight multiplicity and density law as described in the frozen record does not cover the weighted result.

## value

PASS

A standard Fourier zero-set representation does not tell how many distinct orthogonality frequencies are created by repeated scales. This natural family has an exact arithmetic correction to the density, with dense but individually quantifiable jumps, unbounded orders only in the resonant strict regime, and an isolated degree-zero boundary regime. The uniform counting error makes comparisons across weights meaningful without presuming uniform continuity of the limiting density. This is a complete density classification for a specified weighted family, not just a computation at equal weights.

The dated certificate retains the supplied scientific assessment, sources and limitations.
