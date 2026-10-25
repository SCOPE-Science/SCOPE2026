---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The Hardy monomial basis yields T e_n=e_(a*n/b) exactly when b divides n, where a=m/gcd(m,k), b=k/gcd(m,k) are coprime; n=0 is the constant invariant direction. For each positive n, maximal powers of a and b give a unique n=a^j b^h c, with a and b not dividing c. If a,b>1, fixed c and j+h=L-1 form one length-L truncated-shift chain; infinitely many c congruent to 1 mod ab give countably infinite multiplicity for every L. If b=1 or a=1 the corresponding families are countably many forward or backward shifts; a=b=1 is I. All powers are partial isometries. Von Neumann inequality bounds p(T) by its maximum on the closed disk; phase vectors in arbitrarily long blocks or shift copies give the reverse norm and Calkin-norm inequality. Weakly null singular sequences and infinite-dimensional kernels/cokernels establish every |lambda|<=1 as Fredholm essential spectral point for m!=k; Neumann series excludes |lambda|>1. The basis action also proves point spectra and strong but not uniform power convergence when b>1. Independent exact divisibility/transition checks on 2,495 indices for five (m,k) pairs passed; the proof, not finite tests, handles all m,k>=2.

## originality

PASS

The 1970 Halmos–Wallen power-partial-isometry model already supplies the abstract building blocks and is not new; the assessed assertion computes the complete multiplicity spaces for these concrete Hardy monomial products, including all incomparable exponent pairs becoming unitarily equivalent, and their sharp Fredholm/polynomial essential profiles. The 2026 Leng–Zhao product paper targets Schatten membership, not the exact unitary multiplicities. Resultary semantic queries found neighboring weighted shifts and composition problems but not this source-specific multiplicity classification. This is best-of-knowledge, not exhaustive priority certification.

## value

PASS

The family C_k* C_m is a natural composition-adjoint construction on Hardy space. A complete two-integer unitary classification, exact all-length infinite multiplicity for incomparable exponents, and full Calkin polynomial norm are structural invariants not automatically known from general power-partial-isometry theory. The counterintuitive collapse of every incomparable pair to one unitary type is mathematically informative and reusable even without a general-nonmonomial extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
