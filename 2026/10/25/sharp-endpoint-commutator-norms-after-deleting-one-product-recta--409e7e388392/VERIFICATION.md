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

Conditioning on X or Y after removing A×B yields exact 3-block row-stochastic matrices P0=[[1-q,q,0],[1-q,q,0],[0,0,1]] and Q0=[[1-p,0,p],[0,1,0],[1-p,0,p]], where S0=A^c×B^c,S1=A^c×B,S2=A×B^c. Their commutator C0=P0Q0-Q0P0 has rows (0,pq,-pq),(-p(1-q),0,p(1-q)),((1-p)q,-(1-p)q,0). The integral kernel K_ij=C0_ij/m_j is skew in the product-measure block masses, and every output block depends only on input block means. Thus the L∞ norm equals maximum absolute row sum 2max{pq,p(1-q),(1-p)q}, attained by block signs; L1 equality is dual since C*=-C in weighted L². Pairwise comparisons give the stated three regions and ties. On orthonormal normalized block indicators H_ij=K_ij sqrt(m_i m_j) is real skew with squared nonzero singular value pq(1-pq), so eigenvalues ±i sqrt(pq(1-pq)); C kills the orthogonal complement. As p=q→1 endpoint norm→2 while Hilbert norm→0. Independently verified symbolic matrix, skewness, C³=-pq(1-pq)C, and row sums. Arbitrary underlying probability spaces are covered because the 3-block kernel is exact.

## originality

PASS

PASS qualified: classical maximal correlation/two-projection theory already implies the Hilbert spectral formula, which is explicitly excluded from novelty. Full-text Resultary records on fixed three-atom real ell4 numerical radius and centered binary-chain mixing norms do not evaluate the asymmetric 2-parameter endpoint commutator. The sharp endpoint row-sum phase diagram and cross-norm separation are new to the inspected primary material, with residual priority risk from elementary finite-state conditional-expectation literature.

## value

PASS

Deletion of a rectangular forbidden event from independent data is a natural conditioning/missing-data model. Exact endpoint commutator norms for two coordinate projections quantify noncommutation in L1/L∞, exhibit phase transitions according to deleted-mass geometry, and separate endpoint and Hilbert stability sharply. The exact 2-parameter statement is a motivated non-Hilbert invariant, not merely a renamed 3x3 matrix norm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
