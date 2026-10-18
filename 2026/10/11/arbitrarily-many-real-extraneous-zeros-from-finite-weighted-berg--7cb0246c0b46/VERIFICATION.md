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

The focal Lin--Xu--Yu arXiv:2609.36723v1 has a limiting kernel K_tau(x)=exp(-s0 x) P(x)+O(exp(-b x)), 0<s0<b, with nonzero real finite trigonometric P of nonzero distinct frequencies. Its Lemma 4.3 proves liminf P<0. Applied to -P it also proves limsup P>0, so alternating signs occur at arbitrarily large, finitely chosen x_0<...<x_N. Uniform convergence K_h(x,0)->K_tau(x) for all real x is Theorem 3.5 (NOT Theorem 4.6 as the source RESULT.md erroneously says). Lemma 5.2 yields convergence of finite truncation kernel values at each of the finitely many probes. A common sufficiently small h and large finite truncation M preserve signs and yield N distinct real zeros by continuity. The conformal multiplier J_alpha(x)J_alpha(0)>0 and the finite conjugation-invariant A excluding the real line preserve them under psi(x)=tanh(x/2). The polynomial product(z-a) for a in A belongs to I_A and is nonzero at each real kernel zero; hence these are extraneous. This proves each finite N, not one fixed finite A with infinitely many zeros. Repaired the erroneous theorem cross-reference in complete RESULT.md without changing the quantified mathematical statement.

## originality

PASS

The focal theorem explicitly transfers one negative sign to one finite extraneous zero; its stronger oscillatory machinery supports a finite arbitrary alternating pattern only after the additional sign-symmetric application and simultaneous two-limit transfer. The supplied N-unboundedness conclusion is not the same as the focal one-zero existence statement, nor was it found in checked canonical divisor / extremal function aliases. This is a short but independently precise strengthening; the existing lemmas make it readily derivable, and that limited novelty is disclosed.

## value

PASS

Extraneous zeros measure failure of a prescribed-zero Bergman extremal problem. An unbounded finite number for each weight alpha>1 rules out an interpretation of failure as isolated one-zero behavior. The exact N quantifier on natural kernels is mathematically motivated and could be used for multiplicity and instability questions; neither an effective cardinality cutoff nor simplicity is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
