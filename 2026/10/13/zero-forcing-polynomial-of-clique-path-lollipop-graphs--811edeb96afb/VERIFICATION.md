---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For k>=3, ell>=1, the k-1 nonattachment clique vertices X are pairwise true twins: leaving two white creates an unbreakable obstruction. With zero X omissions the clique supplies path propagation; with one omission and attachment initially blue, another clique vertex forces it. With one omitted X vertex and a white attachment, the clique is frozen until the path drives a force into the attachment. This happens iff the initial path blue set has its far endpoint or some adjacent blue pair; otherwise every path blue vertex is blocked. These mutually exclusive cases yield x^(k-1)(1+x)^(ell+1)+(k-1)x^(k-1)(1+x)^ell+(k-1)x^(k-2)((1+x)^ell-I_(ell-1)(x)), I an independence polynomial for P_(ell-1). The minimum coefficient gives Z=k-1 and exactly 2k-1 minimum sets. Independently exhaustively checked 24 parameter pairs k=3..6, ell=1..6, including ell=1 boundary; universal result rests on case proof.

## originality

PASS

Aalipour et al. define precisely the same lollipop but study distance spectral invariants; their use of forcing elsewhere does not yield the lollipop polynomial. Boyer et al. provide the path criterion but cannot resolve the attachment-clique lock without a new case split. Menon–Singh supplies operation inequalities, not this exact two-parameter all-sets classification.

## value

PASS

Lollipop graphs are a natural named family interpolating a dense clique and a path. The theorem explicitly characterizes every forcing set and all polynomial coefficients for two unbounded parameters; the k-1 minimum and the 2k-1 minimizer count are structural consequences rather than the only object of interest.

The dated certificate retains the supplied scientific assessment, sources and limitations.
