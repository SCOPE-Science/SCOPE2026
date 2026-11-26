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

Under weights 1,2,3, F(0)=0 and every increment F(k)−F(k−1) lies in {1,2,3}: extend a maximizing shorter factor by one letter, or truncate a maximizing longer factor. Splitting a factor gives subadditivity F(i+k)≤F(i)+F(k); thus the word formed from the increments has each factor weight F(i+k)−F(i)≤F(k), with equality on the prefix. This proves existence and uniqueness of the normal form in the exact regime used. Equal length and F(n) force the displacement (t,−2t,t). Orient t>0: F(1)=3 forces a c in the lower-c word, which also needs ≥2t b's. Then n≥2t+1. For odd n=2r+1, equality t=r would force count vectors (0,2r,1) versus (r,0,r+1), with maximum length-two weight 5 versus an even value, impossible. For sharpness subtract weight 2 from every letter. The witness core c(ac)^(r−1), of length 2r−1, alternates +1 and −1, starting and ending +1. It attains +1 at every odd length up to the core length. The preceding b (deviation 0) plus an odd core prefix attains +1 at every even length through 2r. All factors have deviation ≤1. The additional initial a in the odd case has deviation −1 and makes the full-length deviation 0 without affecting these proper-length maxima. This gives the displayed normal-form prefixes and Parikh-distance 4(r−1), including the zero endpoints n=2 and n=3. The finite replay independently confirms the expected sequence, but is not used to infer the infinite result.

## originality

PASS

The inspected primary text gives factor-weight equivalence, a unique ternary standard weighted prefix normal form, and a nontrivial example attaining 4 at length four. It explicitly leaves exact Parikh-vector behavior open. No checked statement implies the all-length bound with matching witnesses for each length, or the stronger bound on every pair within a class. The inaccessible journal expansion is a material residual risk, not a claim of noncoverage.

## value

PASS

This measures exactly how much Parikh information the canonical weighted normalization can lose in the smallest alphabet that permits such loss. The bound answers a quantitative version of the original paper's identified question at every length and, as a class-diameter bound, applies independently of which representative is used. It has parity-sensitive sharpness, with explicit infinite families, rather than merely showing a change is possible.

The dated certificate retains the supplied scientific assessment, sources and limitations.
