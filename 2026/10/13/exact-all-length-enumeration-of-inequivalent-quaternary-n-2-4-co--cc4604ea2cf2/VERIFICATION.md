---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Verified the scope and reconstructed the proof. Row changes induce the faithful five-point PGL(2,4) action of order 60, hence A5; ordinary monomial changes remove each nonzero column scalar and permute columns, and leave the number of zero columns invariant. Each nonzero scalar has Hermitian norm 1. The five Hermitian outer products sum to zero (zero off-diagonals by 1+omega+omega^2=0, and even diagonal counts); two distinct projective representatives form an invertible two-column matrix, so their two outer products sum to a rank-two Hermitian matrix. Complementing parity subsets therefore gives Gram ranks 0,1,2 for odd-count sectors {0,5},{1,4},{2,3}. Nullity on the two-dimensional row space gives the hull dimension. Directly from the A5 cycles, a length-L fixed cycle contributes (1+x^L*y^L)/(1-x^(2L)); excluding empty or single-point supports gives the stated two corrections and independent zero padding gives 1/(1-x). Inspected RESULT.md, VERIFICATION.md, verify.py and inequality_certificate.json without executing the supplied script. Independently replayed with `python3 /tmp/opencode/frozen_math_replay_1_2_4.py 4`: a dynamic program counts sorted five-multisets, adding a second orbit exactly when all five entries differ. It reproduces all listed triples, reconstructs both period numerators through degree 358 (an exact degree bound from the denominators) and matches the bundled certificate. Every residue has a nonempty numerator subsequence and U<=5; the smallest coefficient after the shift, multiplied by 120, is 4,050,000 for D01 and 3,240,000 for D12. All pre-shift cases with n>=4 pass. This proves the unbounded inequalities by the exact polynomial representation, not by inferring a trend from finite tests. It is for rank two with zero columns allowed; neither a semilinear nor a full-support ordering is claimed.

## originality

PASS

Ishizuka's cited v1 actually does identify the Hermitian analogue on inequivalent quaternary codes as an open direction (§6 p. 20); the later version instead includes finite semilinear full-support counts. Neither the raw-code theorem nor these finite counts proves the all-length result in the specified monomial equivalence. Araya–Harada cover closely related LCD families and use the projective multiplicity model, but the supported contribution here is the all-length hull-refined orbit formula and strict ordering, not those ingredients or the overlapping LCD entries.

## value

PASS

Dimension two is the natural projective-line case of the named inequivalent-code monotonicity problem. The generating functions cover every length and all hull dimensions and distinguish the two equivalence conventions. They also explain why allowing zero coordinates is material: full-support hull-zero need not dominate hull-one even at the small available lengths. The exact rank-two benchmark and strict ordering are useful independently of extending the method to higher rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
