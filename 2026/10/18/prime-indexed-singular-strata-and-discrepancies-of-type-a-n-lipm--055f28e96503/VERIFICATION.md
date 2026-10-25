---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The definition is the INTERSECTION-NUMBER semigroup C_n Z^n∩Z_nonnegative^n over C, not the original dimension-two Du Val singularity. The A_n Cartan determinant N=n+1 and weighted congruence phi(a)=sum i*a_i (mod N) have equal index and C_n columns in kernel, hence lattice equals kernel and X_n=A^n/mu_N weights 1..N-1. Stabilizer of order d fixes indices divisible by d, codimension N−N/d>=2; no pseudoreflections, so Chevalley–Shephard–Todd reduces singular support to prime-order fixed-image Z_p, irreducible incomparable components of dimension N/p−1. Generic stabilizer mu_p yields transverse weights j repeated N/p for j=1..p−1. Toric character-lattice class group Z/N and canonical character weight nN/2 give index 1 for even n, 2 for odd. For group element of order d the exact fractional age is (N−N/d)/2; all >=1, >1 iff n>=4. For center EXACTLY at origin, interior cocharacter lift adds N/d−1 zero residues and reaches (N+N/d)/2−1, minimized at d=N -> n/2; identity class contributes n. Independent exact calculations confirmed age/interior/terminal statements for 3<=N<=54. Distinction between closed-cone age and strict interior mld is essential.

## originality

PASS

A uniform explicit specialization of the known toric quotient and discrepancy criteria to type-A_n Lipman semigroup; prior semigroup invariant-ring representation and general Ambro/reid-Tai theory are fully credited. The arithmetic full singular-component profile with primes p|n+1, generic slice, canonical index and torus-fixed mld n/2 was not stated together in the materially inspected seminal semigroup and toric sources. Best-of-knowledge only: earlier weighted-graph paper and general cyclic quotient catalogues may cover these explicit calculations.

## value

PASS

The coordinate-invariant toric family arising from all A_n root resolution graphs is natural, as are singular components, class groups, canonical index, terminality and closed-point mld. The theorem provides a uniform complete arithmetic singularity profile for every n>=2, with prime-divisor dependent component count/dimensions, generic quotient slices and exact strict-center discrepancy, instead of isolated table recomputations. It is a meaningful classification within a classical family even though general toric tools supply the abstract criteria.

The dated certificate retains the supplied scientific assessment, sources and limitations.
