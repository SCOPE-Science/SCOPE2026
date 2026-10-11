---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Every nonidentity kernel element has order p. For j=1,…,q-1, fixed-point-freeness makes c^j-1 invertible, while (1+c^j+…+c^{(q-1)j})(c^j-1)=0, so every vc^j has order exactly q. This gives the two ψ formulas. Frobenius orbits on V\{0} give q|(p^r-1); hence D=p^{r+1}-p+1 is congruent to one modulo p and q. The gcd therefore reduces to gcd(D,q-1), which is strictly smaller than D because q-1<p^r<D. An independent arithmetic sweep checked the gcd identity on 53 feasible small (p,r,q) triples; the proof is universal.

## originality

PASS

Lazorec's foundational ψ-divisibility paper treats ZM and cyclic-by-cyclic cases and uses cyclic normal Sylow obstructions; it does not cover an elementary abelian Frobenius kernel of rank at least two. The later ψ-divisibility-graph paper keeps the existence of a nonabelian ψ-divisible group open. A fresh Resultary search returned the audited theorem as the exact match and a separate cyclic-Sylow obstruction, whose cyclic-kernel hypothesis does not dominate this family.

## value

PASS

The theorem removes a natural infinite noncyclic-kernel Frobenius family from the open search for nonabelian ψ-divisible groups and identifies the kernel itself as a uniform exact obstruction. That is a motivated structural exclusion rather than a small-instance computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
