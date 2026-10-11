---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For even \(m\ge2\), induction gives \(F(m)\le2\phi(m)-1\). If \(3^kp\) is perfect totient and \(p-1=2^a3^bu\) with \((u,6)=1\), then \(F(\phi(3^kp))=3^{k-1}(p+2)\) and \(\phi(\phi(3^kp))=2\cdot3^{k-2}(p-1)\phi(u)/u\). Substitution yields \(\phi(u)/u>3(p+2)/(4(p-1))>3/4\); the support exclusions follow from the Euler product. The finite checker is corroborative only.

## originality

PASS

The directly relevant full papers treat \(3^kp\) under special nested-prime factorizations and do not state a uniform Euler-product restriction on the arbitrary \(6\)-coprime part of \(p-1\). Targeted Resultary and statement searches found no earlier covering theorem.

## value

PASS

The theorem gives a uniform necessary sieve across every \(k\ge2\), including the unresolved \(k\ge4\) range, and excludes infinite congruence classes of candidates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
