---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For H=M⊕N with M=Ce0 and N=ell2, K=P_M and U=I_M⊕B with B the backward unilateral shift, U is onto, commutes with K, leaves R(K)^perp invariant and is noninjective (ker U=C f1). The one-atom family Φ=(e0) is a Parseval K-frame: its coefficient square equals ||K*f||². UΦ=UP_MΦ=Φ; none of these singleton families permits removal, so all three deletion excesses equal zero. This directly contradicts the iff global-injectivity assertion of Corollary 5.11 despite satisfying its printed assumptions. For the corrected restricted statement, the relevant ordinary projected frame lies in M; on V=U|M the synthesis-kernel exact sequence of a surjective V gives dim ker(VT)=dim ker T+dim ker V, in finite-excess cases. The visible excess can detect only ker(U|M), never a kernel solely in M-perp. Critically, this argument does NOT assume the false unrestricted equality E_K(Φ)=E(P_MΦ) in general; it holds here because all atoms are in M. All steps are exact infinite-dimensional operator identities, not finite approximations.

## originality

PASS

Source-specific failure of the exact iff in Corollary 5.11 and the invisible-complement obstruction are not given by known ordinary-frame excess theory. The separate previously published SCOPE projection-counterexample attacks Theorem 5.9 instead and cannot subsume this supported-atom case. Qualified best-of-knowledge originality PASS for the concrete operator-theoretic correction; basic backward-shift facts and ordinary synthesis-kernel formula are not novel.

## value

PASS

Correcting a specific published iff whose claimed ambient injectivity is invisible to any range-supported K-frame is a genuine interpretive obstruction, despite the economical one-atom witness. The restricted synthesis-kernel exact sequence locates the precise algebraic fault; no stronger general classification is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
