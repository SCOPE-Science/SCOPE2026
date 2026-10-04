---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The theorem is verified deductively; no finite computation is required or used as a certificate for the infinite statement.

1. The identity \(D(a)=Q_a(\{0,1\})\), the definition of sparsity, Campbell's Lemmas 3--6, and the complete proof of Campbell's Theorem 2 were inspected in arXiv:2609.30771v1.
2. In Campbell's proof, total reality is invoked only when passing from a bad conjugate \(a^{\ast}\notin(0,1)\) to \(a^{\ast}\in\mathbb R\). The replacement argument is exhaustive: if \(a^{\ast}\notin\mathbb R\), then \(a^{\ast}\notin[0,1]\) immediately; if \(a^{\ast}\in\mathbb R\), irreducibility excludes the endpoints \(0\) and \(1\), so again \(a^{\ast}\notin[0,1]\).
3. Every subsequent step uses only the real compact set \(K=[0,1]\cup\{a\}\), the fact that the bad conjugate is outside \(K\), and the stated lemmas. Thus the proof survives with no total-reality assumption.
4. The strong-PV definition and Theorem 4.12 of Fenner--Green--Homer were inspected in the open-access article; they give uniform discreteness of \(D(a)\) for every real strong PV number.
5. The real-parameter algebraic-integrality implication is explicitly restated as Pinch's Theorem 8.1 in the extended full text of Fenner--Green--Homer.

Limits: the original 1985 paper was not full-text inspected here, and the theorem does not address nonreal parameters. Independent audit has not been performed.
