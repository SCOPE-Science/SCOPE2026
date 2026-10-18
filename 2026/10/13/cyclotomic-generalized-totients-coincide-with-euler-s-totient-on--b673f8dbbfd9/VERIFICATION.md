---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

PASS: CRT yields phi_P(n)=n product_{p|n}(1-rho_P(p)/p) for arbitrary integer polynomial. For m=ell^a the reduction Phi_m(X) mod ell=(X-1)^phi(m) has one distinct root, whereas for p!=ell the cyclic group F_p^* has phi(m) primitive mth roots exactly if m|(p-1), else none. The global equality cancels the ell factors and becomes product_{other p}(p-rho_m(p))=product_{other p}(p-1). Since phi(m) is even, for odd p!=ell all left factors are odd; parity eliminates any extra odd p when ell=2 and when ell odd with 2 absent. When ell odd and 2 divides n, v2 forces exactly one other odd prime q, where 2(q-rho(q))=q-1; rho=0 impossible, rho=phi(m) implies q=2phi(m)-1 and m|q-1=2(phi(m)-1), contradicting m odd and 0<phi(m)-1<m. Thus no extra prime; conversely ell powers obey both local factors. Independently compared definition and predicted equality for nine indices 3,4,5,7,8,9,11,16,25 and every n=2..300 (2691 pairs). The finite cases are corroboration, not the proof.

## originality

PASS

PASS best-of-knowledge: Robu introduced the generalized totient and proved broad asymptotic lower bounds, not the exact cyclotomic prime-power coincidence set. Standard finite-field root-of-unity facts give the local factors, while the global parity and exceptional {2,q} elimination yield a quantified classification. No published exact same equality classification appeared in targeted semantic and primary searches. An unindexed elementary special case remains possible.

## value

PASS

PASS: The exact equality locus for a generalized totient attached to the canonical infinite family of prime-power cyclotomic polynomials is a natural arithmetic classification. The global parity/2-adic obstruction gives a nontrivial all-n theorem beyond the known local root-count formula and can serve as a precise boundary for further non-prime-power indices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
