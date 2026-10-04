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

The proof was checked directly at the level of definitions and implications.

1. For \(1<p<\infty\), the dual of \(\ell_p\) is \(\ell_{p^*}\), where \(p^*=p/(p-1)\). Hence the canonical basis \((e_k)\) is weakly \(r\)-summable for every finite \(r\ge p^*\), because every scalar evaluation sequence belongs to \(\ell_{p^*}\subseteq\ell_r\).
2. A normalized weakly null sequence in \(\ell_p\) has a subsequence equivalent to a block basic sequence of the canonical basis. Normalized disjoint block basic sequences in \(\ell_p\) are isometric to the canonical basis. Thus a weakly null maximizing sequence cannot be weakly \(r\)-singular when \(r\ge p^*\).
3. Therefore WMP for \((\ell_p,Y)\) implies \(\mathrm{SMP}_r\) for arbitrary \(Y\) and finite \(r\ge p^*\). Proposition 2.1(4) of arXiv:2609.03988v1 supplies the reverse implication.
4. Proposition 4.1(1) of the same source transfers \(\mathrm{SMP}_r\) to the \(r\)-convergent perturbation property.
5. Under isometric \(\ell_p\)-containment in \(Y\), the closed-subspace inheritance statements in Proposition 2.1(1) and Proposition 4.1(3), together with Theorem 2.2 and Examples 4.2(1), force failure of both properties for every \(r<p^*\).

No computation is used. No claim is made about \(r=\infty\), arbitrary codomains below \(p^*\), or merely isomorphic copies of \(\ell_p\) in the exact perturbation statement.
