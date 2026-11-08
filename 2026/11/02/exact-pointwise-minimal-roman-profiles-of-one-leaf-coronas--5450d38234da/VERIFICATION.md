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

For finite simple G of order n>=1, each minimal Roman function on G corona K1 has precisely pair states (2,0) on A=vertices labeled 2, (0,1) on B=N(A)\A, and independently (0,2) or (1,1) on U=V\(A union N(A)). A positive coordinate decrement destroys feasibility, so these states are exactly pointwise-minimal. This proves M(z)=sum_A 2^|U| z^(2n-|B|). Adding a missing edge strictly decreases sum_A2^|U| via singleton A; empty and complete G yield 3^n and 2^(n+1)-1, with n=1 coincidence. The length-n cyclic binary triple transfer gives the stated four-by-four T(z), with characteristic polynomial t*(t^3-3z^2t^2+(2z^4-z^3)t+2z^5-z^4); its z=1 eigenvalues give 1+(1+sqrt2)^n+(1-sqrt2)^n. Independently implemented graph generation, direct original Roman feasibility and coordinate-minimality checks for all 75 n<=4 base graphs, plus symbolic characteristic polynomial equality; all succeeded. These checks only corroborate the proof for arbitrary n.

## originality

PASS

General pointwise-minimal Roman algorithms and private-neighbor criteria precede this work. The exact full weighted one-leaf-corona distribution, strict edge-monotone total extrema and sunlet Pell–Lucas trace are additional product-specific assertions not located in inspected sources. This is a qualified best-of-knowledge judgment, not a claim that the older criteria are new or cannot be specialized to recover it.

## value

PASS

The pointwise-minimal Roman function weight distribution is a natural graph invariant substantially finer than the minimum Roman domination number. This formula for any base graph gives full weights, a strict densification order and a nontrivial explicit sunlet spectrum; it is neither a tiny-instance exercise nor merely an already-known minimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
