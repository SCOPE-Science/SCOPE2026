---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For a finite strict ordinal sum of nonempty antichains, nested diamonds ◇^k top detect exactly how many later levels are accessible; hence δ_i=◇^(h-i)⊤ ∧ ¬◇^(h-i+1)⊤ marks level i. Any r-input Boolean modal formula at a point is determined by (level i, local color c in q=2^r symbols, palette sets P_j for j>i), by structural induction on modal depth. Each such signature is definable with level/color predicates and ◇(δ_j ∧ χ_d), so every Boolean assignment to signatures yields one distinct term operation. Number of signatures E(q)=q sum_i product_{j>i} S_{n_j}(q), S_m(q)=sum_{k=1}^m C(q,k), giving 2^E. At q=1, E(1)=h. The normalized polynomial F=E/q factors F_h=1+S_{n_h}F_{h-1}, and derivative [q] S_m=1-1/2+...+(-1)^(m-1)/m separates all positive m (even partial sums increase, odd decrease). Exact recursive polynomial division recovers widths n_h through n_2, while n_1 is absent. Direct independent small q evaluations: (1,2,1) and (5,2,1) at q=2 have E=18, while (1,1,2) gives E=20; rational S-polynomial checks consistent. Finite numerical check is corroborative.

## originality

PASS

General finite Kripke bisimulation/type semantics and algebra generation are known; Goldblatt discusses transitive frames and modal complex algebra varieties but not this exact arity clone-size polynomial or inverse width theorem. Camerlo–Pistone–Rapallo study image/range and toric ideals of a single modal operator, not whole Boolean modal clone operations. Resultary weak-order poset endomorphism dimensions and homotopy class counts concern mathematically distinct functors, and no dominating exact term-spectrum theorem appeared in inspected research. The theorem uses ordinary strict accessibility, not reflexive preorder accessibility.

## value

PASS

The arity-by-arity term clone spectrum of a natural finite algebra class is a meaningful algebraic invariant. Proving it recovers the entire ordered later-width vector yet loses exactly the initial width supplies a precise reconstruction/non-identifiability boundary, with potential use in comparing finite modal algebras.

The dated certificate retains the supplied scientific assessment, sources and limitations.
