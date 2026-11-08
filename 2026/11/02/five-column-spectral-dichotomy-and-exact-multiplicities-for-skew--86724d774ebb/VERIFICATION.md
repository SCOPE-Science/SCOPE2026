---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For every existing skew conference C of order N>=8, p=N-1, C^2=-pI, G=I+iC/sqrt(p) is the rank-N/2 ETF Gram with unit diagonal. Each 5x5 skew sign principal minor S has characteristic z(z^4+10z^2+5+8r), where r of its five 4-subset Pfaffian squares are 9. Positivity of real skew singular frequencies gives r<=2, while det(I+S)=16+8r and odd-row divisibility 16|det(I+S) forces r even. Thus r=0 or2, giving precisely A and B spectral types. Global characteristic det(zI-C)=(z²+p)^(N/2), coefficient extraction and 4-to-5 incidence give B4=p(p-1)(p+1)^2/96, B5=(p-3)B4/2 and A5=choose(N,5)-B5, hence formulas. For N=8 A=0 and δ5=1, for existing N>=12 A>0 and δ5=sqrt((5+2sqrt5)/p); Gram full rank follows. Independently enumerated all 1024 5x5 skew sign matrices (384 class A, 640 B) and every 5-subset of Paley C for p=7,11,19, obtaining A/B counts (0,56),(132,660),(4104,11400). Finite checks corroborate matrix-independent proof; no existence for arbitrary N claimed.

## originality

PASS

The Paley construction, skew-conference ETF Gram normalization, and 3/4 erasure bounds are established. The complete five-principal-submatrix spectral dichotomy, matrix-independent multiplicities for all skew conference matrices, and sharp five-column RIP constant are the assessed addition. Published four-column Paley harmonic census covers a different (nonaugmented) frame and 4-column sets, and cannot directly imply these 5-subset counts. Possible older Pfaffian/tournament conference submatrix tables are a priority risk.

## value

PASS

Five-column erasure spectra are directly relevant to ETF robustness and small-order restricted-isometry constants. This is a natural complete finite classification valid for an infinite family of existing designs, with exact relative frequencies and a sharp N=8 singularity boundary; the parity lock and incidence proof supply nontrivial universal structure not a generic code-check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
