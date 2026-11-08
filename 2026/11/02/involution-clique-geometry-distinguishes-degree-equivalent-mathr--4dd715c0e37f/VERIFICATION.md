---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Reduction of either SL2 length-two ring to SL2(F_q) has elementary abelian congruence kernel of order q³. In Witt characteristic four, Cayley–Hamilton for A²=I, detA=1 gives tr(A)A=2I and mod 2 forces reduction A=I, so every involution lies in abelian kernel. In the split ring write (X,h) with X traceless; h²=1 implies h=1 or a nonidentity transvection belonging to a unique root group U_L. Fixed X for that U_L is the 2-plane kI+kN_L, giving E_L=K_L×U_L, |E_L|=q³, |K∩E_L|=q², |E_L∩E_M|=q and q+2 maximal elementary abelian groups/cliques. The commuting relation reduces two non-K involutions to the same line, so every clique lies in one E_L or in K. Counting yields split involution spectrum c_I: q elements of size q⁴+q³−q², q³−q of size 2q³−q², and q⁴−q² of size q³, and ordered pair total q⁷+2q⁶−q⁵−q⁴. Independent brute-force ring-matrix multiplication and graph maximal-clique enumeration confirmed BOTH q=2 and q=4 split/Witt cases and all centralizer strata; universal proof remains algebraic.

## originality

PASS

Stasinski 2021 Theorem 5.3 already proves the equality of irreducible character-degree multiplicities for the two length-two rings, and Remark 6.3 already observes a nontrivial transvection has no Witt involutive lift. These facts cannot count as original. The new claim classifies all maximal elementary abelian subgroups (one in Witt, q+2 in split), their exact intersection pencil and the complete involution-commuting centralizer spectra, yielding a sharper representation-theoretic distinction. General 2-local subgroup literature may contain an equivalent classification, but no direct prior implication was identified in inspected sources.

## value

PASS

This complete projective-line classification of 2-local clique geometry separates two natural finite group families whose entire complex character-degree multiplicity distributions are identical. It strengthens a known single no-lift distinction into exact maximal-subgroup structure, intersection sizes, induced graph centralizer census and a Frobenius–Schur indicator-weighted sum obstruction, a motivated invariant rather than an arbitrary special example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
