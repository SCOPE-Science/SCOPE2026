---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Every pattern with a descent must include the original first entry and is uniquely a grid element tau_(a,b) with 1<=a<=k-1 and 0<=b<=n-k; all others are identities iota_s. Length ranks and longest increasing subsequences force all covers to be identity-chain edges, identity-to-tau bridge edges, or two-coordinate grid edges. The specified labels s,n,a+1,(k-1)+b+1 are strictly increasing for exactly one lex-minimal maximal chain in each of the three possible interval types; a premature bridge labeled n would have to be followed by a smaller label. Reverse-complement preserves pattern order. I wrote a separate exact subsequence poset checker, enumerating every family through n=8 (28 n,k families, 5132 maximal-chain tests) and independently matching the label condition; the universal proof rests on the complete element/order description, not bounded enumeration. Degenerate k=2,k=n,n=2 included.

## originality

PASS

PASS best-of-knowledge. Smith proves the equal-descent endpoint case and explicitly conjectures the broader [1,pi] one-descent avoidance case; the new family has unequal endpoint descent counts. McNamara–Steingrímsson prove a layered-permutation theorem; nontrivial members k>=3 are not layered.

## value

PASS

The claim gives a concrete infinite subclass of Smith’s one-descent shellability conjecture, proving the stronger EL property with an explicit reusable edge-labeling and complete interval model. It is not a trivial restatement of shellability for intervals whose endpoints share descent counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
