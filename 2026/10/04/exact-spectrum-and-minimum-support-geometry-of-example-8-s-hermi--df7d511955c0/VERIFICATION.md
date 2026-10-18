---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The frozen RESULT.md generator polynomials were expanded over F4 with omega^2=omega+1 and all seven cyclic shifts of three R-module generators; exact independent GF4 Gaussian elimination gives rank(C)=14. Conjugation of the ordinary nullspace constructs D=C^{perp_h} of dimension 7, rank of Hermitian Gram D*conj(D)^T is 6. Independent exhaustive enumeration of all 4^7=16,384 words reproduces W_D(z)=1+357z^11+756z^12+1113z^13+1998z^14+2520z^15+3633z^16+3024z^17+1722z^18+987z^19+210z^20+63z^21. The hull is spanned by (1^14,0^7); 357 min words/3 nonzero scalars yield exactly 119 support sets; closure under block-cyclic shifts gives 17 orbits of size 7. Independently re-counted all ten claimed block-weight patterns: 14,14,7,21,14,7,14,14,7,7. All enumeration is exhaustive for THIS finite code, not universal over optimal codes.

## originality

PASS

Best-of-knowledge statement-level comparison against original and broader sources, with explicit covered components and material-access residual risks. A failed search is not proof of novelty.

## value

PASS

An explicitly published optimal quaternary [21,7,11] Hermitian dual is a natural benchmark. Full weight distribution, hull (relevant to Hermitian LCD/quantum constructions) and geometry/orbits of minimum supports are intrinsic, motivated invariants not determined by the published distance parameters. The exact support incidence structure can be used in subsequent design/decoding classification. This does not purport to classify all optimal codes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
