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

Counting the nonzero-difference hyperbola by (x−y)(x+y)=a proves the character sum −1 for x²−a and hence ∑χ(1−δc²)=χ(−1); there are no zeros. A graph tiles vertically and the trace characters in the first coordinate form its spectrum (the finite-field trace pairing is nondegenerate, even when Tr(1)=0). Squaring the chosen ± representatives and their negatives gives each square once; the other slope multiplies those norms by a nonsquare. The punctured graph thus has one representative at each nonzero norm, and norm-one field multiplication acts simply transitively on each level, tiling all nonzero frequencies. With determinant one and the stated transpose/shift, the Fourier amplitude is q^(−1/2) times the character in the graph coordinate; disjoint blocks and trace-character orthogonality yield Parseval and the exact simplex Gram. Each nonzero slope and its zero locus recover c and H from the graph, so the count is of distinct graphs for fixed δ, not equivalence classes or all graph transversals. Exact finite arithmetic at q=3,5,9,27 independently confirmed slope counts, orbits and off-diagonal character sums.

## originality

PASS

Qualified PASS for the explicit two-slope norm transversal for every odd prime power and exact count of the stated family at fixed nonsquare δ, not for the abstract frame criterion or the previously constructed prime q≡3 (mod 4) graph. Iosevich–Lai–Mayeli’s Theorem 4.4 is an exact special case at δ=−1 with the usual half of the prime field. The anisotropic form, unlike the q≡1 Euclidean form, has a norm-one group acting regularly on each nonzero norm level. The trace-character and deleted-column Gram computations are natural consequences of this explicit construction, not an independent novelty claim.

## value

PASS

The useful step is the explicit graph transversal that is simultaneously compatible with additive tiling, spectrality, and anisotropic cyclic norm dilation in the previously problematic q≡1 regime as well as in nonprime fields. The exact family count makes that construction quantitative; the simplex computation alone would not be a contribution independent of the transversal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
