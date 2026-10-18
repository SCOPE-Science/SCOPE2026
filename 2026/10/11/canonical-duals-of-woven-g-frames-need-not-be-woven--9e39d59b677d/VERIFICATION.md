---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

F=(e1,e1,e2), G=(e1,e1+e2,2e1+e2). The first vector is common, and direct enumeration of remaining two binary choices gives positive definite frame operators [[6,3],[3,2]], [[6,2],[2,1]], [[2,1],[1,2]], [[2,0],[0,1]], with determinants 3,2,3,2. Their exact eigenvalues yield positive common lower (7−√41)/2 and upper 4+√13. I independently recomputed the exact 2×2 matrices, determinants, S_F=diag(2,1), S_G=[[6,3],[3,2]] and inverse matrices using SymPy. The canonical dual vectors are F~=(e1/2,e1/2,e2), G~=(2e1/3−e2,−e1/3+e2,e1/3); choosing F~ indices1,2 and G~ index3 gives three collinear e1 vectors, hence loses the frame lower bound. Scalar g-frame identification is exact. If S_F=S_G=S, a shared invertible S^{-1} applied to every original weave preserves uniform bounds.

## originality

PASS

The original arXiv source v1/v3 publicly states the unconditional canonical-dual corollary. Later Arabyani Neyshaburi–Arefijamaal and Agheshteh Moghaddam–Arefijamaal only give sufficient dual-wovenness hypotheses and a canonical PARSEVAL (S^{-1/2}) non-weaving example, which does not logically subsume separately canonical DUAL (S^{-1}) non-weaving. No checked source gives this particular source-correction or counterexample. The journal final version’s exact theorem text was not verified and is not claimed to match the arXiv version.

## value

PASS

This concrete counterexample addresses a consequential false blanket stability assertion in weaving frame theory and shows why independently normalizing constituent frames can destroy spanning, even with uniform positive original weaving bounds. The single common-operator sufficient repair identifies the structural issue; it is mathematically motivated beyond a routine frame calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
