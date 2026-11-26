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

At depth zero the atoms and truth constant span the formula space; inductively atoms, the constant, and diamonds of the finitely many preceding-depth truth functions span the next space, since box is NOT-diamond-NOT. Hence the test vector including the constant coordinate 1 is well defined at each finite depth even over infinite frames. For a successor set S in that hyperplane, the false diamond tests are exactly the linear annihilator of span(S). Equality of annihilators is equality of spans; for a nonempty S, slicing the span at constant coordinate 1 recovers its affine hull. The all-zero span is precisely the empty case. This proves both directions with the current atoms also fixed. An affine basis chosen from S uses r+1 distinct successor vectors, and fewer worlds cannot generate a hull of dimension r. Recursive selection in disjoint depth-limited unravelings preserves the selected vectors even when original edges have cycles or shared targets. For the census, the one-variable depth-one configuration is F₂ times the four affinely independent points (u OR v,u,v) in F₂³. If a hull projects onto the affine span of k of these vertices, its projection is either injective (a graph, 2^k choices, dimension k−1), or has the full one-dimensional vertical kernel (one full preimage, dimension k). Each is realized by choosing points over the k vertices and, for the second case, doubling one fiber. Summing over the binomial choices for k=1,2,3,4 and appending the empty case gives (1,8,28,38,20,1); each hull admits both root atom values. Dimension four occurs and needs five successors. Counting all affine flats and the independent root valuation gives 8,48,416 at depth one for n=1,2,3. The supplied checker is not needed for these counts and was not run; its use of int.bit_count requires Python 3.10+, rather than the advertised 3.8+.

## originality

PASS

The same-day S5 theorem substantially overlaps the local affine invariant and sharp dimension bound on equivalence-class frames. That fact receives no separate credit here. The arbitrary-relation recursion and its realizable 192 one-variable depth-two theories are not covered by that frame-restricted statement or by the strongest inspected broader literature. Same-day ordering is not established.

## value

PASS

The precise affine hull is a complete replacement invariant with an exact, rather than merely sufficient, branching bound on arbitrary frames. The one-variable census shows how far the second step of the invariant goes and gives a realizable worst-case witness. This distinguishes parity expressivity from both unrestricted Boolean observations and equivalence-class collapse in S5.

The dated certificate retains the supplied scientific assessment, sources and limitations.
