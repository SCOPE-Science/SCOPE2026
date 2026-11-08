---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

PASS: The unsigned vertex-edge incidence B over characteristic two gives F=B^TB with no diagonal self-loops and L=BB^T. Connectedness gives imB=W (coordinate sum 0) and ker B^T=〈1〉. For all-even clique sizes L=Σ_i J_{mi} on tensor factors, with each J²=0; characteristic-two cancellation yields L²=0 and F³=0. Each factor (F2^{mi},J_{mi}) has one contractible 2-block and mi-2 trivial homology blocks; tensor contracting homotopies imply total homology dimension H=∏(mi-2), so rankL=(N-H)/2. Since 1∈W, kerL⊂W and 1∈L(W) (explicit unit⊗all-ones vector, r>=2), rankF=N-2 and rankF²=rankL-2. These ranks exactly yield all three Jordan multiplicities and counts C_t=q^{dim kerF^t}-q^{dim kerF^{t-1}}. With any odd factor, the tensor of e0+e1 in that factor and all-ones elsewhere is a sum-zero Laplacian eigenvector with eigenvalue 1, giving B^Tv a nonzero F-fixed edge state. Independent GF2 line-graph matrices were constructed directly for nine even/odd small tuples and reproduced ranks; no finite test extrapolation to arbitrary field sizes or factors. The claimed exceptional nilpotency index two for K2□K2 follows from rankF²=0.

## originality

PASS

Qualified best-of-knowledge PASS for all even-order Cartesian clique products with H-dependent mixed-alphabet Jordan counts and the odd-factor iff obstruction, NOT for the prior all-m_i=2 cube edge case. Ordinary real adjacency rank results of Davis–Domke–Garner cannot imply characteristic-two Jordan powers. Fish–Key–Mwambene code papers are strongly relevant: their available theorem and summaries cover code ranks and binary Hamming graph geometry, but a complete 2010 primary proof was inaccessible. The independent F² and F³ classification is not established by a rankF code dimension alone. No decisive broader theorem found in actual searches; source-access risk expressly remains.

## value

PASS

PASS: Characteristic-two edge-neighbor dynamics on Cartesian clique/Hamming graphs is a natural linear cellular automaton with a meaningful structural parity boundary. The theorem identifies exactly when every state is extinguished, gives an all-alphabet Jordan census and sharp extinction times, and introduces the nontrivial tensor-homology factor H. The all-binary cube subcase is credited as known rather than claimed new. This is a genuine infinite family classification, not merely a code-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
