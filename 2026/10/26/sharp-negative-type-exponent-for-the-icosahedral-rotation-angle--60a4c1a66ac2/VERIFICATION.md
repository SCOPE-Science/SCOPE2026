---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

PASS: Rotation classes of A5 have sizes 1,15,20,12,12 at angles 0, pi, 2pi/3, 2pi/5, 4pi/5; central Fourier diagonalization on irreps 1,3,3,4,5 reduces the 59-dimensional CND condition to four scalar character sums. Independent reconstruction gives S_3=-15+12phi(2/5)^s+12phi_prime(4/5)^s, S_3prime=-15+12phi_prime(2/5)^s+12phi(4/5)^s, S_4=20(2/3)^s-12[(2/5)^s+(4/5)^s], S_5=15-20(2/3)^s. The first three are strictly negative on (0,s*], while S_5=0 precisely at s*=log(4/3)/log(3/2) and positive above. The character multiplicities 9+9+16+25=59 prove rank 34 at equality; Schoenberg gives PSD for all t and Euclidean Gaussian strict PD for distinct points; a positive centered mode yields failure for sufficiently small t beyond cutoff. Explicit all-s inequalities hold separately; finite spectra corroborate, do not prove it.

## originality

PASS

Qualified best-of-knowledge statement-based originality after checking primary comparison and relevant published Resultary records; no uninspected full text asserted not covering. The new statement requires all four nontrivial A5 character sums and exact signs; none is a direct corollary of the compared general criteria without the substantive new finite-group calculation.

## value

PASS

PASS: The exact maximal negative-type power is a natural invariant of the intrinsic finite rotation-group metric, independent of scale; its exact cutoff and 25-dimensional representation-block degeneracy determine sharp Euclidean embedding dimension and all-damping kernel admissibility. It is not a mere repackaging of the generic Schoenberg criterion; the character-theoretic signs are specific and nontrivial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
