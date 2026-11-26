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

Replayed RESULT.md lines 21–44 for the precise operation (reverse block order, not letters). A suffix of the source ends at a 1 and starts with at most m zeros, while a prefix starts at a 1 and ends with at most m zeros. Hence no joining to another block can extend the initial or final zero run beyond the respective bound. For any permitted p,q,r,s let A=m−s, B=m−p. Then q+r=A+B. Take i=max(0,q−B), j=B+i−q; the bounds 0≤i≤A and 0≤j≤B follow from 0≤q≤A+B. The five pieces 1·0^s, 0^(A−i), 0^i·1·0^j, 0^(B−j), 0^p·1 concatenate to the source, and reversing their order gives the prescribed gaps because B−j+i=q and A−i+j=r. Dropping any empty zero-only pieces preserves both concatenations, also at m=0. The gaps describe distinct outputs uniquely, so the count is Σ_{p,s=0}^m(2m−p−s+1)=(m+1)^3; subtracting the two disjoint endpoint violations from the unrestricted stars-and-bars count agrees. The ratio tends to 3/4. Independent enumeration of all 256 masks for m=3 gave exactly the 64 predicted words, not merely the same size (bounded replay: /workspace/branches/543fc415-d8b7-470d-b666-98df41c39a0a/independent_m3.py). Frozen check.py was read, not executed; its m≤7 range is finite and limited to equal gaps despite a helper function taking two parameters.

## originality

PASS

Pass for the all-m output characterization and its count, not for the block reversal operation or the cube sequence. The inspected related literature and indexed records do not state or subsume this exact reachability theorem. The foundational 2021 full text remains an explicit access risk, not evidence of either coverage or novelty.

## value

PASS

This is a motivated small-weight but unbounded family for a standard word operation. The structural result is saturation of the whole endpoint-constrained set, not a few counts or an arbitrary sample. It gives both a witness partition for every reachable word and an exact benchmark for the density among all words of the same weight.

The dated certificate retains the supplied scientific assessment, sources and limitations.
