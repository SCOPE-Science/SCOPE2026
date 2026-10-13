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

The final claim was replayed directly from the definitions in arXiv:2610.01433v1.

1. **Domain and finiteness.** \(W=\{w\}\) and \(G(w)=\varnothing\). The closure is the constant map with value \(H=b^{-1}(1)\). This meets the source's finite-model definition because only \(W\) and the generators are required to be finite.
2. **Condition \(\mathsf G\).** At the valuation matching \(b\) on atoms, induction on formula complexity gives semantic truth exactly when \(b=1\). Any frame-valid formula is therefore in \(H\).
3. **Condition \(\mathsf K\).** If \(b(\varphi)=b(\varphi\to\psi)=1\), Boolean semantics gives \(b(\psi)=1\), so \(H\) is closed under modus ponens.
4. **Failure of \(\mathsf{KRep}\).** Flip one atom \(p\) to true in the model valuation. Then \(p\notin H\), while \(\neg p\in H\) is false at the only world. Hence the intersection of the truth sets of all formulas in \(H\) is empty, so the right side of the source's \(\mathsf{KRep}\) equivalence holds for \(p\) although the left side fails.
5. **Sharp world bound.** Closure frames have nonempty world sets, so one world is minimal.

No finite search, exhaustive enumeration, or external certificate is used. The proof does not establish any claim under an identity, monotone, extensive, or idempotent closure restriction.
