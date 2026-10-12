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

The exact checker uses symbolic rational arithmetic to verify the defining polynomial and every algebraic identity used in the proof. In particular it checks:

- irreducibility of \(p^4-p^3+2p^2+p+1\) over \(\mathbb Q\);
- preservation of its root set under \(p\mapsto-1/p\), \(p\mapsto(1-p)/(1+p)\), and \(p\mapsto(p+1)/(p-1)\), including the Klein-four composition law;
- \((2p-1-2/p)^2=-15\) modulo the defining polynomial and the corresponding fixed-field signs under all three involutions;
- the factorization over \(\mathbb Q(\sqrt{-15})\);
- the identities yielding square roots of \(5\) and \(-3\);
- \(q\mapsto-1/q\) under the relative involution;
- common scaling of all four coefficient groups in the displayed \(Q_{56}\) equation by \(1/(p^4q^4)\).

The computation proves identities in the source's parameter field; it does not enumerate all 56 line equations and therefore does not test minimal fields of individual lines or the full permutation action on labeled lines.
