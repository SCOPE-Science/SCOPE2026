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

For an ideal element with finite group support, ad_X acts diagonally on each g component with eigenvalue c(g), so polynomial Lagrange spectral projections isolate all finite c-level blocks within the ideal. Multiply each block by an appropriate u_h^(-1) to land in I cap C[X]. For F in this ideal, conjugating by a q with c(q)=a0 !=0 and subtracting F(X-a0)-F(X) decreases its degree with leading coefficient -n a0 b_n. Characteristic zero makes -n a0 invertible; induction forces all coefficients b_n to lie in J=I cap C, yielding I cap C[X]=J[X], hence I=AJ. The coset and polynomial grading gives AJ cap C=J; the same argument shows Z(A)=C. Centrality and faithful graded extension preserve ideal products; prime and maximal correspond. Char p G=Z,c(1)=1: shift fixes X^p-X and its principal two-sided ideal is proper, with zero intersection with k ker c=k[u_p,u_p^(-1)] (the kernel here is pZ). No finite computation substitutes for this all-G proof.

## originality

PASS

The directly relevant Ait Mohamed 2026 work concerns graded ideals and simplicity for a related Ore/skew action; the displayed theorem instead classifies all ordinary two-sided ideals of a non-simple translation action. Öinert-style ideal-intersection theorems provide nonzero intersection with commutants or center, not the exact generation/lattice equality. However Mihovski 2001 may contain a more general crossed-product invariant-ideal generation theorem; only its abstract was available, and comparison of its displayed invariant-subfield version does not decisively imply generation from k ker c. Best-of-knowledge PASS, with this material unresolved overlap risk explicitly retained.

## value

PASS

The exact ideal lattice, center, prime/maximal spectrum and product structure of this natural infinite skew group algebra are a structural classification, beyond the graded ideal theory in its motivating Ore paper. The sharp positive-characteristic counterexample identifies the precise mechanism of failure, providing an independently reusable algebraic criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
