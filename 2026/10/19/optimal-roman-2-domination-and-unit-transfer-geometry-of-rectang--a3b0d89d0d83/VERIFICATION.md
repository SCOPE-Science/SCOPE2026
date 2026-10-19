---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the finite corroboration

Run `python italian_rook_check1.py` and `python italian_rook_check2.py` in a Python 3 environment with the standard library. Each emits deterministic numerical assertions and the terminal success markers `DIRECT_EXHAUSTIVE_CHECKS_OK` and `STRUCTURAL_CHECKS_OK`, respectively.

The first program enumerates each labeling of the tested weight range with cell labels at most \(2\), directly verifies all zero-vertex inequalities by summing actual row and column neighbors, and checks complete minimum-family membership, count and all connected components. The tested parameter pairs are \((m,n)=(2,2),\ldots,(2,6)\), \((3,3),\ldots,(3,7)\), \((4,4),(4,5)\). It explicitly excludes feasible configurations of smaller weight in these cases. Each parameter's full state space is tested, not a random sample; only its reported `sampled_ecc` is one representative's eccentricity and must not be mistaken for a full radius/diameter calculation outside the product regime.

The second constructs all possible row-weight-two profiles independently. For \((m,n)=(2,5),(2,6),(2,8),(3,7),(3,8)\), it checks every constructed state directly, counts the complete degree histogram from the local transfer rule, and checks that a state with disjoint rowwise target supports attains distance \(2m\). It independently enumerates all onto maps and intersection allocations for the critical parameter pairs \((m,n)=(2,4),(3,6),(4,8)\).

Record files `italian_rook_check1.out` and `italian_rook_check2.out` reproduce the two scripts' actual output. Both finish with the expected success markers. These checks do not constitute infinite enumeration or independent external scientific certification; all-parametric results rest on the proof in RESULT.md.
