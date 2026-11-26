---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The normalized monomial ratio cancels t and gives the transfer multiplier sqrt((alpha_i+1)alpha_j); its commutator with a diagonal is an injective weighted shift. On finite homogeneous blocks, every skew-Hermitian direction is a finite combination of these shifts and commuting number operators. Duhamel bounds each block by C_d L(b)||X||, so the logarithm near identity gives the required operator-norm bound uniformly in degree. Conversely norm continuity at the identity propagates to the whole orbit. Convolution with a smooth approximate identity gives smooth norm orbits, and torus averaging preserves smoothness (the group argument is conjugated by the torus element, with derivatives uniform over the compact torus). The torus has distinct monomial characters, so this expectation restores diagonality. A single matrix entry of a skew coordinate generator extracts the forward transfer without interference from the reverse transfer, uniformly in alpha. This establishes approximation by arrays of bounded weighted slope. Path summation and the bounded inf-convolution, with the same delta and Lipschitz constant on all degrees, give the two-way metric criterion. In d=2 the inequalities follow by integrating the angular derivative between adjacent sites, using k+s≥(k+1)s and m-k-s≥(m-k)(1-s). The first separation example comes from a globally Lipschitz phase in the square-root coordinates; in the middle of a degree-m block a displacement of floor(pi sqrt(m)) gives angular distance O(m^-1/2) and a coefficient ratio tending to -1. Degree parity is exactly invariant but fails square-root continuity across adjacent degrees. The inspected prior Toeplitz criterion establishes both membership inferences. There is no control across different homogeneous degrees, and the theorem does not cover off-diagonal operators.

## originality

PASS

The prior square-root compatibility criterion is for Toeplitz membership within the coordinate-torus class. The same source explicitly poses the full unitary problem and does not give this nontrivial metric for the full-group diagonal subclass. No earlier equivalent statement emerged in the checked literature and catalogue comparisons.

## value

PASS

This provides a usable, dimension-uniform-in-degree test for a natural full-group matrix subproblem and identifies the geometric scale of coordinate transfers. The two explicit opposing Toeplitz witnesses show why the angular condition is not just the known square-root condition rewritten.

The dated certificate retains the supplied scientific assessment, sources and limitations.
