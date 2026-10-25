---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Under each independent global refresh, a frozen arrow trajectory on Z walks monotonically until encountering its first reverse arrow, then alternates between that pair forever. The geometric clock therefore produces a zero atom 2az/(1+z) and positive/negative two-sided geometric tails with numerators q(1-q²z²), (1-q)(1-(1-q)²z²), and ratios qz, (1-q)z. Summing the tails yields one. Differentiating the resulting Laurent generating function M(w) gives E D, E D²; E T=1/p, E T²=(1+z)/p², E(TD)=E D/p+z (d/dz)E D. Renewal-reward law and CLT then yield v=p E D=b p K/[(1+z)H] and σ²=p E(D-vT)² equal to the stated rational expression; the original symbolic checker contains explicit factor equality. The derivative dv/dp=2abz(2-az³)/[(1+z)²H²] has sign b; at b=0 the displayed variance has negative z derivative. At b!=0 its expansion near z=0 is 4a+12ab²z²+O(z³), while p→0 gives zero, guaranteeing at least one interior maximum by continuity. Independently enumerated all frozen arrow assignments for t=1..5 and checked rational finite geometric mixture laws. Independently verified E D and full rational variance identity symbolically for q=2/3 with arbitrary z, confirming sigma^2 at z=2/5 as 916451688/1003003001. Full two-variable (q,z) symbolic elimination did not complete independently within the bounded check, so the universal rational reduction additionally rests on inspected algebraic source checker and analytic formulas. Analytic differentiation supports the all-parameter formula; no uniqueness of maximum or quenched CLT is asserted.

## originality

PASS

Martin–Nagel arXiv:2610.11919 (2026-10-08) gives the same global refresh framework, general renewal-reward LLN/CLT and biased near-full-refresh diffusivity effect; these are treated as PRIOR, not new. Its full text could not be accessed in current run, so a stronger explicit-block result inside its paper cannot be ruled out. Avena–den Hollander arXiv:1610.00641 treat deterministic cooling refresh intervals rather than iid geometric blocks. Compared arrow walk, reinforced two-cycle trap and global refresh renewal-reward representations; specialization of general formulas may produce coefficients if block moments are computed, but is not the same explicit law. General transport representation does not by itself list exact nonelliptic two-sided geometric block law or rational global p-profile; the inability to reread the entire most relevant manuscript is a nontrivial originality risk, not proof of noncoverage.

## value

PASS

This exact solvable deterministic nonelliptic edge case of a naturally regenerated environment supplies a complete block-displacement distribution and exact all-refresh-rate transport coefficients, showing global speed monotonicity contrasting interior diffusivity amplification for every nonzero bias. It goes beyond the literature’s general regeneration identities and local full-refresh expansion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
