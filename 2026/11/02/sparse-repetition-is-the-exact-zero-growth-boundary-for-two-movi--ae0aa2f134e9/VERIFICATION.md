---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The binary cylinders 00 and 11 give A=[[0,1],[1,1]], B=[[1,1],[1,0]], so N_n=1^T product M_j 1 and Lebesgue mass N_n/2^(n+1). Each disjoint pair AA or BB doubles the column-one vector; total selected pairs ≥ceil(d_n/2), yielding N_n≥2^(1+ceil(d_n/2)). Cutting at each equal neighboring pair gives d_n+1 alternating matrix blocks; AB and BA are triangular unipotents, their length-ell maximal row sum is ell+1, and AM-GM yields N_n≤2(1+n/(d_n+1))^(d_n+1). The limiting function t log(1+1/t)→0 proves both limsup and liminf iff statements without claiming a universal entropy limit. Bit-flip conjugacy transforms perfect alternation to forbidden 01, giving exactly n+2 monotone words. Independent direct itineraries across every schedule through n=10 verified counts and integer inequalities. All claims are specific to those two holes, not arbitrary holes.

## originality

PASS

Best-knowledge PASS for the uniform all-schedule zero-growth density equivalence; general moving-hole dimension papers explicitly require base ≥3 for the relevant theorem and periodic capacity results cover at most periodic instances. The matrix word-count mechanics itself is elementary and not claimed independently novel. An unindexed direct binary matrix-product theorem could cover this claim.

## value

PASS

The contrast between two Fibonacci-growth static holes and zero-growth alternating switching is a natural open-dynamical effect; the sharp arbitrary-schedule density boundary and uniform finite-size bounds are useful for nonautonomous symbolic escape rates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
