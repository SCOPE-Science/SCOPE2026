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

In odd characteristic the minimal polynomial divides a separable (X−1)(X+1); every involutory matrix, including I, corresponds to a unique labeled two-block decomposition. Commuting ordered pairs correspond to four labeled blocks from (I±U)(I±V)/4. Orbit–stabilizer gives G_n times the respective sum of reciprocal G_d products. For p=2 or p=4, write d_i=n/p+x_i, so ∑x_i=0 and ∑d_i²=n²/p+∑x_i². The resulting offsets are the parity lattice for p=2 and a translate of A_3 for p=4. Where every d_i≥n/(2p), the product of reciprocal Φ factors differs from Φ_∞^(−p) by relative O_q(q^(−n/(2p))), since its Euler-product tail begins at d_i+1. All remaining and missing terms have at least one |x_i|≥n/(2p). Bound the omitted hyperplane sum by a union over coordinates and relax the hyperplane constraint for each one-coordinate Gaussian tail; the other coordinate sums are uniformly bounded, giving O_q(q^(−n²/(4p²))) and avoiding any unjustified radial-tail count. For p=2, ∑x_i²=2t² gives the slightly sharper two-block tail in the record by the one-dimensional parametrization. On the retained region the full theta weight is uniformly bounded over the finitely many residues. Positivity converts the errors to multiplicative errors. In C_n/I_n² the two Euler factors from the sums cancel, leaving 1/Φ_n, and the quadratic powers leave q^(−n²/4); replacing Φ_n by Φ_∞ costs only O_q(q^(−n)). The involution k↦1−k in all four coordinates identifies residues 1 and 3. This proves the stated probability with its relative O_q(q^(−n/8)) remainder.

## originality

PASS

Credit the exact two- and four-block finite counts, including the idempotent-equivalent count/probability, and the prior single-involution parity limits. The supported distinction is the full fixed-field, increasing-dimension commuting-pair probability with all residue-coset constants and a relative error estimate. A field-leading polynomial term retains only minimizers at large q; it cannot be exchanged with the fixed-field growing-dimension limit in which every bounded lattice offset contributes. Balanced-rank results condition on both ranks and sample only a lower-dimensional subset of the offset lattice. The known exact finite sum is the starting point, but the new asymptotic comparison needs the surviving contributions from all offsets and uniform error control, not merely re-labeling that sum.

## value

PASS

Commutation of natural finite classical-group samples is a meaningful statistic, and the fixed-field regime is materially different from a field-leading estimate. A coarse decay rate does not resolve the persistent residue effects; this result computes the full leading factor from the distribution of all near-balanced four-block dimensions and controls its relative error. The choice of residue class is forced by integrality of four blocks, not by an arbitrary dimension slice. The value judgment concerns the sharp growing-dimension probability, not recomputation of known finite counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
