---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For finite fields of prime-power order q, dimensions n>=1 and all product lengths m>=1, the proof is correct. Fitting decomposition partitions every n-endomorphism into invariant nilpotent and invertible summands. Counting ordered decompositions proves N_r=q^{r^2-r} (also for r=0). If fixed C has rank r, write C=P diag(I_r,0) Q; P^{-1}CBP=diag(I_r,0)(QBP) is block upper-triangular with a uniform r-by-r leading block, so Pr(CB nilpotent|C)=q^{-r}. This is also Pr(Cv=0|C) for an independent uniform vector v. For C=A_1...A_{m-1}, independence allows replacing nilpotence of CB by vanishing of Cv. Starting with a uniform vector, nonzero survives each independent matrix multiplication with probability 1-q^{-n}; zero is absorbing. The survival probability is (1-q^{-n})^m and its complement proves the result. For products of matrix blocks Wedderburn–Artin and independence of uniform coordinates show exact multiplication of their probabilities. Edge cases m=1, n=1, any prime-power q and r=0 are consistent; the zero ring and m=0 are correctly excluded. The reviewed script performs exact power-test enumeration in limited small rings; independently written trace-and-determinant convolution verifies all q=2,n=2,m=1..5 and q=3,n=2,m=1..4, nine exact counts. The universal proof, not finite tests, establishes unrestricted quantifiers. No inconsistency found in displayed 2026 proof, scopes or normalizations.

## originality

PASS

IMPORTANT NEW PRIOR COVERAGE: Wästlund (2020), arXiv:2008.13017 Proposition 14, establishes the exact m=2 square-matrix value as a specialization of his stronger rectangular two-factor formula; Fine–Herstein/Leinster establish m=1. Thus neither m=1 nor m=2 is novel. The all-product-length formula for m>=3 is the surviving substantive originality claim: Wästlund assumes two independent UNIFORM factors; their proposition cannot simply be applied to a grouped product of m-1 matrices because it is nonuniform. The submitted conditional-rank/vector-survival derivation proves the additional step, yielding an exact all-length law and a natural complete semisimple family. Full relevant primary sections of Wästlund and Leinster and two complete published Resultary findings were read. Sarma–Subedi 2026 is highly relevant but only an accessible extended excerpt was inspected; protected full-text access required a disconnected VPN. We therefore do not claim whole-document noncoverage of that paper, and retain its priority risk. The PASS is best-of-knowledge for the extension m>=3, not historical uniqueness of any two-factor formula.

## value

PASS

The probability of nilpotence after m unrestricted independent uniform matrix factors is a canonical, motivated finite-ring invariant; it is not determined by a one-factor count or Wästlund’s exact two-factor result alone. The full m>=3 identity provides a closed all-length law for every n and prime power, quantifies absorption across successive random linear maps and yields the complete finite semisimple class by direct-product decomposition. The surprising match to zero products over the extension field is an exact structural observation despite nonisomorphic rings. This is a natural complete family with future comparative usefulness; it is not an arbitrary tiny case, although the foundational calculation is short and the m=1,2 specializations are prior work. No claims for nonuniform/correlated factors or nonsimisimple rings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
