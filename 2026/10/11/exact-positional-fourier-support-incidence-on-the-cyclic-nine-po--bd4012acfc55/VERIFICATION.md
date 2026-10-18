---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

Frozen RESULT and C++ checker prove exact support existence for A,B iff rank of rows G\B and cols A is below |A|, each A-column deletion leaves rank unchanged, and each demanded Fourier row increases rank. Nonzero kernel coordinate constraints are finitely many proper hyperplanes over infinite cyclotomic field. Independently checked all ranks by two large split-prime reductions: both 100000000000099 and 100000001000377 certified prime by full trial division; ninth roots verified; each k-minor norm bounded by k^(3k)<=9^27 and product primes exceeds bound, proving max modular ranks exactly characteristic-zero ranks. Independently implemented exhaustive all 511^2 nonempty pairs, recovered all 9x9 entries, total 92236, affine 302 and duality 158 orbit-size distributions including all checksums. Original checker.cpp inspected; independent implementation compiled C++17 -O3 and output retained locally. Exhaustiveness is finite for Z9 only, not an infinite-group proof.

## originality

PASS

Same-group prime-square DFT literature already establishes the exact-support rank condition, the size-level uncertainty diagram, and boundary extremals. The audited contribution is the independently reproduced 9x9 numerical POSITIONAL multiplicity matrix and complete orbit distributions, not the known lemmas. Sources inspected do not supply the full counts; database failure remains a risk.

## value

PASS

Z9 is the smallest odd cyclic prime-square group, so complete positional time/frequency support incidence and affine symmetry classes are a natural finite harmonic-analysis invariant. This refines known size-only uncertainty diagrams, isolates one rigid (4,5) affine orbit, and supplies an independently reproducible exact-arithmetic rank certificate for every support pair; meaningful despite being a finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
