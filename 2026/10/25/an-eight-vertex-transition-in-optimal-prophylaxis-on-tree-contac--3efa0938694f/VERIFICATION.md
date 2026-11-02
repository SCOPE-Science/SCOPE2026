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

The expected infected count equals the uniform-source sum of percolation connectivities; on a tree every open path has probability p^{distance}, so (n-1)R(v,p)=sum over ordered residual connected pairs p^{distance}. Directly inspected RESULT.md and verify.py; a fresh independent finite exhaustive checker regenerated unlabelled tree class counts 1,1,2,3,6,11 for orders 2..7, checked a fixed minimizer in every class using exact polynomial root/sign tests, and independently reconstructed the n=8 witness F_2=7+8p+6p^2+4p^3+2p^4 and F_1=7+10p+6p^2+2p^3. Their difference 2p(p^3+p^2-1) has a unique interior root; all other target polynomials are dominated by a candidate globally. Finite enumeration is exhaustive here because leaf deletion recovers every unlabelled tree and the exact sign algorithm covers the entire probability interval; it is not an extrapolation to larger trees.

## originality

PASS

The bond-percolation connection formula is established background, and the nearby exact vaccination-ranking study concerns continuous-time Markovian SIR rather than independent bond transmission. Inspected primary statements do not give the smallest-tree all-p cutoff or the explicit global switch. Conditional best-of-knowledge originality is accepted with older graph-reliability and vaccine-ranking literature as residual risks.

## value

PASS

Whether one fixed intervention target minimizes expected infection irrespective of transmissibility is a natural network intervention question. The theorem supplies the complete sharp order-through-seven boundary and a concrete eight-vertex algebraic transition, separating topology-only selection from probability-dependent selection. This is mathematically motivated finite classification, not a cosmetic isolated calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
