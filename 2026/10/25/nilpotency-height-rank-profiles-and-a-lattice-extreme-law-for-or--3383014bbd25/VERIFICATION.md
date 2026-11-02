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

An order-preserving partial isometry on [n] is a partial translation. For fixed nonzero displacement d, domain masks split into d residue chains; ν(f)=one plus longest consecutive-one run, and every nonzero such shift is nilpotent. The finite-state no-k-run generating function is derived by terminal and nonterminal blocks, and product over the chains gives the stated complete rank/height polynomial including the one empty map. For fixed d, isolated starts of k-runs have factorial moments approaching (θ/2)^h; the geometric distribution of |d| permits truncation and mixing, giving e^{-θ/2}. Distinct endpoint and k=1 cases checked; independent mask/finite-automaton comparisons for 36 (n,k) pairs n≤8 agreed. Finite tests do not prove the lattice law.

## originality

PASS

Prior work counts all nilpotents of this inverse semigroup and separately studies longest Bernoulli head runs. The full rank-by-least-zero-power filtration H_n,k(z) for all n,k and its random uniform-nilpotent lattice extreme law are not determined by the old totals or rank census without the submitted translation-chain decomposition and geometric-mixture argument. Some older 2014/2016 semigroup texts not read completely and remain priority risks.

## value

PASS

Nilpotency height is a canonical semigroup invariant and refining it simultaneously by domain rank provides a complete natural finite classification; the sharp lattice law describes a uniform random element of the same semigroup rather than an arbitrary run model. Existing nilpotent totals and longest-run theory are credited, not claimed new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
