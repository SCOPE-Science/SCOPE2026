---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The folded nine-cube is X=F₂^9/<all-ones> with 256 cosets, distance d=min(Hamming distance,9−Hamming distance). Even-weight Walsh characters descend to all 256 characters; their nontrivial weights 2,4,6,8 have multiplicities 36,126,84,9. Direct Krawtchouk summation yields λ2=5+8·2^p−14·4^p, λ4=1−4·2^p−4·3^p+6·4^p, λ6=−3+8·3^p−6·4^p, λ8=−7+20·2^p−28·3^p+14·4^p. There is no antipodal-shell doubling factor. In a=2^p, α=log₂3, λ8=14a²−28a^α+20a−7 strictly increases for a≥1 (positive derivative at 1, positive second derivative using α<8/5); it uniquely vanishes at p*=0.323267128142707..., below 1/3 by exact rational cubing bounds. Rational inequalities keep the three other nonconstant multipliers strictly negative on (0,1/3]. Thus d^p is conditionally negative exactly 0<p≤p*. The centered Euclidean Gram loses only the multiplicity-nine weight-eight sector at the endpoint, so dimensions are 255 below and 246 at p*. Squared Euclidean embedding/Schoenberg gives positive definiteness of e^(−td^p) for every t>0 exactly on that interval; a positive Walsh eigenvalue gives a small-t counterexample above. Independent 256-coset Walsh/Krawtchouk reconstruction checked the exact eigenvalue vectors, root and dimensions.

## originality

PASS

The final statement, not the title or isolated numbers, was compared against the actual prior implications and synonyms, with bounded source reading and explicit priority risks. The surviving precise assertion is not implied by the inspected sources. Best-of-knowledge PASS, not unconditional certification. A folded-cube association-scheme or generalized-roundness article may already contain the same Krawtchouk specialization, threshold and endpoint dimension without the same terminology. Published general machinery is prior; claim of first discovery is qualified.

## value

PASS

The folded nine-cube is a canonical distance-transitive antipodal Hamming quotient, and the supremal negative-type exponent is a natural metric embedding invariant. A complete all-p classification, exact transcendental crossing equation, and nine-dimensional endpoint rank collapse are mathematically useful data for metric embeddings and radial kernels on this natural graph. The narrow n=9 scope is explicit, not a fabricated family-wide classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
