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

Full local definition reviewed: labels {-1,1,2,3}, 3/2 defenders and closed-neighborhood weight >=1. Discharging on any cubic graph transfers (2q-1)/4 from positive q to negative neighbors, forcing every adjusted vertex weight >=1/2; equality is equivalent to positive vertices having exactly two negative neighbors and negative vertices one negative neighbor plus positive labels summing 4. Alternating columns realize weight m for even m. An explicit 256-state finite integer transfer then bijects cyclic length-m words and closed walks. Independently regenerated 81 edges, cyclic SCCs of sizes 22,4,4,4,2, the core characteristic polynomial t^14(t^8-7t^4+1), trace values and direct brute-force m=4 count=42. The exact finite characteristic polynomial plus general equality-rigidity argument proves every even m, not an extrapolated finite sequence.

## originality

PASS

Iurlano, Zec, Djukanovic and Raidl Theorem 6 gives gamma_sdR(C_m square K_2)=m (even m), with example labelings but no full count or trace of all minimizing functions. The new statement is a full multiplicity invariant with exponentially many at m=0 mod4 but only two at m=2 mod4; scalar minimum does not imply counts. Published Roman-{3} complete-prism and signed-Roman multipartite counts have different admissibility and graph. Unindexed equivalent cyclic-word enumerations remain possible.

## value

PASS

The exact number of minimizers of a natural extremal labeling problem is independently useful: an equality classification reveals a striking mod-four rigidity-versus-exponential-growth dichotomy. The 22-state transfer certificate is a nontrivial all-size classification, not recomputation of known gamma=m.

The dated certificate retains the supplied scientific assessment, sources and limitations.
