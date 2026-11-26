---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The last-position bijection maps all distinct subsequences of x, including empty, bijectively to those of xc ending in c by appending c; the other ending class is unchanged. This gives precisely the two transfers. Both adjoint identities, det H=2t^2 and H e_3=t(1,1,0)^T give M(u^R)=H^{-1}M(u)^T H over Q(t). Inserting the identity or T_c between the two half transfers gives the two stated polynomials without specializing at t=0. Empty half gives P=0 for the empty host and P=t for either center. Exact symbolic multiplication and an explicit distinct-string oracle agreed coefficientwise on 381 hosts from all 127 halves of lengths 0–6. Replay with Python 3 and SymPy: /workspace/branches/db63b1c3-41e7-4fe0-be69-70be77ccef6a/adjoint_check.py. These finite checks corroborate the general proof; uploaded script inspected, not executed.

## originality

PASS

Qualified to the explicit length-graded reflection identity and common adjoint for both parities. The ungraded case for either parity and the distinct-subsequence recurrence are prior background. The elementary length-weighted algebra can be viewed as an extension of the known concatenation method; no inspected prior theorem supplies the polynomial pairing or implies it merely by specializing an existing stronger graded formula.

## value

PASS

The useful fact is the explicit quadratic pairing that translates two half-word ending profiles to every length of an unrestricted subsequence spectrum, uniformly for no center or either center. It gives a direct reflection rule without propagating a second half through the dynamic program and exposes which graded statistics of the half enter. This is a modest structural enumeration result, not a claim of a new DP, faster general algorithm or new extremal theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
