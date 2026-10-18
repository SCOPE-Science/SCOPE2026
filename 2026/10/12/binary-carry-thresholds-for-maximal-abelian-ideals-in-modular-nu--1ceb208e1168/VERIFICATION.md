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

Left multiplication by e_1 has one Jordan block, so every two-sided ideal is a chain tail A_j, provided the specified multiplication is Zinbiel (the integral binomial identity verifies this in every reduction). Lucas parity gives e_i∘e_k nonzero exactly when (i-1)&k=0, in range i+k<=n. The candidate product e_j∘e_{t(j)} has odd coefficient; for all smaller i+k with i,k>=j, the common t(j)/2 bit forces even coefficients. Thus least nonzero total degree is j+t(j), the tail is abelian exactly when j+t(j)>n, and solving within powers of two gives beta=min(2^r,n-2^{r-1}) and unique largest tail. Independent direct modular-binomial enumeration checked 8,255 pairs of n,j across 2<=n<=128, including all threshold cases; the infinite claim follows from Lucas and Jordan-block reasoning.

## originality

PASS

The closest same-object Ceballos–Towers result is over C and gives a numerically incompatible cutoff. The canonical form from Camacho et al holds more broadly but does not classify char2 abelian ideal dimensions. Lucas is a standard tool, yet applying it to the minimal nonzero tail-product degree and exact all-n beta produces a different invariant theorem.

## value

PASS

The maximal dimension of abelian two-sided ideals is a natural invariant for nilpotent nonassociative algebras. The canonical one-generated Zinbiel family has a known characteristic-zero value but a sharply different modular behavior: an exact binary-carry classification and an unbounded excess along n=3·2^{r-1}. The explicit all-dimension formula provides a nonroutine modular structural fact; finite enumeration alone is not its justification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
