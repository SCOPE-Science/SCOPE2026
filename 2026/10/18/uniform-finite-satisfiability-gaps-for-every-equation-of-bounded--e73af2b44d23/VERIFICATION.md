---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Finite bounded commutative BCK-algebras split into standard finite chain factors, and independent uniform sampling of each tuple induces independent uniform tuples in the factors; equation degrees therefore multiply. On the standard continuum, truncated subtraction is 1-Lipschitz for the sum of the two argument distances, so the real-valued difference of the two terms is L-Lipschitz in the sup norm, including repeated variables. A witness in C_(n₀) gives |t−s|≥1/(n₀−1). For Q=L(n₀−1) and δ=1/(4Q), a one-sided coordinate box of length δ at the witness stays in the cube and entirely violates the equation, even for boundary witnesses. If n−1≥8Q, each interval has at least (n−1)δ/2 grid points and thus at least a δ/4 fraction of C_n. If n−1<8Q, a nonzero failure fraction is at least n^(−k)≥(16Q)^(−k). The trivial algebra satisfies every equation; terms with no variables evaluate to 0 or 1 on nontrivial chains, and are either equal everywhere or fail entirely there. Consequently the dichotomy and bound hold. In the accompanying example a pair violates exactly when x>y>0, giving (n−1)(n−2)/2 failures, hence one at n=3 and the reported witness bound 1/25600. The frozen exact-arithmetic checker was inspected, not executed; its finite range is not used for the proof.

## originality

PASS

The all-equation quantitative bound is distinct on the evidence inspected. Evans provides a conditional chain-gap criterion and examples, not a uniform quantitative grid estimate for arbitrary equations. The finite product theorem and McNaughton representation are established background. The closest indexed all-equation classification is for Gödel chains, and the closer same-chain indexed result is restricted to two identities.

## value

PASS

The result replaces a per-identity hypothesis about the set of chain degrees by a bound recoverable from just a single witness and the term syntax. It explains why no sequence of nonunit degrees can approach one in this class, for all arities, and is a useful contrast to Heyting or unrestricted BCK behavior. It does not claim a sharp gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
