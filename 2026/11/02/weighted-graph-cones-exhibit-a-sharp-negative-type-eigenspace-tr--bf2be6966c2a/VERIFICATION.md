---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Anchor the putative Euclidean realization at the apex. With b=h^p and c=(2h)^p, its Gram matrix is bJ minus half of B=c(J-I)+(1-c)A, by polarization. Positive semidefiniteness is equivalent to an embedding and the Gram rank is the minimum affine dimension. On constants the eigenvalue is -[k+(N-1-k)c-2Nb]/2; on a nonconstant adjacency mode theta it is [c+(c-1)theta]/2. The least mode is theta=-s when c>1, and at c=1 all nonconstant modes are strictly positive. F(p,h) in the constant branch strictly increases with p, is negative at p=1, and diverges at every h in [1/2,1]. At a root the coefficient of h^p in k+h^p[(N-1-k)2^p-2N] is negative, so p0 strictly increases with h; p1 strictly decreases from infinity to at most 1. Solving c=s/(s-1) jointly with F=0 gives the stated crossing, and counting zero modes gives the rank drops, also when the base is disconnected. The tensor decomposition for Hamming adjacency verifies the stated least eigenvalue, multiplicity and limits. Independent exact check: for the disconnected base C4 disjoint union C4 the crossing has c=2, b=3/4 and Gram rank 5, certified by three explicit integer null vectors and a rank-5 reduction modulo 101 (node /workspace/independent_checks.js, section 4). This is a single finite check; the diagonalization proves the general result. The uploaded verifier was inspected, not executed.

## originality

PASS

The basic Schoenberg criterion and two-distance least-eigenvalue branch are not distinct contributions. The supported new claim is the explicit competition with the independent apex constraint across the whole continuous apex-weight interval, including the unique closed-form crossover and exact minimum dimensions on both sides and at coincidence for all admissible regular bases. A same-day weighted triangle barbell exhibits a similar two-obstruction pattern but varies one bridge, not all cone spokes, and does not cover this regular-base family. The exact previously inspected finite-metric criterion supplies a general implicit first singularity; it does not supply the two branches, their opposite monotonicity, or the explicit simultaneous rank defect. The evidence supports this distinction to the best of current knowledge, not historical priority.

## value

PASS

Negative type and minimal Euclidean snowflake dimension are natural invariants of weighted graph metrics. The result reduces a whole interval of weighted realizability and rank questions to a scalar branch switch determined by N,k,s,m, and locates the extra loss of dimension at equality. The Hamming family illustrates potentially large multiplicity losses rather than just a small exceptional case. These are usable structural and geometric conclusions beyond recomputing a fixed graph spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
