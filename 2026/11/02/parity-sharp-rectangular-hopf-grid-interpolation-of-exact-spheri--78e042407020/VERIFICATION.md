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

An explicit Laplacian recurrence c_(a+1)=-c_a (m-a)(m-a+beta)/((a+1)(a+1+alpha)) constructs one harmonic for every angular weight (u,v) with |u|+|v|<=k and k-|u|-|v| even. These (k+1)^2 distinct torus characters span H_k(S³); their radial factors are nonzero rational polynomials Q(s) with Q(0)=1. Since s=e^-1 is transcendental, no radial coefficient vanishes for any weight or degree. The grid evaluation matrix is therefore diagonalized into discrete characters modulo (N,M), and its rank equals the exact number of residues of the weight diamond W_k. Along coordinate axes the step-2 weights -k,-k+2,...,k force each period T to be odd T>=k+1 or even T>2k. Conversely, congruent differences must respect |du|+|dv|<=2k and even total parity; the allowed periods prevent nonzero collisions in all mixed parity cases. Thus the necessary/sufficient rectangular-grid rule and optimal (k+1)^2 even, (k+2)^2 odd site counts follow for every degree, including k=0 and size-one grids. Independently exhaustively enumerated 4056 (k,N,M) combinations through k=12 to check the alias criterion. This is finite corroboration, not the transcendental universal proof.

## originality

PASS

Separated S^3 Hopf/Jacobi harmonics are established, and ordinary DFT aliasing is standard. The exact finite rectangular-grid necessary-and-sufficient condition for all exact degree-k harmonics, including parity sharpness and optimal site counts on a fixed nonresonant torus, was not found in inspected primary work. Qualified best-of-knowledge originality with general Nyquist-theorem and unindexed interpolation-literature risks.

## value

PASS

Determines the exact sampling threshold of a natural separated harmonic basis on a single torus, identifying parity-sensitive angular Nyquist aliasing and a sharp interpolation-vs-oversampling cost. The constraint to root-of-unity product grids and a nonresonant radius is mathematically motivated by Fourier separation and not a synthetic slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
