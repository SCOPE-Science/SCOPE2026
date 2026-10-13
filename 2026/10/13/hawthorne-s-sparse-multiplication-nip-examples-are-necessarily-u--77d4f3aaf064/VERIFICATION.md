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

This is a source-backed structural deduction.

1. **NIP premises.** Hawthorne proves that \(\operatorname{Th}(\mathbb Z,+,d^{\mathbb N},\times\upharpoonright d^{\mathbb N})\) is NIP for every \(d\ge2\), and that \(\operatorname{Th}(\mathbb F_p[t],+,t^{\mathbb N},\times\upharpoonright t^{\mathbb N})\) is NIP for every prime \(p\ge7\).
2. **Exponent addition.** For \(a=d\) or \(a=t\), \(R(a^i,a^j,a^k)\) iff \(i+j=k\).
3. **Definable order.** On \(P=\{a^n:n\in\mathbb N\}\), define \(x\prec y\) iff \(x\ne y\) and \(\exists z\in P\,R(x,z,y)\). Then \(a^i\prec a^j\) iff \(i<j\).
4. **Order property.** The sequence \(a^0,a^1,\ldots\) witnesses the order property for \(\prec\). Therefore the complete theory is unstable.
5. **Conclusion.** Combining Steps 1 and 4 yields NIP but unstable in both families.

The full thesis pages containing Theorems 6.15 and 6.16 were visually inspected in addition to the arXiv and publisher metadata. No computational experiment is needed. No independent audit has been performed.
