---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The idempotent equation in the specified natural basis is x=Aᵀx^[2]. Its fixed space is binary-linear. In a minimal nontrivial dependence among binary-independent fixed vectors over F_q, normalize one coefficient and compare the relation with its semilinear image. The remaining vectors are F_q-independent, so every coefficient equals its square, contradicting binary independence. Thus the fixed dimension is at most s by containment in im(Aᵀ). For an F_q frame of r fixed-point candidates, its squared frame spans an r-plane. The kernel must miss this plane. The kernel is uniform and the transverse kernels are graph lifts of (n−s)-planes in the quotient, giving q^{r(n−s)}[n−r:n−s]_q choices. Conditional on transversality, the image frame is uniform by left GL_n invariance. Summing over all candidate frames cancels its cardinality and gives the claimed moment α. Division by |GL_r(2)| converts frames to binary subspaces; binary Gaussian inversion gives the signed formula. The r=0 moment is one; rank zero has only zero as idempotent, and rank one gives the stated Bernoulli law. Equivalently α=∏_{j=0}^{r−1}(1−q^{j−s})/(1−q^{j−n}), so it is identically one for s=n and tends to one at fixed n,s. The latter moments are exactly those of uniform GL_s(2) by transitivity on binary r-frames, completing the limit.

## originality

PASS

The exact law on each singular rank stratum, and its fixed-rank field-size limit, are the distinct contributions. The perfect-algebra distribution and the binary fixed-frame and Gaussian inversion methods are established ingredients. Exact full-rank and all-matrix laws must not be credited to this record.

## value

PASS

Rank is a natural invariant of the algebra's multiplication image. Conditioning on it identifies what the perfect law and the mixture hide: finite-field variation already at rank one, exact probabilities up to the maximal possible idempotent count at any rank, and a universal binary fixed-space limit at fixed rank. The complete conditional classification is more informative than the unconditional mean or a finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
