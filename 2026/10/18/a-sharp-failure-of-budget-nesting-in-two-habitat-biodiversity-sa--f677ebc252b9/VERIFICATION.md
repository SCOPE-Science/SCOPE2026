---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For independent uniform-without-replacement habitat draws, exact absence multiplication yields F(x,y)=sum_s[1-C(A-a_s,x)/C(A,x)*C(B-b_s,y)/C(B,y)]. An independent exhaustive exact-rational enumeration of all species-abundance-pair multisets modulo habitat swap through N=6 reproduces the 2,4,14,28,69 census counts, three globally nonnested N=6 profiles, and the unique adjacent-gap profile with budget-2 optimum (x,y)=(2,0) and budget-3 optimum (0,3). For unbounded r>=2 and K>=r+2, the displayed loss D=(1-x/r)y(y-1)/(K(K-1))+x(r+1)y/(rK) is the expectation of within-B duplication plus cross-habitat repeated species; xy>=r for x>=1 makes D(x,r+1-x)>D(0,r+1). At budget r all-A is uniquely perfect: every competing split has positive repetition probability. For disjoint species sets each habitat marginal richness gain is decreasing, so sorted marginal increments produce nested optima. Finite enumeration does not prove the unrestricted r,K statement; the inequalities do.

## originality

PASS

Best-of-knowledge originality after comparing exact statements/implications, relevant published corpus findings and available primary material. Classical ingredients are credited; no located stronger theorem or exact table entails the claimed new conclusion. Residual access and priority limits are recorded.

## value

PASS

Survey cost and effort reoptimization with overlap is a natural problem. This yields the exact smallest census where optimal plans cease to nest, distinguishes adjacent incompatibility from failure of a whole optimal chain, and provides a uniform arbitrarily large forced redesign family. These are structural optimization boundaries, not merely a numerical six-individual curiosity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
