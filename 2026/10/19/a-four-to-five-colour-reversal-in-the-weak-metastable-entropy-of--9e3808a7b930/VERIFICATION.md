---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For q=4 the cosine interaction is exactly the sum of two Ising interactions with coupling J/2. All single-component flips are available, and flipping both costs the sum, so weak blocking factors. Ising wall patterns are cyclic independent sets of even size; the two choices of initial spin cancel the factor 1/2 in the parity projection. The matrices at weights ±1 have the claimed eigenvalues. For q=5 each middle spin must maximize the projection on the sum of its neighbours: equal neighbours force their common spin, neighbouring colours permit either endpoint, and two-step neighbours force their short-arc midpoint. Thus in (0,+1,−1) coordinates only the two adjacent opposite nonzero increments are disallowed. Closure requires the increment sum to be zero mod 5, and the five initial spins cancel the character projection factor 1/5. The trace counts labelled cycles, not necklaces. No nontrivial twist attains the Perron radius: equality in the triangle inequality for a Perron-modulus eigenvector would force a common phase on all three self-loops, which is impossible. Both leading coefficients are one, giving the stated ratio. An independent spin-pair transfer with exact local scores in Z[sqrt(5)] was run for n=3..16 using /workspace/independent_checks/clock_local_scores.py; it gave the five reported small-n pairs and, for example, (4866436,1332585) at n=16. The finite run corroborates, rather than proves, the all-n formulas.

## originality

PASS

Credit the exact prior overlap for the Ising factor and the standard four-clock-to-two-Ising reduction; those are not original contributions. The supported distinct claim is the exact five-colour periodic weak-blocking enumeration with closure, and the resulting comparison to four colours. The checked sources cover neighbouring models, not this content.

## value

PASS

This is a concrete nonmonotonicity witness for the growth of the weakly blocked state space as clock resolution increases, on the same natural Hamiltonian and labelled ring. The finite periodic count identifies the winding restriction, and the exact unequal rates quantify the effect. The value is not the known Ising count or a claim about dynamical freezing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
