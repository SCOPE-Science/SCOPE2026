---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The normal-basis expansion converts B v^[2]=v into B^m u=u over F2 without requiring invertibility. With B=S+S^-1 the relevant cyclic module map is multiplication by X^-m P_m, whose kernel dimension is deg gcd(X^n-1,P_m). Since P_m=P_r^(2^s), P_r(0)=1 and P_r prime-derivative X^(r-1) for odd r, P_r is squarefree and its X-class has finite odd order o_r; multiplicity in X^n-1 yields saturation iff 2^s o_r divides n. Taking large multiples proves least period. Independent GF2 matrix-vs-gcd comparison covered 225 pairs, plus F4 direct enumeration for n=3..6. These finite checks are corroboration, not proof.

## originality

PASS

The normal-basis fixed-point mechanism and graph evolution-algebra definitions are established background. The specific nonperfect, characteristic-two, undirected two-neighbor cycle distribution, uniform 2^(2m) bound and exact least period are not implied by the checked general idempotent-equation or perfect-algebra results. Best-of-knowledge qualified originality remains subject to algebraic-dynamics equivalences.

## value

PASS

This is a complete two-parameter arithmetic census of a natural graph-defined algebra family and sharp periodic recurrence, not an arbitrary isolated calculation; the five-cycle resonance at extension degree three illustrates real arithmetic structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
