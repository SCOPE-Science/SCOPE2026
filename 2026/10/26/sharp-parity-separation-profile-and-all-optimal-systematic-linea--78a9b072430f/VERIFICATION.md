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

The encoder E(u)=(u,uP) gives, for a nonempty message support T, the exact weight |T|+wt(sum_{i in T}h_i). Data distance at least three and message-parity separation at least four are therefore equivalent to distinct nonzero check columns h_i with wt(h_i)>=3 and no zero sum of three distinct columns. For r>=5, the Davydov--Tombak structural bound for non-hyperplane sum-free subsets (5*2^(r-4)) lies strictly below M_r=2^(r-1)-r. Thus a maximizer must lie in an affine hyperplane, and counting the s weight-one and s(r-s) weight-two exclusions in {a·v=1} gives at most 2^(r-1)-s(r-s+1), with equality only at wt(a)=1 or r. A through-origin hyperplane holds at most 2^(r-2) sum-free elements. This proves the exact K(r) profile and all r+1 large-r extremizers; r<=4 is checked directly. Strict codeword-distance-three versus full-distance-four distinctions follow from explicit two-column differences. Fresh exhaustive independent set enumeration for r=3,4,5 found K=1,5,11 with 1,1,6 maximizers and inspected constructions r=5,6,7. The finite enumeration is corroboration, not the proof for all r.

## originality

PASS

PASS, qualified: complete restricted sum-free column extremizers and exact systematic fixed-redundancy parity/data protection profile not directly supplied by the inspected source statements; the non-hyperplane sum-free bound is openly credited. Some recent closely relevant coding preprints were accessed only at abstract level; their uninspected main texts remain a material priority risk.

## value

PASS

The fixed appended parity-symbol budget and unequal message/data distance protection are natural practical and mathematical constraints. The sharp dimension-loss profile and all r+1 maximizers distinguish r genuinely strict schemes from one distance-four scheme; this classification is a nontrivial structural consequence of the sum-free stability theorem, not merely a restatement or a one-line coding substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
