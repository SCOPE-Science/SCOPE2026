---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For each partition, the local 0- and normalized one-excitation subspaces reduce |W_n> exactly to a q-party weighted W with coefficients sqrt(p_j), p_j=|B_j|/n. The explicit normalized block-product witness (|0_j>+alpha sqrt(p_j)|1_j>)/sqrt(1+alpha² p_j) has squared overlap alpha²/prod_j(1+alpha² p_j). Strict concavity of log(1+alpha²p) gives product <= (1+alpha²/q)^q, and alpha²=q/(q-1) yields F_Pi²>=((q-1)/q)^(q-1) strictly for nonuniform block sizes. For q|n the equal-block state is locally the symmetric q-qubit W, whose standard exact product overlap is A_q; singletons give A_n. Expanding (q-1)log(1-1/q) gives e^-1(1+1/(2q)+7/(24q²)+O(q^-3)). Bounds 2<=q<=n, q|n for equality; finite tests only corroborate.

## originality

PASS

Symmetric W product fidelity is preexisting, and Shimoni–Biham previously studied the *same* W state under arbitrary partitions, including exact bipartition values. Their accessible analysis does not establish the all-q best-partition equality or the O(1/q) lower sharpness relative to the 2026 random-coloring upper existence theorem. Distinct optimization quantifiers and limiting regime matter. Best-of-knowledge originality passes with explicit risk from full unread Bao manuscript and possible unindexed optimal-partition results.

## value

PASS

The W family provides a sharp natural witness that the 2026 block-product relaxation cannot enjoy a uniform o(1/q) additive error over arbitrary states, with exact best partition and first two asymptotic terms. This evaluates a specifically motivated quantitative loss in product-state testing, not merely another known W fidelity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
