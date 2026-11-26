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

In the Hilbert–Schmidt orthonormal Weyl basis, each column of the orbit analysis operator is a distinct conjugation character of length N in observation space multiplied by a normalized Weyl coefficient. The coefficient magnitude is |A_g|/(N sqrt(N)), so the singular values are |A_g|/sqrt(N). The N−1 nonidentity diagonal Weyl coefficients vanish for a flat modulus. For nonzero shift and nontrivial character the two exceptional summands give (conj(z)−1)+(z−1)chi(a), of magnitude |z−1||z−conj(chi(a))|. Every nonidentity E-th root is realized by character restriction to an element of order E. For t=arg(z) in [0,pi], the interval [0,2pi/E] gives at most 4 sin²(pi/(2E)) using the first nonidentity root, for E>2. Beyond this interval the closest nonidentity root is within angle pi/E; hence the bound is 4 sin(t/2) sin(pi/(2E)). It peaks uniquely at pi when E is odd, and for even E it is strictly below the claimed optimum before pi−pi/E. After that midpoint, the root −1 gives the strictly decreasing bound 2 sin(t). For E=2 this same expression gives the unique optimizer pi/2 in the chosen half-circle. Equality is reached: the root 1, if also realized by a nontrivial character at a nonzero shift, does not lower the optimum; the scalar branch is at least N−4 for N≥8 and exceeds the minimum also at N=6,7. Thus no additional zeros remain, the largest unnormalized magnitude is N by Cauchy–Schwarz, and the claimed rank and ratio follow. The companion finite checker was inspected; its scan is ancillary to the analytic proof. This optimizes one-defect phases on the maximal visible subspace, not all flat-modulus windows.

## originality

PASS

The distinct theorem is the exact phase-constrained visible-space optimum and its phase classification for every finite abelian exponent. The cyclic rank component substantially overlaps prior work and the Weyl spectral identity is prior machinery. The retrieved full-rank amplitude-unconstrained impulse optima are different problems; even equality of some parameters would not transfer their optimizing values to this restricted, rank-deficient objective. No stronger statement covering the optimum was found in the material compared.

## value

PASS

Constant modulus imposes a fixed invisible diagonal space, so maximal rank alone leaves a meaningful stability question for what can be observed. The exact sharp ratio and equality phases solve that constrained design problem and show why groups of equal size but different exponents have different optima.

The dated certificate retains the supplied scientific assessment, sources and limitations.
