---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The explicit group law on 27 elements and four generators yield distance shells (1,4,8,12,2) by independently enumerated BFS. All nine one-dimensional characters give the scalar sectors 4+8a+12b+2c (trivial), 1−4a+2c (4 copies), and −2+2a−3b+2c (4 copies), where a=2^p,b=3^p,c=4^p. The conjugate three-dimensional irreps yield three real eigenvalue branches 2a−c−2 and 1−a−c±sqrt(3)(1+a−2b), each multiplicity six, totaling 27. The controlling fourfold branch F=2c+2a−3b−2 increases through a unique zero p* in (2/3,7/10), from convexity in a=2^p; exact rational-power endpoint bounds keep all other branches strictly negative there. For smaller p the fractional-power Schoenberg strictness theorem applies; larger p has a positive centered F. Thus the endpoint nullity is four and squared-Euclidean rank 22 versus 26 below. Positive e^{-t d^p} for all t uses the CND equivalence, while t>log26 follows from strict diagonal dominance for every p. Independent BFS/27×27 eigenvalue checks at p=.5,p*,.8 corroborated; full intervals rely on the analytic factorization and bounds.

## originality

PASS

DeDeo–Martínez–Medrano–Minei–Stark–Terras (2003) uses the same four-generator Heisenberg Cayley graph and exact group Fourier representations, but computes adjacency spectra, not the nonlinear 1^p,2^p,3^p,4^p convolution spectrum. Sánchez and Murugan supply general negative-type/determinant or vertex-transitivity methods but no p*=0.677622... or fourfold endpoint degeneracy. Resultary Heisenberg matches concern three-tap convolution nullity and different group graphs. The exact finite metric invariant could have been calculated elsewhere; no absolute novelty claim is made.

## value

PASS

The smallest odd-characteristic finite Heisenberg Cayley graph is a canonical, natural noncommutative metric embedding test. Computing its exact powered negative-type threshold and four-dimensional abelian controlling kernel, despite 18 nonabelian regular dimensions, is a useful precise invariant for geometry and positive kernels; the statement is not an arbitrary subset or merely a decimal root.

The dated certificate retains the supplied scientific assessment, sources and limitations.
