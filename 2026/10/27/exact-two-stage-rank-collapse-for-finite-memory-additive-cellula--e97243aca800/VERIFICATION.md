---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Pass for the stated layered update, with the corrected literature attribution in repairs/5/RESULT.md and the scope stated explicitly in the replacement slogan. The physical field is F_p, while p^a is the spatial period. A unit vector is cyclic for the spatial shift, so setting z=S-1 identifies its module with F_p[z]/(z^L). The neighborhood sum is z^(p-1) by the polynomial geometric-sum identity in characteristic p, not division by a singular operator. Adding p-1 to exponents gives one chain of length q+1 (residue 0) and p-2 of length q; these lengths are positive for a>=1 and sum to L. On k copies of any one spatial chain of length ell, the last k-1 rows of the memory map shift layers and the first row is T0 on their sum. The companion identity M^k=T0(I+M+...+M^(k-1)) follows by iterating the recurrence on each layer; the operators commute, so raising it to ell proves nilpotence there. Its kernel consists exactly of last-layer vectors in the one-dimensional spatial kernel, hence the memory restriction is one Jordan block of dimension k ell. This also covers k=1 and leaves just one block when p=2. Summation of max(k ell-t,0) yields all image ranks, with matching formulas at kq and zero first at k(q+1). Kernel sizes p^(kL-rank) give the histogram and the last-step fraction follows from rank one at tau-1. The 17 stated finite exact-field cases were read in the frozen script and recorded output, not executed; the analytic chain/kernel argument establishes the unbounded result. The replacement does not equate the stated update with an additional-delay rule, or attribute a printed combined-case bound to Endo where the inspected text states separate bounds.

## originality

PASS

Pass for the exact spatial-and-memory Jordan partition and resulting complete rank/extinction profiles for the specified layered rule, not the rule family or the companion or spatial nilpotence methods themselves. Endo's paper supplies the model and the upper-bound mechanism, not the exact partition in the inspected sections. Distinct indexed automata do not cover this geometry and operator. The potentially broad Guan–He coverage remains unresolved at full-text level, not grounds to fail by itself.

## value

PASS

The sharp large-time behavior of a previously studied finite-memory rule is a motivated exact invariant. It specifies when the short directions stop contributing and leaves an exact terminal rank-one regime, supplying the entire distribution over layered initial states rather than just an upper bound. The structural chain lift explains those facts uniformly instead of enumerating a few ring sizes. The replacement confines these claims to the equal-weight prescribed neighborhood and explicit memory convention.

The dated certificate retains the supplied scientific assessment, sources and limitations.
