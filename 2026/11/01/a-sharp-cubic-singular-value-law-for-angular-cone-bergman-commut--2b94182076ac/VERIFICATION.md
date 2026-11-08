---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

PASS. The weighted-ball monomial norms give the exact orthonormal basis e_{k,l} and shift factor sqrt((k+1)/(k+l+alpha+3)). Angular mass |z1|²/(|z1|²+|z2|²) is Beta(k+1,l+1), yielding diagonal lambda_{k,l}=Pr(Bin(k+l+1,t)<=k). The binomial-tail difference is (1-t)BinMass(n+1,m), m=k+1, so [T,M_z1] is a weighted unilateral shift with pairwise orthogonal target vectors and exact singular weights. A local binomial CLT with m=(n+1)t+u sqrt n yields amplitude A=sqrt(1-t)/sqrt(2pi) times n^-1/2 e^-u²/[2t(1-t)], while log-concavity/Stirling gives global Gaussian domination. Counting the cells in r=eps² n, u gives (2/3)A³ integral e^{-3u²/(2sigma²)} du = sqrt(t)(1-t)²/(3 pi sqrt3); omission of n<delta eps^-2 and n>R eps^-2 is controlled by squared-mass sums and uniform sup bounds. Standard monotone inversion proves weak-Schatten and sorted s_j, and derivative of log coefficient proves t=1/5. Independently verified 462 exact small-n beta-binomial recursions and local n=3000 critical power sums for t=.2,.5,.8; inspected verify_spectrum.py, not treating such finite checks as the infinite proof. All parameters fixed in stated open ranges.

## originality

PASS

PASS with general jump-symbol theorem priority risk. Quiroga-Barranco–Sánchez-Nungaray (arXiv:2009.12448) and Quiroga-Barranco (arXiv:2106.01980) establish torus-invariant Toeplitz spectral decompositions, hence the diagonalization is known. Engliš–Guo–Zhang (arXiv:0707.2025) obtain boundary commutator weak-ideal/Dixmier-trace results for smooth functions, not this discontinuous cone characteristic symbol. The new stated fact is the complete exact beta-binomial commutator singular spectrum and explicit eps^-3 counting coefficient, including weight-independence and aperture optimization. Relevant sections of the above primary papers were inspected for implications; no governing jump-interface theorem with the same coefficient was found, though it may exist outside inspected literature.

## value

PASS

PASS. A characteristic function with a codimension-one angular jump is a natural borderline Toeplitz symbol for which smooth-symbol commutator results do not directly apply. The complete singular-value multiset and sharp weak-Schatten exponent/coefficient, independent of the radial Bergman weight, resolve a specific natural spectral invariant and identify a sharp cone angle. Exactness and the jump geometry—not generic reproducibility—motivate the result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
