---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Checked full four-parameter domain, original map branch matrices, all cyclic words of length three; all-one-branch hyperbolic affine solutions cannot have prime 3. Independently formed the 3-step affine linear systems for LLR and LRR in SymPy and matched the stated coordinate numerators B,K,C,H and denominators D_L,D_R. Checked denominator-singular cases are inconsistent since positive B,H remain nonzero, and sign analysis K=(d+ℓ)(s-s*) provides no valid word below, exactly one common nonsmooth orbit at equality, both above. Independent exact matrix multiplication yields trace/determinant signs and the DR threshold factorization; for strict s>s*, DR<0 implies LRR unstable positive >1 with stable (0,1); LL R characteristic value at -1 negative implies multiplier below -1 and stable (0,1). No derivative at switching line asserted. All inequalities in proof use strict stated determinant/slope restrictions; finite rational checker not elevated to universal proof.

## originality

PASS

Direct original Ghosh–McLachlan–Simpson 2024 paper defines the same four-parameter border-collision normal form, but its original primary full text concentrates on chaotic-attractor components and renormalization, with special low periods, not this complete opposite-determinant primitive-three saddle census. Fatoyinbo–Simpson 2022 treats noninvertible border-collision period-three boundaries (a genuine near-overlap) but uses different parameter regimes and does not in the accessible summary establish both saddle cycles and the complete 0/1/2 count. Glendinning–Simpson period-three slices have same-sign positive determinants. Broader implicit formulas remain a priority risk.

## value

PASS

Sharp border-collision threshold simultaneously creates two non-attracting period-three saddles with opposing unstable signs; complete classification excludes unseen primitive-three attractors throughout a natural open four-parameter regime. This separates phase-space period existence from stable attractor dynamics and supplies exact bifurcation benchmarks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
