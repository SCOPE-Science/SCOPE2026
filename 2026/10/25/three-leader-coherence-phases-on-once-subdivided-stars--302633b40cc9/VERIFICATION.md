---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Reconstructed combinatorial Laplacian on T_k (k≥3 arms, two edges each), principal grounded follower matrix L_FF, and J=tr(L_FF⁻¹), noting physical total stationary variance J/2. With hub selected, each untouched arm contributes 3, each leaf leader saves 5/2, yielding Jhub=3k−5 for leaves on distinct arms. With hub unselected, Schur elimination of arm blocks yields J=3n0+nV/2+nI+(1+2n0+nV/4)/(nI+nB+nV/2) for three nonhub leaders. Exhaustively classify III,IIV,IVV,VVV,B+I,B+V orbit types and compare exact linear costs against hub option. This yields uniquely all leaves at k=3 (J=8/3, one set), I+two other leaves at k=4 (J=27/4, twelve sets), and hub+two distinct leaves at k≥5 (J=3k−5, binomial(k,2) sets). Independently formed and inverted exact rational grounded Laplacians for all labeled 3-leader triples for k=3..7 and checked all six symbolic orbit cost formulas through k=20. The proof, rather than finite k tests, establishes the unbounded k claim.

## originality

PASS

Qualified PASS: grounded-Laplacian trace coherence, Schur complementation and general leader-selection algorithms are classical; path/cycle special cases also predate this work. The assessed contribution is the exact global 3-phase optimizer placement and multiplicity classification on the natural once-subdivided star family, which is not stated or implied by the inspected general leader-centrality formulas without carrying out the nontrivial orbit comparison.

## value

PASS

PASS: exact optimal placement and transition thresholds are central natural invariants in noisy network leader selection. The classification pinpoints a counterintuitive switch from nonhub to hub-based placements at five arms and counts every optimal configuration, giving a closed-form benchmark useful in network design beyond general heuristic algorithms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
