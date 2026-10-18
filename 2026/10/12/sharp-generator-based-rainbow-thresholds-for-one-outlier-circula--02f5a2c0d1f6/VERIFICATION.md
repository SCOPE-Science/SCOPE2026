---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

All cyclic distances are represented by ≤2 steps as [1,2k] union [ell-k,ell+k], touching since ell<=3k+1, and n/2<=ell+k. Positive bands yield explicit color sets red={ell} or {k,ell}, blue the other short lengths, covering each nonedge by two different generator lengths. Negative middle top n require ell+j all force every short color opposite ell but short-only k+1 has no rainbow path. Negative ell=3k forces short colors by k+j descending and contradicts ell-1/ell-2, while ell=3k+1 distance2k has no two distinct generator-length representation. Independent exhaustive color assignments for k=3..6 across all specified (ell,n) agreed with closed form; proof is general.

## originality

PASS

The 2026 Barát–Boyadzhiyska–Freschi super-Dirac study raises generator-based rainbow colorings but addresses dense graphs, while the published exact contiguous-step Dirac-cycle-power result covers ell=k+1 excluded here. Li–Li–Liu treat unrestricted rainbow connection of other abelian Cayley families, not exact uniform-per-generator two-colorability for interval+outlier steps. Primary full-text accessibility for the most relevant 2026 preprint was limited to abstract/secondary scope, retained as originality risk.

## value

PASS

One-outlier circulants are a natural minimal perturbation of well-studied cycle powers; a complete exact three-parameter classification with two sharp positive bands and explicit generator-homogeneity obstructions distinguishes diameter-two rainbow connection from its more rigid symmetric coloring variant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
